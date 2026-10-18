# wokeai

One lowercase word. Pronounced *wohk/ē/eye*.

wokeai is a grassroots, open-source community for people using their own AI to push back against systemic oppression, and building the tools to do it in the open. It is not an AI product. It is a website (wokeainow.com), social profiles, a list of tools that already exist, and the people who want to build the next ones. Three pillars: open source, liberation, community. It answers a 2025 U.S. executive order that uses "woke AI" as an insult, and it takes the word back.

This system was built on October 18, 2026 from the project's own repository: the two marks, the static site's stylesheet, and the README that dates every brand decision. Values are exact copies, not approximations. Danny Aguilar owns the decisions recorded here.

## Content fundamentals

### The name

- **wokeai**, one word, always lowercase, even at the start of a sentence. Never *Wokeai*, never *woke AI* when you mean the brand, never *wokeainow* (that is only the domain).
- **The pronunciation line** sits under the wordmark wherever the wordmark is large enough to carry a second line: `pronounced wohk/ē/eye`. The spelling says one thing to a glance; the line tells you how it is actually said. This gap is the brand's one joke and its whole posture: subversive, not hiding, proud. State it once per surface, then never wink again.
- **The secondary wordmark** is `wōke•ĀĪ` (lowercase *wōke*, interpunct, uppercase *ĀĪ* with macrons). It is the pronunciation line turned into type, meant to look like a dictionary entry. Use it on social headers, merch, and the podcast lockup. Set it in the same face as the main wordmark; the face must have real macron glyphs.
- **The podcast** (future) is **wahkeeye**, tagline `pronounced wōke•ĀĪ`, with the Heard mark. The brand is never written *wahkeeye*; only the show is.

### Voice

Plain, direct, warm. Pride without volume. Short sentences. Name things by what people recognize. No slogans borrowed from anyone; no quotation of historical figures in brand copy. Avoid: "by any means necessary," any phrasing that implies violence, any wording that claims a movement's or a thinker's endorsement.

### What the brand does not show

No eye, no rays, no fist, no chains, no torch, no lightbulb, no face or likeness of any person, no X-shaped mark. The earlier placeholder was an open eye with rays; it was replaced because it read as surveillance, and the whole point is the watched being heard. These are rules, not preferences.

## Visual foundations

### Marks

Two marks, both one color, both drawn with `currentColor` in source so they take the ink of their surface, both safe inside a circle crop. The asset store holds explicit-ink copies for places that cannot inherit color (see Marks under Assets).

**Roots (the wokeai mark).** Grass above a ground line; below it, the roots are a git graph: one main branch straight down, 35% longer than its branches; one branch down-right from the top node; one down-left from the 60% mark of the main branch; every branch ends in a node; no merge. It means grass roots, literally, and open-source forking, literally: what sustains the thing is underneath and shared. Keep the geometry. Stroke 26 and nodes r=26 on a 512 grid; everything sits inside r=200 of center so the circle crop never clips.

**Heard (the podcast mark).** Three arcs of sound arriving at a listening dot. The arcs' center of curvature is outside the circle, so they bulge toward the listener; this is deliberately not the Wi‑Fi construction, where arcs are centered on the dot. Nothing is emitted; something is heard.

Rules for both: minimum 24px on screen beside text, 32px alone; clear space equal to the mark's ground-line length ÷ 8 on every side; never recolor with more than one ink; never add a drop shadow or outline; never put either mark on the accent unless the mark is set in `surface`.

Favicon: the Roots mark at 16px needs its own cut (grass reduced to one blade, nodes enlarged). Not yet drawn; until then the full mark is used and reads as a sprout.

### Color

A warm paper and a near-black ink, one accent green (roots, growth), and a brown only the cover and illustrations use. Both themes are designed, not inverted. Every pair below meets 4.5:1 for body text.

| token | use |
| --- | --- |
| `surface` | page background |
| `card` | cards and raised panels |
| `rule` | hairlines, card borders |
| `ink` | text and the marks on `surface` and `card` |
| `muted` | secondary text, captions, the pronunciation line |
| `accent` | links, primary buttons, the one emphasis per screen |
| `accent-ink` | text on `accent` |
| `earth` | cover blocks and illustration only, never text |

One accent per screen. Semantic states (success, warning, error) are not defined yet; add them as tokens before adding them to a screen.

### Type

One family, **Archivo** (Google Fonts), for wordmark, headings, body, and labels. It is a sturdy grotesk with the Latin Extended glyphs the secondary wordmark needs (Ā, Ī, ō) and a real interpunct. Check those three glyphs render before shipping any surface that uses `wōke•ĀĪ`; if they fall back, the face is wrong.

| style | size / leading / weight | use |
| --- | --- | --- |
| `wordmark` | 44px / 1 / 750, tracking −0.03em | the name, lowercase |
| `heading` | 28px / 1.2 / 700 | section titles |
| `lede` | 21px / 1.4 / 400 | the one opening paragraph |
| `body` | 17px / 1.55 / 400 | running text, 680px measure |
| `label` | 13px / 1.3 / 600, uppercase, tracking .09em, `muted` | section eyebrows |
| `caption` | 16px / 1.4 / 400, `muted` | the pronunciation line, notes |

### Spacing and radius

An 4px base. `space-4` (16px) is the phone gutter and card padding; `space-5` (24px) separates stacked cards; `space-7` (56px) is the header's top. Cards use `radius-md` (10px); avatars and chips use `radius-full`.

### Layout

Single column, 680px measure, 16px side gutters at phone width, mobile first. No framework, no build step: the site is one static HTML file whose stylesheet is these tokens.

## Iconography

None yet beyond the two marks. When icons are needed, draw them on the same 512 grid with the same stroke-to-size ratio as the Roots mark (26/512), round caps, one color.

## Usage rules that name tokens

- Body text is `ink` on `surface`; captions and the pronunciation line are `muted` on `surface`. Never `muted` on `card` for anything a person must read.
- Links are `accent`, underlined, 1px, offset 2px. Buttons: primary is `accent` with `accent-ink` text; quiet is `ink` text on `card` with a `rule` border.
- The mark takes `ink` by inheritance. On an `accent` avatar it is set in `surface`.
- Lockup: mark at 72px, `wordmark` style, `caption` style on the second line, 18px gap. Stacked lockup (square avatars): mark centered above the name, 12px gap, no pronunciation line below 160px.

## Sources

Built from the wokeai repository (`marks/a-roots.svg`, `marks/b-heard.svg`, `index.html`, `README.md`, `design/claude-design-brief.md`) as of commit 3a8bb3d, October 18, 2026.
