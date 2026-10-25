# -*- coding: utf-8 -*-
"""Helpers for building the French (/fr/) pages of unbanz.com from the English templates."""
import re, json, html, os, hashlib

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
BASE = 'https://unbanz.com'
LASTMOD = '2026-10-24'
WA = 'https://wa.me/447723162824?text=Hey%20Unbanz%2C%20I%20need%20help%20with%20an%20account'
MAIL = 'mailto:team@unbanz.com?subject=Account%20help'
CSS = '/assets/site.5861d0cd0caa.css'
TCSS = '/assets/testimonials.633529d805.css'
TJS = '/assets/testimonials.633529d805.js'
SHARE = 'https://unbanz.com/assets/unbanz-share-v5.jpg'

def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f:
        return f.read()

# ---------- French typography ----------
NB = '\u00a0'
_ENT = r'(?<!&amp)(?<!&gt)(?<!&lt)(?<!&quot)(?<!&nbsp)(?<!&#x27)(?<!&#39)'
def ty(s):
    """Typographic cleanup for plain text (no tags)."""
    s = s.replace("'", '\u2019')
    s = re.sub(r'\s*«\s*', ' «' + NB, s)
    s = re.sub(r'\s*»', NB + '»', s)
    s = re.sub(r'(?:^|(?<=\S))[ \u00a0]?' + _ENT + r'([?!;:])(?=\s|$|[«»)\u2019"])', NB + r'\1', s)
    s = s.replace(' «' + NB, ' «' + NB)
    s = re.sub(r'^\u00a0«', '«', s)
    s = re.sub(r'^\u00a0', '', s)
    return s

def tyh(h):
    """Typography applied to the text nodes of an HTML fragment only."""
    parts = re.split(r'(<[^>]+>)', h)
    out = []
    for i, p in enumerate(parts):
        if p.startswith('<') and p.endswith('>'):
            out.append(p)
        else:
            out.append(ty(p))
    return ''.join(out)

def plain(h):
    return html.unescape(re.sub(r'<[^>]+>', '', h)).replace('\n', ' ')

def a(s):  # attribute-safe
    return html.escape(s, quote=True)

# ---------- shared bits extracted from the English templates ----------
_en = read('instagram-account-suspended-180-days/index.html')
_en_home = read('index.html')
SPRITE = re.search(r'<body>\s*<a class="skip-link"[^>]*>[^<]*</a>\s*(<svg.*?</svg>)', _en_home, re.S).group(1)
SOCIAL = re.search(r'<div class="social-links">.*?</div>', _en, re.S).group(0)
FOOT_SOCIAL = re.search(r'<span class="social-links">.*?</span></p>', _en, re.S).group(0)[:-4]
CLARITY = re.search(r'<script type="text/javascript">\s*\(function\(c,l,a,r,i,t,y\).*?</script>', _en, re.S).group(0)
VT_CARDS = re.findall(r'<li class="vt-card".*?</li>', read('reviews/index.html'), re.S)
assert len(VT_CARDS) == 3
def _frcard(c):
    c = c.replace('<summary>Transcript</summary>', '<summary>Transcription (en anglais)</summary>')
    c = re.sub(r'aria-label="Play video: ([^"]*)"', lambda m: 'aria-label="Lire la vidéo : ' + {'Management agency owner on working with Unbanz': 'une gérante d’agence parle de son travail avec Unbanz', 'Client on claiming an inactive Instagram username with Unbanz': 'un client à propos d’une demande de pseudo Instagram inactif', 'Restricted Facebook ad account restored by Unbanz': 'un annonceur parle de son compte publicitaire Facebook', }.get(m.group(1), m.group(1)) + '"', c)
    c = re.sub(r'alt="Management agency owner on working with Unbanz"', 'alt="Propriétaire d’agence : témoignage vidéo sur Unbanz"', c)
    c = re.sub(r'alt="Client on claiming an inactive Instagram username with Unbanz"', 'alt="Client : témoignage vidéo sur une demande de pseudo Instagram"', c)
    c = c.replace('alt="Restricted Facebook ad account restored by Unbanz"', 'alt="Annonceur : témoignage vidéo sur un compte publicitaire Facebook"')
    c = c.replace('Play video: Restricted Facebook ad account restored by Unbanz', 'Lire la vidéo : un annonceur parle de son compte publicitaire Facebook')
    return c
