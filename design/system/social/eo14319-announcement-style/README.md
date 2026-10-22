# EO 14319 graphic, in the announcement page's style

Made October 22, 2026, for Danny to post himself. Nothing here has been posted.

This is one still about Executive Order 14319, "Preventing Woke AI in the Federal Government" (July 23, 2025), in two sizes. The header and body take their type, color and spacing from the White House page where the order was announced:
https://www.whitehouse.gov/presidential-actions/2025/07/preventing-woke-ai-in-the-federal-government/

A band at the bottom, in wokeai's own colors and type, says plainly that the image is commentary and not a government document.

## Files

| file | pixels | bytes | what |
| --- | --- | --- | --- |
| `eo14319-announcement-1080x1080.png` | 1080×1080 | 215,798 | the graphic, square |
| `eo14319-announcement-1200x627.png` | 1200×627 | 155,198 | the same design, 1.91:1 feed or link-preview size |
| `eo14319-announcement.html` | — | 14,318 | the composition both PNGs are drawn from |
| `eo14319-style.json` | — | 4,584 | the page's type, color and spacing tokens, with the dated note on how they were read |
| `capture-server.mjs` | — | 2,479 | the local receiver that serves the page and writes the PNGs |
| `README.md` | — | (this file) | |

## Text used

Only these lines appear, verbatim:

- **Eyebrow**: `Executive Order 14319 · July 23, 2025`. It is set uppercase, in the page's label style.
- **Title**: `Preventing Woke AI in the Federal Government`. It is set uppercase, in the page's headline style.
- **Three phrases**, one line each, each under 60 characters, in the page's body style:
  - `Tells federal agencies which AI models they may buy` (51 characters). This is Sec. 3: agencies are to "procure only those LLMs developed in accordance with" two principles.
  - `Requires “Truth-seeking” and “Ideological Neutrality”` (53). These are the two "Unbiased AI Principles" Sec. 3 names, in the page's own capitalization.
  - `Lists “systemic racism” in what it says DEI includes` (52). Sec. 1 says that "In the AI context, DEI includes… incorporation of concepts like critical race theory, transgenderism, unconscious bias, intersectionality, and systemic racism."
- **Band**: `wokeai`, `wokeainow.com`, and `Commentary from wokeai, not a government document.`

The composition refuses to save if any of this text changes, if a phrase wraps or reaches 60 characters, or if the quoted words are not exactly `Truth-seeking`, `Ideological Neutrality` and `systemic racism`.

## Alt text

**`eo14319-announcement-1080x1080.png`**:
A square graphic. A navy band at the top reads "Executive Order 14319 · July 23, 2025" above the title "Preventing Woke AI in the Federal Government" in tall capitals. On white below are three lines: "Tells federal agencies which AI models they may buy," "Requires 'Truth-seeking' and 'Ideological Neutrality'," and "Lists 'systemic racism' in what it says DEI includes." A cream band at the bottom shows the wokeai roots mark, the name wokeai, wokeainow.com, and the words "Commentary from wokeai, not a government document."

**`eo14319-announcement-1200x627.png`**:
A wide graphic with the same content as the square version. A navy band at the top reads "Executive Order 14319 · July 23, 2025" above the title "Preventing Woke AI in the Federal Government." On white below are three lines: "Tells federal agencies which AI models they may buy," "Requires 'Truth-seeking' and 'Ideological Neutrality'," and "Lists 'systemic racism' in what it says DEI includes." A cream band at the bottom shows the wokeai roots mark, the name wokeai, wokeainow.com, and the words "Commentary from wokeai, not a government document."

## Fonts

| where | font | source | substitution |
| --- | --- | --- | --- |
| title | Instrument Serif 400 | Google Fonts (OFL) | none, the page's own font |
| eyebrow | Instrument Sans 600 | Google Fonts (OFL) | none, the page's own font |
| phrases | Instrument Sans 400 | Google Fonts (OFL) | none, the page's own font |
| band | Archivo 400 and 750 | Google Fonts (OFL), from `design/system/tokens.json` | none, wokeai's own font |

