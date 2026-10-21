# Claude Design prompt (2026-10-18)

> **Pronunciation respelled October 21, 2026 (Danny):** the line is now **pronounced wōk•ē•ī**. This file records what was sent on October 18 and keeps the old spelling; use the new one if you paste it again.

The design system already exists; Claude Design's job is to build screens on it. Paste the block under PROMPT. Attach the files under UPLOAD with the same message.

## UPLOAD

Attach `design/wokeai-design-system-upload.zip` (or its contents). It holds the published system: `README.md` (the brand book), `tokens.json`, the four component previews with their guidelines, the cover, and `marks/` with both marks as `currentColor` sources plus explicit-ink copies. The system is also published at https://claude.ai/artifact/FALr3euRfEpufD7eyDu8dL; paste that link too, and if Claude Design can read it the upload is a backup.

## PROMPT

Use the attached wokeai design system as given. Read `README.md` first; `tokens.json` is the only source of color, type, spacing, and radius; the marks in `marks/` are final geometry and are not to be redrawn. Everything below is built from that system, with no new colors, no new typeface, and nothing added to the marks.

What wokeai is: a grassroots, open-source community for people using their own AI to push back against systemic oppression, starting as a website (wokeainow.com) and social profiles with no budget. Three pillars: open source, liberation, community. The brand is **wokeai**, one word, always lowercase. Under the wordmark: **pronounced wohk/ē/eye**. The secondary wordmark is **wōke•ĀĪ**. The future podcast is **wahkeeye**, tagline "pronounced wōke•ĀĪ", using the Heard mark.

Build, in this order:

1. **Home page, desktop (1440) and phone (390).** Sections: header lockup (Roots mark, wordmark, pronunciation line); a "What this is" block with the lede and three pillar cards; "Open tools you can use today" as a list of tool cards (use these five: Ollama, llama.cpp, Open WebUI, Hugging Face, Jupyter, each with one plain line of what it does); a Join block with one primary button; a footer. Single column, 680px measure, mobile first. Light and dark versions of both widths. The copy in the attached `components/Card/preview.html` and the brand book is the copy; do not rewrite it.
2. **Social kit.** Circle avatar at 400×400: Roots mark in `ink` on `surface`, and a second in `surface` on `accent`. Header 1500×500 using the secondary wordmark `wōke•ĀĪ` large, left-aligned, on `surface`, with the mark small at right. OG image 1200×630 with the horizontal lockup and the pronunciation line.
3. **Favicon cut.** A 16px and 32px version of the Roots mark: keep the ground line, one blade of grass, the main branch, and the two branch nodes; drop whatever doesn't survive at 16px. Show it at 1x next to the full mark so the lineage is obvious.
4. **Podcast lockup.** `wahkeeye` in the wordmark style with the Heard mark at 72px and "pronounced wōke•ĀĪ" beneath, horizontal and stacked, light and dark. One artboard, not a system.

Rules that are not negotiable: no eye, rays, fist, chains, torch, lightbulb, face, likeness, or X-shaped mark; no quotation of any historical figure; "wokeai" never capitalized, never written "woke AI" or "wokeainow" as the brand; one accent per screen; body text meets 4.5:1 in both themes. If something in the system is missing for a screen (a semantic color, an icon), stop and ask rather than inventing it.

Deliver artboards I can export (SVG for marks and lockups, PNG for the social sizes) and a short note listing anything you had to assume.