VT_CARDS = [_frcard(c) for c in VT_CARDS]
AVIS_STYLE = ''.join('<style>%s</style>' % x for x in re.findall(r'<style[^>]*>(.*?)</style>', read('reviews/index.html'), re.S))
WEBSITE_NODE = {"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": "Unbanz",
                "alternateName": ["unbanz.com", "Unbanz HQ"], "inLanguage": "en",
                "publisher": {"@id": BASE + "/#organization"}}
ORG_NODE = {"@type": "Organization", "@id": BASE + "/#organization", "name": "Unbanz", "url": BASE + "/"}

def fr_js_name():
    return '/assets/' + [f for f in os.listdir(os.path.join(ROOT, 'assets')) if f.startswith('site-fr.') and f.endswith('.js')][0]

# ---------- page registry ----------
PAGES = {}      # slug -> dict
ORDER = []

def reg(slug, kind, en, title, desc, nav, **kw):
    assert slug not in PAGES, slug
    if len(title) > 70 and title.endswith(' | Unbanz'):
        title = title[:-len(' | Unbanz')]
    d = dict(slug=slug, kind=kind, en=en, title=title, desc=desc, nav=nav)
    d.update(kw)
    PAGES[slug] = d
    ORDER.append(slug)
    return d

def url(slug):
    return BASE + ('/fr/' if slug == '' else '/fr/%s/' % slug)

def path(slug):
    return '/fr/' if slug == '' else '/fr/%s/' % slug

def en_url(d):
    return BASE + ('/' if not d['en'] else '/' + d['en'].strip('/') + '/') if d['en'] is not None else None

# ---------- chrome ----------
FOOT_LINKS = [
    ('/fr/services/', 'Services'), ('/fr/recuperer-compte-instagram/', 'Instagram'),
    ('/fr/compte-facebook-desactive/', 'Facebook'), ('/fr/compte-snapchat-verrouille/', 'Snapchat'),
    ('/fr/compte-publicitaire-meta-restreint/', 'Comptes publicitaires'),
    ('/fr/suppression-faux-comptes/', 'Faux comptes'), ('/fr/usurpation-identite-instagram/', 'Usurpation d’identité'),
    ('/fr/harcelement-compte-signalement/', 'Harcèlement'), ('/fr/pseudo-instagram/', 'Pseudos'),
    ('/fr/prix-recuperation-compte/', 'Prix'), ('/fr/comment-ca-marche/', 'Comment ça marche'),
    ('/fr/faq/', 'FAQ'), ('/fr/avis/', 'Avis'), ('/fr/unbanz-est-il-fiable/', 'Unbanz est-il fiable ?'),
    ('/fr/contact/', 'Contact'),
]

def header(home=False):
    nav = ('<nav class="desktop-nav" aria-label="Navigation principale"><a href="/fr/services/">Services</a>'
           '<a href="/fr/pseudo-instagram/">Pseudos</a><a href="/fr/avis/">Avis</a>'
           '<a href="/fr/faq/">Questions</a><a href="/fr/contact/">Contact</a></nav>')
    mobile = ('<nav class="mobile-nav" id="mobile-nav" hidden aria-label="Navigation mobile"><a href="/fr/">Accueil</a>'
              '<a href="/fr/services/">Services</a><a href="/fr/pseudo-instagram/">Pseudos</a>'
              '<a href="/fr/avis/">Avis</a><a href="/fr/comment-ca-marche/">Comment ça marche</a>'
              '<a href="/fr/faq/">Questions</a><a href="/fr/contact/">Contact</a>' + SOCIAL + '</nav>')
    return nav, mobile

