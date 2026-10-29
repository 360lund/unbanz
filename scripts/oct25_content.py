# -*- coding: utf-8 -*-
"""Content for the 13 pages added on 2026-10-25. Rendered by build_oct25_pages.py."""

DATE = "2026-10-25"

def A(href, label):
    return '<a href="%s">%s</a>' % (href, label)

def how(step1, username=False):
    price = ('We tell you honestly if we can help and what it costs.' if username
             else 'We tell you honestly if we can help and what it costs.')
    what = 'handle the username through the platform’s official process' if username else 'handle the appeal through the platform’s official process'
    return ('<h2 id="how">How it works with Unbanz</h2><ol><li>%s</li><li>%s</li><li>We prepare everything and %s.</li>'
            '<li>We keep you posted until there’s a result.</li></ol>') % (step1, price, what)

ACCT_STEP1 = 'Message us on WhatsApp or email with the username or profile link, the email or phone on the account, and a screenshot of the notice.'
USER_STEP1 = 'Message us on WhatsApp or email with the handle you want, your current profile, and any proof of a brand or trademark if you have one.'

def who(items):
    return '<h2 id="who">Who this is for</h2><ul>%s</ul>' % ''.join('<li>%s</li>' % i for i in items)

def sec(id_, h2, body):
    return '<h2 id="%s">%s</h2>%s' % (id_, h2, body)

def ul(items): return '<ul>%s</ul>' % ''.join('<li>%s</li>' % i for i in items)
def ol(items): return '<ol>%s</ol>' % ''.join('<li>%s</li>' % i for i in items)

CONTACT_FAQ = ('How do I contact Unbanz?', 'WhatsApp +1 934 201 2490 or team@unbanz.com.')
PASSWORD_FAQ = ('Do I need to share my Instagram password?', 'No. Your password and login codes stay with you. Anyone who asks for them is not someone to work with.')
WA_USER = 'Hey%20Unbanz%2C%20I%20want%20to%20claim%20this%20username%3A%20%40'
RECOVER_WA = 'Hey%20Unbanz%2C%20I%20need%20help%20recovering%20my%20Instagram%20account'
CAN_FAQ = ('Can Unbanz recover my account?', 'We help you submit a clean appeal through Meta’s official process and handle it end to end. Meta makes the final decision, so we tell you upfront whether we think it’s doable.')
COMMON_REL = [('/instagram-account-recovery/','Instagram account recovery'),('/instagram-account-disabled-appeal/','Instagram disabled appeal'),('/instagram-hacked-account-recovery-service/','Hacked Instagram recovery'),('/hacker-changed-my-instagram-email-and-password/','Hacker changed email and password'),('/instagram-appeal-denied/','Appeal denied'),('/unban-pricing/','Unban cost and timing'),('/services/','All services')]

def hf(place):
    return ('How do I recover a hacked Instagram account in %s?' % place,
            'Use the undo link in Instagram’s email about the change if there is one, then go to instagram.com/hacked on a device you used before and follow the steps. Instagram may ask for a code or a video selfie. If you see a disabled notice, request a review once.')

PAGES = []

def country(slug, cc, title, desc, h1, crumb, hero, answer, first, local_h, local, extra, who_items, faq, related, relq):
    PAGES.append(dict(
     slug=slug, lang='en-US' if cc == 'us' else 'en', title=title, desc=desc, h1=h1, crumb=crumb, svc=crumb,
     hero=hero, wa=RECOVER_WA, ws='unban', subj='Instagram%20account%20recovery', answer=answer,
     body=[
      sec('first','Official steps that come first', ol(first)),
      sec('local', local_h, ul(local)) + extra,
      sec('avoid','What not to do', ul([
        'Don’t pay or message anyone from a DM who says they can “open” your account.',
        'Don’t share your password or login codes with anyone, including us.',
        'Don’t create new accounts to plead with Instagram, and don’t send the same appeal over and over.'])),
      sec('help','How Unbanz helps','<p>We work out whether the account is disabled, hacked or both, gather the notice, the old email and phone and the dates, and handle the appeal through Meta’s official process. Main page: '+A('/instagram-account-recovery/','Instagram account recovery')+'.</p>'),
      how(ACCT_STEP1),
      who(who_items),
     ],
     faq=faq + [PASSWORD_FAQ, CONTACT_FAQ], related=related, relq=relq))

# 1 USA
country('instagram-account-recovery-usa','us',
 'Instagram Account Recovery Service in the USA | Unbanz',
 'Hacked or disabled Instagram account in the US? The official recovery routes, US-specific checks, and how Unbanz helps with a clean appeal.',
 'Instagram account recovery service in the USA.','Instagram account recovery USA',
 'Locked out of Instagram, or disabled after a hack? This page covers the official routes first, then how Unbanz helps US accounts with a clean appeal through Meta’s official process.',
 'Instagram account recovery in the US starts with Instagram’s own tools: the in-app review for disabled accounts and instagram.com/hacked for hijacked ones. If those stall, Unbanz helps you submit a clean appeal through Meta’s official process. Meta makes the final decision, and your password stays with you.',
 ['Search your inbox and spam for an email from Instagram about a changed email address or password. If it has a link to undo the change, use it straight away.',
  'Open instagram.com/hacked on a phone or computer you have logged in from before, on your usual network.',
  'Follow the prompts. Instagram may send a code to the email or number on the account, or ask for a video selfie where you turn your head in different directions.',
  'If you only see a disabled notice, tap through it and request a review. Do this once and complete every step it asks for.',
  'Watch the email on the account. Replies from Instagram arrive there, so check spam too.'],
 'Checks that matter in the US',
 ['<strong>Your phone number:</strong> text codes go to your US number. If you lost the SIM or stopped getting texts, sort that with your carrier first, and ask about port-out protection. SIM swapping is a known way accounts get hijacked.',
  '<strong>Your deadline:</strong> a disabled notice can carry a date after which the appeal option goes away. Read the date on your own notice and act before it.',
  '<strong>Business accounts:</strong> have your business name, website and state registration details to hand if Meta asks you to show the business is real.',
  '<strong>Money or blackmail involved:</strong> report it at ReportFraud.ftc.gov, and at ic3.gov (the FBI’s Internet Crime Complaint Center) if it’s serious. That’s separate from getting the account back.'],
 '<p>Not sure which problem you have? '+A('/instagram-account-disabled-appeal/','Disabled or suspended')+', '+A('/instagram-hacked-account-recovery-service/','hacked')+' and '+A('/instagram-account-disabled-after-hack-appeal/','hacked, then disabled')+' each have their own steps.</p>',
 ['US creators and small businesses who run sales or clients through Instagram.','People hacked through a phishing link or a SIM swap.','Anyone who already appealed once and got nowhere.','Not for: accounts that were really used for scams or abuse.'],
 [hf('the US'),
  ('Is Instagram recovery different in the US?','No. Instagram uses the same official routes everywhere. The US parts are your phone number for codes, the business details you may need to show, and where to report fraud, such as ReportFraud.ftc.gov.'),
  ('What if I no longer have the email or phone on the account?','Instagram’s hacked flow offers other ways to prove it’s you, such as a video selfie. If your number was swapped, call your carrier too. Send us what you have and we tell you which route fits.'),
  CAN_FAQ],
 COMMON_REL,
 [('/instagram-account-recovery-uk/','Recovery in the UK'),('/instagram-account-recovery-india/','Recovery in India'),('/instagram-account-recovery-uae/','Recovery in the UAE')])

