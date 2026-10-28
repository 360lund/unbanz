# -*- coding: utf-8 -*-
"""Generic native (nl, es, pt-br, fr) agency page builder, on each language's service template."""
import re, os, sys, json, html
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__)); AG = os.path.dirname(HERE); SC = os.path.dirname(AG)
sys.path.insert(0, SC); sys.path.insert(0, AG)
import oct28e_native as N
from oct28e_native_content import S
import lib as agency_lib

ROOT = N.ROOT; DATE = '2026-10-28'
KEYS = ['pillar', 'how', 'client', 'compare', 'social', 'ads', 'faq', 'conf']
EN = {'pillar': 'white-label-account-recovery', 'how': 'how-white-label-account-recovery-works', 'client': 'what-your-client-sees-white-label-recovery',
      'compare': 'white-label-vs-referral-vs-in-house-recovery', 'social': 'white-label-recovery-for-social-media-agencies',
      'ads': 'white-label-recovery-for-ad-agencies', 'faq': 'white-label-agency-faq', 'conf': 'agency-client-confidentiality-account-recovery'}
LANGS = ['nl', 'es', 'pt-br', 'fr']
def esc(s): return html.escape(s, quote=True)
def txt(s): return html.escape(s, quote=False)
def P(*t): return ''.join('<p>%s</p>' % x for x in t)
def UL(i): return '<ul>' + ''.join('<li>%s</li>' % x for x in i) + '</ul>'
def OL(i): return '<ol>' + ''.join('<li>%s</li>' % x for x in i) + '</ol>'
def T(head, rows): return '<div class="table-wrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (''.join('<th>%s</th>' % h for h in head), ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in rows))
def D(term, t): return '<div class="dfn"><p class="dfn-term">%s</p><p>%s</p></div>' % (term, t)
def TM(title, *lines): return '<div class="tmpl"><p class="tmpl-title">%s</p>%s</div>' % (title, ''.join('<p>%s</p>' % l for l in lines))

PAGES = {}   # lang -> key -> dict
UI = {}      # lang -> dict
def load():
    import importlib
    for lg in ['nl', 'es', 'pt', 'fr']:
        importlib.import_module('p_' + lg)
LGDIR = {'nl': 'nl', 'es': 'es', 'pt-br': 'pt-br', 'fr': 'fr'}
def url(lang, key): return '/%s/%s/' % (LGDIR[lang], PAGES[lang][key]['slug'])

def cluster(key):
    en = 'https://unbanz.com/%s/' % EN[key]
    ent = [('en', en), ('en-US', en)]
    for lg in LANGS:
        for c in N.LANG_CODES[lg]: ent.append((c, 'https://unbanz.com' + url(lg, key)))
    ent.append(('x-default', en))
    return ent
def alt_links(key): return ''.join('<link rel="alternate" hreflang="%s" href="%s">' % (c, u) for c, u in cluster(key))

def foot_links(tail, lang, key):
    en = '/%s/' % EN[key]
    def f(m):
        name = m.group(3)
        if name not in N.FOOT_NAMES: return m.group(0)
        lg = N.FOOT_NAMES[name]
        href = 'https://unbanz.com' + en if lg == 'en' else url(lg, key)
        return '<a href="%s" hreflang="%s" lang="%s">%s</a>' % (href, m.group(1), m.group(2), name)
    return re.sub(r'<a href="[^"]*" hreflang="([^"]*)" lang="([^"]*)">([^<]*)</a>', f, tail)