def footer(en_href):
    links = ''.join('<a href="%s">%s</a>' % (h, tyh(t)) for h, t in FOOT_LINKS)
    links += ('<a href="%s" hreflang="en" lang="en">English</a><a href="/privacy/" hreflang="en" lang="en">Privacy</a>'
              '<a href="/terms/" hreflang="en" lang="en">Terms</a>') % en_href
    return ('<footer class="site-footer container"><div class="footer-top"><a class="wordmark" href="/fr/">unbanz.</a>'
            '<p>Récupération de comptes &amp; signalements.<br>Parlez-nous directement.' + FOOT_SOCIAL + '</p>'
            '<div class="footer-links">' + links + '</div></div>'
            '<div class="footer-bottom"><span>© <span id="year">2026</span> Unbanz</span>'
            '<span>Service indépendant. Non affilié à Meta.</span>'
            '<a href="mailto:team@unbanz.com?subject=Account%20help">team@unbanz.com</a></div></footer>')

MOBILE_CONTACT = ('<div class="mobile-contact"><a class="" href="' + WA + '">Écrivez-nous sur WhatsApp <span aria-hidden="true">↗︎</span></a>'
                  '<a href="' + MAIL + '">E-mail</a></div>')

SVC = ['unban']
def cta_pair(label='Nous écrire sur WhatsApp', mail='Nous écrire par e-mail'):
    return ('<div class="cta-pair"><a class="button button-blue" href="%s" data-service="%s">%s <span aria-hidden="true">↗︎</span></a>'
            '<a class="button button-light" href="%s">%s</a></div>') % (WA, SVC[0], label, MAIL, mail)

def hero_cta(label='Parlons-en sur WhatsApp'):
    return ('<div class="hero-cta"><a class="button button-light" href="%s" data-service="%s">%s <span aria-hidden="true">↗︎</span></a>'
            '<a class="hero-email" href="%s">Plutôt par e-mail ? ↗︎</a></div>') % (WA, SVC[0], label, MAIL)

def faq_section(items, eyebrow='QUESTIONS COURANTES', title='Bon à savoir.'):
    det = ''.join('<details><summary>%s<span aria-hidden="true">+</span></summary><p>%s</p></details>' % (q, ans) for q, ans in items)
    return ('<section class="faq-section" id="faq"><div class="container faq-layout"><div class="faq-intro"><p class="eyebrow">%s</p>'
            '<h2>%s</h2></div><div class="simple-faq">%s</div></div></section>') % (eyebrow, title, det)

def proof(title='Dites-nous ce qui s’est passé.'):
    return '<section class="service-proof container"><h2>%s</h2>%s</section>' % (title, cta_pair())

def related_nav(slugs, label='Pages liées'):
    items = [PAGES[s] for s in slugs if s in PAGES]
    return ('<nav class="related-services container" aria-label="%s">' % label +
            ''.join('<a href="%s">%s</a>' % (path(d['slug']), d['nav']) for d in items) + '</nav>')

def vt_section(title='Ce que disent les clients', note=True):
    cards = VT_CARDS[1]
    return ('<section class="vt container svc-testi" aria-labelledby="vt-title"><div class="vt-head"><div><p class="eyebrow">CLIENTS</p>'
            '<h2 id="vt-title">%s</h2></div></div><ul class="vt-track">%s</ul></section>' % (title, cards))

# ---------- head ----------
def hreflang(d):
    fr = url(d['slug'])
    if d['en'] is None:
        return ('<link rel="alternate" hreflang="fr" href="%s"><link rel="alternate" hreflang="fr-FR" href="%s">'
                '<link rel="alternate" hreflang="x-default" href="%s">') % (fr, fr, fr)
    e = en_url(d)
    return ('<link rel="alternate" hreflang="en" href="{e}"><link rel="alternate" hreflang="en-US" href="{e}">'
            '<link rel="alternate" hreflang="fr" href="{f}"><link rel="alternate" hreflang="fr-FR" href="{f}">'
            '<link rel="alternate" hreflang="x-default" href="{e}">').format(e=e, f=fr)

def ld_script(graph):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(',', ':')) + '</script>'