# 2 India
country('instagram-account-recovery-india','in',
 'Instagram Account Recovery in India: Official Help | Unbanz',
 'Hacked or disabled Instagram account in India? Official steps, the India grievance route, and how Unbanz helps with a clean appeal in English.',
 'Instagram account recovery in India.','Instagram account recovery India',
 'Instagram account hacked or disabled and you’re in India? Here are the official steps, the extra India-specific route, and how Unbanz helps you appeal through Meta’s official process.',
 'In India, Instagram account recovery follows Instagram’s own routes: the review option on a disabled notice, or instagram.com/hacked for hijacked accounts. India also has a separate grievance route under the IT Rules. Unbanz helps you submit a clean appeal through Meta’s official process; Meta makes the final decision.',
 ['If you see a disabled or suspended notice, tap it and request a review. Finish every step it asks for.',
  'If you can’t log in because the email, number or password was changed, go to instagram.com/hacked and follow the prompts.',
  'Check your email, including spam, for a message from Instagram about the change. If it has an undo link, use it first.',
  'If Instagram asks for a video selfie, record it in good light and turn your head as shown. If it isn’t accepted, you can try again.'],
 'What is different in India',
 ['<strong>Codes go to your number:</strong> text codes go to your +91 number. If you lost the SIM or changed operator, sort that out first or the codes will go nowhere.',
  '<strong>Phishing is the usual way in:</strong> fake “copyright violation” warnings, “blue tick” or verification-badge offers, and DM links claiming to show who viewed your profile. Never enter your login on a page you reached from a message.',
  '<strong>If money or blackmail is involved:</strong> the National Cyber Crime Reporting Portal (cybercrime.gov.in) takes reports, and 1930 is the helpline for financial cyber fraud.',
  '<strong>Everything in English:</strong> we work over WhatsApp or email in English. You send the notice as it appears on your screen.'],
 '<h2 id="gac">The India grievance route</h2><p>This is separate from Instagram’s in-app appeal. India’s IT Rules, 2021 set up a grievance process for users of social platforms. If you complained to the platform’s Grievance Officer and are unhappy with the response, you can appeal to the Grievance Appellate Committee at gac.gov.in within 30 days of that response. It’s a formal route with its own limits, not a shortcut, so try the in-app appeal first and read the portal’s own guidance before you file.</p>',
 ['Indian creators, shops and agencies who run their work through Instagram.','People hacked through a phishing link or a fake badge offer.','Anyone who already appealed once and got nowhere.','Not for: accounts that were really used for scams or abuse.'],
 [hf('India'),
  ('Can I complain to the Grievance Appellate Committee about my Instagram account?','Yes, but only after the platform’s Grievance Officer has responded to your complaint. You then have 30 days from that response to appeal at gac.gov.in. It sits alongside Instagram’s own appeal and isn’t certain to restore an account.'),
  ('My Instagram account was hacked and my +91 number was changed. What now?','Contact your operator about the SIM first, then use instagram.com/hacked. Instagram offers other ways to prove it’s you, such as a video selfie. Send us what you have and we tell you which route fits.'),
  CAN_FAQ],
 [r for r in COMMON_REL if 'hacker-changed' not in r[0]] + [('/guides/instagram-fake-ban-or-copyright-emails/','Fake Instagram ban emails')],
 [('/instagram-account-recovery-usa/','Recovery in the USA'),('/instagram-account-recovery-uae/','Recovery in the UAE'),('/instagram-account-recovery-uk/','Recovery in the UK')])

# 3 UAE
country('instagram-account-recovery-uae','ae',
 'Instagram Account Recovery in UAE: Official Help | Unbanz',
 'Hacked or disabled Instagram account in the UAE? Official recovery steps, UAE reporting options, and how Unbanz helps with a clean appeal.',
 'Instagram account recovery in the UAE.','Instagram account recovery UAE',
 'Instagram account hacked or disabled and you’re in the UAE? Here are the official steps first, then how Unbanz helps you appeal through Meta’s official process.',
 'Instagram account recovery in the UAE uses the same official routes as everywhere: the review option on a disabled notice, or instagram.com/hacked if someone took over the account. Unbanz helps you submit a clean appeal through Meta’s official process, in English, over WhatsApp. Meta makes the final decision.',
 ['If you see a disabled or suspended notice, tap it and request a review. The notice may show in Arabic or English. The options are the same.',
  'If someone changed your email, number or password, go to instagram.com/hacked on a device you have used before.',
  'Check your email, including spam, for a message from Instagram about the change and use its undo link if it’s still valid.',
  'Follow any code or video selfie request. Then wait for the reply to the email on the account rather than sending repeat appeals.'],
 'Checks that matter in the UAE',
 ['<strong>Keep the notice as it is:</strong> screenshot it in whatever language it shows and send it to us unedited.',
  '<strong>Your +971 number:</strong> codes are sent by text. If you changed number, or run two, tell us which one is on the account.',
  '<strong>Business accounts:</strong> if the account sells or promotes a business, have the business name, website and trade licence details ready. They help you show the business is real if you’re asked for documents.',
  '<strong>Reporting a hack:</strong> if there was fraud, blackmail or stolen money, report it to UAE police through an official e-service such as Dubai Police’s eCrime platform (ecrime.ae) or the Ministry of Interior’s e-services. That runs alongside the Instagram appeal.',
  '<strong>Time zone:</strong> the UAE is on Gulf Standard Time (UTC+4). Notice deadlines are counted in days, so check the date on yours.'],
 '',
 ['UAE shops, agencies and creators who run their work through Instagram.','People hacked through a phishing link.','Anyone who already appealed once and got nowhere.','Not for: accounts that were really used for scams or abuse.'],
 [hf('the UAE'),
  ('Does it matter that my Instagram notice is in Arabic?','No. The review options are the same whichever language the notice shows. Take a screenshot of it as it appears and send it to us.'),
  ('Where do I report a hacked Instagram account in the UAE?','To Instagram first, through instagram.com/hacked. If there was fraud, blackmail or stolen money, also report it to UAE police through an official e-service such as Dubai Police’s eCrime platform (ecrime.ae).'),
  CAN_FAQ],
 COMMON_REL,
 [('/instagram-account-recovery-usa/','Recovery in the USA'),('/instagram-account-recovery-india/','Recovery in India'),('/instagram-account-recovery-uk/','Recovery in the UK')])

