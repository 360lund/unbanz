# -*- coding: utf-8 -*-
"""Ad account recovery pages, 2026-10-29: shared helpers + page builder (English). Built from the same template, hero /
answer-first / 3-card block, testimonials component and footer as the existing fixed service pages."""
import html, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import build_oct25_pages as B
import oct28d_top as T2

ROOT = B.ROOT
DATE = '2026-10-29'
DATE_LONG = '29 October 2026'
HUB = '/meta-ad-account-help/'
PAGES = []
def esc(s): return html.escape(s, quote=True)
def A(h, t): return '<a href="%s">%s</a>' % (h, t)
def ul(items): return '<ul>%s</ul>' % ''.join('<li>%s</li>' % i for i in items)
def ol(items): return '<ol>%s</ol>' % ''.join('<li>%s</li>' % i for i in items)
def slugify(t): return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')[:40]
def S(h2, *blocks):
    """section: h2 + blocks (strings; plain strings not starting with '<' become <p>)"""
    return '<h2 id="%s">%s</h2>%s' % (slugify(h2), h2, ''.join(b if b.startswith('<') else '<p>%s</p>' % b for b in blocks))

_ad = open(os.path.join(ROOT, 'facebook-ad-account-disabled/index.html'), encoding='utf-8').read()
SAFE_ABOUT = _ad[_ad.index('<h2 id="safe">'):_ad.index('</article>', _ad.index('<h2 id="safe">'))]
TESTI = B.TESTI
FOOT = B.FOOT

WA_AD = 'Hey%20Unbanz%2C%20I%20need%20help%20with%20a%20Meta%20ad%20account'
MAIL_AD = 'Meta%20ad%20account%20help'
PASSWORD_FAQ = ('Do I need to share my Facebook or Meta login?', 'No. Your password and login codes stay with you. Unbanz works from the ad account ID, the portfolio ID and a screenshot of the notice. Anyone who asks for your login is not someone to work with.')
CONTACT_FAQ = ('How do I contact Unbanz about an ad account?', 'WhatsApp +1 934 201 2490 or email team@unbanz.com. Send the ad account ID, the business portfolio ID and a screenshot of the notice.')

def send_block(extra=()):
    items = ['The ad account ID and the business portfolio ID.', 'A screenshot of the notice in Account Quality, with the date it appeared.',
             'What was running: the product or offer, the landing page and roughly how much was being spent per day.',
             'Anything that changed shortly before: a new card, a new admin, a new domain, a login from another country.'] + list(extra)
    return S('What to send', ul(items), 'Please do not send passwords, login codes, card numbers or access tokens.')

def how_block():
    return S('How it works with Unbanz', ol([
        'Message us on WhatsApp or email with the ad account ID, the business portfolio ID and a screenshot of the notice.',
        'We tell you honestly whether we can help and what it costs.',
        'We prepare the appeal and the supporting details, then send it through Meta’s official review.',
        'We keep you posted until Meta responds. Meta makes the final decision, and nobody can promise the outcome.']))

def who_block(items):
    return S('Who this is for', ul(items))

def page(slug, group, title, desc, h1, crumb, hero, answer, cards, body, faq, who, send_extra=(), area=None, audience=None,
         related=(), alts=None, lang='en-US'):
    PAGES.append(dict(slug=slug, group=group, title=title, desc=desc, h1=h1, crumb=crumb, svc=crumb, hero=hero, answer=answer,
        cards=cards, body=body, faq=faq, who=who, send_extra=send_extra, area=area, audience=audience, related=list(related),
        alts=alts, lang=lang, wa=WA_AD, ws='ad', subj=MAIL_AD))

# ------------------------------------------------------------------ builder
LD_OPEN = B.LD_OPEN
def alt_tags(p, url):
    if p.get('alts'):
        return ''.join('<link rel="alternate" hreflang="%s" href="%s">' % (c, u) for c, u in p['alts'])
    return ('<link rel="alternate" hreflang="en" href="%s"><link rel="alternate" hreflang="x-default" href="%s">' % (url, url))

def head_for(p, url):
    h = B.HEAD_PRE.replace(B.TPL_DESC, esc(p['desc'])).replace(B.TPL_TITLE, esc(p['title'])).replace(B.TPL_URL, url)
    h = h.replace('</title>', '</title><meta property="article:modified_time" content="%s">' % DATE, 1)
    h = re.sub(r'(<link rel="canonical" href="[^"]*">)(<link rel="alternate"[^>]*>)+', lambda m: m.group(1) + alt_tags(p, url), h, count=1)
    assert 'threads' not in h.lower() and h.count(url) >= 4, p['slug']
    return h

