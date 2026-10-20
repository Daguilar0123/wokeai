# Plan: forward-only brand addresses on wokeainow.com

Written October 18, 2026; this version supersedes two earlier drafts the same day (a grownfromconcrete.org alias, and before that a mailbox). Danny's decision: *whichever address we create is the one every social account uses.*

## What is true (checked October 18, 2026)

- `grownfromconcrete.org` delivers mail to Microsoft 365 sold through GoDaddy (MX `grownfromconcrete-org.mail.protection.outlook.com`; SPF `include:secureserver.net`). `danny@grownfromconcrete.org` is that mailbox.
- The `wokeai@grownfromconcrete.org` mailbox Danny created in SiteGround can never receive mail (the domain's MX doesn't point at SiteGround). **Delete it**: SiteGround → Site Tools → Email → Accounts.
- `wokeainow.com` has no MX record and no mail service. Good: nothing to migrate.
- Already in place: an Outlook category `wokeai` (green) on danny@'s mailbox.

## The decision

Forward-only addresses on **wokeainow.com**, run by **Forward Email** (forwardemail.net): free for forwarding, the whole service is open source, and it is configured with DNS records alone, so the domain's nameservers stay at GoDaddy and the GitHub Pages records are untouched.

- `accounts@wokeainow.com` → `danny@grownfromconcrete.org` — the address for **every** social sign-up (unpublished, so verification codes never share a stream with public spam).
- `hello@wokeainow.com` → `danny@grownfromconcrete.org` — the public contact address for the site and bios.

(Danny, October 19, 2026: `wokeai@wokeainow.com` was redundant; replaced by `accounts@`.)

No mailbox exists anywhere; replies arrive in Danny's inbox. Sending *as* these addresses needs Forward Email's paid plan (outbound SMTP); not needed to claim accounts.

## DNS records at GoDaddy for wokeainow.com (from Forward Email's FAQ, read October 18, 2026)

| Type | Name | Value | Priority | TTL |
|---|---|---|---|---|
| MX | `@` | `mx1.forwardemail.net` | 0 | 1 Hour |
| MX | `@` | `mx2.forwardemail.net` | 0 | 1 Hour |
| TXT | `@` | `forward-email=hello:danny@grownfromconcrete.org,accounts:danny@grownfromconcrete.org` | | 1 Hour |
| TXT | `@` | `v=spf1 a include:spf.forwardemail.net -all` | | 1 Hour |

Notes from their docs: both MX records are required and no other MX may exist (there is none); several aliases go in one `forward-email=` record separated by commas, each record under 255 characters; specific aliases beat a catch-all, and there is no catch-all here on purpose (a catch-all invites spam); they recommend `-all` in SPF.

**A privacy trade-off to know:** on the free plan the forwarding rule lives in public DNS, so anyone who looks up the domain's TXT records can see that mail goes to `danny@grownfromconcrete.org`. The paid plan (a few dollars a month) hides destinations and adds outbound SMTP. For now the exposure is one email address that already appears on Danny's public work; revisit when the site needs to send mail.

## Steps

1. **GoDaddy → wokeainow.com → DNS Records:** add the four records above. **Done October 19, 2026:** Danny saved the TXT edit (hello + accounts) and the SPF record; all four records confirmed live on GoDaddy's nameserver and on public DNS with `dig`. GoDaddy shows 10 records per page and the TXT rows sit on page 2, which is why an earlier walkthrough showed nothing to save.
2. **Forward Email account:** Danny adds `wokeainow.com` under My Account → Domains and clicks **Verify Records**. The agent never creates accounts. **Decided October 19, 2026 (Danny, relayed by the handles session):** wokeai gets its own **new** Forward Email account, not the one he already has for another site. He named two possible logins, danny@dannysdigitaldesigns.com or an address at wokeainow.com. The agent recommends danny@dannysdigitaldesigns.com: it is a real mailbox on that domain's own mail server, while a wokeainow.com login would be forwarded by the very account it unlocks. Rule: the account's login must be a real mailbox, never an address that the same account forwards. Danny creates the account himself. **Optional, not blocking:** step 3 proved delivery works on the DNS records alone, with no account. The account adds a dashboard, delivery logs, and the paid options (hidden destinations, sending as the address); create it when one of those is wanted. thetatteredrose.com has forwarded the same DNS-only way.
3. **Test:** from any outside address, send to `accounts@wokeainow.com` and to `hello@wokeainow.com`; both should land in danny@'s inbox within a minute or two. DNS can take up to an hour to propagate. **`accounts@` passed October 19, 2026:** Danny's test from his Gmail, sent 21:53:42 UTC, arrived in danny@grownfromconcrete.org at 21:54:02 UTC (seen by the handles session). `hello@` is not tested yet.
4. **Outlook on the web → Settings → Mail → Rules:** rule `wokeai mail`: condition *Sent to* contains `wokeainow.com` → actions *Move to* a new folder `wokeai` and *Categorize* `wokeai`. (The connected tools can't make folders or sent-to rules, so this is by hand.)
5. **SiteGround:** delete the dead `wokeai@grownfromconcrete.org` mailbox.
6. **Separately, grownfromconcrete.org's SPF** is `v=spf1 include:secureserver.net -all` and omits `include:spf.protection.outlook.com`, which can hurt every email Danny sends from his M365 mailbox. Fix it in that domain's DNS at GoDaddy; there must be exactly one `v=spf1` TXT record.

## Done looks like

Mail to both addresses arrives in danny@'s `wokeai` folder; the SiteGround mailbox is gone; the handles plan uses `accounts@wokeainow.com` as the sign-up address; this file records the date, the Forward Email account's recovery details location, and the SPF fix.