The page uses one more font, **Nord**, but only for its "EXECUTIVE ORDER 14319" line. Nord is not on Google Fonts (the css2 request answered 400 on October 22, 2026) and is not a system font. The graphic has no element in that style, so nothing was substituted for it.

The page self-hosts static Instrument Sans cuts. The graphic loads the Google Fonts variable version at the same weights.

## Sizes as rendered

| | eyebrow | title | phrases | wordmark | url and note | band | mark |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1080×1080 | 24px | 86px | 36px | 50px | 25px | 196px | 150px |
| 1200×627 | 20px | 58px | 28px | 36px | 22px | 128px | 92px |

The title and phrase sizes are fitted by the page itself. The title takes the largest size that balances onto two lines, as on the page. The phrases take the largest size at which the longest one stays on one line. Other values are scaled from the page's ratios:

- title line-height 1.08 and tracking 0.0218em;
- eyebrow tracking 0.06em and padding 0.35em;
- eyebrow-to-title gap 0.29× the title size;
- body line-height 1.6 and tracking 0.01165em.

The square uses the page's paragraph gap of 1.5em. The wide version tightens it to 1.05em to fit its height.

## What was taken from the page, and what was not

**Taken (type, color, spacing only):**

- the header's navy gradient (`#0b1b33` to `#0d132d`) and its white text;
- the headline, label and body type styles;
- the body's white background and `#293340` text;
- the spacing ratios.

**Not taken:**

- the seal at the top of the page's header;
- the arrow icon beside the page's eyebrow;
- any emblem, flag, eagle, photograph, likeness or logo.

The only image in the graphic is wokeai's own mark.

**The band is wokeai's, not the page's:**

- `surface #f6f4ef`, a 2px `rule #d9d5cc` line on top, `ink #141414`, and `accent #1f6f4a` for the address;
- Archivo, with the wordmark at weight 750 and -0.03em tracking (all from `design/system/tokens.json`, light theme);
- `marks/roots-official-light.svg`, used byte for byte. The page fetches the file, checks its SHA-256 against `065db6c431d11ab8a61038b4821e4b51ac0f7984d3586c656d39207a898ac8ce`, and draws that exact file. It is never redrawn, recolored or traced.

## Decisions (October 22, 2026)

- **Title in capitals.** On the page, the headline's source text is itself in capitals. The graphic keeps the title as given and sets it uppercase with CSS, so it reads like the page.
- **The page's capitalization for the quote.** The brief wrote the second principle as "Ideological neutrality". The page's section heading reads "Ideological Neutrality", so the graphic quotes "Ideological Neutrality".
- **Phrases reworded from the brief's examples.** The examples were "Tells federal agencies which AI they may buy" and "Lists systemic racism among the ideas it bars." The order speaks of LLMs, so the first phrase says "AI models." The order does not literally bar an idea; it lists systemic racism among concepts it says DEI includes, so the third phrase says that.
- **One version, light band.** The band uses wokeai's light theme and the light mark on its cream surface. The cream, the rule line and the different typeface set it apart from the page's white body. No dark version was made.
- **Captured inside the built-in browser (Danny chose this).** The built-in browser cannot save a 1× screenshot to disk. So the page draws its own stage onto a canvas at scale 1 and posts the PNG to `capture-server.mjs`:
  - the same Google Fonts files are inlined into an SVG `foreignObject`;
  - the mark's exact bytes are inlined as a data URI.

  This is a re-render by the same browser engine, not a literal screenshot. Both PNGs were opened and checked by eye, at full size and at 50%. All text is legible at 50%.

## Regenerate

Start the receiver (it serves the repo on 127.0.0.1:4319):

```bash
node design/system/social/eo14319-announcement-style/capture-server.mjs
```

Then, in a browser, open each URL below with the viewport at the same size, and wait for the tab title to read `saved …`:

- `http://127.0.0.1:4319/design/system/social/eo14319-announcement-style/eo14319-announcement.html?size=1080x1080&save=1`
- `http://127.0.0.1:4319/design/system/social/eo14319-announcement-style/eo14319-announcement.html?size=1200x627&save=1`

Leave off `&save=1` to preview. A tab title that starts `failed:` names the check that stopped the save. The full report is printed below the stage. The fonts come from Google Fonts, so this needs a network connection.
