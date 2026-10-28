# -*- coding: utf-8 -*-
"""Answer-first reference pages added 2026-10-28 (rendered by build_oct28_pages.py)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from oct25_content import A, how, who, sec, ul, ol, CAN_FAQ, PASSWORD_FAQ, CONTACT_FAQ, ACCT_STEP1, USER_STEP1

DATE = '2026-10-28'
UPD = '<p><em>Last updated: 28 October 2026.</em></p>'
PAGES = []
def page(**kw): PAGES.append(kw)

def table(head, rows):
    return '<div class="table-wrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (
        ''.join('<th>%s</th>' % h for h in head),
        ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in rows))

COMMON = [('/instagram-account-recovery/','Instagram account recovery'),('/instagram-account-disabled-appeal/','Instagram disabled appeal'),('/instagram-appeal-denied/','Appeal denied'),('/unban-pricing/','Unban cost and timing'),('/services/','All services')]

# 1 ------------------------------------------------------------------
page(slug='instagram-account-disabled-vs-suspended-vs-restricted', lang='en',
 title='Instagram Disabled vs Suspended vs Restricted | Unbanz',
 desc='Disabled, suspended, restricted, hacked or deleted? What each Instagram message means, how to tell them apart and what to do first.',
 h1='Instagram disabled, suspended, restricted or deleted: what is the difference?',
 crumb='Disabled vs suspended vs restricted', svc='Instagram account status help',
 hero='Instagram uses several different screens for different problems. Read yours below, find the match and see the right first step.',
 wa='Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20Instagram%20account', ws='unban', subj='Instagram%20account%20status',
 answer='A disabled or suspended Instagram account shows a notice at login and is offline. A restricted account still logs in but some features are limited. A hacked account usually shows no notice, just a password that stops working. A deleted account cannot be restored. Each one has a different first step.',
 body=[UPD,
  sec('glance','At a glance', table(['What you see','What it usually means','First step'], [
    ['“We disabled your account”','Instagram took account-level action. The account is offline.','Screenshot the notice, then request a review once from that screen. '+A('/guides/instagram-account-disabled/','Disabled guide')],
    ['“We suspended your account” with a countdown','Account-level action with a deadline to disagree.','Use the Disagree or Appeal button before the deadline. '+A('/guides/instagram-account-suspended-appeal/','Suspension guide')],
    ['You can log in but cannot post, comment or message','A restriction or feature limit, not a disabled account.','Open Settings, then Account Status, and read the end date. '+A('/guides/instagram-check-account-status/','Account Status guide')],
    ['No notice and the password stops working','A login problem, or someone else got in.','Go to instagram.com/hacked. '+A('/guides/hacked-instagram-account-recovery/','Hacked account guide')],
    ['The profile has vanished','It may have been deleted by you or by someone with your password.','Instagram says a deleted account cannot be restored. Check email for any message first.']])),
  sec('disabled','Disabled', '<p>A disabled account is offline. According to Instagram’s Help Center, accounts that do not follow Meta’s Community Standards may be disabled, and you see a message about it when you try to log in. If you think it was a mistake, you may be able to ask for a review by logging in and following the on-screen steps. There is no separate unban email address. Related: '+A('/instagram-account-disabled-appeal/','Instagram disabled account appeal')+'.</p>'),
  sec('suspended','Suspended', '<p>A suspended account shows a similar notice, often with a date. The date is the deadline to use the Disagree or Appeal option, which is usually 180 days. Use it once and keep the screenshots. Related: '+A('/instagram-account-suspended-180-days/','180-day suspension')+'.</p>'),
  sec('restricted','Restricted or action blocked', '<p>A restriction limits a feature, such as messaging new people or going live. You can still log in. Account Status shows the feature and the end date. These limits are usually temporary. Related: '+A('/instagram-we-restrict-certain-activity-action-blocked/','Action blocked message')+'.</p>'),
  sec('hacked','Hacked', '<p>A hacked account often shows no enforcement notice at all. Look for an email from Instagram about a changed email, phone number or password and use the undo link in it. Then use instagram.com/hacked on a device you have used before. Related: '+A('/instagram-hacked-account-recovery-service/','Hacked Instagram recovery')+'.</p>'),
  sec('deleted','Deleted or deactivated', '<p>Deleted and deactivated are not the same. A deactivated account is hidden by choice and Instagram says you can bring it back by logging in. A deleted account cannot be restored. Related: '+A('/is-my-instagram-account-deleted-or-disabled/','Is my account deleted or disabled?')+'.</p>'),
  sec('help','How Unbanz helps', '<p>We read the notice with you, tell you which of these it is and whether we think an appeal is realistic, and handle the appeal through Meta’s official process. Meta makes the final decision. Main page: '+A('/instagram-account-recovery/','Instagram account recovery')+'.</p>'),
  how(ACCT_STEP1),
  who(['People who are not sure what their Instagram screen means.','Anyone who has seen “suspended”, “disabled” or “restricted” and wants the right next step.','Not for: accounts that were really used for scams or abuse.']),
 ],
 faq=[
  ('What is the difference between a disabled and a suspended Instagram account?','Both mean account-level action and the account is offline. A suspended notice usually carries a deadline to disagree or appeal, often 180 days. A disabled notice tells you the account was disabled and may offer a review option.'),
  ('Is a restricted Instagram account the same as a ban?','No. A restricted account still logs in. A feature such as messaging or live video is limited for a set time. Account Status shows which feature and when it ends.'),
  ('How do I tell if my Instagram was hacked or disabled?','A disabled account shows a notice when you log in. A hacked account often shows none, and the password simply stops working or the email on the account has changed. Use instagram.com/hacked for the second situation.'),
  ('Can a deleted Instagram account be restored?','Instagram says a deleted account cannot be restored. A deactivated account is different: it is hidden and you can bring it back by logging in.'),
  CAN_FAQ, CONTACT_FAQ],
 related=[('/guides/instagram-account-disabled/','Disabled account guide'),('/guides/instagram-check-account-status/','Check Account Status'),('/instagram-appeal-checklist/','Appeal checklist'),('/instagram-recovery-glossary/','Recovery glossary')]+COMMON[:3],
 relq=[('/ways-to-get-a-banned-instagram-account-back/','Ways to get an account back'),('/is-an-unban-service-safe/','Is an unban service safe?'),('/how-long-does-an-instagram-appeal-take/','How long an appeal takes')])

# 2 ------------------------------------------------------------------
page(slug='ways-to-get-a-banned-instagram-account-back', lang='en',
 title='Ways to Get a Banned Instagram Account Back | Unbanz',
 desc='The routes to get a banned or disabled Instagram account back, ranked free first: in-app review, hacked flow, Meta Verified support and independent help.',
 h1='Ways to get a banned Instagram account back, free options first.',
 crumb='Ways to get an account back', svc='Instagram account recovery',
 hero='Start with the free official routes. If they are closed or did not work, an independent service is one more option. Meta makes the final decision on every route.',
 wa='Hey%20Unbanz%2C%20I%20need%20help%20recovering%20my%20Instagram%20account', ws='unban', subj='Instagram%20account%20recovery',
 answer='The best first route is the free in-app review: log in, follow the on-screen steps and submit once. If the account was hacked, use instagram.com/hacked. If you subscribe to Meta Verified, contact its support. If those are closed or failed, an independent service like Unbanz can prepare and handle the appeal. Meta makes the final decision.',
 body=[UPD,
  sec('list','The routes, in the order to try them', ol([
    '<strong>In-app review or appeal (free).</strong> Log in, read the full notice and use the Disagree, Appeal or Request review button once. Add a short, factual note if there is a text box. Guide: '+A('/guides/instagram-account-suspended-appeal/','how to appeal a suspension')+'.',
    '<strong>instagram.com/hacked (free).</strong> For accounts where the password or email was changed by someone else. Use a device you have logged in from before. Guide: '+A('/guides/hacked-instagram-account-recovery/','hacked Instagram account recovery')+'.',
    '<strong>Meta Verified support (paid subscription).</strong> If you already have an active Meta Verified subscription, Instagram’s Help Center says you can contact support from the app where it is available. Compare it with the other routes on '+A('/compare/','Compare options')+'.',
    '<strong>Identity checks (free).</strong> If Instagram asks for a code or a video selfie, complete it. Many reviews wait on this step. Guide: '+A('/guides/instagram-video-selfie-verification/','video selfie verification')+'.',
    '<strong>An independent service such as Unbanz (paid).</strong> We read the notice, say whether an appeal looks realistic, prepare it and handle it through Meta’s official process. Price is agreed before work starts.'])),
  sec('wait','Do not repeat the same request', '<p>Sending the same appeal again and again does not help. Submit once, keep a screenshot of the confirmation and watch your email and the app for the answer. If the answer is no, read what it says and see '+A('/instagram-appeal-denied/','what to do after a denied appeal')+'.</p>'),
  sec('no','What does not work', ul([
    'Paying a stranger who says they know someone at Meta. No one outside Meta can change a decision.',
    'Sharing your password or login codes with anyone.',
    'Buying a replacement account, or an account that someone says is “restored”.',
    'Filing false or mass reports against other accounts.'])),
  sec('which','Which route fits your situation', table(['Situation','Start here'], [
    ['A notice with a button to disagree or appeal','In-app review'],
    ['No notice, password or email changed','instagram.com/hacked'],
    ['Active Meta Verified subscription and you can still reach the app','Meta Verified support'],
    ['No button, the review was denied, or you would rather not do it yourself','Independent help'],
    ['An account on someone else’s name or a username you want','See '+A('/instagram-username-claim-routes/','username claim routes')]])),
  sec('help','Where Unbanz fits', '<p>Unbanz is an independent service. We do not have special access at Meta and are not affiliated with it. We prepare the appeal, send it through the official process and keep you posted. Main page: '+A('/instagram-account-recovery/','Instagram account recovery')+'.</p>'),
  how(ACCT_STEP1),
  who(['People whose Instagram account is disabled, suspended or hacked.','Creators and businesses that depend on the account.','Anyone who already appealed once and did not get a clear answer.','Not for: accounts that were really used for scams or abuse.']),
 ],
 faq=[
  ('What is the best way to get a banned Instagram account back?','Try the free in-app review first. If the account was hacked, use instagram.com/hacked. If you subscribe to Meta Verified, contact its support. If those are closed or did not work, an independent service can handle the appeal for you.'),
  ('Can I pay someone at Meta to restore my Instagram account?','No. Anyone offering a Meta insider or a private channel is not offering something real. Decisions are made by Meta through its official process.'),
  ('Do I have to share my password with a recovery service?','No. A legitimate service works from the username and the notice. Your password and login codes stay with you.'),
  ('How many times should I appeal?','Once per notice. Repeated identical requests do not help. Submit, keep the confirmation and wait for the reply.'),
  ('Will an independent service get my account back?','No service controls the outcome. Meta makes the final decision. Unbanz tells you upfront whether an appeal looks realistic and agrees the price before work starts.'),
  CONTACT_FAQ],
 related=[('/compare/','Compare options'),('/instagram-appeal-checklist/','Appeal checklist'),('/instagram-account-disabled-vs-suspended-vs-restricted/','Disabled vs suspended vs restricted'),('/best-instagram-recovery-service/','What a good service looks like')]+COMMON[:2],
 relq=[('/is-an-unban-service-safe/','Is an unban service safe?'),('/guides/account-recovery-scams-fake-hackers-warning/','Recovery scams warning'),('/how-long-does-an-instagram-appeal-take/','How long an appeal takes')])

# 3 ------------------------------------------------------------------
page(slug='instagram-username-claim-routes', lang='en',
 title='Instagram Username Claim Routes Compared | Unbanz',
 desc='The real routes to an Instagram username held by someone else: trademark report, impersonation, squatted or inactive, a freed handle, and a swap.',
 h1='Instagram username claim routes, compared.',
 crumb='Username claim routes', svc='Instagram username claims',
 hero='Instagram has no public form for asking for a name because an account looks inactive. A claim works when the handle fits one of the platform’s own processes. Here they are side by side.',
 wa='Hey%20Unbanz%2C%20I%20want%20to%20claim%20this%20username%3A%20%40', ws='username', subj='Instagram%20username%20claim',
 answer='An Instagram username claim works through the platform’s own processes: a registered trademark report, an impersonation report, a squatted or abandoned handle, or a handle that gets freed up. Which route fits depends on the handle. Meta makes the final decision, and some handles have no honest route at all.',
 body=[UPD,
  sec('table','The routes at a glance', table(['Route','When it fits','What you bring','Honest limit'], [
    ['Trademark (IP) report','The handle matches a registered trademark you own.','Registration details and proof it is yours.','Needs a real registered mark. A name you simply like does not qualify.'],
    ['Impersonation report','An account is pretending to be you or your brand.','Proof of who you are and how the account copies you.','The account has to be impersonating, not just similar.'],
    ['Squatted or abandoned handle','A parked, dead or look-alike account holds the name.','The handle, your current profile and any history with the name.','There is no public inactive-account form, so the route depends on the facts.'],
    ['Handle that gets freed up','The holder deletes or changes it, or the account is removed.','Your account ready to take the name.','A freed handle can return to the open pool, so a claim only counts when it is on your profile.'],
    ['Username swap','Two real people agree to trade names.','Both sides willing, no logins shared.','Risky. The other side can walk away after you rename. See '+A('/instagram-username-swap-vs-claim/','swap vs claim')+'.'],
    ['Buying a username','Someone offers to sell you a handle.','Not a route.','Instagram’s terms do not allow selling usernames. See '+A('/can-you-buy-an-instagram-username/','can you buy a username')+'.']])),
  sec('trademark','Trademark route', '<p>If you own a registered trademark that matches the handle, the platform’s intellectual property report is the standard route. Have the registration number and the territory ready. See '+A('/trademark-username-claim/','trademark username claims')+'.</p>'),
  sec('impersonation','Impersonation route', '<p>If another account uses your name, photos or brand to mislead people, report it as impersonation. This is a report about behaviour, and every report must be true. See '+A('/report-business-impersonation/','business impersonation reports')+'.</p>'),
  sec('inactive','Inactive or squatted route', '<p>An inactive account is not automatically available. The platform’s processes for abandoned and squatted handles depend on the facts, so we check the handle first and tell you whether a route exists. See '+A('/can-you-claim-a-username-from-an-inactive-instagram-account/','claiming from an inactive account')+' and '+A('/inactive-instagram-username/','inactive Instagram usernames')+'.</p>'),
  sec('refund','Refund policy for username claims', '<p>If a username claim fails, meaning the username is not successfully claimed onto your profile, the refund policy is a full 100% refund. Details: '+A('/refund-policy/','refund policy')+'.</p>'),
  sec('help','How Unbanz helps', '<p>We check what holds your handle, say which route fits or that none does, and handle the process through the platform’s official channels. Nothing is charged for asking. Main page: '+A('/instagram-username-claim/','Instagram username claims')+'.</p>'),
  how(USER_STEP1, username=True),
  who(['Founders, creators and businesses who want a specific handle.','Brand owners whose name is held by a squatter or a look-alike.','Not for: handles held by active strangers with no breach of the platform’s rules.']),
 ],
 faq=[
  ('Can I claim an inactive Instagram username?','Not just because the account looks inactive. Instagram has no public form for that. A claim works when the handle fits a platform process such as a trademark report, an impersonation report or a squatted handle.'),
  ('Which username claim route is the most reliable?','A registered trademark matching the handle is the clearest route, because it rests on a legal right. Other routes depend on facts about the account holding the name.'),
  ('Does a username claim move someone’s account to me?','No. The handle goes onto your own profile through the platform’s processes. No accounts change hands and your password stays with you.'),
  ('What happens if a username claim fails?','The refund policy is a full 100% refund if the username is not successfully claimed onto your profile.'),
  ('Does Unbanz use false reports to free up a username?','No. Every report is true and goes through the platform’s own tools. If a handle has no honest route, we say so.'),
  CONTACT_FAQ],
 related=[('/instagram-username-claim/','Instagram username claims'),('/username-claim-pricing/','Username claim pricing'),('/how-long-does-it-take-to-claim-an-instagram-username/','How long a claim takes'),('/is-a-username-claim-safe/','Is a username claim safe?'),('/refund-policy/','Refund policy')],
 relq=[('/best-instagram-username-claim-service/','Best username claim service'),('/how-to-get-a-short-og-instagram-username/','Short OG usernames'),('/instagram-username-not-available-but-no-account/','Not available but no account')])

# 4 ------------------------------------------------------------------
page(slug='meta-ad-account-restricted-vs-disabled', lang='en',
 title='Meta Ad Account Restricted vs Disabled | Unbanz',
 desc='Restricted, disabled or a rejected ad? What each Meta ad status means, which asset it hits and where to look first.',
 h1='Meta ad account restricted or disabled: what is the difference?',
 crumb='Restricted vs disabled ad account', svc='Meta ad account recovery',
 hero='A restriction and a disabled ad account are different problems. Find which asset is affected, then follow the matching step.',
 wa='Hey%20Unbanz%2C%20my%20Meta%20ad%20account%20is%20restricted%20or%20disabled', ws='unban', subj='Meta%20ad%20account%20help',
 answer='A restricted Meta ad account has limits on what you can do, such as spend or features. A disabled one cannot run ads until the decision changes. A restriction can sit on the business portfolio, the ad account, a Page or a personal profile. Open Account Quality to see which asset is affected and whether a review button exists.',
 body=[UPD,
  sec('assets','Which asset is affected', table(['Asset','What a restriction means'], [
    ['Business portfolio','The portfolio is not allowed to advertise.'],
    ['Ad account','The ad account, its ads and some advertising assets are disabled.'],
    ['Page','The Page is not allowed to advertise.'],
    ['Personal profile','That person cannot advertise or create new ads. Other people on the business may still be able to advertise.']])+'<p>This follows the structure in Meta’s About advertising restrictions page. Walkthrough: '+A('/guides/meta-ad-account-restricted/','restricted ad account guide')+'.</p>'),
  sec('statuses','Statuses in plain language', table(['Status','Meaning'], [
    ['Restricted or limited','Some features or ad spending are held back while the issue is fixed.'],
    ['Disabled','The asset cannot be used until the decision changes. Look for a review option.'],
    ['Disapproved ad','One ad was rejected. The account itself may be fine.'],
    ['Warning','Meta is flagging a risk. Fix the cause before it becomes a restriction.']])),
  sec('where','Where to look first', '<p>On a computer, open Meta Business Support Home and check Account status overview, or open Account Quality. Select the affected asset, screenshot the reason and the date, and note the policy named. Guide: '+A('/guides/meta-account-quality-status-walkthrough/','Account Quality walkthrough')+'.</p>'),
  sec('reasons','Common reasons Meta lists', ul([
    'The advertiser does not follow the Advertising Standards, Community Standards or Commerce Policies.',
    'Meta suspects the business portfolio or its assets were compromised.',
    'Two-factor authentication requirements are not met.',
    'Unusual payment or account activity, or failed or disputed payments.'])),
  sec('review','Requesting a review', '<p>You need to be an admin on the account. Fix the cause first, for example secure the account or resolve a failed payment, then request a review once from the What you can do section. Repeated requests for the same item do not help. See '+A('/guides/meta-ad-rejected-request-review/','rejected ad review')+' and '+A('/meta-ad-account-appeal-rejected-what-next/','what to do after a rejected appeal')+'.</p>'),
  sec('help','How Unbanz helps', '<p>We read the status with you, say whether a review looks realistic, prepare it and handle it through Meta’s official process. Meta makes the final decision. Main page: '+A('/ad-account-recovery/','Meta ad account recovery')+'.</p>'),
  how('Message us on WhatsApp or email with the ad account or business portfolio, a screenshot of the status and the reason shown.'),
  who(['Advertisers and agencies with a restricted or disabled ad account.','Business owners who lost access to ads after a security or payment flag.','Not for: accounts running ads that break Meta’s rules.']),
 ],
 faq=[
  ('What is the difference between a restricted and a disabled ad account?','A restricted ad account has limits, such as spending or features. A disabled ad account cannot run ads until the decision changes. Both show their reason in Account Quality.'),
  ('Can a personal profile restriction stop my ads?','Yes. A restricted personal profile cannot advertise or create new ads, and ad accounts where that person is the only user may also be disabled. Other people on the business may still be able to advertise.'),
  ('Where do I see why my ad account was restricted?','In Meta Business Support Home under Account status overview, or in Account Quality. Select the asset and read the reason and the policy named.'),
  ('Should I request a review straight away?','Fix the obvious cause first, such as security or payment problems, then request a review once.'),
  CAN_FAQ, CONTACT_FAQ],
 related=[('/ad-account-recovery/','Meta ad account recovery'),('/meta-ad-account-restricted/','Meta ad account restricted'),('/facebook-ad-account-disabled/','Facebook ad account disabled'),('/how-long-does-meta-ad-account-review-take/','How long a review takes'),('/services/','All services')],
 relq=[('/why-was-my-facebook-ad-account-disabled-without-warning/','Disabled without warning'),('/best-facebook-ad-account-recovery-service/','What a good service looks like'),('/how-much-does-ad-account-recovery-cost/','Ad account recovery cost')])

# 5 ------------------------------------------------------------------
page(slug='instagram-appeal-checklist', lang='en',
 title='Instagram Appeal Checklist: Before You Submit | Unbanz',
 desc='A step-by-step checklist to run before you appeal a disabled or suspended Instagram account: screenshots, deadline, identity check, wording and what to avoid.',
 h1='Instagram appeal checklist: what to do before you submit.',
 crumb='Instagram appeal checklist', svc='Instagram appeals',
 hero='Run through these steps once, in order, before you press submit. A clean first appeal beats several rushed ones.',
 wa='Hey%20Unbanz%2C%20I%20want%20help%20with%20my%20Instagram%20appeal', ws='unban', subj='Instagram%20appeal',
 answer='Before you appeal a disabled or suspended Instagram account, screenshot the notice, read the deadline, secure your email, finish any identity check, then submit once with a short factual note. Do not delete posts, share your password or file the same request repeatedly. Meta makes the final decision.',
 body=[UPD,
  sec('list','The checklist', ol([
    '<strong>Screenshot every screen.</strong> Capture the exact wording, date, policy named and any deadline before you tap anything.',
    '<strong>Read the whole notice.</strong> Note whether it says disabled or suspended and whether a Disagree, Appeal or Request review button is shown. See '+A('/instagram-account-disabled-vs-suspended-vs-restricted/','disabled vs suspended vs restricted')+'.',
    '<strong>Check the deadline.</strong> Suspension notices carry a date, usually 180 days. Do not wait for it.',
    '<strong>Secure your email.</strong> Make sure you can open the inbox on the account. Instagram’s replies and codes go there. Turn on two-step verification on the email.',
    '<strong>Use a familiar device and network.</strong> Appeal from a phone or computer you have used with the account before.',
    '<strong>Write a short, factual note.</strong> If there is a text box, say who you are, how you use the account and why you believe the decision is wrong. Do not paste a template and do not claim things that are not true.',
    '<strong>Finish any identity check.</strong> If Instagram asks for a code or a video selfie, complete it. See '+A('/guides/instagram-video-selfie-verification/','video selfie verification')+'.',
    '<strong>Submit once.</strong> Keep a screenshot of the confirmation. Repeating the request does not help.',
    '<strong>Watch email and the app.</strong> The answer usually comes by email or on the login screen. Meta does not publish a fixed timeline.',
    '<strong>Keep a record.</strong> Save the dates of each step. If the answer is no, you will need them. See '+A('/instagram-appeal-denied/','after a denied appeal')+'.'])),
  sec('avoid','What to avoid', ul([
    'Deleting posts in a panic. Removing evidence can complicate a later appeal.',
    'Sharing your password or login codes with anyone who offers to help.',
    'Creating a new account just to continue the same activity that was flagged.',
    'Paying someone who says they have a contact at Meta.'])),
  sec('hacked','If the account was hacked', '<p>Start with the undo link in Instagram’s email about the change and instagram.com/hacked before an appeal. See '+A('/guides/hacked-instagram-account-recovery/','hacked account recovery')+'.</p>'),
  sec('help','When to bring in help', '<p>If there is no appeal button, the first appeal was denied or you would rather hand it over, send us the username and the notice. We tell you whether an appeal looks realistic and handle it through Meta’s official process. Main page: '+A('/instagram-account-recovery/','Instagram account recovery')+'.</p>'),
  how(ACCT_STEP1),
  who(['People about to appeal a disabled or suspended Instagram account.','Anyone whose first appeal went unanswered or was denied.','Not for: accounts that were really used for scams or abuse.']),
 ],
 faq=[
  ('What should I do before appealing an Instagram ban?','Screenshot the notice, read the deadline, secure your email, finish any identity check, then submit once with a short factual note.'),
  ('How long do I have to appeal a suspended Instagram account?','The notice shows the date. It is usually 180 days. Do not wait for the last day.'),
  ('Should I write a long appeal?','No. Keep it short, factual and specific to the policy named. Say who you are, how you use the account and why you think the decision was wrong.'),
  ('Can I appeal more than once?','Submit once per notice. Repeated identical requests do not help. If the answer is no, read what it says and decide the next step.'),
  PASSWORD_FAQ, CONTACT_FAQ],
 related=[('/guides/instagram-account-suspended-appeal/','Suspension appeal guide'),('/guides/instagram-account-disabled/','Disabled account guide'),('/ways-to-get-a-banned-instagram-account-back/','Ways to get an account back'),('/instagram-recovery-glossary/','Recovery glossary')]+COMMON[:3],
 relq=[('/how-long-does-an-instagram-appeal-take/','How long an appeal takes'),('/instagram-appeal-form-not-working/','Appeal form not working'),('/guides/instagram-appeal-sent-no-response/','Appeal sent, no response')])

# 6 glossary ----------------------------------------------------------
GLOSS = [
 ('Disabled account','An account Instagram has taken offline for not following its rules. A notice appears at login and the profile is not visible to others.','/guides/instagram-account-disabled/'),
 ('Suspended account','An account under account-level action with a deadline, usually 180 days, to disagree or appeal.','/instagram-account-suspended-180-days/'),
 ('Restricted account or feature limit','An account that still logs in but cannot use a feature, such as messaging new people, for a set period.','/guides/instagram-check-account-status/'),
 ('Action blocked','The message Instagram shows when it limits an action such as following or commenting.','/instagram-we-restrict-certain-activity-action-blocked/'),
 ('Account Status','The Instagram settings screen that lists removed content, feature limits and recommendation eligibility.','/guides/instagram-check-account-status/'),
 ('Strike','A recorded violation. More strikes lead to longer restrictions and, after repeated violations, possible removal.','/guides/instagram-community-guidelines-strikes/'),
 ('Appeal or request for review','The button or form on a notice that asks Meta to look at a decision again.','/instagram-appeal-checklist/'),
 ('Video selfie','An identity check where Instagram asks you to record a short video of your face, turning your head in different directions.','/guides/instagram-video-selfie-verification/'),
 ('Hacked account','An account where someone else changed the password, email or phone number. Recovery starts at instagram.com/hacked.','/guides/hacked-instagram-account-recovery/'),
 ('Memorialized account','An account kept as a tribute after a person has died.','/guides/instagram-memorialized-account/'),
 ('Username claim','Getting a specific handle onto your own profile through a platform process, such as a trademark or impersonation report.','/instagram-username-claim-routes/'),
 ('Trademark (IP) report','A report to the platform that a handle infringes a registered trademark.','/trademark-username-claim/'),
 ('Impersonation report','A report that an account is pretending to be you or your brand.','/report-business-impersonation/'),
 ('Squatted username','A handle held by an account that is parked or unused, often to resell it.','/can-you-claim-a-username-from-an-inactive-instagram-account/'),
 ('Business portfolio','Meta’s container for a business’s Pages, ad accounts and Instagram accounts.','/guides/meta-business-portfolio-restricted/'),
 ('Account Quality','The Meta page that shows restrictions, reasons and review options for business assets.','/guides/meta-account-quality-status-walkthrough/'),
 ('Ad account restriction','A limit on advertising placed on a business portfolio, ad account, Page or personal profile.','/meta-ad-account-restricted-vs-disabled/'),
 ('Meta Verified','Meta’s paid subscription that includes access to account support for eligible profiles.','/compare/'),
]
page(slug='instagram-recovery-glossary', lang='en',
 title='Instagram Account Recovery Glossary | Unbanz',
 desc='Plain definitions of the terms in Instagram and Meta account recovery: disabled, suspended, strike, appeal, username claim, Account Quality and more.',
 h1='Instagram and Meta account recovery glossary.',
 crumb='Recovery glossary', svc='Instagram account recovery',
 hero='Short definitions of the words that appear on Instagram and Meta notices, each linked to the guide that goes deeper.',
 wa='Hey%20Unbanz%2C%20I%20need%20help%20with%20an%20account', ws='unban', subj='Account%20help',
 answer='This glossary defines the terms used on Instagram and Meta account notices: disabled, suspended, restricted, strike, appeal, video selfie, hacked, username claim, trademark report, Account Quality and ad account restriction. Each entry is one or two sentences and links to the guide for that topic.',
 body=[UPD, '<h2 id="terms">Terms</h2><dl>' + ''.join('<dt id="%s"><strong>%s</strong></dt><dd>%s <a href="%s">Read more</a></dd>' % (t.lower().replace(' ','-').replace('(','').replace(')',''), t, d, u) for t, d, u in GLOSS) + '</dl>',
  sec('help','How Unbanz helps', '<p>If a term on your notice is not here or you are unsure what to do next, send us the username and a screenshot. We tell you what it means and whether an appeal looks realistic. Main page: '+A('/instagram-account-recovery/','Instagram account recovery')+'.</p>'),
  how(ACCT_STEP1),
  who(['People reading an Instagram or Meta notice and unsure what it means.','Not for: accounts that were really used for scams or abuse.']),
 ],
 faq=[
  ('What does disabled mean on Instagram?','The account is offline for not following Instagram’s rules. A notice appears at login and the profile is not visible to others.'),
  ('What is an Instagram strike?','A recorded violation. More strikes lead to longer restrictions, and after repeated violations an account may be removed.'),
  ('What is a username claim?','Getting a specific handle onto your own profile through a platform process such as a trademark or impersonation report.'),
  ('What is Account Quality?','The Meta page that lists restrictions on business assets, the reason shown and, where available, a request review button.'),
  CAN_FAQ, CONTACT_FAQ],
 related=[('/instagram-account-disabled-vs-suspended-vs-restricted/','Disabled vs suspended vs restricted'),('/instagram-appeal-checklist/','Appeal checklist'),('/ways-to-get-a-banned-instagram-account-back/','Ways to get an account back'),('/instagram-username-claim-routes/','Username claim routes'),('/meta-ad-account-restricted-vs-disabled/','Ad account restricted vs disabled')],
 relq=[('/guides/','All guides'),('/faq/','FAQ'),('/compare/','Compare options')])
