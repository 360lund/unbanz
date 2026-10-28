#!/usr/bin/env python3
"""Build the 13 pages added on 2026-10-25 from the threads-account-suspended template."""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from oct25_content import PAGES, DATE
import oct28d_top as T2

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
T = open(os.path.join(ROOT, 'threads-account-suspended/index.html'), encoding='utf-8').read()
SLUGS = {p['slug'] for p in PAGES}

LD_OPEN = '<script type="application/ld+json">'
i0 = T.index(LD_OPEN); i1 = T.index('</script>', i0)
HEAD_PRE, LD_T, HEAD_POST = T[:i0], T[i0 + len(LD_OPEN):i1], T[i1 + len('</script>'):T.index('<main')]
TPL_DESC = 'Threads account suspended or disabled? How Threads is tied to Instagram, how to appeal, and how Unbanz helps through Meta&#x27;s official process.'
TPL_TITLE = 'Threads Account Suspended or Disabled? Help | Unbanz'
TPL_URL = 'https://unbanz.com/threads-account-suspended/'
ld_t = json.loads(LD_T)
ORG = next(x for x in ld_t['@graph'] if x['@type'] == 'Organization')
WEB = next(x for x in ld_t['@graph'] if x['@type'] == 'WebSite')
ORG.pop('subjectOf', None)
ORG['sameAs'] = [u for u in ORG['sameAs'] if 'trustpilot' not in u]
AREA = next(x for x in ld_t['@graph'] if x['@type'] == 'Service')['areaServed']

TESTI = T[T.index('<section class="vt'):T.index('<section class="faq-section"')]
FOOT = T[T.index('<footer'):]
SAFE_ABOUT = T[T.index('<h2 id="safe">'):T.index('</article>')]
HERE_WA = 'https://wa.me/19342012490?text=Hey%20Unbanz%2C%20I%20need%20help%20with%20an%20account'
HERE_MAIL = 'mailto:team@unbanz.com?subject=Account%20help'
assert FOOT.count(HERE_WA) == 1 and 'data-service' not in FOOT

def esc(s): return html.escape(s, quote=True)
def plain(h): return html.unescape(re.sub(r'<[^>]+>', '', h)).strip()

