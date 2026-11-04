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
IGHACK=A('/guides/hacked-instagram-account-recovery/','hacked Instagram account recovery')
HSTEPS=ol(['Open the "Your account was changed" email Instagram sent and use the secure link to undo the change, if it is still there.',
 'On the login screen tap Forgot password, then Need more help, and follow the identity check.',
 'Do the video selfie if offered. It works best when your face is in older posts.',
 'Once back in, change the password, turn on two-factor authentication and remove unknown devices.',
 'Tell followers not to send money or codes to messages from the account.'])
ACE=A('/appeals-centre-europe-instagram-facebook-suspension/','Appeals Centre Europe')
DSA=A('/dsa-appeal-right-instagram-facebook/','your DSA appeal right')
NOPASS=('Does anyone need my password to help?','No. Never share your password or login codes. Anyone who asks for them is a risk.')
def hacked(slug,country,h1c,crumb,lede,answer,cards,local,faqs,who,area):
    page(slug,'ighacked','Instagram Hacked in %s: What to Do'%country,
     'Your Instagram account was hacked and you are in %s. Recovery steps in the app, where to report it locally, and what to send.'%country,
     'Instagram account hacked and you are in %s?'%h1c,crumb,lede,answer,cards,
     [S('Steps',HSTEPS),S('Where to report it in %s'%country,local+' Related: %s and %s.'%(IGHACK,A('/hacker-changed-my-instagram-email-and-password/','hacker changed the email and password')))],
     faqs+[('What if the email and phone were both changed?','Use Need more help on the login screen and the video selfie. The changed email Instagram sent to your old address may also have a secure undo link.'),NOPASS],who,area=area)
hacked('instagram-hacked-usa-what-to-do','the US','the US','Instagram hacked, US',
 'Anywhere in the US, recovery happens inside Instagram. Federal and state reports help if money or identity theft is involved.',
 'If your Instagram was hacked in the US, use the account changed email link or the Need more help recovery flow, then the video selfie. If the hacker scammed followers or used your card, report it to the FBI at ic3.gov and the FTC at ReportFraud.ftc.gov, and keep the reference numbers for the appeal.',
 [('Recover in the app','Changed email link or Need more help.'),('IC3 and FTC','Report scams and identity theft.'),('State AG','A consumer complaint if it drags on.')],
 'Report scams sent from the account or charges to your card to the FBI Internet Crime Complaint Center at ic3.gov and the FTC at ReportFraud.ftc.gov. If your identity was used, IdentityTheft.gov gives a recovery plan. Your state attorney general takes consumer complaints. None of these restore the account, but reference numbers help explain the hack.',
 [('Will the FBI get my account back?','No. IC3 collects reports. It helps if money was lost and gives you a reference to mention.')],
 ['US creators and small businesses after a takeover.','People whose account is being used to scam followers.','Anyone locked out after the email and phone were changed.'],'US')
hacked('instagram-hacked-uk-what-to-do','the UK','the UK','Instagram hacked, UK',
 'Anywhere in the UK, recovery happens inside Instagram. Action Fraud and the ICO cover the parts Instagram does not.',
 'If your Instagram was hacked in the UK, use the account changed email link or the Need more help recovery flow, then the video selfie. If followers were scammed or money was taken, report it to Action Fraud, or Police Scotland in Scotland, and keep the crime reference number for the appeal.',
 [('Recover in the app','Changed email link or Need more help.'),('Action Fraud','Get a crime reference number.'),('ICO','Your data rights.')],
 'Report fraud to Action Fraud at actionfraud.police.uk, or Police Scotland if you live in Scotland. You can ask Meta for the data it holds with a UK GDPR subject access request, and complain to the ICO if it is ignored. Ofcom enforces the Online Safety Act but does not handle individual account complaints.',
 [('Can Ofcom get my account back?','No. Ofcom regulates platforms overall and does not take individual account complaints.')],
 ['UK creators and small businesses after a takeover.','People whose account is scamming their followers.','Anyone locked out after the email and phone were changed.'],'GB')