# 4 UK
country('instagram-account-recovery-uk','gb',
 'Instagram Account Recovery in the UK: Official Help | Unbanz',
 'Hacked or disabled Instagram account in the UK? Official recovery steps, where to report fraud, and how Unbanz helps with a clean appeal.',
 'Instagram account recovery in the UK.','Instagram account recovery UK',
 'Instagram account hacked or disabled and you’re in the UK? Here are the official steps first, where to report fraud, and how Unbanz helps you appeal through Meta’s official process.',
 'UK Instagram account recovery starts with Instagram’s own routes: request a review on a disabled notice, or use instagram.com/hacked if someone took over the account. If you lost money, report it too. Unbanz helps you submit a clean appeal through Meta’s official process; Meta makes the final decision.',
 ['If you see a disabled or suspended notice, tap it and request a review. Complete every step, including any selfie check.',
  'If the email, number or password was changed, go to instagram.com/hacked on a device and network you have used before.',
  'Check your email, including spam, for a message from Instagram about the change and use its undo link if it works.',
  'Send one complete appeal, then watch the email on the account for the reply.'],
 'Checks that matter in the UK',
 ['<strong>Your +44 number:</strong> text codes go to your UK number. If you lost the SIM or the number was ported, speak to your network first.',
  '<strong>Reporting fraud:</strong> if the hack led to scams, blackmail or lost money, report it through Report Fraud (reportfraud.police.uk) in England, Wales and Northern Ireland, or call Police Scotland on 101. If money left your bank account, tell your bank straight away.',
  '<strong>Practical guidance:</strong> the National Cyber Security Centre publishes a plain-English “Recovering a hacked account” guide at ncsc.gov.uk, which is worth reading alongside Instagram’s steps.',
  '<strong>Business accounts:</strong> have your trading name, website and Companies House details to hand if you’re asked to show the business is real.'],
 '',
 ['UK creators, shops and agencies who run their work through Instagram.','People hacked through a phishing link or a fake login page.','Anyone who already appealed once and got nowhere.','Not for: accounts that were really used for scams or abuse.'],
 [hf('the UK'),
  ('Where do I report a hacked Instagram account in the UK?','To Instagram first, through instagram.com/hacked. If there was fraud or lost money, also use Report Fraud at reportfraud.police.uk (England, Wales, Northern Ireland) or call Police Scotland on 101, and tell your bank if money was taken.'),
  ('What if the hacker changed my email and phone number?','instagram.com/hacked still applies. Instagram can offer other ways to prove it’s you, such as a video selfie. Send us what you have and we tell you which route fits.'),
  CAN_FAQ],
 COMMON_REL,
 [('/instagram-account-recovery-usa/','Recovery in the USA'),('/instagram-account-recovery-india/','Recovery in India'),('/instagram-account-recovery-uae/','Recovery in the UAE')])

def page(**kw):
    PAGES.append(kw)

# 5 hacked IG service
page(slug='instagram-hacked-account-recovery-service', lang='en',
 title='Hacked Instagram Account Recovery Service | Unbanz',
 desc='Instagram account hacked? The official recovery steps, what to do first, and how Unbanz helps you appeal through the official process.',
 h1='Hacked Instagram account recovery service.', crumb='Hacked Instagram account recovery', svc='Hacked Instagram account recovery service',
 hero='Someone changed your Instagram email or password, or posted as you? This page walks through the official recovery routes and how Unbanz helps you appeal through Meta’s official process.',
 wa='Hey%20Unbanz%2C%20my%20Instagram%20account%20was%20hacked%20and%20I%20need%20help', ws='unban', subj='Hacked%20Instagram%20account',
 answer='To recover a hacked Instagram account, use the undo link in Instagram’s email about the change, then go to instagram.com/hacked on a device you’ve used before and follow the prompts, including any video selfie. Unbanz helps you handle that appeal through Meta’s official process. Meta makes the final decision.',
 body=[
  sec('signs','Signs your account was hacked', ul([
    'An email from Instagram saying your email, phone number or password changed, and you didn’t do it.',
    'Your login stops working, or the account shows a different email.',
    'Posts, DMs or follows you didn’t make, or a changed username and bio.',
    'Login codes arriving that you didn’t request.'])),
  sec('first','What to do, in order', ol([
    'Find Instagram’s email about the change (check spam). If it offers a way to revert or secure the account, use it at once. It expires.',
    'Go to instagram.com/hacked on a phone or computer you’ve used to log in before, on your usual network.',
    'Choose the option that matches what you still have: the old email, the old number, or neither. Instagram can offer a video selfie where you turn your head in different directions.',
    'Once you’re back in, change the password, then remove any email or number you don’t recognise.',
    'Open Accounts Center, then Password and security, and log out of sessions you don’t know. Turn on two-factor authentication with an authenticator app rather than SMS if you can.'])),
  sec('email','Secure your email first','<p>The hacker usually got in through your email or a phishing page. If your email password is the same, or it’s also compromised, they can undo your recovery. Change the email password and turn on two-step verification there before you rely on Instagram’s codes. See also '+A('/hacker-changed-my-instagram-email-and-password/','when a hacker changed your email and password')+'.</p>'),
  sec('disabled','If the account is also disabled','<p>Hackers often post spam or scams, and that can get the account disabled. If you see a disabled notice, tell Instagram in the review that the account was compromised, and finish the selfie check. Details: '+A('/instagram-account-disabled-after-hack-appeal/','appealing a disabled account after a hack')+'.</p>'),
  sec('avoid','What not to do', ul([
    'Don’t pay a “hacker” or “recovery expert” who contacts you, or who asks for your password.',
    'Don’t click links in emails that claim to be from Instagram unless you can see they come from Instagram’s own domain.',
    'Don’t create a new account and abandon the old one before you’ve tried the official routes.'])),
  sec('help','How Unbanz helps','<p>We work out which route fits, put the details in order (old email and phone, dates, the notice, anything you remember about when it happened), and handle the appeal through Meta’s official process. If you have an active Meta Verified subscription, Instagram’s Help Center says you can also contact Meta Verified support from the app, where it’s available. Main page: '+A('/instagram-account-recovery/','Instagram account recovery')+'.</p>'),
  how(ACCT_STEP1),
  who(['People locked out after a phishing link, a fake login page or reused passwords.','Creators and businesses that can’t afford to lose the account.','Anyone whose email and phone were both changed.','Not for: accounts that were really used for scams or abuse.']),
 ],
 faq=[
  ('How do I recover a hacked Instagram account?','Use the undo link in Instagram’s email about the change if there is one, then go to instagram.com/hacked on a device you used before. Pick the option that matches what you still have, and complete any code or video selfie request.'),
  ('What if the hacker changed my email and phone number?','instagram.com/hacked still applies. Instagram can offer other ways to prove it’s you, including a video selfie. Send us what you have and we tell you which route fits.'),
  ('Why do I need to secure my email first?','If the hacker also controls your email, they can reset Instagram again. Change the email password and turn on two-step verification before you rely on Instagram’s codes.'),
  CAN_FAQ, PASSWORD_FAQ, CONTACT_FAQ],
 related=[('/instagram-account-recovery/','Instagram account recovery'),('/hacker-changed-my-instagram-email-and-password/','Hacker changed email and password'),('/instagram-account-disabled-after-hack-appeal/','Disabled after a hack'),('/guides/hacked-instagram-account-recovery/','Hacked Instagram guide'),('/instagram-appeal-denied/','Appeal denied'),('/unban-pricing/','Unban cost and timing'),('/services/','All services')],
 relq=[('/facebook-hacked-account-recovery-service/','Hacked Facebook recovery'),('/instagram-account-recovery-usa/','Recovery in the USA'),('/instagram-account-recovery-uk/','Recovery in the UK')])

