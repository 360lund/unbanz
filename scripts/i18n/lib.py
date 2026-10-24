# -*- coding: utf-8 -*-
"""Config-driven builder for the localized (NL / ES / PT-BR) pages of unbanz.com.
Mirrors the structure of scripts/fr/lib.py. Content lives in lang_<code>.py."""
import re, json, html, os, hashlib, glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
BASE = 'https://unbanz.com'
LASTMOD = '2026-10-25'
CSS = '/assets/site.6f99c22548e9.css'
TCSS = '/assets/testimonials.633529d805.css'
TJS = '/assets/testimonials.633529d805.js'
SHARE = 'https://unbanz.com/assets/unbanz-share-v5.jpg'
WA_NUM = 'https://wa.me/19342012490'

def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f:
        return f.read()

def plain(h):
    return html.unescape(re.sub(r'<[^>]+>', '', h)).replace('\n', ' ')

def a(s):
    return html.escape(s, quote=True)

_en = read('instagram-account-suspended-180-days/index.html')
_en_home = read('index.html')
SPRITE = re.search(r'<body>\s*<a class="skip-link"[^>]*>[^<]*</a>\s*(<svg.*?</svg>)', _en_home, re.S).group(1)
SOCIAL = re.search(r'<div class="social-links">.*?</div>', _en, re.S).group(0)
FOOT_SOCIAL = re.search(r'<span class="social-links">.*?</span></p>', _en, re.S).group(0)[:-4]
CLARITY = re.search(r'<script type="text/javascript">\s*\(function\(c,l,a,r,i,t,y\).*?</script>', _en, re.S).group(0)
_rv = read('reviews/index.html')
VT_RAW = re.findall(r'<li class="vt-card".*?</li>', _rv, re.S)
assert len(VT_RAW) == 3
AVIS_STYLE = ''.join('<style>%s</style>' % x for x in re.findall(r'<style[^>]*>(.*?)</style>', _rv, re.S))
WEBSITE_NODE = {"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": "Unbanz",
                "alternateName": ["unbanz.com", "Unbanz HQ"], "inLanguage": "en",
                "publisher": {"@id": BASE + "/#organization"}}
ORG_NODE = {"@type": "Organization", "@id": BASE + "/#organization", "name": "Unbanz", "url": BASE + "/"}

# language-neutral page keys -> English twin path (None = no English twin)
TWINS = {
    'home': '', 'services': 'services', 'pricing': 'unban-pricing', 'faq': 'faq', 'contact': 'contact',
    'reviews': 'reviews', 'about': 'about', 'how': 'how-it-works', 'legit': 'is-unbanz-legit',
    'ig': 'instagram-account-recovery', 'fb': 'facebook-account-recovery', 'ad': 'ad-account-recovery',
    'snap': 'snapchat-unban-service', 'fake': 'fake-account-takedown', 'imp': 'impersonation-account-removal',
    'har': 'harassment-account-removal', 'user': 'instagram-username-claim',
    'ig-disabled': 'instagram-account-disabled-appeal', 'ig-hacked': 'hacker-changed-my-instagram-email-and-password',
    'appeal-time': 'how-long-does-an-instagram-appeal-take', 'appeal-denied': 'instagram-appeal-denied',
    'deleted': 'is-my-instagram-account-deleted-or-disabled', 'no-button': 'guides/instagram-disabled-no-appeal-button',
    'blocked': 'instagram-we-restrict-certain-activity-action-blocked', 'ad-disabled': 'facebook-ad-account-disabled',
    'fb-appeal': 'guides/facebook-account-disabled-appeal', 'fb-hacked': 'guides/hacked-facebook-account-recovery',
    'inactive-user': 'inactive-instagram-username', 'report-fake': 'fake-instagram-account-using-my-photos',
    'scams': 'guides/account-recovery-scams-fake-hackers-warning', 'sextortion': 'guides/sextortion-what-to-do-on-instagram',
    'support': None, 'rights': None,
}
LANG_ORDER = ['en', 'fr', 'nl', 'es', 'pt-br']
LANG_DIR = {'nl': 'nl', 'es': 'es', 'pt-br': 'pt-br'}

def en_path(twin):
    return '/' if not twin else '/' + twin.strip('/') + '/'

