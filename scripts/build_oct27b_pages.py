#!/usr/bin/env python3
"""Build the high-income country recovery pages added on 2026-10-27 from the current threads-account-suspended template."""
import os as _o, sys as _s
_d = _o.path.dirname(_o.path.abspath(__file__))
while not _o.path.exists(_o.path.join(_d, 'cta_note.py')): _d = _o.path.dirname(_d)
_s.path.append(_d); from cta_note import write_page  # adds the human-only CTA note tag (homepages excluded)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import build_oct25_pages as b
import oct27b_content as c
b.DATE = c.DATE
for _p in c.PAGES: _p['v2'] = True
for p in c.PAGES:
    d = os.path.join(b.ROOT, p['slug']); os.makedirs(d, exist_ok=True)
    out = b.build(p)
    write_page(os.path.join(d, 'index.html'), out)
    print('wrote', p['slug'], len(out))
