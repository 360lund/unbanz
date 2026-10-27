# -*- coding: utf-8 -*-
"""Country pages added 2026-10-27 (rendered by build_oct27_pages.py via build_oct25_pages.build)."""
DATE = "2026-10-27"

def A(href, label):
    return '<a href="%s">%s</a>' % (href, label)
def sec(id_, h2, body):
    return '<h2 id="%s">%s</h2>%s' % (id_, h2, body)
def ul(items): return '<ul>%s</ul>' % ''.join('<li>%s</li>' % i for i in items)
def ol(items): return '<ol>%s</ol>' % ''.join('<li>%s</li>' % i for i in items)

def how(plat):
    return ('<h2 id="how">How it works with Unbanz</h2><ol>'
            '<li>Message us on WhatsApp or email with the %s name or profile link, the email or phone on the account, and a screenshot of the notice.</li>'
            '<li>We tell you honestly whether we can help and what it would cost.</li>'
            '<li>We prepare everything and handle the appeal through the platform’s official process.</li>'
            '<li>We keep you posted until there’s a result. Meta makes the final decision.</li></ol>') % plat

def who(items):
    return '<h2 id="who">Who this is for</h2><ul>%s</ul>' % ''.join('<li>%s</li>' % i for i in items)

PASSWORD_IG = ('Do I need to share my Instagram password?', 'No. Your password and login codes stay with you. Anyone who asks for them is not someone to work with.')
PASSWORD_FB = ('Do I need to share my Facebook password?', 'No. Your password and login codes stay with you. Anyone who asks for them is not someone to work with.')
CONTACT_FAQ = ('How do I contact Unbanz?', 'WhatsApp +1 934 201 2490 or team@unbanz.com.')
CAN_FAQ = ('Can Unbanz recover my account?', 'We help you submit a clean appeal through Meta’s official process and handle it end to end. Meta makes the final decision, so we tell you upfront whether we think it’s doable.')
IG_WA = 'Hey%20Unbanz%2C%20I%20need%20help%20recovering%20my%20Instagram%20account'
FB_WA = 'Hey%20Unbanz%2C%20I%20need%20help%20recovering%20my%20Facebook%20account'

IG_REL = [('/instagram-account-recovery/','Instagram account recovery'),('/instagram-account-disabled-appeal/','Instagram disabled appeal'),('/instagram-hacked-account-recovery-service/','Hacked Instagram recovery'),('/hacker-changed-my-instagram-email-and-password/','Hacker changed email and password'),('/instagram-appeal-denied/','Appeal denied'),('/guides/instagram-appeal-sent-no-response/','Appeal sent, no response'),('/unban-pricing/','Unban cost and timing'),('/services/','All services')]
FB_REL = [('/facebook-account-recovery/','Facebook account recovery'),('/facebook-account-disabled-appeal-help/','Facebook disabled appeal help'),('/facebook-account-suspended-180-days/','Suspended, 180 days to appeal'),('/facebook-hacked-account-recovery-service/','Hacked Facebook recovery'),('/guides/hacker-changed-facebook-email-and-password/','Hacker changed email and password'),('/guides/facebook-disabled-appeal-rejected/','Facebook appeal rejected'),('/unban-pricing/','Unban cost and timing'),('/services/','All services')]

PAGES = []

def ig_hf(place):
    return ('How do I recover a hacked Instagram account in %s?' % place,
            'Use the undo link in Instagram’s email about the change if there is one, then go to instagram.com/hacked on a device you used before and follow the steps. Instagram may ask for a code or a video selfie. If you see a disabled notice, request a review once.')
def fb_hf(place):
    return ('How do I recover a hacked Facebook account in %s?' % place,
            'Go to facebook.com/hacked on a device and browser you have used before, or search for your account at facebook.com/login/identify and choose the option for no longer having access. Check the email on the account first for a message from Facebook with a link to undo a change.')