# 6 hacked FB service
page(slug='facebook-hacked-account-recovery-service', lang='en',
 title='Hacked Facebook Account Recovery Service | Unbanz',
 desc='Facebook account hacked? The official recovery steps, how to protect Pages and ad accounts, and how Unbanz helps you appeal.',
 h1='Hacked Facebook account recovery service.', crumb='Hacked Facebook account recovery', svc='Hacked Facebook account recovery service',
 hero='Someone took over your Facebook profile, or locked you out of it? This page covers the official recovery routes, what to check on Pages and ad accounts, and how Unbanz helps.',
 wa='Hey%20Unbanz%2C%20my%20Facebook%20account%20was%20hacked%20and%20I%20need%20help', ws='unban', subj='Hacked%20Facebook%20account',
 answer='To recover a hacked Facebook account, open facebook.com/hacked or the “secure your account” link in Facebook’s email about the change, on a device and network you’ve used before. Then confirm it’s you, including any ID check. Unbanz helps you handle the appeal through Meta’s official process; Meta makes the final decision.',
 body=[
  sec('signs','Signs your Facebook account was hacked', ul([
    'An email or notification about a changed password, email or phone you didn’t change.',
    'Login stops working, or Facebook says the account is locked or disabled.',
    'Posts, messages, friend requests or Marketplace listings you didn’t make.',
    'Unknown admins on your Pages, or ad spend you don’t recognise.'])),
  sec('first','What to do, in order', ol([
    'Look in your email, including spam, for a message from Facebook about the change. Facebook’s security emails come from facebookmail.com. If it has a link to secure the account, use it.',
    'Go to facebook.com/hacked on a phone or computer you’ve logged in from before. You can also use “Find your account” on the login page.',
    'Confirm it’s you with the options offered. Facebook may ask you to upload ID or take a selfie. The old trusted contacts option has been discontinued.',
    'Once in, change the password, then open Accounts Center and Password and security. Log out of sessions you don’t know and remove unfamiliar email addresses and numbers.',
    'Turn on two-factor authentication, and check that your email account has a new password and two-step verification too.'])),
  sec('assets','Check Pages, ads and payment methods','<p>A hacked profile often takes Pages and ad accounts with it. Once you’re in, look at who has admin access on each Page and Business Portfolio and remove people you don’t know. Check ad accounts for ads you didn’t create and payment methods you didn’t add. If the ad account was restricted after the hack, see '+A('/ad-account-disabled-after-hack/','ad account disabled after a hack')+'.</p>'),
  sec('disabled','If Facebook disabled the account','<p>If you see a disabled or suspended notice instead, use its option to disagree with the decision and finish any ID check it asks for. See '+A('/facebook-account-recovery/','Facebook account recovery')+' and the guide to '+A('/guides/facebook-id-upload-request/','Facebook’s ID upload request')+'.</p>'),
  sec('avoid','What not to do', ul([
    'Don’t pay a “hacker” or “recovery expert” who contacts you.',
    'Don’t click “secure your account” links that don’t come from Facebook’s own domain.',
    'Don’t share your password or login codes with anyone, including us.'])),
  sec('help','How Unbanz helps','<p>We work out which route fits, get the details in order (old email and phone, dates, the notice, which Pages and ad accounts are linked), and handle the appeal through Meta’s official process. Main page: '+A('/facebook-account-recovery/','Facebook account recovery')+'.</p>'),
  how(ACCT_STEP1),
  who(['People locked out of a Facebook profile after a phishing link or a reused password.','Business owners whose Pages or ad accounts were taken over with the profile.','Anyone whose email and phone were both changed.','Not for: accounts that were really used for scams or abuse.']),
 ],
 faq=[
  ('How do I recover a hacked Facebook account?','Use the secure-your-account link in Facebook’s email about the change, or go to facebook.com/hacked on a device you’ve used before. Confirm it’s you with the options offered, including any ID check, then change the password and log out unknown sessions.'),
  ('What if the hacker changed my email and phone number?','facebook.com/hacked and the “Find your account” page still apply. Facebook can offer other ways to confirm it’s you, such as an ID or selfie check. Send us what you have and we tell you which route fits.'),
  ('Can a hacked Facebook account take my Pages and ads with it?','It can. If the hacker is an admin on your Pages or Business Portfolio, remove unknown admins once you’re back in, and check ads and payment methods you didn’t set up.'),
  ('Can Unbanz recover my Facebook account?','We help you submit a clean appeal through Meta’s official process and handle it end to end. Meta makes the final decision, so we tell you upfront whether we think it’s doable.'),
  ('Do I need to share my Facebook password?','No. Your password and login codes stay with you. Anyone who asks for them is not someone to work with.'),
  CONTACT_FAQ],
 related=[('/facebook-account-recovery/','Facebook account recovery'),('/guides/hacked-facebook-account-recovery/','Hacked Facebook guide'),('/ad-account-disabled-after-hack/','Ad account disabled after a hack'),('/facebook-account-disabled-appeal-help/','Facebook disabled appeal'),('/unban-pricing/','Unban cost and timing'),('/services/','All services')],
 relq=[('/instagram-hacked-account-recovery-service/','Hacked Instagram recovery'),('/guides/facebook-page-hacked-admin-removed/','Page hacked, admin removed')])

