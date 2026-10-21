// wokeai LinkedIn renderer (October 21, 2026). Zero npm dependencies: Node 24, Google Chrome, ffmpeg.
//
//   node design/system/social/linkedin/src/render.mjs [stills|motion|all|<job name>...]
//
// Serves the repo on 127.0.0.1, drives headless Chrome over the DevTools protocol, waits for
// compose.html's window.__ready (font, motion, clear-space and safe-box checks), and captures PNGs.
// Motion jobs seek the animated mark's own SMIL clock frame by frame; ffmpeg encodes the MP4 and
// gif.py (Pillow, exact token palette) the GIF.
// Frames go to $FRAMES_DIR (default: a temp folder) and are never committed.

import http from 'node:http';
import fs from 'node:fs';
import fsp from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { spawn, spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.resolve(HERE, '..');
const ROOT = path.resolve(HERE, '../../../../..');
const FRAMES = process.env.FRAMES_DIR || fs.mkdtempSync(path.join(os.tmpdir(), 'wokeai-frames-'));
const CHROME = process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const TOKENS = JSON.parse(fs.readFileSync(path.join(ROOT, 'design/system/tokens.json'), 'utf8'));
const color = (name, palette) => TOKENS.color.tokens.find((t) => t.name === name).value[palette];

// ---- jobs ----
const still = (slot, w, h, theme) => ({ kind: 'still', slot, layout: slot, w, h, theme,
  file: `wokeai-linkedin-${slot}-${w}x${h}-${theme}.png` });
const JOBS = [
  ...['light', 'dark'].flatMap((t) => [
    still('feed', 1200, 627, t),
    still('square', 1080, 1080, t),
    still('portrait', 1080, 1350, t),
    still('profile-banner', 1584, 396, t),
    still('company-cover', 1128, 191, t),
    still('company-cover', 1512, 256, t),
  ]),
  still('square-accent', 1080, 1080, 'accent'),
  ...['light', 'dark'].flatMap((t) => [
    { kind: 'motion', slot: 'motion-square', layout: 'square', w: 1080, h: 1080, theme: t,
      mp4: `wokeai-linkedin-motion-square-1080x1080-${t}.mp4`, gif: `wokeai-linkedin-motion-square-1080x1080-${t}.gif` },
    // H.264 4:2:0 needs even sizes: the 627-high composition is padded 1px with surface for the MP4
    { kind: 'motion', slot: 'motion-feed', layout: 'feed', w: 1200, h: 627, theme: t, padTo: 628,
      mp4: `wokeai-linkedin-motion-feed-1200x628-${t}.mp4`, gif: `wokeai-linkedin-motion-feed-1200x627-${t}.gif` },
  ]),
];
JOBS.forEach((j) => { j.name = j.file ? j.file.replace(/\.png$/, '') : j.mp4.replace(/\.mp4$/, '').replace('-1200x628', '-1200x627'); });

// ---- static server ----
const TYPES = { '.html': 'text/html; charset=utf-8', '.svg': 'image/svg+xml', '.json': 'application/json',
  '.js': 'text/javascript', '.mjs': 'text/javascript', '.png': 'image/png', '.css': 'text/css' };
function serve() {
  const srv = http.createServer(async (req, res) => {
    const p = path.normalize(decodeURIComponent(new URL(req.url, 'http://x').pathname));
    const f = path.join(ROOT, p);
    if (!f.startsWith(ROOT + path.sep)) { res.writeHead(403).end(); return; }
    try {
      const body = await fsp.readFile(f);
      res.writeHead(200, { 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream', 'Cache-Control': 'no-store' });
      res.end(body);
    } catch { res.writeHead(404).end(); }
  });
  return new Promise((r) => srv.listen(0, '127.0.0.1', () => r(srv)));
}

// ---- Chrome over CDP ----
async function launchChrome() {
  const profile = fs.mkdtempSync(path.join(os.tmpdir(), 'wokeai-chrome-'));
  const proc = spawn(CHROME, ['--headless=new', '--remote-debugging-port=0', `--user-data-dir=${profile}`,
    '--hide-scrollbars', '--force-color-profile=srgb', '--force-device-scale-factor=1', '--no-first-run',
    '--no-default-browser-check', '--disable-renderer-backgrounding', '--disable-background-timer-throttling',
    '--disable-backgrounding-occluded-windows', '--mute-audio', 'about:blank'], { stdio: 'ignore' });
  const portFile = path.join(profile, 'DevToolsActivePort');
  for (let i = 0; i < 200 && !fs.existsSync(portFile); i++) await new Promise((r) => setTimeout(r, 50));
  const [port, wsPath] = fs.readFileSync(portFile, 'utf8').trim().split('\n');
  const ws = new WebSocket(`ws://127.0.0.1:${port}${wsPath}`);
  await new Promise((r, j) => { ws.onopen = r; ws.onerror = j; });
  let id = 0; const pending = new Map(); const listeners = [];
  ws.onmessage = (ev) => {
    const msg = JSON.parse(ev.data);
    if (msg.id && pending.has(msg.id)) {
      const { res, rej } = pending.get(msg.id); pending.delete(msg.id);
      msg.error ? rej(new Error(msg.error.message)) : res(msg.result);
    } else if (msg.method) listeners.forEach((l) => l(msg));
  };
  const send = (method, params = {}, sessionId) => new Promise((res, rej) => {
    const i = ++id; pending.set(i, { res, rej }); ws.send(JSON.stringify({ id: i, method, params, sessionId }));
  });
  const once = (method, sessionId) => new Promise((r) => {
    const l = (m) => { if (m.method === method && m.sessionId === sessionId) { listeners.splice(listeners.indexOf(l), 1); r(m.params); } };
    listeners.push(l);
  });
  const close = async () => {
    try { ws.close(); } catch {}
    const exited = new Promise((r) => proc.once('exit', r));
    proc.kill(); await exited;
    try { fs.rmSync(profile, { recursive: true, force: true, maxRetries: 5, retryDelay: 100 }); } catch {}
  };
  return { send, once, close };
}

async function openPage(cdp, base, job, mode) {
  const { targetId } = await cdp.send('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await cdp.send('Target.attachToTarget', { targetId, flatten: true });
  const s = (m, p) => cdp.send(m, p, sessionId);
  await s('Page.enable');
  await s('Emulation.setDeviceMetricsOverride', { width: job.w, height: job.h, deviceScaleFactor: 1, mobile: false });
  await s('Emulation.setEmulatedMedia', { features: [
    { name: 'prefers-reduced-motion', value: 'no-preference' },
    { name: 'prefers-color-scheme', value: job.theme === 'dark' ? 'dark' : 'light' }] });
  const loaded = cdp.once('Page.loadEventFired', sessionId);
  const q = new URLSearchParams({ layout: job.layout, theme: job.theme, w: job.w, h: job.h, mode });
  await s('Page.navigate', { url: `${base}/design/system/social/linkedin/src/compose.html?${q}` });
  await loaded;
  const ev = async (expr) => {
    const r = await s('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true });
    if (r.exceptionDetails) throw new Error(`${job.name}: ${r.exceptionDetails.exception?.description || r.exceptionDetails.text}`);
    return r.result.value;
  };
  const report = await ev('window.__ready');
  const shot = async (file) => {
    const { data } = await s('Page.captureScreenshot', { format: 'png', fromSurface: true,
      clip: { x: 0, y: 0, width: job.w, height: job.h, scale: 1 } });
    await fsp.writeFile(file, Buffer.from(data, 'base64'));
  };
  const close = () => cdp.send('Target.closeTarget', { targetId });
  return { ev, shot, report, close };
}

function ff(args) {
  const r = spawnSync('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', ...args], { stdio: 'inherit' });
  if (r.status !== 0) throw new Error('ffmpeg failed: ' + args.join(' '));
}

async function renderMotion(cdp, base, job) {
  const pg = await openPage(cdp, base, job, 'motion');
  const sets = [
    { fps: 30, cycle: 210, hold: 30, dir: path.join(FRAMES, job.name, 'mp4') },  // 7.0s + 1s hold
    { fps: 20, cycle: 140, hold: 20, dir: path.join(FRAMES, job.name, 'gif') },  // 5cs per frame, exact
  ];
  for (const set of sets) {
    await fsp.rm(set.dir, { recursive: true, force: true }); await fsp.mkdir(set.dir, { recursive: true });
    for (let f = 0; f < set.cycle + set.hold; f++) {
      const t = f < set.cycle ? f / set.fps : 7.0;
      await pg.ev(`__seek(${t})`);
      await pg.shot(path.join(set.dir, String(f).padStart(4, '0') + '.png'));
    }
  }
  // self-test: the light moves, and 7.0s returns to the 0s state exactly
  const a = await fsp.readFile(path.join(sets[0].dir, '0000.png'));
  const b = await fsp.readFile(path.join(sets[0].dir, '0030.png'));
  const c = await fsp.readFile(path.join(sets[0].dir, '0239.png'));
  if (a.equals(b)) throw new Error(`${job.name}: frame at 1.0s equals 0s; the SMIL clock did not move`);
  if (!a.equals(c)) throw new Error(`${job.name}: frame at 7.0s differs from 0s`);
  await pg.close();

  const bg = color('surface', job.theme === 'dark' ? 'dark' : 'light').replace('#', '0x');
  const toYuv = 'scale=in_range=full:out_range=tv:out_color_matrix=bt709:flags=accurate_rnd+full_chroma_int,format=yuv420p';
  const vf = (job.padTo ? `pad=${job.w}:${job.padTo}:0:0:color=${bg},` : '') + toYuv;
  ff(['-framerate', '30', '-i', path.join(sets[0].dir, '%04d.png'), '-vf', vf, '-c:v', 'libx264', '-profile:v', 'high',
    '-preset', 'slow', '-crf', '16', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
    '-color_range', 'tv', '-movflags', '+faststart', '-an', path.join(OUT, job.mp4)]);
  // GIF through Pillow with a fixed palette that holds every token color exactly (see gif.py)
  const g = spawnSync('python3', ['-P', path.join(HERE, 'gif.py'), sets[1].dir, path.join(OUT, job.gif),
    job.theme === 'dark' ? 'dark' : 'light'], { stdio: 'inherit' });
  if (g.status !== 0) throw new Error('gif.py failed for ' + job.gif);
  return { ...pg.report, files: [job.mp4, job.gif], frames: path.join(FRAMES, job.name) };
}

// legacy-line: fit the old pronunciation line in marks/og.png and draw the new one (see legacy-line.html);
// writes fit.json, old-line.png and new-line.png to $FRAMES_DIR/legacy for legacy.py
const LEGACY = { src: '/marks/og.png', box: '90,250,420,305',
  old: '(pronounced wohk/ē/eye).', new: '(pronounced wōk•ē•ī).' };  // Danny, October 21, 2026
async function legacyLine() {
  const srv = await serve(); const base = `http://127.0.0.1:${srv.address().port}`;
  const cdp = await launchChrome();
  try {
    const { targetId } = await cdp.send('Target.createTarget', { url: 'about:blank' });
    const { sessionId } = await cdp.send('Target.attachToTarget', { targetId, flatten: true });
    const s = (m, p) => cdp.send(m, p, sessionId);
    await s('Page.enable');
    const loaded = cdp.once('Page.loadEventFired', sessionId);
    await s('Page.navigate', { url: `${base}/design/system/social/linkedin/src/legacy-line.html?${new URLSearchParams(LEGACY)}` });
    await loaded;
    const r = await s('Runtime.evaluate', { expression: 'window.__result', awaitPromise: true, returnByValue: true });
    if (r.exceptionDetails) throw new Error('legacy-line: ' + (r.exceptionDetails.exception?.description || r.exceptionDetails.text));
    const { oldURL, newURL, ...fit } = r.result.value;
    const dir = path.join(FRAMES, 'legacy'); await fsp.mkdir(dir, { recursive: true });
    await fsp.writeFile(path.join(dir, 'old-line.png'), Buffer.from(oldURL.split(',')[1], 'base64'));
    await fsp.writeFile(path.join(dir, 'new-line.png'), Buffer.from(newURL.split(',')[1], 'base64'));
    await fsp.writeFile(path.join(dir, 'fit.json'), JSON.stringify({ ...fit, old: LEGACY.old, new: LEGACY.new }, null, 2));
    console.log('legacy-line fit', JSON.stringify(fit), '->', dir);
  } finally { await cdp.close(); srv.close(); }
}

async function main() {
  const want = process.argv.slice(2);
  if (want[0] === 'legacy-line') return legacyLine();
  const jobs = JOBS.filter((j) => !want.length || want.includes('all') || want.includes(j.kind === 'still' ? 'stills' : 'motion') || want.includes(j.name));
  if (!jobs.length) throw new Error('no jobs match ' + want.join(' '));
  const srv = await serve(); const base = `http://127.0.0.1:${srv.address().port}`;
  const cdp = await launchChrome();
  const reports = [];
  try {
    for (const job of jobs) {
      if (job.kind === 'still') {
        const pg = await openPage(cdp, base, job, 'still');
        await pg.shot(path.join(OUT, job.file));
        reports.push({ ...pg.report, files: [job.file] });
        await pg.close();
      } else {
        reports.push(await renderMotion(cdp, base, job));
      }
      const r = reports.at(-1);
      console.log(`ok ${job.name}  k=${r.k} mark=${r.markPx}px clear>=${r.clearPx}px measured=${JSON.stringify(r.clearMeasured)}`);
    }
  } finally { await cdp.close(); srv.close(); }
  const reportFile = path.join(FRAMES, 'report.json');
  let all = {}; try { all = JSON.parse(fs.readFileSync(reportFile, 'utf8')); } catch {}
  for (const r of reports) for (const f of r.files) all[f] = r;
  fs.writeFileSync(reportFile, JSON.stringify(all, null, 2));
  console.log('report:', reportFile);
}

main().catch((e) => { console.error(e.message); process.exit(1); });
