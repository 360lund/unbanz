# -*- coding: utf-8 -*-
import os as _o, sys as _s
_d = _o.path.dirname(_o.path.abspath(__file__))
while not _o.path.exists(_o.path.join(_d, 'cta_note.py')): _d = _o.path.dirname(_d)
_s.path.append(_d); from cta_note import write_page
import os, sys, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'dd29'))
import lib
from c_en4 import *
from lib import ROOT, FAM, esc
C = {'US': 'United States', 'GB': 'United Kingdom', 'CA': 'Canada', 'AU': 'Australia'}
EU = ['France', 'Germany', 'Netherlands', 'Ireland', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Austria', 'Italy', 'Spain', 'Poland']
def area(a):
    if a is None: return None
    out = []
    for x in (a if isinstance(a, list) else [a]):
        out += [{'@type': 'Country', 'name': n} for n in (EU if x == 'EU' else [C[x]])]
    return out
_hb = lib.how_block
def how_block(p):
    s = _hb(p); d = FAM[p['fam']].get('decider')
    return s.replace('Meta makes the final decision', '%s makes the final decision' % d) if d else s
lib.how_block = how_block
fam('hubbiz', **dict(FAM['igsusp'], parent=('Help', '/services/'), stype='Business and creator account help'))
TR = set(l.split('/')[0] for l in subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True).stdout.split('\n') if l)
NEW = [p for p in PAGES if p['slug'] not in TR or p.get('_mine')]
def exists(u): return os.path.exists(os.path.join(ROOT, u.strip('/'), 'index.html')) or u.strip('/') in [p['slug'] for p in PAGES]
def L(p): return ('/%s/' % p['slug'], p['crumb'])
G = {'Disabled business and creator accounts': ['igsusp', 'igrestrict', 'fbdis'], 'Hacked accounts': ['ighacked', 'hacked', 'fblost', 'igrecov'],
     'Meta Verified': ['verified'], 'Meta business and ad accounts': ['ad'], 'Your rights by country': ['legal'], 'Usernames and brands': ['user'], 'Snapchat and TikTok': ['snap', 'tiktok']}
def main():
    for p in PAGES:
        if p['slug'] in TR: raise SystemExit('COLLISION ' + p['slug'])
        p['area'] = area(p['area'])
    hub = [p for p in PAGES if p['fam'] == 'hubbiz'][0]
    secs = []
    for h, fs in G.items():
        items = [p for p in PAGES if p['fam'] in fs and p is not hub]
        if items: secs.append(S(h, ul([A(*L(q)) for q in items])))
    hub['sections'] = secs[:6]
    if len(secs) > 6: hub['sections'][5] = S('Usernames, Snapchat and TikTok', ul([A(*L(q)) for q in PAGES if q['fam'] in ('user', 'snap', 'tiktok')]))
    bad = set()
    for p in PAGES:
        for s in p['sections']:
            for u in re.findall(r'href="(/[^"]*)"', s):
                if not exists(u): bad.add((p['slug'], u))
    if bad: raise SystemExit('BROKEN %s' % sorted(bad))
    others = [p for p in PAGES if p is not hub]
    for i, p in enumerate(PAGES):
        F = FAM[p['fam']]
        sib = [q for q in others if q['fam'] == p['fam'] and q is not p] or others
        sib2 = [others[(i + k) % len(others)] for k in (3, 7, 11, 17)]
        rel = [F['parent'], L(hub)] + [L(q) for q in sib[:4]]
        relq = [L(q) for q in sib2 if q is not p] + [('/how-it-works/', 'How Unbanz works'), ('/white-label-agency/', 'For agencies')]
        p['related_final'] = (rel, relq)
        h = build(p, None); d = os.path.join(ROOT, p['slug']); os.makedirs(d, exist_ok=True); write_page(os.path.join(d, 'index.html'), h)
    def nav(label, links): return '<nav class="related-services container" aria-label="%s" data-dd29="hv30">%s</nav>' % (label, ''.join('<a href="%s">%s</a>' % (u, esc(t)) for u, t in links))
    def patch(u, label, links):
        f = os.path.join(ROOT, u.strip('/'), 'index.html')
        if not os.path.exists(f): print('skip', u); return
        s = open(f, encoding='utf-8').read()
        if 'data-dd29="hv30"' in s or s.count('</main>') != 1: return
        open(f, 'w', encoding='utf-8').write(s.replace('</main>', nav(label, links) + '</main>', 1))
    by = lambda *fs: [L(q) for q in others if q['fam'] in fs]
    patch('/instagram-account-help/', 'Business, creator and rights guides', [L(hub)] + by('igsusp', 'igrestrict', 'ighacked', 'verified')[:8])
    patch('/facebook-account-help/', 'Business, creator and rights guides', [L(hub)] + by('fbdis', 'fblost', 'legal')[:8])
    patch('/meta-ad-account-help/', 'Business portfolio and verification', [L(hub)] + by('ad'))
    patch('/username/', 'Trademarks and brand names', [L(hub)] + by('user'))
    patch('/snapchat-account-help/', 'More Snapchat help', [L(hub)] + by('snap'))
    patch('/services/', 'Business and creator help', [L(hub), ('/your-rights-when-meta-disables-your-account/', 'Your rights after a ban')])
    patch('/guides/instagram-account-suspended-appeal/', 'If it is your business or you are in the EU, UK or US', [L(hub)] + by('igsusp')[:6] + [('/appeals-centre-europe-instagram-facebook-suspension/', 'Appeals Centre Europe')])
    patch('/guides/facebook-account-disabled-appeal/', 'If it is your business or you are in the EU, UK or US', [L(hub)] + by('fbdis', 'legal')[:7])
    items = [(p['slug'], p['title'], p['desc']) for p in PAGES]
    open('/tmp/hv30_urls.txt', 'w').write('\n'.join('https://unbanz.com/%s/' % s for s, _, _ in items) + '\n')
    sm = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
    add = ''.join('<url><loc>https://unbanz.com/%s/</loc><lastmod>2026-10-29</lastmod></url>\n' % s for s, _, _ in items if 'https://unbanz.com/%s/</loc>' % s not in sm)
    if add: open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm.replace('</urlset>', add + '</urlset>'))
    for fn, fmt in (('llms.txt', '- [%s](%s): %s'), ('llms-full.txt', '- %s: %s — %s')):
        f = os.path.join(ROOT, fn); s = open(f, encoding='utf-8').read(); H = '## Business, creator, hacked and rights guides (2026-10-29)'
        if H not in s: open(f, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n\n' + H + '\n\n' + '\n'.join(fmt % (t, 'https://unbanz.com/%s/' % sl, d) for sl, t, d in items) + '\n')
    print(len(PAGES), 'pages')
if __name__ == '__main__': main()
