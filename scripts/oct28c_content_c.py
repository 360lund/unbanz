# -*- coding: utf-8 -*-
"""2026-10-28 part C: username-claim pages for six countries and the country hub."""
import oct25_content as q
from oct25_content import A, sec, ul, how, who, WA_USER, USER_STEP1, RECOVER_WA
from oct28c_base import DATE
UPAGES = []

REFUND = lambda: sec('refund', 'Refund policy', '<p>If a username claim fails, you get a full 100% refund. A claim fails when the username is not successfully claimed onto your profile. The full wording is on our ' + A('/refund-policy/', 'refund policy') + ' page.</p>')

def up(slug, place, title, desc, hero, answer, routes_h, routes, reg_h, reg, notenough, extra, who_items, faq, relq):
    UPAGES.append(dict(
     slug=slug, lang='en', title=title, desc=desc,
     h1='Instagram username claim in %s.' % place, crumb='Username claim in %s' % place.replace('the ', ''),
     svc='Instagram username claim in %s' % place,
     hero=hero, wa=WA_USER, ws='username', subj='Username%20claim', answer=answer,
     body=[
      sec('routes', routes_h, ul(routes)),
      sec('register', reg_h, ul(reg)),
      sec('notenough', 'What does not give you a right to a handle', ul(notenough)) + extra,
      sec('never', 'What we never do', ul(['Buy, sell or take over accounts. The handle goes onto your own profile.', 'File false or mass reports to free up a name.', 'Ask for your password or login codes.'])),
      REFUND(),
      how(USER_STEP1, True),
      who(who_items)],
     faq=faq, related=[('/username/', 'All username claims'), ('/instagram-username-claim/', 'Instagram username claims'), ('/trademark-username-claim/', 'Trademark username claims'), ('/instagram-username-claim-refund/', 'Username claim refund'), ('/username-claim-pricing/', 'Username claim pricing'), ('/inactive-instagram-username/', 'Inactive usernames'), ('/instagram-username-claim-usa/', 'Username claim in the USA')],
     relq=relq))

REFUND_FAQ = ('What if the username claim fails?', 'You get a full 100% refund. A claim fails when the username is not successfully claimed onto your profile.')
PASS_FAQ = ('Do I need to share my Instagram password?', 'No. Your password and login codes stay with you.')
DECIDE_FAQ = ('Who decides whether the claim succeeds?', 'Instagram does. We pick the right official route, file it properly, and tell you upfront whether the handle looks doable.')
BUY_FAQ = ('Can I buy the handle from the current owner?', 'No. Buying or selling usernames breaks Instagram’s Terms of Use. The handle goes onto your own profile through official routes. Unbanz does not buy or sell accounts.')

# ------------------------------------------------------------------ UK
up('instagram-username-claim-uk', 'the UK',
 'Instagram Username Claim in the UK | Unbanz',
 'Want an Instagram handle that matches your UK business or trade mark? Official routes, what the UKIPO register shows, and a 100% refund if the claim fails.',
 'Your UK business has the name, the Companies House record and the website, but someone else has the Instagram handle. Here is how a claim works from the UK.',
 'Instagram usernames can’t be bought. From the UK, the routes that can work are Meta’s trade mark report for a registered mark, the impersonation report, recovery of a handle that was yours, or the platform’s processes for abandoned accounts. Unbanz files the claim; Instagram decides. If it fails, you get a 100% refund.',
 'Routes that can work from the UK',
 ['<strong>Registered trade mark:</strong> a UK registered trade mark that matches the handle is the strongest route, through Meta’s intellectual property report.',
  '<strong>Impersonation:</strong> an account posing as you or your business. Instagram’s impersonation report applies.',
  '<strong>Used to be yours:</strong> if you lost the handle in a hack or by mistake, recovery usually comes first.',
  '<strong>Inactive or abandoned account:</strong> there is no “inactive” button on Instagram, so the claim goes through the platform’s own processes.'],
 'Checking your UK trade mark',
 ['The UK Intellectual Property Office (UKIPO) keeps the register of UK trade marks, and you can search it on GOV.UK. Have the registration number, the owner and the classes of goods or services ready.',
  'An EU trade mark registered with EUIPO stopped covering the UK after the transition period ended on 31 December 2020. If your mark is only an EU mark, check how it relates to a UK right before you rely on it.',
  'A pending application is weaker than a registration, and the mark should be the same as, or very close to, the handle.'],
 ['A Companies House registration. A company name is not a trade mark.', 'A domain name on its own.', 'A handle that is an active account run by someone unrelated, such as a person who shares your name.'],
 '',
 ['UK founders, shops and agencies who hold a registered trade mark and want the matching handle.', 'People whose name sits on a dead or squatting account.', 'Not for: handles held by active, unrelated people.'],
 [('Can I claim an Instagram username from the UK?', 'Yes, through Instagram’s official routes: a registered trade mark, impersonation, recovery of a handle that used to be yours, or an abandoned account. Send us the handle and you hear upfront which route fits and whether it looks doable.'),
  ('Does a Companies House registration give me the handle?', 'No. Registering a company name does not give you a right to an Instagram handle. A registered trade mark that matches the handle is the strongest route.'),
  ('Is an EU trade mark enough for a UK claim?', 'Not on its own. EU trade marks registered with EUIPO no longer cover the UK, so check for a UK right. We can tell you what Meta’s form will need.'),
  BUY_FAQ, REFUND_FAQ, DECIDE_FAQ],
 [('/instagram-account-recovery-uk/', 'Instagram recovery in the UK'), ('/instagram-username-claim-germany/', 'Username claim in Germany')])