def build_graph(d, faq_items, crumbs, service=None):
    u = url(d['slug'])
    wp = {"@type": "WebPage", "@id": u + "#webpage", "url": u, "name": ty(d['title']), "description": ty(plain(d['desc'])),
          "isPartOf": {"@id": BASE + "/#website"}, "about": {"@id": BASE + "/#organization"}, "inLanguage": "fr",
          "primaryImageOfPage": {"@type": "ImageObject", "url": SHARE}, "breadcrumb": {"@id": u + "#breadcrumb"}}
    g = [ORG_NODE, WEBSITE_NODE, wp]
    if service:
        wp["mainEntity"] = {"@id": u + "#service"}
        s = {"@type": "Service", "@id": u + "#service", "url": u, "inLanguage": "fr",
             "provider": {"@id": BASE + "/#organization"}, "areaServed": [{"@type": "Country", "name": "France"}],
             "availableChannel": {"@type": "ServiceChannel", "serviceUrl": "https://wa.me/447723162824"},
             "offers": {"@type": "Offer", "url": u, "availability": "https://schema.org/InStock",
                        "description": "Le prix est indiqué après que vous avez expliqué votre situation, avant le début du travail.",
                        "seller": {"@id": BASE + "/#organization"}}}
        s.update({k: ty(v) if isinstance(v, str) else v for k, v in service.items()})
        g.append(s)
    g.append({"@type": "BreadcrumbList", "@id": u + "#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": ty(n), "item": h} for i, (n, h) in enumerate(crumbs)]})
    if faq_items:
        g.append({"@type": "FAQPage", "@id": u + "#faq", "url": u, "inLanguage": "fr", "mainEntity": [
            {"@type": "Question", "name": ty(plain(q)), "acceptedAnswer": {"@type": "Answer", "text": ty(plain(ans))}} for q, ans in faq_items]})
    return g

def head(d, faq_items, crumbs, service=None, vt=False):
    u = url(d['slug'])
    title = ty(d['title'])
    desc = ty(plain(d['desc']))
    h = ['<!doctype html>', '<html lang="fr">', '<head>', '<meta charset="UTF-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">',
         '<meta name="theme-color" content="#73b7f3">',
         '<meta name="description" content="%s">' % a(desc),
         '<meta property="og:title" content="%s">' % a(title),
         '<meta property="og:description" content="%s">' % a(desc),
         '<meta property="og:type" content="website">',
         '<meta name="robots" content="index,follow,max-image-preview:large"><link rel="canonical" href="%s">%s' % (u, hreflang(d)),
         '<meta property="og:url" content="%s">' % u,
         '<meta property="og:locale" content="fr_FR"><meta property="og:locale:alternate" content="en_US"><meta property="og:site_name" content="Unbanz">',
         '<meta property="og:image" content="%s">' % SHARE,
         '<meta property="og:image:width" content="1200">', '<meta property="og:image:height" content="628">',
         '<meta property="og:image:alt" content="Unbanz : récupération de comptes et signalements.">',
         '<meta name="twitter:site" content="@unbanzhq"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="%s"><meta name="twitter:description" content="%s"><meta name="twitter:image:alt" content="Unbanz : récupération de comptes Instagram et Facebook">' % (a(title), a(desc)),
         '<title>%s</title>' % html.escape(title, quote=False),
         '<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">',
         '<link rel="preload" href="/assets/unbanz-sans-latin.woff" as="font" type="font/woff" crossorigin>',
         '<meta property="og:image:type" content="image/jpeg"><meta name="twitter:image" content="%s"><link rel="stylesheet" href="%s"><script src="%s" defer></script>' % (SHARE, CSS, fr_js_name())]
    if vt:
        h.append('<link rel="preconnect" href="https://cdn.dbimg.app"><link rel="stylesheet" href="%s"><script src="%s" defer></script>' % (TCSS, TJS))
    h.append(ld_script(build_graph(d, faq_items, crumbs, service)))
    h.append(CLARITY)
    h.append('</head>')
    return '\n'.join(h)

