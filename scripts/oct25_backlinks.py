#!/usr/bin/env python3
"""Add links to the 13 pages (2026-10-25) from related existing pages. Idempotent."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
L = {
 'usa': ('/instagram-account-recovery-usa/', 'Recovery in the USA'),
 'india': ('/instagram-account-recovery-india/', 'Recovery in India'),
 'uae': ('/instagram-account-recovery-uae/', 'Recovery in the UAE'),
 'uk': ('/instagram-account-recovery-uk/', 'Recovery in the UK'),
 'hig': ('/instagram-hacked-account-recovery-service/', 'Hacked Instagram recovery'),
 'hfb': ('/facebook-hacked-account-recovery-service/', 'Hacked Facebook recovery'),
 'dah': ('/instagram-account-disabled-after-hack-appeal/', 'Disabled after a hack'),
 'biz': ('/instagram-business-account-disabled-recovery/', 'Business account disabled'),
 'cre': ('/instagram-creator-account-disabled-recovery/', 'Creator account disabled'),
 'frm': ('/instagram-appeal-form-not-working/', 'Appeal form not working'),
 'ref': ('/instagram-username-claim-refund/', 'Username claim refund'),
 'inf': ('/instagram-username-claim-for-influencers/', 'Username claims for influencers'),
 'fnd': ('/instagram-username-claim-for-founders-and-startups/', 'Username claims for founders'),
}
SRC = {
 '/instagram-account-recovery/': ['usa','india','uae','uk','hig'],
 '/guides/hacked-instagram-account-recovery/': ['hig','usa','india','uae','uk'],
 '/instagram-account-disabled-appeal/': ['dah','biz','cre','frm'],
 '/hacker-changed-my-instagram-email-and-password/': ['hig','dah'],
 '/instagram-appeal-denied/': ['frm','dah'],
 '/guides/instagram-disabled-no-appeal-button/': ['frm'],
 '/facebook-account-recovery/': ['hfb'],
 '/guides/hacked-facebook-account-recovery/': ['hfb'],
 '/ad-account-disabled-after-hack/': ['hfb'],
 '/business-manager-disabled/': ['biz'],
 '/guides/instagram-business-vs-creator-account/': ['biz','cre'],
 '/guides/instagram-disabled-for-impersonation/': ['cre'],
 '/refund-policy/': ['ref'],
 '/username-claim-pricing/': ['ref'],
 '/instagram-username-claim-usa/': ['ref','inf'],
 '/username/': ['inf','fnd','ref'],
 '/og-username/': ['inf'],
 '/instagram-username-claim/': ['inf','ref'],
 '/business-username-claim/': ['fnd'],
 '/trademark-username-claim/': ['fnd'],
 '/how-much-does-it-cost-to-claim-an-instagram-username/': ['fnd'],
}
NAV = re.compile(r'<nav class="related-services container"[^>]*>.*?</nav>', re.S)
n = 0
for src, keys in SRC.items():
    path = os.path.join(ROOT, src.strip('/'), 'index.html')
    if not os.path.exists(path):
        print('MISSING source', src); continue
    s = open(path, encoding='utf-8').read()
    navs = list(NAV.finditer(s))
    if not navs:
        print('NO NAV', src); continue
    m = navs[-1]; block = m.group(0)
    add = ''.join('<a href="%s">%s</a>' % L[k] for k in keys if 'href="%s"' % L[k][0] not in s)
    if not add: continue
    s = s[:m.start()] + block[:-len('</nav>')] + add + '</nav>' + s[m.end():]
    open(path, 'w', encoding='utf-8').write(s); n += 1
    print('updated', src, '+', len(keys))
print(n, 'pages updated')