def country(slug, cc, plat, title, desc, h1, crumb, hero, answer, first, local_h, local, extra, who_items, faq, related, relq):
    fb = plat == 'Facebook'
    PAGES.append(dict(
     slug=slug, lang='en-US' if cc == 'us' else 'en', title=title, desc=desc, h1=h1, crumb=crumb, svc=crumb,
     hero=hero, wa=FB_WA if fb else IG_WA, ws='unban', subj='%s%%20account%%20recovery' % plat, answer=answer,
     body=[
      sec('first', 'Official steps that come first', ol(first)),
      sec('local', local_h, ul(local)) + extra,
      sec('avoid', 'What not to do', ul([
        'Don’t pay or message anyone from a DM who says they can “open” your account.',
        'Don’t share your password or login codes with anyone, including us.',
        'Don’t create new accounts to plead with %s, and don’t send the same appeal over and over.' % plat])),
      sec('help', 'How Unbanz helps', '<p>We work out whether the account is disabled, hacked or both, gather the notice, the old email and phone and the dates, and handle the appeal through Meta’s official process. Main page: ' +
          (A('/facebook-account-recovery/', 'Facebook account recovery') if fb else A('/instagram-account-recovery/', 'Instagram account recovery')) + '.</p>'),
      how(plat),
      who(who_items),
     ],
     faq=faq + [PASSWORD_FB if fb else PASSWORD_IG, CONTACT_FAQ], related=related, relq=relq))

# ---------------------------------------------------------------- Bangladesh, Instagram
country('instagram-account-recovery-bangladesh', 'bd', 'Instagram',
 'Instagram Account Recovery in Bangladesh | Unbanz',
 'Hacked or disabled Instagram account in Bangladesh? Official recovery steps, where to report it locally, and how Unbanz helps with a clean appeal.',
 'Instagram account recovery in Bangladesh.', 'Instagram account recovery Bangladesh',
 'Instagram account hacked or disabled and you’re in Bangladesh? Here are the official steps first, the local reporting options, and how Unbanz helps you appeal through Meta’s official process.',
 'Instagram account recovery in Bangladesh starts with Instagram’s own routes: request a review on a disabled notice, or use instagram.com/hacked if someone took over the account. Report blackmail or fraud locally as well. Unbanz helps you submit a clean appeal through Meta’s official process; Meta makes the final decision.',
 ['If you see a disabled or suspended notice, tap it and request a review. Finish every step it asks for, including any selfie check.',
  'If the email, number or password was changed, go to instagram.com/hacked on a phone or computer you have logged in from before, on your usual network.',
  'Search your inbox and spam for an email from Instagram about the change. If it has a link to undo the change, use it straight away.',
  'If Instagram asks for a video selfie, record it in good light and turn your head as shown. If it isn’t accepted, you can try again.',
  'Send one complete appeal and then watch the email on the account for the reply.'],
 'Checks that matter in Bangladesh',
 ['<strong>Your +880 number:</strong> text codes go to the number on the account. If you lost the SIM, your operator can issue a replacement, usually after you re-verify with your NID. Do that before you try recovery, or the codes go nowhere.',
  '<strong>Phishing is the usual way in:</strong> messages saying your page will be deleted for “copyright violation”, offers of a blue badge, free-follower sites, and job or giveaway links. Never type your login into a page you reached from a message.',
  '<strong>Blackmail or fraud:</strong> do not pay. Save screenshots and links, then report to Bangladesh Police. The Cyber Police Center (CID) runs a cyber support hotline on 01320-010148 and a complaint portal at cpccid.org, and 999 is the national emergency number. Women can also use Police Cyber Support for Women on 01320-000888.',
  '<strong>Shops and online sellers:</strong> if the account sells products, keep your shop name, product photos and any trade licence to hand. They help you show the account is a real business if you are asked.',
  '<strong>Language:</strong> the notice may show in Bangla or English and the review options are the same. Screenshot it as it appears. We work over WhatsApp or email in English.'],
 '<p>Not sure which problem you have? ' + A('/instagram-account-disabled-appeal/', 'Disabled or suspended') + ', ' + A('/instagram-hacked-account-recovery-service/', 'hacked') + ' and ' + A('/instagram-account-disabled-after-hack-appeal/', 'hacked, then disabled') + ' each have their own steps. If someone is threatening you with private photos, read ' + A('/guides/sextortion-what-to-do-on-instagram/', 'what to do about sextortion on Instagram') + '.</p>',
 ['Bangladeshi creators, online shops and agencies who run their work through Instagram.', 'People hacked through a phishing link or a fake badge offer.', 'Anyone who already appealed once and got nowhere.', 'Not for: accounts that were really used for scams or abuse.'],
 [ig_hf('Bangladesh'),
  ('Where do I report a hacked Instagram account in Bangladesh?', 'To Instagram first, through instagram.com/hacked. If there was fraud, blackmail or stolen money, also report it to Bangladesh Police, for example through the Cyber Police Center portal at cpccid.org or the national emergency number 999. Tell your bank or mobile wallet provider at once if money moved.'),
  ('What if my number was changed or I lost my SIM?', 'Get the SIM replaced with your operator first, then use instagram.com/hacked. Instagram offers other ways to prove it is you, such as a video selfie. Send us what you have and we tell you which route fits.'),
  CAN_FAQ],
 IG_REL,
 [('/instagram-account-recovery-india/', 'Recovery in India'), ('/instagram-account-recovery-pakistan/', 'Recovery in Pakistan'), ('/facebook-account-recovery-bangladesh/', 'Facebook recovery in Bangladesh')])

