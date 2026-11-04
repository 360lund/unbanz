# -*- coding: utf-8 -*-
import os as _o, sys as _s
_d = _o.path.dirname(_o.path.abspath(__file__))
while not _o.path.exists(_o.path.join(_d, 'cta_note.py')): _d = _o.path.dirname(_d)
_s.path.append(_d); from cta_note import write_page
import os, sys, re, subprocess, html as H
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'dd29'))
import lib
lib.DATE = '2026-11-04'; lib.DATE_LONG = '4 November 2026'
from c_nov04h import *
from lib import ROOT, FAM, esc
D = '2026-11-04'
C = {'US': 'United States', 'GB': 'United Kingdom', 'CA': 'Canada', 'AU': 'Australia',
     'AE': 'United Arab Emirates', 'SA': 'Saudi Arabia', 'QA': 'Qatar', 'KW': 'Kuwait',
     'FR': 'France', 'DE': 'Germany', 'CH': 'Switzerland', 'NL': 'Netherlands', 'IN': 'India'}
TERMS = 'Terms are agreed with you before any work starts.'
def area(a):
    if not a: return None
    return [{'@type': 'Country', 'name': C[x]} for x in (a if isinstance(a, list) else [a])]
_hb = lib.how_block
def how_block(p):
    s = _hb(p); old = 'We tell you honestly whether this is something we can help with.'
    assert old in s
    return s.replace(old, old + ' ' + TERMS)
lib.how_block = how_block
TR = set(l.split('/')[0] for l in subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True).stdout.split('\n') if l)
def exists(u): return os.path.exists(os.path.join(ROOT, u.strip('/'), 'index.html')) or u.strip('/') in [p['slug'] for p in PAGES]
def L(p): return ('/%s/' % p['slug'], p['crumb'])
WIN = [('/guides/instagram-account-suspended-appeal/', 'Instagram suspended: how to appeal'),
       ('/guides/facebook-account-disabled-appeal/', 'Facebook disabled appeal'),
       ('/guides/meta-ad-account-restricted/', 'Meta ad account restricted'),
       ('/guides/instagram-disabled-no-appeal-button/', 'No appeal button'),
       ('/guides/facebook-lost-access-to-email-or-phone/', 'Lost email or phone'),
       ('/guides/meta-ad-payment-declined-fix/', 'Ad payment declined')]
EXTRA = {'instagram-hacked-usa-what-to-do': ['/guides/hacked-instagram-account-recovery/', '/hacker-changed-my-instagram-email-and-password/', '/guides/instagram-account-suspended-appeal/'], 'instagram-hacked-uk-what-to-do': ['/guides/hacked-instagram-account-recovery/', '/hacker-changed-my-instagram-email-and-password/', '/guides/instagram-account-suspended-appeal/'], 'instagram-hacked-canada-what-to-do': ['/guides/hacked-instagram-account-recovery/', '/hacker-changed-my-instagram-email-and-password/', '/guides/instagram-account-suspended-appeal/'], 'instagram-hacked-netherlands-what-to-do': ['/guides/hacked-instagram-account-recovery/', '/hacker-changed-my-instagram-email-and-password/', '/guides/instagram-account-suspended-appeal/'], 'instagram-hacked-france-what-to-do': ['/guides/hacked-instagram-account-recovery/', '/hacker-changed-my-instagram-email-and-password/', '/guides/instagram-account-suspended-appeal/'], 'instagram-account-suspended-netherlands-what-to-do': ['/guides/instagram-account-suspended-appeal/', '/appeals-centre-europe-instagram-facebook-suspension/', '/facebook-account-disabled-netherlands-what-to-do/'], 'instagram-account-suspended-france-what-to-do': ['/guides/instagram-account-suspended-appeal/', '/appeals-centre-europe-instagram-facebook-suspension/', '/meta-ad-account-disabled-france/'], 'facebook-account-disabled-france-what-to-do': ['/guides/facebook-account-disabled-appeal/', '/appeals-centre-europe-instagram-facebook-suspension/', '/meta-ad-account-disabled-france/']}
BANNED = re.compile(
  r'\bcases?\b|we review|fixed price|fast turnaround|\bguarantees?\b|\bguaranteed\b|'
  r'meta reps?|insiders?|partners with meta|payment timing|'
  r'gets it done|price in the chat|wa\.me/44|447723',
  re.I,
)
def title_of(u):
    f = os.path.join(ROOT, u.strip('/'), 'index.html')
    m = re.search(r'<title>([^<|]*)', open(f, encoding='utf-8').read()); return H.unescape(m.group(1).strip().split(':')[0])
