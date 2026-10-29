# -*- coding: utf-8 -*-
"""Idempotent: add/refresh the CTA-note script tag on every page (utility pages excluded). Run from anywhere."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from cta_note import with_cta_note
n = 0
for d, dirs, files in os.walk(ROOT):
    dirs[:] = [x for x in dirs if x not in ('.git', 'node_modules', 'scripts', 'assets', 'api')]
    for fn in files:
        if not fn.endswith('.html'): continue
        f = os.path.join(d, fn); rel = os.path.relpath(f, ROOT)
        s = open(f, encoding='utf-8').read(); t = with_cta_note(s, rel)
        if t != s: open(f, 'w', encoding='utf-8').write(t); n += 1
print('pages changed', n)