def page_shell(d, main, faq_items, crumbs, service=None, vt=False, body_class='service-page', skip='#content'):
    nav, mobile = header()
    en_href = en_url(d) or (BASE + '/')
    top = ('<body class="%s"><a class="skip-link" href="%s">Aller au contenu</a><header class="service-header container">'
           '<a class="wordmark" href="/fr/">unbanz.</a>%s<button class="menu-button" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="mobile-nav">'
           '<span></span><span></span><span></span></button></header>%s\n') % (body_class, skip, nav, mobile)
    return head(d, faq_items, crumbs, service, vt) + '\n' + top + tyh(main) + '\n' + footer(en_href) + '\n' + MOBILE_CONTACT + '</body>\n</html>\n'

def crumb(label):
    return '<a class="crumb" href="/fr/">Accueil / %s</a>' % label

def hero(d, h1, lead, crumb_label):
    return ('<section class="service-hero"><div class="container">%s<h1>%s</h1><p>%s</p>%s</div></section>'
            % (crumb(crumb_label), h1, lead, hero_cta()))

STD_ABOUT = ('<h2 id="a-propos">À propos d’Unbanz</h2><p>Unbanz (unbanz.com) est un service indépendant qui aide particuliers, '
             'entreprises et agences pour les demandes de réactivation de comptes Instagram, Facebook et Snapchat, le signalement de comptes '
             'qui enfreignent les règles via les outils officiels, les demandes de pseudo et la récupération de comptes publicitaires Meta. '
             'Ce n’est ni Unbanx ni unbanx.me, et nous ne sommes pas affiliés à Meta. Voir <a href="/fr/unbanz-est-il-fiable/">Unbanz est-il fiable ?</a></p>')

STD_SAFE = ('<h2 id="prudence">Rester prudent</h2><p>Personne n’a besoin de votre mot de passe ni de vos codes de connexion pour vous aider. '
            'Ni nous, ni qui que ce soit. Si quelqu’un vous propose en message privé de « tout régler », vous demande de vous connecter via son lien '
            'ou prétend connaître quelqu’un chez Meta, passez votre chemin. Unbanz ne demande jamais vos identifiants et ne prétend à aucun accès spécial : '
            'nous passons par les mêmes voies officielles que vous.</p>')

STD_HOWTO = ('<h2 id="avec-unbanz">Comment ça se passe avec Unbanz</h2><ol><li>Vous nous écrivez sur WhatsApp ou par e-mail, avec votre nom d’utilisateur '
             'et une capture d’écran de la notification.</li><li>Nous vous disons franchement si nous pouvons vous aider. Le prix vous est indiqué dans la '
             'discussion, une fois que vous nous avez expliqué votre situation et avant que le travail commence. Demander ne coûte rien.</li>'
             '<li>Nous préparons la demande et la déposons via le processus officiel de la plateforme.</li>'
             '<li>Nous vous tenons informé(e) jusqu’à ce qu’il y ait une réponse.</li></ol>'
             '<p>Nos échanges se font principalement en anglais ; un message court avec le pseudo, la capture d’écran et la date suffit pour démarrer.</p>')

def guide_page(slug, h1, answer, secs, faq, related, help_html, crumb_label='Guides', std=True, extra_after=''):
    d = PAGES[slug]
    body = ''.join('<h2 id="%s">%s</h2>%s' % (sid, h2, content) for sid, h2, content in secs)
    body += '<h2 id="aide">Si vous voulez de l’aide</h2>' + help_html
    if std:
        body += STD_HOWTO + STD_SAFE + STD_ABOUT
    main = ('<main id="content">' + hero(d, h1, answer, crumb_label) + '<article class="guide-body container">' + body + '</article>' +
            extra_after + faq_section(faq, title='Bon à savoir.') + proof() + related_nav(related) + '</main>')
    crumbs = [('Accueil', BASE + '/fr/'), (crumb_label, url('services') if crumb_label == 'Services' else url('faq')), (d['nav'], url(slug))]
    return page_shell(d, main, faq, crumbs)

