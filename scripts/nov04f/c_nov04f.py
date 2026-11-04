# -*- coding: utf-8 -*-
"""2026-11-04 (f): Facebook gap pages, best-service comparison pages for Facebook,
Meta ad accounts and username claims in US, UK, Canada, Netherlands, France."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dd29'))
from fams import *
from lib import PAGES
def T(head, rows):
    return '<div class="table-wrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (
        ''.join('<th scope="col">%s</th>' % h for h in head),
        ''.join('<tr>%s</tr>' % ''.join(('<th scope="row">%s</th>' if i == 0 else '<td>%s</td>') % c for i, c in enumerate(r)) for r in rows))
NOPASS = ('Does anyone need my password to help?', 'No. Never share your password or login codes. Anyone who asks for them is a risk.')
FBAPP = A('/guides/facebook-account-disabled-appeal/', 'Facebook disabled: how to appeal')
FBLOST = A('/guides/facebook-lost-access-to-email-or-phone/', 'lost access to the email or phone')
FBHS = A('/facebook-hacked-account-recovery-service/', 'hacked Facebook account recovery')
FBREC = A('/facebook-account-recovery/', 'Facebook account recovery')
DSA = A('/dsa-appeal-right-instagram-facebook/', 'your DSA appeal right')
ADREC = A('/ad-account-recovery/', 'Meta ad account recovery')
ADREST = A('/guides/meta-ad-account-restricted/', 'Meta ad account restricted')
UN = A('/instagram-username-claim/', 'Instagram username claims')
UNELIG = A('/instagram-username-claim-eligibility/', 'username claim eligibility')

fam('fbhacked', ws='unban', platform='Facebook', parent=('Facebook account help', '/facebook-account-help/'), stype='Hacked Facebook account recovery',
    wa=FB_WA, subj='Hacked%20Facebook%20account', what='a hacked Facebook account', send=FBSEND,
    how1='your Facebook profile link and what the hacker changed',
    how3='We map the recovery routes that fit what was changed and prepare what to send through Facebook’s own process.')
FHSTEPS = ol(['Open the "security alert" or "email changed" message Facebook sent to your old address and use the link to secure the account, if it is there.',
 'Go to facebook.com/hacked on a device and network you have used before and follow the steps.',
 'If the email and phone were both changed, choose the option that you no longer have access to them and follow the identity check.',
 'Upload ID if asked. The name must match the profile.',
 'Once back in, change the password, turn on two-factor authentication, remove unknown devices and check Page and ad account admins.'])
def fbh(slug, country, crumb, lede, answer, cards, local, faqs, who, area):
    page(slug, 'fbhacked', 'Facebook Hacked in %s: What to Do' % country,
     'Your Facebook account was hacked and you are in %s. The facebook.com/hacked steps, where to report it locally, and what to send.' % country,
     'Facebook account hacked and you are in %s?' % country, crumb, lede, answer, cards,
     [S('Steps', FHSTEPS), S('Where to report it in %s' % country, local + ' Related: %s, %s and %s.' % (FBHS, FBLOST, FBAPP))],
     faqs + [('What if the hacker got the account disabled?', 'Appeal from the disabled notice and say in one line that the account was hacked and when. Keep it short and accurate.'), NOPASS], who, area=area)
fbh('facebook-hacked-usa-what-to-do', 'the US', 'Facebook hacked, US',
 'Anywhere in the US, recovery happens through Facebook. Federal reports help if money or identity theft is involved.',
 'If your Facebook was hacked in the US, use the security link Facebook emailed to your old address or go to facebook.com/hacked, then complete the ID check if asked. If the hacker scammed friends, ran ads on your card or used your identity, report it to the FBI at ic3.gov and the FTC at ReportFraud.ftc.gov.',
 [('facebook.com/hacked', 'The official start point.'), ('IC3 and FTC', 'Report scams and identity theft.'), ('Your bank', 'Dispute ad charges you did not make.')],
 'Report scams sent from the account to the FBI Internet Crime Complaint Center at ic3.gov and the FTC at ReportFraud.ftc.gov. If your identity was used, IdentityTheft.gov gives a recovery plan. If ads were charged to your card, call your bank. None of these restore the account, but reference numbers help explain the hack.',
 [('Is there a Facebook phone number I can call?', 'No. Facebook does not run phone support for hacked personal accounts. Numbers that claim to be Facebook support are often scams.')],
 ['US users and small businesses after a takeover.', 'People whose account is messaging friends with scams.', 'Page and ad account owners who lost admin access.'], 'US')
fbh('facebook-hacked-uk-what-to-do', 'the UK', 'Facebook hacked, UK',
 'Anywhere in the UK, recovery happens through Facebook. Action Fraud and the ICO cover the parts Facebook does not.',
 'If your Facebook was hacked in the UK, use the security link Facebook emailed to your old address or go to facebook.com/hacked, then complete the ID check if asked. If friends were scammed or money was taken, report it to Action Fraud, or Police Scotland in Scotland, and keep the crime reference number.',
 [('facebook.com/hacked', 'The official start point.'), ('Action Fraud', 'Get a crime reference number.'), ('ICO', 'Your data rights.')],
 'Report fraud to Action Fraud at actionfraud.police.uk, or Police Scotland if you live in Scotland. If ads were charged to your card, call your bank. You can ask Meta for your data with a UK GDPR subject access request and complain to the ICO if it is ignored. Ofcom does not handle individual account complaints.',
 [('Can Ofcom get my account back?', 'No. Ofcom regulates platforms overall and does not take individual account complaints.')],
 ['UK users and small businesses after a takeover.', 'People whose account is messaging friends with scams.', 'Page and ad account owners who lost admin access.'], 'GB')
fbh('facebook-hacked-canada-what-to-do', 'Canada', 'Facebook hacked, Canada',
 'Anywhere in Canada, recovery happens through Facebook. The CAFC and the privacy commissioner cover the rest.',
 'If your Facebook was hacked in Canada, use the security link Facebook emailed to your old address or go to facebook.com/hacked, then complete the ID check if asked. If friends were scammed or money was taken, report it to the Canadian Anti-Fraud Centre and your local police, and keep the file number.',
 [('facebook.com/hacked', 'The official start point.'), ('CAFC', 'Report fraud and keep the number.'), ('OPC', 'Privacy and data access.')],
 'Report fraud to the Canadian Anti-Fraud Centre and your local police. If ads were charged to your card, call your bank. Under PIPEDA you can ask Meta for your personal data and complain to the Office of the Privacy Commissioner of Canada if it is not answered. These bodies do not restore accounts.',
 [('Can I write in French?', 'Yes. Write in the language you are most comfortable with.')],
 ['Canadian users and small businesses after a takeover.', 'People whose account is messaging friends with scams.', 'Page and ad account owners who lost admin access.'], 'CA')
fbh('facebook-hacked-netherlands-what-to-do', 'the Netherlands', 'Facebook hacked, Netherlands',
 'Anywhere in the Netherlands, recovery happens through Facebook. Fraudehelpdesk, the police and the Dutch DPA cover the rest.',
 'If your Facebook was hacked in the Netherlands, use the security link Facebook emailed to your old address or go to facebook.com/hacked, then complete the ID check if asked. If friends were scammed or money was taken, report it to the Fraudehelpdesk and file a police report (aangifte).',
 [('facebook.com/hacked', 'The official start point.'), ('Fraudehelpdesk', 'Report scams, then the police.'), ('DSA', 'EU routes if it is then disabled.')],
 'Report scams to the Fraudehelpdesk and file a report with the police. Under the GDPR you can ask Meta for your data and complain to the Autoriteit Persoonsgegevens if it is ignored. If the account is disabled after the hack, the EU DSA gives you %s.' % DSA,
 [('Can I write in Dutch?', 'Yes. Write in the language you are most comfortable with.')],
 ['Dutch users and small businesses after a takeover.', 'People whose account is messaging friends with scams.', 'Page and ad account owners who lost admin access.'], 'NL')

# Best service: Facebook
OPT_FB = T(['Option', 'What it covers', 'Cost', 'Watch out for'], [
 ['Facebook’s own tools', 'Appeal on the notice, facebook.com/hacked, ID upload.', 'Free.', 'Automated replies. One clean try matters.'],
 ['Meta Verified support', 'Chat support for subscribers on eligible accounts.', 'Monthly subscription.', 'Not available to every account, and it does not overrule a decision.'],
 ['Doing it yourself with a guide', 'Same official routes, with your own research.', 'Free.', 'Easy to send a weak or duplicate appeal.'],
 ['An independent recovery service', 'Help preparing and handling the appeal through Meta’s official process.', 'Agreed with you before work starts.', 'Anyone asking for your password or claiming inside access.'],
 ['"Recovery hackers" in DMs or comments', 'Nothing legitimate.', 'Upfront fees.', 'These are scams. Avoid them.']])
CHECK = ul(['Never asks for your password or login codes.', 'Does not claim inside access at Meta or a special form.', 'Tells you the terms before any work starts.',
 'Explains which official route it will use.', 'Can be reached on a public contact, not only through DMs.', 'Says plainly that Meta makes the final decision.'])
page('best-service-to-recover-disabled-facebook-account', 'fbdis', 'Best Service to Recover a Disabled Facebook Account',
 'How to choose a service to recover a disabled or hacked Facebook account. Official routes, Meta Verified, DIY and independent services compared.',
 'Best service to recover a disabled Facebook account', 'Best Facebook recovery service',
 'The right choice depends on the notice, what you have already tried and how much time you can give it. Here is how the options compare.',
 'Start with Facebook’s own appeal on the notice, or facebook.com/hacked if you were hacked. If that stalls, a legitimate service, such as Unbanz, helps you prepare and handle the appeal through Meta’s official process without ever asking for your password. Avoid anyone who claims inside access or asks for login codes. Meta makes the final decision.',
 [('Official routes first', 'Free and always available.'), ('No password', 'A legitimate service never needs it.'), ('Terms first', 'Agreed with you before any work starts.')],
 [S('How the options compare', OPT_FB),
  S('How to check a Facebook recovery service', CHECK),
  S('Where Unbanz fits', 'Unbanz is an independent service that helps people recover disabled, suspended and hacked Instagram, Facebook and Meta ad accounts, and claim usernames. We work from your profile link and a screenshot of the notice, prepare the appeal and the supporting details, and handle it through Meta’s official process. The usual estimate is 3-14 days from the day we start. Terms are agreed with you before any work starts. Related: %s, %s and %s.' % (FBREC, FBHS, FBAPP))],
 [('Is there a way to talk to a human at Facebook?', 'Meta Verified subscribers can chat with support on eligible accounts. Otherwise, Facebook does not offer phone support for disabled accounts.'),
  ('Can a service get my account back faster than Meta?', 'No one can speed up Meta. A clear, accurate appeal with matching documents is what helps.'),
  ('Which countries does Unbanz help in?', 'We work remotely, including with people in the US, the UK, Canada, the Netherlands and France.'), NOPASS],
 ['People whose Facebook appeal was rejected or went unanswered.', 'Small businesses whose Page and ads sit on a disabled profile.', 'Anyone weighing up whether to get help.'])

CN = {'usa': ('the US', 'US', 'US'), 'uk': ('the UK', 'UK', 'GB'), 'canada': ('Canada', 'Canada', 'CA'),
      'netherlands': ('the Netherlands', 'Netherlands', 'NL'), 'france': ('France', 'France', 'FR')}
ADLOC = {'usa': 'US businesses often run ads in USD with a US card; make sure the card holder name and business name match what Meta sees.',
 'uk': 'UK businesses can match the business name to Companies House records and the VAT number, if they have one.',
 'canada': 'Canadian businesses can match the business name to the provincial or federal registration and the GST/HST number, if they have one.',
 'netherlands': 'Dutch businesses can match the business name to the KvK (Chamber of Commerce) extract and the VAT number. EU DSA statement-of-reasons rights also apply.',
 'france': 'French businesses can match the business name to the SIRET/Kbis extract and the VAT number. EU DSA statement-of-reasons rights also apply.'}
UNLOC = {'usa': 'A registered US trademark (USPTO) is the strongest proof for a brand handle.',
 'uk': 'A UK trademark from the UKIPO, or an EU mark, is the strongest proof for a brand handle.',
 'canada': 'A registered Canadian trademark (CIPO) is the strongest proof for a brand handle.',
 'netherlands': 'A Benelux trademark (BOIP) or EU trademark (EUIPO) is the strongest proof for a brand handle.',
 'france': 'A French trademark from INPI, or an EU trademark (EUIPO), is the strongest proof for a brand handle.'}
OPT_AD = T(['Option', 'What it covers', 'Cost', 'Watch out for'], [
 ['Request review in Account Quality', 'The official appeal for a restricted or disabled ad account.', 'Free.', 'One clean request with matching details works best.'],
 ['Meta Business support chat', 'Available to some advertisers.', 'Free where offered.', 'Agents often cannot overrule a policy decision.'],
 ['Your media buyer or agency', 'Context on what ran before the restriction.', 'Varies.', 'Shared logins and new admins can cause flags.'],
 ['An independent recovery service', 'Help reading the notice, fixing the cause and preparing the review through Meta’s process.', 'Agreed with you before work starts.', 'Anyone selling "unbanned" ad accounts or asking for logins.'],
 ['Renting or buying ad accounts', 'Not a fix.', 'Varies.', 'Against Meta policy and can get the whole portfolio restricted.']])
OPT_UN = T(['Option', 'What it covers', 'Cost', 'Watch out for'], [
 ['Trademark report to Instagram', 'Official route when a handle infringes a registered mark.', 'Free.', 'Needs the registration details and a clear match.'],
 ['Wait for an inactive handle', 'Instagram may free up inactive names over time.', 'Free.', 'No set timeline. Many never free up.'],
 ['Contact the current holder', 'Sometimes works for unused names.', 'Varies.', 'Buying or selling usernames is against Instagram terms.'],
 ['An independent claim service', 'Checks the handle and uses the official route that fits it. Your password stays with you.', 'Agreed with you before work starts.', 'Anyone offering to "hack" or "swap" a handle.'],
 ['Username sellers', 'Not legitimate.', 'Upfront fees.', 'Handles can be taken back and the account restricted.']])
for k, (cname, short, area) in CN.items():
    page('best-meta-ad-account-recovery-service-%s' % k, 'ad', 'Best Meta Ad Account Recovery Service in %s' % short,
     'How to choose a Meta ad account recovery service in %s. Account Quality, Meta support, agencies and services compared.' % cname,
     'Best Meta ad account recovery service in %s' % cname, 'Best ad account recovery, %s' % short,
     'For a restricted or disabled Meta ad account in %s, the right help depends on what is limited and why. Here is how the options compare.' % cname,
     'For a Meta ad account in %s, start with Request review in Account Quality after fixing the likely cause. If that stalls, a legitimate service, such as Unbanz, helps you read the notice, fix the cause and prepare the review through Meta’s official process. Avoid anyone selling replacement ad accounts. Meta makes the final decision.' % cname,
     [('Account Quality first', 'The official review route.'), ('Fix the cause', 'Payment, identity, policy.'), ('Terms first', 'Agreed before any work starts.')],
     [S('How the options compare', OPT_AD), S('Local details that help in %s' % cname, ADLOC[k]), S('How to check a service', CHECK),
      S('Where Unbanz fits', 'Unbanz is an independent service that helps people recover disabled, suspended and hacked Instagram, Facebook and Meta ad accounts, and claim usernames. For ad accounts we work from the ad account ID and the notice. The usual estimate is 3-14 days from the day we start. Terms are agreed with you before any work starts. Related: %s and %s.' % (ADREC, ADREST))],
     [('Can anyone get my ad account back faster?', 'No one can speed up Meta. A clear request with matching documents is what helps.'), ('Should I open a new ad account?', 'Opening new ad accounts to get around a restriction can get the whole business portfolio restricted.'), NOPASS],
     ['Advertisers in %s with a restricted or disabled ad account.' % cname, 'Agencies and media buyers managing client accounts.', 'Small businesses whose sales depend on Meta ads.'], area=area)
    page('best-username-claim-service-%s' % k, 'user', 'Best Instagram Username Claim Service in %s' % short,
     'How to claim an Instagram username in %s. Trademark reports, waiting and claim services compared.' % cname,
     'Best Instagram username claim service in %s' % cname, 'Best username claim, %s' % short,
     'Want a handle that is taken or inactive, and you are in %s? The right route depends on why the name is yours. Here is how the options compare.' % cname,
     'To claim an Instagram username in %s, the official route is a trademark report if you hold a registered mark that matches the handle. Without one, options are narrower. A legitimate service, such as Unbanz, checks the handle and uses the official route that fits it. Avoid anyone offering to hack or swap a handle.' % cname,
     [('Trademark first', 'The strongest official route.'), ('No password', 'It stays with you.'), ('Terms first', 'Agreed before any work starts.')],
     [S('How the options compare', OPT_UN), S('Proof that helps in %s' % cname, UNLOC[k]), S('How to check a service', CHECK),
      S('Where Unbanz fits', 'Unbanz is an independent service that helps people recover disabled, suspended and hacked Instagram, Facebook and Meta ad accounts, and claim usernames. We check the handle and tell you honestly if a route fits. Terms are agreed with you before any work starts. Related: %s and %s.' % (UN, UNELIG))],
     [('Can I buy a username?', 'Buying or selling usernames is against Instagram terms and the handle can be taken back.'), ('Do I need a trademark?', 'It is the strongest proof. Without one, Instagram rarely moves a handle that is in use.'), NOPASS],
     ['Brands and businesses in %s whose name is taken.' % cname, 'Creators who lost a handle they used before.', 'Agencies claiming handles for clients.'], area=area)
