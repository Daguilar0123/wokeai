# wokeai design system

Version 2, October 18, 2026. Supersedes the October 18 upload (version 1). Danny Aguilar owns the decisions recorded here.

`tokens.json` is the only source of color, type, spacing, radius, and mark geometry. The files in `marks/` are final; use them as they are and do not redraw them. The visual brand book is `wokeai Brand Book.dc.html` in the project root.

## Intro

wokeai (pronounced wohk/ē/eye). A grassroots, open-source community for people using their own AI to push back against systemic oppression. Open tools, shared in common. Starting small. wokeainow.com

## The name

- **wokeai**: one word, always lowercase, even at the start of a sentence. Never *Wokeai*, never *woke AI* when you mean the brand, never *wokeainow* (that is only the domain).
- **Pronunciation line**: `pronounced wohk/ē/eye`, set in `caption`, `muted`, under the wordmark wherever there is room for a second line. State it once per surface.
- **Secondary wordmark**: `wōke•ĀĪ`, set in `wordmark-secondary`. Use it on social headers, merch, the home page's "The name" block, and in the podcast tagline. Check that Ā, Ī, ō, and • render in Archivo before shipping.
- **Podcast** (future): **wahkeeye**, tagline `pronounced wōke•ĀĪ`, with the Heard mark.

## Site copy (verbatim)

> wokeai is one word, always lowercase, and it’s said wohk/ē/eye. The spelling says one thing to a glance. We’ll tell you how it’s said.
>
> We’re a grassroots community for people who use their own AI to push back against systemic oppression: students, independent researchers, organizers, and builders. Not a product. A place to gather, a list of open tools that already exist, and the people who want to build the next ones.
>
> Three things hold it up. Open source: tools held in common, with the code where everyone can read it. Liberation: starting from the people with the least power, not the most. Community: nobody does this alone. The roots are the point.
>
> We’re in our first days and there’s no budget, so we start with what we have. Read the tool list, bring the ones you use, and tell someone.
>
> wokeainow.com · github.com/Daguilar0123/wokeai

Voice: plain, direct, warm. Short sentences. No borrowed slogans, no quotation of historical figures, nothing that implies violence or claims anyone's endorsement.

## Roots mark

Three clumps of grass above a ground line. Below, each clump has its own roots, drawn as a network:

- **Middle root**: a node just under the ground, a main root straight down to a deep node, one branch down-left and one down-right, each bending to vertical before its node.
- **Side roots**: smaller, under the outer clumps. Each has a main root and one branch, and the branch faces outward (left on the left, right on the right). They have no top node.

Geometry is on a 512 grid: stroke 12, round caps and joins, main nodes r=24, side trunk nodes r=16, side branch nodes r=13. Everything sits inside r=200 of center, so a circle crop never clips.

### Versions and files (`marks/`)

| use | file |
| --- | --- |
| **Official logo**, light surfaces | `roots-official-light.svg` |
| **Official logo**, dark surfaces | `roots-official-dark.svg` |
| **Official animated logo**, light | `roots-animated-light.svg` |
| **Official animated logo**, dark | `roots-animated-dark.svg` |
| Blueprint (one ink, inherits color) | `roots-blueprint.svg` |
| Blueprint in ink / paper | `roots-blueprint-ink.svg`, `roots-blueprint-paper.svg` |
| Blueprint, animated (growth only, no light) | `roots-animated-blueprint.svg` |
| Favicon | `favicon-16.svg`, `favicon-32.svg`, and `-dark` versions |
| Podcast mark | `heard.svg`, `heard-ink.svg`, `heard-paper.svg` |

Alternate animations are kept in the brand book, not as files: light running down only, and light running up only. Both use the same `wokeai Mark.dc.html` component (`lightDir="down"` or `"up"`).

### Mark colors

- grass is `accent`
- the ground line is `earth`
- roots and nodes are `root`
- the traveling light is `light-core` with a `light-halo` glow

The blueprint uses one ink: `ink` on `surface`, or `surface` on `accent`. On an `accent` background, always use the blueprint in `surface`, never the color mark.

### Animation (official)

The loop runs 7.0s:

1. **0.1s**: light starts at the grass tips and runs down through the ground to every node. Each node flashes as the light arrives.
2. **1.75s**: after a beat, the light rises from the nodes, back through the ground, to the grass tips. Each tip flashes.
3. **3.5s**: the roots sink toward their deepest node, the side branches fold in, and the grass sinks into the ground.
4. **4.7s**: everything has vanished. At 4.85s a node pops in just under the ground.
5. **5.0s**: the roots regrow downward and the grass regrows upward, with a small overshoot.

The light travels at 320 grid units per second. With `prefers-reduced-motion`, show the static official logo. On the site header, play the loop once on hover rather than continuously.

### Rules

- Minimum size: 24px beside text, 32px alone. Below 32px, use the favicon cut.
- Clear space on every side: one eighth of the ground-line length.
- No drop shadows or outlines, and never recolor the mark outside the tokens above.
- The brand never shows an eye, rays, fist, chains, torch, lightbulb, face or likeness, or an X-shaped mark.

### Favicon cut

- **32px**: ground, the middle clump, and the middle root with both branches.
- **16px**: ground, one blade, the main root, and one branch.

The side roots and side clumps drop out at both sizes.

## Lockups

- **Horizontal**: mark at 72px, an 18px gap, then `wordmark` with `caption` beneath (6px gap).
- **Stacked** (square avatars): mark centered above the name, 12px gap. Drop the pronunciation line below 160px.
- **OG image** (1200×630): the horizontal lockup scaled 2.6×.
- **Social header** (1500×500): `wōke•ĀĪ` large and left-aligned on `surface`, with the official mark at right.
- **Avatars** (400, circle crop):
  - official on `surface`
  - official dark on dark `surface`
  - blueprint in `surface` on `accent`

## Color, type, layout

The tokens are in `tokens.json`. Every text pair there meets 4.5:1. One accent per screen.

- **Type**: one family, Archivo, for everything.
- **Layout**: one column, 680px measure, 16px phone gutter, mobile first.
- **Cards**: `card` fill, a 1px `rule` border, `radius-md`.
- **Links**: `accent`, underlined 1px with a 2px offset.
- **Buttons**: primary is `accent` with `accent-ink` text.

`root`, `earth`, and the light tokens are for the mark and illustration only. Never use them for text.

Semantic states (success, warning, error) are not defined yet. Add them as tokens before using them.

## Home page structure

1. Header lockup, with the animated mark playing once on hover
2. What this is: the lede
3. Three things hold it up: three pillar cards
4. Open tools you can use today: Ollama, llama.cpp, Open WebUI, Hugging Face, Jupyter
5. The name: `wōke•ĀĪ` and the name paragraph
6. Join: one paragraph and one primary button
7. Footer: wokeainow.com · github.com/Daguilar0123/wokeai

## Components (live source)

- `wokeai Mark.dc.html`: the mark renderer. Props:
  - `mark`: roots or heard
  - `color`
  - `theme`
  - `animated`
  - `loop`
  - `lightDir`: cycle, down, or up
  - `cut`: full, 32, or 16
- `wokeai Home.dc.html`: the home page. Prop: `theme`.
- `wokeai Brand Book.dc.html`: the visual brand book.