# ------------------------------------------------------------------ UAE
up('instagram-username-claim-uae', 'the UAE',
 'Instagram Username Claim in the UAE | Unbanz',
 'Want an Instagram handle that matches your UAE brand? Official routes, trade mark and licence checks, English and Arabic names, and a 100% refund if it fails.',
 'You run a licensed business in the UAE and the handle that matches your brand belongs to someone else. Here is how a claim works from Dubai, Abu Dhabi and the other emirates.',
 'Instagram usernames can’t be bought. From the UAE, the routes that can work are Meta’s trade mark report for a registered mark, the impersonation report, recovery of a handle that was yours, or the platform’s processes for abandoned accounts. Unbanz files the claim; Instagram decides. If it fails, you get a 100% refund.',
 'Routes that can work from the UAE',
 ['<strong>Registered trade mark:</strong> a trade mark registered in the UAE that matches the handle is the strongest route, through Meta’s intellectual property report.',
  '<strong>Impersonation:</strong> an account copying your brand, shop or name. Instagram’s impersonation report applies.',
  '<strong>Used to be yours:</strong> if the handle was lost in a hack, recovery usually comes first.',
  '<strong>Inactive or abandoned account:</strong> there is no “inactive” button, so the claim goes through the platform’s own processes.'],
 'Proof to have ready',
 ['The UAE Ministry of Economy runs trade mark registration. Have the certificate, the owner’s name and the class of goods or services ready.',
  'If your brand is written in Arabic and in Latin letters, tell us which spelling is registered. The handle has to match the mark closely.',
  'A trade licence from a mainland authority or a free zone shows your business exists, but it is not a trade mark.'],
 ['A trade licence or free zone registration on its own.', 'A domain name or a Google Business listing.', 'A handle that is an active account run by someone unrelated.'],
 '<p>Many UAE businesses build the brand first and register the mark later. If the handle matters to you, registering the mark early gives you something to show, and it helps on every platform.</p>',
 ['UAE brands, restaurants, salons, real estate firms and agencies that hold a registered trade mark.', 'Founders and creators in Dubai and Abu Dhabi whose name sits on a dead or squatting account.', 'Not for: handles held by active, unrelated people.'],
 [('Can I claim an Instagram username from the UAE?', 'Yes, through Instagram’s official routes: a registered trade mark, impersonation, recovery of a handle that used to be yours, or an abandoned account. Send us the handle and you hear upfront which route fits and whether it looks doable.'),
  ('Does a trade licence give me the handle?', 'No. A trade licence or free zone registration does not give you a right to an Instagram handle. A registered trade mark that matches the handle is the strongest route.'),
  ('My brand has an Arabic and an English name. Which one counts?', 'The handle uses Latin letters, so the registered Latin spelling of the mark matters most. Tell us what is registered and we will check it against the handle.'),
  BUY_FAQ, REFUND_FAQ, DECIDE_FAQ],
 [('/instagram-account-recovery-uae/', 'Instagram recovery in the UAE'), ('/instagram-username-claim-uk/', 'Username claim in the UK')])