def build(lang, key):
    s = S[lang]; u = UI[lang]; pg = PAGES[lang][key]; t = N.tpl_html(lang)
    path = url(lang, key); full = 'https://unbanz.com' + path
    title, desc = pg['title'], pg['desc']
    assert len(title) <= 60 and len(desc) <= 160, (path, len(title), len(desc))
    wa = 'https://wa.me/19342012490?text=' + quote(u['wa'], safe='')
    mail = 'mailto:team@unbanz.com?subject=' + s['mail_subj']
    i0 = t.find('<main'); head, rest = t[:i0], t[i0:]
    for tag, val in (('name="description"', desc), ('property="og:title"', title), ('property="og:description"', desc), ('name="twitter:title"', title), ('name="twitter:description"', desc)):
        head = re.sub(r'(<meta %s content=")[^"]*' % tag, lambda m: m.group(1) + esc(val), head)
    head = re.sub(r'<title>.*?</title>', lambda m: '<title>%s</title>' % txt(title), head, flags=re.S)
    head = re.sub(r'<link rel="canonical"[^>]*>(<link rel="alternate"[^>]*>)*', lambda m: '<link rel="canonical" href="%s">' % full + alt_links(key), head)
    head = re.sub(r'(<meta property="og:url" content=")[^"]*', lambda m: m.group(1) + full, head)
    head = head.replace('</head>', agency_lib.css_tag() + '</head>', 1) if '/assets/agency.' not in head else head
    cm = re.search(r'<a class="crumb" href="([^"]*)">([^<]*)</a>', rest)
    home_href, crumb_text = cm.group(1), cm.group(2)
    bcs = re.findall(r'"name": ?"([^"]*)", ?"item": ?"([^"]*)"', re.search(r'<script type="application/ld\+json">(.*?)</script>', t, re.S).group(1))[:2]
    hero_btn = re.search(r'data-service="unban">(.*?) <span', rest).group(1)
    hero_mail = re.search(r'class="hero-email" href="[^"]*">([^<]*)</a>', rest).group(1)
    cards = '<section class="service-editorial container">' + ''.join('<article><h2>%s</h2><p>%s</p></article>' % (txt(a), txt(b)) for a, b in pg['cards']) + '</section>'
    secs = pg['secs']
    body = ['<p class="updated">%s</p>' % u['updated']]
    if len(secs) >= 4:
        body.append('<nav class="toc" aria-label="%s"><p>%s</p><ul>%s</ul></nav>' % (esc(u['toc']), u['toc'], ''.join('<li><a href="#%s">%s</a></li>' % (i, txt(h)) for i, h, _ in secs)))
    for i, h, b in secs: body.append('<h2 id="%s">%s</h2>%s' % (i, txt(h), b))
    body.append('<p><a href="/%s/" hreflang="en" lang="en">English: %s</a></p>' % (EN[key], txt(u['en_link'])))
    faq = pg['faq']; assert 4 <= len(faq) <= 6, path
    faq_html = ''.join('<details><summary>%s<span aria-hidden="true">+</span></summary><p>%s</p></details>' % (txt(q), txt(a)) for q, a in faq)
    faq_sec = '<section class="faq-section" id="faq"><div class="container faq-layout"><div class="faq-intro"><p class="eyebrow">%s</p><h2>%s</h2></div><div class="simple-faq">%s</div></div></section>' % (s['h_faq_eyebrow'], s['h_faq'], faq_html)
    proof = ('<section class="service-proof container"><h2>%s</h2><div class="cta-pair"><a class="button button-blue" href="%s" data-service="unban">%s <span aria-hidden="true">↗︎</span></a>'
             '<a class="button button-light" href="%s">%s</a></div></section>') % (txt(s['h_proof']), wa, txt(s['btn_wa']), mail, txt(s['btn_mail']))
    rel = [(N.HUBS[lang], s['hubrel'])] + [(url(lang, k), PAGES[lang][k]['label']) for k in KEYS if k != key] + list(s['rel'])[:3] + [('/%s/' % EN[key], 'English')]
    rel_nav = '<nav class="related-services container" aria-label="%s">%s</nav>' % (esc(s['rel_label']), ''.join('<a href="%s">%s</a>' % (a, txt(b)) for a, b in rel))
    all_nav = re.search(r'<nav class="related-services container" aria-label="[^"]*">.*?</nav>', rest, re.S).group(0)
    main = ('<main id="content"><section class="service-hero"><div class="container"><a class="crumb" href="%s">%s</a><h1>%s</h1><p>%s</p><div class="hero-cta">'
            '<a class="button button-light" href="%s" data-service="unban">%s <span aria-hidden="true">↗︎</span></a><a class="hero-email" href="%s">%s</a></div></div></section>'
            '<section class="answer-first container" id="answer" style="padding-top:48px"><p style="max-width:860px;font-size:19px;line-height:1.5;margin:0"><strong>%s</strong> %s</p></section>%s'
            '<article class="guide-body container">%s</article>%s%s%s%s</main>') % (
        home_href, crumb_text, txt(pg['h1']), txt(pg['hero']), wa, hero_btn, mail, hero_mail, txt(pg['answer'][0]), txt(pg['answer'][1]), cards, ''.join(body), faq_sec, proof, rel_nav, all_nav)
    tail = rest[rest.find('</main>') + 7:]
    tail = re.sub(r'https://wa\.me/19342012490\?text=[^"]*', wa.replace('\\', '\\\\'), tail)
    tail = re.sub(r'mailto:team@unbanz\.com\?subject=[^"]*', mail, tail)
    tail = foot_links(tail, lang, key)
    hl = re.search(r'<html lang="([^"]*)"', t).group(1)
    graph = [
     {'@type': 'Organization', '@id': 'https://unbanz.com/#organization', 'name': 'Unbanz', 'url': 'https://unbanz.com/'},
     {'@type': 'WebSite', '@id': 'https://unbanz.com/#website', 'url': 'https://unbanz.com/', 'name': 'Unbanz', 'alternateName': ['unbanz.com', 'Unbanz HQ'], 'inLanguage': 'en', 'publisher': {'@id': 'https://unbanz.com/#organization'}},
     {'@type': 'WebPage', '@id': full + '#webpage', 'url': full, 'name': title, 'description': desc, 'isPartOf': {'@id': 'https://unbanz.com/#website'}, 'about': {'@id': 'https://unbanz.com/#organization'},
      'inLanguage': hl, 'dateModified': DATE, 'primaryImageOfPage': {'@type': 'ImageObject', 'url': 'https://unbanz.com/assets/unbanz-share-v5.jpg'},
      'breadcrumb': {'@id': full + '#breadcrumb'}, 'mainEntity': {'@id': full + '#service'}},
     {'@type': 'BreadcrumbList', '@id': full + '#breadcrumb', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': bcs[0][0], 'item': 'https://unbanz.com' + home_href if home_href.startswith('/') else home_href},
        {'@type': 'ListItem', 'position': 2, 'name': bcs[1][0], 'item': bcs[1][1]},
        {'@type': 'ListItem', 'position': 3, 'name': s['crumb_hub'], 'item': 'https://unbanz.com' + N.HUBS[lang]},
        {'@type': 'ListItem', 'position': 4, 'name': pg['label'], 'item': full}]},
     {'@type': 'FAQPage', '@id': full + '#faq', 'url': full, 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq]},
     {'@type': 'Service', '@id': full + '#service', 'url': full, 'inLanguage': hl, 'provider': {'@id': 'https://unbanz.com/#organization'},
      'audience': {'@type': 'Audience', 'audienceType': 'Marketing agencies'},
      'availableChannel': {'@type': 'ServiceChannel', 'serviceUrl': 'https://wa.me/19342012490'},
      'name': pg['h1'].rstrip('.'), 'serviceType': 'White label account recovery for agencies', 'description': desc}]
    ld = '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, separators=(',', ':')) + '</script>'
    head = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: ld, head, flags=re.S)
    out = head + main + tail
    assert out.count('<script type="application/ld+json">') == 1, path
    return out

def write_all(only=None):
    n = 0
    for lg in LANGS:
        if only and lg not in only: continue
        for k in KEYS:
            h = build(lg, k); d = os.path.join(ROOT, url(lg, k).strip('/')); os.makedirs(d, exist_ok=True)
            open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(h); n += 1
    return n
