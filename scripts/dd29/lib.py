# -*- coding: utf-8 -*-
"""Double-down pages, 2026-10-29. Same page template as the Oct 28 ad-account pages (hero, answer-first, 3 cards, article,
5-card testimonials, FAQ, contact block, related nav, footer). Copy rules built in: no price/timing/outcome promises."""
import html, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'adacct'))
import build_oct25_pages as B
import oct28d_top as T2
ROOT = B.ROOT
DATE = '2026-10-29'; DATE_LONG = '29 October 2026'
PAGES = []
def esc(s): return html.escape(s, quote=True)
def A(h, t): return '<a href="%s">%s</a>' % (h, t)
def ul(items): return '<ul>%s</ul>' % ''.join('<li>%s</li>' % i for i in items)
def ol(items): return '<ol>%s</ol>' % ''.join('<li>%s</li>' % i for i in items)
def slugify(t): return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')[:40]
def S(h2, *blocks):
    return '<h2 id="%s">%s</h2>%s' % (slugify(h2), h2, ''.join(b if b.startswith('<') else '<p>%s</p>' % b for b in blocks))
TESTI = B.TESTI; FOOT = B.FOOT

# family settings -------------------------------------------------------------------------------------------------------
FAM = {}
def fam(key, **kw): FAM[key] = kw
IG_WA = 'Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20Instagram%20account'
FB_WA = 'Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20Facebook%20account'
SC_WA = 'Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20Snapchat%20account'
AD_WA = 'Hey%20Unbanz%2C%20I%20need%20help%20with%20a%20Meta%20ad%20account'
UN_WA = 'Hey%20Unbanz%2C%20I%20want%20to%20claim%20this%20username%3A%20%40'
def pw_faq(platform):
    return ('Do I need to share my %s password?' % platform, 'No. Your password and login codes stay with you. Unbanz works from your public username, the notice and the details you send. Anyone who asks for your login is not someone to work with.')
def contact_faq(what):
    return ('How do I contact Unbanz about %s?' % what, 'WhatsApp +1 934 201 2490 or email team@unbanz.com. Send your username and a screenshot of the notice, if there is one.')

def page(slug, f, title, desc, h1, crumb, hero, answer, cards, sections, faq, who, send_extra=(), area=None, audience=None, native=None):
    PAGES.append(dict(slug=slug, fam=f, title=title, desc=desc, h1=h1, crumb=crumb, hero=hero, answer=answer, cards=cards,
        sections=sections, faq=faq, who=who, send_extra=list(send_extra), area=area, audience=audience, native=native))

def send_block(p):
    F = FAM[p['fam']]
    items = list(F['send']) + p['send_extra']
    return S('What to send', ul(items), F.get('send_note', 'Please do not send passwords, login codes, card numbers or access tokens.'))

def how_block(p):
    F = FAM[p['fam']]
    return S('How it works with Unbanz', ol([
        'Message us on WhatsApp or email with %s.' % F['how1'],
        'We tell you honestly whether this is something we can help with.',
        '%s' % F['how3'],
        'We stay in touch while you wait. %s makes the final decision, and nobody can promise the outcome.' % ('Snapchat' if F['platform'] == 'Snapchat' else 'Meta')]))

def who_block(p): return S('Who this is for', ul(p['who']))

SAFE = ('<h2 id="safe">Staying safe</h2><p>Nobody needs your password or login codes to help you. If someone in your DMs offers to fix it, asks you to '
        'log in through their link, or claims to have a special way in, walk away. Unbanz never asks for logins and has no special access. '
        'We use the same official routes that are open to you.</p>'
        '<h2 id="about-unbanz">About Unbanz</h2><p>Unbanz (unbanz.com) is an independent service that helps people, businesses and agencies with Instagram, Facebook '
        'and Snapchat account unbans, username claims, and Meta ad account recovery. Contact: WhatsApp +1 934 201 2490 or team@unbanz.com. Not affiliated with Meta.</p>')

def head_for(p, url, alts=None):
    h = B.HEAD_PRE.replace(B.TPL_DESC, esc(p['desc'])).replace(B.TPL_TITLE, esc(p['title'])).replace(B.TPL_URL, url)
    h = h.replace('</title>', '</title><meta property="article:modified_time" content="%s">' % DATE, 1)
    if alts: at = ''.join('<link rel="alternate" hreflang="%s" href="%s">' % (c, u) for c, u in alts)
    else: at = '<link rel="alternate" hreflang="en" href="%s"><link rel="alternate" hreflang="x-default" href="%s">' % (url, url)
    h = re.sub(r'(<link rel="canonical" href="[^"]*">)(<link rel="alternate"[^>]*>)+', lambda m: m.group(1) + at, h, count=1)
    assert 'threads' not in h.lower() and h.count(url) >= 4, p['slug']
    return h

