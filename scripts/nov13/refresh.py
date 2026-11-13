# -*- coding: utf-8 -*-
"""Nov 13 2026 freshness + SEO/AEO pass. Idempotent-ish; run once from repo root."""
import re, glob, json, os, html as H

TODAY = "2026-11-13"
ROOT = os.getcwd()
changed = set()

SKIP_PREFIX = ("users/", "api/", "node_modules/", ".git/", "scripts/", "marketing/", "research/")

def files():
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith(SKIP_PREFIX) or f == "404.html":
            continue
        yield f

# ---------- visible date text ----------
OCT2NOV = [("October", "November"), ("octobre", "novembre"), ("octubre", "noviembre"),
           ("outubro", "novembro"), ("Oktober", "November"), ("oktober", "november"),
           ("ottobre", "novembre"), ("Ekim", "Kasım"), ("أكتوبر", "نوفمبر")]

def new_date_text(t):
    m = re.match(r"\s*(\d{4})年(\d{1,2})月(\d{1,2})日", t)
    if m:
        return "2026年11月13日"
    if not re.search(r"2026", t):
        return None
    t2 = re.sub(r"^(\D*?)\d{1,2}", lambda m: m.group(1) + "13", t, count=1)
    for a, b in OCT2NOV:
        t2 = t2.replace(a, b)
    if not re.search(r"(November|novembre|noviembre|novembro|november|Kasım|نوفمبر)", t2):
        return None
    return t2

UPD_KW = re.compile(r"(Updated|Last updated:?|Bijgewerkt op|Mis à jour le|Aktualisiert am|Aggiornato il|Actualizado el|Atualizado em|Güncellendi:?|تحديث|更新(?:日期)?[:：]?)\s*$")
TIME_RE = re.compile(r'<time datetime="(\d{4}-\d{2}-\d{2})">([^<]*)</time>')

def refresh_dates(s):
    def tr(m):
        pre = re.sub(r"<[^>]+>", "", s[max(0, m.start() - 80):m.start()])
        if not UPD_KW.search(pre):
            return m.group(0)
        nt = new_date_text(m.group(2))
        if nt is None:
            return m.group(0)
        return f'<time datetime="{TODAY}">{nt}</time>'
    s = TIME_RE.sub(tr, s)
    s = re.sub(r'("dateModified":\s?")\d{4}-\d{2}-\d{2}', r"\g<1>" + TODAY, s)
    s = re.sub(r'((?:article:modified_time|og:updated_time)" content=")\d{4}-\d{2}-\d{2}', r"\g<1>" + TODAY, s)
    s = s.replace("Last updated: October 2026", "Last updated: November 2026")
    return s

# ---------- guarantee wording (EN only, timing) ----------
GUAR = "Guaranteed 3–7 days from the day we start, with a 100% refund if it fails"
GUAR_SUBS = [
    (re.compile(r"Work usually takes 3–7 days from the day we start(?:,| —|;)? (?:but )?(?:timing|that) is not guaranteed(?:,)? and [A-Z][A-Za-z]+ makes the final decision"), GUAR),
    (re.compile(r"Work usually takes 3–7 days from the day we start(?:,|;) not guaranteed(?:,|;) (?:and )?[A-Z][A-Za-z]+ makes the final decision"), GUAR),
    (re.compile(r"Work usually takes 3–7 days from the day we start, but timing is not guaranteed"), GUAR),
    (re.compile(r"Work usually takes 3–7 days, not guaranteed"), "Guaranteed 3–7 days"),
    (re.compile(r"Usually 3–7 days from the day we start; not guaranteed"), "Guaranteed 3–7 days from the day we start"),
    (re.compile(r"(?:The platform|YouTube|TikTok|Meta) makes the final decision; usually 3–7 days, not guaranteed"), "Guaranteed 3–7 days, with a 100% refund if it fails"),
    (re.compile(r"Most cases take 3–7 days, though that is not guaranteed, and Meta makes the final decision"), "Cases are guaranteed within 3–7 days, with a 100% refund if it fails"),
    (re.compile(r"usually 3–7 days but no guarantee"), "guaranteed 3–7 days"),
    (re.compile(r"Usually 3–7 days, not guaranteed"), "Guaranteed 3–7 days"),
    (re.compile(r"Usual, not guaranteed"), "Guaranteed"),
]

