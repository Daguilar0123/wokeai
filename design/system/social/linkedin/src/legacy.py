"""Put the new pronunciation line into the legacy intro-card files, changing nothing else (October 21, 2026).

    node design/system/social/linkedin/src/render.mjs legacy-line     # fit the old line, draw the new one
    python3 -P design/system/social/linkedin/src/legacy.py LEGACY_DIR  # composite (LEGACY_DIR = $FRAMES_DIR/legacy)

Danny, October 21, 2026: "I like the • instead of the / from now on. Change everywhere, including the images."
The intro card came from Claude Design as pixels, so the line is swapped in place:

- marks/wokeai-brand-intro.gif (and its copy design/system/social/wokeai-brand-intro.gif): every one of
  the 140 frames keeps its own pixels, its own palette and its 50 ms timing, including the sink-and-regrow
  of the mark. Only the line's box (x 90..420, y 250..305, plain background apart from the line) is replaced.
- marks/og.png is the GIF's first frame, so it gets the same box.
- marks/png/wokeai-header-1500x500.png and marks/png/wokeai-youtube-banner-2048x1152.png were made from
  og.png with Pillow (Lanczos to 1000x500 at (250, 0), and to 846x423 at (601, 364), on surface); that
  derivation reproduces the old files exactly, and is re-applied to the new og.png.
Every step is checked: pixels outside the box must be identical to the originals.
"""
import json
import shutil
import sys
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
LEG = Path(sys.argv[1])
fit = json.loads((LEG / "fit.json").read_text(encoding="utf-8"))
x0, y0, x1, y1 = fit["box"]
tile = np.asarray(Image.open(LEG / "new-line.png").convert("RGB"), dtype=np.uint8)
assert tile.shape == (y1 - y0, x1 - x0, 3)
surface = tuple(int(fit["background"][i:i + 2], 16) for i in (1, 3, 5))

GIF = ROOT / "marks/wokeai-brand-intro.gif"
GIF_COPY = ROOT / "design/system/social/wokeai-brand-intro.gif"
OG = ROOT / "marks/og.png"
HEADER = ROOT / "marks/png/wokeai-header-1500x500.png"
YT = ROOT / "marks/png/wokeai-youtube-banner-2048x1152.png"
assert GIF.read_bytes() == GIF_COPY.read_bytes(), "the two intro GIFs differ; stop"


def outside(a, b):
    m = np.ones(a.shape[:2], bool)
    m[y0:y1, x0:x1] = False
    return np.array_equal(a[m], b[m])


def derive(card, size, offset, canvas):
    out = Image.new("RGB", canvas, surface)
    out.paste(card.resize(size, Image.LANCZOS), offset)
    return out


# --- check that the old derivations reproduce the old files before trusting them
old_og = Image.open(OG).convert("RGB")
for path, size, off, canvas in [(HEADER, (1000, 500), (250, 0), (1500, 500)), (YT, (846, 423), (601, 364), (2048, 1152))]:
    again = np.asarray(derive(old_og, size, off, canvas))
    assert np.array_equal(again, np.asarray(Image.open(path).convert("RGB"))), f"{path.name}: derivation does not reproduce"

# --- the GIF, frame by frame
g = Image.open(GIF)
info = {"loop": g.info.get("loop", 0)}
frames, durations, disposals = [], [], []
for i in range(g.n_frames):
    g.seek(i)
    frames.append(np.asarray(g.convert("RGB"), dtype=np.uint8).copy())
    durations.append(g.info["duration"])
    disposals.append(getattr(g, "disposal_method", 0))
first_old = frames[0].copy()
assert np.array_equal(first_old, np.asarray(old_og)), "og.png is no longer the GIF's first frame; stop"

out_frames = []
for f in frames:
    new = f.copy()
    new[y0:y1, x0:x1] = tile
    flat = new.reshape(-1, 3)
    mask_out = np.ones(new.shape[:2], bool); mask_out[y0:y1, x0:x1] = False
    keep = np.unique(new[mask_out].reshape(-1, 3), axis=0)          # colors outside the box: kept exactly
    if len(keep) > 256:
        raise SystemExit(f"a frame has {len(keep)} colors outside the box; cannot keep it exact")
    box_colors, counts = np.unique(tile.reshape(-1, 3), axis=0, return_counts=True)
    extra = [c for c in box_colors[np.argsort(-counts)] if not (keep == c).all(axis=1).any()]
    pal = np.concatenate([keep, np.array(extra[:256 - len(keep)], dtype=keep.dtype).reshape(-1, 3)])
    uniq, inv = np.unique(flat, axis=0, return_inverse=True)
    d = ((uniq[:, None, :].astype(np.int32) - pal[None, :, :].astype(np.int32)) ** 2).sum(axis=2)
    idx = d.argmin(axis=1).astype(np.uint8)[inv.reshape(-1)]
    im = Image.fromarray(idx.reshape(new.shape[:2]), mode="P")
    im.putpalette(pal.astype(np.uint8).flatten().tolist() + [0] * (768 - 3 * len(pal)))
    out_frames.append((im, new))

tmp_gif = LEG / "wokeai-brand-intro.gif"
out_frames[0][0].save(tmp_gif, save_all=True, append_images=[im for im, _ in out_frames[1:]],
                      duration=durations, loop=info["loop"], optimize=False, disposal=1)

# verify the written GIF on the original's 50 ms timeline (Pillow merges identical consecutive frames
# into one longer frame): every slot shows the original frame outside the box, and the new line inside it
assert set(durations) == {50}, "the original GIF no longer has uniform 50 ms frames; stop"
chk = Image.open(tmp_gif)
slots = []
for i in range(chk.n_frames):
    chk.seek(i)
    d = chk.info["duration"]
    assert d % 50 == 0, d
    slots += [np.asarray(chk.convert("RGB"), dtype=np.uint8)] * (d // 50)
assert len(slots) == len(frames), (len(slots), len(frames))
worst_box = 0
for i, a in enumerate(slots):
    assert outside(a, frames[i]), f"slot {i}: pixels outside the line box changed"
    worst_box = max(worst_box, int(np.abs(a[y0:y1, x0:x1].astype(int) - tile.astype(int)).max()))
print(f"GIF: {len(slots)} slots of 50 ms ({chk.n_frames} stored frames), outside the box identical to the original; "
      f"worst box pixel off by {worst_box}")

# --- og.png = the new first frame
new_og = Image.fromarray(out_frames[0][1])
assert outside(np.asarray(new_og), np.asarray(old_og))
assert np.array_equal(np.asarray(new_og)[y0:y1, x0:x1], tile)

# --- write everything
shutil.copyfile(tmp_gif, GIF)
shutil.copyfile(tmp_gif, GIF_COPY)
new_og.save(OG, optimize=True)
derive(new_og, (1000, 500), (250, 0), (1500, 500)).save(HEADER, optimize=True)
derive(new_og, (846, 423), (601, 364), (2048, 1152)).save(YT, optimize=True)
for p in (GIF, GIF_COPY, OG, HEADER, YT):
    print(f"wrote {p.relative_to(ROOT)} ({p.stat().st_size:,} bytes)")
