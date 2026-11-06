# -*- coding: utf-8 -*-
"""Apply the Nov 6 inner-page editorial layer, llms reconciliation, and country-page CTA policy.

Idempotent. Does not change sitemap.xml, robots.txt, homepage identity, or noindex flags.
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from country_cta_policy import (  # noqa: E402
    FEE_ANSWER,
    FEE_QUESTION,
    NO_ENQUIRY,
    NO_FEE_KINDS,
    fee_html,
    hold_country,
    service_kind,
)

os.chdir(ROOT)

ACTIVE_JS = [
    "assets/site.1b5d9ba8f668.js",
    "assets/site-fr.781dec2b08d1.js",
    "assets/site-nl.17a8755dc80c.js",
    "assets/site-pt.f00ef472e4f3.js",
    "assets/site-es.1d3f7f1253f4.js",
    "assets/cta-note.e97d68bd7a10.js",
    "assets/mail-pick.155b8781830c.js",
]

PHRASES = [
    ("WhatsApp +1 934 201 2490 or team@unbanz.com.", NO_ENQUIRY),
    ("WhatsApp +1 934 201 2490 or email team@unbanz.com.", NO_ENQUIRY),
    ("Contact: WhatsApp +1 934 201 2490 or team@unbanz.com.", ""),
    ("We work over WhatsApp or email in English.", "Unbanz works in English. This page does not open a WhatsApp or email enquiry."),
    ("Message us on WhatsApp or email with", "Have ready:"),
    ("message us on WhatsApp or email", "use the official steps on this page"),
    ("on WhatsApp or email", "without a WhatsApp or email button on this page"),
    ("over WhatsApp or email", "without a WhatsApp or email button on this page"),
    ("pelo WhatsApp ou por e-mail", "sem um botão de WhatsApp ou e-mail nesta página"),
    ("pelo WhatsApp ou e-mail", "sem um botão de WhatsApp ou e-mail nesta página"),
    ("Você nos escreve pelo WhatsApp ou por e-mail com", "Reúna"),
    ("Você envia os dados pelo WhatsApp ou por e-mail.", "Esta página não abre um pedido por WhatsApp ou e-mail."),
]


def sha12(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def patch_js(src, name):
    original = src
    if name.startswith("assets/site.") and "Mobile primary CTA" in src:
        src = src.replace(
            "  try {\n    if (!/^en\\b/i.test(document.documentElement.lang || '')) return;",
            "  try {\n    if (document.body && document.body.classList.contains('cta-hold')) return;\n    if (!/^en\\b/i.test(document.documentElement.lang || '')) return;",
            1,
        )
    needle = "// Contact modal: intercepts WhatsApp CTAs; plain wa.me href stays as no-JS fallback.\n(() => {\n"
    guard = needle + "  if (document.body.classList.contains('cta-hold')) return;\n"
    if needle in src and "cta-hold" not in src[src.find(needle):src.find(needle) + 400]:
        src = src.replace(needle, guard, 1)
    needle2 = "// CTA helpers: trust line in the sticky bar, and one inline CTA after the first section of guides.\n(() => {\n"
    guard2 = needle2 + "  if (document.body.classList.contains('cta-hold')) return;\n"
    if needle2 in src:
        src = src.replace(needle2, guard2, 1)
    if name.startswith("assets/cta-note"):
        src = src.replace(
            "(function () {\n  try {\n",
            "(function () {\n  try {\n    if (document.body && document.body.classList.contains('cta-hold')) return;\n",
            1,
        )
    if name.startswith("assets/mail-pick"):
        src = src.replace(
            "(function () {\n  try {\n    var lang",
            "(function () {\n  try {\n    if (document.body && document.body.classList.contains('cta-hold')) return;\n    var lang",
            1,
        )
    if src == original:
        raise SystemExit("JS patch made no change: " + name)
    return src


def write_hashed(original_rel, text, prefix):
    digest = sha12(text)
    base = os.path.basename(original_rel)
    # site.HASH.js / site-fr.HASH.js / cta-note.HASH.js / mail-pick.HASH.js
    if base.startswith("site-"):
        lang = base.split(".")[0]  # site-fr
        new_rel = "assets/%s.%s.js" % (lang, digest)
    elif base.startswith("site."):
        new_rel = "assets/site.%s.js" % digest
    elif base.startswith("cta-note"):
        new_rel = "assets/cta-note.%s.js" % digest
    elif base.startswith("mail-pick"):
        new_rel = "assets/mail-pick.%s.js" % digest
    else:
        new_rel = "assets/%s.%s.js" % (prefix, digest)
    with open(new_rel, "w", encoding="utf-8") as fh:
        fh.write(text)
    return original_rel.replace("assets/", "/assets/"), "/" + new_rel


def prepare_assets():
    mapping = {}
    for rel in ACTIVE_JS:
        text = open(rel, encoding="utf-8").read()
        if "cta-hold" in text and rel.endswith(sha12(text) + ".js"):
            continue
        patched = patch_js(text, rel)
        old, new = write_hashed(rel, patched, "asset")
        mapping[old] = new
    css = open("assets/editorial.inner.css", encoding="utf-8").read()
    digest = sha12(css)
    css_rel = "assets/editorial.%s.css" % digest
    if not os.path.exists(css_rel) or open(css_rel, encoding="utf-8").read() != css:
        with open(css_rel, "w", encoding="utf-8") as fh:
            fh.write(css)
    return mapping, "/assets/editorial.%s.css" % digest


def strip_anchor(html, href_prefix):
    pattern = r'<a\b[^>]*href="' + href_prefix + r'[^"]*"[^>]*>(.*?)</a>'

    def repl(m):
        inner = re.sub(r"<[^>]+>", "", m.group(1))
        inner = re.sub(r"\s+", " ", inner).strip()
        if re.search(r"whatsapp|e-mail|email|correo|mail|mensagem", inner, re.I) and len(inner) < 90:
            return ""
        return inner

    return re.sub(pattern, repl, html, flags=re.I | re.S)


def scrub_json(obj, kind, canon):
    changed = False

    def walk(o):
        nonlocal changed
        if isinstance(o, dict):
            if o.get("@type") == "ContactPoint":
                if "telephone" in o:
                    o.pop("telephone", None)
                    changed = True
                url = o.get("url")
                if isinstance(url, str) and "wa.me" in url:
                    o.pop("url", None)
                    changed = True
            if o.get("@type") == "Offer" and o.get("description") == "Price depends on the account and the issue.":
                if kind in ("ig", "fb"):
                    o["price"] = "800" if kind == "ig" else "900"
                    o["priceCurrency"] = "USD"
                    o["description"] = FEE_ANSWER[kind]
                    changed = True
                elif kind in ("ad", "menu", "username"):
                    o.pop("price", None)
                    o.pop("priceCurrency", None)
                    o["description"] = FEE_ANSWER[kind]
                    changed = True
            if o.get("@type") == "Question":
                name = o.get("name") or ""
                ans = o.get("acceptedAnswer")
                if isinstance(ans, dict) and re.search(r"contact|contato|reach", name, re.I):
                    text = ans.get("text") or ""
                    if "WhatsApp" in text or "wa.me" in text or "team@unbanz.com" in text:
                        ans["text"] = NO_ENQUIRY
                        changed = True
            if o.get("@type") == "FAQPage" and kind in FEE_ANSWER:
                ents = o.get("mainEntity")
                if isinstance(ents, list):
                    q = FEE_QUESTION[kind]
                    if not any(isinstance(item, dict) and item.get("name") == q for item in ents):
                        ents.append({
                            "@type": "Question",
                            "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": FEE_ANSWER[kind]},
                        })
                        changed = True
            for k, v in list(o.items()):
                if isinstance(v, str) and "wa.me" in v:
                    o[k] = canon
                    changed = True
                else:
                    walk(v)
        elif isinstance(o, list):
            for item in o:
                walk(item)

    walk(obj)
    return changed


def patch_schema(html, kind, canon):
    def repl(m):
        raw = m.group(1)
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            return m.group(0)
        if not scrub_json(data, kind, canon):
            return m.group(0)
        return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "</script>"

    return re.sub(r'<script type="application/ld\+json">(.*?)</script>', repl, html, flags=re.S)


def apply_hold(html, rel, kind):
    if "cta-hold" not in html:
        html = re.sub(r'<body class="([^"]*)"', lambda m: '<body class="%s cta-hold"' % m.group(1), html, count=1)
    for a, b in PHRASES:
        html = html.replace(a, b)
    html = re.sub(r'<div class="hero-cta">[\s\S]*?</div>', "", html)
    html = re.sub(r'<div class="mobile-contact">[\s\S]*?</div>', "", html)
    html = re.sub(
        r'<section class="service-proof[^"]*"[^>]*>[\s\S]*?</section>',
        lambda m: "" if ("wa.me" in m.group(0) or "mailto:" in m.group(0)) else m.group(0),
        html,
    )
    html = re.sub(r'<script src="/assets/mail-pick\.[^"]+" defer></script>', "", html)
    html = html.replace(
        '<a href="mailto:team@unbanz.com?subject=Account%20help">team@unbanz.com</a>',
        '<span class="legal-mail">team@unbanz.com</span>',
    )
    html = re.sub(
        r'<a href="mailto:team@unbanz.com[^"]*">\s*team@unbanz.com\s*</a>',
        '<span class="legal-mail">team@unbanz.com</span>',
        html,
    )
    html = strip_anchor(html, r"https://wa\.me/")
    html = strip_anchor(html, r"mailto:")
    canon_m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    canon = canon_m.group(1) if canon_m else "https://unbanz.com/" + rel.split("/index.html")[0] + "/"
    if 'id="published-fee"' not in html and kind not in NO_FEE_KINDS:
        lang = "pt" if rel.startswith("pt-br/") else "en"
        block = fee_html(kind, lang)
        if block:
            if '<section class="faq-section"' in html:
                html = html.replace('<section class="faq-section"', block + '<section class="faq-section"', 1)
            elif "</main>" in html:
                html = html.replace("</main>", block + "</main>", 1)
    html = patch_schema(html, kind, canon)
    html = re.sub(r"https://wa\.me/19342012490[^\"'\s<]*", canon, html)
    if kind in ("ig", "fb"):
        price = "800" if kind == "ig" else "900"
        if '"price":"%s"' % price not in html:
            offer = {
                "@context": "https://schema.org",
                "@type": "Offer",
                "url": canon,
                "price": price,
                "priceCurrency": "USD",
                "description": FEE_ANSWER[kind],
                "seller": {"@id": "https://unbanz.com/#organization"},
            }
            tag = '<script type="application/ld+json">' + json.dumps(offer, ensure_ascii=False, separators=(",", ":")) + "</script>"
            html = html.replace("</head>", tag + "</head>", 1)
    return html


AEO_USERNAME = '''<section class="aeo-lead container" id="short-answer" data-aeo="2026-11-06"><p class="aeo-kicker">Short answer</p><p><strong>Unbanz claims an Instagram username onto a profile you already control. The price depends on the handle and is agreed before any work. Nothing is charged for asking. If a username claim fails, the published policy is a full refund. Instagram makes the decision. Unbanz is not affiliated with Meta and does not ask for your password.</strong></p><dl class="aeo-facts"><div><dt>Start</dt><dd><a href="/instagram-username-claim/">Instagram username claims</a></dd></div><div><dt>Situation</dt><dd><a href="/inactive-instagram-username/">Inactive handles</a> · <a href="/taken-instagram-username/">Taken handles</a> · <a href="/business-username-claim/">Business names</a></dd></div><div><dt>Readers in</dt><dd><a href="/best-username-claim-service-usa/">the United States</a> · <a href="/best-username-claim-service-canada/">Canada</a> · <a href="/best-username-claim-service-uk/">the United Kingdom</a> · <a href="/best-username-claim-service-france/">France</a> · <a href="/best-username-claim-service-netherlands/">the Netherlands</a></dd></div></dl><p class="aeo-sources">Primary sources: <a href="https://help.instagram.com/">Instagram Help Center</a>, <a href="https://www.instagram.com/hacked/">Instagram’s hacked-account page</a>, <a href="https://www.uspto.gov/trademarks">USPTO trademarks</a>, <a href="https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en">CIPO</a>, <a href="https://www.gov.uk/topic/intellectual-property/trade-marks">UK Intellectual Property Office</a>, <a href="https://www.inpi.fr/">INPI</a>, <a href="https://www.boip.int/en">BOIP</a>. A registered mark is evidence you can send. It is not a promise that Instagram will release a handle.</p></section>'''

AEO_SERVICES = '''<section class="aeo-lead container" id="short-answer" data-aeo="2026-11-06"><p class="aeo-kicker">Start here</p><p><strong>Match the notice to one service. Asking on WhatsApp or email is free, and the price is agreed before work. Instagram username claims are priced after the handle is reviewed.</strong></p><ul><li><a href="/instagram-account-recovery/">Instagram account recovery</a> and <a href="/instagram-unban-service/">Instagram unbans</a></li><li><a href="/facebook-account-recovery/">Facebook account recovery</a> and <a href="/facebook-unban-service/">Facebook unbans</a></li><li><a href="/ad-account-recovery/">Meta ad account recovery</a></li><li><a href="/instagram-username-claim/">Instagram username claims</a></li><li><a href="/meta-appeal-links-and-forms-directory/">Official Meta appeal links</a></li></ul><p class="aeo-sources">Readers in the United States, Canada, the United Kingdom, France, the Netherlands, the UAE and Italy use these same hubs. A country page that does not take enquiries says so on that page. Official starting points: <a href="https://help.instagram.com/">Instagram Help Center</a> and <a href="https://www.facebook.com/business-support-home/">Meta Business Support Home</a>.</p></section>'''

SOURCE_BY_PAGE = {
    "best-username-claim-service-usa/index.html": (
        "United States",
        "https://www.uspto.gov/trademarks",
        "USPTO trademark search",
    ),
    "best-username-claim-service-canada/index.html": (
        "Canada",
        "https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en",
        "Canadian Intellectual Property Office",
    ),
    "best-username-claim-service-uk/index.html": (
        "the United Kingdom",
        "https://www.gov.uk/topic/intellectual-property/trade-marks",
        "UK Intellectual Property Office",
    ),
    "best-username-claim-service-france/index.html": (
        "France",
        "https://www.inpi.fr/",
        "INPI",
    ),
    "best-username-claim-service-netherlands/index.html": (
        "the Netherlands",
        "https://www.boip.int/en",
        "BOIP",
    ),
}


def source_block(place, url, label):
    return (
        '<section class="aeo-lead container" data-aeo="2026-11-06"><p class="aeo-kicker">Primary source</p>'
        '<p>For a brand handle in %s, the official record to check is <a href="%s">%s</a>. '
        'Instagram’s own instructions start at the <a href="https://help.instagram.com/">Instagram Help Center</a>. '
        'A registration is evidence you can show. It does not by itself award the username. '
        'Unbanz prices a username claim after reviewing the handle.</p></section>'
        % (place, url, label)
    )


def insert_aeo(html, rel):
    if 'data-aeo="2026-11-06"' in html:
        return html
    block = None
    if rel == "username/index.html":
        block = AEO_USERNAME
    elif rel == "services/index.html":
        block = AEO_SERVICES
    elif rel in SOURCE_BY_PAGE:
        block = source_block(*SOURCE_BY_PAGE[rel])
    if not block:
        return html
    if '<section class="faq-section"' in html:
        return html.replace('<section class="faq-section"', block + '<section class="faq-section"', 1)
    if "</main>" in html:
        return html.replace("</main>", block + "</main>", 1)
    return html


def fix_about(html):
    html = re.sub(
        r"We also go by Unbanz HQ, and you’ll find us as\s+and\s+\.",
        "We also go by Unbanz HQ. Pages are published by Unbanz. There is no named individual author.",
        html,
        count=1,
    )
    return html


def collect_meta():
    meta = {}
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "assets", "scripts")]
        if "index.html" not in files and root != ".":
            continue
        candidates = []
        if "index.html" in files:
            candidates.append(os.path.join(root, "index.html"))
        if root == "." and os.path.exists("index.html"):
            candidates.append("index.html")
        for path in candidates:
            rel = path[2:] if path.startswith("./") else path
            text = open(path, encoding="utf-8", errors="ignore").read(12000)
            robots = re.search(r'name="robots" content="([^"]*)"', text)
            canon = re.search(r'<link rel="canonical" href="([^"]+)"', text)
            url_path = "/" + rel[: -len("index.html")] if rel.endswith("index.html") else "/" + rel
            if url_path == "/index.html":
                url_path = "/"
            if not url_path.endswith("/"):
                url_path += "/"
            canon_path = None
            if canon:
                c = re.sub(r"^https://unbanz.com", "", canon.group(1).split("?")[0])
                if not c.endswith("/"):
                    c += "/"
                canon_path = c
            meta[url_path] = {
                "noindex": bool(robots and "noindex" in robots.group(1)),
                "canonical": canon_path or url_path,
                "rel": rel,
            }
    return meta


def url_path(url):
    path = re.sub(r"^https://unbanz.com", "", url.split("?")[0].split("#")[0])
    if not path.startswith("/"):
        path = "/" + path
    if not path.endswith("/"):
        path += "/"
    return path


def fix_llms(name, meta):
    lines = open(name, encoding="utf-8").read().splitlines()
    out = []
    removed = 0
    retargeted = 0
    for line in lines:
        urls = re.findall(r"https://unbanz.com[^\s)>\"]+", line)
        if not urls:
            out.append(line)
            continue
        drop = True
        new = line
        for url in urls:
            info = meta.get(url_path(url))
            if not info:
                drop = False
                continue
            if info["noindex"]:
                new = new.replace(url, "")
                removed += 1
            elif info["canonical"] != url_path(url):
                new = new.replace(url, "https://unbanz.com" + info["canonical"])
                retargeted += 1
                drop = False
            else:
                drop = False
        if drop:
            continue
        new = re.sub(r"\[[^\]]*\]\(\)", "", new)
        new = re.sub(r"[ \t]{2,}", " ", new).rstrip()
        if new.strip() in ("-", "- :", "-:"):
            continue
        out.append(new)
    text = "\n".join(out) + "\n"
    note = "Indexable pages only. URLs with a noindex tag are omitted on purpose. Alias URLs are listed at their canonical path. Submission or an HTTP 200 response is not the same as being indexed."
    if note not in text:
        text = text.replace(
            "Last updated: 2026-11-04",
            "Last updated: 2026-11-06\n\n" + note,
            1,
        )
        if "Last updated: 2026-11-06" not in text:
            text = "Last updated: 2026-11-06\n\n" + note + "\n\n" + text
    open(name, "w", encoding="utf-8").write(text)
    return removed, retargeted


def walk_html(js_map, css_href):
    hold_rows = []
    editorial = 0
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "assets", "scripts")]
        pages = [f for f in files if f.endswith(".html")]
        for name in pages:
            path = os.path.join(root, name)
            rel = path[2:] if path.startswith("./") else path
            html = open(path, encoding="utf-8").read()
            original = html
            for old, new in js_map.items():
                html = html.replace(old, new)
            if 'class="service-page' in html and "editorial." not in html:
                html = html.replace("</head>", '<link rel="stylesheet" href="%s"></head>' % css_href, 1)
                editorial += 1
            if rel == "about/index.html":
                html = fix_about(html)
            html = insert_aeo(html, rel)
            country = hold_country(rel)
            if country:
                title_m = re.search(r"<title>([^<]*)</title>", html)
                title = title_m.group(1) if title_m else ""
                kind = service_kind(rel, title)
                html = apply_hold(html, rel, kind)
                hold_rows.append((rel, country, kind))
            if html != original:
                open(path, "w", encoding="utf-8").write(html)
    return editorial, hold_rows


def write_reports(meta, hold_rows, css_href):
    os.makedirs("docs", exist_ok=True)
    sitemap = open("sitemap.xml", encoding="utf-8").read()
    locs = re.findall(r"<loc>([^<]+)</loc>", sitemap)
    # primary page locs: sitemap also has video locs inside the same file? count url blocks
    url_blocks = sitemap.count("<url>")
    indexable = [p for p, info in meta.items() if not info["noindex"] and info["canonical"] == p]
    noindex = [p for p, info in meta.items() if info["noindex"]]
    aliases = [p for p, info in meta.items() if (not info["noindex"]) and info["canonical"] != p]
    loc_set = set()
    for loc in locs:
        if "/assets/" in loc or loc.endswith(".mp4") or loc.endswith(".jpg"):
            continue
        loc_set.add(url_path(loc) if loc.startswith("https://unbanz.com") else loc)
    missing = sorted(p for p in indexable if p not in loc_set and p != "/")
    # homepage loc is https://unbanz.com/ which url_path makes /
    if "/" not in loc_set and "https://unbanz.com/" in sitemap:
        pass
    inv = []
    inv.append("# Indexing inventory — 6 Nov 2026")
    inv.append("")
    inv.append("Built from the files in this commit. Google Search Console and Bing Webmaster were not available, so this is not a coverage percentage and not proof of indexing.")
    inv.append("")
    inv.append("| Check | Result |")
    inv.append("| --- | --- |")
    inv.append("| Sitemap `<url>` blocks | %d |" % url_blocks)
    inv.append("| Sitemap `<loc>` values | %d |" % len(locs))
    inv.append("| HTML paths with `noindex` | %d |" % len(noindex))
    inv.append("| Self-canonical indexable HTML paths | %d |" % len(indexable))
    inv.append("| Indexable alias paths (canonical points elsewhere) | %d |" % len(aliases))
    inv.append("| Self-canonical indexable paths absent from sitemap `<loc>` | %d |" % len(missing))
    inv.append("")
    inv.append("The live audit on 6 Nov 2026 counted 1008 primary page locs and found no hard 1000 cap. This commit does not rebuild or truncate the sitemap. Intentional `noindex` is unchanged.")
    inv.append("")
    inv.append("An HTTP 200 response, an IndexNow submission, or a line in `llms.txt` is not an indexed URL. Confirm indexing in Search Console URL Inspection or Bing Webmaster when those accounts are connected.")
    inv.append("")
    inv.append("## Alias paths")
    inv.append("")
    for p in sorted(aliases):
        inv.append("- `%s` → `%s`" % (p, meta[p]["canonical"]))
    if not aliases:
        inv.append("- None found in this tree.")
    inv.append("")
    inv.append("## Self-canonical indexable paths not listed as a sitemap loc")
    inv.append("")
    if not missing:
        inv.append("None. No sitemap rewrite was required.")
    else:
        for p in missing[:80]:
            inv.append("- `%s`" % p)
        if len(missing) > 80:
            inv.append("- … %d more" % (len(missing) - 80))
    inv.append("")
    inv.append("## Country pages with no enquiry buttons")
    inv.append("")
    if not hold_rows:
        inv.append("None.")
    for rel, country, kind in sorted(hold_rows):
        inv.append("- `%s` — %s — %s" % (rel, country, kind))
    inv.append("")
    inv.append("No public landing page was found for Mexico, Afghanistan, Iran, Iraq or Indonesia. Nothing was invented for those countries.")
    open("docs/indexing-inventory-2026-11-06.md", "w", encoding="utf-8").write("\n".join(inv) + "\n")

    cov = []
    cov.append("# Template coverage — 6 Nov 2026")
    cov.append("")
    cov.append("Editorial stylesheet: `%s`, linked from every `body.service-page` document." % css_href)
    cov.append("")
    cov.append("## Unchanged on purpose")
    cov.append("")
    cov.append("- `/`, `/fr/`, `/nl/`, `/es/`, `/pt-br/` homepage identity (no editorial stylesheet, no `cta-hold`).")
    cov.append("- `404.html`, `/users/`, `/apply/`.")
    cov.append("- `robots.txt` and `sitemap.xml` bytes.")
    cov.append("- Indexed URLs, canonicals, and intentional noindex.")
    cov.append("- Legal pages keep their contact disclosures and enquiry links. They are not country landings.")
    cov.append("- Priority country pages (USA, Canada, UK, France, Netherlands, UAE, Dubai, Italy) keep WhatsApp and email.")
    cov.append("- Gulf pages that also cover the UAE keep WhatsApp and email.")
    cov.append("- Global service hubs (`/services/`, `/contact/`, `/username/`, recovery hubs) keep WhatsApp and email.")
    cov.append("")
    cov.append("## Country-page CTA removals")
    cov.append("")
    cov.append("| Path | Country | Service class | Fee shown |")
    cov.append("| --- | --- | --- | --- |")
    for rel, country, kind in sorted(hold_rows):
        shown = "none" if kind in NO_FEE_KINDS else kind
        cov.append("| `%s` | %s | %s | %s |" % (rel, country, kind, shown))
    cov.append("")
    cov.append("Username rows say the claim is priced after handle review. They do not show $800–$1,200 as a username price.")
    cov.append("Instagram account rows show $800. Facebook profile rows show $900. Ad-account and mixed account rows list $800, $900 and $1,200 by service, and say a Business Portfolio or two-account case is not the $1,200 fee.")
    cov.append("Agency, Snapchat and official-link pages do not gain a new price.")
    cov.append("")
    cov.append("The ZIP preview `robots.txt` and preview index were not deployed.")
    open("docs/template-coverage.md", "w", encoding="utf-8").write("\n".join(cov) + "\n")
    return url_blocks, len(missing), len(aliases)


def main():
    js_map, css_href = prepare_assets()
    # Point the generator constant at the new cta-note asset.
    note = [v for k, v in js_map.items() if "cta-note" in k]
    if note:
        path = "scripts/cta_note.py"
        text = open(path, encoding="utf-8").read()
        text2 = re.sub(r'CTA_ASSET = "/assets/cta-note\.[0-9a-f]+\.js"', 'CTA_ASSET = "%s"' % note[0], text)
        if text2 != text:
            open(path, "w", encoding="utf-8").write(text2)
    editorial, hold_rows = walk_html(js_map, css_href)
    meta = collect_meta()
    llms_stats = []
    for name in ("llms.txt", "llms-full.txt"):
        llms_stats.append((name,) + fix_llms(name, meta))
    blocks, missing, aliases = write_reports(meta, hold_rows, css_href)
    print("js", js_map)
    print("css", css_href)
    print("editorial_links_added", editorial)
    print("hold_pages", len(hold_rows))
    for row in sorted(hold_rows):
        print(" ", row[1], row[2], row[0])
    print("llms", llms_stats)
    print("sitemap_url_blocks", blocks, "missing_self_canonical", missing, "aliases", aliases)


if __name__ == "__main__":
    main()
