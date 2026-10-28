# -*- coding: utf-8 -*-
import lib
from lib import *
I = [('/guides/instagram-account-suspended-appeal/', 'Instagram suspension appeal guide'), ('/guides/instagram-account-disabled/', 'Instagram account disabled'),
     ('/instagram-account-recovery/', 'Instagram account recovery'), ('/instagram-unban-service/', 'Instagram unban service'),
     ('/guides/hacked-instagram-account-recovery/', 'Hacked Instagram account recovery'), ('/guides/instagram-disabled-no-appeal-button/', 'Instagram disabled, no appeal button')]
FBL = [('/guides/facebook-account-disabled-appeal/', 'Facebook disabled account appeal'), ('/facebook-account-recovery/', 'Facebook account recovery'), ('/facebook-unban-service/', 'Facebook unban service')]
AD = [('/meta-ad-account-help/', 'Meta ad account help'), ('/ad-account-recovery/', 'Ad account recovery'), ('/guides/meta-ad-account-restricted/', 'Meta ad account restricted')]
WIN = {
 'igsusp': [I[0], I[1], I[3]], 'igappeal': [I[1], I[5], I[0]], 'igverify': [I[3], I[1], I[2]], 'ighacked': [I[4], I[2], I[3]],
 'igrecov': [I[2], I[3], I[1]], 'igrestrict': [I[3], I[0], I[2]],
 'fbdis': [FBL[0], FBL[2], FBL[1]], 'fblost': [FBL[1], FBL[2], FBL[0]], 'fbrecov': [FBL[1], FBL[2], FBL[0]],
 'snap': [('/snapchat-unban-service/', 'Snapchat unban service'), ('/how-long-does-a-snapchat-lock-last/', 'How long a Snapchat lock lasts'), ('/can-a-permanently-banned-snapchat-account-be-recovered/', 'Permanently banned Snapchat account')],
 'user': [('/username/', 'Instagram username claims'), ('/instagram-username-claim-refund/', 'Username claim refund'), ('/someone-took-my-old-instagram-username/', 'Someone took my old username')],
 'ad': AD, 'hubig': I[:3], 'hubfb': FBL, 'hubsc': [('/snapchat-unban-service/', 'Snapchat unban service')],
}
POOL = {
 'igsusp': [('/instagram-appeal-denied/', 'Instagram appeal denied'), ('/guides/instagram-appeal-sent-no-response/', 'Appeal sent, no response'), ('/guides/why-instagram-bans-accounts/', 'Why Instagram bans accounts')],
 'igappeal': [('/instagram-appeal-denied/', 'Instagram appeal denied'), ('/guides/instagram-appeal-sent-no-response/', 'Appeal sent, no response'), ('/guides/why-instagram-bans-accounts/', 'Why Instagram bans accounts')],
 'igverify': [('/guides/instagram-account-disabled/', 'Instagram account disabled'), ('/guides/why-instagram-bans-accounts/', 'Why Instagram bans accounts')],
 'ighacked': [('/instagram-hacked-account-recovery-service/', 'Hacked account recovery service'), ('/guides/instagram-account-restored-next-steps/', 'Account restored next steps')],
 'igrecov': [('/guides/instagram-account-restored-next-steps/', 'Account restored next steps'), ('/guides/why-instagram-bans-accounts/', 'Why Instagram bans accounts')],
 'igrestrict': [('/guides/why-instagram-bans-accounts/', 'Why Instagram bans accounts'), ('/guides/instagram-account-restored-next-steps/', 'Account restored next steps')],
 'fbdis': [('/facebook-account-disabled-appeal-help/', 'Facebook disabled appeal help'), ('/facebook-hacked-account-recovery-service/', 'Hacked Facebook account')],
 'fblost': [('/facebook-hacked-account-recovery-service/', 'Hacked Facebook account'), ('/facebook-account-disabled-appeal-help/', 'Facebook disabled appeal help')],
 'fbrecov': [('/facebook-hacked-account-recovery-service/', 'Hacked Facebook account'), ('/facebook-account-disabled-appeal-help/', 'Facebook disabled appeal help')],
 'snap': [('/snapchat-account-ban-service/', 'Snapchat account removal'), ('/snapchat-username-claim/', 'Snapchat username claim')],
 'user': [('/trademark-username-claim/', 'Trademark username claim'), ('/business-username-claim/', 'Brand username claim'), ('/one-letter-username/', 'One-letter usernames')],
 'ad': [('/how-long-does-meta-ad-account-review-take/', 'How long a review takes'), ('/meta-ad-account-appeal-what-to-write/', 'What to write in an appeal'), ('/meta-ad-account-appeal-rejected-what-next/', 'Appeal rejected, what next')],
}
GROUPS = {
 'hubig': [('igsusp', 'Suspended accounts'), ('igappeal', 'Appeal problems'), ('ighacked', 'Hacked accounts'), ('igverify', 'Identity and selfie checks'), ('igrestrict', 'Action blocked and restrictions'), ('igrecov', 'Recovery by business type')],
 'hubfb': [('fbdis', 'Disabled accounts'), ('fblost', 'Lost access and hacked accounts'), ('fbrecov', 'Recovery by account type')],
 'hubsc': [('snap', 'Locked and banned accounts')],
}
for k, parent_t in (('hubig', 'Instagram'), ('hubfb', 'Facebook'), ('hubsc', 'Snapchat')):
    base = {'hubig': 'igsusp', 'hubfb': 'fbdis', 'hubsc': 'snap'}[k]
    F = dict(FAM[base]); F['parent'] = ('Services', '/services/'); FAM[k] = F
