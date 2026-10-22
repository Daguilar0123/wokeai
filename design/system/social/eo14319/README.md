# wokeai: Executive Order 14319 graphics

Made October 22, 2026 at Danny's word: "i also want to clarify that i do want the executive order stuff on the website, as well as i would like some socials made up for it." These are drafts. Nothing is posted.

The copy for each platform, with its alt text and character counts, is in `design/social-copy.md` under "Executive Order 14319". It is taken word for word from the home page's "What it answers" section, so post and page agree.

## Files

| file | pixels | bytes | slot |
| --- | --- | --- | --- |
| `wokeai-eo14319-feed-1200x627-light.png` | 1200×627 | 44,131 | LinkedIn, Bluesky and Facebook image post, 1.91:1 |
| `wokeai-eo14319-feed-1200x627-dark.png` | 1200×627 | 44,269 | X and dark-mode feeds |
| `wokeai-eo14319-square-1080x1080-light.png` | 1080×1080 | 57,091 | Instagram, Threads and Facebook, 1:1 |
| `wokeai-eo14319-square-1080x1080-dark.png` | 1080×1080 | 57,456 | dark-mode feeds, 1:1 |
| `wokeai-eo14319-motion-square-1080x1080-light.mp4` | 1080×1080 | 121,436 | LinkedIn native video, Instagram reel |
| `wokeai-eo14319-motion-square-1080x1080-dark.mp4` | 1080×1080 | 121,340 | the same, dark |
| `wokeai-eo14319-motion-square-1080x1080-light.gif` | 1080×1080 | 612,887 | platforms that play GIFs |
| `wokeai-eo14319-motion-square-1080x1080-dark.gif` | 1080×1080 | 591,774 | the same, dark |

Every file carries the same text and nothing else: the wordmark "wokeai", then these two lines, one under the other.

- `Executive Order 14319, July 23, 2025`, in `muted`
- `wokeai answers it. wokeainow.com`, in `ink`

There is no pronunciation line, no seal, flag, eagle or likeness of any official, and nothing laid out like a government document. It is the brand's own lockup on `surface`.

## Making them

The marks are `roots-official-light.svg` and `-dark.svg` for the stills, and `roots-animated-light.svg` and `-dark.svg` for motion, used unchanged. Colors and type come from `design/system/tokens.json`. They are built with the LinkedIn pipeline in `design/system/social/linkedin/src/`, which has two layouts for this set, `eo-square` and `eo-feed`.

- **Square:** the stacked lockup (mark 64, gap 12, name 28) scaled to fit inside 64px margins.
- **Feed:** the horizontal lockup (mark 72, gap 18, name 44).
- **The two lines:** both in the caption style, under the wordmark.
- **Motion:** one full 7.0-second loop of the mark's light plus a 1-second hold, so 8 seconds, under the 10-second limit. The MP4s are H.264 at 30 fps with no sound. The GIFs run at 20 fps with an exact token palette. The two lines stay still while the light runs down the roots and back up to the grass.

```bash
node design/system/social/linkedin/src/render.mjs eo14319
```

```bash
python3 -P design/system/social/linkedin/src/check.py --set eo14319 --report "$FRAMES_DIR/report.json"
```

```bash
python3 -P design/system/social/eo14319/count_copy.py
```

The first command renders the set. It refuses to render if Archivo or any glyph is missing, if the clear space falls below one eighth of the ground line, if anything leaves the safe box, or if the text differs from the two lines.

The second command checks sizes, opacity, background tokens, the video format and the GIF timing. With `--report`, it also checks that every file's rendered text is the allowed text for this set. All 8 files pass.

The third command checks the copy against each platform's limit and the rules in `design/social-copy.md`. All five blocks pass.

## Alt text

- **Feed, light:** The wokeai logo on a light background: three clumps of grass above a brown ground line, with roots below that branch into a network ending in round nodes. To its right, the wordmark “wokeai” and two lines of text: “Executive Order 14319, July 23, 2025” and “wokeai answers it. wokeainow.com”
- **Feed, dark:** the same, "on a dark background", without "brown".
- **Square, light:** the same as the feed, with "Below it" for "To its right".
- **Square, dark:** the same as the light square, "on a dark background".
- **Motion, light or dark:** An 8-second animation of the wokeai logo on a light (or dark) background: three clumps of grass above a ground line, with roots below that branch into a network ending in round nodes. A green light runs from the grass tips down through the roots to every node and back up to the grass, then the logo holds still. Below it, the wordmark “wokeai” and two lines of text: “Executive Order 14319, July 23, 2025” and “wokeai answers it. wokeainow.com”