def ld_for(p, url):
    F = FAM[p['fam']]
    title, desc = p['title'], p['desc']
    faq_ld = [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in p['faq']]
    parent = F['parent']
    crumbs = [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://unbanz.com/'},
              {'@type': 'ListItem', 'position': 2, 'name': parent[0], 'item': 'https://unbanz.com' + parent[1]},
              {'@type': 'ListItem', 'position': 3, 'name': p['crumb'], 'item': url}]
    graph = [B.ORG, B.WEB,
      {'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': title, 'description': desc,
       'isPartOf': {'@id': 'https://unbanz.com/#website'}, 'about': {'@id': 'https://unbanz.com/#organization'},
       'inLanguage': 'en-US', 'datePublished': DATE, 'dateModified': DATE,
       'breadcrumb': {'@id': url + '#breadcrumb'}, 'mainEntity': {'@id': url + '#service'}},
      {'@type': 'BreadcrumbList', '@id': url + '#breadcrumb', 'itemListElement': crumbs},
      {'@type': 'FAQPage', '@id': url + '#faq', 'url': url, 'mainEntity': faq_ld},
      {'@type': 'Service', '@id': url + '#service', 'name': p['crumb'], 'serviceType': F['stype'],
       'url': url, 'description': desc, 'provider': {'@id': 'https://unbanz.com/#organization'},
       'areaServed': p.get('area') or B.AREA,
       'availableChannel': {'@type': 'ServiceChannel', 'serviceUrl': 'https://wa.me/19342012490', 'availableLanguage': 'English'}}]
    if p.get('audience'): graph[-1]['audience'] = {'@type': 'Audience', 'audienceType': p['audience']}
    ld = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, separators=(',', ':'))
    return ld.replace('</', '<\\/')

def build(p, alts=None):
    F = FAM[p['fam']]
    slug = p['slug']; url = 'https://unbanz.com/%s/' % slug
    assert len(p['title']) <= 60, (slug, len(p['title']), p['title'])
    assert len(p['desc']) <= 160, (slug, len(p['desc']))
    assert "'" not in p['desc'] and '&' not in p['title'], slug
    assert 40 <= len(p['answer'].split()) <= 60, (slug, len(p['answer'].split()))
    assert len(p['cards']) == 3 and 2 <= len(p['sections']) <= (6 if p['fam'].startswith('hub') else 4) and len(p['faq']) in (3, 4), slug
    wa = 'https://wa.me/19342012490?text=' + F['wa']
    mail = 'mailto:team@unbanz.com?subject=' + F['subj']
    ds = ' data-service="%s"' % F['ws'] + (' data-platform="Instagram"' if F['ws'] == 'username' else '')
    faq = list(p['faq']) + [pw_faq(F['platform']), contact_faq(F['what'])]
    p['faq_final'] = faq
    faq_html = ''.join('<details><summary>%s<span aria-hidden="true">+</span></summary><p>%s</p></details>' % (esc(q), esc(a)) for q, a in faq)
    hero = T2.top_v2(h1=p['h1'], hero_html=esc(p['hero']), wa=wa, ws=F['ws'], mail=mail, answer=p['answer'], cards=p['cards'])
    hero = re.sub(r'<a class="crumb" href="[^"]*">Home / [^<]*</a>', lambda m: '<a class="crumb" href="%s">Home / %s</a>' % (F['parent'][1], esc(F['parent'][0])), hero, count=1)
    assert F['parent'][1] in hero, slug
    hero = hero.replace('<div class="hero-cta">', '<p class="guide-meta">Updated <time datetime="%s">%s</time></p><div class="hero-cta">' % (DATE, DATE_LONG), 1)
    art = '<article class="guide-body container">%s%s%s%s%s</article>' % (
        ''.join(p['sections']), send_block(p), how_block(p), who_block(p), SAFE)
    faqs = ('<section class="faq-section" id="faq"><div class="container faq-layout"><div class="faq-intro">'
            '<p class="eyebrow">QUICK ANSWERS</p><h2>Good to know.</h2></div><div class="simple-faq">%s</div></div></section>') % faq_html
    proof = ('<section class="service-proof container"><h2>Tell us what you need.</h2><div class="cta-pair">'
             '<a class="button button-blue" href="%s"%s>Message us on WhatsApp <span aria-hidden="true">↗︎</span></a>'
             '<a class="button button-light" href="%s">Email us</a></div></section>') % (wa, ds, mail)
    def nav(label, items):
        seen = set(); out = []
        for u, t in items:
            if u.strip('/') == slug or u in seen: continue
            seen.add(u); out.append((u, t))
        return '<nav class="related-services container" aria-label="%s">%s</nav>' % (label, ''.join('<a href="%s">%s</a>' % (u, esc(t)) for u, t in out))
    rel, relq = p['related_final']
    main = hero + art + TESTI + faqs + proof + nav('Related pages', rel) + nav('Related questions', relq) + '</main>'
    foot = FOOT.replace('<a class="" href="%s">' % B.HERE_WA, '<a class="" href="%s"%s>' % (wa, ds))
    foot = re.sub(r'(<div class="mobile-contact">.*?)' + re.escape(B.HERE_MAIL), lambda m: m.group(1) + mail, foot, flags=re.S)
    foot = foot.replace(B.HERE_WA, wa)
    return head_for(p, url, alts) + B.LD_OPEN + ld_for(p, url) + '</script>' + B.HEAD_POST + main + foot
