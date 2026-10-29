# -*- coding: utf-8 -*-
"""Native (nl, es, pt-br, fr) white label pages, built on each language's own service page for head, footer and hero markup."""
import os as _o, sys as _s
_d = _o.path.dirname(_o.path.abspath(__file__))
while not _o.path.exists(_o.path.join(_d, 'cta_note.py')): _d = _o.path.dirname(_d)
_s.path.append(_d); from cta_note import write_page  # adds the human-only CTA note tag (homepages excluded)
import re, os, json, html
from urllib.parse import quote
from oct28e_native_content import S, L
from oct28e_content import TWINS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = '2026-10-28'
TPL = {'nl': 'nl/instagram-account-terugkrijgen', 'es': 'es/recuperar-cuenta-instagram', 'pt-br': 'pt-br/recuperar-conta-instagram', 'fr': 'fr/recuperer-compte-instagram'}
HUBS = {'nl': '/nl/white-label-bureau/', 'es': '/es/white-label-agencias/', 'pt-br': '/pt-br/white-label-agencias/', 'fr': '/fr/white-label-agences/'}
FOOT_NAMES = {'English': 'en', 'Français': 'fr', 'Nederlands': 'nl', 'Español': 'es', 'Português': 'pt-br'}
LOCALE = {'/nl/white-label-bureau-belgie/': 'nl_BE', '/fr/white-label-agences-belgique/': 'fr_BE', '/fr/white-label-agences-suisse/': 'fr_CH', '/fr/white-label-agences-luxembourg/': 'fr_LU'}
# hreflang code per native url (region codes only where the page targets a region other than the main one)
HREF_CODE = {'/nl/white-label-bureau-belgie/': ['nl-BE'], '/fr/white-label-agences-belgique/': ['fr-BE'], '/fr/white-label-agences-suisse/': ['fr-CH'], '/fr/white-label-agences-luxembourg/': ['fr-LU']}
LANG_CODES = {'nl': ['nl', 'nl-NL'], 'es': ['es', 'es-ES'], 'pt-br': ['pt-BR'], 'fr': ['fr', 'fr-FR']}
NAMES = {'': ''}

def fixfr(lang, x): return x.replace('en Luxembourg', 'au Luxembourg') if lang == 'fr' else x
def esc(s): return html.escape(s, quote=True)
def txt(s): return html.escape(s, quote=False)
def tpl_html(lang): return open(os.path.join(ROOT, TPL[lang], 'index.html'), encoding='utf-8').read()

def native_pages():
    """-> list of dicts (url path, lang, slug key, ...)"""
    out = []
    for key, tw in TWINS.items():
        for lg, u, _ in tw:
            out.append(dict(lang=lg, key=key, path=u))
    return out

def cluster(key):
    """hreflang entries (code, url) for the cluster of an english page: english + natives."""
    en = 'https://unbanz.com/white-label-agency%s/' % ('-' + key if key else '')
    ent = [('en', en)]
    if not key: ent.append(('en-US', en))
    for lg, u, _ in TWINS.get(key, []):
        codes = HREF_CODE.get(u) or LANG_CODES[lg]
        for c in codes: ent.append((c, 'https://unbanz.com' + u))
    ent.append(('x-default', en))
    return ent

def alt_links(key):
    return ''.join('<link rel="alternate" hreflang="%s" href="%s">' % (c, u) for c, u in cluster(key))

def foot_links(h, key, own_lang=None):
    """swap footer language links to the twins of this cluster (fallback: that language's white label hub)."""
    en = '/white-label-agency%s/' % ('-' + key if key else '')
    tw = {lg: u for lg, u, _ in TWINS.get(key, [])}
    def f(m):
        name = m.group(3)
        if name not in FOOT_NAMES: return m.group(0)
        lg = FOOT_NAMES[name]
        if lg == 'en': href = 'https://unbanz.com' + en
        else: href = tw.get(lg, HUBS[lg])
        return '<a href="%s" hreflang="%s" lang="%s">%s</a>' % (href, m.group(1), m.group(2), name)
    return re.sub(r'<a href="[^"]*" hreflang="([^"]*)" lang="([^"]*)">([^<]*)</a>', f, h)

def li(items): return '<ul>' + ''.join('<li>%s</li>' % i for i in items) + '</ul>'
def ol(items): return '<ol>' + ''.join('<li>%s</li>' % i for i in items) + '</ol>'

