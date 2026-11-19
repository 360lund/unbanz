"""Nov 19 2026: build US/UK/CA hubs + TikTok/WhatsApp x country pages + NL WhatsApp page.
Shell (head scripts, header, hx-help, hx-steps, testimonials, footer) is copied from an existing
country page so assets, CTA note, contact policy and tracking stay identical."""
import os, re, json, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from content import PAGES
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
BASE = 'https://unbanz.com/'
TODAY = '2026-11-19'
OGLOC = {'en-US': 'en_US', 'en-GB': 'en_GB', 'en-CA': 'en_CA', 'nl-NL': 'nl_NL'}
IMG = {'tiktok': 'tiktok.webp', 'whatsapp': 'whatsapp.webp', 'ig_disabled': 'instagram-glass-600.webp'}

def esc(t): return html.escape(t, quote=True)
def strip(t): return re.sub(r'<[^>]+>', '', t)

def cut(s, start, end_tok, from_pos=0):
    i = s.index(start, from_pos); j = s.index(end_tok, i) + len(end_tok); return s[i:j]

def build(p):
    tpl = open(os.path.join(ROOT, p['template'], 'index.html'), encoding='utf-8').read()
    nl = p['locale'].startswith('nl')
    url = BASE + p['slug'] + '/'
    head = tpl[:tpl.index('</head>')]
    head = re.sub(r'<html lang="[^"]*">', f'<html lang="{"nl" if nl else "en"}">', head)
    head = re.sub(r'<title>.*?</title>', f'<title>{esc(p["title"])}</title>', head, flags=re.S)
    for attr in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        head = re.sub(r'<meta content="[^"]*" ' + re.escape(attr) + '/>', f'<meta content="{esc(p["desc"])}" {attr}/>', head)
    for attr in ('property="og:title"', 'name="twitter:title"'):
        head = re.sub(r'<meta content="[^"]*" ' + re.escape(attr) + '/>', f'<meta content="{esc(p["title"])}" {attr}/>', head)
    head = re.sub(r'<meta content="[^"]*" property="og:url"/>', f'<meta content="{url}" property="og:url"/>', head)
    head = re.sub(r'<meta content="[^"]*" property="og:locale"/>', f'<meta content="{OGLOC[p["locale"]]}" property="og:locale"/>', head)
    head = re.sub(r'<meta content="[^"]*" property="article:modified_time"/>', f'<meta content="{TODAY}" property="article:modified_time"/>', head)
    head = re.sub(r'<link href="[^"]*" rel="canonical"/>', f'<link href="{url}" rel="canonical"/>', head)
    head = re.sub(r'<link href="[^"]*" hreflang="[^"]*" rel="alternate"/>', '', head)
    head = head.replace(f'<link href="{url}" rel="canonical"/>', f'<link href="{url}" rel="canonical"/><link href="{url}" hreflang="{p["locale"]}" rel="alternate"/><link href="{url}" hreflang="x-default" rel="alternate"/>')
    # JSON-LD: keep template Organization/WebSite nodes, replace page nodes.
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', head, flags=re.S)
    g = json.loads(m.group(1))
    keep = [n for n in g['@graph'] if n.get('@type') in ('Organization', 'WebSite')]
    for n in keep:
        n.pop('paymentAccepted', None)
    lang = 'nl' if nl else 'en'
    country = {'en-US': 'United States', 'en-GB': 'United Kingdom', 'en-CA': 'Canada', 'nl-NL': 'Netherlands'}[p['locale']]
    nodes = keep + [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p['title'], "description": p['desc'], "isPartOf": {"@id": BASE + "#website"}, "about": {"@id": BASE + "#organization"}, "inLanguage": p['locale'], "dateModified": TODAY, "breadcrumb": {"@id": url + "#breadcrumb"}, "mainEntity": {"@id": url + "#service"}},
        {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + ("nl/" if nl else "")}, {"@type": "ListItem", "position": 2, "name": p['crumb'], "item": url}]},
        {"@type": "Service", "@id": url + "#service", "name": strip(p['h1']).rstrip('.'), "description": p['desc'], "provider": {"@id": BASE + "#organization"}, "areaServed": {"@type": "Country", "name": country}, "availableLanguage": lang, "url": url},
        {"@type": "FAQPage", "@id": url + "#faq", "url": url, "inLanguage": p['locale'], "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in p['faqs']]},
    ]
    ld = json.dumps({"@context": "https://schema.org", "@graph": nodes}, ensure_ascii=False, separators=(',', ':'))
    head = head[:m.start()] + '<script type="application/ld+json">' + ld + '</script>' + head[m.end():]

    body_start = tpl[tpl.index('</head>'):tpl.index('<main id="content">') + len('<main id="content">')]
    help_block = cut(tpl, '<section aria-labelledby="hx-help-t"', '</section>')
    help_block = help_block.replace('hx-opt is-match', 'hx-opt')
    help_block = help_block.replace(f'class="hx-opt" data-topic="{p["topic"]}"', f'class="hx-opt is-match" data-topic="{p["topic"]}"', 1)
    topic_href = re.search(r'data-topic="' + p['topic'] + r'" href="([^"]*)"', help_block).group(1)
    steps = cut(tpl, '<section aria-labelledby="hx-steps-t"', '</section>')
    steps = re.sub(r'data-topic="[^"]*" href="[^"]*"', f'data-topic="{p["topic"]}" href="{topic_href}"', steps)
    testi = cut(tpl, '<section aria-labelledby="vt-title"', '</ul></section>')
    faq_open = tpl[tpl.index('<section class="faq-section" id="faq">'):tpl.index('<div class="simple-faq">', tpl.index('<section class="faq-section" id="faq">')) + len('<div class="simple-faq">')]
    proof = cut(tpl, '<section class="service-proof', '</section>')
    tail = tpl[tpl.index('</main>'):]
    home = '/nl/' if nl else '/'
    crumb_home = 'Home / Gidsen' if nl else 'Home / Country help'
    updated = f'Bijgewerkt op <time datetime="{TODAY}">19 november 2026</time>' if nl else (f'Updated <time datetime="{TODAY}">' + ('November 19, 2026' if p['locale'] == 'en-US' else '19 November 2026') + '</time>')
    cta_txt = 'Help mij verder' if nl else 'Get help with my case'
    img = IMG.get(p['topic'], 'instagram-glass-600.webp')
    hero = (f'<section class="service-hero"><div class="container"><div class="ub-hero-copy"><a class="crumb" href="{home}">{crumb_home}</a><h1>{p["h1"]}</h1><p class="guide-meta">{updated}</p><p>{p["intro"]}</p>'
            f'<div class="hero-cta"><a class="button button-light hx-start" data-hx="nov14" data-topic="{p["topic"]}" href="{topic_href}">{cta_txt} <span aria-hidden="true">→</span></a></div></div>'
            f'<div aria-hidden="true" class="ub-hero-art"><img alt="" fetchpriority="high" height="620" src="/redesign/assets/{img}" width="620"/></div></div></section>')
    answer = f'<section class="answer-first container" id="answer" style="padding-top:48px"><p style="max-width:860px;font-size:19px;line-height:1.5;margin:0">{p["answer"]}</p></section>'
    cards = '<section class="service-editorial container">' + ''.join(f'<article><h2>{a}</h2><p>{b}</p></article>' for a, b in p['cards']) + '</section>'
    toc_t = 'Op deze pagina' if nl else 'On this page'
    about_h = 'Over Unbanz' if nl else 'About Unbanz'
    about_p = ('Unbanz (unbanz.com) is een onafhankelijke dienst die mensen, bedrijven en bureaus helpt met uitgeschakelde, verbannen en gehackte accounts op Instagram, Facebook, TikTok, YouTube en WhatsApp, en met gebruikersnamen. Contact: team@unbanz.com. Niet verbonden aan Meta, TikTok of WhatsApp.' if nl else
               'Unbanz (unbanz.com) is an independent service that helps people, businesses and agencies with disabled, banned and hacked Instagram, Facebook, TikTok, YouTube and WhatsApp accounts, and with username claims. Contact: team@unbanz.com. Not affiliated with Meta, TikTok or WhatsApp.')
    secs = p['sections'] + [('about-unbanz', about_h, f'<p>{about_p}</p>')]
    reading = ('<div class="ub-reading container"><nav aria-label="' + toc_t + '" class="ub-toc"><p>' + toc_t + '</p>' + ''.join(f'<a href="#{i}">{h}</a>' for i, h, _ in secs) + '</nav><article class="guide-body container">'
               + ''.join(f'<h2 id="{i}">{h}</h2>{b}' for i, h, b in secs) + '</article></div>')
    faq = faq_open + ''.join(f'<details><summary>{esc(q)}<span aria-hidden="true">+</span></summary><p>{a}</p></details>' for q, a in p['faqs']) + '</div></div></section>'
    rel_label = 'Gerelateerde pagina’s' if nl else 'Related pages'
    related = f'<nav aria-label="{rel_label}" class="related-services container">' + ''.join(f'<a href="/{s}/">{t}</a>' for s, t in p['related']) + '</nav>'
    out = head + body_start + hero + answer + help_block + cards + reading + steps + testi + faq + proof + related + tail
    # Breadcrumb trail in body (crumb) points home; done.
    d = os.path.join(ROOT, p['slug']); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(out)
    return p['slug']

if __name__ == '__main__':
    for p in PAGES:
        print('built', build(p))
