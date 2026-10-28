#!/usr/bin/env python3
"""Build the 2026-10-28 country pages (recovery, username claim) and the by-country hub from the current template."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import build_oct25_pages as b
import oct28c_content_a, oct28c_content_b, oct28c_content_c as c
import oct27_content as o
b.DATE = c.DATE
PAGES = list(o.PAGES) + c.UPAGES + [c.HUB]
if __name__ == '__main__':
    for p in PAGES:
        d = os.path.join(b.ROOT, p['slug']); os.makedirs(d, exist_ok=True)
        out = b.build(p)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(out)
        print('wrote', p['slug'], len(out))
    print(len(PAGES), 'pages')
