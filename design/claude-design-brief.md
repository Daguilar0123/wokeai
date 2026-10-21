# Claude Design brief: wokeai design system

> **Pronunciation respelled October 21, 2026 (Danny):** the line is now **pronounced wōk/ē/ī**. This file records what was sent on October 18 and keeps the old spelling; use the new one if you paste it again.

Written 2026-10-18. Paste the block under "PROMPT" into Claude Design. Upload the files listed under "UPLOAD" with it.

## UPLOAD

- `marks/a-roots.svg` — the wokeai mark (final geometry; use it, don't redraw it)
- `marks/b-heard.svg` — the podcast mark (reserved; include in the system)
- `index.html` — the current one-page site shell (copy and structure to keep)
- `preview.html` — size, theme, and lookalike tests already done
- `README.md` — every brand decision, dated

## PROMPT

Build a design system for **wokeai**, a grassroots, open-source community hub for people using their own AI to push back against systemic oppression. Not an AI product yet: a website plus social profiles, run on no budget, with open source, liberation, and community as its three pillars. It answers a 2025 U.S. executive order that uses "woke AI" as an insult; the brand takes the word back. It is informed by the Black liberation struggle, but the public brand speaks in plain liberation and open-source language and names no theological sources.

### The name (fixed; do not change any of this)

- Brand: **wokeai**. One word, always lowercase, even at the start of a sentence. Never "Wokeai", never "woke AI", never "wokeainow".
- Website: wokeainow.com.
- Pronunciation line, set under the wordmark: **pronounced wohk/ē/eye**. The spelling says one thing to a glance; the line tells you how it's actually said. That gap is the brand's one joke and its whole posture: subversive, not hiding, proud.
- Secondary wordmark: **wōke•ĀĪ** (interpunct, macrons). It is the pronunciation line turned into type, meant to look like a dictionary entry. Use it on social headers, merch, and the podcast lockup. It must be set in the same typeface as the main wordmark, so that face must have real macron glyphs (Ā, Ī, ō) and a proper interpunct.
- Podcast (future): **wahkeeye**, tagline "pronounced wōke•ĀĪ", with mark B.

### The mark (fixed geometry; refine, don't redraw)

`a-roots.svg` is the mark: grass above a ground line, and below it a root system drawn as a git graph, one main branch straight down, two branches ending in nodes, no merge. It means grass roots (literally) and open-source forking (literally): what sustains the thing is underneath and shared. It is one color, uses `currentColor`, and is safe inside a circle crop. Keep the geometry. You may tune stroke weight and node size for optical balance, and you must produce:

1. A 16px favicon cut (fewer elements if needed, same idea).
2. Horizontal lockup: mark + `wokeai` + pronunciation line.
3. Stacked lockup for square avatars.
4. Clear-space and minimum-size rules.
5. The same for `b-heard.svg` as the podcast mark with `wahkeeye`.

Do not add: an eye, rays, a fist, chains, a torch, a lightbulb, any face or likeness, any quotation from a historical figure, or an X-shaped mark. The earlier placeholder was an open eye with rays and it was replaced on purpose; it read as surveillance.

### What to deliver

- **Color**: tokens for light and dark, defined on `:root` and under `prefers-color-scheme: dark`. The current site uses a warm off-white (#f6f4ef) and near-black (#141414) with one accent (#1f6f4a light / #6fcf9a dark). Keep the warmth and the single accent; propose the full ramp (surface, card, rule, muted text, accent, accent-on-dark) with contrast ratios that pass AA for body text and UI.
- **Type**: one typeface family for wordmark and UI, with weights for the 44px wordmark, headings, 17px body, 13px uppercase labels, and the pronunciation line. Must have Ā Ī ō and •. Show the wordmark and the secondary wordmark side by side in it.
- **Spacing and layout**: a single-column 680px measure, 16px side gutters on phones, the card pattern already in `index.html` (tool cards, pillar cards). Mobile first.
- **Components**: header lockup, mission block with three pillar cards, tool-link card list, join block, footer; buttons (primary, quiet); a "pronounced" caption style. Build them from the tokens; keep the HTML semantic and dependency-free (no framework, no build step; the site is a single static file).
- **Social kit**: circle avatar (mark only, and mark on accent), 1500×500 header using the secondary wordmark, a 1200×630 OG image with the lockup and the pronunciation line.
- **Usage page**: the lockups, the do-not list above, minimum sizes, and the lowercase rule.

### Voice, in three lines

Plain, direct, warm. Pride without volume. It explains the joke once and then never winks again.

### Done looks like

A design-system page I can read and hand to a developer, plus exported assets (SVG for marks and lockups, PNG for social sizes), with the tokens in a CSS block I can drop into `index.html` without changing its structure.
