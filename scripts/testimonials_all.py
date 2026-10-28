#!/usr/bin/env python3
"""Show ALL testimonials on every service / country / white-label / agency page (EN + fr/nl/es/pt-br).
Same component as /reviews/ (vt-page carousel: larger cards, phone auto-swipe + loop from testimonials.js), cards copied
verbatim from each language's reviews page. Idempotent post-pass: run it AFTER any page generator (the generators'
own 1-3 card testimonial blocks are replaced) -> python3 scripts/testimonials_all.py
Adds hashed assets/testimonials.<hash>.css/.js (old hashed files stay for browser caches) and updates the head refs."""
import re, os, glob, hashlib, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda x: os.path.join(R, x)
css, js = open(P('scripts/testimonials.css')).read(), open(P('scripts/testimonials.js')).read()
H = hashlib.md5((css + js).encode()).hexdigest()[:10]
for ext, src in (('css', css), ('js', js)):
    p = P(f'assets/testimonials.{H}.{ext}')
    if not os.path.exists(p): open(p, 'w').write(src)
HEAD = f'<link rel="stylesheet" href="/assets/testimonials.{H}.css"><script src="/assets/testimonials.{H}.js" defer></script>'
PRE = '<link rel="preconnect" href="https://cdn.dbimg.app">'
LANGS = {  # dir -> (reviews page the cards come from, eyebrow, heading)
    '': ('reviews/index.html', 'CLIENTS', 'What clients say'),
    'fr': ('fr/avis/index.html', 'CLIENTS', 'Avec leurs mots.'),
    'nl': ('nl/reviews/index.html', 'KLANTEN', 'In hun eigen woorden.'),
    'es': ('es/opiniones/index.html', 'CLIENTES', 'En sus propias palabras.'),
    'pt-br': ('pt-br/avaliacoes/index.html', 'CLIENTES', 'Com as próprias palavras.'),
}
def lang(f): d = f.split('/')[0]; return d if d in LANGS and d else ''
def section(l):
    page, eb, h2 = LANGS[l]
    cards = re.findall(r'<li class="vt-card".*?</li>', open(P(page)).read(), re.S)
    assert len(cards) == 5, (page, len(cards))
    return ('<section class="vt vt-page svc-testi container" aria-labelledby="vt-title"><div class="vt-head"><div><p class="eyebrow">%s</p>'
            '<h2 id="vt-title">%s</h2></div></div><ul class="vt-track">%s</ul></section>' % (eb, h2, ''.join(cards)))
SEC = {l: section(l) for l in LANGS}
OLD = re.compile(r'<section class="vt container svc-testi"[^>]*>.*?</ul></section>', re.S)
FAQ = re.compile(r'<section[^>]*(?:class="faq(?:-section)?"|id="faq")')
# extra pages (no section today) that get one: EN best-instagram-recovery-service + native pages whose EN twin has one
EXTRA = {'best-instagram-recovery-service/index.html'}
def native_extra(f):
    if lang(f) == '' or f.count('/') != 2: return False
    s = open(f).read()
    m = re.search(r'hreflang="en"[^>]*href="https://unbanz.com/([^"]+)"|href="https://unbanz.com/([^"]+)"[^>]*hreflang="en"', s)
    if not m: return False
    en = (m.group(1) or m.group(2)) + 'index.html'
    if en.startswith('guides/') or en == 'reviews/index.html' or not os.path.exists(en): return False
    return 'class="vt ' in open(en).read() and 'svc-testi' in open(en).read() or en in EXTRA
def process(f):
    s = open(f).read(); l = lang(f)
    if OLD.search(s): n = OLD.sub(lambda m: SEC[l], s, count=1)
    elif (f in EXTRA or native_extra(f)) and 'class="vt ' not in s and (m := FAQ.search(s)): n = s[:m.start()] + SEC[l] + s[m.start():]
    else: return False
    if '/assets/testimonials.' in n: n = re.sub(r'<link rel="stylesheet" href="/assets/testimonials\.\w+\.css"><script src="/assets/testimonials\.\w+\.js" defer></script>', lambda m: HEAD, n, count=1)
    else: n = n.replace('</head>', ('' if PRE in n else PRE) + HEAD + '</head>', 1)
    if n != s: open(f, 'w').write(n); return True
    return False
if __name__ == '__main__':
    os.chdir(R)
    done = [f for f in sorted(glob.glob('**/index.html', recursive=True)) if f not in ('index.html',) and process(f)]
    print('updated', len(done), 'pages; assets', H)
    open('/tmp/testi_changed.txt', 'w').write('\n'.join(done))
