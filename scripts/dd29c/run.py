# -*- coding: utf-8 -*-
"""Daily 2026-10-29 (morning): 6 ad account pages. Writes pages, links them from ad hubs, sitemap, llms files."""
import os as _o, sys as _s
_d = _o.path.dirname(_o.path.abspath(__file__))
while not _o.path.exists(_o.path.join(_d, 'cta_note.py')): _d = _o.path.dirname(_d)
_s.path.append(_d); from cta_note import write_page
import os, sys, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'dd29'))
from lib import *
import c_ad3
from hubs_and_links import WIN, POOL
TR = set(l.split('/')[0] for l in subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True).stdout.split('\n') if l)
def related_for(p, group):
    i = group.index(p); sib = [group[(i + k) % len(group)] for k in (1, 2, 3, 4, 5)]
    F = FAM[p['fam']]
    rel = [(F['parent'][1], F['parent'][0])] + [('/%s/' % s['slug'], s['crumb']) for s in sib[:3]] + list(WIN['ad'])[:3]
    relq = [('/%s/' % s['slug'], s['crumb']) for s in sib[3:]] + list(POOL['ad'])[:4] + [('/agency-ad-account-recovery/', 'Agency ad account recovery'), ('/white-label-agency/', 'For agencies'), ('/how-it-works/', 'How Unbanz works')]
    return rel, relq
def nav(label, links, mark):
    return '<nav class="related-services container" aria-label="%s" data-dd29="%s">%s</nav>' % (label, mark, ''.join('<a href="%s">%s</a>' % (u, esc(t)) for u, t in links))
def patch(path, label, links, mark):
    f = os.path.join(ROOT, path.strip('/'), 'index.html'); s = open(f, encoding='utf-8').read()
    if 'data-dd29="%s"' % mark in s: return
    assert s.count('</main>') == 1, f
    open(f, 'w', encoding='utf-8').write(s.replace('</main>', nav(label, links, mark) + '</main>', 1))
def main():
    group = [p for p in PAGES if p['fam'] == 'ad']; assert len(group) == 6
    for p in group:
        p['related_final'] = related_for(p, group)
        if p['slug'] in TR: raise SystemExit('COLLISION ' + p['slug'])
        h = build(p, None); d = os.path.join(ROOT, p['slug']); os.makedirs(d, exist_ok=True); write_page(os.path.join(d, 'index.html'), h)
    L = [('/%s/' % p['slug'], p['crumb']) for p in group]
    for u in ('/meta-ad-account-help/', '/ad-account-recovery/', '/guides/meta-ad-account-restricted/', '/guides/ad-account-circumventing-systems/', '/facebook-ad-account-disabled/'):
        patch(u, 'New ad account situations', L, 'inj3')
    for u in ('/agency-ad-account-recovery/', '/white-label-facebook-ad-account-recovery/', '/client-ad-account-disabled-agency-help/'):
        patch(u, 'Ad account situations for agencies', [L[4], L[2], L[5], L[0]], 'inj3')
    items = [(p['slug'], p['title'], p['desc']) for p in group]
    open('/tmp/dd29c_urls.txt', 'w').write('\n'.join('https://unbanz.com/%s/' % s for s, _, _ in items) + '\n')
    sm = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
    add = ''.join('<url><loc>https://unbanz.com/%s/</loc><lastmod>2026-10-29</lastmod></url>\n' % s for s, _, _ in items if 'https://unbanz.com/%s/</loc>' % s not in sm)
    if add: open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm.replace('</urlset>', add + '</urlset>'))
    def app(fn, fmt):
        f = os.path.join(ROOT, fn); s = open(f, encoding='utf-8').read()
        if '## Meta ad account situations (2026-10-29, morning)' in s: return
        open(f, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n\n## Meta ad account situations (2026-10-29, morning)\n\n' + '\n'.join(fmt % (t, 'https://unbanz.com/%s/' % sl, d) for sl, t, d in items) + '\n')
    app('llms.txt', '- [%s](%s): %s'); app('llms-full.txt', '- %s: %s — %s')
    print(len(group), 'pages')
if __name__ == '__main__': main()