# ------------------------------------------------------------------ AUSTRALIA
up('instagram-username-claim-australia', 'Australia',
 'Instagram Username Claim in Australia | Unbanz',
 'Want an Instagram handle that matches your Australian business? Official routes, IP Australia trade marks, why an ABN is not enough, and a refund.',
 'Your business name is registered and your ABN is active, but the matching Instagram handle belongs to someone else. Here is how a claim works from Australia.',
 'Instagram usernames can’t be bought. From Australia, the routes that can work are Meta’s trade mark report for a registered mark, the impersonation report, recovery of a handle that was yours, or the platform’s processes for abandoned accounts. Unbanz files the claim; Instagram decides. If it fails, you get a 100% refund.',
 'Routes that can work from Australia',
 ['<strong>Registered trade mark:</strong> an Australian registered trade mark that matches the handle is the strongest route, through Meta’s intellectual property report.',
  '<strong>Impersonation:</strong> an account posing as you or your business. Instagram’s impersonation report applies.',
  '<strong>Used to be yours:</strong> if you lost the handle in a hack or by mistake, recovery usually comes first.',
  '<strong>Inactive or abandoned account:</strong> there is no “inactive” button, so the claim goes through the platform’s own processes.'],
 'Checking your Australian trade mark',
 ['IP Australia keeps the Register of Trade Marks, and you can search it online. Have the trade mark number, the owner and the classes ready.',
  'A pending application is weaker than a registered mark, and the mark should be the same as, or very close to, the handle.',
  'If your mark is registered in another country, ask us what Meta’s form will need before you rely on it.'],
 ['An ABN or a business name registration. ASIC says registering a business name does not give you exclusive rights to it, and it does not create a trade mark.', 'A domain name on its own.', 'A handle that is an active account run by someone unrelated, such as a person who shares your name.'],
 '<p>Many Australian sole traders and small businesses start with a business name and add a trade mark later. If the handle is part of the brand, applying early gives you something to show.</p>',
 ['Australian founders, retailers, tradies and agencies who hold a registered trade mark and want the matching handle.', 'People whose name sits on a dead or squatting account.', 'Not for: handles held by active, unrelated people.'],
 [('Can I claim an Instagram username from Australia?', 'Yes, through Instagram’s official routes: a registered trade mark, impersonation, recovery of a handle that used to be yours, or an abandoned account. Send us the handle and you hear upfront which route fits and whether it looks doable.'),
  ('Does my ABN or business name give me the handle?', 'No. An ABN or a business name registration does not give you a right to an Instagram handle. A registered trade mark that matches the handle is the strongest route.'),
  ('Where do I find my trade mark number?', 'On your IP Australia certificate or in a search of the Register of Trade Marks. Send us the number and we check that it matches the handle.'),
  BUY_FAQ, REFUND_FAQ, DECIDE_FAQ],
 [('/instagram-account-recovery-australia/', 'Instagram recovery in Australia'), ('/instagram-username-claim-canada/', 'Username claim in Canada')])

# ------------------------------------------------------------------ CANADA
up('instagram-username-claim-canada', 'Canada',
 'Instagram Username Claim in Canada | Unbanz',
 'Want an Instagram handle that matches your Canadian brand? Official routes, CIPO trademarks, why incorporation is not enough, and a 100% refund if it fails.',
 'Your business is incorporated and your brand is in use, but the matching Instagram handle is held by someone else. Here is how a claim works from Canada.',
 'Instagram usernames can’t be bought. From Canada, the routes that can work are Meta’s trademark report for a registered mark, the impersonation report, recovery of a handle that was yours, or the platform’s processes for abandoned accounts. Unbanz files the claim; Instagram decides. If it fails, you get a 100% refund.',
 'Routes that can work from Canada',
 ['<strong>Registered trademark:</strong> a Canadian registered trademark that matches the handle is the strongest route, through Meta’s intellectual property report.',
  '<strong>Impersonation:</strong> an account posing as you or your business. Instagram’s impersonation report applies.',
  '<strong>Used to be yours:</strong> if you lost the handle in a hack or by mistake, recovery usually comes first.',
  '<strong>Inactive or abandoned account:</strong> there is no “inactive” button, so the claim goes through the platform’s own processes.'],
 'Checking your Canadian trademark',
 ['The Canadian Intellectual Property Office (CIPO) keeps the Canadian Trademarks Database, which you can search online. Have the application or registration number, the owner and the goods or services ready.',
  'Canadian brands are often in English and French. Tell us which wording is registered, because the handle has to match the mark closely.',
  'A pending application is weaker than a registration.'],
 ['Incorporation or a business name registration. A corporate name is not a trademark.', 'A domain name on its own.', 'A handle that is an active account run by someone unrelated, such as a person who shares your name.'],
 '',
 ['Canadian founders, retailers and agencies who hold a registered trademark and want the matching handle.', 'Creators whose name sits on a dead or squatting account.', 'Not for: handles held by active, unrelated people.'],
 [('Can I claim an Instagram username from Canada?', 'Yes, through Instagram’s official routes: a registered trademark, impersonation, recovery of a handle that used to be yours, or an abandoned account. Send us the handle and you hear upfront which route fits and whether it looks doable.'),
  ('Does incorporating my business give me the handle?', 'No. Incorporation does not give you a right to an Instagram handle. A registered trademark that matches the handle is the strongest route.'),
  ('My brand has a French and an English name. Which one matters?', 'The one that is registered, and it has to match the handle closely. Send us the registration and we check it against the handle.'),
  BUY_FAQ, REFUND_FAQ, DECIDE_FAQ],
 [('/instagram-account-recovery-canada/', 'Instagram recovery in Canada'), ('/instagram-username-claim-australia/', 'Username claim in Australia')])

