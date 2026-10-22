// EO 14319 capture receiver (October 22, 2026). Zero npm dependencies: Node 24.
//
//   node design/system/social/eo14319-announcement-style/capture-server.mjs
//
// Serves the repo read-only on 127.0.0.1:4319 so the built-in browser can open
// eo14319-announcement.html with the marks beside it, and takes the PNG that page draws of
// itself (?save=1) as POST /save/<name>. Only the two approved filenames are written, and
// only into this folder.

import http from 'node:http';
import fsp from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, '../../../..');
const PORT = Number(process.env.PORT || 4319);
const SAVES = new Set(['eo14319-announcement-1080x1080.png', 'eo14319-announcement-1200x627.png']);
const MAX_BYTES = 8 * 1024 * 1024;
const TYPES = { '.html': 'text/html; charset=utf-8', '.svg': 'image/svg+xml', '.json': 'application/json',
  '.js': 'text/javascript', '.mjs': 'text/javascript', '.png': 'image/png', '.css': 'text/css' };

const srv = http.createServer(async (req, res) => {
  const url = new URL(req.url, 'http://x');
  if (req.method === 'POST') {
    const name = url.pathname.replace(/^\/save\//, '');
    if (!url.pathname.startsWith('/save/') || !SAVES.has(name)) { res.writeHead(403).end('name not allowed'); return; }
    const chunks = []; let size = 0;
    for await (const c of req) { size += c.length; if (size > MAX_BYTES) { res.writeHead(413).end(); return; } chunks.push(c); }
    const body = Buffer.concat(chunks);
    if (!body.subarray(0, 8).equals(Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]))) {
      res.writeHead(400).end('not a PNG'); return;
    }
    await fsp.writeFile(path.join(HERE, name), body);
    console.log(`saved ${name} ${body.length} bytes`);
    res.writeHead(200, { 'Content-Type': 'text/plain' }).end(String(body.length));
    return;
  }
  const p = path.normalize(decodeURIComponent(url.pathname));
  const f = path.join(ROOT, p);
  if (!f.startsWith(ROOT + path.sep)) { res.writeHead(403).end(); return; }
  try {
    const body = await fsp.readFile(f);
    res.writeHead(200, { 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream', 'Cache-Control': 'no-store' });
    res.end(body);
  } catch { res.writeHead(404).end(); }
});
srv.listen(PORT, '127.0.0.1', () => console.log(`eo14319 capture receiver on http://127.0.0.1:${PORT}/`));
