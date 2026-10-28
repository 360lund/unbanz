# -*- coding: utf-8 -*-
from lib import *
IGSEND = ['Your Instagram username (the public @handle).', 'A screenshot of the notice or error, with the date visible.',
          'Which email address or phone number is on the account (just which one, never a code).', 'What happened in the days before it started, in a few lines.']
FBSEND = ['Your Facebook profile link or the name on the profile.', 'A screenshot of the message or error, with the date visible.',
          'Which email address or phone number is on the account (just which one, never a code).', 'What happened before it started, in a few lines.']
SCSEND = ['Your Snapchat username.', 'A screenshot of the lock or ban message, with the date visible.',
          'Which phone number or email is on the account (just which one, never a code).', 'What phone you use and what happened before it started.']
fam('igsusp', ws='unban', platform='Instagram', parent=('Instagram account help', '/instagram-account-help/'), stype='Instagram suspension appeal help',
    wa=IG_WA, subj='Instagram%20suspension', what='an Instagram suspension', send=IGSEND,
    how1='your Instagram username and a screenshot of the notice',
    how3='We prepare the appeal and the supporting details, to go through Instagram’s own channels.')
fam('igappeal', ws='unban', platform='Instagram', parent=('Instagram account help', '/instagram-account-help/'), stype='Instagram appeal help',
    wa=IG_WA, subj='Instagram%20appeal', what='an Instagram appeal', send=IGSEND,
    how1='your Instagram username and a screenshot of where the appeal stops',
    how3='We work out which official route fits where you are stuck and prepare what to send.')
fam('igverify', ws='unban', platform='Instagram', parent=('Instagram account help', '/instagram-account-help/'), stype='Instagram identity verification help',
    wa=IG_WA, subj='Instagram%20verification', what='Instagram verification', send=IGSEND,
    how1='your Instagram username and a screenshot of the verification request',
    how3='We check what is going wrong in the request and help you prepare it again properly.')
fam('ighacked', ws='unban', platform='Instagram', parent=('Instagram account help', '/instagram-account-help/'), stype='Hacked Instagram account recovery',
    wa=IG_WA, subj='Hacked%20Instagram%20account', what='a hacked Instagram account', send=IGSEND,
    how1='your Instagram username and what you can still see or do',
    how3='We map the recovery routes that fit what the hacker changed and prepare the reports.')
fam('igrecov', ws='unban', platform='Instagram', parent=('Instagram account help', '/instagram-account-help/'), stype='Instagram account recovery',
    wa=IG_WA, subj='Instagram%20account%20recovery', what='Instagram account recovery', send=IGSEND,
    how1='your Instagram username and what happened to the account',
    how3='We prepare the recovery request and the supporting details for Instagram’s official process.')
fam('igrestrict', ws='unban', platform='Instagram', parent=('Instagram account help', '/instagram-account-help/'), stype='Instagram restriction help',
    wa=IG_WA, subj='Instagram%20restriction', what='an Instagram restriction', send=IGSEND,
    how1='your Instagram username and a screenshot of the message',
    how3='We tell you what the message points to and what is worth doing, including when waiting is the right call.')
fam('fbdis', ws='unban', platform='Facebook', parent=('Facebook account help', '/facebook-account-help/'), stype='Facebook disabled account appeal help',
    wa=FB_WA, subj='Facebook%20disabled%20account', what='a disabled Facebook account', send=FBSEND,
    how1='your Facebook profile link and a screenshot of the message',
    how3='We prepare the appeal and the supporting details, to go through Facebook’s own channels.')
fam('fblost', ws='unban', platform='Facebook', parent=('Facebook account help', '/facebook-account-help/'), stype='Facebook account access recovery',
    wa=FB_WA, subj='Facebook%20access%20problem', what='a Facebook login problem', send=FBSEND,
    how1='your Facebook profile link and what happens when you try to log in',
    how3='We work out which official recovery route fits and prepare what you need to send.')
fam('fbrecov', ws='unban', platform='Facebook', parent=('Facebook account help', '/facebook-account-help/'), stype='Facebook account recovery',
    wa=FB_WA, subj='Facebook%20account%20recovery', what='Facebook account recovery', send=FBSEND,
    how1='your Facebook profile link and what happened to the account',
    how3='We prepare the recovery request and the supporting details for Facebook’s official process.')
fam('snap', ws='unban', platform='Snapchat', parent=('Snapchat account help', '/snapchat-account-help/'), stype='Snapchat account unban help',
    wa=SC_WA, subj='Snapchat%20account%20help', what='a locked or banned Snapchat account', send=SCSEND,
    how1='your Snapchat username and a screenshot of the message',
    how3='We prepare the appeal and the details to go through Snapchat’s own support channels.')
fam('user', ws='username', platform='Instagram', parent=('Username claims', '/username/'), stype='Instagram username claim',
    wa=UN_WA, subj='Username%20claim', what='an Instagram username claim',
    send=['The exact @username you want.', 'Your current Instagram profile, so the handle can go onto it.', 'Why the name is yours: brand, business name, registered trademark, or the name you used before.',
          'What you have already tried, if anything.'],
    how1='the @username you want and your current profile',
    how3='We check the handle and pick the official route that fits it. Your password stays with you.')
fam('ad', ws='ad', platform='Facebook', parent=('Meta ad account help', '/meta-ad-account-help/'), stype='Meta ad account recovery',
    wa=AD_WA, subj='Meta%20ad%20account%20help', what='a Meta ad account problem',
    send=['The ad account ID and the business portfolio ID, if you have one.', 'A screenshot of the notice in Account Quality, with the date visible.',
          'What you were advertising and what changed just before the notice.', 'Who the admins on the account are.'],
    how1='the ad account ID and a screenshot of the notice',
    how3='We read the notice with you and prepare the appeal and the supporting details, to go through Meta’s own review.')
