#!/usr/bin/env python3
"""Register the high-income country pages added on 2026-10-27: sitemap, llms files, inbound links, and 301s for the five removed low-income pages. Idempotent."""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import oct27b_content as c
DATE = c.DATE
def rd(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def wr(p, s): open(os.path.join(ROOT, p), 'w', encoding='utf-8').write(s)
pages = [(p['slug'], p['title'].replace(' | Unbanz', ''), p['desc']) for p in c.PAGES]

# ---- sitemap
s = rd('sitemap.xml'); add = ''
for slug, _, _ in pages:
    u = 'https://unbanz.com/%s/' % slug
    if u not in s: add += '<url><loc>%s</loc><lastmod>%s</lastmod></url>\n' % (u, DATE)
if add: wr('sitemap.xml', s.replace('</urlset>', add + '</urlset>'))

# ---- llms.txt
t = rd('llms.txt')
if 'instagram-account-recovery-australia' not in t:
    lines = ''.join('- [%s](https://unbanz.com/%s/): %s\n' % (ti, sl, de) for sl, ti, de in pages)
    t = t.replace('### New pages (2026-10-27)\n', '### New pages (2026-10-27)\n\n' + lines.rstrip('\n') + '\n', 1)
    wr('llms.txt', t)

# ---- llms-full.txt
f = rd('llms-full.txt')
if 'instagram-account-recovery-australia' not in f:
    uk = [l for l in f.split('\n') if l.startswith('- Instagram Account Recovery in the UK: Official Help: ')][0]
    f = f.replace(uk, uk + '\n' + '\n'.join('- %s: https://unbanz.com/%s/ — %s' % (ti, sl, de) for sl, ti, de in pages), 1)
    ukb = [l for l in f.split('\n') if l.startswith('- [Instagram Account Recovery in the UK: Official Help](')][0]
    f = f.replace(ukb, ukb + '\n' + '\n'.join('- [%s](https://unbanz.com/%s/): %s' % (ti, sl, de) for sl, ti, de in pages), 1)
    wr('llms-full.txt', f)

# ---- inbound links (appended to the last related-services nav)
IG = [('instagram-account-recovery-' + k, 'Recovery in ' + v) for k, v in [
 ('australia', 'Australia'), ('canada', 'Canada'), ('switzerland', 'Switzerland'), ('israel', 'Israel'), ('singapore', 'Singapore'),
 ('norway', 'Norway'), ('sweden', 'Sweden'), ('denmark', 'Denmark'), ('ireland', 'Ireland'), ('new-zealand', 'New Zealand'),
 ('germany', 'Germany'), ('austria', 'Austria'), ('qatar', 'Qatar'), ('saudi-arabia', 'Saudi Arabia'), ('japan', 'Japan')]]
FB = [('facebook-account-recovery-' + k, 'Facebook recovery in ' + v) for k, v in [
 ('australia', 'Australia'), ('canada', 'Canada'), ('switzerland', 'Switzerland'), ('israel', 'Israel')]]
def L(lst, names=None): return [('/%s/' % s, l) for s, l in lst if names is None or s.split('-', 3)[-1] in names or s.split('recovery-', 1)[1] in names]
SRC = {
 '/instagram-account-recovery/': L(IG),
 '/facebook-account-recovery/': L(FB),
 '/instagram-account-recovery-uk/': L(IG, ['ireland', 'australia', 'canada', 'germany']),
 '/instagram-account-recovery-usa/': L(IG, ['canada', 'australia', 'ireland', 'japan']),
 '/instagram-account-recovery-uae/': L(IG, ['qatar', 'saudi-arabia', 'israel', 'singapore']),
 '/instagram-account-recovery-india/': L(IG, ['singapore', 'australia', 'canada']),
 '/guides/hacked-instagram-account-recovery/': L(IG, ['australia', 'canada', 'switzerland', 'israel', 'germany', 'japan']),
 '/instagram-hacked-account-recovery-service/': L(IG, ['australia', 'canada', 'switzerland', 'israel']),
 '/guides/hacked-facebook-account-recovery/': L(FB),
 '/facebook-hacked-account-recovery-service/': L(FB),
 '/facebook-ad-account-disabled-australia/': L(FB, ['australia']),
 '/facebook-ad-account-disabled-canada/': L(FB, ['canada']),
}
NAV = re.compile(r'<nav class="related-services container"[^>]*>.*?</nav>', re.S)
n = 0
for src, links in SRC.items():
    path = os.path.join(ROOT, src.strip('/'), 'index.html')
    if not os.path.exists(path): print('MISSING', src); continue
    s = open(path, encoding='utf-8').read(); navs = list(NAV.finditer(s))
    if not navs: print('NO NAV', src); continue
    m = navs[-1]; block = m.group(0)
    add = ''.join('<a href="%s">%s</a>' % (u, l) for u, l in links if 'href="%s"' % u not in s)
    if not add: continue
    s = s[:m.start()] + block[:-len('</nav>')] + add + '</nav>' + s[m.end():]
    open(path, 'w', encoding='utf-8').write(s); n += 1; print('updated', src)
    sm = rd('sitemap.xml'); u = 'https://unbanz.com' + src
    sm = re.sub(r'(<loc>%s</loc><lastmod>)[^<]*' % re.escape(u), r'\g<1>' + DATE, sm); wr('sitemap.xml', sm)
print(n, 'pages linked')

# ---- redirects for the five removed pages
v = rd('vercel.json')
RED = {'instagram-account-recovery-bangladesh': 'instagram-account-recovery', 'instagram-account-recovery-pakistan': 'instagram-account-recovery',
       'instagram-account-recovery-nigeria': 'instagram-account-recovery', 'facebook-account-recovery-india': 'facebook-account-recovery',
       'facebook-account-recovery-bangladesh': 'facebook-account-recovery'}
if 'instagram-account-recovery-bangladesh' not in v:
    j = json.loads(v); new = []
    for k, d in RED.items():
        for src in ('/%s' % k, '/%s/' % k):
            new.append({'source': src, 'destination': '/%s/' % d, 'permanent': True})
    j['redirects'].extend(new)
    wr('vercel.json', json.dumps(j, indent=2, ensure_ascii=False) + '\n')