# 7 disabled after hack
page(slug='instagram-account-disabled-after-hack-appeal', lang='en',
 title='Instagram Account Disabled After a Hack: Appeal | Unbanz',
 desc='Instagram disabled your account after it was hacked? How to tell which route to take, what to include in the appeal, and how Unbanz helps.',
 h1='Instagram account disabled after a hack: how to appeal.', crumb='Instagram disabled after a hack', svc='Instagram account disabled after a hack appeal',
 hero='A hacker posted from your account and now Instagram has disabled it. Here is how to appeal through Instagram’s official process, and what to say so the review makes sense.',
 wa='Hey%20Unbanz%2C%20my%20Instagram%20account%20was%20disabled%20after%20a%20hack%20and%20I%20need%20help%20with%20the%20appeal', ws='unban', subj='Instagram%20disabled%20after%20hack',
 answer='If a hack got your Instagram disabled, first work out whether you can still see a disabled notice. If you can, request a review from it and finish the video selfie. If you can’t log in at all, start at instagram.com/hacked. Appeal once, and say plainly that the account was compromised.',
 body=[
  sec('which','Which route are you on?', ul([
    '<strong>You see a disabled or suspended notice when you log in:</strong> request a review from that notice.',
    '<strong>The email, number or password was changed and you can’t log in:</strong> start at instagram.com/hacked, and appeal if the flow leads you to a disabled notice.',
    '<strong>You’re not sure:</strong> try logging in with your old details on a device you’ve used before and see what appears.'])),
  sec('why','Why hacked accounts get disabled','<p>A hacker usually uses the account the way a scammer would: spam links, mass follows, giveaway scams, or impersonating you under a changed username. Instagram’s systems see that behaviour on your account and can disable it, even though you didn’t do it. That’s the point to make in the review.</p>'),
  sec('steps','Steps to appeal', ol([
    'Open the notice and tap the option to request a review or disagree with the decision.',
    'Complete every step it asks for. If it asks for a video selfie, record it in good light and turn your head as shown. If it isn’t accepted, you can try again.',
    'Tell Instagram the account was hacked, and when you noticed. Keep it short, specific and true.',
    'Use the email address on the account for follow-ups and check spam. Replies come there.',
    'Wait for the answer instead of sending repeat appeals. Several submissions can slow things down.'])),
  sec('include','What helps the review make sense', ul([
    'The date you noticed the hack, and any email from Instagram about a changed email, number or password.',
    'The email address and phone number that were on the account before the hack.',
    'Screenshots of the posts or messages you didn’t make.',
    'Confirmation that you changed your email password and turned on two-step verification.'])),
  sec('after','If it’s denied','<p>A denial isn’t always the end. Read '+A('/instagram-appeal-denied/','Instagram appeal denied')+' for the next steps, and see how a hacked account is handled in '+A('/instagram-hacked-account-recovery-service/','hacked Instagram account recovery')+'.</p>'),
  sec('help','How Unbanz helps','<p>We put the details in order, work out which route fits, and handle the appeal through Meta’s official process. Main page: '+A('/instagram-account-disabled-appeal/','Instagram disabled appeal')+'.</p>'),
  how(ACCT_STEP1),
  who(['People hacked and then disabled for what the hacker posted.','Creators and businesses relying on the account.','Anyone who already appealed once and got nowhere.','Not for: accounts that were really used for scams or abuse.']),
 ],
 faq=[
  ('Why did Instagram disable my account after it was hacked?','Because of what the hacker did with it: spam, scam posts, mass follows or impersonation. Instagram’s systems act on the behaviour, not on who was behind it. That’s why your appeal should say the account was compromised.'),
  ('Do I appeal first or recover the account first?','If you can still see a disabled notice, request a review from it. If the hacker changed your login and you can’t get in, start at instagram.com/hacked, then deal with any disabled notice that appears.'),
  ('What should I say in the appeal?','Say the account was hacked, when you noticed, and what you’ve done since: changed the email password and turned on two-step verification. Keep it short and true, and complete the video selfie if asked.'),
  ('Can I send the appeal more than once?','Send one complete appeal and wait. Repeat submissions can slow things down. If it’s denied, see the next steps in our appeal denied guide.'),
  ('Can Unbanz help with this?','Yes. We handle the appeal through Meta’s official process and Meta makes the final decision, so we tell you upfront whether we think it’s doable.'),
  CONTACT_FAQ],
 related=[('/instagram-account-disabled-appeal/','Instagram disabled appeal'),('/instagram-hacked-account-recovery-service/','Hacked Instagram recovery'),('/hacker-changed-my-instagram-email-and-password/','Hacker changed email and password'),('/instagram-appeal-denied/','Appeal denied'),('/guides/instagram-video-selfie-verification/','Video selfie verification'),('/unban-pricing/','Unban cost and timing')],
 relq=[('/instagram-appeal-form-not-working/','Appeal form not working'),('/instagram-account-recovery-usa/','Recovery in the USA')])

# 8 business disabled
page(slug='instagram-business-account-disabled-recovery', lang='en',
 title='Instagram Business Account Disabled: Recovery Steps | Unbanz',
 desc='Instagram business account disabled? The official appeal steps, what to check on your Page, Business Portfolio and ads, and how Unbanz helps.',
 h1='Instagram business account disabled: recovery steps.', crumb='Instagram business account disabled', svc='Instagram business account disabled recovery',
 hero='Your Instagram business account is disabled and customers can’t reach you. Here is the official appeal route, plus the business checks that matter: Page, Business Portfolio and ads.',
 wa='Hey%20Unbanz%2C%20my%20Instagram%20business%20account%20was%20disabled%20and%20I%20need%20help', ws='unban', subj='Instagram%20business%20account%20disabled',
 answer='A disabled Instagram business account is appealed like any other: log in, open the notice and request a review. Business accounts add checks, though: the connected Facebook Page, Business Portfolio and any ad account. Look at them together, appeal through Instagram’s official process, and expect Meta to make the final decision.',
 body=[
  sec('which','Is it disabled, or just restricted?', ul([
    '<strong>Disabled:</strong> you can’t use the account and see a notice. Request a review from the notice.',
    '<strong>Restricted features:</strong> you can log in but something is limited. Check Account Status in the app, which lists what’s affecting the account and lets you request another look where it’s offered.',
    '<strong>Ads only:</strong> the account works but ads are blocked. That’s an ad account issue. See '+A('/ad-account-recovery/','ad account recovery')+'.'])),
  sec('steps','Steps to appeal', ol([
    'Log in and tap the disabled notice. Choose to request a review and complete every step, including any ID or video selfie check.',
    'Use the email on the account for replies and check spam.',
    'Check the connected Facebook Page and Business Portfolio in Meta Business Suite and Account Quality for any linked restriction, so you know the full picture.',
    'While the appeal is open, avoid big changes such as switching account type or changing the username.',
    'Send one complete appeal rather than many.'])),
  sec('business','Business checks that help', ul([
    'The business name, website and product or service pages that show what you sell.',
    'Any business registration documents, for when you’re asked to show the business is real.',
    'A note of whether you use ads, a Shop or branded content, and who has admin access.',
    'The email and phone on the account, and any email you got from Instagram.'])),
  sec('meta','Meta Verified subscribers','<p>If you have an active Meta Verified subscription, Instagram’s Help Center says you can contact Meta Verified support from the app, where it’s available. It doesn’t replace the appeal, but it’s another route to use.</p>'),
  sec('help','How Unbanz helps','<p>We work out whether the problem sits on the Instagram account, the Page, the Business Portfolio or the ads, and handle the appeal through Meta’s official process. Main pages: '+A('/instagram-account-disabled-appeal/','Instagram disabled appeal')+' and '+A('/business-manager-disabled/','Business Manager disabled')+'.</p>'),
  how(ACCT_STEP1),
  who(['Shops, agencies and local businesses that take orders through Instagram.','Marketers whose Instagram and ad account are linked.','Anyone who already appealed once and got nowhere.','Not for: accounts that were really used for scams or abuse.']),
 ],
 faq=[
  ('How do I appeal a disabled Instagram business account?','Log in, tap the disabled notice, request a review, and complete every step including any ID or selfie check. Then wait for the reply to the email on the account.'),
  ('Does a disabled Instagram account affect my Facebook Page or ads?','Check them together. The Page, Business Portfolio and ad account can each carry their own restrictions, so look at Account Quality in Meta Business Suite as well as Instagram’s Account Status.'),
  ('Should I switch to a personal account while I appeal?','We’d avoid big changes such as switching account type or changing the username while the appeal is open. Send one complete appeal and wait for the answer.'),
  ('I have Meta Verified. Can I use that support?','If your subscription is active, Instagram’s Help Center says you can contact Meta Verified support from the app, where it’s available. It’s an extra route, not a replacement for the appeal.'),
  ('Can Unbanz help with a disabled business account?','Yes. We handle the appeal through Meta’s official process and Meta makes the final decision, so we tell you upfront whether we think it’s doable.'),
  CONTACT_FAQ],
 related=[('/instagram-account-disabled-appeal/','Instagram disabled appeal'),('/instagram-creator-account-disabled-recovery/','Creator account disabled'),('/business-manager-disabled/','Business Manager disabled'),('/ad-account-recovery/','Ad account recovery'),('/instagram-appeal-denied/','Appeal denied'),('/unban-pricing/','Unban cost and timing')],
 relq=[('/instagram-appeal-form-not-working/','Appeal form not working'),('/guides/instagram-business-vs-creator-account/','Business vs creator account')])

