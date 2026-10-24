import re, glob, hashlib, os, sys
ROOT = '/workspace/site'
base = open(ROOT + '/assets/site.1467f35602a6.css', encoding='utf-8').read()
add = open(ROOT + '/scripts/guides/guide_v2.css', encoding='utf-8').read()
css = base.rstrip('\n') + '\n' + add
name = 'site.' + hashlib.sha256(css.encode()).hexdigest()[:12] + '.css'
path = ROOT + '/assets/' + name
# remove previous (uncommitted) generated bundles from earlier runs
for old in glob.glob(ROOT + '/assets/site.*.css'):
    pass
open(path, 'w', encoding='utf-8').write(css)
n = 0
for f in glob.glob(ROOT + '/guides/**/index.html', recursive=True):
    h = open(f, encoding='utf-8').read()
    h2 = re.sub(r'/assets/site\.[0-9a-f]{12}\.css', '/assets/' + name, h)
    if h2 != h:
        open(f, 'w', encoding='utf-8').write(h2); n += 1
print(name, 'pages updated', n)
