from common import *
from b_tiktok import TT_LINKS
from b_youtube import YL
from b_contact import M
PAGES=[]
ALL=[('Instagram',[M['igdis'],M['status'],M['ighack'],M['igac']],'/instagram-appeal-links-and-forms-directory/'),
('Facebook',[M['fbdis'],M['fbhack'],('Find your account','https://www.facebook.com/login/identify','Password reset and lost email or phone.')],'/facebook-appeal-links-and-forms-directory/'),
('Meta ad accounts, Pages and Business Portfolios',[M['bsh'],M['adtrb'],('Page Admin Dispute','https://www.facebook.com/business/help/1580486349413648','When someone else controls a Page that should be yours.')],'/meta-ad-account-appeal-links-directory/'),
('Threads',[M['threads'],M['status']],'/threads-appeal-links-directory/'),
('WhatsApp',[M['wacontact'],M['wafaq']],'/whatsapp-banned-number-appeal-links-directory/'),
('TikTok',[TT_LINKS[0],TT_LINKS[1],TT_LINKS[5]],'/tiktok-appeal-links-and-forms-directory/'),
('YouTube',[YL['term'],YL['appeal'],YL['hack']],'/youtube-channel-terminated-appeal-links-directory/'),
('Snapchat',[M['snapacc'],M['snapappeal'],M['snaphack']],'/snapchat-support-links-and-forms-directory/'),
('EU dispute bodies',[M['ace'],('Oversight Board','https://www.oversightboard.com/','Takes a small number of Meta content decisions after the appeal.')],'/dsa-appeal-right-instagram-facebook/')]
secs=[('quick','Quick answer by platform',table([('Instagram','Appeal from the login notice or Account Status','No'),('Facebook','Appeal from the login notice','No'),('Meta ads','Business Support Home (admin)','Chat for some advertisers'),('TikTok','In-app appeal or tiktok.com/feedback','No'),('YouTube','Termination appeal form','Creator Support for some'),('Snapchat','accounts.snapchat.com, then appeal','No'),('WhatsApp','Request a review on the ban screen','No')],('Platform','Where appeals start','Phone or live support?')))]
for name,rows,href in ALL: secs.append((re.sub(r'[^a-z]+','-',name.lower()).strip('-'),name,linkrows(rows)+f'<p>Full list: {a(href,name+" directory")}.</p>'))
secs.append(('prices','If the official route fails',table([('Instagram','$800'),('Facebook profile','$900'),('Facebook Page','$600 per Page'),('Ad account','$1,200'),('Business Portfolio','$1,500'),('Snapchat','$800'),('TikTok','$900'),('YouTube channel','$1,200'),('Username claim','$1,200 flat')],('Unbanz service','Fixed fee'))+'<p>Every fee is paid upfront by card, with a 100% refund if the case fails. Usually 3–7 days, not guaranteed. Unbanz is independent and never asks for passwords.</p>'))
PAGES.append(P(slug='account-recovery-links-directory-all-platforms',crumb=('Guides','/guides/'),sv='unban',
 title='Account Recovery and Appeal Links for Every Platform (2026 Directory)',short='All-platform recovery links',
 desc='One page with the official appeal, recovery and support links for Instagram, Facebook, Meta ads, Threads, WhatsApp, TikTok, YouTube and Snapchat, checked November 2026.',
 h1='Official appeal and recovery links for every platform.',lede='Instagram, Facebook, Meta ads, Threads, WhatsApp, TikTok, YouTube and Snapchat, on one page.',
 answer='<strong>Every major platform starts appeals inside its own app or notice, and none offers a general phone line for banned accounts.</strong> Instagram and Facebook appeals start from the login notice, Meta ad accounts from Business Support Home, TikTok from the in-app appeal or tiktok.com/feedback, YouTube from the termination appeal form, Snapchat from accounts.snapchat.com, and WhatsApp from Request a review. The official links for each are below.',
 cards=[('Official only','Every link goes to the platform or an official body.'),('Checked','November 2026.'),('No phone lines','For banned accounts.')],
 sections=secs,
 faqs=[('Which platform has phone support for bans?','None offers a general phone line for banned accounts. Some paid programmes and advertisers get chat.'),('Is there one form for all Meta apps?','No. Each problem has its own route, listed above.'),('What does Unbanz charge?','Fixed fees from $600 to $1,500 depending on the service, paid upfront with a 100% refund if it fails.')],
 itemlist=[(t,u) for _,rows,_ in ALL for t,u,_w in rows]))
