"""Check the wokeai LinkedIn files and build 50%-scale contact sheets (October 21, 2026).

    python3 -P design/system/social/linkedin/src/check.py [SHEETS_DIR]

Checks every wokeai-linkedin-* file in the folder above this script against its name
(slot, size, theme) and design/system/tokens.json:
  PNG  exact size, fully opaque, all four corner pixels equal to the background token
  MP4  h264 yuv420p, 30 fps, 8.0 s, 240 frames; frame 0 decoded back within 2 of the background
  GIF  exact size, 8.0 s on a 50 ms grid, loops forever, frame 0 corners equal to the background
Then writes contact sheets (light, dark, accent) at 50% width, with video frames at 1.0 s and
2.0 s and the LinkedIn crop zones outlined on the banners, to SHEETS_DIR (default: a temp
folder), and prints a markdown table of files for the README. Exits 1 on any failure.
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
OUT = HERE.parent
ROOT = HERE.parents[4]
SHEETS = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(tempfile.mkdtemp(prefix="wokeai-sheets-"))
SHEETS.mkdir(parents=True, exist_ok=True)
TOKENS = json.loads((ROOT / "design/system/tokens.json").read_text(encoding="utf-8"))
NAME = re.compile(r"^wokeai-linkedin-(?P<slot>[a-z-]+?)-(?P<w>\d+)x(?P<h>\d+)-(?P<theme>light|dark|accent)\.(?P<ext>png|mp4|gif)$")


def hexrgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def token(name, palette):
    return hexrgb(next(t for t in TOKENS["color"]["tokens"] if t["name"] == name)["value"][palette])


def background(theme):
    return token("accent", "light") if theme == "accent" else token("surface", theme)


def corners(img):
    w, h = img.size
    return [img.getpixel(p) for p in ((0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1))]


def video_frame(path, t, w, h):
    raw = subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", str(t), "-i", str(path), "-frames:v", "1",
         "-vf", "scale=in_color_matrix=bt709:in_range=tv:flags=accurate_rnd+full_chroma_int,format=rgb24",
         "-f", "rawvideo", "-"], capture_output=True, check=True).stdout
    return Image.frombytes("RGB", (w, h), raw)


failures, rows, sheet_items = [], [], {"light": [], "dark": [], "accent": []}


def fail(f, msg):
    failures.append(f"{f}: {msg}")


files = sorted(p for p in OUT.iterdir() if p.name.startswith("wokeai-linkedin-"))
for p in files:
    m = NAME.match(p.name)
    if not m:
        fail(p.name, "name does not follow wokeai-linkedin-<slot>-<w>x<h>-<theme>.<ext>")
        continue
    w, h, theme, ext, slot = int(m["w"]), int(m["h"]), m["theme"], m["ext"], m["slot"]
    bg = background(theme)
    if ext == "png":
        img = Image.open(p)
        if img.size != (w, h):
            fail(p.name, f"size {img.size}")
        rgba = img.convert("RGBA")
        if rgba.getextrema()[3][0] != 255:
            fail(p.name, "not fully opaque")
        if any(c[:3] != bg for c in corners(rgba)):
            fail(p.name, f"corner {corners(rgba)[0][:3]} != background {bg}")
        sheet_items[theme].append((p.name, rgba.convert("RGB"), slot, (w, h)))
    elif ext == "mp4":
        info = json.loads(subprocess.run(
            ["ffprobe", "-v", "error", "-count_frames", "-show_streams", "-show_format", "-of", "json", str(p)],
            capture_output=True, check=True, text=True).stdout)
        v = next(s for s in info["streams"] if s["codec_type"] == "video")
        dur = float(info["format"]["duration"])
        checks = {"codec": v["codec_name"] == "h264", "pix_fmt": v["pix_fmt"] == "yuv420p",
                  "fps": v["avg_frame_rate"] == "30/1", "frames": v.get("nb_read_frames") == "240",
                  "size": (v["width"], v["height"]) == (w, h), "duration": abs(dur - 8.0) < 0.05 and dur < 15,
                  "audio": all(s["codec_type"] == "video" for s in info["streams"])}
        for k, ok in checks.items():
            if not ok:
                fail(p.name, f"{k} check failed ({v['codec_name']} {v['pix_fmt']} {v['avg_frame_rate']} {v.get('nb_read_frames')} {dur:.2f}s)")
        f0 = video_frame(p, 0, w, h)
        if any(max(abs(a - b) for a, b in zip(c, bg)) > 2 for c in corners(f0)):
            fail(p.name, f"decoded corner {corners(f0)[0]} not within 2 of {bg}")
        for t in (1.0, 2.0):
            sheet_items[theme].append((f"{p.name} @ {t:.1f}s", video_frame(p, t, w, h), slot, (w, h)))
    elif ext == "gif":
        img = Image.open(p)
        if img.size != (w, h):
            fail(p.name, f"size {img.size}")
        if img.info.get("loop") != 0:
            fail(p.name, "does not loop forever")
        durations = []
        for i in range(img.n_frames):
            img.seek(i)
            durations.append(img.info.get("duration"))
        # identical frames in the hold are merged into one longer frame; the timing must still be 8.0 s on a 50 ms grid
        if sum(durations) != 8000 or any(d % 50 for d in durations) or min(durations) != 50:
            fail(p.name, f"{img.n_frames} frames, total {sum(durations)} ms, durations {sorted(set(durations))}")
        img.seek(0)
        if any(c != bg for c in corners(img.convert("RGB"))):
            fail(p.name, f"frame 0 corners {corners(img.convert('RGB'))} != {bg}")
    rows.append((p.name, f"{w}×{h}", p.stat().st_size))

# contact sheets at 50% width, crop zones outlined on the banner copies only
for theme, items in sheet_items.items():
    if not items:
        continue
    tiles = []
    for label, img, slot, (w, h) in items:
        t = img.resize((w // 2, h // 2), Image.LANCZOS)
        d = ImageDraw.Draw(t)
        if slot == "profile-banner":
            d.rectangle((0, 198 // 2, 360 // 2, 396 // 2), outline=(220, 40, 40), width=2)    # desktop photo, approx.
            d.line((192 // 2, 0, 192 // 2, h // 2), fill=(40, 90, 220), width=2)               # mobile side crop
            d.line((1392 // 2, 0, 1392 // 2, h // 2), fill=(40, 90, 220), width=2)
        if slot == "company-cover":
            s = w / 1128 / 2
            d.rectangle((0, int(95 * s), int(180 * s), h // 2), outline=(220, 40, 40), width=2)  # page logo, approx.
        tiles.append((label, t))
    pad, label_h, max_w = 16, 22, 1800
    rows_layout, row, x = [], [], pad
    for label, t in tiles:
        if row and x + t.width + pad > max_w:
            rows_layout.append(row)
            row, x = [], pad
        row.append((label, t))
        x += t.width + pad
    rows_layout.append(row)
    H = pad + sum(max(t.height for _, t in r) + label_h + pad for r in rows_layout)
    sheet = Image.new("RGB", (max_w, H), (128, 128, 128))
    d = ImageDraw.Draw(sheet)
    y = pad
    for r in rows_layout:
        x = pad
        for label, t in r:
            d.text((x, y), label, fill=(255, 255, 255))
            sheet.paste(t, (x, y + label_h))
            x += t.width + pad
        y += max(t.height for _, t in r) + label_h + pad
    out = SHEETS / f"contact-sheet-{theme}.png"
    sheet.save(out)
    print("sheet:", out)

print()
print("| file | pixels | bytes |")
print("| --- | --- | --- |")
for name, px, size in rows:
    print(f"| `{name}` | {px} | {size:,} |")
print()
if failures:
    print("FAILURES:")
    for f in failures:
        print(" -", f)
    sys.exit(1)
print(f"all {len(rows)} files pass")