def main():
    for p in PAGES:
        if p['slug'] in TR: raise SystemExit('COLLISION ' + p['slug'])
        if p.get('area'): p['area'] = area(p['area'])
    bad = set()
    for p in PAGES:
        for s in p['sections']:
            for u in re.findall(r'href="(/[^"]*)"', s):
                if not exists(u): bad.add((p['slug'], u))
        for u in EXTRA.get(p['slug'],[]):
            if not exists(u): bad.add((p['slug'], u))
    for u, _ in WIN:
        if not exists(u): bad.add(('WIN', u))
    if bad: raise SystemExit('BROKEN %s' % sorted(bad))
    for p in PAGES:
        F = FAM[p['fam']]
        sib = [L(q) for q in PAGES if q is not p and q['fam'] == p['fam']] or [L(q) for q in PAGES if q is not p]
        rel = [F['parent']] + [(u, title_of(u)) for u in EXTRA.get(p['slug'],[])] + sib[:3]
        relq = WIN[:4] + [('/how-it-works/', 'How Unbanz works'), ('/white-label-agency/', 'For agencies')]
        p['related_final'] = (rel, relq)
        h = lib.build(p, None)
        assert TERMS in h and 'Not affiliated with Meta' in h and 'wa.me/19342012490' in h
        assert '447723' not in h.replace(' ', '') and 'wa.me/44' not in h
        badm = BANNED.search(h)
        assert not badm, (p['slug'], badm.group(0))
        assert 'testimonials' in h.lower() or 'review-carousel' in h or 'testimonial' in h
        d = os.path.join(ROOT, p['slug']); os.makedirs(d, exist_ok=True); write_page(os.path.join(d, 'index.html'), h)
    def nav(label, links):
        return '<nav class="related-services container" aria-label="%s" data-dd29="nov04h">%s</nav>' % (
            label, ''.join('<a href="%s">%s</a>' % (u, esc(t)) for u, t in links))
    changed = []
    def patch(u, label, links):
        f = os.path.join(ROOT, u.strip('/'), 'index.html')
        if not os.path.exists(f): print('skip', u); return
        s = open(f, encoding='utf-8').read()
        if 'data-dd29="nov04h"' in s or s.count('</main>') != 1: print('nopatch', u); return
        s = s.replace('</main>', nav(label, links) + '</main>', 1)
        s = re.sub(r'("dateModified"\s*:\s*")[^"]*', r'\g<1>' + D, s)
        # bump visible Updated time if present
        s = re.sub(r'(Updated <time datetime=")[^"]*("[^>]*>)[^<]*', r'\g<1>%s\g<2>%s' % (D, '4 November 2026'), s, count=1)
        open(f, 'w', encoding='utf-8').write(s); changed.append(u)
    def deepen_note(u, html_note):
        f = os.path.join(ROOT, u.strip('/'), 'index.html')
        if not os.path.exists(f): print('skipnote', u); return
        s = open(f, encoding='utf-8').read()
        if 'data-nov04-note="1"' in s: print('hasnote', u); return
        # Prefer inserting before Prefer someone else / Want help / service-proof
        inserted = False
        for marker in ('<h2 id="help">', '<section class="service-proof', '<div class="guide-sources"'):
            if marker in s:
                s = s.replace(marker, html_note + marker, 1); inserted = True; break
        if not inserted:
            s = s.replace('</article>', html_note + '</article>', 1)
        s = re.sub(r'("dateModified"\s*:\s*")[^"]*', r'\g<1>' + D, s)
        s = re.sub(r'(Updated <time datetime=")[^"]*("[^>]*>)[^<]*', r'\g<1>%s\g<2>%s' % (D, '4 November 2026'), s, count=1)
        open(f, 'w', encoding='utf-8').write(s)
        if u not in changed: changed.append(u)
        print('noted', u)
    P = {p['slug']: L(p) for p in PAGES}
    ig=P['instagram-appeal-what-to-write']; fw=P['facebook-disabled-appeal-what-to-write']; fn=P['facebook-appeal-sent-no-response']
    patch('/guides/instagram-account-suspended-appeal/','Writing the appeal',[ig])
    patch('/guides/instagram-account-disabled/','Writing the appeal',[ig])
    patch('/guides/instagram-appeal-sent-no-response/','Writing the appeal',[ig])
    patch('/guides/facebook-account-disabled-appeal/','Writing the appeal and waiting',[fw,fn])
    patch('/guides/facebook-disabled-appeal-rejected/','Writing the appeal and waiting',[fw,fn])
    patch('/facebook-account-help/','Writing the appeal and waiting',[fw,fn])
    patch('/instagram-account-help/','Writing the appeal',[ig])
    items = [(p['slug'], p['title'], p['desc'], p['answer']) for p in PAGES]
    open('/tmp/nov04h_urls.txt', 'w').write('\n'.join('https://unbanz.com/%s/' % s for s, _, _, _ in items) + '\n')
    open('/tmp/nov04h_changed.txt', 'w').write('\n'.join('https://unbanz.com' + u for u in changed) + '\n')
    sm = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
    for u in changed + ['/site-map/']:
        sm = re.sub(r'(<loc>https://unbanz.com%s</loc>\s*<lastmod>)[^<]*' % re.escape(u), r'\g<1>' + D, sm)
    add = ''.join('<url><loc>https://unbanz.com/%s/</loc><lastmod>%s</lastmod></url>\n' % (s, D) for s, _, _, _ in items if 'https://unbanz.com/%s/</loc>' % s not in sm)
    open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm.replace('</urlset>', add + '</urlset>'))
    # HTML site map
    f = os.path.join(ROOT, 'site-map', 'index.html'); s = open(f, encoding='utf-8').read()
    i = s.index('<h2>English</h2>'); j = s.index('</ul>', i); seg = s[i:j]
    lis = re.findall(r'<li><a href="([^"]+)">(.*?)</a></li>', seg)
    have = {h for h, _ in lis}
    for sl, t, _, _ in items:
        if '/%s/' % sl not in have: lis.append(('/%s/' % sl, esc(t)))
    lis.sort(key=lambda x: x[0])
    k = seg.index('<li>'); seg2 = seg[:k] + ''.join('<li><a href="%s">%s</a></li>' % x for x in lis)
    s = s[:i] + seg2 + s[j:]; open(f, 'w', encoding='utf-8').write(s)
    Hh = '## Writing and waiting on appeals (2026-11-04)'
    for fn, fmt in (('llms.txt', '- [%s](%s): %s'), ('llms-full.txt', '- %s: %s — %s')):
        f = os.path.join(ROOT, fn); s = open(f, encoding='utf-8').read()
        if Hh not in s:
            block = Hh + '\n\n' + '\n'.join(fmt % (t, 'https://unbanz.com/%s/' % sl, (a if fn == 'llms-full.txt' else d)) for sl, t, d, a in items) + '\n'
            open(f, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n\n' + block)
    print(len(PAGES), 'pages;', len(changed), 'patched')
if __name__ == '__main__': main()
