# -*- coding: utf-8 -*-
import copy, html, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from lib import ROOT, DATE
from nat import fr, nl, es, pt
LANGS = {'fr': (fr, 'fr', 'fr/compte-publicitaire-meta-restreint'), 'nl': (nl, 'nl', 'nl/advertentieaccount-terugkrijgen'),
         'es': (es, 'es', 'es/recuperar-cuenta-publicitaria'), 'pt-br': (pt, 'pt-br', 'pt-br/recuperar-conta-de-anuncios')}
EN = {'payment': 'ad-account-restricted-payment-issue', 'identity': 'ad-account-identity-verification-loop',
      'appeal': 'meta-ad-account-appeal-what-to-write', 'boost': 'ad-account-disabled-after-boosting-post',
      'again': 'ad-account-reinstated-then-disabled-again', 'admin': 'ad-account-lost-admin-after-employee-left'}
TOPICS = list(EN)
HL = {'fr': ('fr', 'fr-FR', 'Français'), 'nl': ('nl', 'nl-NL', 'Nederlands'), 'es': ('es', 'es-ES', 'Español'), 'pt-br': ('pt-BR', 'pt-BR', 'Português')}
CORE = {'fr': 'fr/compte-publicitaire-meta-restreint', 'nl': 'nl/advertentieaccount-terugkrijgen', 'es': 'es/recuperar-cuenta-publicitaria', 'pt-br': 'pt-br/recuperar-conta-de-anuncios'}
esc = lambda t: html.escape(t, quote=True)
def path(lk, topic): return '%s/%s' % (lk, LANGS[lk][0].T[topic]['slug'])
def url(p): return 'https://unbanz.com/%s/' % p
def pages():
    return [path(lk, t) for t in TOPICS for lk in LANGS]
def alts_for(topic):
    a = [('en', url(EN[topic])), ('en-US', url(EN[topic]))]
    for lk in LANGS:
        h1, h2, _ = HL[lk]; a += [(h1, url(path(lk, topic))), (h2, url(path(lk, topic)))] if h1 != h2 else [(h1, url(path(lk, topic)))]
    a.append(('x-default', url(EN[topic]))); return a