# ------------------------------------------------------------------ GERMANY
up('instagram-username-claim-germany', 'Germany',
 'Instagram Username Claim in Germany | Unbanz',
 'Want an Instagram handle that matches your German brand? Official routes, DPMA and EU trade marks, why a Handelsregister entry is not enough, and a refund.',
 'Your GmbH or Einzelunternehmen is registered and the brand is in use, but someone else has the matching Instagram handle. Here is how a claim works from Germany.',
 'Instagram usernames can’t be bought. From Germany, the routes that can work are Meta’s trademark report for a registered mark, the impersonation report, recovery of a handle that was yours, or the platform’s processes for abandoned accounts. Unbanz files the claim; Instagram decides. If it fails, you get a 100% refund.',
 'Routes that can work from Germany',
 ['<strong>Registered trade mark:</strong> a German or EU trade mark that matches the handle is the strongest route, through Meta’s intellectual property report.',
  '<strong>Impersonation:</strong> an account posing as you or your business. Instagram’s impersonation report applies.',
  '<strong>Used to be yours:</strong> if you lost the handle in a hack or by mistake, recovery usually comes first.',
  '<strong>Inactive or abandoned account:</strong> there is no “inactive” button, so the claim goes through the platform’s own processes.'],
 'Checking your German or EU trade mark',
 ['The German Patent and Trade Mark Office (DPMA) keeps the register of German trade marks, searchable in DPMAregister. Have the registration number, the owner and the classes ready.',
  'An EU trade mark registered with EUIPO also covers Germany, and the EUIPO database is searchable online. Tell us which one you hold.',
  'A pending application is weaker than a registration, and the mark should be the same as, or very close to, the handle.'],
 ['An entry in the Handelsregister or a Gewerbeanmeldung. A company name is not a trade mark.', 'A domain name on its own.', 'A handle that is an active account run by someone unrelated, such as a person who shares your name.'],
 '<p>If you are an EU user, notices and replies may come in German. The routes are the same in German and English, and we work in English over WhatsApp or email.</p>',
 ['German founders, shops and agencies who hold a registered trade mark and want the matching handle.', 'Creators whose name sits on a dead or squatting account.', 'Not for: handles held by active, unrelated people.'],
 [('Can I claim an Instagram username from Germany?', 'Yes, through Instagram’s official routes: a registered trade mark, impersonation, recovery of a handle that used to be yours, or an abandoned account. Send us the handle and you hear upfront which route fits and whether it looks doable.'),
  ('Does a Handelsregister entry give me the handle?', 'No. A commercial register entry or a business registration does not give you a right to an Instagram handle. A registered trade mark that matches the handle is the strongest route.'),
  ('Does an EU trade mark count for a German claim?', 'Yes. An EU trade mark registered with EUIPO covers Germany. Send us the registration and we check it against the handle.'),
  BUY_FAQ, REFUND_FAQ, DECIDE_FAQ],
 [('/instagram-account-recovery-germany/', 'Instagram recovery in Germany'), ('/instagram-username-claim-switzerland/', 'Username claim in Switzerland')])