PAGES.append(P(slug='tiktok-unban-service',svc='tt',crumb=('Services','/services/'),
 title='TikTok Unban Service: Banned TikTok Account Recovery ($900, 100% Refund)',short='TikTok unban service',
 desc='Unbanz recovers banned and permanently banned TikTok accounts for a fixed $900, paid upfront, with a 100% refund if it fails. No passwords. Usually 3–7 days.',
 h1='TikTok unban service.',lede='Done-for-you recovery for banned TikTok accounts, for a fixed $900.',
 answer='<strong>Unbanz is an independent TikTok unban service: we recover banned and permanently banned TikTok accounts for $900, paid upfront, with a 100% refund if it fails.</strong> We never ask for your password or login codes, and work through TikTok’s own appeal and support channels. Work usually takes 3–7 days from the day we start; timing is not guaranteed and TikTok makes the final decision.',
 cards=[('$900 fixed','One account.'),('100% refund','If it fails.'),('3–7 days','Usual, not guaranteed.')],
 sections=[('what-we-handle','What we handle',ul(['Permanently banned TikTok accounts.','Accounts banned after mass reporting or a hack.','Creator and business accounts.','Appeals that were rejected or never answered.'])),
 ('not','What we do not do',ul(['Sell or buy TikTok accounts.','Ask for passwords, codes or ID outside TikTok’s own forms.','Promise a result; TikTok decides.'])),
 ('process','How it works',ol(['Send the username, a screenshot of the ban notice and your country to team@unbanz.com.','We tell you honestly if we can take it.','You pay $900 upfront by card through a secure checkout link.','We file and follow up through TikTok’s own channels.','If it fails, you get a 100% refund.'])),
 ('guides','Free guides first',ul([a('/tiktok-account-banned-how-to-get-it-back/','How to get a banned TikTok back'),a('/tiktok-appeal-what-to-write/','What to write in the appeal'),a('/tiktok-appeal-links-and-forms-directory/','TikTok appeal links')]))],
 faqs=[('Is a TikTok unban service legit?','Only if it never asks for your password and works through TikTok’s own processes. Unbanz does both and refunds 100% if it fails.'),('How much does it cost to unban a TikTok?','$900 per account at Unbanz.'),('Can you guarantee an unban?','No one can. We offer a 100% refund if it fails.')],
 related=[('/tiktok-account-help/','TikTok account help'),('/pricing/','Pricing')]))
