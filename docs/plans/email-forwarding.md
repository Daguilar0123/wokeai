# Plan: a wokeai email address that lands in Danny's inbox

Written October 18, 2026, revised the same day after checking DNS.

## What is true (checked October 18, 2026)

- `grownfromconcrete.org` delivers mail to **Microsoft 365**: its MX record is `grownfromconcrete-org.mail.protection.outlook.com`, and `danny@grownfromconcrete.org` is a live M365 mailbox (the connected Outlook account reports userPrincipalName danny@grownfromconcrete.org).
- That M365 service is **sold through GoDaddy** (the domain's SPF is `include:secureserver.net`, GoDaddy's mail signature), billed on the GoDaddy account, managed at GoDaddy's Email & Office dashboard, not at admin.microsoft.com. Danny never saw a Microsoft bill, which is why it never looked like a Microsoft subscription.
- The `wokeai@grownfromconcrete.org` mailbox Danny created in **SiteGround** can never receive mail: the domain's MX doesn't point at SiteGround. It was used once and "didn't work" for exactly that reason. **Delete it** (SiteGround → Site Tools → Email → Accounts). Nothing depends on it.
- `wokeainow.com` has no MX record and no mail service yet.
- Already done from the main session: an Outlook **category** `wokeai` (green) exists in danny@'s mailbox.

## The decision

Make the brand address an **alias on danny@'s existing mailbox**: free, no new license, no forwarding to break, and Danny can send as it. Two candidate addresses:

1. **`wokeai@grownfromconcrete.org`** (recommended now): zero setup beyond adding the alias in GoDaddy's dashboard. Fine for platform sign-ups, which nobody else sees.
2. **`wokeai@wokeainow.com`** (on-brand, for later): needs `wokeainow.com` added as a second domain on the GoDaddy M365 account, which GoDaddy may or may not allow on the current plan. Not needed for sign-ups; revisit when the site has a public contact address.

## Steps (15 minutes, Danny's hands on the keyboard)

1. **SiteGround:** delete the dead `wokeai@` mailbox. Site Tools → Email → Accounts → the wokeai row → Delete.
2. **GoDaddy → Email & Office (productivity.godaddy.com)** → the danny@grownfromconcrete.org mailbox → **Aliases** (or "Manage → Email aliases") → add `wokeai`. Save. Aliases are free on GoDaddy's Microsoft 365 plans.
3. **Test:** send one message from any outside address (Gmail is fine) to `wokeai@grownfromconcrete.org`. It should arrive in danny@'s inbox within a minute.
4. **Outlook on the web (outlook.office.com), Settings → Mail → Rules:** new rule `wokeai mail`: condition *Sent to* `wokeai@grownfromconcrete.org` → actions *Move to* a new folder `wokeai` (create it from the folder picker) and *Categorize* `wokeai`. Run it on existing mail once. (The connected tools can make categories and sender/subject rules but not folders or sent-to rules, so this part is by hand.)
5. **Send as the alias:** in Outlook on the web, Settings → Mail → Compose and reply, confirm the alias appears in the From picker. If not, GoDaddy's dashboard has a "send from alias" toggle for the mailbox.
6. **Record** in this file: which form the address is (alias on danny@), where recovery and 2FA for the mailbox go, and the date.

## Fix while you are in there: the SPF record

`grownfromconcrete.org`'s SPF is `v=spf1 include:secureserver.net -all`. Mail sent from the M365 mailbox goes out through Microsoft's servers, which that record does not authorize, so some recipients may spam-folder or reject Danny's outgoing mail. GoDaddy's own setup normally writes `v=spf1 include:secureserver.net include:spf.protection.outlook.com -all`. Check in GoDaddy's DNS for grownfromconcrete.org whether a second SPF record exists (there must be exactly one TXT starting with `v=spf1`) and make it include both. This is unrelated to wokeai but it affects every email Danny sends from that address.

## Done looks like

The SiteGround mailbox is gone; `wokeai@grownfromconcrete.org` is an alias on danny@; a test message lands in the `wokeai` folder, tagged; Danny can send as the alias; SPF includes Microsoft; this file records the date and where recovery goes.