def ld_for(p, url):
    title, desc = p['title'], p['desc']
    faq_ld = [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in p['faq']]
    parent = p.get('crumb_parent', ('Meta ad account help', HUB))
    crumbs = [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://unbanz.com/'}]
    if parent:
        crumbs.append({'@type': 'ListItem', 'position': 2, 'name': parent[0], 'item': 'https://unbanz.com' + parent[1]})
    crumbs.append({'@type': 'ListItem', 'position': len(crumbs) + 1, 'name': p['crumb'], 'item': url})
    graph = [B.ORG, B.WEB,
      {'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': title, 'description': desc,
       'isPartOf': {'@id': 'https://unbanz.com/#website'}, 'about': {'@id': 'https://unbanz.com/#organization'},
       'inLanguage': p['lang'], 'datePublished': p.get('published', DATE), 'dateModified': DATE,
       'breadcrumb': {'@id': url + '#breadcrumb'}, 'mainEntity': {'@id': url + '#service'}},
      {'@type': 'BreadcrumbList', '@id': url + '#breadcrumb', 'itemListElement': crumbs},
      {'@type': 'FAQPage', '@id': url + '#faq', 'url': url, 'mainEntity': faq_ld},
      {'@type': 'Service', '@id': url + '#service', 'name': p['svc'], 'serviceType': 'Meta ad account recovery and appeals',
       'url': url, 'description': desc, 'provider': {'@id': 'https://unbanz.com/#organization'},
       'areaServed': p.get('area') or B.AREA,
       'availableChannel': {'@type': 'ServiceChannel', 'serviceUrl': 'https://wa.me/19342012490', 'availableLanguage': 'English'},
       'offers': {'@type': 'Offer', 'url': url, 'availability': 'https://schema.org/InStock',
                  'description': 'Price depends on the account and the issue.', 'seller': {'@id': 'https://unbanz.com/#organization'}}}]
    if p.get('audience'): graph[-1]['audience'] = {'@type': 'Audience', 'audienceType': p['audience']}
    ld = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, separators=(',', ':'))
    return ld.replace('</', '<\\/')

def build(p):
    slug = p['slug']; url = 'https://unbanz.com/%s/' % slug
    assert len(p['title']) <= 60, (slug, len(p['title']), p['title'])
    assert len(p['desc']) <= 160, (slug, len(p['desc']))
    assert "'" not in p['desc'] and '&' not in p['title'], slug
    assert 40 <= len(p['answer'].split()) <= 60, (slug, len(p['answer'].split()))
    assert 3 <= len(p['faq']) <= 6, slug
    wa = 'https://wa.me/19342012490?text=' + p['wa']
    mail = 'mailto:team@unbanz.com?subject=' + p['subj']
    ds = ' data-service="ad"'
    faq = list(p['faq'])
    if len(faq) <= 4: faq += [PASSWORD_FAQ, CONTACT_FAQ]
    elif len(faq) == 5: faq += [PASSWORD_FAQ]
    p['faq'] = faq
    faq_html = ''.join('<details><summary>%s<span aria-hidden="true">+</span></summary><p>%s</p></details>' % (esc(q), esc(a)) for q, a in faq)
    hero = T2.top_v2(h1=p['h1'], hero_html=esc(p['hero']), wa=wa, ws='ad', mail=mail, answer=p['answer'], cards=p['cards'])
    if p.get('crumb_parent', True) is not None:
        hero = hero.replace('<a class="crumb" href="/">Home / Services</a>', '<a class="crumb" href="%s">Home / %s</a>' % (HUB, 'Meta ad account help'), 1)
    hero = hero.replace('<div class="hero-cta">', '<p class="guide-meta">Updated <time datetime="%s">%s</time></p><div class="hero-cta">' % (DATE, DATE_LONG), 1)
    art = '<article class="guide-body container">%s%s%s%s%s</article>' % (
        ''.join(p['body']), send_block(p['send_extra']), how_block(), who_block(p['who']), SAFE_ABOUT)
    faqs = ('<section class="faq-section" id="faq"><div class="container faq-layout"><div class="faq-intro">'
            '<p class="eyebrow">QUICK ANSWERS</p><h2>Good to know.</h2></div><div class="simple-faq">%s</div></div></section>') % faq_html
    proof = ('<section class="service-proof container"><h2>Tell us what you need.</h2><div class="cta-pair">'
             '<a class="button button-blue" href="%s"%s>Message us on WhatsApp <span aria-hidden="true">↗︎</span></a>'
             '<a class="button button-light" href="%s">Email us</a></div></section>') % (wa, ds, mail)
    def nav(label, items):
        items = [(u, t) for u, t in items if u.strip('/') != slug]
        seen = set(); out = []
        for u, t in items:
            if u not in seen: seen.add(u); out.append((u, t))
        return '<nav class="related-services container" aria-label="%s">%s</nav>' % (label, ''.join('<a href="%s">%s</a>' % (u, esc(t)) for u, t in out))
    rel, relq = p['related_final']
    main = hero + art + TESTI + faqs + proof + nav('Related pages', rel) + nav('Related questions', relq) + '</main>'
    foot = FOOT.replace('<a class="" href="%s">' % B.HERE_WA, '<a class="" href="%s"%s>' % (wa, ds))
    foot = re.sub(r'(<div class="mobile-contact">.*?)' + re.escape(B.HERE_MAIL), lambda m: m.group(1) + mail, foot, flags=re.S)
    foot = foot.replace(B.HERE_WA, wa)
    return head_for(p, url) + LD_OPEN + ld_for(p, url) + '</script>' + B.HEAD_POST + main + foot