PAGES.append(P(slug='youtube-channel-recovery-service',svc='yt',crumb=('Services','/services/'),
 title='YouTube Channel Recovery Service: Terminated Channels ($1,200, 100% Refund)',short='YouTube channel recovery service',
 desc='Unbanz recovers terminated and hacked YouTube channels for a fixed $1,200, paid upfront, with a 100% refund if it fails. No passwords. Usually 3–7 days.',
 h1='YouTube channel recovery service.',lede='Done-for-you recovery for terminated YouTube channels, for a fixed $1,200.',
 answer='<strong>Unbanz recovers terminated YouTube channels for $1,200, paid upfront, with a 100% refund if it fails.</strong> We handle terminations for spam and scams, linked channels, strikes and hacked channels, through YouTube’s own processes, without your password. Work usually takes 3–7 days from the day we start; not guaranteed, and YouTube makes the final decision.',
 cards=[('$1,200 fixed','One channel.'),('100% refund','If it fails.'),('No password','Never.')],
 sections=[('what-we-handle','What we handle',ul(['Channels terminated for spam, deceptive practices and scams.','Channels terminated because of a related channel.','Hacked channels terminated after scam streams.','Rejected termination appeals.'])),
 ('process','How it works',ol(['Send the channel link, the termination email and your country to team@unbanz.com.','We tell you honestly if we can take it.','You pay $1,200 upfront by card through a secure checkout link.','We prepare and file through YouTube’s processes and follow up.','If it fails, you get a 100% refund.'])),
 ('guides','Free guides first',ul([a('/youtube-channel-terminated-how-to-get-it-back/','Get a terminated channel back'),a('/youtube-termination-appeal-what-to-write/','What to write'),a('/youtube-channel-terminated-appeal-links-directory/','YouTube appeal links')]))],
 faqs=[('How much does YouTube channel recovery cost?','$1,200 per channel at Unbanz, upfront, with a 100% refund if it fails.'),('Do you handle copyright strikes?','Copyright terminations follow a different route; send us the details and we will tell you honestly.')],
 related=[('/youtube-account-help/','YouTube account help'),('/pricing/','Pricing')]))
PAGES.append(P(slug='account-recovery-service-cost-2026',crumb=('Pricing','/pricing/'),sv='unban',
 title='How Much Does Account Recovery Cost in 2026? (Instagram, Facebook, TikTok, YouTube)',short='Account recovery cost 2026',
 desc='What account recovery services cost in 2026 for Instagram, Facebook, Pages, ad accounts, TikTok, YouTube and usernames, what a fair deal includes, and red flags.',
 h1='How much does account recovery cost?',lede='Real fixed prices, what should be included, and the red flags that mean walk away.',
 answer='<strong>At Unbanz, recovery costs $800 for an Instagram account, $900 for a Facebook profile, $600 per Facebook Page, $1,200 for an ad account, $1,500 for a Business Portfolio, $800 for Snapchat, $900 for TikTok, $1,200 for a YouTube channel, and $1,200 flat for a username claim.</strong> Every fee is paid upfront, with a 100% refund if the case fails. Whatever service you use, a fair deal puts the price and refund terms in writing and never asks for your password.',
 cards=[('Fixed fees','Known before you pay.'),('100% refund','If it fails.'),('No passwords','A must, anywhere.')],
 sections=[('table','Unbanz price list',table([('Instagram disabled, suspended or hacked','$800'),('Facebook profile disabled, suspended or hacked','$900'),('Facebook Page (lost admin, or held by another Business Portfolio)','$600 per Page'),('Facebook Marketplace','$800'),('Instagram or Facebook ad account','$1,200'),('Meta Business Portfolio','$1,500'),('Username claim, including banned or inactive handles','$1,200 flat'),('Snapchat locked or banned','$800'),('TikTok banned','$900'),('YouTube channel terminated','$1,200')],('Service','Fee'))),
 ('fair-deal','What a fair deal includes',ul(['The price and refund terms in writing before you pay.','No request for passwords, login codes or session cookies.','Work through the platform’s own processes, not “insider” claims.','A realistic timeline, not a guaranteed result.'])),
 ('red-flags','Red flags',ul(['“Meta insider” or “TikTok employee” claims.','Payment in crypto or gift cards only.','Asking for your login.','Guaranteed results with no refund.'])),
 ('free-first','Try the free route first','<p>If you have not appealed yet, do that first: it is free. See '+a('/account-recovery-links-directory-all-platforms/','official links for every platform')+'.</p>')],
 faqs=[('Why pay upfront?','We take on the work immediately; the 100% refund protects you if it fails.'),('Is there a cheaper option?','The free in-app appeal. Use it before paying anyone.')],
 related=[('/pricing/','Pricing'),('/refund-policy/','Payment and refunds'),('/is-unbanz-legit/','Is Unbanz legit?')]))