# ---------------------------------------------------------------- Pakistan, Instagram
country('instagram-account-recovery-pakistan', 'pk', 'Instagram',
 'Instagram Account Recovery in Pakistan | Unbanz',
 'Hacked or disabled Instagram account in Pakistan? Official recovery steps, NCCIA reporting, and how Unbanz helps with a clean appeal.',
 'Instagram account recovery in Pakistan.', 'Instagram account recovery Pakistan',
 'Instagram account hacked or disabled and you’re in Pakistan? Here are the official steps first, how to report it to the NCCIA, and how Unbanz helps you appeal through Meta’s official process.',
 'Instagram account recovery in Pakistan uses the same official routes as everywhere: request a review on a disabled notice, or use instagram.com/hacked if someone took over the account. Report blackmail or fraud to the NCCIA on 1799. Unbanz helps you submit a clean appeal through Meta’s official process; Meta makes the final decision.',
 ['If you see a disabled or suspended notice, tap it and request a review. Complete every step, including any selfie check.',
  'If the email, number or password was changed, go to instagram.com/hacked on a device and network you have used before. Avoid a VPN or a new location while you do it.',
  'Check your email, including spam, for a message from Instagram about the change and use its undo link if it is still valid.',
  'Follow any code or video selfie request exactly as shown, then wait for the reply to the email on the account.'],
 'Checks that matter in Pakistan',
 ['<strong>Your +92 number:</strong> text codes go to your number. If you lost the SIM, a replacement needs biometric verification against your CNIC with your operator. Sort that out first or the codes will go nowhere.',
  '<strong>Phishing is the usual way in:</strong> fake “your account will be removed” messages, verification-badge offers, and links that claim to show who viewed your profile. Never enter your login on a page you reached from a message.',
  '<strong>Blackmail, fraud or a fake profile:</strong> the National Cyber Crime Investigation Agency (NCCIA) takes complaints on its 24/7 helpline, 1799, and at complaint.nccia.gov.pk. Older pages may still say FIA. If you are in physical danger, call 15 first.',
  '<strong>Sellers and brands:</strong> if the account sells through Instagram, keep your business name, product photos and any registration details to hand if you are asked to show it is a real business.',
  '<strong>Everything in English:</strong> we work over WhatsApp or email in English. You send the notice as it appears on your screen.'],
 '<p>Not sure which problem you have? ' + A('/instagram-account-disabled-appeal/', 'Disabled or suspended') + ', ' + A('/instagram-hacked-account-recovery-service/', 'hacked') + ' and ' + A('/instagram-account-disabled-after-hack-appeal/', 'hacked, then disabled') + ' each have their own steps.</p>',
 ['Pakistani creators, online sellers and agencies who run their work through Instagram.', 'People hacked through a phishing link or a fake badge offer.', 'Anyone who already appealed once and got nowhere.', 'Not for: accounts that were really used for scams or abuse.'],
 [ig_hf('Pakistan'),
  ('Where do I report a hacked Instagram account in Pakistan?', 'To Instagram first, through instagram.com/hacked. If there was fraud, blackmail or a fake profile using your photos, also file a complaint with the NCCIA at complaint.nccia.gov.pk or on 1799. Tell your bank or wallet provider straight away if money moved.'),
  ('What if the hacker changed my email and phone number?', 'instagram.com/hacked still applies. Instagram can offer other ways to prove it is you, such as a video selfie. Send us what you have and we tell you which route fits.'),
  CAN_FAQ],
 IG_REL,
 [('/instagram-account-recovery-india/', 'Recovery in India'), ('/instagram-account-recovery-bangladesh/', 'Recovery in Bangladesh'), ('/instagram-account-recovery-uae/', 'Recovery in the UAE')])

