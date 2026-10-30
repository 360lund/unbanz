# -*- coding: utf-8 -*-
"""2026-10-30 daily: high-value country pages (CA, AU, UAE, UK, US, EU) and Gulf username claims."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dd29'))
from fams import *
from lib import PAGES
ACE = A('/appeals-centre-europe-instagram-facebook-suspension/', 'Appeals Centre Europe')
SUSP = A('/guides/instagram-account-suspended-appeal/', 'Instagram suspended: how to appeal')
NOBTN = A('/guides/instagram-disabled-no-appeal-button/', 'No appeal button on Instagram')
FBAPP = A('/guides/facebook-account-disabled-appeal/', 'Facebook disabled: how to appeal')
FBLOST = A('/guides/facebook-lost-access-to-email-or-phone/', 'Lost access to the email or phone')
IGID = A('/guides/instagram-id-verification-request/', 'Instagram ID verification request')
NOPHONE = ('Can I call Instagram?', 'Instagram does not offer phone support. Numbers online that claim to be Instagram support are often scams.')
NEWACC = ('Should I open a new account while I wait?', 'Not on the same phone or email. Linked accounts are often removed too, and it can count against the appeal.')
IGSTEPS = ol(['Screenshot the notice with the date and any appeal deadline shown.',
              'Appeal from the notice, logged in on the phone you normally use.',
              'If asked for ID or a video selfie, do it once, in good light, with the name on your ID matching the account.',
              'Check Accounts Center. If the linked Facebook profile is restricted too, mention it in the appeal.',
              'Check that any email about the account really came from Instagram before you click anything.'])
FBSTEPS = ol(['Screenshot the notice with the date and any appeal deadline shown.',
              'Appeal from the notice, logged in on the device you normally use.',
              'If asked for ID, upload a clear photo of a government ID where the name matches the profile.',
              'If you manage Pages or ad accounts, ask another admin to check them in Meta Business Suite.',
              'Once you are back in, turn on two-factor authentication and remove devices you do not recognise.'])

page('instagram-disabled-canada-what-to-do', 'igsusp', 'Instagram Disabled in Canada: Your Options',
 'Your Instagram account was disabled and you are in Canada. The appeal, ID checks, a PIPEDA data request, fraud reports and what to avoid.',
 'Instagram disabled your account and you are in Canada?', 'Instagram disabled, Canada',
 'In Canada the in-app appeal is the main route. Privacy and fraud bodies help with your data and with scams, not with bans.',
 'If Instagram disabled your account in Canada, appeal once from the notice and complete any ID or video selfie check it asks for. You can ask Meta for a copy of your personal data under Canadian privacy law. If the account was hacked or used to scam people, report it to the Canadian Anti-Fraud Centre.',
 [('Appeal once', 'From the notice, with accurate details.'), ('Your data', 'Ask Meta for a copy under PIPEDA.'), ('Fraud reports', 'Canadian Anti-Fraud Centre and police.')],
 [S('Steps', IGSTEPS),
  S('Privacy and fraud bodies',
    'PIPEDA, the federal private-sector privacy law, gives you a right to ask an organisation for the personal information it holds about you, and you can make that request to Meta. The Office of the Privacy Commissioner of Canada takes complaints if a request is mishandled. If the account was hacked or used to scam your followers, report it to the Canadian Anti-Fraud Centre and your local police, and keep the reference number. None of these bodies can restore an account.'),
  S('Related', 'See %s, %s and %s.' % (SUSP, NOBTN, A('/canada-australia-hacked-or-banned-account-where-to-report/', 'where to report in Canada and Australia'))),
 ],
 [NOPHONE, ('Does it matter if I write the appeal in French?', 'No. Write in English or French, whichever you are more comfortable with. Clear facts matter more than the language.'), NEWACC],
 ['Instagram users in Canada after a ban.', 'Canadian small businesses and creators.', 'Parents of teens in Canada.'], area='CA')

page('instagram-disabled-australia-what-to-do', 'igsusp', 'Instagram Disabled in Australia: Your Options',
 'Your Instagram account was disabled and you are in Australia. The appeal, ID checks, ReportCyber for hacks, eSafety for abuse and what to avoid.',
 'Instagram disabled your account and you are in Australia?', 'Instagram disabled, Australia',
 'In Australia the in-app appeal is the main route. Government services help with hacks, scams and abuse, not with bans.',
 'If Instagram disabled your account in Australia, appeal once from the notice and complete any ID or video selfie check it asks for. If the account was hacked, report it through ReportCyber and warn your followers. If you are the target of serious online abuse, the eSafety Commissioner takes reports. None of them can reinstate an account.',
 [('Appeal once', 'From the notice, with accurate details.'), ('Hacked', 'Report it through ReportCyber.'), ('Abuse', 'The eSafety Commissioner takes reports.')],
 [S('Steps', IGSTEPS),
  S('Privacy, scams and abuse',
    'The Privacy Act lets you ask an organisation for the personal information it holds about you, and the OAIC takes privacy complaints. Scamwatch, run by the ACCC, collects scam reports. eSafety deals with serious online abuse and harmful content. These bodies record reports and can act within their own powers, but they do not review account bans.'),
  S('Related', 'See %s, %s and %s.' % (SUSP, IGID, A('/canada-australia-hacked-or-banned-account-where-to-report/', 'where to report in Canada and Australia'))),
 ],
 [NOPHONE, ('Can eSafety get my account back?', 'No. eSafety handles serious online abuse and harmful content. It does not review or reverse account bans.'), NEWACC],
 ['Instagram users in Australia after a ban.', 'Australian small businesses and creators.', 'Parents of teens in Australia.'], area='AU')

page('instagram-disabled-uae-what-to-do', 'igsusp', 'Instagram Disabled in the UAE: Your Options',
 'Your Instagram account was disabled and you are in the UAE. How to appeal, pass the ID check, report a hack to police and avoid recovery scams.',
 'Instagram disabled your account and you are in the UAE?', 'Instagram disabled, UAE',
 'From Dubai, Abu Dhabi or anywhere in the Emirates, the in-app appeal is the route. Here is how to give it the best chance.',
 'If Instagram disabled your account in the UAE, appeal once from the notice and complete any ID or video selfie check it asks for. A passport or a national ID card such as an Emirates ID works best when the name matches the account. If the account was hacked or used to scam people, report it to the police.',
 [('Appeal once', 'From the notice, with accurate details.'), ('Matching ID', 'Passport or Emirates ID, same name.'), ('Hacked', 'Report it to the police.')],
 [S('Steps', IGSTEPS),
  S('ID checks from the UAE',
    'If your profile uses a nickname, a business name or an Arabic spelling and your ID uses Latin letters, say so in the appeal so the names can be matched. Use one document and the same one each time you are asked.'),
  S('Hacks and recovery scams',
    'Dubai Police runs an online eCrime reporting platform. In the other emirates, report to your local police and keep the reference number. Be wary of anyone in your DMs who says they work with Meta or asks for your login and a fee in advance. Nobody can buy a reinstatement.'),
  S('Related', 'See %s, %s and %s.' % (A('/instagram-account-recovery-uae/', 'Instagram account recovery in the UAE'), A('/instagram-username-claim-uae/', 'username claims in the UAE'), NOBTN)),
 ],
 [NOPHONE, ('Can I write the appeal in Arabic?', 'Yes. Write in Arabic or English, whichever you are more comfortable with. Keep it short and factual.'),
  ('Does logging in from abroad cause problems?', 'Logins from several countries in a short time can trigger security checks. Appeal from your usual phone and connection.')],
 ['Instagram users in the UAE after a ban.', 'UAE businesses, shops and creators.', 'Residents and expats in the Emirates.'], area='AE')

page('instagram-no-appeal-button-eu-uk-routes', 'igappeal', 'No Appeal Button on Instagram: EU and UK Routes',
 'Instagram shows no appeal option and you live in the EU or UK. The statement of reasons, Appeals Centre Europe, UK data requests and what to try.',
 'No appeal button on Instagram and you live in Europe?', 'No appeal button, EU and UK',
 'When the button is missing, the app is not the only route. Where you live decides what else is open to you.',
 'If Instagram shows no appeal button and you live in the EU, find the decision in your email or Account Status and use the Digital Services Act routes: the internal complaint, then a certified dispute body such as Appeals Centre Europe. In the UK, a data subject access request can show what Meta holds about the account.',
 [('Find the decision', 'Email or Account Status.'), ('EU: dispute body', 'Appeals Centre Europe.'), ('UK: data request', 'Under UK GDPR.')],
 [S('Why the button disappears', ul(['The appeal window has closed.', 'An earlier appeal was already decided.', 'The account is linked to another account that was removed.', 'The app version or device does not show it. Try the latest app, then a browser.'])),
  S('In the EU', ol(['Find the decision email or the notice in Account Status. Under the DSA the platform has to give you a statement of reasons.',
                     'Use the complaint link in that notice or the help centre form. The DSA says the internal complaint route must stay open for at least six months after the decision.',
                     'If the complaint fails, or no route is offered, take the decision to %s.' % ACE,
                     'Keep dated screenshots of the screen with no button.'])),
  S('In the UK', 'The UK is outside the DSA. The main tool is a data subject access request under UK GDPR, which can show what Meta holds about the account. See %s. If the account was hacked, report it to Action Fraud in England, Wales and Northern Ireland, or to Police Scotland.' % A('/uk-gdpr-subject-access-request-meta-disabled-account/', 'UK GDPR subject access request')),
  S('Related', 'See %s, %s and %s.' % (NOBTN, A('/statement-of-reasons-dsa-account-ban/', 'the statement of reasons'), A('/instagram-disabled-uk-what-to-do/', 'Instagram disabled in the UK'))),
 ],
 [('Does the DSA force Instagram to restore my account?', 'No. A dispute body gives a decision the platform has to engage with in good faith, but it is not a court order.'),
  ('Can I use Appeals Centre Europe from the UK?', 'It handles disputes from people in the EU. If you live in the UK, use the UK routes above.'),
  ('What if the account was hacked first?', 'Say so clearly. Explain when it happened and what changed, and include any police reference number.')],
 ['People in the EU or UK with no appeal button.', 'Creators and businesses in Europe.', 'People whose appeal window has closed.'], area=['EU', 'GB'])

page('facebook-account-disabled-uk-what-to-do', 'fbdis', 'Facebook Disabled in the UK: Your Options',
 'Your Facebook account was disabled and you are in the UK. The appeal, the ID upload, a UK GDPR data request, Action Fraud for hacks and what to avoid.',
 'Facebook disabled your account and you are in the UK?', 'Facebook disabled, UK',
 'In the UK the appeal in the notice is the main route. Data rights and fraud reports sit alongside it.',
 'If Facebook disabled your account in the UK, appeal once from the notice and upload ID if asked, with the name on the profile. A UK GDPR subject access request can show what Meta holds about the account. If it was hacked or used for fraud, report it to Action Fraud or, in Scotland, to Police Scotland.',
 [('Appeal once', 'From the notice, with accurate details.'), ('Your data', 'A UK GDPR subject access request.'), ('Fraud reports', 'Action Fraud or Police Scotland.')],
 [S('Steps', FBSTEPS),
  S('If you run Pages or ads', 'A disabled profile can cut you off from your Pages and ad accounts. If there is no second admin, say in the appeal that the profile manages a business Page. See %s.' % A('/facebook-profile-disabled-managing-business-pages/', 'profile disabled while managing business Pages')),
  S('Related', 'See %s, %s and %s.' % (FBAPP, FBLOST, A('/uk-gdpr-subject-access-request-meta-disabled-account/', 'UK GDPR subject access request'))),
 ],
 [('Can I call Facebook?', 'Facebook does not offer phone support for disabled accounts. Numbers online that claim to be Facebook support are often scams.'),
  ('Can the ICO restore my account?', 'No. The ICO handles data protection complaints. It does not review bans.'),
  ('Will a new profile help?', 'Facebook allows one personal profile per person. A new one can be removed and can count against the appeal.')],
 ['Facebook users in the UK after a ban.', 'UK small businesses that run Pages.', 'Page and group admins.'], area='GB')

page('facebook-account-disabled-usa-what-to-do', 'fbdis', 'Facebook Disabled in the US: Your Options',
 'Your Facebook account was disabled and you are in the US. The appeal, the ID upload, Meta Verified support, IC3 and FTC reports and what to avoid.',
 'Facebook disabled your account and you are in the US?', 'Facebook disabled, US',
 'In the US the appeal in the notice is the main route. Federal agencies take fraud reports, not ban appeals.',
 'If Facebook disabled your account in the US, appeal once from the notice and upload ID if asked, with the name on the profile. If you have Meta Verified on a linked account, use its support. If it was hacked or used for fraud, report it to IC3 and the FTC. These agencies log complaints but do not restore accounts.',
 [('Appeal once', 'From the notice, with accurate details.'), ('Meta Verified', 'From a linked active account.'), ('Fraud reports', 'IC3 and the FTC.')],
 [S('Steps', FBSTEPS),
  S('If you run Pages or ads', 'A disabled profile can cut you off from your Pages and ad accounts. If there is no second admin, say in the appeal that the profile manages a business Page. See %s.' % A('/facebook-profile-disabled-managing-business-pages/', 'profile disabled while managing business Pages')),
  S('Related', 'See %s, %s and %s.' % (FBAPP, A('/ftc-and-state-attorney-general-complaint-meta-account/', 'FTC and state AG complaints'), A('/meta-verified-support-how-to-use/', 'Meta Verified support'))),
 ],
 [('Can I call Facebook?', 'Facebook does not offer phone support for disabled accounts. Numbers online that claim to be Facebook support are often scams.'),
  ('Can I sue Facebook?', 'Talk to a lawyer. Meta’s terms include rules on where disputes are heard.'),
  ('Will a new profile help?', 'Facebook allows one personal profile per person. A new one can be removed and can count against the appeal.')],
 ['Facebook users in the US after a ban.', 'US small businesses that run Pages.', 'Page and group admins.'], area='US')

def gulf_user(slug, country, the, office, cities, area):
    page(slug, 'user', 'Instagram Username Claim in %s' % country,
     'Claim the Instagram handle that matches your brand in %s. The routes that can work, the trade mark proof to have ready, and what does not count.' % country,
     'Instagram username claim in %s.' % the, 'Username claim, %s' % country,
     'You run a business in %s and the handle that matches your brand belongs to someone else. Here is how a claim works.' % the,
     'Instagram usernames cannot be bought. From %s, the routes that can work are Meta’s trade mark report for a registered mark, the impersonation report, recovery of a handle that was yours, or the platform’s own processes for abandoned accounts. A registered trade mark that matches the handle is the strongest proof.' % the,
     [('Registered trade mark', 'The strongest route, through Meta’s IP report.'), ('Impersonation', 'An account posing as your brand.'), ('A handle that was yours', 'Recovery usually comes first.')],
     [S('Proof to have ready', '%s handles trade mark registration. Have the certificate, the owner’s name and the class of goods or services ready. If the brand is registered in Arabic and in Latin letters, tell us which spelling matches the handle. A commercial registration shows the business exists, but it is not a trade mark.' % office),
      S('What does not give you a right to a handle', ul(['A commercial registration or licence on its own.', 'A domain name or a Google Business listing.', 'A handle that is an active account run by someone unrelated.'])),
      S('What we never do', ul(['Buy, sell or take over accounts. The handle goes onto your own profile.', 'File false or mass reports to free up a name.', 'Ask for your password or login codes.']),
        'Our %s explains what happens if a claim does not work. See also %s and %s.' % (A('/refund-policy/', 'refund policy'), A('/instagram-username-claim-uae/', 'username claims in the UAE'), A('/inactive-instagram-username/', 'inactive Instagram usernames'))),
     ],
     [('Does a commercial registration count?', 'It shows the business exists, but it is not a trade mark. On its own it is weak proof for a handle.'),
      ('What if my brand is an Arabic word?', 'Instagram handles use Latin letters, numbers, full stops and underscores. The claim has to match how your mark is written in Latin letters.'),
      ('Can I claim a handle someone is actively using?', 'Only if the account infringes your registered mark or impersonates you. A real, unrelated account using a common word keeps it.')],
     ['Brands and retailers in %s.' % the, 'Founders in %s.' % cities, 'Agencies managing brands in %s.' % the], area=area)

gulf_user('instagram-username-claim-saudi-arabia', 'Saudi Arabia', 'Saudi Arabia', 'The Saudi Authority for Intellectual Property (SAIP)', 'Riyadh, Jeddah and Dammam', 'SA')
gulf_user('instagram-username-claim-qatar', 'Qatar', 'Qatar', 'The Ministry of Commerce and Industry', 'Doha and Lusail', 'QA')
