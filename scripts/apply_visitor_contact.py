# -*- coding: utf-8 -*-
"""Restore email CTAs, gate WhatsApp by visitor country, and state service fees."""
import hashlib
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

def sha12(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]

css = open("assets/contact-policy.css", encoding="utf-8").read()
js = open("assets/contact-policy.js", encoding="utf-8").read()
css_name = "assets/contact-policy.%s.css" % sha12(css)
js_name = "assets/contact-policy.%s.js" % sha12(js)
open(css_name, "w", encoding="utf-8").write(css)
open(js_name, "w", encoding="utf-8").write(js)
CSS_HREF = "/" + css_name
JS_SRC = "/" + js_name
MAIL = '<script src="/assets/mail-pick.b0ade601709f.js" defer></script>'
HEAR = '<script src="/assets/hear-source.5c7315a4962e.js" defer></script>'
POLICY = '<link rel="stylesheet" href="%s"><script src="%s" defer></script>' % (CSS_HREF, JS_SRC)

OLD_USER = (
    "An Instagram username claim is priced after the handle is reviewed. "
    "There is no flat public username price. A recovery fee for a disabled account is a different "
    "service and is not a username price."
)
NEW_USER = (
    "An Instagram username claim is priced after the handle is reviewed. "
    "For a standard claim assessment the indicative range is $800–$1,200. "
    "That range is not a fixed price and not a guarantee. Complex handles are quoted separately."
)
OLD_PORT = "Those are quoted separately and are not reduced to $1,200."
NEW_PORT = "A Business Portfolio case or more than one account is a separate scope at $1,500, not a discount of the $1,200 fee."
OLD_PORT2 = "Business Portfolio work and a two-account case are different services and are not this $800 fee."
NEW_PORT2 = "A Business Portfolio case or more than one account is a separate scope at $1,500 and is not this $800 fee."
OLD_PORT3 = "Business Portfolio work and a two-account case are different services and are not this $900 fee."
NEW_PORT3 = "A Business Portfolio case or more than one account is a separate scope at $1,500 and is not this $900 fee."

FEE_BLOCK = (
    '<section class="service-fees container" id="service-fees">'
    '<p class="eyebrow">SERVICE FEES</p>'
    '<h2>Published fees.</h2>'
    '<p>$800 is one disabled, suspended or hacked Instagram account. '
    '$800 is a separate fee for one Facebook Marketplace case. Marketplace is a Facebook product, not part of the Instagram fee. '
    '$900 is one disabled, suspended or hacked Facebook profile and does not include Marketplace. '
    '$1,200 is one Instagram ad-account restriction. '
    'A Business Portfolio case or more than one account is a separate scope at $1,500. '
    'An Instagram username claim is priced after the handle is reviewed. For a standard claim assessment the indicative range is $800–$1,200. '
    'That range is not a fixed price and not a guarantee. Complex handles are quoted separately. '
    'None of these fees is a country discount. The platform decides the outcome. '
    'WhatsApp is offered in the United States, Canada, the United Kingdom, France, the Netherlands, the United Arab Emirates and Italy. Elsewhere, use email.</p>'
    '</section>'
)

SKIP_FEE = re.compile(
    r"appeal-links|onde-denunciar|falar-com|sextor|crime|golpe|news|snapchat",
    re.I,
)
COMMERCIAL = re.compile(
    r"(account-recovery|unban-service|username-claim|ad-account|^username/|^services/|^pricing/|^unban-pricing/|^contact/|white-label|marketplace)",
    re.I,
)

def git_show(rel):
    try:
        return subprocess.check_output(["git", "show", "bc3800e0:" + rel], stderr=subprocess.DEVNULL).decode("utf-8")
    except subprocess.CalledProcessError:
        return ""

def grab(html, pattern):
    m = re.search(pattern, html, re.S)
    return m.group(0) if m else ""

def restore_contact(rel, html):
    old = git_show(rel)
    if not old:
        return html
    if "cta-hold" in html:
        html = html.replace(' cta-hold', '', 1)
    if "hero-cta" not in html:
        block = grab(old, r'<div class="hero-cta">[\s\S]*?</div>')
        if block:
            html = re.sub(
                r'(<section class="service-hero"><div class="container">[\s\S]*?</p>)',
                r'\1' + block,
                html,
                count=1,
            )
    if "mobile-contact" not in html:
        block = grab(old, r'<div class="mobile-contact">[\s\S]*?</div>')
        if block:
            html = html.replace("</body>", block + "</body>", 1)
    if "service-proof" not in html:
        block = grab(old, r'<section class="service-proof[\s\S]*?</section>')
        if block and "</main>" in html:
            html = html.replace("</main>", block + "</main>", 1)
    html = re.sub(
        r'<span class="legal-mail">team@unbanz.com</span>',
        '<a href="mailto:team@unbanz.com?subject=Account%20help">team@unbanz.com</a>',
        html,
    )
    if "mail-pick." not in html:
        html = html.replace("</head>", MAIL + HEAR + "</head>", 1)
    return html

def ensure_assets(html):
    if CSS_HREF not in html:
        html = html.replace("</head>", POLICY + "</head>", 1)
    return html

def fee_text(html):
    html = html.replace(OLD_USER, NEW_USER)
    html = html.replace(OLD_PORT, NEW_PORT)
    html = html.replace(OLD_PORT2, NEW_PORT2)
    html = html.replace(OLD_PORT3, NEW_PORT3)
    return html

def maybe_fee_block(rel, html):
    if 'id="service-fees"' in html or 'id="published-fee"' in html:
        return html
    if SKIP_FEE.search(rel):
        return html
    if not COMMERCIAL.search(rel):
        return html
    if "</main>" in html:
        return html.replace("</main>", FEE_BLOCK + "</main>", 1)
    return html

changed = 0
restored = 0
fees = 0
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "assets", "scripts", "users")]
    for name in files:
        if not name.endswith(".html"):
            continue
        path = os.path.join(root, name)
        rel = path[2:] if path.startswith("./") else path
        if rel.startswith("users/") or rel.startswith("api/"):
            continue
        html = open(path, encoding="utf-8").read()
        original = html
        if "cta-hold" in html or "legal-mail" in html:
            html = restore_contact(rel, html)
            if html != original:
                restored += 1
        before_fee = html
        html = fee_text(html)
        html = maybe_fee_block(rel, html)
        if html != before_fee:
            fees += 1
        html = ensure_assets(html)
        if html != original:
            open(path, "w", encoding="utf-8").write(html)
            changed += 1
print("css", CSS_HREF)
print("js", JS_SRC)
print("changed", changed, "restored", restored, "fee_touch", fees)