def build(lk, topic):
    mod, _, skel = LANGS[lk]; L = mod.L; t = mod.T[topic]; me = path(lk, topic); U = url(me)
    s = open(os.path.join(ROOT, skel, 'index.html'), encoding='utf-8').read()
    skel_url = url(skel); T, D = esc(t['title']), esc(t['desc'])
    assert len(t['title']) <= 60, (lk, topic, len(t['title']), t['title'])
    assert len(t['desc']) <= 160, (lk, topic, len(t['desc']))
    assert 35 <= len(t['answer'].split()) <= 62, (lk, topic, len(t['answer'].split()))
    # head
    s = re.sub(r'<title>.*?</title>', '<title>%s</title>' % T, s, 1)
    s = re.sub(r'(<meta name="description" content=")[^"]*"', r'\g<1>%s"' % D, s, 1)
    s = re.sub(r'(<meta property="og:title" content=")[^"]*"', r'\g<1>%s"' % T, s, 1)
    s = re.sub(r'(<meta property="og:description" content=")[^"]*"', r'\g<1>%s"' % D, s, 1)
    s = re.sub(r'(<meta name="twitter:title" content=")[^"]*"', r'\g<1>%s"' % T, s, 1)
    s = re.sub(r'(<meta name="twitter:description" content=")[^"]*"', r'\g<1>%s"' % D, s, 1)
    s = re.sub(r'(<link rel="canonical" href=")[^"]*"', r'\g<1>%s"' % U, s, 1)
    s = re.sub(r'(<meta property="og:url" content=")[^"]*"', r'\g<1>%s"' % U, s, 1)
    s = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">', '', s)
    alt = ''.join('<link rel="alternate" hreflang="%s" href="%s">' % a for a in alts_for(topic))
    s = s.replace('<link rel="canonical" href="%s">' % U, '<link rel="canonical" href="%s">%s<meta property="article:modified_time" content="%s">' % (U, alt, DATE), 1)
    # json-ld
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    g = json.loads(m.group(1).replace(skel_url, U))
    for x in g['@graph']:
        ty = x['@type']
        if ty == 'WebPage': x.update(name=t['title'], description=t['desc'], datePublished=DATE, dateModified=DATE)
        if ty == 'Service':
            x.update(name=t['title'], description=t['desc'], serviceType=t['title'])
            x['areaServed'] = [{'@type': 'Country', 'name': L['area']}]
        if ty == 'BreadcrumbList':
            items = x['itemListElement']
            items[1] = {'@type': 'ListItem', 'position': 2, 'name': L['crumb_mid'], 'item': url(CORE[lk])}
            items[2] = {'@type': 'ListItem', 'position': 3, 'name': t['title'], 'item': U}
        if ty == 'FAQPage':
            x['mainEntity'] = [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in t['faq'] + [L['faq_pw']]]
    assert not any(x['@type'] in ('Review', 'AggregateRating') for x in g['@graph'])
    s = s[:m.start(1)] + json.dumps(g, ensure_ascii=False, separators=(',', ':')) + s[m.end(1):]
    # main
    mm = re.search(r'<main id="content">(.*)</main>', s, re.S); old = mm.group(1)
    cta = re.search(r'<div class="hero-cta">.*?</div>', old, re.S).group(0)
    testi = re.search(r'<section class="vt vt-page svc-testi.*?</ul></section>', old, re.S).group(0)
    proof = re.search(r'<section class="service-proof container">.*?</section>', old, re.S).group(0)
    fi = re.search(r'<div class="faq-intro">.*?</div>', old, re.S).group(0)
    first, _, rest = t['answer'].partition('. ')
    ans = '<strong>%s.</strong> %s' % (esc(first), esc(rest)) if rest else '<strong>%s</strong>' % esc(first)
    h = '<section class="service-hero"><div class="container"><a class="crumb" href="%s">%s / %s</a><h1>%s</h1><p>%s</p><p class="guide-meta">%s <time datetime="%s"></time></p>%s</div></section>' % (
        CORE[lk].join(['/', '/']), esc(L['crumb_home']), esc(L['crumb_mid']), esc(t['h1']), esc(t['lead']), esc(L['updated']), DATE, cta)
    h = h.replace(' <time datetime="%s"></time>' % DATE, '')
    h = h.replace('<time', '<time')
    h = re.sub(r'(<p class="guide-meta">)(.*?)(</p>)', lambda m_: m_.group(1) + m_.group(2) + m_.group(3), h)
    ansec = '<section class="answer-first container" id="answer" style="padding-top:48px"><p style="max-width:860px;font-size:19px;line-height:1.5;margin:0">%s</p></section>' % ans
    cards = '<section class="service-editorial container">%s</section>' % ''.join('<article><h2>%s</h2><p>%s</p></article>' % (esc(a), esc(b)) for a, b in t['cards'])
    body = ('<article class="guide-body container"><h2>%s</h2><ol>%s</ol><h2>%s</h2><ul>%s</ul><p>%s</p><h2>%s</h2><p>%s</p></article>' % (
        esc(L['h_check']), ''.join('<li>%s</li>' % esc(i) for i in t['steps']), esc(L['h_send']),
        ''.join('<li>%s</li>' % esc(i) for i in t['send']), esc(L['send_note']), esc(L['h_how']), esc(L['how'])))
    faq = ('<section class="faq-section" id="faq"><div class="container faq-layout">%s<div class="simple-faq">%s</div></div></section>' % (
        fi, ''.join('<details><summary>%s<span aria-hidden="true">+</span></summary><p>%s</p></details>' % (esc(q), esc(a)) for q, a in t['faq'] + [L['faq_pw']])))
    sibs = [x for x in TOPICS if x != topic]
    k = TOPICS.index(topic); sib = [TOPICS[(k + i) % 6] for i in (1, 2, 3)]
    rel = ''.join('<a href="/%s/">%s</a>' % (path(lk, x), esc(mod.T[x]['title'])) for x in sib)
    rel2 = '<a href="/%s/">%s</a>' % (CORE[lk], esc(L['crumb_mid']))
    nav = '<nav class="related-services container" aria-label="%s">%s%s</nav>' % (esc(L['h_related'] if 'h_related' in L else 'Related'), rel2, rel)
    new = h + ansec + cards + body + testi + faq + proof + nav
    s = s[:mm.start(1)] + new + s[mm.end(1):]
    # footer language links
    def lang_links(mo):
        out = []
        for code, (nm, hl) in (('en', ('English', 'en')),):
            pass
        parts = ['<a href="%s" hreflang="en" lang="en">English</a>' % url(EN[topic])]
        for ok in LANGS:
            if ok == lk: continue
            parts.append('<a href="/%s/" hreflang="%s" lang="%s">%s</a>' % (path(ok, topic), HL[ok][0], HL[ok][0], HL[ok][2]))
        return ''.join(parts)
    s = re.sub(r'(?:<a href="[^"]*" hreflang="(?:en|fr|nl|es|pt-BR)" lang="[^"]*">(?:English|Français|Nederlands|Español|Português)</a>){4}', lang_links, s, 1)
    s = s.replace('<p class="guide-meta">%s' % esc(L['updated']), '<p class="guide-meta">%s' % esc(L['updated']))
    return s
if __name__ == '__main__':
    for lk in LANGS:
        for t in TOPICS:
            p = path(lk, t); os.makedirs(os.path.join(ROOT, p), exist_ok=True)
            open(os.path.join(ROOT, p, 'index.html'), 'w', encoding='utf-8').write(build(lk, t))
    print(len(pages()))