# 9 creator disabled
page(slug='instagram-creator-account-disabled-recovery', lang='en',
 title='Instagram Creator Account Disabled: Recovery Steps | Unbanz',
 desc='Instagram creator account disabled? Common reasons, the official appeal steps, and how Unbanz helps you appeal through the official process.',
 h1='Instagram creator account disabled: recovery steps.', crumb='Instagram creator account disabled', svc='Instagram creator account disabled recovery',
 hero='Your creator account is disabled and your audience can’t find you. Here is the official appeal route, the usual reasons creator accounts get flagged, and how Unbanz helps.',
 wa='Hey%20Unbanz%2C%20my%20Instagram%20creator%20account%20was%20disabled%20and%20I%20need%20help', ws='unban', subj='Instagram%20creator%20account%20disabled',
 answer='A disabled Instagram creator account is appealed from the notice itself: log in, tap it, request a review and complete any selfie check. Creator accounts are often flagged for impersonation reports, copyright claims, automation or bought engagement. Unbanz helps you appeal through Meta’s official process; Meta makes the final decision.',
 body=[
  sec('why','Common reasons creator accounts get disabled', ul([
    'Impersonation reports, for example a name or photo that looks like someone else’s.',
    'Repeated copyright or music removals.',
    'Automation, follow/unfollow tools or bought followers and engagement.',
    'Spam-like behaviour such as mass tagging, mass DMs or the same link everywhere.',
    'Strikes for content that broke the Community Guidelines. See '+A('/guides/instagram-community-guidelines-strikes/','Community Guidelines strikes')+'.'])),
  sec('steps','Steps to appeal', ol([
    'Log in and tap the disabled notice. Request a review and complete every step, including any ID or video selfie check.',
    'If you can still log in to a restricted account, open Account Status in the app to see what’s flagged and request another look where it’s offered.',
    'Use the email on the account for replies and check spam.',
    'Send one complete appeal. Repeat submissions can slow things down.',
    'If you get no appeal option, see '+A('/guides/instagram-disabled-no-appeal-button/','no appeal button')+'.'])),
  sec('protect','Protect your audience while you wait', ul([
    'Don’t create a duplicate account to get around the disable. Meta can disable accounts made to avoid a restriction.',
    'Tell people where else to find you, on your other platforms.',
    'Keep a list of your collaborators’ and brand contacts outside Instagram.'])),
  sec('meta','Meta Verified subscribers','<p>If you have an active Meta Verified subscription, Instagram’s Help Center says you can contact Meta Verified support from the app, where it’s available. It’s an extra route, not a replacement for the appeal.</p>'),
  sec('help','How Unbanz helps','<p>We work out why the account was flagged, put the details in order, and handle the appeal through Meta’s official process. Main page: '+A('/instagram-account-disabled-appeal/','Instagram disabled appeal')+'.</p>'),
  how(ACCT_STEP1),
  who(['Creators and influencers whose income depends on the account.','Agencies and managers who run creator accounts.','Anyone who already appealed once and got nowhere.','Not for: accounts that were really used for scams or abuse.']),
 ],
 faq=[
  ('Why was my Instagram creator account disabled?','Usually impersonation reports, repeated copyright removals, automation or bought engagement, spam-like behaviour or Community Guidelines strikes. The notice gives the stated reason, so screenshot it.'),
  ('How do I appeal a disabled creator account?','Log in, tap the disabled notice, request a review and complete every step, including any ID or video selfie check. Then wait for the reply to the email on the account.'),
  ('Should I make a new account while I wait?','We’d avoid it. Meta can disable accounts created to get around a restriction. Point followers to your other platforms and wait for the appeal.'),
  ('Does Meta Verified help with a disabled account?','If your subscription is active, Instagram’s Help Center says you can contact Meta Verified support from the app, where it’s available. It’s an extra route, not a replacement for the appeal.'),
  ('Can Unbanz help with a creator account?','Yes. We handle the appeal through Meta’s official process and Meta makes the final decision, so we tell you upfront whether we think it’s doable.'),
  CONTACT_FAQ],
 related=[('/instagram-account-disabled-appeal/','Instagram disabled appeal'),('/instagram-business-account-disabled-recovery/','Business account disabled'),('/guides/instagram-disabled-for-impersonation/','Disabled for impersonation'),('/instagram-appeal-denied/','Appeal denied'),('/unban-pricing/','Unban cost and timing'),('/services/','All services')],
 relq=[('/instagram-appeal-form-not-working/','Appeal form not working'),('/instagram-username-claim-for-influencers/','Username claims for influencers')])

# 10 appeal form not working
page(slug='instagram-appeal-form-not-working', lang='en',
 title='Instagram Appeal Form Not Working? What to Try | Unbanz',
 desc='Instagram appeal form not working, no button, or stuck in a loop? What to check, what to try, and what to do when nobody replies.',
 h1='Instagram appeal form not working? What to try.', crumb='Instagram appeal form not working', svc='Instagram appeal form not working help',
 hero='The appeal button is missing, the form won’t submit, or nothing happens after you send it. Here are the checks that fix most of it and what to do when they don’t.',
 wa='Hey%20Unbanz%2C%20my%20Instagram%20appeal%20is%20not%20working%20and%20I%20need%20help', ws='unban', subj='Instagram%20appeal%20not%20working',
 answer='For most disabled accounts there isn’t a separate appeal form: the review is in the notice you see when you log in. If it won’t load or submit, update the app, try instagram.com in a browser, drop any VPN, and use a device you’ve logged in from before. Send one complete appeal and wait.',
 body=[
  sec('what','What “the form” usually is','<p>For a disabled account, Instagram puts the review inside the login flow. You log in, tap the notice and request a review. There’s no separate public form to find and fill in, so a link from a random site is often a scam. If you can still log in, Account Status and Support Requests in the app show what’s been flagged and where a review is offered.</p>'),
  sec('fixes','Fixes to try, in order', ol([
    'Update the Instagram app, or reinstall it, then try again.',
    'Try the same login on instagram.com in a browser, or the reverse if the browser fails.',
    'Turn off any VPN and use your normal network.',
    'Use a phone or computer you’ve logged in from before, with the date and time set automatically.',
    'Use the email, username or phone exactly as they are on the account.',
    'Finish every step in the flow, including any code or video selfie. Skipping one can stop the request.'])),
  sec('stuck','If it still doesn’t work', ul([
    '<strong>No appeal button at all:</strong> see '+A('/guides/instagram-disabled-no-appeal-button/','no appeal button')+'.',
    '<strong>Selfie won’t be accepted:</strong> record again in good light with your face fully in frame. See '+A('/guides/instagram-video-selfie-verification/','video selfie verification')+'.',
    '<strong>Submitted, no reply:</strong> check spam for mail from Instagram and reply on that same thread if there is one. Instagram doesn’t publish a response time.',
    '<strong>Denied:</strong> see '+A('/instagram-appeal-denied/','Instagram appeal denied')+'.',
    '<strong>Meta Verified subscribers:</strong> Instagram’s Help Center says you can contact Meta Verified support from the app, where it’s available.'])),
  sec('avoid','What not to do', ul([
    'Don’t send the same appeal over and over. It can slow things down.',
    'Don’t pay anyone who says they can reach “Instagram staff” or open a hidden form.',
    'Don’t give your password or login codes to anyone, including us.'])),
  sec('help','How Unbanz helps','<p>We check what the notice actually says, work out which route fits, and handle the appeal through Meta’s official process. Main page: '+A('/instagram-account-disabled-appeal/','Instagram disabled appeal')+'.</p>'),
  how(ACCT_STEP1),
  who(['People who can’t find or submit an appeal.','Anyone who submitted and got no reply.','Anyone who already appealed once and got nowhere.','Not for: accounts that were really used for scams or abuse.']),
 ],
 faq=[
  ('Why is the Instagram appeal form not working?','Often it’s the app, the network or the device: an old app version, a VPN, or a device Instagram doesn’t recognise. Update the app, try instagram.com in a browser, and use a device you’ve logged in from before.'),
  ('Is there a separate Instagram appeal form?','For most disabled accounts, no. The review is part of the notice shown when you log in. Be wary of any outside link that claims to be a hidden appeal form.'),
  ('I appealed and nothing happened. What now?','Check the email on the account, including spam, and reply on that thread if there is one. Instagram doesn’t publish a response time, so send one complete appeal and wait rather than resubmitting.'),
  ('Why is there no appeal button on my account?','The notice can differ by account or decision, and some decisions don’t offer a review. Our no appeal button guide covers what to check next.'),
  ('Can Unbanz help if my appeal won’t go through?','Yes. We check what the notice says and handle the appeal through Meta’s official process. Meta makes the final decision, so we tell you upfront whether we think it’s doable.'),
  CONTACT_FAQ],
 related=[('/instagram-account-disabled-appeal/','Instagram disabled appeal'),('/instagram-appeal-denied/','Appeal denied'),('/guides/instagram-disabled-no-appeal-button/','No appeal button'),('/guides/instagram-video-selfie-verification/','Video selfie verification'),('/unban-pricing/','Unban cost and timing')],
 relq=[('/instagram-account-disabled-after-hack-appeal/','Disabled after a hack'),('/instagram-business-account-disabled-recovery/','Business account disabled')])

