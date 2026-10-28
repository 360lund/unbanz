# -*- coding: utf-8 -*-
import os, re
import write_all as W
from lib import PAGES, ROOT, esc
import hubs_and_links as H
import nat29
W.main(write=False)
title = {p['slug']: p['title'] for p in PAGES}
by = {}
for p in PAGES:
    if not p['fam'].startswith('hub'): by.setdefault(p['fam'], []).append(p)
def nav(label, links, mark):
    return '<nav class="related-services container" aria-label="%s" data-dd29="%s">%s</nav>' % (esc(label), mark, ''.join('<a href="%s">%s</a>' % (u, esc(t)) for u, t in links))
def patch(path, label, links, mark):
    f = os.path.join(ROOT, path.strip('/'), 'index.html')
    assert os.path.exists(f), f
    s = open(f, encoding='utf-8').read()
    if 'data-dd29="%s"' % mark in s: return None
    assert s.count('</main>') == 1, f
    s = s.replace('</main>', nav(label, links, mark) + '</main>', 1)
    open(f, 'w', encoding='utf-8').write(s); return f
out = []
for url, (label, fams, n, extra) in H.INJECT.items():
    links = [(u, t) for u, t in extra]
    seen = set()
    for fm in fams:
        for p in by[fm]:
            if len(links) >= n + len(extra): break
            if p['slug'] in seen: continue
            seen.add(p['slug']); links.append(('/%s/' % p['slug'], p['title']))
    r = patch(url, label, links, 'inj')
    if r: out.append(r)
# native parents
NATL = {'fr': 'Autres situations', 'pt-br': 'Outras situações', 'es': 'Otras situaciones'}
for lk in ('fr', 'pt-br', 'es'):
    new = nat29.SRC[lk][0]
    groups = {}
    for t in nat29.ORDER:
        if t in new.T: groups.setdefault(new.T[t]['parent'], []).append(t)
    for par, tps in groups.items():
        pp = nat29.PARENT[lk][par][0] or nat29.N.CORE_ORIG[lk]
        links = [('/%s/' % nat29.pth(lk, t), new.T[t]['title']) for t in tps]
        r = patch(pp, NATL[lk], links, 'nat')
        if r: out.append(r)
open('/tmp/dd29_injected.txt', 'w').write('\n'.join(out))
print(len(out), 'pages patched')
