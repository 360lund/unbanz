# -*- coding: utf-8 -*-
"""2026-11-04 daily: deepen converting Facebook / Instagram / Meta-ad themes with gap pages
that answer stressed-user prompts (appeal pack, logged out, countdown wait, missing appeal
after ID check, ad restricted vs profile disabled, payment then restricted, lost email+phone,
Facebook disabled in Switzerland)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dd29'))
from fams import *
from lib import PAGES

FBAPP = A('/guides/facebook-account-disabled-appeal/', 'Facebook disabled: how to appeal')
FBLOST = A('/guides/facebook-lost-access-to-email-or-phone/', 'lost access to the email or phone')
IGAPP = A('/guides/instagram-account-suspended-appeal/', 'how to appeal an Instagram suspension')
IGNO = A('/guides/instagram-disabled-no-appeal-button/', 'no appeal button')
IGID = A('/guides/instagram-id-verification-request/', 'Instagram ID verification')
IG180 = A('/instagram-account-suspended-180-days/', 'the 180-day countdown')
IG48 = A('/instagram-disabled-first-48-hours/', 'the first 48 hours')
ADREST = A('/guides/meta-ad-account-restricted/', 'Meta ad account restricted')
ADPAY = A('/guides/meta-ad-payment-declined-fix/', 'Meta ad payment declined')
ADFIX = A('/meta-ad-account-fix-the-cause-before-appeal/', 'fix the cause before the appeal')
WTSEND = A('/what-to-send-for-account-recovery-help/', 'what to send for recovery help')
NOPHONE = ('Can I call Facebook?', 'Facebook does not offer phone support for disabled accounts. Numbers online that claim to be Facebook support are often scams.')
NEWPROF = ('Will a new profile help?', 'Facebook allows one personal profile per person. A new one can be removed and can count against the appeal.')
NOPASS_AD = ('Can an agency get my ad account back faster?', 'No one can speed up Meta. A clear, accurate appeal with documents that match is what helps. Meta makes the final decision.')

FBSTEPS = ol(['Screenshot the notice with the date and any appeal deadline shown.',
              'Appeal from the notice, logged in on the device you normally use.',
              'If asked for ID, upload a clear photo of a government ID where the name matches the profile.',
              'If you manage Pages or ad accounts, ask another admin to check them in Meta Business Suite.',
              'Once you are back in, turn on two-factor authentication and remove devices you do not recognise.'])
IGSTEPS = ol(['Screenshot the notice, with the date and any deadline shown.',
              'Appeal from the notice in the app, once, with accurate details.',
              'Do the video selfie or ID check if Instagram asks for it.',
              'Keep the final decision message. You need it for the next step.'])
ADSTEPS = ol(['Open Account Quality in Meta Business Suite and screenshot the notice before changing anything.',
              'Work out which asset is limited: the ad account, the business portfolio, a Page or an admin profile.',
              'Clear any unpaid balance and remove payment methods that are not in the business name.',
              'Make the business name and address match across the portfolio, the ad account, the website and your documents.',
              'Request one review, with a short note that explains what the business does.'])

# 1. Companion to top FB appeal guide
INDIA=('Is there an India-specific route?', 'Under the IT Rules 2021, large platforms must have a Grievance Officer for India. If that complaint does not resolve it, the Grievance Appellate Committee at gac.gov.in takes appeals. These run alongside the in-app appeal, not instead of it.')
page('instagram-account-suspended-india-what-to-do', 'igsusp',
 'Instagram Suspended in India: Your Options',
 'Your Instagram account was suspended and you are in India. The in-app appeal, the selfie or ID check, the India grievance route and what to avoid.',
 'Instagram suspended your account and you are in India?',
 'Instagram suspended, India',
 'From Delhi, Mumbai, Bengaluru or anywhere in India, the appeal on the notice comes first. India also has a formal grievance route.',
 'If Instagram suspended your account in India, appeal once from the notice before the countdown ends and complete the video selfie or ID check if asked. Under the IT Rules 2021 you can also send a complaint to the platform Grievance Officer for India, and if that does not resolve it, appeal to the Grievance Appellate Committee at gac.gov.in.',
 [('Appeal once', 'From the notice, before the countdown ends.'),
  ('Selfie or ID', 'Good light, same face as the profile.'),
  ('Grievance route', 'Grievance Officer, then gac.gov.in.')],
 [S('Steps', IGSTEPS),
  S('The India grievance route', 'The IT Rules 2021 require significant social media platforms to name a Grievance Officer for India and acknowledge complaints. Use the grievance contact listed in the Instagram Help Center for India, attach the notice screenshot and your username, and keep the reference. If the reply does not resolve it, the Grievance Appellate Committee at gac.gov.in accepts appeals against the platform decision. Related: %s, %s and %s.' % (IGAPP, IGID, IG180)),
  S('If it was hacked first', 'If someone took over the account before the suspension, report it at cybercrime.gov.in or on the 1930 helpline and keep the acknowledgement number. Mention the hack in the appeal. See %s.' % A('/guides/hacked-instagram-account-recovery/', 'hacked Instagram account recovery')),
 ],
 [INDIA,
  ('Can I write the appeal in Hindi or another Indian language?', 'Write in the language you are most comfortable with. Short and accurate matters more than the language.'),
  ('Should I pay someone on Telegram who says they can unban me?', 'Be careful. Many such offers are scams. Nobody needs your password or login codes.')],
 ['Instagram users in India after a suspension.',
  'Creators and small businesses in India whose account is their shop.',
  'People in India whose account was hacked before it was suspended.'], area='IN')
page('facebook-account-disabled-india-what-to-do', 'fbdis',
 'Facebook Disabled in India: Your Options',
 'Your Facebook account was disabled and you are in India. How to appeal, which ID to upload, the India grievance route and reporting a hack.',
 'Facebook disabled your account and you are in India?',
 'Facebook disabled, India',
 'Anywhere in India, the appeal on the notice is the first route. India also gives you a formal grievance route.',
 'If Facebook disabled your account in India, appeal once from the notice and upload ID if asked. Aadhaar, PAN or a passport can work when the name matches. Under the IT Rules 2021 you can also complain to the Grievance Officer for India and then appeal to the Grievance Appellate Committee at gac.gov.in.',
 [('Appeal once', 'From the notice, with accurate details.'),
  ('Matching ID', 'Same name as the profile.'),
  ('Grievance route', 'Grievance Officer, then gac.gov.in.')],
 [S('Steps', FBSTEPS),
  S('ID from India', 'Use one document and the same one each time you are asked. If the profile uses a short or nickname form and the ID shows your full name, say so in the appeal. On Aadhaar, the masked version that hides most digits is usually enough.'),
  S('The India grievance route', 'Large platforms must name a Grievance Officer for India under the IT Rules 2021. Send the notice screenshot and your profile link through the grievance contact in the Facebook Help Center, and keep the reference. If that does not resolve it, the Grievance Appellate Committee at gac.gov.in takes appeals. Related: %s, %s and %s.' % (FBAPP, FBLOST, A('/guides/facebook-id-upload-request/', 'Facebook asked for ID'))),
 ],
 [INDIA, NOPHONE, NEWPROF],
 ['Facebook users in India after a ban.',
  'Indian businesses that run Pages and ads.',
  'People whose account was hacked and then disabled.'], area='IN')
page('instagram-account-suspended-pakistan-what-to-do', 'igsusp',
 'Instagram Suspended in Pakistan: Your Options',
 'Your Instagram account was suspended and you are in Pakistan. The in-app appeal, the selfie or ID check, VPN and SIM issues, and what to avoid.',
 'Instagram suspended your account and you are in Pakistan?',
 'Instagram suspended, Pakistan',
 'From Karachi, Lahore, Islamabad or elsewhere in Pakistan, the appeal on the notice comes first.',
 'If Instagram suspended your account in Pakistan, appeal once from the notice before the countdown ends, with your VPN off, and complete the video selfie or ID check if asked. If the number on the account is a SIM you no longer have, recover the SIM from your network first so you can receive codes.',
 [('Appeal once', 'From the notice, VPN off.'),
  ('Selfie or ID', 'CNIC or passport, same name.'),
  ('Your number', 'Keep the SIM on the account working.')],
 [S('Steps', IGSTEPS),
  S('VPNs and SIMs', 'Many people in Pakistan use a VPN, and a login from another country right before the suspension can add checks. Turn it off for the appeal and the selfie. If the account phone number is an old SIM, get a duplicate from your network with your CNIC before you start. Related: %s, %s and %s.' % (IGAPP, IGNO, IG180)),
  S('If it was hacked first', 'If someone took over the account, report it to the federal cyber crime authorities and keep the complaint reference. Mention the hack in the appeal. See %s.' % A('/guides/hacked-instagram-account-recovery/', 'hacked Instagram account recovery')),
 ],
 [('Can I upload my CNIC?', 'Yes, if Instagram asks for ID. Use one clear photo, with the name matching the profile.'),
  ('Can I write the appeal in Urdu?', 'Yes. Short and accurate matters more than the language.'),
  ('Should I pay someone who says they know someone at Meta?', 'No. Such offers are often scams. Nobody needs your password or login codes.')],
 ['Instagram users in Pakistan after a suspension.',
  'Creators and online sellers in Pakistan.',
  'People whose account was hacked before it was suspended.'], area='PK')
page('facebook-account-disabled-pakistan-what-to-do', 'fbdis',
 'Facebook Disabled in Pakistan: Your Options',
 'Your Facebook account was disabled and you are in Pakistan. How to appeal, using your CNIC, VPN and SIM issues, and reporting a hack.',
 'Facebook disabled your account and you are in Pakistan?',
 'Facebook disabled, Pakistan',
 'Anywhere in Pakistan, the appeal on the notice is the route. A matching CNIC and a working phone number matter most.',
 'If Facebook disabled your account in Pakistan, appeal once from the notice with your VPN off, and upload your CNIC or passport if asked, with the name matching the profile. If the phone number on the account is an old SIM, get a duplicate from your network first so you can receive codes.',
 [('Appeal once', 'From the notice, VPN off.'),
  ('Matching ID', 'CNIC or passport, same name.'),
  ('Hacked', 'Report it and keep the reference.')],
 [S('Steps', FBSTEPS),
  S('Names and CNIC', 'If the profile shows a nickname or a different spelling from your CNIC, say so in the appeal so the names can be matched. Use the same document each time. Related: %s, %s and %s.' % (FBAPP, FBLOST, A('/guides/facebook-id-upload-request/', 'Facebook asked for ID'))),
  S('Pages and ads', 'If the profile ran a business Page or ads, ask another admin to check them in Meta Business Suite now. See %s.' % A('/facebook-profile-disabled-managing-business-pages/', 'profile disabled while managing business Pages')),
 ],
 [NOPHONE, NEWPROF,
  ('Can I write the appeal in Urdu?', 'Yes. Short and accurate matters more than the language.')],
 ['Facebook users in Pakistan after a ban.',
  'Pakistani businesses that run Pages and ads.',
  'People whose account was hacked and then disabled.'], area='PK')
