# -*- coding: utf-8 -*-
import os as _o, sys as _s
_d = _o.path.dirname(_o.path.abspath(__file__))
while not _o.path.exists(_o.path.join(_d, 'cta_note.py')): _d = _o.path.dirname(_d)
_s.path.append(_d); from cta_note import write_page
import os, sys, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'dd29'))
import lib
lib.DATE = '2026-10-31'; lib.DATE_LONG = '31 October 2026'
from c_oct31 import *
from lib import ROOT, FAM, esc
C = {'US': 'United States', 'GB': 'United Kingdom', 'CA': 'Canada', 'AU': 'Australia', 'AE': 'United Arab Emirates', 'SA': 'Saudi Arabia', 'QA': 'Qatar', 'KW': 'Kuwait'}
EU = ['France', 'Germany', 'Netherlands', 'Ireland', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Austria', 'Italy', 'Spain', 'Poland']
TERMS = 'Terms are agreed with you before any work starts.'
def area(a):
    out = []
    for x in (a if isinstance(a, list) else [a]):
        out += [{'@type': 'Country', 'name': n} for n in (EU if x == 'EU' else [C[x]])]
    return out
_hb = lib.how_block
def how_block(p):
    s = _hb(p); old = 'We tell you honestly whether this is something we can help with.'
    assert old in s
    return s.replace(old, old + ' ' + TERMS)
lib.how_block = how_block
TR = set(l.split('/')[0] for l in subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True).stdout.split('\n') if l)
def exists(u): return os.path.exists(os.path.join(ROOT, u.strip('/'), 'index.html')) or u.strip('/') in [p['slug'] for p in PAGES]
def L(p): return ('/%s/' % p['slug'], p['crumb'])
WIN = [('/guides/instagram-account-suspended-appeal/', 'Instagram suspended: how to appeal'), ('/guides/instagram-disabled-no-appeal-button/', 'No appeal button'),
       ('/guides/instagram-id-verification-request/', 'ID verification request'), ('/guides/facebook-account-disabled-appeal/', 'Facebook disabled appeal'),
       ('/guides/facebook-lost-access-to-email-or-phone/', 'Lost access to email or phone'), ('/inactive-instagram-username/', 'Inactive usernames')]
EXTRA = {'facebook-account-disabled-canada-what-to-do': ['/facebook-account-disabled-usa-what-to-do/', '/instagram-disabled-canada-what-to-do/'],
         'facebook-account-disabled-australia-what-to-do': ['/facebook-account-disabled-uk-what-to-do/', '/instagram-disabled-australia-what-to-do/'],
         'facebook-account-disabled-uae-what-to-do': ['/facebook-account-recovery-uae/', '/meta-ad-account-disabled-uae/'],
         'facebook-account-disabled-saudi-arabia-what-to-do': ['/facebook-account-recovery-saudi-arabia/', '/instagram-disabled-saudi-arabia-what-to-do/'],
         'facebook-appeal-rejected-eu-options': ['/guides/facebook-disabled-appeal-rejected/', '/appeals-centre-europe-instagram-facebook-suspension/'],
         'facebook-lost-access-to-email-or-phone-gulf': ['/guides/facebook-lost-access-to-email-or-phone/', '/facebook-account-recovery-saudi-arabia/'],
         'facebook-lost-access-to-email-or-phone-uk-eu': ['/guides/facebook-lost-access-to-email-or-phone/', '/facebook-account-recovery-uk/']}
def title_of(u):
    f = os.path.join(ROOT, u.strip('/'), 'index.html')
    m = re.search(r'<title>([^<|]*)', open(f, encoding='utf-8').read()); return m.group(1).strip().split(':')[0]