# ---------------------------------------------------------------- Nigeria, Instagram
country('instagram-account-recovery-nigeria', 'ng', 'Instagram',
 'Instagram Account Recovery in Nigeria | Unbanz',
 'Hacked or disabled Instagram account in Nigeria? Official recovery steps, where to report it locally, and how Unbanz helps with a clean appeal.',
 'Instagram account recovery in Nigeria.', 'Instagram account recovery Nigeria',
 'Instagram account hacked or disabled and you’re in Nigeria? Here are the official steps first, where to report fraud, and how Unbanz helps you appeal through Meta’s official process.',
 'Instagram account recovery in Nigeria follows Instagram’s own routes: request a review on a disabled notice, or use instagram.com/hacked if someone took over the account. If money or blackmail is involved, report it locally too. Unbanz helps you submit a clean appeal through Meta’s official process; Meta makes the final decision.',
 ['If you see a disabled or suspended notice, tap it and request a review. Finish every step, including any selfie check.',
  'If the email, number or password was changed, go to instagram.com/hacked on a device and network you have used before.',
  'Check your email, including spam, for a message from Instagram about the change and use its undo link if it still works.',
  'If Instagram asks for a video selfie, record it in good light and turn your head as shown. Then wait for the reply to the email on the account instead of sending repeat appeals.'],
 'Checks that matter in Nigeria',
 ['<strong>Your +234 number:</strong> text codes go to the number on the account. SIMs are linked to a NIN, so a replacement SIM is issued through your network’s service centre with your NIN. Do that first or the codes go nowhere. If the SIM was swapped without you, tell your bank too.',
  '<strong>Phishing is the usual way in:</strong> fake “verification badge”, grant and giveaway messages, and links sent from a friend’s hacked account. Never enter your login on a page you reached from a message.',
  '<strong>Blackmail or fraud:</strong> do not pay. Save screenshots and links, then report through the Nigeria Police Force National Cybercrime Centre e-reporting portal at nccc.npf.gov.ng/ereport/. Financial fraud can also be reported to the EFCC. The old incb.npf.gov.ng address has been replaced.',
  '<strong>Brands and online sellers:</strong> if the account sells products, keep your business name, CAC registration if you have one, and product photos to hand if you are asked to show the business is real.',
  '<strong>Everything in English:</strong> we work over WhatsApp or email in English. You send the notice as it appears on your screen.'],
 '<p>Not sure which problem you have? ' + A('/instagram-account-disabled-appeal/', 'Disabled or suspended') + ', ' + A('/instagram-hacked-account-recovery-service/', 'hacked') + ' and ' + A('/instagram-account-disabled-after-hack-appeal/', 'hacked, then disabled') + ' each have their own steps. If someone is threatening you with private photos, read ' + A('/guides/sextortion-what-to-do-on-instagram/', 'what to do about sextortion on Instagram') + '.</p>',
 ['Nigerian creators, online shops and agencies who run their work through Instagram.', 'People hacked through a phishing link or a fake badge offer.', 'Anyone who already appealed once and got nowhere.', 'Not for: accounts that were really used for scams or abuse.'],
 [ig_hf('Nigeria'),
  ('Where do I report a hacked Instagram account in Nigeria?', 'To Instagram first, through instagram.com/hacked. If there was fraud, blackmail or stolen money, also report it through the Nigeria Police Force National Cybercrime Centre e-reporting portal, and tell your bank at once if money moved.'),
  ('What if I lost my SIM or the number on the account?', 'Get the SIM replaced through your network with your NIN, then use instagram.com/hacked. Instagram offers other ways to prove it is you, such as a video selfie. Send us what you have and we tell you which route fits.'),
  CAN_FAQ],
 IG_REL,
 [('/instagram-account-recovery-usa/', 'Recovery in the USA'), ('/instagram-account-recovery-uk/', 'Recovery in the UK'), ('/instagram-account-recovery-india/', 'Recovery in India')])