# 18 refund
page(slug='instagram-username-claim-refund', lang='en',
 title='Instagram Username Claim: 100% Refund if It Fails | Unbanz',
 desc='If your Instagram username claim with Unbanz fails, you get a full 100% refund. What counts as a failed claim and what the policy covers.',
 h1='Instagram username claim: 100% refund if it fails.', crumb='Instagram username claim refund', svc='Instagram username claim refund policy',
 hero='Claiming a username through Unbanz comes with a clear refund policy: if the claim fails, you get all your money back. Here is what that means in plain terms.',
 wa=WA_USER, ws='username', subj='Username%20claim',
 answer='If your Instagram username claim with Unbanz fails, you get a full 100% refund. A claim fails when the username isn’t successfully claimed onto your profile. The policy covers username claims only. Instagram makes the final decision on every claim, and you hear upfront whether the handle looks doable.',
 body=[
  sec('policy','What the policy says','<p>If a username claim fails, you get a full 100% refund. That’s the whole rule: if the username isn’t claimed onto your profile, you get all of your money back. The full wording is on our '+A('/refund-policy/','refund policy')+' page.</p>'),
  sec('fails','What counts as a failed claim','<p>A claim fails when the username isn’t successfully claimed onto your profile. If the handle ends up on your own Instagram profile, the claim worked. If it doesn’t, it failed and you get the refund.</p>'),
  sec('covers','What it covers, and what it doesn’t', ul([
    '<strong>Covered:</strong> username claims, meaning inactive, taken or OG handles claimed onto your own profile.',
    '<strong>Not covered by this page:</strong> other services such as unbans or account recovery. For those, price and any refund terms are agreed with you before we start.'])),
  sec('route','How a claim works','<p>Instagram has no “inactive” button and doesn’t sell usernames. Every claim goes through the platform’s own processes, matched to the handle: Meta’s intellectual property report if it matches your registered trademark, the impersonation report if the account pretends to be you or your brand, account recovery if the handle used to be yours, and the platform’s own processes for abandoned or squatted handles. We tell you which route fits and the price first. Instagram makes the final decision.</p>'),
  sec('never','What we never do', ul([
    'Buy, sell or take over accounts. The handle goes onto your own profile.',
    'File false or mass reports to free up a name.',
    'Ask for your password or login codes.'])),
  sec('ask','If something isn’t right','<p>Email team@unbanz.com with your WhatsApp number or email thread, and we’ll sort it under the refund policy. See also '+A('/username-claim-pricing/','username claim pricing')+' and '+A('/is-a-username-claim-safe/','is a username claim safe?')+'</p>'),
  how(USER_STEP1, True),
  who(['Creators and brands who want a clean, matching handle.','People whose name sits on a dead or squatting account.','Not for: handles held by active, unrelated people.']),
 ],
 faq=[
  ('Do I get a refund if my Instagram username claim fails?','Yes. If a username claim fails you get a full 100% refund. A claim fails when the username isn’t successfully claimed onto your profile.'),
  ('Is the refund full or partial?','Full. It’s 100% of your money back if the username isn’t claimed onto your profile.'),
  ('Does the refund apply to unbans and recovery too?','No. The 100% refund covers username claims.'),
  ('How do I ask for the refund?','Email team@unbanz.com with your WhatsApp number or email thread, or message us in the chat you already have. The refund policy page has the wording.'),
  ('Who decides whether a username claim succeeds?','Instagram does. We pick the right official route and file it properly, and tell you upfront if the handle looks doable.'),
  ('Do you buy usernames from other people?','No. Buying or selling usernames breaks Instagram’s Terms of Use. The handle goes onto your own profile through official routes.')],
 related=[('/refund-policy/','Refund policy'),('/instagram-username-claim/','Instagram username claims'),('/username-claim-pricing/','Username claim pricing'),('/is-a-username-claim-safe/','Is a username claim safe?'),('/username/','All username claims'),('/inactive-instagram-username/','Inactive usernames'),('/taken-instagram-username/','Taken usernames')],
 relq=[('/instagram-username-claim-for-influencers/','Claims for influencers'),('/instagram-username-claim-for-founders-and-startups/','Claims for founders and startups')])

