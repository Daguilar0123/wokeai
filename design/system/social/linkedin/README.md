# wokeai LinkedIn graphics

Made October 21, 2026, for Danny to post himself. Nothing here has been posted.

Every file is rendered from the marks in `marks/`, used unchanged, and from `design/system/tokens.json`, the only source of color and type. The stills use `roots-official-light.svg` or `-dark.svg`. The motion uses `roots-animated-light.svg` or `-dark.svg`, with its own SMIL light timeline (October 20, 2026). The accent square uses `roots-blueprint.svg` in `surface`. The wordmark is Archivo at weight 750. The lockups keep the brand book's proportions (mark 72, gap 18, wordmark 44, caption 16; stacked: mark 64, gap 12, name 28), scaled by one factor per layout.

## Files

| file | pixels | bytes | text | slot |
| --- | --- | --- | --- | --- |
| `wokeai-linkedin-feed-1200x627-dark.png` | 1200×627 | 41,602 | wokeai + line 1 | image post or link preview, 1.91:1 |
| `wokeai-linkedin-feed-1200x627-light.png` | 1200×627 | 41,590 | wokeai + line 1 | image post or link preview, 1.91:1 |
| `wokeai-linkedin-square-1080x1080-dark.png` | 1080×1080 | 51,549 | wokeai + line 1 | image post, 1:1 |
| `wokeai-linkedin-square-1080x1080-light.png` | 1080×1080 | 51,277 | wokeai + line 1 | image post, 1:1 |
| `wokeai-linkedin-square-accent-1080x1080-accent.png` | 1080×1080 | 49,299 | wokeai + line 1 | image post, 1:1, accent variant |
| `wokeai-linkedin-portrait-1080x1350-dark.png` | 1080×1350 | 67,359 | wokeai + line 2 | image post, 4:5 |
| `wokeai-linkedin-portrait-1080x1350-light.png` | 1080×1350 | 66,986 | wokeai + line 2 | image post, 4:5 |
| `wokeai-linkedin-profile-banner-1584x396-dark.png` | 1584×396 | 31,371 | wokeai + line 1 | personal profile background photo |
| `wokeai-linkedin-profile-banner-1584x396-light.png` | 1584×396 | 31,203 | wokeai + line 1 | personal profile background photo |
| `wokeai-linkedin-company-cover-1128x191-dark.png` | 1128×191 | 11,250 | wokeai only | Company Page cover |
| `wokeai-linkedin-company-cover-1512x256-dark.png` | 1512×256 | 15,500 | wokeai only | Company Page cover |
| `wokeai-linkedin-company-cover-1128x191-light.png` | 1128×191 | 11,231 | wokeai only | Company Page cover |
| `wokeai-linkedin-company-cover-1512x256-light.png` | 1512×256 | 15,383 | wokeai only | Company Page cover |
| `wokeai-linkedin-motion-feed-1200x627-dark.gif` | 1200×627 | 456,492 | wokeai + line 1 | other platforms (GIF) |
| `wokeai-linkedin-motion-feed-1200x628-dark.mp4` | 1200×628 | 94,295 | wokeai + line 1 | native video post |
| `wokeai-linkedin-motion-feed-1200x627-light.gif` | 1200×627 | 468,588 | wokeai + line 1 | other platforms (GIF) |
| `wokeai-linkedin-motion-feed-1200x628-light.mp4` | 1200×628 | 96,284 | wokeai + line 1 | native video post |
| `wokeai-linkedin-motion-square-1080x1080-dark.gif` | 1080×1080 | 1,002,821 | wokeai + line 1 | other platforms (GIF) |
| `wokeai-linkedin-motion-square-1080x1080-dark.mp4` | 1080×1080 | 144,301 | wokeai + line 1 | native video post |
| `wokeai-linkedin-motion-square-1080x1080-light.gif` | 1080×1080 | 1,043,317 | wokeai + line 1 | other platforms (GIF) |
| `wokeai-linkedin-motion-square-1080x1080-light.mp4` | 1080×1080 | 146,073 | wokeai + line 1 | native video post |