# ---------------------------------------------------------------- India, Facebook
country('facebook-account-recovery-india', 'in', 'Facebook',
 'Facebook Account Recovery in India: Official Help | Unbanz',
 'Hacked or disabled Facebook account in India? Official steps, the India grievance route, and how Unbanz helps with a clean appeal in English.',
 'Facebook account recovery in India.', 'Facebook account recovery India',
 'Facebook account hacked, suspended or disabled and you’re in India? Here are the official steps, the extra India-specific route, and how Unbanz helps you appeal through Meta’s official process.',
 'In India, Facebook account recovery follows Facebook’s own routes: Disagree with decision on a suspension notice within 180 days, or facebook.com/hacked for a hijacked account. India also has a separate grievance route under the IT Rules. Unbanz helps you submit a clean appeal through Meta’s official process; Meta makes the final decision.',
 ['If you see a suspended or disabled notice, log in and follow the prompts to disagree with the decision. Facebook gives most suspended accounts 180 days, but trust the date on your own screen.',
  'If you can’t log in because the email, number or password was changed, go to facebook.com/hacked on a device you have used before.',
  'You can also search for your account at facebook.com/login/identify and choose the option for no longer having access to your email or phone.',
  'Check your email, including spam, for a message from Facebook about the change. If it has a link to undo it, use it first.',
  'If Facebook asks for ID or a video selfie, use your real details and follow the instructions exactly.'],
 'What is different in India',
 ['<strong>Codes go to your number:</strong> text codes go to your +91 number. If you lost the SIM or changed operator, sort that out first or the codes will go nowhere.',
  '<strong>Pages and ads:</strong> if the profile is disabled, any Page where you are the only admin can be lost, and ad accounts tied to the profile can stop working. Ask someone you trust to confirm they have full control of the Page.',
  '<strong>Phishing is the usual way in:</strong> fake “policy violation” warnings, “blue tick” offers, and DM links claiming to show who viewed your profile. Never enter your login on a page you reached from a message.',
  '<strong>If money or blackmail is involved:</strong> the National Cyber Crime Reporting Portal (cybercrime.gov.in) takes reports, and 1930 is the helpline for financial cyber fraud.',
  '<strong>Everything in English:</strong> we work over WhatsApp or email in English. You send the notice as it appears on your screen.'],
 '<h2 id="gac">The India grievance route</h2><p>This is separate from Facebook’s own appeal. India’s IT Rules, 2021 set up a grievance process for users of social platforms. If you complained to the platform’s Grievance Officer and are unhappy with the response, you can appeal to the Grievance Appellate Committee at gac.gov.in within 30 days of that response. It is a formal route with its own limits, not a shortcut, so use Facebook’s own appeal first and read the portal’s guidance before you file.</p>',
 ['Indian creators, shops, Page owners and agencies who run their work through Facebook.', 'People hacked through a phishing link or a fake badge offer.', 'Anyone who already appealed once and got nowhere.', 'Not for: accounts that were really used for scams or abuse.'],
 [fb_hf('India'),
  ('What happens if I miss the 180 days on a Facebook suspension?', 'Facebook says the account is then permanently disabled and you cannot request another review. The time to appeal can vary by region, so check the date on your own notice and act early.'),
  ('Can I complain to the Grievance Appellate Committee about my Facebook account?', 'Yes, but only after the platform’s Grievance Officer has responded to your complaint. You then have 30 days from that response to appeal at gac.gov.in. It sits alongside Facebook’s own appeal and isn’t certain to restore an account.'),
  CAN_FAQ],
 FB_REL,
 [('/instagram-account-recovery-india/', 'Instagram recovery in India'), ('/facebook-account-recovery-bangladesh/', 'Facebook recovery in Bangladesh'), ('/instagram-account-recovery-pakistan/', 'Recovery in Pakistan')])

