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
page('facebook-disabled-what-to-send-with-the-appeal', 'fbdis',
 'Facebook Disabled: What to Send With the Appeal',
 'What to include with a Facebook disabled-account appeal: notice screenshot, matching ID, short note, dates. What never to send.',
 'Facebook disabled your account. What should go with the appeal?',
 'What to send with a Facebook appeal',
 'A short, accurate pack beats a long story. The notice, matching ID and a few plain facts are enough.',
 'If Facebook disabled your account, send the appeal from the notice with a screenshot of that notice, a government ID that matches the profile name, and a short note about how you use the account. Add dates and what changed just before. Never send your password, login codes or email access. Meta makes the final decision.',
 [('Screenshot', 'The notice, with the date and reason visible.'),
  ('Matching ID', 'Same name as the profile, clear and current.'),
  ('Short note', 'Who you are, how you use it, what changed.')],
 [S('What belongs in the pack', ul(['A screenshot of the disabled or suspended notice, including the date and any policy named.',
     'A government ID where the name matches the profile. Passports and national ID cards work best.',
     'Two or three sentences: you own the account, what you use it for, and why the reason looks wrong.',
     'If it was hacked first, say so and give the date you lost control.',
     'If you run Pages or ads, note that another admin may need to check them.'])),
  S('What to leave out', ul(['Your password, backup codes and login codes.',
     'Long emotional stories, threats or copied templates from forums.',
     'Extra appeals for the same decision while one is open.',
     'A new profile made on the same phone while you wait.'])),
  S('Related', 'See %s, %s and %s.' % (FBAPP, WTSEND, A('/guides/facebook-id-upload-request/', 'Facebook ID upload request'))),
 ],
 [('Do I need a lawyer letter?', 'No. Clear facts and matching ID are what the form is built for.'),
  ('Should I attach bank statements or bills?', 'Only if Facebook asks for them. Extra documents that are not requested rarely help.'),
  NEWPROF],
 ['People preparing a Facebook disabled-account appeal.',
  'Business owners whose profile controls Pages or ads.',
  'Anyone who has been asked for ID after a disable.'])

# 2. Common stress prompt
page('facebook-account-disabled-while-logged-out', 'fbdis',
 'Facebook Account Disabled While Logged Out',
 'You were logged out of Facebook and now the account looks disabled. How to open the notice, appeal once and what to avoid.',
 'Facebook disabled your account while you were logged out?',
 'Disabled while logged out',
 'Many people only learn about a disable when a login fails. The notice after login is still the route.',
 'If Facebook disabled your account while you were logged out, try to log in on the phone or computer you normally use. The disabled notice often appears after a failed login. Appeal once from that notice, with matching ID if asked. Do not open a new profile on the same device while you wait. Meta makes the final decision.',
 [('Log in as usual', 'Same phone, same network, VPN off.'),
  ('Find the notice', 'It often appears after the failed login.'),
  ('Appeal once', 'From the notice, with matching ID.')],
 [S('How to reach the notice when you are logged out', ol(['Open Facebook on the device and Wi-Fi you normally use.',
     'Enter the usual password. If login fails with a disabled message, read the full screen and screenshot it.',
     'If Facebook offers “Disagree with decision” or an appeal link, use it once.',
     'If you cannot reach any notice, try the Help Center path for suspended or disabled accounts while logged out, still from your usual device.',
     'If the password or email was changed by someone else, start at facebook.com/hacked instead of a ban appeal.'])),
  S('Mistakes that make it harder', ul(['Creating a second profile on the same phone.',
     'Appealing from a VPN or a brand-new device.',
     'Paying someone in Messenger who claims to work with Meta.',
     'Sending several appeals for the same decision.'])),
  S('Related', 'See %s, %s and %s.' % (FBAPP, A('/guides/hacked-facebook-account-recovery/', 'hacked Facebook recovery'), A('/facebook-disabled-what-to-send-with-the-appeal/', 'what to send with the appeal'))),
 ],
 [NOPHONE,
  ('The login just spins and never shows a notice. What then?', 'Try another usual device, turn the VPN off, and check the email on the account for a disable message. If nothing appears, send us a screenshot of the login screen.'),
  NEWPROF],
 ['People who found out about a disable only after logging out.',
  'Users locked out on a new phone or after travel.',
  'Page admins who lost the profile while signed out.'])