SAFE = {
 'nl': ('Blijf voorzichtig', 'Niemand hoeft je wachtwoord of inlogcodes te kennen om te helpen. Wees voorzichtig met berichten die beloven een account tegen betaling terug te krijgen, en geef nooit toegang uit handen. Unbanz vraagt er niet om.',
        'Over Unbanz', 'Unbanz (unbanz.com) is een onafhankelijke dienst die mensen helpt met Instagram- en Facebook-accounts via de officiële processen van de platforms. We zijn niet verbonden aan Meta.'),
 'es': ('Ten cuidado', 'Nadie necesita tu contraseña ni tus códigos de acceso para ayudarte. Desconfía de los mensajes que prometen devolverte una cuenta a cambio de un pago y nunca cedas el acceso. Unbanz no lo pide.',
        'Sobre Unbanz', 'Unbanz (unbanz.com) es un servicio independiente que ayuda con cuentas de Instagram y Facebook a través de los procesos oficiales de las plataformas. No estamos afiliados a Meta.'),
 'pt-br': ('Fique atento', 'Ninguém precisa da sua senha nem dos seus códigos de acesso para ajudar. Desconfie de mensagens que prometem devolver uma conta mediante pagamento e nunca entregue o acesso. A Unbanz não pede isso.',
           'Sobre a Unbanz', 'A Unbanz (unbanz.com) é um serviço independente que ajuda com contas do Instagram e do Facebook pelos processos oficiais das plataformas. Não somos afiliados à Meta.'),
 'fr': ('Restez prudent', 'Personne n’a besoin de votre mot de passe ni de vos codes de connexion pour vous aider. Méfiez-vous des messages qui promettent de rendre un compte contre paiement et ne cédez jamais l’accès. Unbanz ne le demande pas.',
        'À propos d’Unbanz', 'Unbanz (unbanz.com) est un service indépendant qui aide pour les comptes Instagram et Facebook via les processus officiels des plateformes. Nous ne sommes pas affiliés à Meta.'),
}