# ---------------------------------------------------------------- Bangladesh, Facebook
country('facebook-account-recovery-bangladesh', 'bd', 'Facebook',
 'Facebook Account Recovery in Bangladesh | Unbanz',
 'Hacked or disabled Facebook account in Bangladesh? Official recovery steps, where to report it locally, and how Unbanz helps with a clean appeal.',
 'Facebook account recovery in Bangladesh.', 'Facebook account recovery Bangladesh',
 'Facebook account hacked, suspended or disabled and you’re in Bangladesh? Here are the official steps first, the local reporting options, and how Unbanz helps you appeal through Meta’s official process.',
 'Facebook account recovery in Bangladesh starts with Facebook’s own routes: Disagree with decision on a suspension notice within 180 days, or facebook.com/hacked for a hijacked account. Report blackmail or fraud locally as well. Unbanz helps you submit a clean appeal through Meta’s official process; Meta makes the final decision.',
 ['If you see a suspended or disabled notice, log in and follow the prompts to disagree with the decision. Facebook gives most suspended accounts 180 days, but trust the date on your own screen.',
  'If the email, number or password was changed, go to facebook.com/hacked on a phone or computer you have used before.',
  'You can also search for your account at facebook.com/login/identify and choose the option for no longer having access to your email or phone.',
  'Check your email, including spam, for a message from Facebook about the change and use its undo link if there is one.',
  'If Facebook asks for ID or a video selfie, use your real details and follow the instructions exactly. Then wait for the reply instead of sending repeat appeals.'],
 'Checks that matter in Bangladesh',
 ['<strong>Your +880 number:</strong> text codes go to the number on the account. If you lost the SIM, your operator can issue a replacement, usually after you re-verify with your NID. Do that before you try recovery.',
  '<strong>Pages and shops:</strong> many Bangladeshi businesses sell through a Facebook Page. If your profile is disabled, a Page where you are the only admin can be lost. Ask someone you trust to confirm they have full control of the Page, and keep your shop name and product photos to hand.',
  '<strong>Phishing is the usual way in:</strong> messages saying your Page will be deleted for “copyright violation”, blue-badge offers, and fake job or giveaway links. Never type your login into a page you reached from a message.',
  '<strong>Blackmail or fraud:</strong> do not pay. Save screenshots and links, then report to Bangladesh Police. The Cyber Police Center (CID) runs a cyber support hotline on 01320-010148 and a complaint portal at cpccid.org, and 999 is the national emergency number. Women can also use Police Cyber Support for Women on 01320-000888.',
  '<strong>Language:</strong> the notice may show in Bangla or English and the options are the same. Screenshot it as it appears. We work over WhatsApp or email in English.'],
 '<p>Not sure which problem you have? ' + A('/facebook-account-disabled-appeal-help/', 'Disabled or suspended') + ', ' + A('/facebook-hacked-account-recovery-service/', 'hacked') + ' and ' + A('/guides/facebook-account-locked/', 'locked') + ' each have their own steps.</p>',
 ['Bangladeshi shops, Page owners, creators and agencies who run their work through Facebook.', 'People hacked through a phishing link or a fake badge offer.', 'Anyone who already appealed once and got nowhere.', 'Not for: accounts that were really used for scams or abuse.'],
 [fb_hf('Bangladesh'),
  ('Where do I report a hacked Facebook account in Bangladesh?', 'To Facebook first, through facebook.com/hacked. If there was fraud, blackmail or stolen money, also report it to Bangladesh Police, for example through the Cyber Police Center portal at cpccid.org or the national emergency number 999. Tell your bank or mobile wallet provider at once if money moved.'),
  ('My Facebook Page admin account was disabled. Do I lose the Page?', 'Facebook says a Page with nobody who has full control is deactivated. If another person already has full control, the Page stays under them. If you are the only admin, act on the appeal quickly and tell us about the Page.'),
  CAN_FAQ],
 FB_REL,
 [('/instagram-account-recovery-bangladesh/', 'Instagram recovery in Bangladesh'), ('/facebook-account-recovery-india/', 'Facebook recovery in India'), ('/instagram-account-recovery-pakistan/', 'Recovery in Pakistan')])