## Text used

Only these lines appear, verbatim, and the pronunciation line at most once per file:

- **Line 1**, `pronounced wohk/ē/eye`: feed, square, square-accent, profile banner, and both motion pieces. "pronounced" is set in `muted` and "wohk/ē/eye" in `ink`, as on the site; on the accent square both are `accent-ink`.
- **Line 2**, `A grassroots, open-source community for people using their own AI to push back against systemic oppression.`: the portrait, in the `lede` style.
- **No line**: the company cover, mark and wordmark only.

Lines 3 to 5 from the brief are not used yet. Each image carries one line.

## Where each goes on LinkedIn

- **feed (1200×627)**: an image post or a link preview, 1.91:1.
- **square (1080×1080)** and **square-accent**: an image post, 1:1.
- **portrait (1080×1350)**: an image post, 4:5. It takes the most room in the mobile feed.
- **profile-banner (1584×396)**: the background photo on Danny's personal profile.
- **company-cover**: the cover image on the wokeai Company Page. Upload 1512×256 first; if LinkedIn refuses it, use 1128×191.
- **motion MP4s**: a native video post. LinkedIn shows GIFs in image posts as still images, so the animation reaches LinkedIn only as video. Each clip is one full 7.0-second loop of the mark plus a 1-second hold, 8 seconds, H.264 at 30 fps, no sound.
- **motion GIFs**: the same animation for other platforms, at 20 fps so every frame lasts exactly 50 ms.

## Decisions (Danny, October 21, 2026, unless noted)

- **Only variant A of the pronunciation line.** The B spelling for the A/B test is not settled. B files will be a text change only, once Danny chooses the spelling.
- **The profile banner keeps its content inside the safe center.** Everything sits between x 420 and 1392 and above y 264. That keeps it clear of the desktop profile photo, which covers about the first 360px of the bottom half, and of the photo's lower position on mobile. It also stays inside the 1200px center that phones keep. The brief asked for the mark in the left third, which conflicts with that clear zone; Danny chose the safe center. The crop zones are approximate, taken from design guides rather than LinkedIn's own help pages.
- **The company cover comes in two sizes.** Guides report that LinkedIn raised the minimum to 1512×256 in mid-2026; this could not be confirmed on LinkedIn's help pages. Both sizes have the same 5.9:1 shape and layout.
- **No secondary wordmark** (decided in the plan, October 21, 2026). The live site now says wōke•ĀĪ is what wokeai does *not* sound like, so the mark shown bare on a graphic would read as the pronunciation.
- **The 1200×627 video is 1200×628.** H.264 at 4:2:0 needs even dimensions, so the composition is rendered at 627 and padded with one row of `surface` at the bottom. The GIF keeps 1200×627.
- **The motion is still for most of each clip.** The light in `roots-animated-*.svg` runs from 0.10 to 3.25 seconds of its 7-second loop, so most of each clip is the still mark. The brief asked for one full cycle plus a hold, and that is what was made.

## Regenerate

```bash
node design/system/social/linkedin/src/render.mjs all
```

```bash
python3 -P design/system/social/linkedin/src/check.py
```

The first command needs Google Chrome, ffmpeg and a network connection, for Archivo from Google Fonts. `src/compose.html` is the one composition page. It refuses to render if any of these checks fails:

- Archivo's variable weight range did not load;
- reduced motion is on;
- the clear space is below one eighth of the ground line;
- anything falls outside the layout's safe box;
- the text differs from the approved lines.

`src/render.mjs` captures the PNGs and frames and encodes the MP4s and GIFs. It also tests that the light moves and that each loop returns to its first frame. `src/check.py` checks sizes, opacity, background colors against the tokens, the video format and the GIF timing. It also writes 50% contact sheets with the crop zones outlined.

## Not done

- Variant B of the pronunciation line, waiting on the spelling.
- Adobe tools were not used. The connector is not authorized, and nothing here needed them.
- The LinkedIn crop zones and the company cover size come from design guides, not from LinkedIn. Check the profile banner and the cover once after uploading.
