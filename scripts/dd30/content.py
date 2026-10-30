# -*- coding: utf-8 -*-
"""2026-10-30 double-down: pages around the topics that brought real high-value visitors and leads
(Instagram recovery in the Gulf and Switzerland, inactive usernames, Snapchat locks, Facebook recovery by country, username claims by country)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dd29'))
from fams import *
def C(*n): return [{'@type': 'Country', 'name': x} for x in n]
LEG = '/your-rights-when-meta-disables-your-account/'

# ---------------- country facts (only well-established public bodies) ----------------
K = {
 'uae': dict(n='the UAE', N='UAE', c='United Arab Emirates', police='Dubai Police eCrime platform (ecrime.ae) or Abu Dhabi Police through its Aman service', tm='the UAE Ministry of Economy trademark register', data='the UAE’s federal data protection law', lang='English or Arabic'),
 'saudi-arabia': dict(n='Saudi Arabia', N='Saudi Arabia', c='Saudi Arabia', police='the Kollona Amn app run by the Ministry of Interior', tm='the Saudi Authority for Intellectual Property (SAIP)', data='the Saudi Personal Data Protection Law', lang='Arabic or English'),
 'qatar': dict(n='Qatar', N='Qatar', c='Qatar', police='the Ministry of Interior’s cybercrime department, which you can reach through the Metrash app', tm='the Ministry of Commerce and Industry trademark office', data='Qatar’s personal data privacy law (Law 13 of 2016)', lang='Arabic or English'),
 'kuwait': dict(n='Kuwait', N='Kuwait', c='Kuwait', police='the Ministry of Interior’s cybercrime department', tm='the Ministry of Commerce and Industry trademark office', data=None, lang='Arabic or English'),
 'switzerland': dict(n='Switzerland', N='Switzerland', c='Switzerland', police='the Federal Office for Cyber Security report form and your cantonal police', tm='the Swiss Federal Institute of Intellectual Property (IPI)', data='the Swiss Federal Act on Data Protection', lang='German, French, Italian or English'),
 'germany': dict(n='Germany', N='Germany', c='Germany', police='the online police report service (Onlinewache) of your federal state', tm='the German Patent and Trade Mark Office (DPMA) or the EUIPO', data='the GDPR', lang='German or English', eu=True),
 'ireland': dict(n='Ireland', N='Ireland', c='Ireland', police='your local Garda station', tm='the Intellectual Property Office of Ireland or the EUIPO', data='the GDPR; the Data Protection Commission in Dublin is Meta’s lead EU regulator', lang='English', eu=True),
 'uk': dict(n='the UK', N='UK', c='United Kingdom', police='Action Fraud (England, Wales and Northern Ireland) or Police Scotland', tm='the UK Intellectual Property Office', data='UK GDPR; the ICO handles complaints', lang='English'),
 'usa': dict(n='the US', N='USA', c='United States', police='the FTC at ReportFraud.ftc.gov and the FBI’s IC3 if money was taken', tm='the USPTO', data=None, lang='English'),
 'singapore': dict(n='Singapore', N='Singapore', c='Singapore', police='the Singapore Police Force e-services', tm='IPOS, the Intellectual Property Office of Singapore', data='the PDPA', lang='English'),
 'new-zealand': dict(n='New Zealand', N='New Zealand', c='New Zealand', police='Netsafe, and the police if money or threats are involved', tm='IPONZ', data='the Privacy Act 2020', lang='English'),
 'canada': dict(n='Canada', N='Canada', c='Canada', police='the Canadian Anti-Fraud Centre and your local police', tm='the Canadian Intellectual Property Office (CIPO)', data=None, lang='English or French'),
 'australia': dict(n='Australia', N='Australia', c='Australia', police='ReportCyber and Scamwatch', tm='IP Australia', data=None, lang='English'),
 'austria': dict(n='Austria', N='Austria', c='Austria', tm='the Austrian Patent Office or the EUIPO', lang='German or English', eu=True),
 'belgium': dict(n='Belgium', N='Belgium', c='Belgium', tm='the Benelux Office for Intellectual Property (BOIP) or the EUIPO', lang='Dutch, French or English', eu=True),
 'denmark': dict(n='Denmark', N='Denmark', c='Denmark', tm='the Danish Patent and Trademark Office or the EUIPO', lang='Danish or English', eu=True),
 'norway': dict(n='Norway', N='Norway', c='Norway', tm='the Norwegian Industrial Property Office (Patentstyret)', lang='Norwegian or English'),
 'italy': dict(n='Italy', N='Italy', c='Italy', tm='the Italian Patent and Trademark Office (UIBM) or the EUIPO', lang='Italian or English', eu=True),
 'spain': dict(n='Spain', N='Spain', c='Spain', tm='the Spanish Patent and Trademark Office (OEPM) or the EUIPO', lang='Spanish or English', eu=True),
 'finland': dict(n='Finland', N='Finland', c='Finland', tm='the Finnish Patent and Registration Office (PRH) or the EUIPO', lang='Finnish, Swedish or English', eu=True),
}
def EU(k): return ('People in %s can also take a final Instagram or Facebook decision to a certified out-of-court dispute body such as Appeals Centre Europe, under the EU Digital Services Act. See %s.' % (K[k]['n'], A(LEG, 'your rights when an account is banned'))) if K[k].get('eu') else None
def P(*xs): return [x for x in xs if x]

# ---------------- A. Instagram recovery and disabled accounts: Gulf and Switzerland ----------------
def ig_country(slug, k, kind, place=None):
    d = K[k]; where = place or d['n']; W = place or d['N']
    if kind == 'hacked':
        title = 'Instagram Hacked in %s: Recovery Steps' % W
        h1 = 'Instagram account hacked in %s?' % where
        crumb = 'Instagram hacked in %s' % W
        desc = 'Your Instagram was hacked in %s. The recovery steps that work, where to report it locally, and what to do if the email and phone were changed.' % where
        hero = 'Start with Instagram’s own recovery, then report it locally if money or threats are involved.'
        ans = ('If your Instagram was hacked in %s, open Instagram’s hacked-account page on your usual phone and follow its steps. '
               'Look for an email from Instagram’s security team that lets you undo an email change. '
               'If money was taken or you are being threatened, report it to %s.') % (where, d['police'].split(',')[0])
        fam_ = 'ighacked'
        cards = [('Use the hacked-account page', 'The official start point for hacked accounts.'), ('Check the undo email', 'Instagram emails the old address when it changes.'), ('Report locally', 'If money or threats are involved.')]
        secs = [S('First steps', ol(['Search your inbox and spam for an email from Instagram’s security team about an email or password change. If it has a link to revert the change, use it.',
                    'Open Instagram’s hacked-account page on the phone and Wi-Fi you normally use, and choose the option that matches what you can still access.',
                    'If Instagram offers a video selfie check, do it in good light. It compares your face with photos on the account.',
                    'Secure your email account first if that was taken too. Instagram recovery goes to that inbox.'])),
                S('If the hacker is messaging your followers', 'Ask friends and customers through another channel not to send money or codes to the account. Ask a few of them to report the account as hacked from its profile menu. Do not pay anyone who contacts you offering to get it back.'),
                S('Reporting in %s' % W, 'For fraud, extortion or money taken, report to %s. Keep screenshots of messages, payment receipts and the date you lost access. Police reports do not unlock the account, but they help if a bank or Meta asks what happened.' % d['police'])]
        faq = [('Can Instagram support in %s help me by phone?' % W, 'Instagram does not offer a phone line for account recovery. The routes are in the app, on the hacked-account page and through Accounts Center.'),
               ('The hacker turned on two-factor login. Is it over?', 'Not necessarily. The hacked-account flow and the video selfie check are built for this situation. Use the device you normally log in from.'),
               ('Should I make a new account?', 'Wait until the recovery steps are exhausted. A new account does not stop the hacker using the old one.')]
        who = ['People in %s whose Instagram email, phone or password was changed by someone else.' % where, 'Businesses whose account is being used to message customers.', 'Anyone being asked for money to get their account back.']
    elif kind == 'disabled':
        title = 'Instagram Disabled in %s: What to Do' % W
        h1 = 'Instagram account disabled in %s?' % where
        crumb = 'Instagram disabled in %s' % W
        desc = 'Instagram disabled or suspended your account in %s. How to read the notice, appeal properly and protect your business while you wait.' % where
        hero = 'One careful appeal from the notice matters more than anything else you do this week.'
        ans = ('If Instagram disabled your account in %s, appeal from the notice itself, once, before the deadline it shows. '
               'Complete any ID or video selfie request carefully. Do not open new accounts on the same phone, because linked accounts are often removed too. '
               'Save every notice with its date.') % where
        fam_ = 'igsusp'
        cards = [('Appeal from the notice', 'Use the button on the suspension screen.'), ('No new accounts', 'They tend to be removed with the first.'), ('Keep records', 'Dates and screenshots help later.')]
        secs = [S('Read the notice first', 'The notice names the rule Instagram says was broken and usually shows how long you have to disagree. Write both down. A suspension with an appeal button and a final “disabled” decision without one need different next steps; see %s.' % A('/instagram-account-disabled-vs-suspended-vs-restricted/', 'disabled vs suspended vs restricted')),
                S('Appealing from %s' % W, ol(['Appeal from the phone you normally use, ideally on your usual connection rather than a VPN.',
                    'Write in %s, plainly: who you are, what the account is for, and why the decision looks wrong.' % d['lang'],
                    'If asked for ID, use a government document where the name matches the account owner.',
                    'If the linked Facebook profile is restricted in Accounts Center, deal with that too, as it can block the Instagram appeal.'])),
                S('If the account is your business', 'Tell customers on your website, WhatsApp Business or email how to reach you. Pause any ads tied to the account in Ads Manager. %s' % ('You can also ask Meta for a copy of the data it holds on you under %s.' % d['data'] if d.get('data') else ''))]
        faq = [('Is there an Instagram office in %s I can visit?' % W, 'Meta does not handle individual account appeals in person. Appeals go through the app, the notice and Accounts Center.'),
               ('Does using a VPN cause suspensions?', 'Logging in from unusual locations can trigger security checks. It is better to appeal from your normal connection.'),
               ('What if there is no appeal button?', 'Then the decision may be final on Instagram’s side. Check whether you have any other route, such as a data request, before giving up.')]
        who = ['Personal and business accounts in %s that were suspended or disabled.' % where, 'Shops and service businesses that take orders through Instagram.', 'Anyone whose appeal deadline is running.']
    else:  # recovery hub-style for a city/business
        title = 'Instagram Account Recovery %s' % W
        h1 = 'Instagram account recovery in %s' % where
        crumb = 'Instagram recovery %s' % W
        desc = 'Locked out, hacked or disabled on Instagram in %s? Which official route fits your situation and how Unbanz can help you prepare it.' % where
        hero = 'Locked out, hacked or disabled: each one has a different official route. Here is how to tell which one you need.'
        ans = ('Instagram account recovery in %s uses the same official routes as everywhere else: Instagram’s hacked-account page for hacked accounts, the login help flow for lost passwords and codes, '
               'and the appeal on the notice for suspended or disabled accounts. The right one depends on the exact message you see.') % where
        fam_ = 'igrecov'
        cards = [('Hacked', 'Start at the hacked-account page.'), ('Lost access', 'Use “Forgot password” and the login help flow.'), ('Disabled', 'Appeal from the notice itself.')]
        secs = [S('Which situation are you in?', ul(['Someone else changed your email, phone or password: see %s.' % A('/instagram-hacked-uae-what-to-do/', 'Instagram hacked in the UAE'),
                    'You lost the phone number or email on the account: see %s.' % A('/guides/instagram-lost-access-to-email-or-phone/', 'lost access to email or phone'),
                    'Instagram suspended or disabled the account: see %s.' % A('/instagram-disabled-uae-what-to-do/', 'Instagram disabled in the UAE')])),
                S('Local points worth knowing', 'Many people in %s use a phone number from another country or travel often. Logging in from a new country can trigger security checks, so recover from the phone and network you normally use. For fraud or extortion, report to %s.' % (where, d['police'])),
                S('Business accounts', 'If the account sells or takes bookings, keep customers informed through WhatsApp Business, your website or email while you recover it, and pause any ads linked to it.')]
        faq = [('Does it matter which emirate I am in?', 'Not for Instagram. The routes are the same; only the local police service for reporting fraud differs.'),
               ('Can I recover an account opened with an old UAE number?', 'Often, yes, if you still have the email on the account or can pass the video selfie check. Tell us what you still have.'),
               ('Is Arabic fine for the appeal?', 'Yes. Write in the language you are most comfortable with and keep it short and factual.')]
        who = ['Residents and businesses in %s locked out of Instagram.' % where, 'Expats whose account is tied to a number from home.', 'Shops and creators whose account brings in work.']
    return dict(slug=slug, f=fam_, title=title, desc=desc, h1=h1, crumb=crumb, hero=hero, answer=ans, cards=cards, sections=secs, faq=faq, who=who, area=C(d['c']))

IGA = [ig_country('instagram-account-recovery-dubai', 'uae', 'recov', 'Dubai'),
       ig_country('instagram-account-recovery-abu-dhabi', 'uae', 'recov', 'Abu Dhabi'),
       ig_country('instagram-hacked-uae-what-to-do', 'uae', 'hacked'),
       ig_country('instagram-hacked-saudi-arabia-what-to-do', 'saudi-arabia', 'hacked'),
       ig_country('instagram-disabled-saudi-arabia-what-to-do', 'saudi-arabia', 'disabled'),
       ig_country('instagram-disabled-qatar-what-to-do', 'qatar', 'disabled'),
       ig_country('instagram-disabled-kuwait-what-to-do', 'kuwait', 'disabled'),
       ig_country('instagram-hacked-switzerland-what-to-do', 'switzerland', 'hacked'),
       ig_country('instagram-disabled-switzerland-what-to-do', 'switzerland', 'disabled')]

# ---------------- B. Inactive Instagram usernames ----------------
def inactive_country(k):
    d = K[k]; W = d['N']
    return dict(slug='inactive-instagram-username-%s' % k, f='user', title='Inactive Instagram Username in %s: Your Options' % W,
      desc='The Instagram username you want in %s belongs to an inactive account. What Instagram allows, the trademark route, and what to avoid.' % d['n'],
      h1='Want an inactive Instagram username in %s?' % d['n'], crumb='Inactive username %s' % W,
      hero='An inactive account does not release its name by itself. These are the routes that are actually open.',
      answer=('Instagram does not hand over a username just because the account looks inactive. The account holder keeps it unless Instagram removes the account or releases the name. '
              'If the name matches a trademark registered with %s, Instagram’s trademark report is the strongest route.') % d['tm'],
      cards=[('Inactive is not abandoned', 'The holder still owns the name.'), ('Trademark route', 'Registered marks carry the most weight.'), ('No account buying', 'It breaks Instagram’s terms.')],
      sections=P(S('What Instagram allows', 'Instagram’s terms let it reclaim usernames, but it does not run a public request form for inactive names. In practice a name opens up when the account is deleted or removed, or when Instagram acts on a trademark or impersonation report.'),
        S('The trademark route in %s' % W, 'If you hold a registered mark with %s that matches the handle, you can file Instagram’s trademark report. The report is stronger when the inactive account uses the name in a way that could confuse people. A business name alone, without a registration, carries less weight.' % d['tm']),
        S('What to avoid', ul(['Paying the account holder or a seller for the login. Buying accounts breaks Instagram’s terms and the account can be removed with your money.', 'Mass reporting the account. It does not work and can count against you.', 'Anyone promising a date. Instagram decides when, and whether, a name is released.']))),
      faq=[('How long must an account be inactive before I can claim the name?', 'Instagram does not publish a time limit. Inactivity alone does not release a name.'),
           ('Can I use a trademark from another country?', 'A registered mark anywhere can help, but one registered where you trade, here %s, is easier to explain.' % d['n']),
           ('What if the name has no posts and no profile photo?', 'It may still be logged into. Empty profiles are often kept on purpose for the name.')],
      who=['Brands and businesses in %s whose name is held by a dormant account.' % d['n'], 'Founders who registered a trademark and want the matching handle.', 'Creators who want a cleaner handle and want to stay within the rules.'],
      area=C(d['c']))
IGB = [inactive_country(k) for k in ('uk', 'usa', 'canada', 'australia', 'germany', 'uae')]
IGB.append(dict(slug='how-to-tell-if-an-instagram-account-is-inactive', f='user', title='How to Tell if an Instagram Account Is Inactive',
  desc='Signs that an Instagram account is inactive, what they do and do not prove, and what that means if you want its username.',
  h1='Is that Instagram account really inactive?', crumb='Is the account inactive?',
  hero='Old posts do not mean nobody logs in. Here is what you can and cannot tell from the outside.',
  answer=('You cannot know for sure from outside. An account with no posts for years, no profile photo and no recent story highlights may still be logged into, used for messages or kept for its name. '
          'Treat these as signs, not proof, and plan the claim around a trademark or a rule Instagram enforces.'),
  cards=[('Signs, not proof', 'Last post dates say little about logins.'), ('Private accounts', 'You see even less.'), ('Plan for the rules', 'Trademark and impersonation routes.')],
  sections=[S('Signs people look at', ul(['The date of the last post or reel.', 'Whether it has a profile photo, bio or link.', 'Follower and following counts that never change.', 'Whether the name was used years ago and then left.'])),
    S('What they do not tell you', 'None of these show logins or direct messages. Many people keep a dormant handle on purpose. That is why Instagram does not release names on inactivity alone.'),
    S('What to do next', 'If the handle matches your registered trademark, read %s. If you only want the name, look at close variants first and read %s.' % (A('/trademark-username-claim/', 'trademark username claims'), A('/inactive-instagram-username/', 'inactive Instagram usernames')))],
  faq=[('Does Instagram delete inactive accounts?', 'Instagram says it may remove accounts that are inactive, but it does not publish a schedule.'),
       ('Can I message the owner?', 'You can ask whether they still use it. Do not pay for the login; buying accounts breaks the terms.'),
       ('Does reporting an inactive account help?', 'Not unless it breaks a rule, such as impersonating your brand.')],
  who=['Anyone looking at a dormant handle they want.', 'Brands checking whether a name is worth pursuing.', 'People comparing a claim with picking a variant.'], area=None))
IGB.append(dict(slug='inactive-instagram-username-for-a-business-name', f='user', title='Inactive Account Using Your Business Name on Instagram',
  desc='A dormant Instagram account holds your business name. When Instagram can act, what proof helps, and what to do before you file.',
  h1='A dormant account holds your business name?', crumb='Business name held by inactive account',
  hero='Your company name is taken by an account that never posts. Whether you can get it depends on what you can prove.',
  answer=('If an inactive Instagram account holds your business name, Instagram can act when the name matches your registered trademark or the account impersonates your business. '
          'A company registration alone is weaker. Gather the trademark certificate, your website and proof you trade under the name before you file.'),
  cards=[('Registered mark', 'The strongest basis for a request.'), ('Impersonation', 'If it pretends to be you.'), ('Proof of trading', 'Website, invoices, other socials.')],
  sections=[S('What helps', ul(['A registered trademark that matches the handle exactly.', 'Your website and email domain using the same name.', 'Other social accounts in the same name.', 'Evidence that people confuse the dormant account with you, if any.'])),
    S('If you have no trademark yet', 'Consider filing one where you trade. In the meantime, pick a clear variant such as adding your city or “hq”, and keep it consistent everywhere. See %s.' % A('/instagram-username-claim-with-uk-or-eu-trademark/', 'claims with a UK or EU trademark')),
    S('Where this fits', 'This is a username claim, not an account recovery. Unbanz checks the handle and the route before anything starts. Terms are agreed with you before any work starts.')],
  faq=[('Is a company registration enough?', 'Usually not on its own. Instagram looks for a registered trademark or a clear rule breach.'),
       ('Will the inactive account be told?', 'Instagram may contact the account holder as part of its process.'),
       ('What if the account is a fan page?', 'See our page on usernames taken by fan pages.')],
  who=['Companies whose name is held by a dormant account.', 'Startups preparing a launch.', 'Agencies handling a client’s brand name.'], area=None))

# ---------------- C. Snapchat locks ----------------
def snap_country(k):
    d = K[k]; W = d['N']
    return dict(slug='snapchat-account-locked-%s' % k, f='snap', title='Snapchat Account Locked in %s: What to Do' % W,
      desc='Snapchat locked or banned your account in %s. How to tell a temporary lock from a permanent one and which official route to use.' % d['n'],
      h1='Snapchat account locked in %s?' % d['n'], crumb='Snapchat locked %s' % W,
      hero='Snapchat is how a lot of people here keep in touch. Here is how to tell what kind of lock you have and what to do.',
      answer=('If Snapchat locked your account in %s, first check whether the lock is temporary or permanent at accounts.snapchat.com. '
              'A temporary lock shows an unlock option once it is available. A permanent ban needs a request to Snapchat Support. Remove any third-party apps or tweaks first.') % d['n'],
      cards=[('Check the lock type', 'At accounts.snapchat.com.'), ('Remove add-ons', 'Third-party apps and tweaks cause locks.'), ('Use Snapchat Support', 'For permanent bans.')],
      sections=P(S('Temporary or permanent?', 'Log in at accounts.snapchat.com from a browser. If it shows an Unlock option, the lock is temporary. If it says the account is permanently locked for breaking the Community Guidelines, you need to contact Snapchat Support through help.snapchat.com.'),
        S('Common causes we see from %s' % W, ul(['Unofficial Snapchat versions or apps that save snaps or add features.', 'Adding many people in a short time, for example after sharing your username in groups.', 'Logging in from a new phone or a VPN, or while travelling.', 'Reports from other users.'])),
        S('If someone else got into it', 'If your email or phone was changed by someone else, use the hacked-account steps, not the unlock flow. See %s. For extortion or threats, report to %s.' % (A('/guides/snapchat-account-hacked/', 'Snapchat account hacked'), d.get('police', 'the police')))),
      faq=[('Will deleting the app unlock it?', 'No. Reinstalling does not change the lock on the account.'),
           ('Can I write to Snapchat Support in %s?' % d['lang'].split(' or ')[0], 'Snapchat Support is reached through help.snapchat.com. Write clearly and keep it short; English is the safest choice.' if d['lang'] != 'English' else 'Yes. Snapchat Support is reached through help.snapchat.com.'),
           ('What about Snapchat+ or memories?', 'Memories are tied to the account. If it comes back, they usually come back with it.')],
      who=['Snapchat users in %s with a locked or banned account.' % d['n'], 'People who lost access after changing phones or travelling.', 'Creators and businesses with a public profile on Snapchat.'],
      area=C(d['c']))
IGC = [snap_country(k) for k in ('saudi-arabia', 'uae', 'kuwait', 'qatar', 'uk', 'australia')]
IGC.append(dict(slug='snapchat-hacked-saudi-arabia-what-to-do', f='snap', title='Snapchat Hacked in Saudi Arabia: What to Do',
  desc='Someone took over your Snapchat in Saudi Arabia. The recovery steps, how to protect your contacts, and where to report blackmail.',
  h1='Snapchat hacked in Saudi Arabia?', crumb='Snapchat hacked Saudi Arabia',
  hero='Recover the account through Snapchat’s own steps, and report any blackmail straight away.',
  answer=('If your Snapchat was hacked in Saudi Arabia, try “Forgot password” with your phone or email, then contact Snapchat Support at help.snapchat.com if the details were changed. '
          'Warn your contacts through another app. If someone threatens to share private photos, report it through the Kollona Amn app.'),
  cards=[('Reset if you can', 'Forgot password, by phone or email.'), ('Snapchat Support', 'If the details were changed.'), ('Report blackmail', 'Kollona Amn app.')],
  sections=[S('Steps in order', ol(['Try “Forgot password” in the app using your phone number, then your email.', 'Check your email for a message from Snapchat about a changed email or phone.', 'If you cannot get in, use the “My account was hacked” option at help.snapchat.com.', 'Once back in, turn on two-factor login and remove unknown devices.'])),
    S('If you are being blackmailed', 'Do not pay and do not keep talking to the person. Save the messages and usernames, and report it through %s. This is the official channel for reporting cybercrime in Saudi Arabia.' % K['saudi-arabia']['police']),
    S('More help', 'See %s and %s.' % (A('/snapchat-hacked-account-locked-by-hacker/', 'Snapchat locked by a hacker'), A('/snapchat-hacked-no-access-to-email-or-phone/', 'hacked with no access to email or phone')))],
  faq=[('Can the hacker see my memories?', 'Anyone logged in can see memories that are not in My Eyes Only. Recover the account first.'),
       ('Should I make a new account?', 'Not yet. The hacker can keep using the old one to message your friends.'),
       ('Is reporting to the police worth it?', 'For blackmail or fraud, yes. Keep everything as evidence.')],
  who=['Snapchat users in Saudi Arabia who lost access to a hacker.', 'People being threatened after an account takeover.', 'Parents helping a teenager recover an account.'], area=C('Saudi Arabia')))

# ---------------- D. Facebook recovery by country ----------------
def fb_country(k):
    d = K[k]; W = d['N']
    return dict(slug='facebook-account-recovery-%s' % k, f='fbrecov', title='Facebook Account Recovery %s: Official Routes' % W,
      desc='Locked out, hacked or disabled on Facebook in %s. Which official recovery route fits, where to report fraud, and what to send.' % d['n'],
      h1='Facebook account recovery in %s' % d['n'], crumb='Facebook recovery %s' % W,
      hero='The right route depends on whether you were hacked, lost your email or phone, or got disabled.',
      answer=('Facebook account recovery in %s starts with the message you see. Hacked accounts go through Facebook’s hacked-account page. Lost email or phone goes through the login help flow from a device you used before. '
              'Disabled accounts need the appeal on the notice, before the deadline it shows.') % d['n'],
      cards=[('Hacked', 'The hacked-account page.'), ('Lost email or phone', 'Login help from a known device.'), ('Disabled', 'Appeal from the notice.')],
      sections=P(S('Pick the right route', ul(['Hacked: %s.' % A('/facebook-hacked-account-recovery-service/', 'hacked Facebook account recovery'), 'Lost the email or phone on the account: %s.' % A('/guides/facebook-lost-access-to-email-or-phone/', 'lost access to email or phone'), 'Disabled or suspended: %s.' % A('/guides/facebook-account-disabled-appeal/', 'Facebook disabled appeal')])),
        S('Local reporting in %s' % W, 'If money was taken, ads were run on your card or you are being threatened, report to %s and tell your bank about any card charges. %s' % (d['police'], ('You can also ask Meta for a copy of your data under %s.' % d['data']) if d.get('data') else '')),
        EU(k) and S('Your rights in the EU', EU(k)),
        S('Tips that help', ul(['Use the phone or computer you normally log in from.', 'Use the same network you normally use, not a VPN.', 'Have a government ID ready in the exact name on the profile.', 'Write in %s, briefly and factually.' % d['lang']]))),
      faq=[('Is there a Facebook phone number in %s?' % W, 'Meta does not offer a phone line for personal account recovery. Be careful with numbers found online; many are scams.'),
           ('My profile manages business pages. What now?', 'Add a second admin to the pages if anyone still has access, and see our guide on disabled profiles that manage pages.'),
           ('Can Meta Verified help?', 'Meta Verified includes account support, but you need access to an account to subscribe.')],
      who=['People in %s locked out of their Facebook profile.' % d['n'], 'Page admins and small businesses whose profile runs their pages and ads.', 'Anyone who has tried the automated steps and is stuck.'],
      area=C(d['c']))
IGD = [fb_country(k) for k in ('germany', 'ireland', 'uk', 'usa', 'uae', 'saudi-arabia', 'qatar', 'singapore', 'new-zealand')]

# ---------------- E. Username claims by country ----------------
def un_country(k):
    d = K[k]; W = d['N']
    return dict(slug='instagram-username-claim-%s' % k, f='user', title='Instagram Username Claim %s' % W,
      desc='Claim an Instagram username in %s through the official routes: how a registered trademark helps, and what to prepare.' % d['n'],
      h1='Instagram username claim in %s' % d['n'], crumb='Username claim %s' % W,
      hero='Want the handle that matches your name or brand? Here is what works from %s.' % d['n'],
      answer=('An Instagram username claim in %s goes through Instagram’s own routes. The strongest is a trademark report, backed by a mark registered with %s. '
              'Without a trademark, a claim depends on the account breaking a rule, such as impersonating you. Unbanz checks the handle first.') % (d['n'], d['tm']),
      cards=[('Trademark first', 'A registered mark is the strongest basis.'), ('Impersonation', 'If the account pretends to be you.'), ('Refund policy', 'Full refund if a claim fails.')],
      sections=P(S('Trademarks in %s' % W, 'A mark registered with %s that matches the handle is the clearest proof. %s' % (d['tm'], 'An EU trade mark from the EUIPO covers %s as well.' % d['n'] if d.get('eu') else 'Keep the registration certificate and number ready.')),
        S('What we check first', ul(['Whether the handle is held by a real, active account.', 'Whether it breaks a rule Instagram enforces.', 'Which route fits and what proof you have.'])),
        S('Before anything starts', 'Terms are agreed with you before any work starts. If a claim fails, our refund policy gives you a full refund. See %s.' % A('/instagram-username-claim-refund/', 'the refund policy'))),
      faq=[('Can I claim a handle without a trademark?', 'Sometimes, if the account breaks a rule such as impersonation. Without that, a trademark makes the claim much stronger.'),
           ('Do I need a company in %s?' % W, 'No. What matters is the right to the name, usually a registered mark.'),
           ('Do you need my password?', 'No. The handle is moved to the profile you choose without sharing your login.')],
      who=['Brands and businesses in %s.' % d['n'], 'Founders launching a product under a registered name.', 'Creators whose own name is taken by an unused account.'],
      area=C(d['c']))
IGE = [un_country(k) for k in ('austria', 'belgium', 'denmark', 'norway', 'italy', 'spain', 'kuwait', 'finland')]

for p in IGA + IGB + IGC + IGD + IGE:
    page(p['slug'], p['f'], p['title'], p['desc'], p['h1'], p['crumb'], p['hero'], p['answer'], p['cards'], p['sections'], p['faq'], p['who'], area=p.get('area'))
GROUPS = {'Instagram in the Gulf and Switzerland': [p['slug'] for p in IGA], 'Inactive usernames': [p['slug'] for p in IGB],
          'Snapchat locks': [p['slug'] for p in IGC], 'Facebook recovery by country': [p['slug'] for p in IGD], 'Username claims by country': [p['slug'] for p in IGE]}