# 3. Countdown wait companion (differs from existing countdown-running page)
page('instagram-suspended-countdown-what-happens-if-you-wait', 'igsusp',
 'Instagram Suspended Countdown: What If You Wait?',
 'Instagram suspended your account and the countdown is running. What happens if you wait it out, and why appealing once still matters.',
 'Instagram suspended you. What if you just wait?',
 'Suspended countdown: if you wait',
 'The countdown is not a cool-down that lifts on its own. Waiting without appealing usually ends in a disable.',
 'If Instagram suspended your account and shows a countdown, waiting without using the appeal usually means the account is disabled when the window ends. The countdown is the time left to disagree, not a pause that clears itself. Appeal once from the notice, finish any selfie or ID step, and keep the screenshots. Instagram makes the final decision.',
 [('Not a cool-down', 'Waiting alone rarely restores access.'),
  ('Appeal once', 'From the notice before the date shown.'),
  ('Keep proof', 'Screenshots of the notice and any reply.')],
 [S('What the countdown actually is', 'On many suspension screens Instagram shows how long you have to disagree, often about 180 days. That clock is for the appeal. If you do nothing, Instagram’s help wording says the account is then disabled and a further review of that decision is not offered. See %s and %s.' % (IG180, IGAPP)),
  S('What to do instead of waiting', IGSTEPS),
  S('If the countdown already ended', 'When the window is gone and there is no appeal button left, read %s. EU users may still have an out-of-court route after a final decision. Related: %s and %s.' % (IGNO, IG48, A('/appeals-centre-europe-instagram-facebook-suspension/', 'Appeals Centre Europe'))),
 ],
 [('Will the suspension lift if I stay quiet?', 'Usually no. The countdown is time to appeal, not a temporary mute that ends by itself.'),
  ('Can I appeal on the last day?', 'If the button is still there, yes. Earlier is better while details are fresh.'),
  ('Should I make a new account while I wait?', 'No. A new account on the same phone or email can be linked to the suspended one.')],
 ['People staring at an Instagram suspension countdown.',
  'Creators and shops whose account is frozen but not yet disabled.',
  'Anyone unsure whether waiting is safer than appealing.'])

# 4. Appeal button missing after ID check
page('instagram-appeal-button-missing-after-id-check', 'igverify',
 'Instagram Appeal Button Missing After ID Check',
 'You finished Instagram ID or selfie verification and the appeal button is gone. What that usually means and what to try next.',
 'Instagram ID check done, but the appeal button is gone?',
 'Appeal button missing after ID check',
 'After an ID or selfie step the screen often changes. Read the new wording before you try anything else.',
 'If Instagram asked for an ID or video selfie and the appeal button then disappeared, open the notice again on your usual phone. The check may still be running, a decision may already be made, or a linked Facebook profile may be blocking it. Do not open a new account while you wait. Instagram makes the final decision.',
 [('Re-open the notice', 'Same phone, VPN off, fresh screenshot.'),
  ('Check Accounts Center', 'A linked Facebook limit can block Instagram.'),
  ('Hold off', 'No new accounts on the same device.')],
 [S('What usually happened', ul(['The ID or selfie is still under review, and the appeal control is hidden until that finishes.',
     'Instagram already accepted or rejected the check, and the screen now shows a final decision without a button.',
     'The Instagram account is tied to a Facebook profile that is restricted in Accounts Center, so the Instagram appeal cannot move.',
     'You are looking at a different login than the one that held the appeal.'])),
  S('What to try', ol(['Force-close the app, turn the VPN off, and open the notice again on your usual phone.',
     'Check the email on the account, including spam, for a decision or a further request.',
     'Open Accounts Center from any working Meta app and see whether the linked Facebook profile has its own limit.',
     'If a final disabled screen appears with no button, see %s and %s.' % (IGNO, IGID)])),
  S('Related', 'See %s, %s and %s.' % (IGAPP, A('/guides/instagram-video-selfie-verification/', 'video selfie verification'), WTSEND)),
 ],
 [('How long does an ID check take?', 'Instagram does not publish a fixed time. Check the app every day or two rather than sending the same upload again.'),
  ('Should I upload ID a second time?', 'Only if Instagram asks again. Repeat uploads without a new request rarely help.'),
  ('Do I need to share my password with anyone?', 'No. Your password and login codes stay with you.')],
 ['People who finished Instagram ID or selfie checks and lost the appeal button.',
  'Users whose linked Facebook profile may be limited too.',
  'Anyone stuck between verification and a final decision.'])

