# wokeai

One lowercase word. Pronounced *wohk/ē/eye*.

Brand: **wokeai**. Website: **wokeainow.com** (Danny's choice, October 18, 2026; $45.99 for three years at GoDaddy, then $22.99/yr; not yet purchased as of this commit).

An aspirational brand and community: a website and social profiles gathering people around grassroots resistance to systemic oppression, from students and independent researchers using their own AI to tools built and shared in the open. Pillars: open source, liberation, community. It answers Executive Order 14319, "Preventing Woke AI in the Federal Government" (July 23, 2025), and is informed by the Black liberation struggle in America.

Not an AI product yet. As of October 2026 there is no budget, so this starts as a site that spreads awareness, shares existing tools, and gathers people who want to build.

## What is here

- `marks/a-roots.svg` — **the wokeai mark.** Grass above a ground line; below it the roots are drawn as a clean git graph: a main branch straight down, 35% longer than its branches; one branch down-right from the top node; one down-left from the 60% mark; every branch ends in a node; no merge (v4, Danny's spec, October 18, 2026). One color (`currentColor`), safe inside a circle crop, built to sit beside the lowercase wordmark.
- **Design system** — published as a claude.ai Design System artifact on October 18, 2026: https://claude.ai/artifact/FALr3euRfEpufD7eyDu8dL (private to Danny until shared). Tokens for both themes, Archivo as the one typeface, the Lockup, Wordmark, Card, and Button components, a cover, and the marks in its asset store. Built from this repo at commit 3a8bb3d; `design/claude-design-brief.md` is the brief it answers. Claude Design builds on it; changes go to that artifact, never to a second one.
- `marks/b-heard.svg` — **reserved for the podcast, working name *wahkeeye*.** Three arcs of sound arriving at a listening point. Deliberately not the Wi‑Fi construction: nothing is emitted, something is heard.
- `preview.html` — both marks at 512 / 64 / 32 / 16 px, light and dark, in the circle crop, beside the wordmark, with lookalike glyphs (a plain git graph, the Wi‑Fi glyph) for the risk check. Open it in a browser.

## Decisions, dated

Danny decided (October 18, 2026):

- **Mark A is the symbol.** Chosen on sight from the first preview, with one tweak: the roots must read as a git graph with a main branch, two open branches, and one merged branch. Three revisions followed to stop the merge bulge and a lower branch from forming a letter R.
- **Mark B is not scrapped.** It is held for the podcast.
- **Theology stays implicit** in the public brand. The images carry it; the site speaks in liberation and open-source language and is interfaith by default. Sources get named on Tattered Rose, not here.
- **The old placeholder (an open eye with rays) is replaced.** It read as the watcher, and the whole point is the watched being heard.
- **The spoken form is *wohk/ē/eye*.** An earlier "whoa-keyah" came from misreading *wokeai* as *wokeia*; Danny caught it the same day. The pronunciation line sits under the wordmark on purpose: the spelling says one thing to a glance, and the brand tells you how it is actually said.
- **Domain: wokeainow.com.** The exact-name .com is a $3,762 premium and woke.ai is taken; wokeainow.com keeps the brand spelled exactly and costs $22.99/yr. The brand stays "wokeai," never "wokeainow."
- **License: AGPL-3.0 for the code; the name and marks reserved; the research writing CC BY-SA 4.0.** Reached by questioning, not by default, October 18, 2026. Danny's first instinct was that it depends who takes the tool (a co-op versus a surveillance vendor); told that no open-source license can tell them apart, he chose the rule that binds everyone equally to share back. Asked *when* an improver owes the public their changes, he chose "as soon as people are using it, any way," hosted or installed, which is the clause that makes it AGPL rather than GPL. The marks stay out of the code license so that using the code is not permission to wear the flag; a community-use policy for the name and marks is to come. The research memo is prose, so it carries the share-alike license for text.
- **The podcast is *wahkeeye*, tagline "pronounced wōke•ĀĪ."** Danny proposed flipping the whole brand to this spelling (October 18, 2026) and decided against it the same day: the main brand stays one legible lowercase word, and the spelled-from-sound name goes to the one medium that is heard rather than seen. The letters are Google's respelling of *wok·e·ai* (wok as in the pan: *wäk*); the "woke" lives in the tagline, which is the joke. Mark B is its mark. Domain `wahkeeye.com` was $45.99 for three years at GoDaddy when checked; not purchased, and not needed until the show exists. Known risks, recorded so they get tested before launch: the word reads like a Pacific Northwest Indigenous place name (cf. Wahkiakum, Wahkon); it is hard to spell from hearing; it puts "eye" back in a name.

## Where the ideas come from

- *Grass roots*: Malcolm X, "Message to the Grass Roots," King Solomon Baptist Church, Detroit, November 10, 1963, is the one speech whose transcript excerpt was verified during research. The brand borrows the idea of the field, not any quotation, likeness, or signature.
- *Roots as a commons*: open-source forking, and the symbiosis image in Danny's own writing (2014, 2025): what sustains a thing is the network underneath it, shared.
- *The heard cry*: the inversion of the surveillance eye. Being awake, in the liberation tradition, is hearing the cry, not watching from above.

## License and brand

- **Code** (the site, `index.html`, `preview.html`, and anything else that runs) is licensed under the [GNU Affero General Public License v3.0](LICENSE). Use it, change it, share it; if you run a changed version for other people, hosted or installed, offer them your source.
- **Research writing** in `research/` is licensed [CC BY-SA 4.0](research/LICENSE.md): share and adapt with credit, under the same terms.
- **The name wokeai, its spoken form, and the marks in `marks/`** are not covered by either license. They are the brand of this community, held by Daniel Aguilar, all rights reserved. A policy for community use of the name and marks is coming; until then, please ask before putting them on a project, product, or merchandise. The code license is permission to use the code, not to speak as wokeai.

## Not done yet

- No trademark or availability search has been run on "wokeai" or on either mark.
- The 16 px favicon needs its own simplified cut of mark A.
- The site is not hosted anywhere yet and wokeainow.com is not purchased. The code is public at https://github.com/Daguilar0123/wokeai (since October 18, 2026, licensed as above).
- `CODE_OF_CONDUCT.md` still has the stock `[INSERT CONTACT METHOD]` placeholder; Danny needs to choose where reports go.
- No written policy yet for community use of the name and marks (see "License and brand").
