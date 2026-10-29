#!/usr/bin/env python3
"""Build the 2026-10-28 country pages (recovery, username claim) and the by-country hub from the current template."""
import os as _o, sys as _s
_d = _o.path.dirname(_o.path.abspath(__file__))
while not _o.path.exists(_o.path.join(_d, 'cta_note.py')): _d = _o.path.dirname(_d)
_s.path.append(_d); from cta_note import write_page  # adds the human-only CTA note tag (homepages excluded)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import build_oct25_pages as b
import oct28c_content_a, oct28c_content_b, oct28c_content_c as c
import oct27_content as o
b.DATE = c.DATE
PAGES = list(o.PAGES) + c.UPAGES + [c.HUB]
for _p in PAGES: _p['v2'] = True
if __name__ == '__main__':
    for p in PAGES:
        d = os.path.join(b.ROOT, p['slug']); os.makedirs(d, exist_ok=True)
        out = b.build(p)
        write_page(os.path.join(d, 'index.html'), out)
        print('wrote', p['slug'], len(out))
    print(len(PAGES), 'pages')
