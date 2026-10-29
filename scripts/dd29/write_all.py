# -*- coding: utf-8 -*-
import os as _o, sys as _s
_d = _o.path.dirname(_o.path.abspath(__file__))
while not _o.path.exists(_o.path.join(_d, 'cta_note.py')): _d = _o.path.dirname(_d)
_s.path.append(_d); from cta_note import write_page  # adds the human-only CTA note tag (homepages excluded)
import os, sys, importlib, json
from lib import *
MODS = ['c_igsusp','c_igappeal','c_ighacked','c_igverify','c_fbdis','c_fblost','c_igrecov','c_igrestrict','c_fbrecov','c_snap','c_user','c_ad']
for m in MODS: importlib.import_module(m)
import hubs_and_links as H
from hubs_and_links import WIN, POOL
H.make_hubs()
import nat29
NAT_ALTS = nat29.en_alts()
def related_for(p, group):
    i = group.index(p)
    sib = [group[(i + k) % len(group)] for k in (1, 2, 3, 4, 5)]
    F = FAM[p['fam']]
    rel = [(F['parent'][1], F['parent'][0])] + [('/%s/' % s['slug'], s['crumb']) for s in sib[:3]] + list(WIN.get(p['fam'], []))[:3]
    relq = [('/%s/' % s['slug'], s['crumb']) for s in sib[3:]] + list(POOL.get(p['fam'], []))[:4] + [('/white-label-agency/', 'For agencies'), ('/how-it-works/', 'How Unbanz works')]
    return rel, relq
import subprocess
TR = set(l.split('/')[0] for l in subprocess.run(['git','ls-files'],cwd=ROOT,capture_output=True,text=True).stdout.split('\n') if l)
def tracked(s): return s in TR
def main(write=True):
    by = {}
    for p in PAGES: by.setdefault(p['fam'], []).append(p)
    slugs = []
    for f, group in by.items():
        for p in group:
            p['related_final'] = related_for(p, group)
            h = build(p, NAT_ALTS.get(p["slug"]))
            d = os.path.join(ROOT, p['slug'])
            if os.path.exists(os.path.join(d, 'index.html')) and tracked(p['slug']):
                raise SystemExit('COLLISION ' + p['slug'])
            if write:
                os.makedirs(d, exist_ok=True); write_page(os.path.join(d, 'index.html'), h)
            slugs.append(p['slug'])
    return slugs
if __name__ == '__main__':
    s = main(); print(len(s), 'pages written')
    open('/tmp/dd29_slugs.txt', 'w').write('\n'.join(s))
    n = nat29.build_all(ROOT); open('/tmp/dd29_native.txt', 'w').write('\n'.join(n)); print(len(n), 'native pages written')
