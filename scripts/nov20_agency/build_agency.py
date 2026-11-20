"""Nov 20 2026: build the agency & white-label Q&A pages (English). Shell copied from the same template the
Nov 19 country Q&A pages use (head assets, header/nav, hx-help, hx-steps, FAQ wrapper, proof, footer), so CSS,
the non-sticky nav, contact policy (3-tier), the IN/PK/IR no-contact guard and the agency band are identical.
Schema: WebPage + Article + BreadcrumbList + FAQPage + Service. No ratings, stats or testimonials."""
import os, re, json, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from qa_agency import P as PAGES
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
BASE = 'https://unbanz.com/'
TODAY = '2026-11-20'
TPL = 'instagram-account-recovery-usa'
def esc(t): return html.escape(t, quote=True)
def strip(t): return re.sub(r'<[^>]+>', '', t)
def cut(s, start, end_tok):
    i = s.index(start); j = s.index(end_tok, i) + len(end_tok); return s[i:j]

def build(p):
    tpl = open(os.path.join(ROOT, TPL, 'index.html'), encoding='utf-8').read()
    url = BASE + p['slug'] + '/'
    head = tpl[:tpl.index('</head>')]
    head = re.sub(r'<html lang="[^"]*">', '<html lang="en">', head)
    head = re.sub(r'<title>.*?</title>', f'<title>{esc(p["title"])}</title>', head, flags=re.S)
    for attr in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        head = re.sub(r'<meta content="[^"]*" ' + re.escape(attr) + '/>', f'<meta content="{esc(p["desc"])}" {attr}/>', head)
    for attr in ('property="og:title"', 'name="twitter:title"'):
        head = re.sub(r'<meta content="[^"]*" ' + re.escape(attr) + '/>', f'<meta content="{esc(p["title"])}" {attr}/>', head)
    head = re.sub(r'<meta content="[^"]*" property="og:url"/>', f'<meta content="{url}" property="og:url"/>', head)
    head = re.sub(r'<meta content="[^"]*" property="og:type"/>', '<meta content="article" property="og:type"/>', head)
    head = re.sub(r'<meta content="[^"]*" property="og:locale"/>', '<meta content="en_US" property="og:locale"/>', head)
    head = re.sub(r'<meta content="[^"]*" property="article:modified_time"/>', f'<meta content="{TODAY}" property="article:modified_time"/>', head)
    head = re.sub(r'<link href="[^"]*" rel="canonical"/>', f'<link href="{url}" rel="canonical"/>', head)
    head = re.sub(r'<link href="[^"]*" hreflang="[^"]*" rel="alternate"/>', '', head)
    head = head.replace(f'<link href="{url}" rel="canonical"/>', f'<link href="{url}" rel="canonical"/><link href="{url}" hreflang="en" rel="alternate"/><link href="{url}" hreflang="x-default" rel="alternate"/>')
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', head, flags=re.S)
    g = json.loads(m.group(1))
    keep = [n for n in g['@graph'] if n.get('@type') in ('Organization', 'WebSite')]
    for n in keep: n.pop('paymentAccepted', None)
    faqs = [(p['q'], strip(p['answer']))] + p['faqs']
    nodes = keep + [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p['title'], "description": p['desc'], "isPartOf": {"@id": BASE + "#website"}, "inLanguage": "en", "datePublished": TODAY, "dateModified": TODAY, "breadcrumb": {"@id": url + "#breadcrumb"}, "mainEntity": {"@id": url + "#article"}},
        {"@type": "Article", "@id": url + "#article", "headline": p['q'], "description": p['desc'], "inLanguage": "en", "datePublished": TODAY, "dateModified": TODAY, "author": {"@type": "Organization", "name": "Unbanz editorial team", "url": BASE + "about/"}, "publisher": {"@id": BASE + "#organization"}, "mainEntityOfPage": {"@id": url + "#webpage"}, "about": p['q'], "audience": {"@type": "BusinessAudience", "audienceType": "Agencies"}},
        {"@type": "Service", "@id": url + "#service", "name": "White-label account recovery for agencies", "serviceType": "White-label social media account recovery", "provider": {"@id": BASE + "#organization"}, "areaServed": "Worldwide", "audience": {"@type": "BusinessAudience", "audienceType": "Marketing, PR, talent and reputation management agencies"}, "url": BASE + "white-label-agency/",
         "offers": {"@type": "Offer", "price": 1200, "priceCurrency": "USD", "description": "$1,200 per case (one account or handle), upfront bank transfer; usually 7–14 days; 100% refund paid the same business day if not reinstated within 14 calendar days."}},
        {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": BASE}, {"@type": "ListItem", "position": 2, "name": "White label for agencies", "item": BASE + "white-label-agency/"}, {"@type": "ListItem", "position": 3, "name": p['q'], "item": url}]},
        {"@type": "FAQPage", "@id": url + "#faq", "url": url, "inLanguage": "en", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faqs]},
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
    crumb = '<a class="crumb" href="/white-label-agency/">Home / White label for agencies</a>'
    by = f'By the Unbanz team · updated <time datetime="{TODAY}">November 20, 2026</time>'
    hero = (f'<section class="service-hero"><div class="container"><div class="ub-hero-copy">{crumb}<h1>{esc(p["q"])}</h1><p class="guide-meta">{by}</p><p>{esc(p["desc"])}</p>'
            f'<div class="hero-cta"><a class="button button-light" href="/white-label-agency/">Start agency onboarding <span aria-hidden="true">→</span></a></div></div>'
            f'</div></section>')
    answer = f'<section class="answer-first container" id="answer" style="padding-top:48px"><p class="eyebrow">Short answer</p><p style="max-width:860px;font-size:19px;line-height:1.5;margin:0">{p["answer"]}</p></section>'
    links = '<ul>' + ''.join(f'<li><a href="{u}" rel="noopener">{esc(t)}</a></li>' for u, t in p['links']) + '</ul>'
    more = '<ul>' + ''.join(f'<li><a href="/{o["slug"]}/">{esc(o["q"])}</a></li>' for o in PAGES if o['slug'] != p['slug']) + '</ul>'
    work = ('<p>Unbanz works behind your agency: your client deals only with you, we never contact them, and updates carry no Unbanz name. We never need passwords or login codes, '
            'we use the platform’s official process, and the platform makes the final decision. Unbanz is independent and not affiliated with Meta, Instagram, Facebook, WhatsApp, TikTok or Google.</p>'
            '<p>The white-label rate is $1,200 per case, paid upfront by bank transfer, usually 7–14 days, with a 100% refund paid the same business day if the account is not reinstated within 14 calendar days. '
            '<a href="/white-label-agency/">Start agency onboarding</a> (five quick questions), or browse the <a href="/white-label-agency/guides/">agency resources</a>.</p>')
    secs = list(p['sections']) + [('official-links', 'Official links', links), ('work-with-unbanz', 'Working with Unbanz', work), ('more-agency-questions', 'More agency questions', more)]
    reading = ('<div class="ub-reading container"><nav aria-label="On this page" class="ub-toc"><p>On this page</p>' + ''.join(f'<a href="#{i}">{h}</a>' for i, h, _ in secs) + '</nav><article class="guide-body container">'
               + ''.join(f'<h2 id="{i}">{h}</h2>{b}' for i, h, b in secs) + '</article></div>')
    faq = faq_open + ''.join(f'<details><summary>{esc(q)}<span aria-hidden="true">+</span></summary><p>{a}</p></details>' for q, a in p['faqs']) + '</div></div></section>'
    related = '<nav aria-label="Related pages" class="related-services container">' + ''.join(f'<a href="/{s}/">{t}</a>' for s, t in p['related']) + '</nav>'
    out = head + body_start + hero + answer + reading + help_block + steps_blk + faq + proof + related + tail
    d = os.path.join(ROOT, p['slug']); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(out)
    return len(strip(out))

if __name__ == '__main__':
    for p in PAGES:
        assert not (os.path.exists(os.path.join(ROOT, p['slug'], 'index.html')) and 'rebuild' not in sys.argv), p['slug']
    for p in PAGES: print(build(p), p['slug'])
