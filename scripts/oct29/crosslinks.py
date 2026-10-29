# -*- coding: utf-8 -*-
"""Oct 29: plain-text cross-links to sister sites (idempotent). Pages are hand-maintained, so this patches the HTML."""
ROOT = '/workspace/site/'
A = lambda u, t: '<a href="%s">%s</a>' % (u, t)
ADS = 'For ad account guides, see also ' + A('https://adsaccountrecovery.com/', 'Ads Account Recovery') + ' and ' + A('https://restoreadaccount.com/', 'Restore Ad Account') + '.'
PATCH = [
 ('guides/meta-ad-account-restricted/index.html', 'through Meta’s official process.</p>', 'through Meta’s official process.</p><p>' + ADS + '</p>', 'adsaccountrecovery.com'),
 ('unban/index.html', '<h2>Ad account unbans</h2><p>Restricted Meta ad accounts and Business Portfolios.</p>', '<h2>Ad account unbans</h2><p>Restricted Meta ad accounts and Business Portfolios. ' + ADS + '</p>', 'adsaccountrecovery.com'),
 ('username/index.html', 'We handle usernames on all three, where the platform allows it.</p>', 'We handle usernames on all three, where the platform allows it. For more on short handles, see ' + A('https://ogclaim.com/', 'OG Claim') + '.</p>', 'ogclaim.com'),
]
for f, old, new, mark in PATCH:
    s = open(ROOT + f, encoding='utf-8').read()
    if mark in s: continue
    assert s.count(old) == 1, f
    open(ROOT + f, 'w', encoding='utf-8').write(s.replace(old, new))
print('ok')
