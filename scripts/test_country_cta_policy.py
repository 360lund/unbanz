# -*- coding: utf-8 -*-
"""Regression checks for country-page enquiries, published fees, sitemap and llms."""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
os.chdir(ROOT)
from country_cta_policy import FEE_ANSWER, NO_FEE_KINDS, hold_country, service_kind  # noqa: E402

FAILS = []


def fail(msg):
    FAILS.append(msg)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def walk_html():
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "assets", "scripts")]
        for name in files:
            if name.endswith(".html"):
                yield os.path.join(root, name)[2:] if os.path.join(root, name).startswith("./") else os.path.join(root, name)


holds = []
for rel in walk_html():
    country = hold_country(rel)
    if not country:
        continue
    html = read(rel)
    holds.append(rel)
    title = re.search(r"<title>([^<]+)", html)
    kind = service_kind(rel, title.group(1) if title else "")
    if "cta-hold" in html:
        fail(rel + " still suppresses every contact control")
    for needle in ("wa.me", "mailto:", "mobile-contact", "mail-pick", "contact-policy."):
        if needle not in html:
            fail(rel + " missing " + needle)
    if 'href="/contact/"' not in html and "contato" not in html and "contact/" not in html:
        fail(rel + " lost contact navigation")
    canon = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    if not canon or not canon.group(1).startswith("https://unbanz.com/"):
        fail(rel + " canonical changed or missing")
    robots = re.search(r'name="robots" content="([^"]*)"', html)
    if rel.startswith("instagram-account-recovery-saudi") and (not robots or "noindex" not in robots.group(1)):
        fail(rel + " noindex was cleared")
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html):
        try:
            data = json.loads(block)
        except json.JSONDecodeError as exc:
            fail(rel + " invalid schema " + str(exc))
            continue
        blob = json.dumps(data)
        if "wa.me" in blob:
            fail(rel + " schema still advertises WhatsApp")
    if "Instagram Marketplace" in html:
        fail(rel + " calls Marketplace an Instagram product")
    if kind in FEE_ANSWER and kind != "menu" and FEE_ANSWER[kind] not in html:
        fail(rel + " visible fee text missing")
    if kind in ("ad", "menu") and "Facebook Marketplace" not in html and "service-fees" not in html and "published-fee" not in html:
        fail(rel + " missing a relevant fee")
    if kind in ("ig", "fb"):
        price = "800" if kind == "ig" else "900"
        if '"price":"%s"' % price not in html:
            fail(rel + " schema price missing")
    if kind == "username":
        if "indicative range is $800–$1,200" not in html and "service-fees" not in html:
            fail(rel + " username page omits the indicative range")
        if re.search(r'"price"\s*:\s*"800"', html) or re.search(r'"price"\s*:\s*"1200"', html):
            fail(rel + " username range marked as a fixed Offer")
    whitelabel = rel in {
        "white-label-agency-brazil/index.html",
        "white-label-agency-saudi-arabia/index.html",
        "pt-br/white-label-agencias-brasil/index.html",
    }
    if kind in NO_FEE_KINDS and 'id="published-fee"' in html and not whitelabel:
        fail(rel + " unexpected published fee")
    if whitelabel:
        for bit in ("$800", "$900", "$1,200", "Business Portfolio", "Marketplace"):
            if bit not in html:
                fail(rel + " white-label fee missing " + bit)
        if rel.startswith("pt-br/") and "não do Instagram" not in html:
            fail(rel + " Portuguese page does not say Marketplace is not Instagram")
        if not rel.startswith("pt-br/") and "not a white-label retainer" not in html:
            fail(rel + " missing white-label scope line")
    if kind == "ad" and "$1,200" not in html:
        fail(rel + " missing Instagram ad-account fee")
    if kind == "menu":
        for bit in ("$800", "$900", "$1,200", "$1,500"):
            if bit not in html:
                fail(rel + " hub menu missing " + bit)
    if kind in ("ig", "fb") and "not a guarantee" not in html:
        fail(rel + " missing no-guarantee line")
    if kind in ("ad", "menu") and "$1,500" not in html:
        fail(rel + " missing separate $1,500 portfolio scope")