hacked('instagram-hacked-canada-what-to-do','Canada','Canada','Instagram hacked, Canada',
 'Anywhere in Canada, recovery happens inside Instagram. The CAFC and the privacy commissioner cover the rest.',
 'If your Instagram was hacked in Canada, use the account changed email link or the Need more help recovery flow, then the video selfie. If followers were scammed or money was taken, report it to the Canadian Anti-Fraud Centre and your local police, and keep the file number for the appeal.',
 [('Recover in the app','Changed email link or Need more help.'),('CAFC','Report fraud and keep the number.'),('OPC','Privacy and data access.')],
 'Report fraud to the Canadian Anti-Fraud Centre and your local police. Under PIPEDA you can ask Meta for the personal data it holds, and complain to the Office of the Privacy Commissioner of Canada if it is not answered. These bodies do not restore accounts.',
 [('Can I write in French?','Yes. Write in the language you are most comfortable with.')],
 ['Canadian creators and small businesses after a takeover.','People whose account is scamming their followers.','Anyone locked out after the email and phone were changed.'],'CA')
hacked('instagram-hacked-netherlands-what-to-do','the Netherlands','the Netherlands','Instagram hacked, Netherlands',
 'Anywhere in the Netherlands, recovery happens inside Instagram. Fraudehelpdesk, the police and the Dutch DPA cover the rest.',
 'If your Instagram was hacked in the Netherlands, use the account changed email link or the Need more help recovery flow, then the video selfie. If followers were scammed or money was taken, report it to the Fraudehelpdesk and file a police report, and keep the reference for the appeal.',
 [('Recover in the app','Changed email link or Need more help.'),('Fraudehelpdesk','Report scams, then the police.'),('DSA','EU appeal routes if it is then banned.')],
 'Report scams to the Fraudehelpdesk and file a report (aangifte) with the police. Under the GDPR you can ask Meta for your data and complain to the Autoriteit Persoonsgegevens if it is ignored. If the account is banned after the hack, the EU DSA gives you %s and the %s.'%(DSA,ACE),
 [('Can I write in Dutch?','Yes. Write in the language you are most comfortable with.')],
 ['Dutch creators and small businesses after a takeover.','People whose account is scamming their followers.','Anyone locked out after the email and phone were changed.'],'NL')
hacked('instagram-hacked-france-what-to-do','France','France','Instagram hacked, France',
 'Anywhere in France, recovery happens inside Instagram. Cybermalveillance.gouv.fr, Pharos and the CNIL cover the rest.',
 'If your Instagram was hacked in France, use the account changed email link or the Need more help recovery flow, then the video selfie. Cybermalveillance.gouv.fr has step-by-step help for hacked accounts, and you can file a complaint with the police or gendarmerie if money was taken. Keep the reference for the appeal.',
 [('Recover in the app','Changed email link or Need more help.'),('Cybermalveillance','Official help for hacks.'),('DSA','EU appeal routes if it is then banned.')],
 'Cybermalveillance.gouv.fr gives official guidance for hacked accounts. Report illegal content posted from the account on Pharos (internet-signalement.gouv.fr) and file a complaint with the police or gendarmerie for fraud. Ask Meta for your data under the GDPR and complain to the CNIL if ignored. If the account is banned afterwards, see %s and the %s.'%(DSA,ACE),
 [('Can I write in French?','Yes. Write in the language you are most comfortable with.')],
 ['French creators and small businesses after a takeover.','People whose account is scamming their followers.','Anyone locked out after the email and phone were changed.'],'FR')
