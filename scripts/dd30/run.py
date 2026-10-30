# -*- coding: utf-8 -*-
import os, sys, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'dd29')); sys.path.append(os.path.join(HERE, '..'))
from cta_note import write_page
import lib
lib.DATE = '2026-10-30'; lib.DATE_LONG = '30 October 2026'
from content import *
from lib import ROOT, FAM, esc
TR = set(l.split('/')[0] for l in subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True).stdout.split('\n') if l)
WIN = {'Instagram in the Gulf and Switzerland': ('/instagram-account-recovery-uae/', 'Instagram recovery UAE'), 'Inactive usernames': ('/inactive-instagram-username/', 'Inactive Instagram usernames'),
       'Snapchat locks': ('/snapchat-account-ban-service/', 'Snapchat ban help'), 'Facebook recovery by country': ('/guides/facebook-account-disabled-appeal/', 'Facebook disabled appeal'),
       'Username claims by country': ('/username/', 'Username claims')}
def exists(u): return os.path.exists(os.path.join(ROOT, u.strip('/'), 'index.html')) or u.strip('/') in [p['slug'] for p in PAGES]
BYS = {p['slug']: p for p in PAGES}
def L(p): return ('/%s/' % p['slug'], p['crumb'])
def main():
    bad = set()
    for p in PAGES:
        if p['slug'] in TR: raise SystemExit('COLLISION ' + p['slug'])
        for s in p['sections']:
            for u in re.findall(r'href="(/[^"]*)"', s):
                if not exists(u): bad.add((p['slug'], u))
    if bad: raise SystemExit('BROKEN %s' % sorted(bad))
    for g, slugs in GROUPS.items():
        grp = [BYS[s] for s in slugs]
        for i, p in enumerate(grp):
            sib = [grp[(i + k) % len(grp)] for k in range(1, len(grp))]
            p['related_final'] = ([FAM[p['fam']]['parent'], WIN[g]] + [L(q) for q in sib[:4]], [L(q) for q in sib[4:8]] + [('/how-it-works/', 'How Unbanz works')])
            h = lib.build(p, None); d = os.path.join(ROOT, p['slug']); os.makedirs(d, exist_ok=True); write_page(os.path.join(d, 'index.html'), h)
    def nav(label, links): return '<nav class="related-services container" aria-label="%s" data-dd30="1">%s</nav>' % (label, ''.join('<a href="%s">%s</a>' % (u, esc(t)) for u, t in links))
    def patch(u, label, slugs):
        f = os.path.join(ROOT, u.strip('/'), 'index.html')
        if not os.path.exists(f): print('skip', u); return
        s = open(f, encoding='utf-8').read()
        if 'data-dd30="1"' in s or s.count('</main>') != 1: print('nopatch', u); return
        open(f, 'w', encoding='utf-8').write(s.replace('</main>', nav(label, [L(BYS[x]) for x in slugs if x != u.strip('/')]) + '</main>', 1))
    G = GROUPS
    patch('/instagram-account-recovery-uae/', 'More help in the Gulf and Switzerland', G['Instagram in the Gulf and Switzerland'])
    patch('/instagram-account-recovery-switzerland/', 'More Instagram help in Switzerland and the Gulf', G['Instagram in the Gulf and Switzerland'][-2:] + G['Instagram in the Gulf and Switzerland'][:3])
    patch('/instagram-account-recovery-saudi-arabia/', 'More Instagram help in Saudi Arabia and the Gulf', G['Instagram in the Gulf and Switzerland'][3:7])
    patch('/inactive-instagram-username/', 'Inactive usernames by country', G['Inactive usernames'])
    patch('/snapchat-account-ban-service/', 'Snapchat locks by country', G['Snapchat locks'])
    patch('/snapchat-unban-service/', 'Snapchat locks by country', G['Snapchat locks'])
    patch('/guides/snapchat-device-banned-appeal/', 'Snapchat locks by country', G['Snapchat locks'])
    patch('/guides/facebook-account-disabled-appeal/', 'Facebook recovery by country', G['Facebook recovery by country'])
    patch('/guides/facebook-lost-access-to-email-or-phone/', 'Facebook recovery by country', G['Facebook recovery by country'])
    patch('/username/', 'Username claims by country', G['Username claims by country'] + ['how-to-tell-if-an-instagram-account-is-inactive'])
    patch('/guides/instagram-check-account-status/', 'Disabled or hacked in the Gulf or Switzerland', [s for s in G['Instagram in the Gulf and Switzerland'] if 'recovery' not in s])
    patch('/guides/instagram-account-suspended-appeal/', 'Disabled in the Gulf or Switzerland', [s for s in G['Instagram in the Gulf and Switzerland'] if 'disabled' in s])
    patch('/account-recovery-by-country/', 'New country guides', G['Instagram in the Gulf and Switzerland'] + G['Facebook recovery by country'] + G['Snapchat locks'])
    urls = ['https://unbanz.com/%s/' % p['slug'] for p in PAGES]
    open('/tmp/dd30_urls.txt', 'w').write('\n'.join(urls) + '\n')
    sm = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
    add = ''.join('<url><loc>%s</loc><lastmod>2026-10-30</lastmod></url>\n' % u for u in urls if '<loc>%s</loc>' % u not in sm)
    if add: open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm.replace('</urlset>', add + '</urlset>'))
    for fn, fmt in (('llms.txt', '- [%s](%s): %s'), ('llms-full.txt', '- %s: %s — %s')):
        f = os.path.join(ROOT, fn); s = open(f, encoding='utf-8').read(); H = '## Country and inactive-username guides (2026-10-30)'
        if H not in s: open(f, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n\n' + H + '\n\n' + '\n'.join(fmt % (p['title'], 'https://unbanz.com/%s/' % p['slug'], p['desc']) for p in PAGES) + '\n')
    print(len(PAGES), 'pages')
if __name__ == '__main__': main()