if len(holds) != 17:
    fail("expected 17 low-priority country pages, found %d" % len(holds))

KEEP = {
    "index.html": False,
    "fr/index.html": False,
    "contact/index.html": True,
    "services/index.html": True,
    "username/index.html": True,
    "privacy/index.html": True,
    "instagram-account-recovery-italy/index.html": True,
    "instagram-account-recovery-dubai/index.html": True,
    "instagram-account-recovery-uae/index.html": True,
    "facebook-account-recovery-canada/index.html": True,
    "best-username-claim-service-usa/index.html": True,
    "best-username-claim-service-france/index.html": True,
    "best-username-claim-service-netherlands/index.html": True,
    "instagram-username-claim-uk/index.html": True,
    "instagram-no-appeal-button-gulf/index.html": True,
    "pt-br/recuperar-conta-instagram/index.html": True,
    "pt-br/index.html": False,
}
for rel, editorial_ok in KEEP.items():
    html = read(rel)
    if "wa.me/19342012490" not in html:
        fail(rel + " lost WhatsApp")
    if "mailto:team@unbanz.com" not in html:
        fail(rel + " lost email")
    if "cta-hold" in html:
        fail(rel + " was treated as a low-priority country page")
    has_ed = "editorial." in html
    if editorial_ok != has_ed:
        fail(rel + " editorial css presence is %s" % has_ed)
    if rel in ("contact/index.html", "services/index.html", "username/index.html") and "hear-source" not in html:
        fail(rel + " missing source question script")

for absent in ("mexico", "afghanistan", "indonesia"):
    found = [h for h in holds if absent in h]
    if found:
        fail("unexpected pages for " + absent + ": " + ",".join(found))

home = read("index.html")
if "unbanz-inner-v2" in home or "Disallow: /" in read("robots.txt").split("Sitemap")[0] and "User-agent: *\nDisallow: /" in read("robots.txt"):
    fail("preview robots or ZIP stylesheet leaked")
robots = read("robots.txt")
if "User-agent: GPTBot\nAllow: /" not in robots:
    fail("AI bot allow rule changed")

old_sitemap = subprocess.check_output(["git", "show", "HEAD:sitemap.xml"])
new_sitemap = open("sitemap.xml", "rb").read()
if old_sitemap != new_sitemap:
    fail("sitemap.xml changed")
if new_sitemap.count(b"<url>") != 1008:
    fail("sitemap url count is not 1008")
old_robots = subprocess.check_output(["git", "show", "HEAD:robots.txt"])
if old_robots != open("robots.txt", "rb").read():
    fail("robots.txt changed")

llms = read("llms.txt")
if "instagram-username-claim-australia/" in llms:
    fail("llms still lists noindex Australia username page")
if "guides/ad-account-circumventing-systems/" in llms:
    fail("llms still lists alias guide")
if "https://unbanz.com/ad-account-disabled-circumventing-systems-help/" not in llms:
    fail("llms missing canonical circumventing page")
if "https://unbanz.com/instagram-username-claim/" not in llms:
    fail("llms dropped the username hub")
if "Last updated: 2026-11-06" not in llms:
    fail("llms date not updated")

# Every remaining llms URL that maps to a file must not be noindex.
linked = set(re.findall(r"https://unbanz.com(/[^)\s\"]*)", llms))
for url_path in linked:
    rel = url_path.strip("/") + "/index.html"
    if url_path in ("/", ""):
        rel = "index.html"
    if not os.path.exists(rel):
        continue
    head = read(rel)[:4000]
    robots_m = re.search(r'name="robots" content="([^"]*)"', head)
    if robots_m and "noindex" in robots_m.group(1):
        fail("llms lists noindex " + url_path)

print("hold pages", len(holds))
for rel in sorted(holds):
    html = read(rel)
    title = re.search(r"<title>([^<]+)", html).group(1)
    kind = service_kind(rel, title)
    print(" -", hold_country(rel), kind, rel)
if FAILS:
    print("FAILURES", len(FAILS))
    for item in FAILS:
        print(" *", item)
    sys.exit(1)
print("OK")
