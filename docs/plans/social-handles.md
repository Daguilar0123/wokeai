# Plan: claim the wokeai social handles (brief for an Opus session)

Written October 18, 2026. Danny tried X already and isn't sure it took. The site is live at https://wokeainow.com; the repo is public at https://github.com/Daguilar0123/wokeai; the brand files are in `design/system/` and `marks/`.

## Ground rules for the agent

- **Danny creates every account himself.** The agent walks him through it in his own browser, prepares the exact text to paste, checks the result, and records what was claimed. The agent never enters passwords, never completes CAPTCHAs, and never submits a sign-up form on his behalf (those are his actions by policy).
- **Handle priority:** `wokeai` first; if taken, `wokeainow`; if both taken, `wokeai_` or `wokeaihq`, and record which. Never a spelling that breaks the lowercase one-word rule in the display name.
- **Email for every account:** `wokeai@grownfromconcrete.org` (the forwarding brief covers where that mail lands). Use the same recovery phone Danny chooses once, and write down where 2FA codes go.
- **Profile kit (same on every platform):**
  - Display name: `wokeai`
  - Avatar: the official mark, light surface (`marks/roots-official-light.svg`, exported to PNG at 400×400 for platforms that refuse SVG; the agent exports it with `qlmanage` or `sips`, no redrawing)
  - Header/banner: `design/system/social/wokeai-brand-intro.gif` for platforms that take 1200×600 or wider; a static first frame (`marks/og.png`) where GIFs are refused
  - Bio (≤160 chars): `pronounced wohk/ē/eye. A grassroots, open-source community for people using their own AI to push back against systemic oppression. wokeainow.com`
  - Longer "About" where allowed: the Facebook About in `design/social-copy.md`
  - Link: https://wokeainow.com
  - Pronouns/location fields: Danny decides live.
- **Rules not to break:** lowercase name everywhere; no eye, fist, chain, or likeness imagery; no borrowed slogans; the pronunciation line once per profile.

## Platforms, in order

Do the first tier in one sitting; the rest as Danny has energy. For each: check availability of `wokeai` → create → set avatar, banner, bio, link → verify the public URL loads logged-out → log it in the table below.

1. **X / Twitter** — first, because the earlier attempt is unresolved. Check x.com/wokeai and x.com/wokeainow logged-out. If Danny's attempt created an account, recover it (he may have an email from X in wokeai@ or danny@grownfromconcrete.org); if not, create it.
2. **Bluesky** — handle `wokeai.bsky.social`, then set the custom handle to `wokeainow.com` by adding the DNS TXT record Bluesky gives (`_atproto` → `did=...`) at GoDaddy. That makes the handle the domain itself, which is on-brand. The agent prepares the record; Danny pastes it.
3. **Mastodon** — pick an instance (ask Danny; a tech/activism instance fits better than mastodon.social). Add `rel="me"` verification by putting the profile link in the site footer, so the profile shows a verified link to wokeainow.com.
4. **Instagram** — `wokeai`; link in bio; square avatar; the GIF won't play, use the static frame.
5. **Threads** — comes with the Instagram account; same handle.
6. **TikTok** — `wokeai`; avatar only.
7. **YouTube** — channel named `wokeai`, custom URL `@wokeai`; banner at 2048×1152 (export from the intro card with padding).
8. **LinkedIn** — a Page named `wokeai` (needs Danny's personal LinkedIn as admin).
9. **Facebook** — a Page named `wokeai`; About from `design/social-copy.md` (already written for it).
10. **GitHub** — already `Daguilar0123/wokeai`; consider a `wokeai` organization later, not now.
11. **Reddit** — `u/wokeai` to hold the name; no subreddit yet.
12. **Substack / newsletter** — only if Danny wants one; otherwise skip.
13. **Podcast directories** (Apple, Spotify) — skip until the show exists; the name there is `wahkeeye`.

## Record (fill in as you go)

| Platform | Handle claimed | Public URL | Email used | 2FA method | Status / notes |
|---|---|---|---|---|---|
| X | | | | | |
| Bluesky | | | | | |
| Mastodon | | | | | |
| Instagram | | | | | |
| Threads | | | | | |
| TikTok | | | | | |
| YouTube | | | | | |
| LinkedIn | | | | | |
| Facebook | | | | | |
| Reddit | | | | | |

When done: commit this file with the table filled in, add the live profile links to `index.html`'s Join section (plain links, no embeds or widgets), and add the Mastodon `rel="me"` link. Commit messages record what was claimed and where the codes go.