class Site:
    def __init__(self, S, slugs):
        self.S = S
        self.code = S['code']
        self.dir = S['dir']
        self.slugs = slugs            # key -> slug ('' = home)
        self.pages = {}               # key -> dict
        self.order = []
        self.build = {}
        self.svc = ['unban']
        self.vt_cards = self._vt_cards()

    # ---- urls
    def path(self, key):
        s = self.slugs[key]
        return '/%s/' % self.dir if s == '' else '/%s/%s/' % (self.dir, s)

    def url(self, key):
        return BASE + self.path(key)

    def res(self, s):
        return re.sub(r'@@([\w-]+)@@', lambda m: self.path(m.group(1)), s)

    @property
    def WA(self):
        return WA_NUM + '?text=' + self.S['wa_default']

    @property
    def MAIL(self):
        return 'mailto:team@unbanz.com?subject=' + self.S['mail_subj']

    def wa(self, text):
        import urllib.parse
        return WA_NUM + '?text=' + urllib.parse.quote(text + ' ' + self.S['tag'], safe='')

    def _vt_cards(self):
        S = self.S
        out = []
        for c in VT_RAW:
            c = c.replace('<summary>Transcript</summary>', '<summary>%s</summary>' % S['vt_transcript'])
            for en_, aria, alt, lab_en, lab in S['vt_titles']:
                c = c.replace('aria-label="Play video: %s"' % en_, 'aria-label="%s"' % aria)
                c = c.replace('alt="%s"' % en_, 'alt="%s"' % alt)
                c = c.replace('<b>%s</b>' % lab_en, '<b>%s</b>' % lab)
            out.append(c)
        return out

    # ---- registry
    def reg(self, key, kind, title, desc, nav, **kw):
        assert key in self.slugs and key not in self.pages, key
        if not title.endswith('Unbanz') and len(title) + 9 <= 60:
            title = title + ' | Unbanz'
        d = dict(key=key, kind=kind, title=title, desc=desc, nav=nav, en=TWINS[key])
        d.update(kw)
        self.pages[key] = d
        self.order.append(key)
        return d

    # ---- chrome
    def header(self):
        S = self.S; p = self.path
        nav = ('<nav class="desktop-nav" aria-label="%s"><a href="%s">%s</a><a href="%s">%s</a><a href="%s">%s</a><a href="%s">%s</a><a href="%s">%s</a></nav>'
               % (S['nav_aria'], p('services'), S['n_services'], p('user'), S['n_user'], p('reviews'), S['n_reviews'], p('faq'), S['n_faq'], p('contact'), S['n_contact']))
        mobile = ('<nav class="mobile-nav" id="mobile-nav" hidden aria-label="%s"><a href="/%s/">%s</a><a href="%s">%s</a><a href="%s">%s</a>'
                  '<a href="%s">%s</a><a href="%s">%s</a><a href="%s">%s</a><a href="%s">%s</a>%s</nav>'
                  % (S['mnav_aria'], self.dir, S['n_home'], p('services'), S['n_services'], p('user'), S['n_user'], p('reviews'), S['n_reviews'],
                     p('how'), S['n_how'], p('faq'), S['n_faq'], p('contact'), S['n_contact'], SOCIAL))
        return nav, mobile

    def lang_links(self, key):
        """Footer links to the other languages for this page (twin if it exists, else that language's home)."""
        return lang_links_for(self.code, self.twin_map.get(key))

    def footer(self, key):
        S = self.S; p = self.path
        links = ''.join('<a href="%s">%s</a>' % (p(k), t) for k, t in S['foot_links'])
        links += self.lang_links(key)
        links += '<a href="/privacy/" hreflang="en" lang="en">Privacy</a><a href="/terms/" hreflang="en" lang="en">Terms</a>'
        return ('<footer class="site-footer container"><div class="footer-top"><a class="wordmark" href="/%s/">unbanz.</a>'
                '<p>%s' % (self.dir, S['foot_tag']) + FOOT_SOCIAL + '</p>'
                '<div class="footer-links">' + links + '</div></div>'
                '<div class="footer-bottom"><span>© <span id="year">2026</span> Unbanz</span>'
                '<span>%s</span>' % S['foot_indep'] +
                '<a href="mailto:team@unbanz.com?subject=%s">team@unbanz.com</a></div></footer>' % S['mail_subj'])

    @property
    def mobile_contact(self):
        S = self.S
        return ('<div class="mobile-contact"><a class="" href="%s">%s <span aria-hidden="true">↗︎</span></a><a href="%s">%s</a></div>'
                % (self.WA, S['mc_wa'], self.MAIL, S['mc_mail']))

    def cta_pair(self, label=None, mail=None):
        S = self.S
        return ('<div class="cta-pair"><a class="button button-blue" href="%s" data-service="%s">%s <span aria-hidden="true">↗︎</span></a>'
                '<a class="button button-light" href="%s">%s</a></div>') % (self.WA, self.svc[0], label or S['cta_quote'], self.MAIL, mail or S['cta_mail'])

    def hero_cta(self, label=None):
        S = self.S
        return ('<div class="hero-cta"><a class="button button-light" href="%s" data-service="%s">%s <span aria-hidden="true">↗︎</span></a>'
                '<a class="hero-email" href="%s">%s ↗︎</a></div>') % (self.WA, self.svc[0], label or S['hero_wa'], self.MAIL, S['hero_mail'])

    def faq_section(self, items, eyebrow=None, title=None):
        S = self.S
        det = ''.join('<details><summary>%s<span aria-hidden="true">+</span></summary><p>%s</p></details>' % (q, ans) for q, ans in items)
        return ('<section class="faq-section" id="faq"><div class="container faq-layout"><div class="faq-intro"><p class="eyebrow">%s</p>'
                '<h2>%s</h2></div><div class="simple-faq">%s</div></div></section>') % (eyebrow or S['faq_eyebrow'], title or S['faq_title'], det)

    def proof(self, title=None):
        return '<section class="service-proof container"><h2>%s</h2>%s</section>' % (title or self.S['proof_title'], self.cta_pair())

    def related_nav(self, keys, label=None):
        items = [self.pages[k] for k in keys if k in self.pages]
        return ('<nav class="related-services container" aria-label="%s">' % (label or self.S['related']) +
                ''.join('<a href="%s">%s</a>' % (self.path(d['key']), d['nav']) for d in items) + '</nav>')

    # ---- head
    def hreflang(self, d):
        return hreflang_block(self.code, d['en'], self.url(d['key']), self.twin_map.get(d['key']))

    def build_graph(self, d, faq_items, crumbs, service=None):
        S = self.S
        u = self.url(d['key'])
        wp = {"@type": "WebPage", "@id": u + "#webpage", "url": u, "name": d['title'], "description": plain(d['desc']),
              "isPartOf": {"@id": BASE + "/#website"}, "about": {"@id": BASE + "/#organization"}, "inLanguage": S['html_lang'],
              "primaryImageOfPage": {"@type": "ImageObject", "url": SHARE}, "breadcrumb": {"@id": u + "#breadcrumb"}}
        g = [ORG_NODE, WEBSITE_NODE, wp]
        if service:
            wp["mainEntity"] = {"@id": u + "#service"}
            s = {"@type": "Service", "@id": u + "#service", "url": u, "inLanguage": S['html_lang'],
                 "provider": {"@id": BASE + "/#organization"}, "areaServed": [{"@type": "Country", "name": S['country']}],
                 "availableChannel": {"@type": "ServiceChannel", "serviceUrl": WA_NUM},
                 "offers": {"@type": "Offer", "url": u, "availability": "https://schema.org/InStock",
                            "description": S['offer_desc'], "seller": {"@id": BASE + "/#organization"}}}
            s.update(service)
            g.append(s)
        g.append({"@type": "BreadcrumbList", "@id": u + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": h} for i, (n, h) in enumerate(crumbs)]})
        if faq_items:
            g.append({"@type": "FAQPage", "@id": u + "#faq", "url": u, "inLanguage": S['html_lang'], "mainEntity": [
                {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(ans)}} for q, ans in faq_items]})
        return g

    def head(self, d, faq_items, crumbs, service=None, vt=False):
        S = self.S
        u = self.url(d['key'])
        title = d['title']; desc = plain(d['desc'])
        h = ['<!doctype html>', '<html lang="%s">' % S['html_lang'], '<head>', '<meta charset="UTF-8">',
             '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">',
             '<meta name="theme-color" content="#73b7f3">',
             '<meta name="description" content="%s">' % a(desc),
             '<meta property="og:title" content="%s">' % a(title),
             '<meta property="og:description" content="%s">' % a(desc),
             '<meta property="og:type" content="website">',
             '<meta name="robots" content="index,follow,max-image-preview:large"><link rel="canonical" href="%s">%s' % (u, self.hreflang(d)),
             '<meta property="og:url" content="%s">' % u,
             '<meta property="og:locale" content="%s"><meta property="og:locale:alternate" content="en_US"><meta property="og:site_name" content="Unbanz">' % S['og_locale'],
             '<meta property="og:image" content="%s">' % SHARE,
             '<meta property="og:image:width" content="1200">', '<meta property="og:image:height" content="628">',
             '<meta property="og:image:alt" content="%s">' % a(S['og_alt']),
             '<meta name="twitter:site" content="@unbanzhq"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="%s"><meta name="twitter:description" content="%s"><meta name="twitter:image:alt" content="%s">' % (a(title), a(desc), a(S['og_alt'])),
             '<title>%s</title>' % html.escape(title, quote=False),
             '<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">',
             '<link rel="preload" href="/assets/unbanz-sans-latin.woff" as="font" type="font/woff" crossorigin>',
             '<meta property="og:image:type" content="image/jpeg"><meta name="twitter:image" content="%s"><link rel="stylesheet" href="%s"><script src="%s" defer></script>' % (SHARE, CSS, self.js_name())]
        if vt:
            h.append('<link rel="preconnect" href="https://cdn.dbimg.app"><link rel="stylesheet" href="%s"><script src="%s" defer></script>' % (TCSS, TJS))
        h.append('<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": self.build_graph(d, faq_items, crumbs, service)}, ensure_ascii=False, separators=(',', ':')) + '</script>')
        h.append(CLARITY)
        h.append('</head>')
        return '\n'.join(h)

    def js_name(self):
        fs = [f for f in os.listdir(os.path.join(ROOT, 'assets')) if f.startswith('site-%s.' % self.S['js_code']) and f.endswith('.js')]
        return '/assets/' + fs[0] if fs else '/assets/site-%s.PENDING.js' % self.S['js_code']

    def page_shell(self, d, main, faq_items, crumbs, service=None, vt=False, body_class='service-page'):
        S = self.S
        nav, mobile = self.header()
        top = ('<body class="%s"><a class="skip-link" href="#content">%s</a><header class="service-header container">'
               '<a class="wordmark" href="/%s/">unbanz.</a>%s<button class="menu-button" aria-label="%s" aria-expanded="false" aria-controls="mobile-nav">'
               '<span></span><span></span><span></span></button></header>%s\n') % (body_class, S['skip'], self.dir, nav, S['menu_open'], mobile)
        out = self.head(d, faq_items, crumbs, service, vt) + '\n' + top + main + '\n' + self.footer(d['key']) + '\n' + self.mobile_contact + '</body>\n</html>\n'
        return self.res(out)

    def crumb(self, label):
        return '<a class="crumb" href="/%s/">%s / %s</a>' % (self.dir, self.S['n_home'], label)

    def hero(self, h1, lead, crumb_label):
        return ('<section class="service-hero"><div class="container">%s<h1>%s</h1><p>%s</p>%s</div></section>'
                % (self.crumb(crumb_label), h1, lead, self.hero_cta()))

    # ---- generic pages
    def guide_page(self, key, h1, answer, secs, faq, related, help_html, crumb_label=None, std=True, extra_after=''):
        S = self.S
        d = self.pages[key]
        crumb_label = crumb_label or S['crumb_guides']
        body = ''.join('<h2 id="%s">%s</h2>%s' % (sid, h2, content) for sid, h2, content in secs)
        body += '<h2 id="help">%s</h2>' % S['help_h2'] + help_html
        if std:
            body += S['std_howto'] + S['std_safe'] + S['std_about']
        main = ('<main id="content">' + self.hero(h1, answer, crumb_label) + '<article class="guide-body container">' + body + '</article>' +
                extra_after + self.faq_section(faq) + self.proof() + self.related_nav(related) + '</main>')
        top = self.url('services') if crumb_label == S['crumb_services'] else self.url('faq')
        crumbs = [(S['n_home'], BASE + '/%s/' % self.dir), (crumb_label, top), (d['nav'], self.url(key))]
        return self.page_shell(d, main, faq, crumbs)

    def service_page(self, key, h1, answer, bold, cards1, steps, faq, guides, svc, extra=''):
        S = self.S
        d = self.pages[key]
        def art(items):
            return '<section class="service-editorial container">' + ''.join('<article><h2>%s</h2><p>%s</p></article>' % (h, p) for h, p in items) + '</section>'
        price = ('<section class="service-price container"><h2>%s</h2><div><p>%s</p><a href="%s">%s ↗︎</a></div></section>'
                 % (S['price_h2'], S['price_p'], self.path('pricing'), S['price_link']))
        gl = ('<section class="guide-links container"><h2>%s</h2>' % S['guides_h2'] + self.related_nav(guides, S['guides_h2']).replace(' container', '') + '</section>') if guides else ''
        main = ('<main id="content">' + self.hero(h1, answer, S['crumb_services']) +
                '<section class="answer-first container" style="padding-top:48px"><p style="max-width:860px;font-size:19px;line-height:1.5;margin:0"><strong>%s</strong></p></section>' % bold +
                art(cards1) + art(steps) + art(S['block3']) + price + extra + self.faq_section(faq, eyebrow=S['faq_eyebrow2']) + self.proof() + gl +
                self.related_nav(['services', 'ig', 'fb', 'snap', 'ad', 'fake', 'user', 'how', 'legit', 'reviews'], S['related_services']) + '</main>')
        crumbs = [(S['n_home'], BASE + '/%s/' % self.dir), (S['crumb_services'], self.url('services')), (d['nav'], self.url(key))]
        return self.page_shell(d, main, faq, crumbs, service=svc)

    def autodesc(self, answer, limit=158):
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

    def guide(self, key, title, nav, h1, answer, secs, faq, related, help_html, desc=None, svc='unban', std=True, crumb_label=None):
        self.reg(key, 'guide', title, desc or self.autodesc(answer), nav)
        def b():
            self.svc[0] = svc
            return self.guide_page(key, h1, answer, secs, faq, related, help_html, crumb_label=crumb_label, std=std)
        self.build[key] = b

    def service(self, key, title, nav, h1, answer, bold, cards1, steps, faq, guides, svcmeta, desc=None, svc='unban', extra=''):
        self.reg(key, 'service', title, desc or self.autodesc(answer), nav)
        def b():
            self.svc[0] = svc
            return self.service_page(key, h1, answer, bold, cards1, steps, faq, guides, svcmeta, extra=extra)
        self.build[key] = b


# ---------- hreflang cluster (shared across languages) ----------
LANG_TAGS = {'en': ['en', 'en-US'], 'fr': ['fr', 'fr-FR'], 'nl': ['nl', 'nl-NL'], 'es': ['es', 'es-ES'], 'pt-br': ['pt-BR']}
LANG_NAME = {'en': 'English', 'fr': 'Français', 'nl': 'Nederlands', 'es': 'Español', 'pt-br': 'Português'}
LANG_ATTR = {'en': 'en', 'fr': 'fr', 'nl': 'nl', 'es': 'es', 'pt-br': 'pt-BR'}
# registry filled by build.py: {lang: {twin_or_None: url}}; for pages without a twin, a page is its own cluster
CLUSTER = {}
LANG_HOME = {'en': BASE + '/', 'fr': BASE + '/fr/', 'nl': BASE + '/nl/', 'es': BASE + '/es/', 'pt-br': BASE + '/pt-br/'}

def hreflang_block(lang, twin, own_url, _unused=None):
    if twin is None:
        return ('<link rel="alternate" hreflang="%s" href="%s"><link rel="alternate" hreflang="x-default" href="%s">'
                % (LANG_ATTR[lang], own_url, own_url))
    out = []
    for lg in LANG_ORDER:
        u = CLUSTER.get(lg, {}).get(twin)
        if not u:
            continue
        for tag in LANG_TAGS[lg]:
            out.append('<link rel="alternate" hreflang="%s" href="%s">' % (tag, u))
    out.append('<link rel="alternate" hreflang="x-default" href="%s">' % CLUSTER['en'][twin])
    return ''.join(out)

def lang_links_for(cur, twin):
    out = []
    for lg in LANG_ORDER:
        if lg == cur:
            continue
        u = CLUSTER.get(lg, {}).get(twin) if twin is not None else None
        u = u or LANG_HOME[lg]
        href = u.replace(BASE, '') if lg != 'en' else u
        if lg == 'en':
            href = u
        out.append('<a href="%s" hreflang="%s" lang="%s">%s</a>' % (href, LANG_ATTR[lg], LANG_ATTR[lg], LANG_NAME[lg]))
    return ''.join(out)

Site.twin_map = TWINS

def meta(name, stype, desc):
    return {"name": name, "serviceType": stype, "description": desc}
