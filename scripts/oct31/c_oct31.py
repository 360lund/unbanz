# -*- coding: utf-8 -*-
"""2026-10-31 daily: Facebook disabled by country (CA, AU, UAE, Saudi Arabia), rejected appeal EU options,
and Facebook lost access to email or phone for the Gulf and for the UK/EU. Modeled on the converting Facebook guides."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dd29'))
from fams import *
from lib import PAGES
FBAPP = A('/guides/facebook-account-disabled-appeal/', 'Facebook disabled: how to appeal')
FBREJ = A('/guides/facebook-disabled-appeal-rejected/', 'Facebook appeal rejected')
FBLOST = A('/guides/facebook-lost-access-to-email-or-phone/', 'lost access to the email or phone')
PAGESBIZ = A('/facebook-profile-disabled-managing-business-pages/', 'profile disabled while managing business Pages')
NOPHONE = ('Can I call Facebook?', 'Facebook does not offer phone support for disabled accounts. Numbers online that claim to be Facebook support are often scams.')
NEWPROF = ('Will a new profile help?', 'Facebook allows one personal profile per person. A new one can be removed and can count against the appeal.')
FBSTEPS = ol(['Screenshot the notice with the date and any appeal deadline shown.',
              'Appeal from the notice, logged in on the device you normally use.',
              'If asked for ID, upload a clear photo of a government ID where the name matches the profile.',
              'If you manage Pages or ad accounts, ask another admin to check them in Meta Business Suite.',
              'Once you are back in, turn on two-factor authentication and remove devices you do not recognise.'])
PAGESEC = S('If you run Pages or ads', 'A disabled profile can cut you off from your Pages and ad accounts. If there is no second admin, say in the appeal that the profile manages a business Page. See %s.' % PAGESBIZ)

page('facebook-account-disabled-canada-what-to-do', 'fbdis', 'Facebook Disabled in Canada: Your Options',
 'Your Facebook account was disabled and you are in Canada. The appeal, the ID upload, a PIPEDA data request, fraud reports and what to avoid.',
 'Facebook disabled your account and you are in Canada?', 'Facebook disabled, Canada',
 'In Canada the appeal in the notice is the main route. Privacy and fraud bodies sit alongside it, but they do not reverse bans.',
 'If Facebook disabled your account in Canada, appeal once from the notice and upload ID if asked, with the name on the profile. You can ask Meta for a copy of your personal data under PIPEDA. If the account was hacked or used to scam people, report it to the Canadian Anti-Fraud Centre and keep the reference number.',
 [('Appeal once', 'From the notice, with accurate details.'), ('Your data', 'Ask Meta for a copy under PIPEDA.'), ('Fraud reports', 'Canadian Anti-Fraud Centre and police.')],
 [S('Steps', FBSTEPS), PAGESEC,
  S('Privacy and fraud bodies', 'The Office of the Privacy Commissioner of Canada takes complaints if a data request is mishandled. The Canadian Anti-Fraud Centre and your local police take reports about hacks and scams. None of them can restore an account, but a reference number is useful to mention in an appeal about a hack.'),
  S('Related', 'See %s, %s and %s.' % (FBAPP, A('/facebook-account-recovery-canada/', 'Facebook account recovery in Canada'), A('/canada-australia-hacked-or-banned-account-where-to-report/', 'where to report in Canada and Australia'))),
 ],
 [NOPHONE, ('Can I write the appeal in French?', 'Yes. Write in English or French, whichever you are more comfortable with. Clear facts matter more than the language.'), NEWPROF],
 ['Facebook users in Canada after a ban.', 'Canadian small businesses that run Pages.', 'Page and group admins in Canada.'], area='CA')

page('facebook-account-disabled-australia-what-to-do', 'fbdis', 'Facebook Disabled in Australia: Your Options',
 'Your Facebook account was disabled and you are in Australia. The appeal, the ID upload, ReportCyber for hacks, Scamwatch and what to avoid.',
 'Facebook disabled your account and you are in Australia?', 'Facebook disabled, Australia',
 'In Australia the appeal in the notice is the main route. Government services help with hacks, scams and abuse, not with bans.',
 'If Facebook disabled your account in Australia, appeal once from the notice and upload ID if asked, with the name on the profile. If the account was hacked first, report it through ReportCyber and mention the reference in the appeal. Scam reports go to Scamwatch. None of these services can reinstate an account.',
 [('Appeal once', 'From the notice, with accurate details.'), ('Hacked', 'Report it through ReportCyber.'), ('Scams', 'Report them to Scamwatch.')],
 [S('Steps', FBSTEPS), PAGESEC,
  S('Privacy, scams and abuse', 'The Privacy Act lets you ask an organisation for the personal information it holds about you, and the OAIC takes privacy complaints. The eSafety Commissioner deals with serious online abuse. These bodies act within their own powers, but they do not review account bans.'),
  S('Related', 'See %s, %s and %s.' % (FBAPP, A('/facebook-account-recovery-australia/', 'Facebook account recovery in Australia'), A('/canada-australia-hacked-or-banned-account-where-to-report/', 'where to report in Canada and Australia'))),
 ],
 [NOPHONE, ('Can eSafety get my account back?', 'No. eSafety handles serious online abuse and harmful content. It does not review or reverse account bans.'), NEWPROF],
 ['Facebook users in Australia after a ban.', 'Australian small businesses that run Pages.', 'Page and group admins in Australia.'], area='AU')

page('facebook-account-disabled-uae-what-to-do', 'fbdis', 'Facebook Disabled in the UAE: Your Options',
 'Your Facebook account was disabled and you are in the UAE. How to appeal, which ID to upload, reporting a hack to police and avoiding recovery scams.',
 'Facebook disabled your account and you are in the UAE?', 'Facebook disabled, UAE',
 'From Dubai, Abu Dhabi or anywhere in the Emirates, the appeal in the notice is the route. Here is how to give it the best chance.',
 'If Facebook disabled your account in the UAE, appeal once from the notice and upload ID if asked. A passport or an Emirates ID works best when the name matches the profile. If the account was hacked or used to scam people, report it to the police and keep the reference number.',
 [('Appeal once', 'From the notice, with accurate details.'), ('Matching ID', 'Passport or Emirates ID, same name.'), ('Hacked', 'Report it to the police.')],
 [S('Steps', FBSTEPS),
  S('ID checks from the UAE', 'If your profile uses a nickname or an Arabic spelling and your ID uses Latin letters, say so in the appeal so the names can be matched. Use one document and the same one each time you are asked. If you moved to the UAE recently and the profile shows logins from your home country, mention the move.'),
  S('Hacks and recovery scams', 'Dubai Police runs an online eCrime reporting platform. In the other emirates, report to your local police. Be wary of anyone in your DMs who says they work with Meta or asks for your login and money to fix it. Nobody can buy a reinstatement.'),
  S('Related', 'See %s, %s and %s.' % (FBAPP, A('/facebook-account-recovery-uae/', 'Facebook account recovery in the UAE'), A('/instagram-disabled-uae-what-to-do/', 'Instagram disabled in the UAE'))),
 ],
 [NOPHONE, ('Can I write the appeal in Arabic?', 'Yes. Write in Arabic or English, whichever you are more comfortable with. Keep it short and factual.'),
  ('Does logging in from abroad cause problems?', 'Logins from several countries in a short time can trigger security checks. Appeal from your usual phone and connection.')],
 ['Facebook users in the UAE after a ban.', 'UAE businesses that run Pages and ads.', 'Residents and expats in the Emirates.'], area='AE')

page('facebook-account-disabled-saudi-arabia-what-to-do', 'fbdis', 'Facebook Disabled in Saudi Arabia: Your Options',
 'Your Facebook account was disabled and you are in Saudi Arabia. How to appeal, which ID to upload, reporting a hack and avoiding recovery scams.',
 'Facebook disabled your account and you are in Saudi Arabia?', 'Facebook disabled, Saudi Arabia',
 'From Riyadh, Jeddah or anywhere in the Kingdom, the appeal in the notice is the route. Here is how to give it the best chance.',
 'If Facebook disabled your account in Saudi Arabia, appeal once from the notice and upload ID if asked. A passport or national ID works best when the name matches the profile. If the account was hacked or used to scam people, report it to the authorities and keep the reference number.',
 [('Appeal once', 'From the notice, with accurate details.'), ('Matching ID', 'Passport or national ID, same name.'), ('Hacked', 'Report it and keep the reference.')],
 [S('Steps', FBSTEPS),
  S('ID checks from Saudi Arabia', 'If the profile name is written in Arabic and your passport uses Latin letters, say so in the appeal and give both spellings. Use one document and the same one each time you are asked. Residents on an Iqama can use their passport, which usually matches the profile name more closely.'),
  S('Hacks and recovery scams', 'Cybercrime can be reported through the Kollona Amn app or to the police. Be wary of anyone in your DMs who says they work with Meta or asks for your login and money to fix it. Nobody can buy a reinstatement.'),
  PAGESEC,
 ],
 [NOPHONE, ('Can I write the appeal in Arabic?', 'Yes. Write in Arabic or English, whichever you are more comfortable with. Keep it short and factual.'), NEWPROF],
 ['Facebook users in Saudi Arabia after a ban.', 'Saudi businesses that run Pages and ads.', 'Residents and expats in the Kingdom.'], area='SA')

page('facebook-appeal-rejected-eu-options', 'fbdis', 'Facebook Appeal Rejected in the EU: What Is Left',
 'Facebook rejected your appeal and you live in the EU. The statement of reasons, certified dispute bodies under the DSA, your data rights and the limits.',
 'Facebook rejected your appeal and you live in the EU?', 'Appeal rejected, EU',
 'Once Facebook rejects an appeal, it says no further review is available. In the EU, the Digital Services Act leaves one more door open.',
 'If Facebook rejected your appeal and you live in the EU, you can take the decision to a certified out-of-court dispute body under Article 21 of the Digital Services Act, such as Appeals Centre Europe or User Rights. The decision notice carries the reference it needs. The body gives a written opinion; it cannot force Facebook to restore the account.',
 [('Find the notice', 'Email, notifications or Account Status.'), ('Dispute body', 'Certified under DSA Article 21.'), ('Your data', 'A GDPR access request.')],
 [S('Steps', ol(['Find the decision in your email, your notifications or Account Status, and look for the section for people in the EU.',
                 'Create the reference number Facebook offers there. Dispute bodies use it to ask Facebook about the decision.',
                 'Pick a certified body and file on its website. %s, User Rights and ODS are examples.' % A('/appeals-centre-europe-instagram-facebook-suspension/', 'Appeals Centre Europe'),
                 'Keep the account details, the dates and the screenshots in one place. You may be asked for them more than once.'])),
  S('What a dispute body can and cannot do', 'Facebook has to engage with a certified body in good faith and consider its view, but the opinion is not binding. Filing does not stop you from going to court, and you can also complain to your national Digital Services Coordinator. Under the GDPR you can ask Meta for a copy of the personal data it holds about the account.'),
  S('Related', 'See %s, %s and %s.' % (FBREJ, A('/statement-of-reasons-dsa-account-ban/', 'the statement of reasons'), A('/dsa-appeal-right-instagram-facebook/', 'your DSA appeal rights'))),
 ],
 [('Does this work from the UK?', 'The DSA routes are for people in the EU. In the UK, a UK GDPR subject access request is the main tool. See the UK guide on our site.'),
  ('Is a dispute body the same as Facebook support?', 'No. It is independent of Facebook and cannot log in to your account or switch it back on.'),
  ('Will a dispute body restore my account?', 'It cannot order that. It gives a reasoned opinion, and Facebook makes the final decision.')],
 ['People in the EU whose Facebook appeal was rejected.', 'Small businesses in Europe that lost a Page admin profile.', 'Creators in France, Germany, the Netherlands and across the EU.'], area='EU')

page('facebook-lost-access-to-email-or-phone-gulf', 'fblost', 'Facebook Lost Email or Phone Access in the Gulf',
 'You live in the UAE, Saudi Arabia, Qatar or Kuwait and Facebook sends codes to an old number or email. The routes that still work and what to prepare.',
 'Facebook codes going to an old number in the Gulf?', 'Lost email or phone, Gulf',
 'People who move to or from the Gulf often change SIMs. When Facebook still sends codes to the old one, here is what is left.',
 'If Facebook sends login codes to a phone number or email you no longer have, start from the login screen on a device you have used before and choose the option that says you no longer have access. Facebook may ask for ID or let a trusted device approve you. An old home-country SIM can sometimes be reactivated.',
 [('Trusted device', 'Try from a phone you used before.'), ('Old SIM', 'Ask the old carrier about reactivation.'), ('ID check', 'Same name as the profile.')],
 [S('Steps', ol(['Try logging in from a phone or laptop you have used with the account before, on your usual connection.',
                 'On the login screen, choose the option for when you no longer have access to the email or number.',
                 'If the old number was from your home country, ask that carrier whether it can be reactivated or moved to an eSIM.',
                 'If Facebook asks for ID, use the document whose name matches the profile, and use the same one each time.',
                 'Once you are back in, add your current Gulf number and a second email, and save your recovery codes.'])),
  S('Expat details that cause trouble', ul(['Logins from two countries in the same week can trigger a security check. Try from one place.', 'A profile name in Arabic and an ID in Latin letters. Mention both spellings if asked.', 'An old work email that was closed when you left a job.'])),
  S('Related', 'See %s, %s and %s.' % (FBLOST, A('/facebook-lost-access-old-phone-number/', 'an old phone number'), A('/facebook-account-recovery-kuwait/', 'Facebook account recovery in Kuwait'))),
 ],
 [('Can Facebook send the code to my new number?', 'Not until the new number is on the account. You need another way in first, such as a trusted device or an ID check.'),
  ('Should I make a new account?', 'Facebook allows one personal profile per person. A new one can be removed and does not bring back your Pages.'), ('Is there a Facebook office in the Gulf I can visit?', 'Not for account recovery. It happens online, through the login screen and the Help Center.')],
 ['Expats in the UAE, Saudi Arabia, Qatar and Kuwait.', 'Gulf businesses whose admin changed numbers.', 'People who moved home and lost their Gulf SIM.'], area=['AE', 'SA', 'QA', 'KW'])

page('facebook-lost-access-to-email-or-phone-uk-eu', 'fblost', 'Facebook Lost Email or Phone Access: UK and EU',
 'You are in the UK or EU and cannot get Facebook login codes because the email or number is gone. The routes that still work and your data rights.',
 'Lost the email or phone on your Facebook in the UK or EU?', 'Lost email or phone, UK and EU',
 'An old work email, a closed mobile contract, a number from another country. Here is what still works when the codes cannot reach you.',
 'If you are in the UK or EU and Facebook sends codes to an email or number you no longer have, start from the login screen on a device you have used before and choose the option that says you no longer have access. Facebook may ask for ID. A GDPR data request does not reopen the account.',
 [('Trusted device', 'Try from a phone you used before.'), ('Old number', 'Ask your carrier about the number.'), ('ID check', 'Same name as the profile.')],
 [S('Steps', ol(['Try logging in from a phone or laptop you have used with the account before, on your usual home connection.',
                 'On the login screen, choose the option for when you no longer have access to the email or number.',
                 'If the number was on a contract you ended, ask the carrier whether it can be restored to a new SIM.',
                 'If it was a work email, ask the old employer whether the mailbox can be reopened briefly.',
                 'Once you are back in, add a personal email you control and save your recovery codes.'])),
  S('Data rights and their limits', 'Under the GDPR and UK GDPR you can ask Meta for a copy of the personal data it holds. That can confirm which email and number are on the account. It does not give you back access. If the account was hacked, report it to the police; in England, Wales and Northern Ireland that means Action Fraud.'),
  S('Related', 'See %s, %s and %s.' % (FBLOST, A('/facebook-recovery-code-sent-to-wrong-email/', 'code sent to the wrong email'), A('/uk-gdpr-subject-access-request-meta-disabled-account/', 'UK GDPR subject access request'))),
 ],
 [('Can I email Facebook to change the number?', 'No. There is no support address for this. Use the login screen options or the ID check Facebook offers.'),
  ('Does it help to try many times?', 'No. Repeated attempts can lock the flow for a while. Try once a day from the same device.'), ('What if a hacker changed the email?', 'Facebook usually emails the old address when the email changes, with a link to undo it. Look for that message, then use the Facebook hacked-account page from a device you used before.')],
 ['People in the UK and EU locked out by an old email or number.', 'Small businesses whose admin left the company.', 'People who moved between countries.'], area=['GB', 'EU'])