# 19 influencers
page(slug='instagram-username-claim-for-influencers', lang='en',
 title='Instagram Username Claim for Influencers | Unbanz',
 desc='Stuck on an underscore handle? How influencers can claim an inactive or taken Instagram username through official routes, with a refund if it fails.',
 h1='Instagram username claim for influencers.', crumb='Username claim for influencers', svc='Instagram username claim for influencers',
 hero='Your name is your brand, and someone else is sitting on the clean handle. Here is how influencers and creators can go after it through Instagram’s official routes.',
 wa=WA_USER, ws='username', subj='Username%20claim',
 answer='Influencers can claim an Instagram username only through Instagram’s official routes: an inactive or abandoned account, an impersonator, a registered trademark, or recovering a handle that was yours. Buying handles breaks Instagram’s terms. Unbanz sends the claim through those routes, and you get a 100% refund if the claim fails.',
 body=[
  sec('routes','Routes that can work', ul([
    '<strong>Inactive or abandoned account:</strong> no posts, no photo, no activity for a long time. There’s no “inactive” button, so the claim goes through the platform’s own processes.',
    '<strong>Squatter:</strong> someone holding your name to sell it back to you. Paying them breaks Instagram’s terms.',
    '<strong>Impersonation:</strong> an account posing as you. Instagram’s impersonation report applies.',
    '<strong>Trademark:</strong> if your creator brand is a registered trademark, Meta’s intellectual property report applies. See '+A('/trademark-username-claim/','trademark username claims')+'.',
    '<strong>Used to be yours:</strong> if you lost the handle in a hack or by mistake, recovery usually brings it back.'])),
  sec('not','What usually doesn’t work', ul([
    'The handle belongs to a real, active person who just shares your name.',
    'It’s a common word or first name you have no special rights to.',
    'Anyone offering to sell you the handle, which breaks Instagram’s terms and is a common scam.'])),
  sec('before','Before you claim', ul([
    'Pick a clean backup now, close to your name and easy to say: no stacked underscores or numbers.',
    'Use the same handle on your other platforms so followers can find you everywhere.',
    'Keep your content and followers on your current account. A claim puts the handle onto your own profile.'])),
  sec('help','How Unbanz helps','<p>We check the handle, tell you which route fits and the price, then file it through the platform’s own process. The handle goes onto your own profile. Main page: '+A('/username/','username claims')+'. If the claim fails, you get a 100% refund. See the '+A('/instagram-username-claim-refund/','refund policy for username claims')+'.</p>'),
  how(USER_STEP1, True),
  who(['Influencers and creators on @name_official or @thename.co.','Managers and agencies handling handles for talent.','Not for: handles held by active, unrelated people.']),
 ],
 faq=[
  ('Can an influencer claim an Instagram username?','Yes, through Instagram’s official routes: an inactive or abandoned account, an impersonator, a registered trademark, or a handle that used to be yours. Send us the handle and you hear upfront which route fits and whether it looks doable.'),
  ('Can I buy an Instagram username?','No. Buying or selling usernames breaks Instagram’s Terms of Use, and bought handles are often recovered by the original owner. Unbanz doesn’t buy or sell accounts.'),
  ('Will I lose my followers when I claim a handle?','No. You keep your account and followers. The claimed handle goes onto your own profile.'),
  ('What if the username claim fails?','You get a full 100% refund. A claim fails when the username isn’t successfully claimed onto your profile.'),
  ('Do I need to share my Instagram password?','No. Your password and login codes stay with you.'),
  ('Who decides whether the claim succeeds?','Instagram does. We pick the right official route and file it properly.')],
 related=[('/username/','All username claims'),('/instagram-username-claim/','Instagram username claims'),('/inactive-instagram-username/','Inactive usernames'),('/taken-instagram-username/','Taken usernames'),('/og-username/','OG usernames'),('/instagram-username-claim-refund/','Username claim refund'),('/username-claim-pricing/','Username claim pricing')],
 relq=[('/instagram-username-claim-for-founders-and-startups/','Claims for founders and startups'),('/instagram-creator-account-disabled-recovery/','Creator account disabled')])

# 20 founders
page(slug='instagram-username-claim-for-founders-and-startups', lang='en',
 title='Instagram Username Claim for Founders and Startups | Unbanz',
 desc='Launching a brand and the Instagram handle is taken? Official routes for founders and startups, including trademark, with a refund if the claim fails.',
 h1='Instagram username claim for founders and startups.', crumb='Username claim for founders and startups', svc='Instagram username claim for founders and startups',
 hero='You have the domain and the company, but the Instagram handle is held by someone else. Here is how founders can go after it through Instagram’s official routes.',
 wa=WA_USER, ws='username', subj='Username%20claim',
 answer='Founders can’t buy an Instagram handle, but there are official routes: an inactive or abandoned account, an impersonator of your brand, or a registered trademark that matches the name. Company registration alone doesn’t give you a right to a handle. Unbanz sends the claim through those routes, and you get a 100% refund if it fails.',
 body=[
  sec('routes','Routes that can work', ul([
    '<strong>Trademark:</strong> a registered trademark that matches the handle is the strongest route, through Meta’s intellectual property report. Have the registration number and office ready (USPTO, UKIPO, EUIPO, CIPO, IP Australia). See '+A('/trademark-username-claim/','trademark username claims')+'.',
    '<strong>Inactive or abandoned account:</strong> no posts, no photo, no activity for a long time. There’s no “inactive” button, so the claim goes through the platform’s own processes.',
    '<strong>Impersonation:</strong> an account posing as your business. Instagram’s impersonation report applies.',
    '<strong>Squatter:</strong> an account holding your name to sell it back. Paying them breaks Instagram’s terms.'])),
  sec('not','What usually doesn’t work', ul([
    'A company registration or domain on its own. It doesn’t give you a right to a handle.',
    'The handle is an active account run by someone unrelated.',
    'A trademark that covers a different industry, with no confusion between the two.'])),
  sec('plan','Plan it before you launch', ul([
    'Check the handle on Instagram before you commit to a brand name or print anything.',
    'Create your account early, even before launch, so a clean handle doesn’t go to someone else.',
    'Choose a backup: yourbrandhq, getyourbrand, yourbrand.co. Avoid stacked underscores and numbers.',
    'Think about a trademark early. It’s the clearest way to show a brand name is yours, and it helps across platforms.'])),
  sec('help','How Unbanz helps','<p>We check the handle, tell you which route fits and the price, then file it through the platform’s own process. The handle goes onto your own profile. Main page: '+A('/business-username-claim/','brand and business usernames')+'. If the claim fails, you get a 100% refund. See the '+A('/instagram-username-claim-refund/','refund policy for username claims')+'.</p>'),
  how(USER_STEP1, True),
  who(['Founders and early teams launching a brand or product.','Startups that have a trademark and want the matching handle.','Agencies handling handles for several clients.','Not for: handles held by active, unrelated people.']),
 ],
 faq=[
  ('Can a startup claim an Instagram username?','Yes, through Instagram’s official routes: an inactive or abandoned account, an impersonator, or a registered trademark that matches the handle. Send the handle and you hear upfront which route fits and whether it looks doable.'),
  ('Does registering my company give me the Instagram handle?','No. Company registration alone doesn’t give you a right to a handle. A registered trademark that matches the name is the strongest route.'),
  ('Can I buy the handle from the current owner?','No. Buying or selling usernames breaks Instagram’s Terms of Use and often ends with the account recovered or disabled. Unbanz doesn’t buy or sell accounts.'),
  ('What if the username claim fails?','You get a full 100% refund. A claim fails when the username isn’t successfully claimed onto your profile.'),
  ('Do I need to share my Instagram password?','No. Your password and login codes stay with you.'),
  ('Who decides whether the claim succeeds?','Instagram does. We pick the right official route and file it properly.')],
 related=[('/business-username-claim/','Brand and business usernames'),('/trademark-username-claim/','Trademark username claims'),('/username/','All username claims'),('/instagram-username-claim/','Instagram username claims'),('/instagram-username-claim-refund/','Username claim refund'),('/how-much-does-it-cost-to-claim-an-instagram-username/','Username claim cost'),('/username-claim-pricing/','Username claim pricing')],
 relq=[('/instagram-username-claim-for-influencers/','Claims for influencers'),('/og-username/','OG usernames')])
