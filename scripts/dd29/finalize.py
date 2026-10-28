# -*- coding: utf-8 -*-
import os, re, html
import write_all as W
from lib import PAGES, ROOT
import nat29
W.main(write=False)
ORDER = ['ad','ighacked','user','igsusp','igappeal','fbdis','igverify','igrecov','igrestrict','fbrecov','fblost','snap','hubig','hubfb','hubsc']
fi = lambda f: ORDER.index(f) if f in ORDER else 99
items = []   # (slug, title, desc)
for p in sorted(PAGES, key=lambda p: fi(p['fam'])): items.append((p['slug'], p['title'], p['desc']))
def meta(path):
    s = open(os.path.join(ROOT, path, 'index.html'), encoding='utf-8').read()
    t = html.unescape(re.search(r'<title>(.*?)</title>', s).group(1)); d = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', s).group(1))
    return t, d
for pth in nat29.paths(): t, d = meta(pth); items.append((pth, t, d))
open('/workspace/new_pages_oct29_double_down.txt', 'w').write('\n'.join('https://unbanz.com/%s/' % s for s, _, _ in items) + '\n')
sm = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
add = ''.join('<url><loc>https://unbanz.com/%s/</loc><lastmod>2026-10-29</lastmod></url>\n' % s for s, _, _ in items if 'https://unbanz.com/%s/</loc>' % s not in sm)
if add: sm = sm.replace('</urlset>', add + '</urlset>'); open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm)
def app(fn, fmt):
    f = os.path.join(ROOT, fn); s = open(f, encoding='utf-8').read()
    if '## Account help situations (2026-10-29)' in s: return 0
    body = '\n'.join(fmt % (t, 'https://unbanz.com/%s/' % sl, d) for sl, t, d in items)
    s = s.rstrip('\n') + '\n\n## Account help situations (2026-10-29)\n\n' + body + '\n'
    open(f, 'w', encoding='utf-8').write(s); return 1
app('llms.txt', '- [%s](%s): %s'); app('llms-full.txt', '- %s: %s — %s')
print(len(items), 'items')
