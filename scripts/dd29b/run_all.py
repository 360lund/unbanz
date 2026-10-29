# -*- coding: utf-8 -*-
"""Batch 2 of the 2026-10-29 double-down: 10 new EN pages each for the user, ad and snap families."""
import os as _o, sys as _s
_d = _o.path.dirname(_o.path.abspath(__file__))
while not _o.path.exists(_o.path.join(_d, 'cta_note.py')): _d = _o.path.dirname(_d)
_s.path.append(_d); from cta_note import write_page  # adds the human-only CTA note tag (homepages excluded)
import os, sys, re, html, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'dd29'))
from lib import *
import c_user2, c_ad2, c_snap2
from hubs_and_links import WIN, POOL
def related_for(p, group):
    i = group.index(p)
    sib = [group[(i + k) % len(group)] for k in (1, 2, 3, 4, 5)]
    F = FAM[p['fam']]
    rel = [(F['parent'][1], F['parent'][0])] + [('/%s/' % s['slug'], s['crumb']) for s in sib[:3]] + list(WIN.get(p['fam'], []))[:3]
    relq = [('/%s/' % s['slug'], s['crumb']) for s in sib[3:]] + list(POOL.get(p['fam'], []))[:4] + [('/white-label-agency/', 'For agencies'), ('/how-it-works/', 'How Unbanz works')]
    return rel, relq
TR = set(l.split('/')[0] for l in subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True).stdout.split('\n') if l)
def write():
    by = {}
    for p in PAGES: by.setdefault(p['fam'], []).append(p)
    slugs = []; out = []; errs = []
    for f, group in by.items():
        for p in group:
            assert len(group) == 10, (f, len(group))
            p['related_final'] = related_for(p, group)
            try: h = build(p, None)
            except AssertionError as e: errs.append((p['slug'], str(e)[:200])); continue
            d = os.path.join(ROOT, p['slug'])
            if p['slug'] in TR or os.path.exists(os.path.join(d, 'index.html')): raise SystemExit('COLLISION ' + p['slug'])
            out.append((d, h)); slugs.append(p['slug'])
    if errs:
        for e in errs: print('ERR', e)
        raise SystemExit(1)
    for d, h in out:
        os.makedirs(d, exist_ok=True); write_page(os.path.join(d, 'index.html'), h)
    return slugs
def nav(label, links, mark):
    return '<nav class="related-services container" aria-label="%s" data-dd29="%s">%s</nav>' % (esc(label), mark, ''.join('<a href="%s">%s</a>' % (u, esc(t)) for u, t in links))
def patch(path, label, links, mark):
    f = os.path.join(ROOT, path.strip('/'), 'index.html')
    s = open(f, encoding='utf-8').read()
    if 'data-dd29="%s"' % mark in s: return
    assert s.count('</main>') == 1, f
    open(f, 'w', encoding='utf-8').write(s.replace('</main>', nav(label, links, mark) + '</main>', 1))
def main():
    slugs = write()
    by = {}
    for p in PAGES: by.setdefault(p['fam'], []).append(p)
    L = lambda f: [('/%s/' % p['slug'], p['title']) for p in by[f]]
    patch('/username/', 'More username situations', L('user'), 'inj2')
    patch('/instagram-username-claim/', 'More username situations', L('user'), 'inj2')
    for u in ('/meta-ad-account-help/', '/ad-account-recovery/', '/guides/meta-ad-account-restricted/'): patch(u, 'More ad account situations', L('ad'), 'inj2')
    patch('/snapchat-unban-service/', 'More Snapchat situations', L('snap'), 'inj2')
    # snapchat hub list
    f = os.path.join(ROOT, 'snapchat-account-help', 'index.html'); s = open(f, encoding='utf-8').read()
    if 'snapchat-locked-after-too-many-login-attempts' not in s:
        m = re.search(r'(<h2 id="locked-and-banned-accounts">.*?)(</ul>)', s, re.S); assert m
        add = ''.join('<li><a href="/%s/">%s</a></li>' % (p['slug'], esc(p['crumb'])) for p in by['snap'])
        s = s[:m.end(1)] + add + s[m.end(1):]; open(f, 'w', encoding='utf-8').write(s)
    items = [(p['slug'], p['title'], p['desc']) for p in PAGES]
    open('/workspace/new_pages_oct29_double_down_b2.txt', 'w').write('\n'.join('https://unbanz.com/%s/' % s for s, _, _ in items) + '\n')
    sm = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
    add = ''.join('<url><loc>https://unbanz.com/%s/</loc><lastmod>2026-10-29</lastmod></url>\n' % s for s, _, _ in items if 'https://unbanz.com/%s/</loc>' % s not in sm)
    if add: open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm.replace('</urlset>', add + '</urlset>'))
    def app(fn, fmt):
        f = os.path.join(ROOT, fn); s = open(f, encoding='utf-8').read()
        if '## Account help situations, batch 2 (2026-10-29)' in s: return
        body = '\n'.join(fmt % (t, 'https://unbanz.com/%s/' % sl, d) for sl, t, d in items)
        open(f, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n\n## Account help situations, batch 2 (2026-10-29)\n\n' + body + '\n')
    app('llms.txt', '- [%s](%s): %s'); app('llms-full.txt', '- %s: %s — %s')
    open('/tmp/dd29b_slugs.txt', 'w').write('\n'.join(slugs)); print(len(slugs), 'pages')
if __name__ == '__main__': main()
