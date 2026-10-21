"""Encode a frame folder as a looping GIF with exact token colors (October 21, 2026).

    python3 -P gif.py FRAMES_DIR OUT.gif light|dark

ffmpeg's palettegen averages colors into its palette, which moved the background one or two
levels off the token. Here the palette starts with every color token of the theme, exactly,
and the remaining entries come from a median cut of the frames where the light is moving.
Frames are mapped to the nearest palette color with no dithering, so flat areas stay exact and
the glow does not flicker. Every frame is 50 ms (20 fps); Pillow merges identical frames in the
hold into one longer frame, which keeps the total at 8.0 s.
"""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image

frames_dir, out, palette_name = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
root = Path(__file__).resolve().parents[5]
tokens = json.loads((root / "design/system/tokens.json").read_text(encoding="utf-8"))
exact = []
for t in tokens["color"]["tokens"]:
    h = t["value"][palette_name].lstrip("#")
    rgb = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    if rgb not in exact:
        exact.append(rgb)

paths = sorted(frames_dir.glob("*.png"))
frames = [Image.open(p).convert("RGB") for p in paths]
w, h = frames[0].size

# median cut over the moving part of the loop (0.0 to 3.5 s at 20 fps), every fifth frame
sample_idx = list(range(0, min(70, len(frames)), 5))
strip = Image.new("RGB", (w, h * len(sample_idx)))
for n, i in enumerate(sample_idx):
    strip.paste(frames[i], (0, h * n))
cut = strip.quantize(colors=256 - len(exact), method=Image.Quantize.MEDIANCUT).convert("RGB")
extra = [c for _, c in sorted(cut.getcolors(256), reverse=True) if c not in exact]
colors = (exact + extra)[:256]

flat_palette = [v for c in colors for v in c] + [0] * (768 - 3 * len(colors))
pal_arr = np.array(colors, dtype=np.int32)


def to_indexed(frame):
    # exact nearest-color mapping (Pillow's own lookup is approximate and moved the background):
    # map each distinct color once, then scatter the indices back
    px = np.asarray(frame, dtype=np.int32).reshape(-1, 3)
    uniq, inverse = np.unique(px, axis=0, return_inverse=True)
    d = ((uniq[:, None, :] - pal_arr[None, :, :]) ** 2).sum(axis=2)
    idx = d.argmin(axis=1).astype(np.uint8)[inverse.reshape(-1)]
    img = Image.fromarray(idx.reshape(frame.size[1], frame.size[0]), mode="P")
    img.putpalette(flat_palette)
    return img


indexed = [to_indexed(f) for f in frames]
indexed[0].save(out, save_all=True, append_images=indexed[1:], duration=50, loop=0, optimize=False, disposal=1)
print(f"{out.name}: {len(frames)} frames, {len(colors)} colors ({len(exact)} exact tokens)")
