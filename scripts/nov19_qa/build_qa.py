"""Nov 19 2026: build country Q&A pages (US/UK/CA in English, NL in Dutch).
Shell (head assets, header, hx-help, hx-steps, FAQ wrapper, proof, footer) is copied from the
country template page so CSS, contact policy (geo WhatsApp) and tracking stay identical.
No testimonials, ratings or stats on these pages."""
import os, re, json, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from qa_us_uk import PAGES as P1
from qa_ca_nl import PAGES as P2
PAGES = P1 + P2
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
BASE = 'https://unbanz.com/'
TODAY = '2026-11-19'
TPL = {'en-US': 'instagram-account-recovery-usa', 'en-GB': 'instagram-account-recovery-uk', 'en-CA': 'instagram-account-recovery-canada', 'nl-NL': 'nl/instagram-account-gehackt'}
OGLOC = {'en-US': 'en_US', 'en-GB': 'en_GB', 'en-CA': 'en_CA', 'nl-NL': 'nl_NL'}
HUB = {'en-US': ('us', 'USA'), 'en-GB': ('uk', 'UK'), 'en-CA': ('ca', 'Canada'), 'nl-NL': ('nl', 'Nederland')}
CNAME = {'en-US': 'the USA', 'en-GB': 'the UK', 'en-CA': 'Canada', 'nl-NL': 'Nederland'}
IMG = {'tiktok': 'tiktok.webp', 'whatsapp': 'whatsapp.webp'}
BYSLUG = {p['slug']: p for p in PAGES}

def esc(t): return html.escape(t, quote=True)
def strip(t): return re.sub(r'<[^>]+>', '', t)
def cut(s, start, end_tok):
    i = s.index(start); j = s.index(end_tok, i) + len(end_tok); return s[i:j]

def help_html(p, nl):
    wa = p['topic'] == 'whatsapp'
    if nl:
        a = ('<p>Probeer eerst de officiële stappen hierboven. Werken die niet, of kun je het account echt niet missen, dan kan Unbanz de zaak overnemen. We bekijken je situatie eerst en zeggen eerlijk als het geen zin heeft om te betalen. Nemen we hem aan: meestal 7–14 dagen zodra we starten, met volledige terugbetaling als het account niet binnen 14 dagen terug is. Tarieven vanaf 1.000 $, betaald per bankoverschrijving. We vragen nooit om je wachtwoord.</p>'
             + ('<p>Alleen WhatsApp kan een ban opheffen. Wij bereiden de officiële beoordeling met je voor en handelen het vervolg af.</p>' if wa else '')
             + '<p>Unbanz is een onafhankelijke dienst, niet verbonden aan Meta, Instagram, Facebook, WhatsApp, TikTok of Google. Het platform neemt de eindbeslissing. Mail <a href="mailto:team@unbanz.com">team@unbanz.com</a> of bekijk <a href="/nl/hoe-het-werkt/">hoe het werkt</a> en de <a href="/nl/prijzen-accountherstel/">prijzen</a>.</p>')
    else:
        a = ('<p>Try the official steps above first. If they don’t work, or you really can’t lose the account, Unbanz can take the case on. We look at it first and tell you honestly if it isn’t worth paying for. If we take it: usually 7–14 days once we start, with a full refund if the account isn’t reinstated within 14 days. Fees start from $1,000, paid by bank transfer. We never ask for your password.</p>'
             + ('<p>Only WhatsApp can lift a ban. We prepare the official review with you and handle the follow-up.</p>' if wa else '')
             + '<p>Unbanz is an independent service, not affiliated with Meta, Instagram, Facebook, WhatsApp, TikTok or Google. The platform makes the final decision. Email <a href="mailto:team@unbanz.com">team@unbanz.com</a>, or see <a href="/how-it-works/">how it works</a> and <a href="/pricing/">pricing</a>.</p>')
    return a