# 5. Restricted-from-advertising vs disabled personal profile
page('meta-ad-account-restricted-vs-disabled-personal-profile', 'ad',
 'Ad Restricted vs Disabled Personal Profile',
 'Meta restricted your ad account, or disabled your personal Facebook profile? How to tell which asset is limited and which route to use.',
 'Is it the ad account, or your personal profile?',
 'Ad restricted vs profile disabled',
 'Ads and personal profiles use different notices and different appeal paths. Mixing them up wastes the one clear request you get.',
 'A Meta ad account restricted from advertising is not the same as a disabled personal Facebook profile. Open Account Quality for ads and the login notice for the profile, then fix the asset the message names. An ad restriction often leaves the profile working; a disabled profile can cut off Pages and ads you admin. Meta makes the final decision.',
 [('Read the asset', 'Ad account, Page, portfolio or personal profile.'),
  ('Use the right screen', 'Account Quality for ads; the login notice for a profile.'),
  ('Fix then request', 'Change the cause, then one clear review.')],
 [S('How to tell them apart', ul(['Restricted from advertising: you can often still use Facebook and Instagram, but ads will not run. The detail sits in Account Quality.',
     'Disabled personal profile: you cannot use the profile, and Pages or ad accounts where you were the only admin may be cut off.',
     'Business portfolio restriction: several ad accounts under one portfolio can be limited together.',
     'Page restriction: the Page cannot run ads or post, while your personal login may still work.'])),
  S('What to do for each', ol(['Screenshot the exact notice and note which asset ID it names.',
     'For an ad restriction, fix the cause first, then request one review. See %s and %s.' % (ADREST, ADFIX),
     'For a disabled personal profile, appeal from the login notice. See %s.' % FBAPP,
     'Ask another admin to check Pages and ads if your profile is the one that is down.'])),
  S('Related', 'See %s and %s.' % (A('/meta-ad-account-restricted-vs-disabled/', 'restricted vs disabled ad accounts'), A('/facebook-profile-disabled-managing-business-pages/', 'profile disabled while managing Pages'))),
 ],
 [NOPASS_AD,
  ('Can I run ads from a new ad account while my profile is disabled?', 'Often no. A disabled personal profile can block the tools you need, and a new ad account tied to the same people can pick up limits too.'),
  ('Does fixing billing help a disabled profile?', 'Billing fixes help payment-related ad restrictions. A disabled personal profile needs the profile appeal, not a billing change.')],
 ['Advertisers who see a restriction and are not sure which asset it hits.',
  'Business owners whose personal profile and ad account both look wrong.',
  'Agencies sorting client portfolios after a notice.'], area=['US','GB','CA','AU','DE','AE'])

# 6. Payment declined then restricted
page('meta-ad-payment-declined-then-account-restricted', 'ad',
 'Payment Declined, Then Ad Account Restricted',
 'A Meta ad payment failed and the ad account was restricted afterwards. Clear the balance, fix billing, then request one review.',
 'Payment declined, then the ad account was restricted?',
 'Payment declined then restricted',
 'Clear the failed charge first. An appeal that ignores an unpaid balance is easy to reject.',
 'If a Meta ad payment declined and the ad account was restricted, open Billing and Account Quality, clear unpaid balance, and use a payment method in the business name. Remove failed cards. Request one review saying you cleared the balance and updated billing. Do not open a new ad account while this one is limited. Meta makes the final decision.',
 [('Clear the balance', 'Pay what is owed in Billing first.'),
  ('Fix the method', 'A working method in the business name.'),
  ('Then one review', 'Say what you changed, in a few lines.')],
 [S('Order that usually works', ADSTEPS),
  S('Why the restriction follows a decline', 'Failed charges, chargebacks and cards used on other limited accounts are common triggers. Meta may restrict the ad account until billing looks clean. See %s and %s. Related: %s.' % (ADPAY, ADFIX, ADREST)),
  S('What not to do', ul(['Opening a second ad account on the same business to keep spending.',
     'Adding random personal cards that are not in the business name.',
     'Sending several review requests while billing is still failing.',
     'Sharing Business Manager passwords with anyone offering a restore.'])),
 ],
 [NOPASS_AD,
  ('The card works everywhere else. Why did Meta decline it?', 'Banks and Meta each run their own checks. A card can work in shops and still fail on ads. Try another method in the business name and clear the unpaid amount.'),
  ('Should I remove the old card?', 'Yes, if it keeps failing. Leave one working method that belongs to the business.')],
 ['Advertisers whose ad account was restricted after a failed charge.',
  'Shops and agencies clearing billing before a review request.',
  'Businesses that saw a decline and then could not run ads.'], area=['US','GB','CA','AU','DE','AE','NL'])

