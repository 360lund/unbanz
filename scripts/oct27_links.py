#!/usr/bin/env python3
"""Register the 10 pages added on 2026-10-27: sitemap, llms files, guides hub, and inbound links. Idempotent."""
import html, os, re, sys, json
sys.exit("Historic: already applied on 2026-10-27 (guides only). Country pages are registered by oct27b_links.py.")
sys.path.insert(0, os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import oct27_content as c, oct27_guides as og
DATE = c.DATE
def rd(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def wr(p, s): open(os.path.join(ROOT, p), 'w', encoding='utf-8').write(s)

pages = [(p['slug'], p['title'].replace(' | Unbanz', ''), p['desc']) for p in c.PAGES]
guides = [(g['slug'], g['h1'], g['desc']) for g in og.GUIDES]

# ---- sitemap
s = rd('sitemap.xml'); add = ''
for slug, _, _ in guides:
    u = 'https://unbanz.com/guides/%s/' % slug
    if u not in s: add += '<url><loc>%s</loc><lastmod>%s</lastmod></url>\n' % (u, DATE)
for slug, _, _ in pages:
    u = 'https://unbanz.com/%s/' % slug
    if u not in s: add += '<url><loc>%s</loc><lastmod>%s</lastmod></url>\n' % (u, DATE)
if add: wr('sitemap.xml', s.replace('</urlset>', add + '</urlset>'))

# ---- llms.txt
t = rd('llms.txt')
if 'instagram-account-recovery-bangladesh' not in t:
    blk = '### New pages (2026-10-27)\n\n' + ''.join('- [%s](https://unbanz.com/%s/): %s\n' % (ti, sl, de) for sl, ti, de in pages) + '\n'
    t = t.replace('\n## Guides\n', '\n' + blk.rstrip('\n') + '\n\n## Guides\n', 1)
    gl = ''.join('- [%s](https://unbanz.com/guides/%s/): %s\n' % (ti, sl, de) for sl, ti, de in guides)
    i = t.index('\n## Optional\n'); t = t[:i].rstrip('\n') + '\n' + gl + t[i:]
    wr('llms.txt', t)

# ---- llms-full.txt
f = rd('llms-full.txt')
if 'instagram-account-recovery-bangladesh' not in f:
    uk = [l for l in f.split('\n') if l.startswith('- Instagram Account Recovery in the UK: Official Help: ')][0]
    f = f.replace(uk, uk + '\n' + '\n'.join('- %s: https://unbanz.com/%s/ — %s' % (ti, sl, de) for sl, ti, de in pages), 1)
    ukb = [l for l in f.split('\n') if l.startswith('- [Instagram Account Recovery in the UK: Official Help](')][0]
    f = f.replace(ukb, ukb + '\n' + '\n'.join('- [%s](https://unbanz.com/%s/): %s' % (ti, sl, de) for sl, ti, de in pages), 1)
    i = f.index('\n## Contact\n'); f = f[:i].rstrip('\n') + '\n' + ''.join('- %s: https://unbanz.com/guides/%s/\n' % (ti, sl) for sl, ti, de in guides) + f[i:]
    wr('llms-full.txt', f)

# ---- guides hub (plain article cards + JSON-LD ItemList)
h = rd('guides/index.html')
art = ''
for sl, ti, de in guides:
    href = '/guides/%s/' % sl
    if 'href="%s"' % href in h: continue
    e = lambda x: html.escape(x, quote=True).replace('&quot;', '"')
    art += '<article><h2><a href="%s">%s</a></h2><p>%s</p><a href="%s">Read the guide ↗︎</a></article>' % (href, e(ti), e(de), href)
if art:
    m = re.search(r'(<section class="guide-cards container">.*?)(</section>)', h, re.S)
    h = h[:m.end(1)] + art + h[m.end(1):]
    jm = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', h, re.S)
    data = json.loads(jm.group(2)); done = False
    for node in data['@graph']:
        items = node.get('mainEntity', {}).get('itemListElement') if isinstance(node.get('mainEntity'), dict) else None
        if items is not None and node.get('@type') == 'CollectionPage':
            have = {i['url'] for i in items}
            for sl, ti, de in guides:
                u = 'https://unbanz.com/guides/%s/' % sl
                if u not in have: items.append({"@type": "ListItem", "position": len(items) + 1, "url": u, "name": ti}); done = True
    if done: h = h.replace(jm.group(0), jm.group(1) + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + jm.group(3))
    wr('guides/index.html', h)

# ---- inbound links (appended to the last "related-services" nav of each source page)
L = {k: v for k, v in {
 'g_fb_rej': ('/guides/facebook-disabled-appeal-rejected/', 'Facebook appeal rejected'),
 'g_fb_nr': ('/guides/facebook-account-disabled-for-no-reason/', 'Facebook disabled for no reason'),
 'g_fb_na': ('/guides/facebook-disabled-no-appeal-option/', 'Facebook disabled, no appeal option'),
 'g_fb_hk': ('/guides/hacker-changed-facebook-email-and-password/', 'Hacker changed Facebook email and password'),
 'g_ig_nr': ('/guides/instagram-appeal-sent-no-response/', 'Instagram appeal, no response'),
}.items()}
SRC = {
 '/guides/facebook-account-disabled-appeal/': ['g_fb_rej', 'g_fb_nr', 'g_fb_na'],
 '/facebook-account-disabled-appeal-help/': ['g_fb_rej', 'g_fb_nr', 'g_fb_na'],
 '/facebook-account-suspended-180-days/': ['g_fb_rej', 'g_fb_nr'],
 '/guides/facebook-account-locked/': ['g_fb_na', 'g_fb_nr'],
 '/guides/hacked-facebook-account-recovery/': ['g_fb_hk'],
 '/facebook-hacked-account-recovery-service/': ['g_fb_hk'],
 '/guides/facebook-lost-access-to-email-or-phone/': ['g_fb_hk'],
 '/facebook-account-recovery/': ['g_fb_rej', 'g_fb_hk'],
 '/facebook-unban-service/': ['g_fb_rej'],
 '/how-long-does-an-instagram-appeal-take/': ['g_ig_nr'],
 '/instagram-appeal-denied/': ['g_ig_nr'],
 '/guides/instagram-account-suspended-appeal/': ['g_ig_nr'],
 '/guides/instagram-check-account-status/': ['g_ig_nr'],
 '/instagram-account-recovery/': [],
 '/instagram-account-recovery-india/': [],
 '/instagram-account-recovery-usa/': [],
 '/instagram-account-recovery-uk/': [],
 '/instagram-account-recovery-uae/': [],
 '/guides/hacked-instagram-account-recovery/': [],
}
NAV = re.compile(r'<nav class="related-services container"[^>]*>.*?</nav>', re.S)
n = 0
for src, keys in SRC.items():
    path = os.path.join(ROOT, src.strip('/'), 'index.html')
    if not os.path.exists(path): print('MISSING', src); continue
    s = open(path, encoding='utf-8').read(); navs = list(NAV.finditer(s))
    if not navs: print('NO NAV', src); continue
    m = navs[-1]; block = m.group(0)
    add = ''.join('<a href="%s">%s</a>' % L[k] for k in keys if 'href="%s"' % L[k][0] not in s)
    if not add: continue
    s = s[:m.start()] + block[:-len('</nav>')] + add + '</nav>' + s[m.end():]
    open(path, 'w', encoding='utf-8').write(s); n += 1; print('updated', src)
print(n, 'pages linked')
