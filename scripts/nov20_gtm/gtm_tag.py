"""Nov 20 2026: Google tag (GTM-PGDPS7SK) immediately after <head> on every public page, exactly once.
Idempotent (replaces an existing copy). Skips /users (internal dashboard, has its own strict CSP), scripts, assets.
Page builders copy the <head> of existing pages, so new pages inherit it; run this after any build to be safe."""
import os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TAG = ('<script async src="https://www.googletagmanager.com/gtm.js?id=GTM-PGDPS7SK"></script>\n'
       '<script>\n  window.dataLayer = window.dataLayer || [];\n  function gtag(){dataLayer.push(arguments);}\n  gtag(\'js\', new Date());\n</script>')
OLD = re.compile(r'<script async src="https://www\.googletagmanager\.com/gtm\.js\?id=GTM-PGDPS7SK"></script>\s*<script>\s*window\.dataLayer = window\.dataLayer \|\| \[\];\s*function gtag\(\)\{dataLayer\.push\(arguments\);\}\s*gtag\(\'js\', new Date\(\)\);\s*</script>')
n = skipped = 0
for r, ds, fs in os.walk(ROOT):
    ds[:] = [d for d in ds if d not in ('.git', 'node_modules', 'scripts', 'assets', 'users')]
    for f in fs:
        if not f.endswith('.html'): continue
        p = os.path.join(r, f); s = open(p, encoding='utf8').read()
        t = OLD.sub('', s)
        if re.search(r'googletagmanager|GTM-', t): skipped += 1; print('other tag present, skipped', p); continue
        i = t.find('<head>')
        if i < 0: skipped += 1; print('no <head>', p); continue
        t = t[:i + 6] + TAG + t[i + 6:]
        if t != s: open(p, 'w', encoding='utf8').write(t); n += 1
print('updated', n, 'skipped', skipped)
