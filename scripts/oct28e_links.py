#!/usr/bin/env python3
"""Register the white label agency pages: sitemap, llms files, inbound links. Idempotent."""
import os, re, sys, html
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATE = '2026-10-28'
def rd(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def wr(p, s): open(os.path.join(ROOT, p), 'w', encoding='utf-8').write(s)
urls = [l.strip().replace('https://unbanz.com', '') for l in open('/tmp/wl_urls.txt') if l.strip()]
pages = []
for u in urls:
    h = rd(u.strip('/') + '/index.html')
    ti = html.unescape(re.search(r'<title>(.*?)</title>', h, re.S).group(1)).replace(' | Unbanz', '')
    de = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', h).group(1))
    pages.append((u, ti, de))

s = rd('sitemap.xml'); add = ''
for u, _, _ in pages:
    full = 'https://unbanz.com' + u
    if full not in s: add += '<url><loc>%s</loc><lastmod>%s</lastmod></url>\n' % (full, DATE)
if add: wr('sitemap.xml', s.replace('</urlset>', add + '</urlset>'))

t = rd('llms.txt')
if '/white-label-agency/' not in t:
    lines = ''.join('- [%s](https://unbanz.com%s): %s\n' % (ti, u, de) for u, ti, de in pages)
    t = t.replace('### New pages (2026-10-28)\n\n', '### New pages (2026-10-28)\n\n' + lines + '\n', 1)
    wr('llms.txt', t)

f = rd('llms-full.txt')
if '/white-label-agency/' not in f:
    uk = [l for l in f.split('\n') if l.startswith('- Instagram Account Recovery in the UK: Official Help: ')][0]
    f = f.replace(uk, uk + '\n' + '\n'.join('- %s: https://unbanz.com%s — %s' % (ti, u, de) for u, ti, de in pages), 1)
    ukb = [l for l in f.split('\n') if l.startswith('- [Instagram Account Recovery in the UK: Official Help](')][0]
    f = f.replace(ukb, ukb + '\n' + '\n'.join('- [%s](https://unbanz.com%s): %s' % (ti, u, de) for u, ti, de in pages), 1)
    wr('llms-full.txt', f)

H = ('/white-label-agency/', 'White label for agencies')
SRC = {
 '/services/': [H], '/agency-ad-account-recovery/': [H], '/account-recovery-by-country/': [H, ('/white-label-agency-uk/', 'White label in the UK'), ('/white-label-agency-usa/', 'White label in the USA')],
 '/instagram-account-recovery/': [H], '/facebook-account-recovery/': [H], '/instagram-username-claim/': [H],
 '/nl/diensten/': [('/nl/white-label-bureau/', 'White label voor bureaus')],
 '/es/servicios/': [('/es/white-label-agencias/', 'White label para agencias')],
 '/pt-br/servicos/': [('/pt-br/white-label-agencias/', 'White label para agências')],
 '/fr/services/': [('/fr/white-label-agences/', 'White label pour agences')],
}
NAV = re.compile(r'<nav class="related-services[^"]*"[^>]*>.*?</nav>', re.S)
changed = []
for src, links in SRC.items():
    path = os.path.join(ROOT, src.strip('/'), 'index.html')
    s = open(path, encoding='utf-8').read(); navs = list(NAV.finditer(s))
    if not navs: print('NO NAV', src); continue
    m = navs[-1]; block = m.group(0)
    add = ''.join('<a href="%s">%s</a>' % (u, l) for u, l in links if 'href="%s"' % u not in s)
    if not add: continue
    s = s[:m.start()] + block[:-len('</nav>')] + add + '</nav>' + s[m.end():]
    open(path, 'w', encoding='utf-8').write(s); changed.append(src); print('updated', src)
    sm = rd('sitemap.xml'); u = 'https://unbanz.com' + src
    sm = re.sub(r'(<loc>%s</loc><lastmod>)[^<]*' % re.escape(u), r'\g<1>' + DATE, sm); wr('sitemap.xml', sm)
open('/tmp/wl_changed.txt', 'w').write(''.join('https://unbanz.com%s\n' % c for c in changed))
print(len(pages), 'pages registered,', len(changed), 'linked')