# ------------------------------------------------------------------ SWITZERLAND
up('instagram-username-claim-switzerland', 'Switzerland',
 'Instagram Username Claim in Switzerland | Unbanz',
 'Want an Instagram handle that matches your Swiss brand? Official routes, IPI trade marks on Swissreg, why a Zefix entry is not enough, and a refund if it fails.',
 'Your company is in the commercial register and the brand is in use, but the matching Instagram handle belongs to someone else. Here is how a claim works from Switzerland.',
 'Instagram usernames can’t be bought. From Switzerland, the routes that can work are Meta’s trademark report for a registered mark, the impersonation report, recovery of a handle that was yours, or the platform’s processes for abandoned accounts. Unbanz files the claim; Instagram decides. If it fails, you get a 100% refund.',
 'Routes that can work from Switzerland',
 ['<strong>Registered trade mark:</strong> a Swiss trade mark that matches the handle is the strongest route, through Meta’s intellectual property report.',
  '<strong>Impersonation:</strong> an account posing as you or your business. Instagram’s impersonation report applies.',
  '<strong>Used to be yours:</strong> if you lost the handle in a hack or by mistake, recovery usually comes first.',
  '<strong>Inactive or abandoned account:</strong> there is no “inactive” button, so the claim goes through the platform’s own processes.'],
 'Checking your Swiss trade mark',
 ['The Swiss Federal Institute of Intellectual Property (IPI, or IGE in German) keeps the Swiss trade mark register, searchable on Swissreg. Have the registration number, the owner and the classes ready.',
  'Switzerland and Liechtenstein form a single trade mark territory, so a Swiss mark also covers Liechtenstein.',
  'Swiss brands are often written in German, French, Italian or English. Tell us which wording is registered, because the handle has to match the mark closely.'],
 ['A commercial register entry on Zefix. A company name is not a trade mark.', 'A domain name on its own.', 'A handle that is an active account run by someone unrelated, such as a person who shares your name.'],
 '',
 ['Swiss founders, shops, hospitality and watch or finance brands that hold a registered trade mark and want the matching handle.', 'Creators whose name sits on a dead or squatting account.', 'Not for: handles held by active, unrelated people.'],
 [('Can I claim an Instagram username from Switzerland?', 'Yes, through Instagram’s official routes: a registered trade mark, impersonation, recovery of a handle that used to be yours, or an abandoned account. Send us the handle and you hear upfront which route fits and whether it looks doable.'),
  ('Does a Zefix entry give me the handle?', 'No. A commercial register entry does not give you a right to an Instagram handle. A registered trade mark that matches the handle is the strongest route.'),
  ('Does my Swiss trade mark cover Liechtenstein?', 'Yes. Switzerland and Liechtenstein form one trade mark territory, so a Swiss mark also covers Liechtenstein.'),
  BUY_FAQ, REFUND_FAQ, DECIDE_FAQ],
 [('/instagram-account-recovery-switzerland/', 'Instagram recovery in Switzerland'), ('/instagram-username-claim-germany/', 'Username claim in Germany')])