# 7. Lost email and phone together
page('facebook-lost-email-and-phone-at-the-same-time', 'fblost',
 'Facebook Lost Email and Phone at the Same Time',
 'You cannot reach the email or phone on your Facebook account. How to use login help, ID checks and trusted contacts without making it worse.',
 'Lost the Facebook email and phone at the same time?',
 'Lost email and phone together',
 'When both contact methods are gone, Facebook leans on devices it already trusts and on identity checks.',
 'If you lost both the email and the phone on your Facebook account at once, start login help on a phone or computer you have used before. Facebook may offer an ID upload, a video selfie or trusted contacts. Do not create a new profile on the same device while you try. Meta makes the final decision on recovery.',
 [('Usual device', 'Start from a phone Facebook already knows.'),
  ('Login help', 'Follow the on-screen options once.'),
  ('ID if asked', 'A clear document that matches the profile.')],
 [S('Steps when both contacts are gone', ol(['On a familiar device, open Facebook and choose “Forgotten password” or the login help link.',
     'When it asks for email or phone, say you no longer have them and continue through the options shown.',
     'Complete any ID or selfie check with a document that matches the profile name.',
     'If trusted contacts are offered and you still have people set up, use that path once.',
     'If someone else changed the email and phone, treat it as a hack and also use facebook.com/hacked.'])),
  S('Why both can disappear together', 'A hacker often changes email and phone in one session. A number that was recycled by a carrier, or an email you deleted years ago, can leave you in the same place even without a hack. See %s.' % FBLOST),
  S('Related', 'See %s, %s and %s.' % (A('/guides/facebook-two-factor-lost-access/', 'lost two-factor access'), A('/guides/hacked-facebook-account-recovery/', 'hacked Facebook recovery'), WTSEND)),
 ],
 [NOPHONE,
  ('Can a friend reset it for me?', 'Only if they are set as a trusted contact and Facebook offers that option. Otherwise the owner has to complete the checks.'),
  ('Should I make a new Facebook account?', 'Not while recovery is open. A new profile on the same device can be linked to the old one.')],
 ['People locked out of Facebook with no working email or phone.',
  'Users whose number was recycled or whose old inbox was deleted.',
  'Anyone who thinks a hacker changed both contact methods.'])

# 8. Rich-country page tied to converting FB disabled family
page('facebook-account-disabled-switzerland-what-to-do', 'fbdis',
 'Facebook Disabled in Switzerland: Your Options',
 'Your Facebook account was disabled and you are in Switzerland. How to appeal, which ID to upload, reporting a hack and privacy routes.',
 'Facebook disabled your account and you are in Switzerland?',
 'Facebook disabled, Switzerland',
 'From Zurich, Geneva, Basel or elsewhere in Switzerland, the appeal in the notice is the route. Matching ID matters most.',
 'If Facebook disabled your account in Switzerland, appeal once from the notice and upload ID if asked. A passport or Swiss ID card works best when the name matches the profile. If the account was hacked or used to scam people, report it through the Federal Office for Cyber Security or your cantonal police and keep the reference number.',
 [('Appeal once', 'From the notice, with accurate details.'),
  ('Matching ID', 'Passport or Swiss ID, same name.'),
  ('Hacked', 'Report it and keep the reference.')],
 [S('Steps', FBSTEPS),
  S('ID checks from Switzerland', 'If the profile uses a nickname and your ID shows your legal name, say so in the appeal so the names can be matched. Use one document and the same one each time you are asked. Residents who moved to Switzerland recently should mention the move if the profile shows older logins from another country.'),
  S('Privacy and cyber reports', 'The Swiss Federal Act on Data Protection lets you ask Meta for the personal data it holds about you. For fraud, extortion or a hack, report through the Federal Office for Cyber Security form and your cantonal police. These bodies do not reverse bans, but a reference number helps if you need to explain a hack in the appeal. Related: %s, %s and %s.' % (FBAPP, A('/facebook-account-recovery-switzerland/', 'Facebook account recovery in Switzerland'), A('/meta-ad-account-disabled-switzerland/', 'Meta ad account disabled in Switzerland'))),
 ],
 [NOPHONE,
  ('Can I write the appeal in German, French or Italian?', 'Yes. Write in the language you are most comfortable with. Meta may reply in English.'),
  NEWPROF],
 ['Facebook users in Switzerland after a ban.',
  'Swiss businesses that run Pages and ads.',
  'Residents and expats in Switzerland.'], area='CH')
