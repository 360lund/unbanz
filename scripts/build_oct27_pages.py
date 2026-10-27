#!/usr/bin/env python3
"""Build the country pages added on 2026-10-27 from the current threads-account-suspended template."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import build_oct25_pages as b
import oct27_content as c
b.DATE = c.DATE
for p in c.PAGES:
    d = os.path.join(b.ROOT, p['slug']); os.makedirs(d, exist_ok=True)
    out = b.build(p)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(out)
    print('wrote', p['slug'], len(out))
