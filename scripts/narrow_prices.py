# -*- coding: utf-8 -*-
"""Replace the all-services fee block with the fee for that page, and drop the country picker script."""
import hashlib
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from country_cta_policy import FEE_ANSWER

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

HUB = (
    "$800 is one disabled, suspended or hacked Instagram account. "
    "$800 is a separate fee for one Facebook Marketplace case. Marketplace is a Facebook product, not part of the Instagram fee. "
    "$900 is one disabled, suspended or hacked Facebook profile and does not include Marketplace. "
    "$1,200 is one Instagram ad-account restriction. "
    "A Business Portfolio case or more than one account is a separate scope at $1,500. "
    "An Instagram username claim is priced after the handle is reviewed. "
    "For a standard claim assessment the indicative range is $800–$1,200. "
    "That range is not a fixed price and not a guarantee. Complex handles are quoted separately. "
    "The platform decides the outcome. This is not a guarantee. Payment is by card."
)
MKT = (
    "The published fee for this service is $800 for one Facebook Marketplace case. "
    "Marketplace is a Facebook product. It is not the fee for an Instagram account. "
    "Facebook decides the outcome. This is not a guarantee. "
    "Scope is confirmed in writing before payment. Payment is by card."
)
PORT = (
    "The published fee for this service is $1,500 for a Business Portfolio case or more than one account. "
    "It is not the $1,200 fee for one Instagram ad-account restriction. "
    "The platform decides the outcome. This is not a guarantee. "
    "Scope is confirmed in writing before payment. Payment is by card."
)
TEXT = {
    "ig": FEE_ANSWER["ig"],
    "fb": FEE_ANSWER["fb"],
    "ad": FEE_ANSWER["ad"],
    "username": FEE_ANSWER["username"],
    "marketplace": MKT,
    "portfolio": PORT,
    "hub": HUB,
    "menu": HUB,
}

def kind_for(rel, title):
    s = (rel + " " + title).lower()
    base = rel[:-len("index.html")].strip("/") if rel.endswith("index.html") else rel
    if base in ("services", "pricing", "contact", "unban", "unban-pricing"):
        return "hub"
    if "white-label" in s or "agencia" in s or "agências" in s or "agency-client" in s:
        return "hub"
    if any(x in s for x in ("portfolio", "business-manager", "business-portfolio", "two-account")):
        return "portfolio"
    if "marketplace" in s:
        return "marketplace"
    if any(x in s for x in ("username", "gebruikersnaam", "pseudo", "nome-de-usuario", "nombre-de-usuario")):
        return "username"
    if any(x in s for x in ("ad-account", "ads-account", "conta-de-anuncio", "compte-publicitaire", "advertentieaccount")):
        return "ad"
    if "facebook" in s and "instagram" not in s:
        return "fb"
    if "instagram" in s:
        return "ig"
    return "hub"

def section(kind):
    title = "Published fees." if kind in ("hub", "menu") else "Published fee."
    return (
        '<section class="service-fees container" id="service-fees"><p class="eyebrow">SERVICE FEES</p><h2>%s</h2><p>%s</p></section>'
        % (title, TEXT[kind])
    )

PT_HUB = (
    "$800 é uma conta do Instagram desativada, suspensa ou hackeada. "
    "$800 é um caso separado do Marketplace do Facebook. O Marketplace é um produto do Facebook, não do Instagram. "
    "$900 é um perfil do Facebook e não inclui o Marketplace. "
    "$1,200 é uma restrição de conta de anúncios do Instagram. "
    "Um Business Portfolio ou mais de uma conta é um escopo separado a $1,500. "
    "Um nome de usuário do Instagram tem o preço definido depois da análise do @. "
    "Para uma avaliação padrão, a faixa indicativa é $800–$1,200. Essa faixa não é um preço fixo nem uma garantia. "
    "A plataforma decide o resultado. Isto não é uma garantia."
)

def narrow(html, kind):
    text = TEXT.get(kind, HUB)
    html = re.sub(r'<section class="service-fees[\s\S]*?</section>', section(kind), html, count=1)
    def repl_p(m):
        inner = m.group(2)
        if any(tok in inner for tok in ("$800", "$900", "$1,200", "$1,500", "indicative range", "priced after the handle", "faixa indicativa")):
            use = PT_HUB if ("não do Instagram" in inner or "Taxas publicadas" in html) else text
            return m.group(1) + use + m.group(3)
        return m.group(0)
    if 'id="published-fee"' in html:
        start = html.find('<section class="published-fee')
        end = html.find("</section>", start)
        block = html[start:end]
        block = re.sub(r"(<p>)([\s\S]*?)(</p>)", repl_p, block)
        html = html[:start] + block + html[end:]
        # one fee section is enough
        html = re.sub(r'<section class="service-fees[\s\S]*?</section>', "", html, count=1)
    def repl_desc(m):
        desc = m.group(1)
        if any(tok in desc for tok in ("nationality", "WhatsApp is offered", "not part of this Instagram fee", "indicative range", "separate scope at $1,500", "Marketplace is a Facebook product")):
            if any(tok in desc for tok in ("$800", "$900", "$1,200", "$1,500", "priced after", "indicative")):
                return '"description":"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
        return m.group(0)
    html = re.sub(r'"description":"((?:\\.|[^"\\])*)"', repl_desc, html)
    return html

css = open("assets/contact-policy.css", encoding="utf-8").read()
js = open("assets/contact-policy.js", encoding="utf-8").read()
css_hash = hashlib.sha256(css.encode()).hexdigest()[:12]
js_hash = hashlib.sha256(js.encode()).hexdigest()[:12]
css_rel = "assets/contact-policy.%s.css" % css_hash
js_rel = "assets/contact-policy.%s.js" % js_hash
open(css_rel, "w", encoding="utf-8").write(css)
open(js_rel, "w", encoding="utf-8").write(js)
old_css = "/assets/contact-policy.83b2ae81d12e.css"
old_js = "/assets/contact-policy.9556b5b6dd18.js"
new_css = "/" + css_rel
new_js = "/" + js_rel

n = 0
narrowed = 0
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "assets", "scripts", "users")]
    for name in files:
        if not name.endswith(".html"):
            continue
        path = os.path.join(root, name)
        rel = path[2:] if path.startswith("./") else path
        html = open(path, encoding="utf-8").read()
        orig = html
        if "service-fees" in html or "published-fee" in html:
            title = re.search(r"<title>([^<]*)", html)
            html = narrow(html, kind_for(rel, title.group(1) if title else ""))
            narrowed += 1
        html = html.replace(old_css, new_css).replace(old_js, new_js)
        if html != orig:
            open(path, "w", encoding="utf-8").write(html)
            n += 1
print("updated", n, "fee pages", narrowed)
print(new_css, new_js)