def build_native(lang, key, path):
    s = S[lang]; t = tpl_html(lang)
    hub = (key == '')
    info = L.get((lang, key)) if not hub else None
    n = info['name'] if info else ''
    url = 'https://unbanz.com' + path
    def fm(x):
        r = x.format(n=n, biz=info['biz'] if info else '')
        return r.replace('en Luxembourg', 'au Luxembourg') if lang == 'fr' else r
    title = s['hub_title'] if hub else fm(s['c_title'])
    desc = s['hub_desc'] if hub else fm(s['c_desc'])
    h1 = s['hub_h1'] if hub else fm(s['c_h1'])
    hero = s['hub_hero'] if hub else fm(s['c_hero'])
    answer = s['hub_answer'] if hub else fm(s['c_answer'])
    crumb = s['crumb_hub'] if hub else fm(s['c_crumb'])
    wa_txt = s['wa_hub'] if hub else fm(s['wa_c'])
    wa = 'https://wa.me/19342012490?text=' + quote(wa_txt, safe='')
    mail = 'mailto:team@unbanz.com?subject=' + s['mail_subj']
    assert len(title) <= 60 and len(desc) <= 160, (path, len(title), len(desc))
    # ---------------- head
    i0 = t.find('<main'); head, rest = t[:i0], t[i0:]
    head = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + esc(desc), head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + esc(title), head)
    head = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1) + esc(desc), head)
    head = re.sub(r'(<meta name="twitter:title" content=")[^"]*', lambda m: m.group(1) + esc(title), head)
    head = re.sub(r'(<meta name="twitter:description" content=")[^"]*', lambda m: m.group(1) + esc(desc), head)
    head = re.sub(r'<title>.*?</title>', lambda m: '<title>%s</title>' % txt(title), head, flags=re.S)
    head = re.sub(r'<link rel="canonical"[^>]*>(<link rel="alternate"[^>]*>)*', lambda m: '<link rel="canonical" href="%s">' % url + alt_links(key), head)
    head = re.sub(r'(<meta property="og:url" content=")[^"]*', lambda m: m.group(1) + url, head)
    loc = LOCALE.get(path)
    if loc: head = re.sub(r'(<meta property="og:locale" content=")[^"]*', lambda m: m.group(1) + loc, head)
    # ---------------- crumbs from template
    cm = re.search(r'<a class="crumb" href="([^"]*)">([^<]*)</a>', rest)
    home_href, crumb_text = cm.group(1), cm.group(2)
    bc_home, bc_svc = re.findall(r'"name": ?"([^"]*)", ?"item": ?"([^"]*)"', re.search(r'<script type="application/ld\+json">(.*?)</script>', t, re.S).group(1))[:2]
    hero_btn = re.search(r'data-service="unban">(.*?) <span', rest).group(1)
    hero_mail = re.search(r'class="hero-email" href="[^"]*">([^<]*)</a>', rest).group(1)
    crumb_a = '<a class="crumb" href="%s">%s</a>' % (home_href, crumb_text)
    # ---------------- sections
    cards = list(s['cards'])
    c3 = s['hub_c3'] if hub else (fm(s['c3'][0]), fm(s['c3'][1]))
    cards = [cards[0], cards[1], c3]
    cards_html = '<section class="service-editorial container">' + ''.join('<article><h2>%s</h2><p>%s</p></article>' % (txt(a), txt(b)) for a, b in cards) + '</section>'
    body = []
    body.append('<h2 id="white-label">%s</h2><p>%s</p>%s' % (txt(s['h_meaning']), txt(s['meaning_p']), li([txt(x) for x in s['meaning']])))
    if hub:
        lst = [(u, txt(tx)) for _, u, tx in []]
        nat = [(p['path'], p['key']) for p in native_pages() if p['lang'] == lang and p['key']]
        items = ['<a href="%s">%s</a>' % (p, txt(fixfr(lang, s['c_crumb'].format(n=L[(lang, k)]['name'])))) for p, k in nat]
        body.append('<h2 id="countries">%s</h2><p>%s</p>%s<p>%s</p>' % (txt(s['h_hubcountries']), txt(s['hubcountries_p']), li(items), s['hub_all']))
    else:
        body.append('<h2 id="before">%s</h2><p>%s</p>%s<p>%s</p>' % (txt(s['h_before']), txt(s['before_p']), li([txt(x) for x in s['before']]), txt(fm(s['before_biz']))))
        colon = ' :' if lang == 'fr' else ':'
        loc_items = ['<strong>%s%s</strong> %s' % (txt(a), colon, txt(b)) for a, b in info['items']]
        body.append('<h2 id="local">%s</h2><p>%s</p>%s' % (txt(fm(s['h_local'])), txt(fm(s['local_p'])), li(loc_items)))
    body.append('<h2 id="services">%s</h2>%s' % (txt(s['h_services']), li(s['services'])))
    body.append('<h2 id="how">%s</h2>%s' % (txt(s['h_how']), ol([txt(x) for x in s['how']])))
    body.append('<h2 id="who">%s</h2>%s' % (txt(s['h_who']), li([txt(re.sub(r' (in|en|no|au) \{n\}', '', x) if hub else fm(x)) for x in s['who']])))
    sh, sp, ah, ap = SAFE[lang]
    body.append('<h2 id="safe">%s</h2><p>%s</p><h2 id="about-unbanz">%s</h2><p>%s</p>' % (txt(sh), txt(sp), txt(ah), txt(ap)))
    # english twin link
    en = '/white-label-agency%s/' % ('-' + key if key else '')
    body.append('<p><a href="%s" hreflang="en" lang="en">English: %s</a></p>' % (en, 'white label agency pages' if hub else 'white label for agencies in ' + (info['area'])))
    faq = s['faq'] if hub else [(fm(q), fm(a)) for q, a in s['faq']]
    if hub:
        faq = [(q, a) for q, a in faq]
        def hfix(x):
            x = re.sub(r' [^.]*\{biz\}\.', '', x)
            return re.sub(r' (in|en|no|au) \{n\}', '', x)
        faq = [(hfix(q), hfix(a)) for q, a in faq]
    faq_html = ''.join('<details><summary>%s<span aria-hidden="true">+</span></summary><p>%s</p></details>' % (txt(q), txt(a)) for q, a in faq)
    faq_sec = '<section class="faq-section" id="faq"><div class="container faq-layout"><div class="faq-intro"><p class="eyebrow">%s</p><h2>%s</h2></div><div class="simple-faq">%s</div></div></section>' % (s['h_faq_eyebrow'], s['h_faq'], faq_html)
    proof = ('<section class="service-proof container"><h2>%s</h2><div class="cta-pair"><a class="button button-blue" href="%s" data-service="unban">%s <span aria-hidden="true">↗︎</span></a>'
             '<a class="button button-light" href="%s">%s</a></div></section>') % (txt(s['h_proof']), wa, txt(s['btn_wa']), mail, txt(s['btn_mail']))
    # related nav
    rel = []
    if not hub: rel.append((HUBS[lang], s['hubrel']))
    rel += s['rel']
    if not hub:
        sib = [p for p in native_pages() if p['lang'] == lang and p['key'] and p['path'] != path]
        for p in sib: rel.append((p['path'], fixfr(lang, s['c_crumb'].format(n=L[(lang, p['key'])]['name']))))
    rel.append((en, 'English'))
    rel_nav = '<nav class="related-services container" aria-label="%s">%s</nav>' % (esc(s['rel_label']), ''.join('<a href="%s">%s</a>' % (u, txt(tx)) for u, tx in rel))
    all_nav = re.search(r'<nav class="related-services container" aria-label="[^"]*">.*?</nav>', rest, re.S).group(0)
    main = ('<main id="content"><section class="service-hero"><div class="container">%s<h1>%s</h1><p>%s</p><div class="hero-cta">'
            '<a class="button button-light" href="%s" data-service="unban">%s <span aria-hidden="true">↗︎</span></a><a class="hero-email" href="%s">%s</a></div></div></section>'
            '<section class="answer-first container" id="answer" style="padding-top:48px"><p style="max-width:860px;font-size:19px;line-height:1.5;margin:0">%s</p></section>%s'
            '<article class="guide-body container">%s</article>%s%s%s%s</main>') % (
        crumb_a, txt(h1), txt(hero), wa, hero_btn, mail, hero_mail, txt(answer), cards_html, ''.join(body), faq_sec, proof, rel_nav, all_nav)
    # footer part of template
    fi = rest.find('</main>') + len('</main>')
    tail = rest[fi:]
    # replace WA/mail links everywhere in the tail (footer, mobile contact)
    tail = re.sub(r'https://wa\.me/19342012490\?text=[^"]*', wa.replace('\\', '\\\\'), tail)
    tail = re.sub(r'mailto:team@unbanz\.com\?subject=[^"]*', mail, tail)
    tail = foot_links(tail, key)
    # JSON-LD
    graph = [
     {'@type': 'Organization', '@id': 'https://unbanz.com/#organization', 'name': 'Unbanz', 'url': 'https://unbanz.com/'},
     {'@type': 'WebSite', '@id': 'https://unbanz.com/#website', 'url': 'https://unbanz.com/', 'name': 'Unbanz', 'alternateName': ['unbanz.com', 'Unbanz HQ'], 'inLanguage': 'en', 'publisher': {'@id': 'https://unbanz.com/#organization'}},
     {'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': title, 'description': desc, 'isPartOf': {'@id': 'https://unbanz.com/#website'}, 'about': {'@id': 'https://unbanz.com/#organization'},
      'inLanguage': re.search(r'<html lang="([^"]*)"', t).group(1), 'dateModified': DATE, 'primaryImageOfPage': {'@type': 'ImageObject', 'url': 'https://unbanz.com/assets/unbanz-share-v5.jpg'},
      'breadcrumb': {'@id': url + '#breadcrumb'}, 'mainEntity': {'@id': url + '#service'}},
     {'@type': 'BreadcrumbList', '@id': url + '#breadcrumb', 'itemListElement': (
        [{'@type': 'ListItem', 'position': 1, 'name': bc_home[0], 'item': 'https://unbanz.com' + home_href if home_href.startswith('/') else home_href},
         {'@type': 'ListItem', 'position': 2, 'name': bc_svc[0], 'item': bc_svc[1]}]
        + ([] if hub else [{'@type': 'ListItem', 'position': 3, 'name': s['crumb_hub'], 'item': 'https://unbanz.com' + HUBS[lang]}])
        + [{'@type': 'ListItem', 'position': 4 if not hub else 3, 'name': crumb, 'item': url}])},
     {'@type': 'FAQPage', '@id': url + '#faq', 'url': url, 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq]},
     {'@type': 'Service', '@id': url + '#service', 'url': url, 'inLanguage': re.search(r'<html lang="([^"]*)"', t).group(1), 'provider': {'@id': 'https://unbanz.com/#organization'},
      'areaServed': [{'@type': 'Country', 'name': info['area']}] if info else [{'@type': 'Country', 'name': c} for c in ['Netherlands', 'Belgium', 'France', 'Switzerland', 'Luxembourg', 'Spain', 'Brazil']],
      'availableChannel': {'@type': 'ServiceChannel', 'serviceUrl': 'https://wa.me/19342012490'},
      'name': h1.rstrip('.'), 'serviceType': 'White label account recovery', 'description': desc}]
    # areaServed for hubs is language specific
    if hub:
        areas = {'nl': ['Netherlands', 'Belgium'], 'es': ['Spain'], 'pt-br': ['Brazil'], 'fr': ['France', 'Belgium', 'Switzerland', 'Luxembourg']}[lang]
        graph[-1]['areaServed'] = [{'@type': 'Country', 'name': c} for c in areas]
    ld = '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, separators=(',', ':')) + '</script>'
    # JSON-LD placement: template has it after footer inside tail; replace
    head = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: ld, head, flags=re.S)
    assert ld in head, path
    assert (head + tail).count('<script type="application/ld+json">') == 1
    return head + main + tail

def write_all():
    out = []
    for p in native_pages():
        lang, key, path = p['lang'], p['key'], p['path']
        h = build_native(lang, key, path)
        d = os.path.join(ROOT, path.strip('/'))
        os.makedirs(d, exist_ok=True)
        write_page(os.path.join(d, 'index.html'), h)
        out.append(path)
    return out

if __name__ == '__main__':
    print(len(write_all()))