def service_page(slug, h1, answer, bold, cards1, steps, cards3_title_override, faq, guides, svc, crumb_label='Services', extra='', refund=False):
    d = PAGES[slug]
    def art(items):
        return '<section class="service-editorial container">' + ''.join('<article><h2>%s</h2><p>%s</p></article>' % (h, p) for h, p in items) + '</section>'
    block3 = [('Où que vous soyez', 'Nous travaillons à distance, par WhatsApp ou par e-mail, avec des clients en Europe et dans le monde. Nos échanges se font principalement en anglais.'),
              ('Le prix d’abord', 'Vous connaissez le prix avant que le travail commence : nous vous l’indiquons dans la discussion, une fois que vous nous avez expliqué votre situation.'),
              ('Votre mot de passe reste chez vous', 'Il nous suffit du nom d’utilisateur et de la notification. Votre mot de passe et vos codes restent avec vous.')]
    price = ('<section class="service-price container"><h2>Connaître le prix<br>avant de commencer.</h2><div><p>Écrivez-nous sur WhatsApp ou par e-mail, expliquez-nous la situation et nous revenons vers vous avec le prix.</p>'
             '<a href="/fr/prix-recuperation-compte/">Comment est établi le prix ↗︎</a></div></section>')
    if refund:
        price += ('<section class="service-price container"><h2>Politique de<br>remboursement.</h2><div><p>Remboursement intégral à 100\u00a0% si la réclamation du nom d’utilisateur échoue. Une réclamation échoue lorsque le pseudo n’est pas obtenu sur votre profil. Cette politique concerne uniquement les réclamations de pseudo.</p>'
                  '<a href="/fr/prix-recuperation-compte/">Comment est établi le prix ↗︎</a></div></section>')
    gl = ('<section class="guide-links container"><h2>Guides associés</h2>' + related_nav(guides, 'Guides associés').replace(' container', '') + '</section>') if guides else ''
    main = ('<main id="content">' + hero(d, h1, answer, crumb_label) +
            '<section class="answer-first container" style="padding-top:48px"><p style="max-width:860px;font-size:19px;line-height:1.5;margin:0"><strong>%s</strong></p></section>' % bold +
            art(cards1) + art(steps) + art(block3) + price + extra + faq_section(faq, eyebrow='VOS QUESTIONS') + proof() + gl +
            related_nav(['services', 'recuperer-compte-instagram', 'compte-facebook-desactive', 'compte-snapchat-verrouille', 'compte-publicitaire-meta-restreint',
                         'suppression-faux-comptes', 'pseudo-instagram', 'comment-ca-marche', 'unbanz-est-il-fiable', 'avis'], 'Services liés') + '</main>')
    crumbs = [('Accueil', BASE + '/fr/'), ('Services', url('services')), (d['nav'], url(slug))]
    return page_shell(d, main, faq, crumbs, service=svc)

ENDP = '<h2'  # placeholder

def autodesc(answer, limit=158):
    t = plain(answer)
    sents = re.split(r'(?<=[.!?])\s+', t)
    out = ''
    for s_ in sents:
        if len(out) + len(s_) + 1 <= limit:
            out = (out + ' ' + s_).strip()
        else:
            break
    if not out:
        out = t[:limit - 1].rsplit(' ', 1)[0] + '…'
    elif len(out) < 110 and len(t) > len(out) + 1:
        rest = t[len(out):].strip()
        room = limit - len(out) - 2
        if room > 30:
            out = out + ' ' + rest[:room].rsplit(' ', 1)[0].rstrip(',;:') + '…'
    return out

BUILD = {}

def guide(slug, en, title, nav, h1, answer, secs, faq, related, help_html, desc=None, svc='unban', std=True, crumb_label='Guides'):
    reg(slug, 'guide', en, title, desc or autodesc(answer), nav)
    def b():
        SVC[0] = svc
        return guide_page(slug, h1, answer, secs, faq, related, help_html, crumb_label=crumb_label, std=std)
    BUILD[slug] = b

def service(slug, en, title, nav, h1, answer, bold, cards1, steps, faq, guides, svcmeta, desc=None, svc='unban'):
    reg(slug, 'service', en, title, desc or autodesc(answer), nav)
    def b():
        SVC[0] = svc
        return service_page(slug, h1, answer, bold, cards1, steps, None, faq, guides, svcmeta, refund=(svc == 'username'))
    BUILD[slug] = b
