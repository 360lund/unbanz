import re, glob, sys, os
new = sys.argv[1]  # e.g. mail-pick.295b5986b083.js
n = 0
for p in glob.glob('/workspace/site/**/*.html', recursive=True):
    if '/users/' in p or '/scripts/' in p or '/docs/' in p: continue
    t = open(p, encoding='utf-8').read()
    u = re.sub(r'/assets/mail-pick\.[0-9a-f]{12}\.js', '/assets/' + new, t)
    if u != t: open(p, 'w', encoding='utf-8').write(u); n += 1
print('pages updated', n)
