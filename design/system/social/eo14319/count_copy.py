"""Count and check the Executive Order 14319 copy in design/social-copy.md (October 22, 2026).

    python3 -P design/system/social/eo14319/count_copy.py          # check; exit 1 on any failure
    python3 -P design/system/social/eo14319/count_copy.py --fill   # also write the counts into the headings

Each platform block under "## Executive Order 14319" is a ```text fence after a "### <Platform>" heading.
Counts:
  plain    Python len(), one per character (LinkedIn, Instagram/Threads, Facebook)
  bluesky  grapheme count; the copy has no emoji or combining marks, so it equals len()
  x        X's weighted count (twitter-text v3): a URL counts 23; characters in U+0000-10FF, U+2000-200D,
           U+2010-201F and U+2032-2037 count 1, everything else 2 (so the interpunct • counts 2)
Rules for every block: the site link https://wokeainow.com; the pronunciation line at most once; at most
three hashtags; no GitHub or covenant link or mention; lowercase wokeai; and the order's words quoted only
as the home page quotes them.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
COPY = ROOT / "design/social-copy.md"
PAGE = (ROOT / "index.html").read_text(encoding="utf-8")
ORDER_QUOTE = "“concepts like critical race theory, transgenderism, unconscious bias, intersectionality, and systemic racism.”"
assert ORDER_QUOTE in PAGE, "the home page no longer carries the order's quoted phrase; stop"
LIMITS = {"LinkedIn": ("plain", 1299), "Bluesky": ("bluesky", 300), "X": ("x", 280),
          "Instagram and Threads": ("plain", 499), "Facebook": ("plain", 999)}
URL = re.compile(r"https?://\S+")


def x_count(t):
    n = 0
    for part in re.split(r"(https?://\S+)", t):
        if URL.fullmatch(part or ""):
            n += 23
            continue
        for ch in part:
            o = ord(ch)
            n += 1 if (o <= 0x10FF or 0x2000 <= o <= 0x200D or 0x2010 <= o <= 0x201F or 0x2032 <= o <= 0x2037) else 2
    return n


def count(kind, t):
    return x_count(t) if kind == "x" else len(t)


md = COPY.read_text(encoding="utf-8")
start = md.index("\n## Executive Order 14319")
end = md.find("\n## ", start + 5)
section = md[start:] if end == -1 else md[start:end]
blocks = re.findall(r"### (?P<name>[^\n(]+?) \((?P<stated>[^)]*)\)\n\n```text\n(?P<body>.*?)\n```", section, re.S)
failures, results = [], []
for name, stated, body in blocks:
    name = name.strip()
    kind, limit = LIMITS[name]
    n = count(kind, body)
    checks = {
        f"over the limit ({n} > {limit})": n > limit,
        "no https://wokeainow.com": "https://wokeainow.com" not in body,
        "pronunciation line more than once": body.count("pronounced") > 1,
        "more than three hashtags": len(re.findall(r"(?<!\w)#\w+", body)) > 3,
        "mentions GitHub or the covenant": bool(re.search(r"github|covenant", body, re.I)),
        # the order's own title ("Preventing Woke AI in the Federal Government") is a name, not the brand
        "capitalized wokeai": bool(re.search(r"Wokeai|WokeAI|WOKEAI|Woke AI",
                                             re.sub(r"[“”\"]?Preventing Woke AI in the Federal Government", "", body))),
        "quotes the order other than as the page does": ("critical race theory" in body and ORDER_QUOTE not in body),
    }
    for msg, bad in checks.items():
        if bad:
            failures.append(f"{name}: {msg}")
    results.append((name, kind, n, limit, stated))

if "--fill" in sys.argv:
    new = section
    for name, kind, n, limit, stated in results:
        unit = {"plain": "characters", "bluesky": "characters", "x": "characters as X counts them"}[kind]
        bound = f"under {limit + 1:,}" if kind == "plain" else f"limit {limit:,}"
        new = new.replace(f"### {name} ({stated})", f"### {name} ({n:,} {unit}, {bound})", 1)
    COPY.write_text(md.replace(section, new), encoding="utf-8")

for name, kind, n, limit, _ in results:
    print(f"{name:22} {n:5,}  (limit {limit:,}, counted as {kind})")
if len(results) != len(LIMITS):
    failures.append(f"found {len(results)} platform blocks, expected {len(LIMITS)}")
if failures:
    print("FAILURES:", *failures, sep="\n - ")
    sys.exit(1)
print("all blocks pass")