def build(p):
    slug = p['slug']; url = 'https://unbanz.com/%s/' % slug
    title, desc = p['title'], p['desc']
    assert len(title) <= 60 and len(desc) <= 160, slug
    assert 40 <= len(p['answer'].split()) <= 60, (slug, len(p['answer'].split()))
    assert "'" not in desc
    wa = 'https://wa.me/19342012490?text=' + p['wa']
    mail = 'mailto:team@unbanz.com?subject=' + p['subj']
    ds = ' data-service="username"' if p['ws'] == 'username' else ''
    # ---- head
    h = HEAD_PRE.replace(TPL_DESC, esc(desc)).replace(TPL_TITLE, esc(title)).replace(TPL_URL, url)
    h = h.replace('</title>', '</title><meta property="article:modified_time" content="%s">' % DATE, 1)
    if p['lang'] != 'en-US':
        h = h.replace('<link rel="alternate" hreflang="en-US" href="%s">' % url, '')
    assert h.count(url) >= 4 and 'threads' not in h.lower(), slug
    # ---- JSON-LD
    faq = p['faq']
    assert 4 <= len(faq) <= 6
    faq_html = ''.join('<details><summary>%s<span aria-hidden="true">+</span></summary><p>%s</p></details>' % (esc(q), esc(a)) for q, a in faq)
    faq_ld = [{'@type': 'Question', 'name': plain(esc(q)), 'acceptedAnswer': {'@type': 'Answer', 'text': plain(esc(a))}} for q, a in faq]
    graph = [ORG, WEB,
      {'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': title, 'description': desc,
       'isPartOf': {'@id': 'https://unbanz.com/#website'}, 'about': {'@id': 'https://unbanz.com/#organization'},
       'inLanguage': p['lang'], 'dateModified': DATE,
       'breadcrumb': {'@id': url + '#breadcrumb'}, 'mainEntity': {'@id': url + '#service'}},
      {'@type': 'BreadcrumbList', '@id': url + '#breadcrumb', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://unbanz.com/'},
        {'@type': 'ListItem', 'position': 2, 'name': p['crumb'], 'item': url}]},
      {'@type': 'FAQPage', '@id': url + '#faq', 'url': url, 'mainEntity': faq_ld},
      {'@type': 'Service', '@id': url + '#service', 'name': p['svc'],
       'serviceType': 'Social media account unbans, account removals and username claims', 'url': url,
       'description': desc, 'provider': {'@id': 'https://unbanz.com/#organization'}, 'areaServed': AREA,
       'availableChannel': {'@type': 'ServiceChannel', 'serviceUrl': 'https://wa.me/19342012490', 'availableLanguage': 'English'},
       'offers': {'@type': 'Offer', 'url': url, 'availability': 'https://schema.org/InStock',
                  'description': 'Price agreed before work starts.', 'seller': {'@id': 'https://unbanz.com/#organization'}}}]
    ld = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, separators=(',', ':'))
    ld = ld.replace('</', '<\\/')
    # ---- main
    if p.get('v2'):
        # same hero, answer-first and 3-card block as the original service pages (see oct28d_top.py)
        h1 = T2.H1.get(slug, p['h1'])
        hero = T2.top_v2(h1=h1, hero_html=esc(p['hero']), wa=wa, ws=p['ws'], mail=mail, answer=p['answer'],
                         cards=p.get('cards') or T2.cards_for(slug, h1))
        art = '<article class="guide-body container">%s%s</article>' % (''.join(p['body']), SAFE_ABOUT)
    else:
        hero = ('<main id="content"><section class="service-hero"><div class="container">'
                '<a class="crumb" href="/">Home / %s</a><h1>%s</h1><p>%s</p><div class="hero-cta">'
                '<a class="button button-light" href="%s"%s>Talk to us on WhatsApp <span aria-hidden="true">↗︎</span></a>'
                '<a class="hero-email" href="%s">Prefer email? ↗︎</a></div></div></section>') % (esc(p['crumb']), esc(p['h1']), esc(p['hero']), wa, ds, mail)
        art = '<article class="guide-body container"><h2 id="answer">Short answer</h2><p>%s</p>%s%s</article>' % (
            esc(p['answer']), ''.join(p['body']), SAFE_ABOUT)
    faqs = ('<section class="faq-section" id="faq"><div class="container faq-layout"><div class="faq-intro">'
            '<p class="eyebrow">QUICK ANSWERS</p><h2>Good to know.</h2></div><div class="simple-faq">%s</div></div></section>') % faq_html
    proof = ('<section class="service-proof container"><h2>Tell us what you need.</h2><div class="cta-pair">'
             '<a class="button button-blue" href="%s"%s>Message us on WhatsApp <span aria-hidden="true">↗︎</span></a>'
             '<a class="button button-light" href="%s">Email us</a></div></section>') % (wa, ds, mail)
    def nav(label, items):
        items = [(u, t) for u, t in items if u.strip('/') != slug]
        assert items
        return '<nav class="related-services container" aria-label="%s">%s</nav>' % (label, ''.join('<a href="%s">%s</a>' % (u, esc(t)) for u, t in items))
    main = hero + art + TESTI + faqs + proof + nav('Related pages', p['related']) + nav('Related questions', p['relq']) + '</main>'
    foot = FOOT.replace('<a class="" href="%s">' % HERE_WA, '<a class="" href="%s"%s>' % (wa, ds))
    foot = foot.replace('<div class="mobile-contact"><a class="" href="%s">' % HERE_WA, '<div class="mobile-contact"><a class="" href="%s"%s>' % (wa, ds))
    foot = re.sub(r'(<div class="mobile-contact">.*?)' + re.escape(HERE_MAIL), lambda m: m.group(1) + mail, foot, flags=re.S)
    if foot.count(HERE_WA):
        foot = foot.replace(HERE_WA, wa)
    return h + LD_OPEN + ld + '</script>' + HEAD_POST + main + foot

if __name__ == '__main__':
    for p in PAGES:
        d = os.path.join(ROOT, p['slug']); os.makedirs(d, exist_ok=True)
        out = build(p)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(out)
        print('wrote', p['slug'], len(out))