def is_en(s):
    m = re.search(r'<html[^>]*lang="([^"]+)"', s)
    return (m.group(1) if m else "en").lower().startswith("en")

def guarantee(s):
    for rx, rep in GUAR_SUBS:
        s = rx.sub(rep, s)
    return s

# ---------- FAQ injection ----------
def add_faq(s, url, qas):
    """Prepend visible <details> and append to FAQPage JSON-LD (create if missing)."""
    vis = "".join(
        f'<details><summary>{H.escape(q, quote=False)}<span aria-hidden="true">+</span></summary><p>{H.escape(a, quote=False)}</p></details>'
        for q, a in qas if q not in s)
    if not vis:
        return s
    if '<div class="simple-faq">' in s:
        s = s.replace('<div class="simple-faq">', '<div class="simple-faq">' + vis, 1)
    else:
        block = ('<section class="faq-section" id="faq-2026"><div class="container faq-layout"><div class="faq-intro">'
                 '<p class="eyebrow">QUICK ANSWERS</p><h2>Good to know.</h2></div><div class="simple-faq">' + vis + '</div></div></section>')
        s = s.replace("</main>", block + "</main>", 1)
    ents = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas]
    done = False
    def jl(m):
        nonlocal done
        raw = m.group(1)
        try:
            d = json.loads(raw)
        except Exception:
            return m.group(0)
        targets = d.get("@graph", [d]) if isinstance(d, dict) else d
        for node in targets:
            if isinstance(node, dict) and node.get("@type") == "FAQPage" and not done:
                names = {e.get("name") for e in node.get("mainEntity", [])}
                node["mainEntity"] = [e for e in ents if e["name"] not in names] + node.get("mainEntity", [])
                done = True
                return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + "</script>"
        return m.group(0)
    s = re.sub(r'<script type="application/ld\+json">(.*?)</script>', jl, s, flags=re.S)
    if not done:
        d = {"@context": "https://schema.org", "@type": "FAQPage", "@id": url + "#faq", "url": url, "mainEntity": ents}
        s = s.replace("</head>", '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + "</script></head>", 1)
    return s

SIX = "6-month guarantee: if the account is banned again within 6 months, we recover it free or refund 100%."
TERMS = "Paid upfront by card, guaranteed 3–7 days from the day we start, 100% refund if it fails, and we never need your password."

PAGES = {
 "instagram-account-recovery": dict(
   title=("Instagram Account Recovery Service: Disabled &amp; Hacked", "Instagram Account Recovery Service 2026: Disabled &amp; Hacked"),
   desc="Disabled, suspended or hacked Instagram account? Recovery for $800, guaranteed 3–7 days, 100% refund if it fails. Your password stays with you.",
   faq=[("How do I recover a disabled Instagram account in 2026?", "Request a review from the notice at login or in Account Status; Instagram does not take appeals by email or phone. If the appeal is rejected or never answered, Unbanz handles the case for $800. " + TERMS),
        ("How much does Instagram account recovery cost?", "$800 per Instagram account, or $1,500 for an Instagram and Facebook account together. " + TERMS + " " + SIX)]),
 "facebook-account-recovery": dict(
   title=("Facebook Account Recovery Service: Disabled &amp; Hacked", "Facebook Account Recovery Service 2026: Disabled &amp; Hacked"),
   desc="Facebook account disabled, suspended or hacked? Profile recovery for $900, guaranteed 3–7 days, 100% refund if it fails. No passwords needed.",
   faq=[("How do I recover a disabled Facebook account in 2026?", "Open the notice Facebook shows at login (or Accounts Center) and request a review there within the window Meta gives. If the appeal is rejected or stuck, Unbanz handles the case for $900. " + TERMS),
        ("How much does Facebook account recovery cost?", "$900 per Facebook profile, $1,500 for Instagram and Facebook together, and $600 per Facebook Page. " + TERMS + " " + SIX)]),
 "ad-account-recovery": dict(
   title=("Meta Ad Account Disabled or Restricted? Recovery Service", "Meta Ad Account Disabled or Restricted? Recovery Service 2026"),
   desc="Meta ad account disabled or restricted, or Business Portfolio blocked? Ad account recovery $1,200, Business Portfolio $1,500. Guaranteed 3–7 days.",
   faq=[("How do I get a disabled Meta ad account back in 2026?", "An admin requests a review in Business Support Home or Account Quality after fixing the cause (billing, domain, policy). If the review is rejected, Unbanz handles the case: $1,200 per ad account, $1,500 per Business Portfolio. " + TERMS),
        ("How much does ad account recovery cost?", "$1,200 for one Instagram or Facebook ad account and $1,500 for a Meta Business Portfolio. " + TERMS + " " + SIX)]),
 "username": dict(
   title=("Username Claim Service: Inactive, Taken &amp; OG Handles", "Username Claim Service 2026: Inactive, Taken &amp; OG Handles"),
   desc="Claim inactive or taken Instagram and Facebook handles for a flat $1,200 per username. 100% refund if the claim fails. Your password stays with you.",
   faq=[("How do I get an inactive or taken Instagram username in 2026?", "Instagram does not sell usernames, and buying an account breaks its terms. Unbanz claims the handle onto your own profile through Instagram’s own processes for a flat $1,200 per handle, paid upfront, with a 100% refund if the claim fails. We never need your password.")]),
 "tiktok-unban-service": dict(
   title=("TikTok Unban Service: Banned TikTok Account Recovery ($900, 100% Refund)", "TikTok Unban Service 2026: Banned Account Recovery ($900)"),
   desc="Unbanz recovers banned and permanently banned TikTok accounts for $900, paid upfront, 100% refund if it fails. No passwords. Guaranteed 3–7 days.",
   faq=[("How do I get a banned TikTok account back in 2026?", "Appeal from the ban notice in the TikTok app (Inbox > System notifications) first. If the appeal is rejected or the ban is permanent, Unbanz handles the case for $900. " + TERMS)]),
 "tiktok-account-help": dict(
   title=("TikTok Account Banned or Suspended? Help, Guides and Recovery ($900)", "TikTok Account Banned? 2026 Help, Guides and Recovery ($900)"),
   desc="Banned, suspended or hacked TikTok account? Official appeal links, notices explained, and TikTok ban recovery for $900 upfront with a 100% refund.",
   faq=[("How much does TikTok ban recovery cost?", "$900 per TikTok account. " + TERMS + " " + SIX)]),
 "whatsapp-banned-number": dict(
   title=("WhatsApp Number Banned? How to Request a Review | Unbanz", "WhatsApp Number Banned? How to Get It Back (2026) | Unbanz"),
   desc="“This account is not allowed to use WhatsApp”? How to request a review in 2026, and WhatsApp ban recovery by Unbanz for $600 with a 100% refund.",
   faq=[("How do I get a banned WhatsApp number back in 2026?", "Tap Request a review on the ban screen in the official WhatsApp app and explain how you use the number. If the review is rejected, Unbanz handles WhatsApp ban cases for $600. " + TERMS),
        ("How much does WhatsApp ban recovery cost?", "$600 per WhatsApp number. " + TERMS + " " + SIX)]),
 "youtube-channel-recovery-service": dict(
   title=("YouTube Channel Recovery Service: Terminated Channels ($1,200, 100% Refund)", "YouTube Channel Recovery Service 2026: Terminated ($1,200)"),
   desc="Unbanz recovers terminated and hacked YouTube channels for $1,200, paid upfront, 100% refund if it fails. No passwords. Guaranteed 3–7 days.",
   faq=[("How do I recover a terminated YouTube channel in 2026?", "Submit the termination appeal from YouTube Studio or the appeal form linked in the termination email. If it is rejected, Unbanz handles the case for $1,200 per channel. " + TERMS + " " + SIX)]),
 "facebook-page-recovery": dict(
   title=("Facebook Page Recovery: Lost Admin or Page Held by Another Business ($600)", "Facebook Page Recovery 2026: Lost Admin or Page Taken ($600)"),
   desc="Lost admin access, or another Business Portfolio holds your Facebook Page? Official routes and Page recovery for $600 per Page, 100% refund if it fails.",
   faq=[("How do I get my Facebook Page back in 2026?", "If you still have any admin, restore access in Business Settings or Page access. If not, Unbanz recovers the Page for $600 per Page. " + TERMS)]),
 "pricing": dict(
   title=("Pricing: Account Recovery and Username Claims | Unbanz", "Unbanz Pricing 2026: Account Recovery and Username Fees"),
   desc="Instagram $800, Facebook $900, both $1,500, ad account $1,200, Business Portfolio $1,500, username $1,200, TikTok $900, YouTube $1,200, WhatsApp $600.",
   faq=[("How much does it cost to recover a banned account in 2026?", "Instagram $800, Facebook $900, Instagram and Facebook together $1,500, Facebook Page $600, ad account $1,200, Business Portfolio $1,500, username claim $1,200, TikTok $900, YouTube $1,200, WhatsApp $600. " + TERMS),
        ("Is there a guarantee?", "Yes. Every case is guaranteed within 3–7 days from the day we start, with a 100% refund if it fails. " + SIX),
        ("Do I pay a deposit or the full price?", "The full fee upfront by card through a secure checkout link, once you agree. No deposits or split payments. Nothing is charged for asking.")]),
 "": dict(
   faq=[("How much does Unbanz cost in 2026?", "Instagram $800, Facebook $900, both $1,500, ad account $1,200, Business Portfolio $1,500, username $1,200, TikTok $900, YouTube $1,200, Facebook Page $600, WhatsApp $600. " + TERMS + " " + SIX)]),
}

def set_desc(s, new):
    m = re.search(r'<meta name="description" content="([^"]*)"', s)
    if not m:
        return s
    old = m.group(1)
    newe = H.escape(new, quote=True).replace("&#x27;", "'")
    s = s.replace(f'content="{old}"', f'content="{newe}"')
    s = s.replace(json.dumps(H.unescape(old), ensure_ascii=False)[1:-1], json.dumps(new, ensure_ascii=False)[1:-1])
    return s

def set_title(s, old, new):
    s = s.replace(old, new)
    s = s.replace(H.unescape(old), H.unescape(new))
    return s

def pricing_extras(s):
    if "WhatsApp number banned" in s and "Instagram + Facebook together" in s:
        return s
    rows = ('<tr><td><a href="/instagram-account-recovery/">Instagram + Facebook together</a></td><td><strong>$1,500</strong></td><td>One Instagram account and one Facebook profile.</td></tr>')
    s = s.replace('<tr><td><a href="/facebook-page-recovery/">Facebook Page recovery</a>', rows + '<tr><td><a href="/facebook-page-recovery/">Facebook Page recovery</a>', 1)
    wa = ('<tr><td><a href="/whatsapp-banned-number/">WhatsApp number banned</a></td><td><strong>$600</strong></td><td>One number.</td></tr>')
    s = s.replace('</tbody></table></div><p><strong>How payment works:', wa + '</tbody></table></div><p><strong>How payment works:', 1)
    s = s.replace("Fixed fees per account: Instagram $800, Facebook $900, Facebook Page $600, ad accounts $1,200, usernames $1,200, TikTok $900, YouTube $1,200.",
                  "Fixed fees per account: Instagram $800, Facebook $900, Instagram + Facebook $1,500, Facebook Page $600, ad accounts $1,200, Business Portfolio $1,500, usernames $1,200, TikTok $900, YouTube $1,200, WhatsApp $600.")
    s = s.replace('<p class="eyebrow">PRICING</p><h1>', f'<p class="eyebrow">PRICING</p><h1>', 1)
    s = s.replace("Send the account.<br>Know the price.</h1>", f'Send the account.<br>Know the price.</h1><p class="guide-meta">Updated <time datetime="{TODAY}">13 November 2026</time></p>', 1) if 'class="guide-meta"' not in s else s
    s = s.replace("$900 is one banned TikTok account. $1,200 is one terminated YouTube channel.",
                  "$900 is one banned TikTok account. $1,200 is one terminated YouTube channel. $600 is one banned WhatsApp number. $1,500 covers one Instagram account and one Facebook profile together.")
    s = s.replace("<p>Upfront, by card. Nothing is charged for asking. If the case fails, you get a full 100% refund. This applies to every service on this page.</p>",
                  "<p>Upfront, by card. Nothing is charged for asking. If the case fails, you get a full 100% refund. This applies to every service on this page.</p><p><strong>6-month guarantee:</strong> if a recovered account is banned again within 6 months, we recover it free or refund 100%.</p>")
    # JSON-LD offers
    def jl(m):
        try:
            d = json.loads(m.group(1))
        except Exception:
            return m.group(0)
        hit = False
        for node in (d.get("@graph", [d]) if isinstance(d, dict) else d):
            if isinstance(node, dict) and node.get("@type") == "OfferCatalog":
                items = node.setdefault("itemListElement", [])
                names = {i.get("name") for i in items}
                for nm, pr, url in [("Instagram and Facebook account together", "1500", "https://unbanz.com/instagram-account-recovery/"),
                                    ("WhatsApp number banned", "600", "https://unbanz.com/whatsapp-banned-number/")]:
                    if nm not in names:
                        items.append({"@type": "Offer", "name": nm, "price": pr, "priceCurrency": "USD", "url": url, "seller": {"@id": "https://unbanz.com/#organization"}})
                hit = True
        if not hit:
            return m.group(0)
        return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + "</script>"
    s = re.sub(r'<script type="application/ld\+json">(.*?)</script>', jl, s, flags=re.S)
    if '"dateModified"' not in s:
        s = s.replace('"@type": "WebPage",', f'"@type": "WebPage", "dateModified": "{TODAY}",', 1).replace('"@type":"WebPage",', f'"@type":"WebPage","dateModified":"{TODAY}",', 1)
    return s

for f in files():
    with open(f, encoding="utf-8") as fh:
        s0 = fh.read()
    s = refresh_dates(s0)
    if is_en(s):
        s = guarantee(s)
    slug = f[:-len("index.html")].rstrip("/") if f.endswith("index.html") else None
    if slug in PAGES:
        cfg = PAGES[slug]
        url = "https://unbanz.com/" + (slug + "/" if slug else "")
        if "title" in cfg:
            s = set_title(s, *cfg["title"])
        if "desc" in cfg:
            s = set_desc(s, cfg["desc"])
        if slug == "pricing":
            s = pricing_extras(s)
        s = add_faq(s, url, cfg["faq"])
        if '"dateModified"' not in s:
            s = re.sub(r'("@type":\s?"WebPage",)', r'\1"dateModified":"' + TODAY + '",', s, count=1)
    if s != s0:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(s)
        changed.add(f)

def url_for(f):
    return "https://unbanz.com/" + (f[:-len("index.html")] if f.endswith("index.html") else f)

curls = {url_for(f) for f in changed}

# ---------- sitemaps ----------
for sm in ["sitemap.xml", "sitemap-en.xml", "sitemap-intl.xml", "sitemap-images.xml"]:
    if not os.path.exists(sm):
        continue
    x = open(sm, encoding="utf-8").read()
    def lm(m):
        if m.group(1) in curls:
            return m.group(0).replace(m.group(2), TODAY)
        return m.group(0)
    x2 = re.sub(r"<loc>([^<]+)</loc>(?:(?!</url>).)*?<lastmod>([^<]+)</lastmod>", lm, x, flags=re.S)
    if x2 != x:
        open(sm, "w", encoding="utf-8").write(x2); changed.add(sm)
x = open("sitemap-index.xml", encoding="utf-8").read()
x2 = re.sub(r"<lastmod>[^<]+</lastmod>", f"<lastmod>{TODAY}</lastmod>", x)
open("sitemap-index.xml", "w", encoding="utf-8").write(x2); changed.add("sitemap-index.xml")

open("scripts/nov13/changed_urls.txt", "w").write("\n".join(sorted(curls)) + "\n")
print(len(changed), "files changed;", len(curls), "page URLs")