def susp(slug,country,crumb,lede,answer,local,lang,area):
    page(slug,'igsusp','Instagram Suspended in %s: Your Options'%country,
     'Your Instagram account was suspended and you are in %s. The in-app appeal, the selfie check, EU DSA routes and what to avoid.'%country,
     'Instagram suspended your account and you are in %s?'%country,crumb,lede,answer,
     [('Appeal once','From the notice, before the countdown ends.'),('Selfie or ID','Same face and name as the profile.'),('DSA routes','Appeals Centre Europe after a final no.')],
     [S('Steps',IGSTEPS),S('EU routes in %s'%country,local+' Related: %s, %s and %s.'%(IGAPP,DSA,ACE))],
     [('Can I write the appeal in %s?'%lang,'Yes. Short and accurate matters more than the language.'),('Will a new account help?','Making a new account to get around a suspension can get that one removed too.'),NOPASS],
     ['Instagram users in %s after a suspension.'%country,'Creators and small businesses whose account is their shop.','People whose account was hacked before it was suspended.'],area=area)
susp('instagram-account-suspended-netherlands-what-to-do','the Netherlands','Instagram suspended, Netherlands',
 'Anywhere in the Netherlands, appeal from the notice first. EU law then gives you more routes than most countries.',
 'If Instagram suspended your account in the Netherlands, appeal once from the notice before the countdown ends and complete the selfie or ID check if asked. Under the EU Digital Services Act, Meta must give a statement of reasons, and after a final decision you can take it to a certified body such as Appeals Centre Europe.',
 'Ask for the statement of reasons Meta must give under the DSA. After the in-app appeal, a certified out-of-court body such as Appeals Centre Europe can look at the decision. You can also ask Meta for your data and complain to the Autoriteit Persoonsgegevens if it is ignored. If a hack came first, report it to the Fraudehelpdesk and the police.','Dutch','NL')
susp('instagram-account-suspended-france-what-to-do','France','Instagram suspended, France',
 'Anywhere in France, appeal from the notice first. EU law then gives you more routes than most countries.',
 'If Instagram suspended your account in France, appeal once from the notice before the countdown ends and complete the selfie or ID check if asked. Under the EU Digital Services Act, Meta must give a statement of reasons, and after a final decision you can take it to a certified body such as Appeals Centre Europe.',
 'Ask for the statement of reasons Meta must give under the DSA. After the in-app appeal, a certified body such as Appeals Centre Europe can look at the decision. You can ask Meta for your data and complain to the CNIL if it is ignored. If a hack came first, use cybermalveillance.gouv.fr and file a complaint with the police or gendarmerie.','French','FR')
page('facebook-account-disabled-france-what-to-do','fbdis','Facebook Disabled in France: Your Options',
 'Your Facebook account was disabled and you are in France. How to appeal, which ID to upload, CNIL and DSA routes, and reporting a hack.',
 'Facebook disabled your account and you are in France?','Facebook disabled, France',
 'From Paris, Lyon, Marseille or elsewhere in France, the appeal on the notice is the first route. EU law adds more.',
 'If Facebook disabled your account in France, appeal once from the notice and upload ID if asked, such as a passport or carte nationale d identite with the same name as the profile. Under the EU Digital Services Act you can then take a final decision to a certified body such as Appeals Centre Europe.',
 [('Appeal once','From the notice, with accurate details.'),('Matching ID','Passport or ID card, same name.'),('DSA routes','Appeals Centre Europe after a final no.')],
 [S('Steps',FBSTEPS),S('Routes in France','Meta must give a statement of reasons under the DSA, and a certified body such as %s can look at a final decision. Ask Meta for your data under the GDPR and complain to the CNIL if ignored. If the account was hacked, use cybermalveillance.gouv.fr, report illegal content on Pharos, and file a complaint with the police or gendarmerie. Related: %s and %s.'%(ACE,FBAPP,DSA))],
 [NOPHONE,NEWPROF,('Can I write the appeal in French?','Yes. Meta may reply in English.')],
 ['Facebook users in France after a ban.','French businesses that run Pages and ads.','People whose account was hacked and then disabled.'],area='FR')
