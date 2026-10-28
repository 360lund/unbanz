#!/usr/bin/env python3
"""Register the 6 reference pages added on 2026-10-28. Idempotent.
Default: sitemap, llms.txt, llms-full.txt. With --html: also inbound links in related-services navs."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import oct28_content as c
DATE = c.DATE
def rd(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def wr(p, s): open(os.path.join(ROOT, p), 'w', encoding='utf-8').write(s)
pages = [(p['slug'], p['title'].replace(' | Unbanz', ''), p['desc']) for p in c.PAGES]

s = rd('sitemap.xml'); add = ''
for slug, _, _ in pages:
    u = 'https://unbanz.com/%s/' % slug
    if u not in s: add += '<url><loc>%s</loc><lastmod>%s</lastmod></url>\n' % (u, DATE)
if add: wr('sitemap.xml', s.replace('</urlset>', add + '</urlset>'))

MARK = '### New pages (2026-10-28)'
t = rd('llms.txt')
if MARK not in t:
    blk = MARK + '\n\n' + ''.join('- [%s](https://unbanz.com/%s/): %s\n' % (ti, sl, de) for sl, ti, de in pages)
    t = t.replace('\n## Guides\n', '\n' + blk + '\n## Guides\n', 1)
    t = t.replace('Last updated: 2026-10-25', 'Last updated: ' + DATE, 1)
    wr('llms.txt', t)
f = rd('llms-full.txt')
if 'instagram-recovery-glossary' not in f:
    i = f.index('\n## Contact\n')
    f = f[:i].rstrip('\n') + '\n' + ''.join('- %s: https://unbanz.com/%s/\n' % (ti, sl) for sl, ti, de in pages) + f[i:]
    f = f.replace('Last updated: 2026-10-25', 'Last updated: ' + DATE, 1)
    wr('llms-full.txt', f)

if '--html' in sys.argv:
    L = {k: ('/%s/' % k, v) for k, v in {
     'instagram-account-disabled-vs-suspended-vs-restricted': 'Disabled vs suspended vs restricted',
     'ways-to-get-a-banned-instagram-account-back': 'Ways to get a banned Instagram account back',
     'instagram-username-claim-routes': 'Username claim routes compared',
     'meta-ad-account-restricted-vs-disabled': 'Meta ad account restricted vs disabled',
     'instagram-appeal-checklist': 'Instagram appeal checklist',
     'instagram-recovery-glossary': 'Recovery glossary'}.items()}
    SRC = {
     '/instagram-account-recovery/': ['instagram-account-disabled-vs-suspended-vs-restricted', 'ways-to-get-a-banned-instagram-account-back', 'instagram-appeal-checklist'],
     '/instagram-account-disabled-appeal/': ['instagram-appeal-checklist', 'instagram-account-disabled-vs-suspended-vs-restricted'],
     '/instagram-appeal-denied/': ['instagram-appeal-checklist', 'ways-to-get-a-banned-instagram-account-back'],
     '/best-instagram-recovery-service/': ['ways-to-get-a-banned-instagram-account-back'],
     '/instagram-username-claim/': ['instagram-username-claim-routes'],
     '/instagram-username-swap-vs-claim/': ['instagram-username-claim-routes'],
     '/inactive-instagram-username/': ['instagram-username-claim-routes'],
     '/meta-ad-account-restricted/': ['meta-ad-account-restricted-vs-disabled'],
     '/guides/meta-ad-account-restricted/': ['meta-ad-account-restricted-vs-disabled'],
     '/guides/instagram-check-account-status/': ['instagram-account-disabled-vs-suspended-vs-restricted', 'instagram-recovery-glossary'],
     '/guides/why-instagram-bans-accounts/': ['instagram-account-disabled-vs-suspended-vs-restricted'],
     '/faq/': ['instagram-recovery-glossary'],
     '/compare/': ['ways-to-get-a-banned-instagram-account-back'],
    }
    NAV = re.compile(r'<nav class="related-services container"[^>]*>.*?</nav>', re.S)
    n = 0
    for src, keys in SRC.items():
        path = os.path.join(ROOT, src.strip('/'), 'index.html')
        if not os.path.exists(path): print('MISSING', src); continue
        h = open(path, encoding='utf-8').read(); navs = list(NAV.finditer(h))
        if not navs: print('NO NAV', src); continue
        m = navs[-1]; block = m.group(0)
        a = ''.join('<a href="%s">%s</a>' % L[k] for k in keys if 'href="%s"' % L[k][0] not in h)
        if not a: continue
        open(path, 'w', encoding='utf-8').write(h[:m.start()] + block[:-len('</nav>')] + a + '</nav>' + h[m.end():]); n += 1; print('updated', src)
    print(n, 'pages linked')