HUBS = {}
def make_hubs():
    spec = {
     'hubig': ('instagram-account-help', 'Instagram Account Help: Suspended, Hacked, Disabled', 'Instagram account help', 'Instagram help',
        'Pick your Instagram situation: suspended, disabled, hacked, stuck on an appeal or a selfie check, or action blocked. Short answers and what to send.',
        'Find the page that matches what Instagram told you.',
        'Instagram problems look similar but need different steps. Find your situation below: a suspension, a disabled account, a hack, an appeal that loops, an identity check or an action block. Each page leads with the answer, lists what to gather, and shows how to reach us.'),
     'hubfb': ('facebook-account-help', 'Facebook Account Help: Disabled, Hacked, Locked Out', 'Facebook account help', 'Facebook help',
        'Pick your Facebook situation: disabled, hacked, locked out or lost access. Short answers on what the message means and what to send.',
        'Find the page that matches what Facebook told you.',
        'Facebook problems need different steps depending on the message: disabled, hacked, locked out after a phone change, or lost two-factor access. Find your situation below. Each page leads with the answer, lists what to gather and shows how to reach us.'),
     'hubsc': ('snapchat-account-help', 'Snapchat Account Help: Locked, Banned, Hacked', 'Snapchat account help', 'Snapchat help',
        'Pick your Snapchat situation: locked, banned, hacked or missing Memories. Short answers on what the message means and what to send.',
        'Find the page that matches what Snapchat told you.',
        'Snapchat locks and bans differ by reason: a modified app, spam, a content flag, a new phone or a hack. Find your situation below. Each page leads with the answer, lists what to gather and shows how to reach us.')}
    for k, (slug, title, h1, crumb, desc, hero, answer) in spec.items():
        secs = []
        for f, label in GROUPS[k]:
            items = [A('/%s/' % p['slug'], esc(p['crumb'])) for p in PAGES if p['fam'] == f]
            secs.append(S(label, ul(items)))
        page(slug, k, title, desc, h1, crumb, hero, answer,
             [('Read the message', 'The exact wording tells you which route applies.'), ('Gather proof', 'Screenshots, dates and the account details.'), ('Do not rush', 'Repeated attempts can make things harder.')],
             (secs + [S('Before you contact us', ul(['The exact wording of the message, with the date.', 'The username or profile link.', 'What happened just before it started.']))] if len(secs) < 2 else secs), [('Do you need my password?', 'No. Your password and codes stay with you.'), ('Is Unbanz part of the platform?', 'No. Unbanz is an independent service and is not affiliated with Meta or Snapchat.'), ('Can you promise a result?', 'No. Nobody can. We tell you honestly what is possible.')],
             ['People who are not sure which page fits.', 'Owners with a notice they do not understand.', 'Agencies helping a client.'])
INJECT = {}
def inj(url, label, fams, n=10, extra=()):
    INJECT[url] = (label, fams, n, list(extra))
def build_inject():
    I_ = lambda *a, **k: inj(*a, **k)
    h_ig = ('/instagram-account-help/', 'Instagram account help: all situations'); h_fb = ('/facebook-account-help/', 'Facebook account help: all situations'); h_sc = ('/snapchat-account-help/', 'Snapchat account help: all situations')
    I_('/guides/instagram-account-suspended-appeal/', 'More suspension situations', ['igsusp'], 10, [h_ig])
    I_('/guides/instagram-account-disabled/', 'More disabled and appeal situations', ['igappeal', 'igverify'], 12, [h_ig])
    I_('/instagram-account-recovery/', 'Recovery for your kind of business', ['igrecov'], 10, [h_ig])
    I_('/instagram-unban-service/', 'Find your situation', ['igsusp', 'igrestrict', 'igverify'], 9, [h_ig])
    I_('/guides/hacked-instagram-account-recovery/', 'More hacked account situations', ['ighacked'], 10, [h_ig])
    I_('/instagram-hacked-account-recovery-service/', 'More hacked account situations', ['ighacked'], 6, [h_ig])
    I_('/guides/instagram-disabled-no-appeal-button/', 'More appeal problems', ['igappeal'], 8, [h_ig])
    I_('/guides/facebook-account-disabled-appeal/', 'More disabled Facebook situations', ['fbdis'], 10, [h_fb])
    I_('/facebook-account-recovery/', 'Facebook recovery situations', ['fbrecov', 'fblost'], 12, [h_fb])
    I_('/facebook-unban-service/', 'Find your situation', ['fbdis', 'fblost'], 8, [h_fb])
    I_('/username/', 'More username situations', ['user'], 10)
    I_('/meta-ad-account-help/', 'More ad account situations', ['ad'], 13)
    I_('/ad-account-recovery/', 'More ad account situations', ['ad'], 13)
    I_('/guides/meta-ad-account-restricted/', 'More ad account situations', ['ad'], 8)
    I_('/snapchat-unban-service/', 'More Snapchat situations', ['snap'], 10, [h_sc])
    I_('/guides/', 'Account help by platform', [], 0, [h_ig, h_fb, h_sc])
    I_('/unban/', 'Account help by platform', [], 0, [h_ig, h_fb, h_sc])
    I_('/services/', 'Account help by platform', [], 0, [h_ig, h_fb, h_sc])
build_inject()
