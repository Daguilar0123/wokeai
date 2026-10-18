# Handoff: replace the wokeai marks (October 18, 2026)

This file came in an attached zip. Unzip it into the repo at `design/system/` (so this file is `design/system/CLAUDE-CODE.md`), then do the following.

1. **Marks.** Copy every file from `design/system/marks/` into `marks/`. Then replace `marks/a-roots.svg` with the contents of `marks/roots-blueprint.svg`. It's the same role (one ink, `currentColor`) with the new geometry. Do not edit the SVG geometry.
2. **Favicon.** In `index.html`, link `marks/favicon-32.svg` and `marks/favicon-16.svg`. Use the `-dark` versions under `prefers-color-scheme: dark`.
3. **Header mark.**
   - In `index.html`, replace the inline Roots mark with `marks/roots-official-light.svg`, or `roots-official-dark.svg` in dark mode, at 72px.
   - The animated versions are `roots-animated-light.svg` and `roots-animated-dark.svg`.
   - Show the static file under `prefers-reduced-motion: reduce`.
4. **Tokens.** Merge `design/system/tokens.json` (version 2) into the site's CSS custom properties. The new tokens are `root`, `light-halo`, and `light-core`. They are for the mark only, never for text.
5. **Copy.** Replace the home page text with the "Site copy (verbatim)" section of `design/system/README.md`, in the order listed under "Home page structure" in the same file.
6. **Docs.** Replace the brand section of the repo `README.md` with `design/system/README.md`. Note the version bump.
7. **Social.** `design/system/social/wokeai-brand-intro.gif` is the 1200×600 animated intro card for social posts.

The podcast tagline is not decided yet ("spelled wokeai" or "spelled wōke•ĀĪ"). Leave the podcast unchanged.