def main():
    for p in PAGES:
        if p['slug'] in TR: raise SystemExit('COLLISION ' + p['slug'])
        p['area'] = area(p['area'])
    bad = set()
    for p in PAGES:
        for s in p['sections']:
            for u in re.findall(r'href="(/[^"]*)"', s):
                if not exists(u): bad.add((p['slug'], u))
        for u in EXTRA[p['slug']]:
            if not exists(u): bad.add((p['slug'], u))
    if bad: raise SystemExit('BROKEN %s' % sorted(bad))
    for p in PAGES:
        F = FAM[p['fam']]
        sib = [L(q) for q in PAGES if q is not p and FAM[q['fam']]['ws'] == F['ws']] or [L(q) for q in PAGES if q is not p]
        rel = [F['parent']] + [(u, title_of(u)) for u in EXTRA[p['slug']]] + sib[:4]
        relq = WIN[:4] + [('/how-it-works/', 'How Unbanz works'), ('/white-label-agency/', 'For agencies')]
        p['related_final'] = (rel, relq)
        h = lib.build(p, None)
        assert TERMS in h and 'Not affiliated with Meta' in h and 'wa.me/19342012490' in h and '447723' not in h.replace(' ', '')
        d = os.path.join(ROOT, p['slug']); os.makedirs(d, exist_ok=True); write_page(os.path.join(d, 'index.html'), h)
    def nav(label, links): return '<nav class="related-services container" aria-label="%s" data-dd29="oct31">%s</nav>' % (label, ''.join('<a href="%s">%s</a>' % (u, esc(t)) for u, t in links))
    changed = []
    def patch(u, label, links):
        f = os.path.join(ROOT, u.strip('/'), 'index.html')
        if not os.path.exists(f): print('skip', u); return
        s = open(f, encoding='utf-8').read()
        if 'data-dd29="oct31"' in s or s.count('</main>') != 1: print('nopatch', u); return
        s = s.replace('</main>', nav(label, links) + '</main>', 1); s = re.sub(r'("dateModified"\s*:\s*")[^"]*', r'\g<1>2026-10-31', s); open(f, 'w', encoding='utf-8').write(s); changed.append(u)
    P = {p['slug']: L(p) for p in PAGES}
    dis = [P[k] for k in ('facebook-account-disabled-canada-what-to-do', 'facebook-account-disabled-australia-what-to-do', 'facebook-account-disabled-uae-what-to-do', 'facebook-account-disabled-saudi-arabia-what-to-do')]
    rej = P['facebook-appeal-rejected-eu-options']; lg = P['facebook-lost-access-to-email-or-phone-gulf']; le = P['facebook-lost-access-to-email-or-phone-uk-eu']
    patch('/guides/facebook-account-disabled-appeal/', 'Facebook disabled: more countries', dis + [rej])
    patch('/guides/facebook-disabled-appeal-rejected/', 'Rejected appeal in the EU', [rej])
    patch('/guides/facebook-lost-access-to-email-or-phone/', 'Lost email or phone: by region', [lg, le])
    patch('/facebook-account-help/', 'Facebook: more countries and regions', dis + [rej, lg, le])
    patch('/facebook-account-disabled-uk-what-to-do/', 'Other countries', dis + [rej])
    patch('/facebook-account-disabled-usa-what-to-do/', 'Other countries', dis)
    patch('/facebook-account-recovery-canada/', 'More for Canada', [dis[0]])
    patch('/facebook-account-recovery-australia/', 'More for Australia', [dis[1]])
    patch('/facebook-account-recovery-uae/', 'More for the UAE', [dis[2], lg])
    patch('/facebook-account-recovery-saudi-arabia/', 'More for Saudi Arabia', [dis[3], lg])
    patch('/facebook-account-recovery-kuwait/', 'More for Kuwait', [lg])
    patch('/facebook-account-recovery-uk/', 'More for the UK', [le])
    patch('/appeals-centre-europe-instagram-facebook-suspension/', 'Facebook appeal rejected', [rej])
    items = [(p['slug'], p['title'], p['desc']) for p in PAGES]
    open('/tmp/oct31_urls.txt', 'w').write('\n'.join('https://unbanz.com/%s/' % s for s, _, _ in items) + '\n')
    open('/tmp/oct31_changed.txt', 'w').write('\n'.join('https://unbanz.com' + u for u in changed) + '\n')
    sm = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
    for u in changed:
        sm = re.sub(r'(<loc>https://unbanz.com%s</loc>\s*<lastmod>)[^<]*' % re.escape(u), r'\g<1>2026-10-31', sm)
    add = ''.join('<url><loc>https://unbanz.com/%s/</loc><lastmod>2026-10-31</lastmod></url>\n' % s for s, _, _ in items if 'https://unbanz.com/%s/</loc>' % s not in sm)
    open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm.replace('</urlset>', add + '</urlset>'))
    for fn, fmt in (('llms.txt', '- [%s](%s): %s'), ('llms-full.txt', '- %s: %s — %s')):
        f = os.path.join(ROOT, fn); s = open(f, encoding='utf-8').read(); H = '## Facebook disabled and lost access by country (2026-10-31)'
        if H not in s: open(f, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n\n' + H + '\n\n' + '\n'.join(fmt % (t, 'https://unbanz.com/%s/' % sl, d) for sl, t, d in items) + '\n')
    print(len(PAGES), 'pages;', len(changed), 'patched')
if __name__ == '__main__': main()