def build(p):
    loc = p['locale']; nl = loc.startswith('nl')
    tpl = open(os.path.join(ROOT, TPL[loc], 'index.html'), encoding='utf-8').read()
    url = BASE + p['slug'] + '/'
    hub, hubname = HUB[loc]
    head = tpl[:tpl.index('</head>')]
    head = re.sub(r'<html lang="[^"]*">', f'<html lang="{"nl" if nl else "en"}">', head)
    head = re.sub(r'<title>.*?</title>', f'<title>{esc(p["title"])}</title>', head, flags=re.S)
    for attr in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        head = re.sub(r'<meta content="[^"]*" ' + re.escape(attr) + '/>', f'<meta content="{esc(p["desc"])}" {attr}/>', head)
    for attr in ('property="og:title"', 'name="twitter:title"'):
        head = re.sub(r'<meta content="[^"]*" ' + re.escape(attr) + '/>', f'<meta content="{esc(p["title"])}" {attr}/>', head)
    head = re.sub(r'<meta content="[^"]*" property="og:url"/>', f'<meta content="{url}" property="og:url"/>', head)
    head = re.sub(r'<meta content="[^"]*" property="og:type"/>', '<meta content="article" property="og:type"/>', head)
    head = re.sub(r'<meta content="[^"]*" property="og:locale"/>', f'<meta content="{OGLOC[loc]}" property="og:locale"/>', head)
    head = re.sub(r'<meta content="[^"]*" property="article:modified_time"/>', f'<meta content="{TODAY}" property="article:modified_time"/>', head)
    head = re.sub(r'<link href="[^"]*" rel="canonical"/>', f'<link href="{url}" rel="canonical"/>', head)
    head = re.sub(r'<link href="[^"]*" hreflang="[^"]*" rel="alternate"/>', '', head)
    alts = [(loc, url)]
    if p.get('alt'):
        a = BYSLUG[p['alt']]; alts.append((a['locale'], BASE + a['slug'] + '/'))
    xdef = next((u for l, u in alts if not l.startswith('nl')), url)
    tags = ''.join(f'<link href="{u}" hreflang="{l}" rel="alternate"/>' for l, u in sorted(alts)) + f'<link href="{xdef}" hreflang="x-default" rel="alternate"/>'
    head = head.replace(f'<link href="{url}" rel="canonical"/>', f'<link href="{url}" rel="canonical"/>' + tags)
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', head, flags=re.S)
    g = json.loads(m.group(1))
    keep = [n for n in g['@graph'] if n.get('@type') in ('Organization', 'WebSite')]
    for n in keep: n.pop('paymentAccepted', None)
    author = {"@type": "Organization", "name": "Unbanz editorial team", "url": BASE + ("nl/over-ons/" if nl else "about/")}
    faqs = [(p['q'], strip(p['answer']))] + p['faqs']
    nodes = keep + [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p['title'], "description": p['desc'], "isPartOf": {"@id": BASE + "#website"}, "inLanguage": loc, "datePublished": TODAY, "dateModified": TODAY, "breadcrumb": {"@id": url + "#breadcrumb"}, "mainEntity": {"@id": url + "#article"}},
        {"@type": "Article", "@id": url + "#article", "headline": p['q'], "description": p['desc'], "inLanguage": loc, "datePublished": TODAY, "dateModified": TODAY, "author": author, "publisher": {"@id": BASE + "#organization"}, "mainEntityOfPage": {"@id": url + "#webpage"}, "about": p['q'], "contentLocation": {"@type": "Country", "name": {'en-US': 'United States', 'en-GB': 'United Kingdom', 'en-CA': 'Canada', 'nl-NL': 'Netherlands'}[loc]}},
        {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + ("nl/" if nl else "")}, {"@type": "ListItem", "position": 2, "name": hubname if not nl else "Vragen", "item": BASE + hub + "/" if not nl else BASE + "nl/veelgestelde-vragen/"}, {"@type": "ListItem", "position": 3, "name": p['q'], "item": url}]},
        {"@type": "FAQPage", "@id": url + "#faq", "url": url, "inLanguage": loc, "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faqs]},
    ]
    ld = json.dumps({"@context": "https://schema.org", "@graph": nodes}, ensure_ascii=False, separators=(',', ':'))
    head = head[:m.start()] + '<script type="application/ld+json">' + ld + '</script>' + head[m.end():]
    body_start = tpl[tpl.index('</head>'):tpl.index('<main id="content">') + len('<main id="content">')]
    help_block = cut(tpl, '<section aria-labelledby="hx-help-t"', '</section>').replace('hx-opt is-match', 'hx-opt')
    help_block = help_block.replace(f'class="hx-opt" data-topic="{p["topic"]}"', f'class="hx-opt is-match" data-topic="{p["topic"]}"', 1)
    topic_href = re.search(r'data-topic="' + p['topic'] + r'" href="([^"]*)"', help_block).group(1)
    steps_blk = cut(tpl, '<section aria-labelledby="hx-steps-t"', '</section>')
    steps_blk = re.sub(r'data-topic="[^"]*" href="[^"]*"', f'data-topic="{p["topic"]}" href="{topic_href}"', steps_blk)
    fo = tpl.index('<section class="faq-section" id="faq">')
    faq_open = tpl[fo:tpl.index('<div class="simple-faq">', fo) + len('<div class="simple-faq">')]
    proof = cut(tpl, '<section class="service-proof', '</section>')
    tail = tpl[tpl.index('</main>'):]
    if nl:
        crumb = '<a class="crumb" href="/nl/veelgestelde-vragen/">Home / Vragen</a>'
        by = f'Door het Unbanz-team · bijgewerkt op <time datetime="{TODAY}">19 november 2026</time>'
        short, cta = 'Kort antwoord', 'Help mij verder'
        H = dict(steps='Stap voor stap', local='Goed om te weten in Nederland', links='Officiële links', help='Wanneer je hulp nodig hebt', about='Over Unbanz', toc='Op deze pagina', rel='Gerelateerde pagina’s')
        about_p = 'Unbanz (unbanz.com) is een onafhankelijke dienst die mensen, bedrijven en bureaus helpt met uitgeschakelde, verbannen en gehackte accounts op Instagram, Facebook, TikTok, YouTube en WhatsApp. Deze pagina is geschreven door het Unbanz-team op basis van de officiële helpcentra en overheidsbronnen hieronder, gecontroleerd op 19 november 2026. Niet verbonden aan Meta, TikTok of WhatsApp.'
    else:
        crumb = f'<a class="crumb" href="/{hub}/">Home / {hubname} help</a>'
        datestr = 'November 19, 2026' if loc in ('en-US', 'en-CA') else '19 November 2026'
        by = f'By the Unbanz team · updated <time datetime="{TODAY}">{datestr}</time>'
        short, cta = 'Short answer', 'Get help with my case'
        H = dict(steps='Step by step', local=f'Good to know in {CNAME[loc]}', links='Official links', help='When you need help', about='About Unbanz', toc='On this page', rel='Related pages')
        about_p = 'Unbanz (unbanz.com) is an independent service that helps people, businesses and agencies with disabled, banned and hacked Instagram, Facebook, TikTok, YouTube and WhatsApp accounts. This page was written by the Unbanz team from the official help centres and government sources listed above, checked on 19 November 2026. Not affiliated with Meta, TikTok or WhatsApp.'
    img = IMG.get(p['topic'], 'instagram-glass-600.webp')
    hero = (f'<section class="service-hero"><div class="container"><div class="ub-hero-copy">{crumb}<h1>{esc(p["q"])}</h1><p class="guide-meta">{by}</p><p>{esc(p["desc"])}</p>'
            f'<div class="hero-cta"><a class="button button-light hx-start" data-hx="nov14" data-topic="{p["topic"]}" href="{topic_href}">{cta} <span aria-hidden="true">→</span></a></div></div>'
            f'<div aria-hidden="true" class="ub-hero-art"><img alt="" fetchpriority="high" height="620" src="/redesign/assets/{img}" width="620"/></div></div></section>')
    answer = f'<section class="answer-first container" id="answer" style="padding-top:48px"><p class="eyebrow">{short}</p><p style="max-width:860px;font-size:19px;line-height:1.5;margin:0">{p["answer"]}</p></section>'
    links = '<ul>' + ''.join(f'<li><a href="{u}" rel="noopener">{esc(t)}</a></li>' for u, t in p['links']) + '</ul>'
    secs = [('steps', H['steps'], '<ol>' + ''.join(f'<li>{s}</li>' for s in p['steps']) + '</ol>'),
            ('local', H['local'], '<ul>' + ''.join(f'<li>{s}</li>' for s in p['local']) + '</ul>'),
            ('official-links', H['links'], links),
            ('help', H['help'], help_html(p, nl)),
            ('about-unbanz', H['about'], f'<p>{about_p}</p>')]
    reading = ('<div class="ub-reading container"><nav aria-label="' + H['toc'] + '" class="ub-toc"><p>' + H['toc'] + '</p>' + ''.join(f'<a href="#{i}">{h}</a>' for i, h, _ in secs) + '</nav><article class="guide-body container">'
               + ''.join(f'<h2 id="{i}">{h}</h2>{b}' for i, h, b in secs) + '</article></div>')
    faq = faq_open + ''.join(f'<details><summary>{esc(q)}<span aria-hidden="true">+</span></summary><p>{a}</p></details>' for q, a in p['faqs']) + '</div></div></section>'
    related = f'<nav aria-label="{H["rel"]}" class="related-services container">' + ''.join(f'<a href="/{s}/">{t}</a>' for s, t in p['related']) + '</nav>'
    out = head + body_start + hero + answer + reading + help_block + steps_blk + faq + proof + related + tail
    d = os.path.join(ROOT, p['slug']); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(out)
    return len(strip(p['answer']).split())

if __name__ == '__main__':
    for p in PAGES:
        assert not (os.path.exists(os.path.join(ROOT, p['slug'], 'index.html')) and 'qa-built' not in sys.argv), p['slug']
    for p in PAGES:
        print(build(p), p['slug'])
