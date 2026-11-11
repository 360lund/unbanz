from common import *
import b_tiktok,b_youtube,b_page
def title_of(slug):
    import re,html
    t=open(f'{SITE}/{slug}/index.html').read(); m=re.search(r'<title>(.*?)</title>',t); s=html.unescape(m.group(1))
    return re.split(r' \| | – Unbanz| - Unbanz',s)[0]
def lst(slugs): return ul([a('/'+s+'/',html.escape(title_of(s))) for s in slugs])
H=[]
tt_new=[p['slug'] for p in b_tiktok.PAGES]
tt_old=['tiktok-appeal-links-and-forms-directory','tiktok-account-banned-appeal','tiktok-your-account-was-permanently-banned-notice','tiktok-your-account-is-temporarily-restricted-notice','tiktok-hacked-account-recovery','tiktok-business-account-suspended','tiktok-shop-account-suspended-business','brand-name-taken-on-instagram-and-tiktok']
H.append(P(slug='tiktok-account-help',svc='tt',crumb=('Services','/services/'),
 title='TikTok Account Banned or Suspended? Help, Guides and Recovery ($900)',short='TikTok account help',
 desc='Everything for a banned, suspended or hacked TikTok account: official appeal links, notices explained, step-by-step guides, and TikTok ban recovery for $900 upfront with a 100% refund.',
 h1='TikTok account banned? Start here.',lede='Guides for every TikTok ban, plus done-for-you recovery for a fixed $900.',
 answer='<strong>Unbanz handles banned TikTok accounts for $900, paid upfront by card, with a 100% refund if it fails.</strong> Work usually takes 3–7 days from the day we start, but that is not guaranteed and TikTok makes the final decision. We are independent, not TikTok, and never need your password. If you have not appealed yet, start with the free in-app appeal; the guides below show how.',
 cards=[('$900','One banned TikTok account.'),('100% refund','If the case fails.'),('No password','We never ask for logins.')],
 sections=[('start','Start with the right guide',lst(tt_new[:6])),('more','More TikTok guides',lst(tt_new[6:])),('reference','Reference pages',lst(tt_old)),
  ('how-we-work','How the service works',ol(['Send the username, a screenshot of the ban notice and your country.','We tell you honestly whether it is a case we can take.','You pay $900 upfront by card through a secure checkout link we send.','We prepare and file the case through TikTok’s own channels and follow up.','If it fails, you get a 100% refund.']))],
 faqs=[('How much does it cost to recover a banned TikTok?','$900 per account at Unbanz, paid upfront, with a 100% refund if it fails.'),('How long does it take?','Usually 3–7 days from the day we start. Not guaranteed.'),('Can you recover a permanently banned TikTok?','Often, yes, especially when the ban was a mistake. TikTok makes the final decision.'),('Do you work with TikTok?','No. Unbanz is independent and works through TikTok’s public processes.')],
 itemlist=[(title_of(s),'https://unbanz.com/'+s+'/') for s in tt_new]))
yt_new=[p['slug'] for p in b_youtube.PAGES]
H.append(P(slug='youtube-account-help',svc='yt',crumb=('Services','/services/'),
 title='YouTube Channel Terminated? Help, Guides and Recovery ($1,200)',short='YouTube account help',
 desc='Help for terminated, struck or hacked YouTube channels: official links, strikes explained, appeal guides, and YouTube channel recovery for $1,200 upfront with a 100% refund.',
 h1='YouTube channel terminated? Start here.',lede='Guides for terminations, strikes and hacked channels, plus done-for-you recovery for a fixed $1,200.',
 answer='<strong>Unbanz handles terminated YouTube channels for $1,200, paid upfront by card, with a 100% refund if it fails.</strong> Work usually takes 3–7 days from the day we start, but that is not guaranteed and YouTube makes the final decision. We are independent, not Google, and never ask for your password or 2-Step codes. Try the free termination appeal first; the guides below show how.',
 cards=[('$1,200','One terminated channel.'),('100% refund','If the case fails.'),('No password','We never ask for logins.')],
 sections=[('start','Start with the right guide',lst(yt_new[:6])),('more','More YouTube guides',lst(yt_new[6:]+['youtube-channel-terminated-appeal-links-directory'])),
  ('how-we-work','How the service works',ol(['Send the channel link, the termination email and your country.','We tell you honestly whether we can take it.','You pay $1,200 upfront by card through a secure checkout link we send.','We prepare and file through YouTube’s own processes and follow up.','If it fails, you get a 100% refund.']))],
 faqs=[('How much does it cost to recover a terminated YouTube channel?','$1,200 per channel at Unbanz, paid upfront, with a 100% refund if it fails.'),('Can a terminated channel come back?','Yes, when the appeal succeeds. Hacked and mistaken terminations are the best candidates.'),('Do you need access to my Google Account?','No passwords or codes. We work from the channel details and the termination email.')],
 itemlist=[(title_of(s),'https://unbanz.com/'+s+'/') for s in yt_new]))
pg_new=[p['slug'] for p in b_page.PAGES]
pg_old=['guides/facebook-page-admin-access-lost','guides/facebook-page-hacked-admin-removed','guides/facebook-page-restricted','facebook-disabled-page-admin-lost-pages','facebook-business-page-unpublished-what-to-do','facebook-page-unpublished-vs-account-disabled','facebook-page-restricted-but-ad-account-ok','facebook-page-recommendations-restricted','facebook-profile-disabled-managing-business-pages','white-label-facebook-page-recovery']
H.append(P(slug='facebook-page-recovery',svc='page',crumb=('Services','/services/'),
 title='Facebook Page Recovery: Lost Admin or Page Held by Another Business ($600)',short='Facebook Page recovery',
 desc='Recover a Facebook Page when you lost admin access or another Business Portfolio controls it. Guides, official routes, and Page recovery for $600 per Page upfront with a 100% refund.',
 h1='Facebook Page recovery.',lede='For Pages where you lost admin access, or the Page is held by another Business Portfolio.',
 answer='<strong>Unbanz recovers Facebook Pages for $600 per Page, paid upfront by card, with a 100% refund if it fails.</strong> That covers lost admin access and Pages controlled by another Business Portfolio, such as a former agency or employee. Work usually takes 3–7 days from the day we start, not guaranteed; Meta makes the final decision. We are independent, not Meta, and never need passwords.',
 cards=[('$600 per Page','Fixed fee.'),('100% refund','If it fails.'),('No logins','Never passwords or codes.')],
 sections=[('situations','Common situations',lst(pg_new)),('reference','More Page guides',lst(pg_old)),
  ('how-we-work','How the service works',ol(['Send the Page link, what happened, and any proof the Page is yours.','We tell you honestly whether we can take it.','You pay $600 per Page upfront by card through a secure checkout link we send.','We work through Meta’s own Page and Business processes.','If it fails, you get a 100% refund.'])),
  ('other-fees','Related fees','<p>If the admin’s personal profile is disabled or hacked, that is a Facebook profile case ($900). A disabled Business Portfolio is $1,500, and a restricted ad account is $1,200. See '+a('/pricing/','pricing')+'.</p>')],
 faqs=[('How much does Facebook Page recovery cost?','$600 per Page, paid upfront, with a 100% refund if it fails.'),('Can you recover a Page another Business Portfolio claimed?','Yes, that is one of the main cases we handle, through Meta’s own processes.'),('Do I lose followers?','No. Followers stay with the Page.')],
 itemlist=[(title_of(s),'https://unbanz.com/'+s+'/') for s in pg_new]))
