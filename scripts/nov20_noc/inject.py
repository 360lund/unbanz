# Nov 20 2026: inline "no contact" guard for IN/PK/IR (time zone or ubz_noc cookie set by middleware / geo API).
# Inserted right after <meta charset>; idempotent (replaces an existing #ubz-noc block). Content/SEO untouched.
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SNIP = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snippet.html'), encoding='utf8').read()
OLD = re.compile(r'<script id="ubz-noc">.*?</script><style id="ubz-noc-css">.*?</style>', re.S)
CH = re.compile(r'(<meta charset="utf-8"\s*/?>)', re.I)
n = skip = 0
for r, ds, fs in os.walk(ROOT):
    ds[:] = [d for d in ds if d not in ('.git', 'node_modules', 'scripts', 'assets', 'users')]
    for f in fs:
        if not f.endswith('.html'): continue
        p = os.path.join(r, f); s = open(p, encoding='utf8').read()
        if OLD.search(s): t = OLD.sub(lambda m: SNIP, s, count=1)
        else:
            m = CH.search(s)
            if not m: skip += 1; print('no charset', p); continue
            t = s[:m.end()] + SNIP + s[m.end():]
        if t != s: open(p, 'w', encoding='utf8').write(t); n += 1
print('updated', n, 'skipped', skip)
