#!/usr/bin/env python3
"""Build the guide pages added on 2026-10-27 from the current instagram-two-factor-lost-access page (same template as the 2026-10-24 guides)."""
import os, re, sys, json, html
sys.path.insert(0, os.path.dirname(__file__)); sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'guides'))
import build_new as bn, build_classic as bc
import oct27_guides as og
ROOT = '/workspace/site'
TPL = 'instagram-two-factor-lost-access'
h = open(f'{ROOT}/guides/{TPL}/index.html', encoding='utf-8').read()
first_ld = h.find('<script type="application/ld+json">')
org = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S).group(1)
nodes = [n for n in json.loads(org)['@graph'] if n['@type'] in ('Organization', 'WebSite')]
parts = (h[:first_ld], nodes, h[h.find('<link rel="preload"'):h.find('<main id="content">') + len('<main id="content">')], h[h.find('</main>'):])
bn.TEMPLATE_SLUG = TPL
bn.OLD_TITLE = re.search(r'<title>(.*?)</title>', h).group(1)
bn.OLD_DESC = re.search(r'<meta name="description" content="(.*?)">', h).group(1)
bn.DATE_ISO, bn.DATE_TXT = '2026-10-27', '27 October 2026'
for g in og.GUIDES:
    out = bc.build_page(g, parts)
    d = f'{ROOT}/guides/{g["slug"]}'; os.makedirs(d, exist_ok=True)
    open(d + '/index.html', 'w', encoding='utf-8').write(out)
    print('wrote', g['slug'], len(out))
