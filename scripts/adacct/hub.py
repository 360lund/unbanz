# -*- coding: utf-8 -*-
from lib import *
import a1, a2, a3, a4, a5, a6

GROUPS = [('notice', 'By notice or problem', 'Pick the message you got, or the closest thing to it.'),
          ('niche', 'By type of business', 'The same notice means different things to a shop, a coach or a clinic.'),
          ('country', 'By country', 'Local registers, tax numbers and rules that matter for an appeal.')]
EXISTING = [  # (url, label, blurb)
 ('/ad-account-recovery/', 'Ad account recovery', 'The main service page: what Unbanz does and how it works.'),
 ('/facebook-ad-account-disabled/', 'Facebook ad account disabled', 'Disabled outright: reasons, steps and the appeal.'),
 ('/facebook-ad-account-restricted-help/', 'Facebook ad account restricted', 'A restriction that is not a full disable.'),
 ('/meta-ad-account-restricted-vs-disabled/', 'Restricted versus disabled', 'What each status means and what you can still do.'),
 ('/ad-account-unusual-activity/', 'Unusual activity notice', 'The vague notice that follows logins and payment changes.'),
 ('/ad-account-policy-violation-appeal/', 'Policy violation appeal', 'Appeal after an ad policy violation.'),
 ('/ad-account-request-review-not-showing/', 'No request review button', 'When the review option is missing.'),
 ('/meta-ad-account-appeal-rejected-what-next/', 'Appeal rejected', 'What to do after a denied review.'),
 ('/ad-account-disabled-after-hack/', 'Disabled after a hack', 'Secure first, then appeal.'),
 ('/business-manager-disabled/', 'Business Manager disabled', 'When the whole portfolio is gone.'),
 ('/why-was-my-facebook-ad-account-disabled-without-warning/', 'Disabled without warning', 'Why there was no notice.'),
 ('/how-long-does-meta-ad-account-review-take/', 'How long a review takes', 'What affects waiting time.'),
 ('/how-much-does-ad-account-recovery-cost/', 'What recovery costs', 'How the price is set.'),
 ('/can-i-make-a-new-ad-account-after-ban/', 'New ad account after a ban', 'Why a fresh account is risky.'),
 ('/agency-ad-account-recovery/', 'Agency ad account recovery', 'For agencies and white label work.'),
 ('/meta-business-verification-rejected/', 'Business verification rejected', 'Fixing a failed verification.'),
 ('/who-can-recover-a-disabled-facebook-ad-account/', 'Who can recover an ad account', 'Who can help and who to avoid.'),
 ('/guides/meta-ad-account-restricted/', 'Guide: restricted ad accounts', 'A long guide to every status.'),
]
def blurb(p):
    return re.split(r'(?<=[.?!])\s', p['hero'])[0]

def hub_body():
    out = []
    for g, h, intro in GROUPS:
        items = ['<a href="/%s/">%s</a> %s' % (p['slug'], esc(p['crumb']), esc(blurb(p))) for p in PAGES if p['group'] == g and p['slug'] != 'meta-ad-account-help']
        out.append(S(h, intro, ul(items)))
    out.append(S('Core pages', ul(['<a href="%s">%s</a> %s' % (u, esc(l), esc(b)) for u, l, b in EXISTING])))
    return out

HUB_P = dict(slug='meta-ad-account-help', group='hub', title='Meta Ad Account Help: Every Notice Explained',
 desc='Find your Meta ad account problem: disabled, restricted, payment, business portfolio or policy notices, by business type and country.',
 h1='Meta ad account help, by notice, business type and country', crumb='Meta ad account help', svc='Meta ad account help',
 hero='Pick the notice you got, your type of business or your country. Each page explains what the message usually means and what you can do first.',
 answer='This is a guide to Meta ad account problems: disabled accounts, restrictions, payment flags, business portfolio notices and rejected appeals. Choose the page that matches your notice. Each one covers what to check first and how Unbanz prepares an appeal through Meta’s official review. Meta makes the final decision.',
 cards=[('Start with the notice', 'Open Account Quality and read the exact wording. Most pages here begin from that message.'),
        ('Fix what you can', 'Billing, admins and ads are usually the first things to clean up before you ask for a review.'),
        ('Ask once, properly', 'One clear review request beats many quick ones. We can help you write it.')],
 body=[], faq=[('Where do I find the notice about my ad account?', 'Open Account Quality in Meta Business Suite or Business Support Home and select the ad account or the business portfolio.'),
               ('Which page should I start with?', 'Start with the one that matches the wording of your notice. If nothing matches, read the page on restricted versus disabled accounts.'),
               ('Does Unbanz work with Meta?', 'No. Unbanz is an independent service. We use the same official review routes that are open to you.'),
               ('Can anyone promise to get an ad account back?', 'No. Meta makes the final decision, and anyone who promises an outcome is not being honest.')],
 who=['Advertisers with a disabled or restricted ad account.', 'Agencies and media buyers with client accounts.', 'Business owners locked out of a portfolio.'],
 send_extra=[], related=[], alts=None, lang='en-US', wa=WA_AD, ws='ad', subj=MAIL_AD, crumb_parent=None)

import re
def related_for(p, idx_by_group, all_pages):
    g = [q for q in all_pages if q['group'] == p['group'] and q['slug'] != p['slug']]
    i = [q['slug'] for q in all_pages if q['group'] == p['group']].index(p['slug'])
    sib = [g[(i + k) % len(g)] for k in range(4)] if g else []
    nav1 = [(HUB, 'Meta ad account help'), ('/ad-account-recovery/', 'Ad account recovery')] + [('/%s/' % q['slug'], q['crumb']) for q in sib]
    pool = [('/facebook-ad-account-disabled/', 'Facebook ad account disabled'),
            ('/meta-ad-account-restricted-vs-disabled/', 'Restricted versus disabled'),
            ('/meta-ad-account-appeal-rejected-what-next/', 'Appeal rejected, what next'),
            ('/how-long-does-meta-ad-account-review-take/', 'How long does a review take?'),
            ('/how-much-does-ad-account-recovery-cost/', 'What does recovery cost?'),
            ('/guides/meta-ad-account-restricted/', 'Guide: restricted ad accounts'),
            ('/ad-account-request-review-not-showing/', 'No request review button'),
            ('/why-was-my-facebook-ad-account-disabled-without-warning/', 'Disabled without warning')]
    j = (i * 3) % len(pool)
    nav2 = [pool[(j + k) % len(pool)] for k in range(4)]
    other = [q for q in all_pages if q['group'] != p['group']]
    if other:
        o = other[(i * 5) % len(other)]
        nav2.append(('/%s/' % o['slug'], o['crumb']))
    return nav1, nav2

def all_pages():
    pages = list(PAGES)
    hub = dict(HUB_P)
    pages.append(hub)
    # hub body needs the list
    hub['body'] = hub_body()
    for p in pages:
        p['related_final'] = related_for(p, None, pages) if p['group'] != 'hub' else (
            [('/ad-account-recovery/', 'Ad account recovery'), ('/facebook-ad-account-disabled/', 'Facebook ad account disabled'), ('/services/', 'All services'), ('/guides/', 'Guides')],
            [('/how-long-does-meta-ad-account-review-take/', 'How long does a review take?'), ('/how-much-does-ad-account-recovery-cost/', 'What does recovery cost?'), ('/faq/', 'FAQ')])
    return pages