# ------------------------------------------------------------------ HUB
def L(slug, label): return '<li>' + A('/%s/' % slug, label) + '</li>'
def IGL(k, v): return L('instagram-account-recovery-' + k, v)
def BOTH(k, v): return '<li>%s: %s, %s</li>' % (v, A('/instagram-account-recovery-%s/' % k, 'Instagram'), A('/facebook-account-recovery-%s/' % k, 'Facebook'))
def IGONLY(k, v): return '<li>%s: %s</li>' % (v, A('/instagram-account-recovery-%s/' % k, 'Instagram'))
def region(id_, h, items): return sec(id_, h, '<ul>' + ''.join(items) + '</ul>')
HUB = dict(
 slug='account-recovery-by-country', lang='en',
 title='Instagram and Facebook Recovery by Country | Unbanz',
 desc='Country guides for Instagram and Facebook account recovery: local phone formats, police and cyber bodies, privacy regulators, and official appeal steps.',
 h1='Instagram and Facebook account recovery by country.', crumb='Recovery by country', svc='Account recovery by country',
 hero='The official recovery steps are the same everywhere, but the phone formats, police reporting routes and consumer rights are not. Pick your country for the local details.',
 wa=RECOVER_WA, ws='unban', subj='Instagram%20account%20recovery',
 answer='Instagram and Facebook account recovery follows the same official routes in every country: a review on a disabled or suspended notice, or the hacked-account tools for a takeover. What changes is local: phone number formats, where to report fraud, and any appeal rights. Unbanz helps you appeal through Meta’s official process; Meta makes the final decision.',
 body=[
  sec('how', 'What is the same in every country', ul(['A disabled or suspended notice has a review or disagree option, and the time to use it is shown on the notice.', 'A hacked account goes through instagram.com/hacked or facebook.com/hacked, on a device you have used before.', 'The email and phone on the account decide how recovery goes, so replace a lost SIM before anything else.', 'Meta makes the final decision on every appeal.'])),
  region('europe', 'Europe', [IGONLY('uk', 'United Kingdom'), BOTH('netherlands', 'Netherlands'), BOTH('belgium', 'Belgium'), BOTH('luxembourg', 'Luxembourg'), BOTH('finland', 'Finland'), BOTH('italy', 'Italy'), BOTH('spain', 'Spain'), BOTH('france', 'France'), IGONLY('ireland', 'Ireland'), IGONLY('germany', 'Germany'), IGONLY('austria', 'Austria'), IGONLY('switzerland', 'Switzerland'), IGONLY('norway', 'Norway'), IGONLY('sweden', 'Sweden'), IGONLY('denmark', 'Denmark'), IGONLY('iceland', 'Iceland'), IGONLY('portugal', 'Portugal'), IGONLY('malta', 'Malta'), IGONLY('cyprus', 'Cyprus'), IGONLY('monaco', 'Monaco'), IGONLY('liechtenstein', 'Liechtenstein'), IGONLY('czech-republic', 'Czech Republic'), IGONLY('poland', 'Poland'), IGONLY('estonia', 'Estonia'), IGONLY('slovenia', 'Slovenia')]),
  region('americas', 'North America and Oceania', [IGL('usa', 'Instagram recovery in the USA'), BOTH('canada', 'Canada'), BOTH('australia', 'Australia'), IGONLY('new-zealand', 'New Zealand')]),
  region('mideast', 'Middle East', [IGL('uae', 'Instagram recovery in the UAE'), BOTH('israel', 'Israel'), BOTH('kuwait', 'Kuwait'), IGONLY('qatar', 'Qatar'), IGONLY('saudi-arabia', 'Saudi Arabia'), IGONLY('bahrain', 'Bahrain'), IGONLY('oman', 'Oman')]),
  region('asia', 'Asia', [BOTH('south-korea', 'South Korea'), BOTH('hong-kong', 'Hong Kong'), IGONLY('japan', 'Japan'), IGONLY('singapore', 'Singapore'), IGONLY('taiwan', 'Taiwan')]),
  region('username', 'Username claims by country', [L('instagram-username-claim-usa', 'USA'), L('instagram-username-claim-uk', 'United Kingdom'), L('instagram-username-claim-uae', 'UAE'), L('instagram-username-claim-australia', 'Australia'), L('instagram-username-claim-canada', 'Canada'), L('instagram-username-claim-germany', 'Germany'), L('instagram-username-claim-switzerland', 'Switzerland')]),
  how(q.ACCT_STEP1),
  who(['Anyone whose Instagram or Facebook account was disabled, suspended or hacked, wherever they live.', 'Businesses, creators and agencies that need a clean appeal.', 'Not for: accounts that were really used for scams or abuse.']),
 ],
 faq=[
  ('Do the recovery steps differ by country?', 'The official steps in the app are the same. What differs is local: phone number formats, where to report fraud or blackmail, and any appeal rights that depend on local law, such as those for EU users.'),
  ('Is my country not on the list?', 'Send us a message anyway. The appeal runs through the same official process, and we tell you upfront whether we can help.'),
  ('Do the country pages promise a result?', 'No. Meta makes the final decision on every appeal. We tell you upfront whether we think it is doable.'),
  ('Do I need to share my password?', 'No. Your password and login codes stay with you.'),
  ('How do I contact Unbanz?', 'WhatsApp +1 934 201 2490 or team@unbanz.com.')],
 related=[('/instagram-account-recovery/', 'Instagram account recovery'), ('/facebook-account-recovery/', 'Facebook account recovery'), ('/instagram-hacked-account-recovery-service/', 'Hacked Instagram recovery'), ('/instagram-account-disabled-appeal/', 'Instagram disabled appeal'), ('/guides/', 'Guides')],
 relq=[('/instagram-account-recovery-uk/', 'Recovery in the UK'), ('/instagram-account-recovery-uae/', 'Recovery in the UAE')])
