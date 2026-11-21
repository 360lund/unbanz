"""Adds /assets/lead-events.<hash>.js (GTM lead_email events) right after the contact-policy script tag on every public page. Idempotent; skips /users."""
import re, pathlib, sys
R = pathlib.Path(__file__).resolve().parents[2]
SRC = "/assets/lead-events.d43f11501d27.js"
TAG = '<script defer="" src="%s"></script>' % SRC
n = 0
for p in R.rglob("*.html"):
    if any(x in p.parts for x in (".git", "node_modules", "scripts", "users", "qa-render")): continue
    s = p.read_text(errors="ignore")
    s2 = re.sub(r'<script defer="" src="/assets/lead-events\.[0-9a-f]+\.js"></script>', "", s)
    m = re.search(r'<script defer="" src="/assets/contact-policy\.[0-9a-f]+\.js"></script>', s2)
    if not m: continue
    s2 = s2[:m.end()] + TAG + s2[m.end():]
    if s2 != s: p.write_text(s2); n += 1
print("pages updated", n)
