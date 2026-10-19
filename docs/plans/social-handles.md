# Plan: claim the wokeai social handles (brief for an Opus session)

Written October 18, 2026. Danny tried X already and isn't sure it took. The site is live at https://wokeainow.com; the repo is public at https://github.com/Daguilar0123/wokeai; the brand files are in `design/system/` and `marks/`.

## Ground rules for the agent

- **Danny creates every account himself.** The agent walks him through it in his own browser, prepares the exact text to paste, checks the result, and records what was claimed. The agent never enters passwords, never completes CAPTCHAs, and never submits a sign-up form on his behalf (those are his actions by policy).
- **Handle priority:** `wokeai` first; if taken, `wokeainow`; if both taken, `wokeai_` or `wokeaihq`, and record which. Never a spelling that breaks the lowercase one-word rule in the display name.
- **Email for every account:** `accounts@wokeainow.com`, a forward-only address that lands in danny@grownfromconcrete.org (Danny's decision, October 19, 2026; it replaced `wokeai@grownfromconcrete.org` and `wokeai@wokeainow.com`, see `docs/plans/email-forwarding.md`). The public contact address on profiles that have a contact field is `hello@wokeainow.com`. **No account is created until a test message to `accounts@wokeainow.com` has landed.** Use the same recovery phone Danny chooses once, and write down where 2FA codes go.
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

1. **X / Twitter** — first, because the earlier attempt is unresolved. Check x.com/wokeai and x.com/wokeainow logged-out. If Danny's attempt created an account, recover it (he may have an email from X in danny@grownfromconcrete.org); if not, create it.
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

## Availability check (October 18, 2026, logged-out, by the handles session)

| Platform | `wokeai` | `wokeainow` | Notes |
|---|---|---|---|
| X | taken: a personal account ("WANG HAINA") | free (404) | |
| Bluesky | taken: `wokeai.bsky.social`, created November 2024 | free | the custom handle `wokeainow.com` replaces the bsky.social one anyway |
| Mastodon | free on mastodon.social | free | instance still to choose |
| Instagram | taken: 7 followers, 85 following | free | |
| Threads | taken (follows the Instagram account) | free | |
| TikTok | taken: account from January 2021 | free | |
| YouTube | taken: a channel from 2007, no description | free | |
| Reddit | not checked: Reddit blocks automated checks | not checked | check live at reddit.com/user/wokeainow |
| GitHub | the login `wokeai` is someone else's | n/a | the repo stays `Daguilar0123/wokeai` |

**Decision (Danny, October 18, 2026):** use **`wokeai` wherever it is free** (Mastodon, and Reddit if the live check allows) and **`wokeainow` elsewhere** (X, Bluesky, Instagram, Threads, TikTok, YouTube). Display name `wokeai` everywhere. The session had recommended `wokeainow` on every platform for uniformity; Danny chose to hold the exact name where he can, per the plan's original priority order. No account is created until the brand email address receives mail.

**Danny's earlier X attempt (checked October 18, 2026):** no mail in danny@grownfromconcrete.org mentions wokeai; the only X welcome mails there are for other accounts. If the attempt used the SiteGround address, the verification mail was never delivered, so X almost certainly never held a name for it. Create fresh; if X reports the email as already in use, recover it by password reset once the brand address receives mail.

**Email (October 19, 2026, Danny's decision relayed by the main session):** sign-ups use `accounts@wokeainow.com`; the public contact address is `hello@wokeainow.com`; both forward to danny@grownfromconcrete.org through Forward Email. `wokeai@wokeainow.com` was dropped as redundant. Status when this was written: the wokeainow.com TXT record still listed `wokeai` and `hello`, the `accounts` alias was not yet in DNS, and no test mail to `accounts@` had landed, so no account has been created.

## Paste sheet (prepared October 18, 2026)

Same values on every platform. Files are in `marks/png/`, exported from `marks/roots-official-light.svg` and `marks/og.png` with Quick Look and Pillow, never redrawn, flattened onto `surface` `#f6f4ef` so circle crops never show black.

- **Handle:** `wokeai` where free (Mastodon, maybe Reddit), otherwise `wokeainow` (Danny's decision, October 18, 2026)
- **Display name:** `wokeai`
- **Account email (every sign-up):** `accounts@wokeainow.com`
- **Public contact email (any contact field):** `hello@wokeainow.com`
- **Bio, 144 characters:** `pronounced wohk/ē/eye. A grassroots, open-source community for people using their own AI to push back against systemic oppression. wokeainow.com`
- **Bio with the name, 153 characters, for platforms that do not show the display name next to the bio:** `wokeai (pronounced wohk/ē/eye). A grassroots, open-source community for people using their own AI to push back against systemic oppression. wokeainow.com`
- **Short bio, 121 characters, where 144 does not fit (TikTok allows 80: use `pronounced wohk/ē/eye. Open tools against systemic oppression. wokeainow.com`):** `A grassroots, open-source community for people using their own AI to push back against systemic oppression. wokeainow.com`
- **Link:** `https://wokeainow.com`
- **Avatar:** `marks/png/wokeai-avatar-400.png`; `wokeai-avatar-800.png` for Instagram, TikTok and YouTube, which upscale small files badly
- **Header 1500×500 (X, Bluesky, Mastodon):** `marks/png/wokeai-header-1500x500.png` (the intro card centered on surface, no crop)
- **YouTube banner 2048×1152:** `marks/png/wokeai-youtube-banner-2048x1152.png` (the intro card scaled to the 1546×423 safe area, so no device crops the text)
- **Facebook cover and LinkedIn cover:** export when those pages are made; they want other ratios
- **About (Facebook, LinkedIn, YouTube description):** the About text in `design/social-copy.md`

**Bluesky custom handle, after the account exists:** Settings → Account → Handle → "I have my own domain" → enter `wokeainow.com` → Bluesky shows a TXT record. At GoDaddy, DNS for wokeainow.com, add: type TXT, name `_atproto`, value `did=did:plc:…` exactly as shown, default TTL. The site's A and CNAME records for GitHub Pages are untouched by this. Back in Bluesky, "Verify DNS record". The profile URL becomes `bsky.app/profile/wokeainow.com`.

**Mastodon verification, after the account exists:** add to the footer of `index.html` a link with `rel="me"` to the profile, for example `<a rel="me" href="https://INSTANCE/@wokeainow">Mastodon</a>`, push, then in Mastodon put `https://wokeainow.com` in a profile metadata field; Mastodon fetches the page and marks the link verified.

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
