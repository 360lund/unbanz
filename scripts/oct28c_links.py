#!/usr/bin/env python3
"""Register the 2026-10-28 country pages: sitemap, llms files, inbound links. Idempotent."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import build_oct28c_pages as bp
DATE = bp.b.DATE
def rd(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def wr(p, s): open(os.path.join(ROOT, p), 'w', encoding='utf-8').write(s)
pages = [(p['slug'], p['title'].replace(' | Unbanz', ''), p['desc']) for p in bp.PAGES]

# ---- sitemap
s = rd('sitemap.xml'); add = ''
for slug, _, _ in pages:
    u = 'https://unbanz.com/%s/' % slug
    if u not in s: add += '<url><loc>%s</loc><lastmod>%s</lastmod></url>\n' % (u, DATE)
if add: wr('sitemap.xml', s.replace('</urlset>', add + '</urlset>'))

# ---- llms.txt
t = rd('llms.txt')
if 'instagram-account-recovery-netherlands' not in t:
    lines = ''.join('- [%s](https://unbanz.com/%s/): %s\n' % (ti, sl, de) for sl, ti, de in pages)
    t = t.replace('### New pages (2026-10-27)\n', '### New pages (2026-10-28)\n\n' + lines.rstrip('\n') + '\n\n### New pages (2026-10-27)\n', 1)
    wr('llms.txt', t)

# ---- llms-full.txt
f = rd('llms-full.txt')
if 'instagram-account-recovery-netherlands' not in f:
    uk = [l for l in f.split('\n') if l.startswith('- Instagram Account Recovery in the UK: Official Help: ')][0]
    f = f.replace(uk, uk + '\n' + '\n'.join('- %s: https://unbanz.com/%s/ — %s' % (ti, sl, de) for sl, ti, de in pages), 1)
    ukb = [l for l in f.split('\n') if l.startswith('- [Instagram Account Recovery in the UK: Official Help](')][0]
    f = f.replace(ukb, ukb + '\n' + '\n'.join('- [%s](https://unbanz.com/%s/): %s' % (ti, sl, de) for sl, ti, de in pages), 1)
    wr('llms-full.txt', f)

# ---- inbound links (appended to the last related-services nav)
NAMES = {'netherlands': 'the Netherlands', 'belgium': 'Belgium', 'luxembourg': 'Luxembourg', 'finland': 'Finland', 'iceland': 'Iceland', 'italy': 'Italy', 'spain': 'Spain', 'portugal': 'Portugal', 'france': 'France',
 'south-korea': 'South Korea', 'hong-kong': 'Hong Kong', 'taiwan': 'Taiwan', 'kuwait': 'Kuwait', 'bahrain': 'Bahrain', 'oman': 'Oman', 'malta': 'Malta', 'cyprus': 'Cyprus', 'monaco': 'Monaco',
 'liechtenstein': 'Liechtenstein', 'czech-republic': 'the Czech Republic', 'poland': 'Poland', 'estonia': 'Estonia', 'slovenia': 'Slovenia'}
UN = {'uk': 'the UK', 'uae': 'the UAE', 'australia': 'Australia', 'canada': 'Canada', 'germany': 'Germany', 'switzerland': 'Switzerland'}
HUB = ('/account-recovery-by-country/', 'Recovery by country')
def ig(*ks): return [('/instagram-account-recovery-%s/' % k, 'Recovery in ' + NAMES[k]) for k in ks]
def fb(*ks): return [('/facebook-account-recovery-%s/' % k, 'Facebook recovery in ' + NAMES[k]) for k in ks]
def un(*ks): return [('/instagram-username-claim-%s/' % k, 'Username claim in ' + UN[k]) for k in ks]
TOP_IG = ig('netherlands', 'belgium', 'luxembourg', 'finland', 'italy', 'spain', 'france', 'south-korea', 'hong-kong', 'kuwait')
TOP_FB = fb('netherlands', 'belgium', 'luxembourg', 'finland', 'italy', 'spain', 'france', 'south-korea', 'hong-kong', 'kuwait')
SRC = {
 '/instagram-account-recovery/': [HUB] + ig(*NAMES) ,
 '/facebook-account-recovery/': [HUB] + TOP_FB,
 '/instagram-account-recovery-uk/': [HUB] + ig('netherlands', 'france', 'malta', 'spain') + un('uk'),
 '/instagram-account-recovery-usa/': [HUB] + ig('south-korea', 'hong-kong', 'spain', 'france'),
 '/instagram-account-recovery-uae/': [HUB] + ig('kuwait', 'bahrain', 'oman') + un('uae'),
 '/instagram-account-recovery-india/': [],
 '/instagram-account-recovery-australia/': [HUB] + ig('hong-kong', 'south-korea') + un('australia'),
 '/facebook-account-recovery-australia/': [HUB] + fb('hong-kong', 'south-korea'),
 '/instagram-account-recovery-canada/': [HUB] + ig('france', 'netherlands') + un('canada'),
 '/facebook-account-recovery-canada/': [HUB] + fb('france', 'netherlands'),
 '/instagram-account-recovery-germany/': [HUB] + ig('poland', 'czech-republic', 'netherlands', 'belgium', 'luxembourg') + un('germany'),
 '/instagram-account-recovery-switzerland/': [HUB] + ig('liechtenstein', 'italy', 'france', 'monaco') + un('switzerland'),
 '/facebook-account-recovery-switzerland/': [HUB] + fb('italy', 'france'),
 '/instagram-account-recovery-austria/': [HUB] + ig('czech-republic', 'slovenia', 'liechtenstein', 'italy'),
 '/instagram-account-recovery-ireland/': [HUB] + ig('malta', 'netherlands'),
 '/instagram-account-recovery-denmark/': [HUB] + ig('finland', 'iceland', 'estonia'),
 '/instagram-account-recovery-sweden/': [HUB] + ig('finland', 'iceland', 'estonia'),
 '/instagram-account-recovery-norway/': [HUB] + ig('finland', 'iceland', 'estonia'),
 '/instagram-account-recovery-new-zealand/': [HUB] + ig('hong-kong'),
 '/instagram-account-recovery-japan/': [HUB] + ig('south-korea', 'hong-kong', 'taiwan'),
 '/instagram-account-recovery-singapore/': [HUB] + ig('hong-kong', 'taiwan', 'south-korea'),
 '/instagram-account-recovery-israel/': [HUB] + ig('cyprus', 'malta'),
 '/facebook-account-recovery-israel/': [HUB] + fb('kuwait'),
 '/instagram-account-recovery-qatar/': [HUB] + ig('kuwait', 'bahrain', 'oman'),
 '/instagram-account-recovery-saudi-arabia/': [HUB] + ig('kuwait', 'bahrain', 'oman'),
 '/guides/hacked-instagram-account-recovery/': [HUB] + ig('netherlands', 'france', 'italy', 'spain', 'south-korea', 'hong-kong'),
 '/instagram-hacked-account-recovery-service/': [HUB] + ig('netherlands', 'france', 'italy', 'spain'),
 '/guides/hacked-facebook-account-recovery/': [HUB] + fb('netherlands', 'france', 'italy', 'spain'),
 '/facebook-hacked-account-recovery-service/': [HUB] + fb('netherlands', 'france', 'italy', 'spain'),
 '/guides/': [HUB],
 '/username/': un('uk', 'uae', 'australia', 'canada', 'germany', 'switzerland'),
 '/instagram-username-claim/': un('uk', 'uae', 'australia', 'canada', 'germany', 'switzerland'),
 '/instagram-username-claim-usa/': un('uk', 'canada', 'australia', 'germany'),
 '/trademark-username-claim/': un('uk', 'australia', 'canada', 'germany', 'switzerland', 'uae'),
}
# the new pages link back to the hub through their own related nav; the hub lists them all
NAV = re.compile(r'<nav class="related-services[^"]*"[^>]*>.*?</nav>', re.S)
n = 0; changed = []
for src, links in SRC.items():
    if not links: continue
    path = os.path.join(ROOT, src.strip('/'), 'index.html')
    if not os.path.exists(path): print('MISSING', src); continue
    s = open(path, encoding='utf-8').read(); navs = list(NAV.finditer(s))
    if not navs: print('NO NAV', src); continue
    m = navs[-1]; block = m.group(0)
    add = ''.join('<a href="%s">%s</a>' % (u, l) for u, l in links if 'href="%s"' % u not in s)
    if not add: continue
    s = s[:m.start()] + block[:-len('</nav>')] + add + '</nav>' + s[m.end():]
    open(path, 'w', encoding='utf-8').write(s); n += 1; changed.append(src); print('updated', src)
    sm = rd('sitemap.xml'); u = 'https://unbanz.com' + src
    sm = re.sub(r'(<loc>%s</loc><lastmod>)[^<]*' % re.escape(u), r'\g<1>' + DATE, sm); wr('sitemap.xml', sm)
print(n, 'pages linked')
open('/workspace/changed_pages_oct28_countries.txt', 'w').write(''.join('https://unbanz.com%s\n' % c for c in changed))
