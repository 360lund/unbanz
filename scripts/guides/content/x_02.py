EXPAND = {}
def add(slug, secs, faq=None, intro=None):
    d = dict(secs=secs)
    if faq: d['faq'] = faq
    if intro: d['intro'] = intro
    EXPAND[slug] = d

add('facebook-two-factor-lost-access', [
 ('why', 'Why the SMS code is the weakest option',
  '<p>Text-message codes depend on a phone number that can be lost, recycled or intercepted through a SIM swap. An authentication app generates codes on the device itself and works without signal, which is why Meta’s own pages steer people toward apps and security keys when you set things up. If you’re still using SMS only, treat the lockout as a reason to add a second method before you need it.</p>'
  '<p>A security key is stronger again. It’s a small physical device you plug in or tap, and it can’t be tricked by a fake login page. Keep one on your keyring and one in a drawer.</p>')],
 faq=[('Can I use the same authenticator app for Facebook and Instagram?', 'You can run several accounts in one app, but each account needs its own setup. Back up the app’s own recovery options, or you’ll just move the lockout there.')])

add('facebook-lost-access-to-email-or-phone', [
 ('inventory', 'Build an inventory before you start',
  '<p>People waste recovery attempts because they can’t remember what’s on the account. Before you open the identify page, write down every email address you’ve owned since you joined, including school and work ones that may be closed, plus every phone number. Add your profile URL or username, the approximate join year and names of two or three friends. Those details help you choose the right search and answer questions in the process.</p>'
  '<p>Also try each address on the identify page one at a time. An old address that’s no longer yours may still be the one linked, and a hit tells you which contact points the account has.</p>'),
 ('device', 'Why the device matters',
  '<p>Facebook’s own help pages recommend starting recovery from a device and location you’ve logged in from before. A familiar device is a quiet signal that the person asking is the person who owns the account. It’s also why switching between your laptop, phone and a friend’s device halfway through can slow things down.</p>')],
 faq=[('Can a friend help me recover it?', 'They can lend you their device or give you your profile link. They can’t verify the account for Facebook, because the trusted contacts feature has been discontinued.')])

add('facebook-id-upload-request', [
 ('scam', 'How to tell a real request from a fake one',
  '<p>Real requests appear after you log in or when you follow a recovery flow you started yourself. Fake ones tend to share the same traits: urgency such as “your account will be deleted in 24 hours”, a link to a lookalike domain, a request to reply with a photo of your ID in a chat, or a demand for a fee. Facebook’s email addresses end in facebookmail.com or similar official domains, but even then, don’t follow the link. Open the app or type facebook.com yourself and look for the same request there.</p>'
  '<p>Scammers also target Page owners with “copyright violation” warnings that ask for ID. If the notice doesn’t appear in your Support Inbox, treat it as suspicious.</p>')],
 faq=[('Can I cover part of my ID?', 'Only if the screen allows it. Hiding the name, photo or date that Facebook needs will make the check fail.')])

add('facebook-name-change-rules', [
 ('examples', 'What passes and what gets flagged',
  '<p>A few examples make the rules easier to apply. “Ana Maria Lopez” and “Ana Lopez” are both fine if you use either one in real life. “Dr. Ana Lopez” breaks the title rule. “Ana Lopez ✨” breaks the symbol rule. “AnaLopez” in odd capitals can be flagged. “Ana Lopez Photography” belongs on a Page, not a profile. If your legal name includes characters that look unusual in Latin script, you can keep them in one language; mixing scripts is what gets flagged.</p>'
  '<p>If you’re known by a different name, such as a married name, a chosen name or a nickname, a profile can use it as long as it’s the name your friends and family know you by. Facebook may ask for documents that show that name if there’s a challenge.</p>')],
 faq=[('Can I add another name without changing my main one?', 'Yes. Facebook lets you add a nickname, maiden name or pronunciation as an additional name in your profile’s About details.')])

add('facebook-deactivate-or-delete-account', [
 ('checklist', 'Before you go: a short checklist',
  '<p>Run through it once, and you’ll avoid the most common regrets:</p>'
  '<ul><li>Download a copy of your information from Accounts Center and confirm the file opens.</li><li>List every site or app where you signed in with Facebook and move each to an email login.</li><li>Check for Pages, groups and ad accounts you admin. Add a replacement admin or transfer ownership.</li><li>Tell people where else to reach you.</li><li>If you sell on Marketplace or take payments, finish open orders.</li></ul>'
  '<p>Deactivation is the safer first move. If after a few weeks you still want to leave, you can come back and delete.</p>')],
 faq=[('Is it better to deactivate first?', 'Usually, yes. It’s reversible, and it gives you time to check that you haven’t left something important behind.')])

add('facebook-memorialized-legacy-contact', [
 ('talk', 'Talking with family before you decide',
  '<p>Memorial or deletion is a personal decision, and families sometimes disagree. A memorialized profile can be a place for friends to share memories. For others, seeing the account is painful. If you’re setting up your own preference, tell your family which you chose and why, and tell the legacy contact so it doesn’t come as a surprise.</p>'
  '<p>Think about what’s in the account too. Photos and messages may matter to relatives, so decide whether your legacy contact should be allowed to download an archive. If you don’t allow it, that content isn’t available to them later.</p>')],
 faq=[('Do I need a legacy contact to be memorialized?', 'No. Anyone can request memorialization with proof of death, but a legacy contact gives you control over how it looks.')])

add('facebook-suspicious-login-active-sessions', [
 ('read', 'Reading the session list like a professional',
  '<p>For each row, ask three questions. Do I recognise the device type? Was I using Facebook at that time? Does the place make sense, remembering that mobile networks often route traffic through another city? A row labelled with your usual phone model and a nearby city is almost always you. A browser on a device you don’t own is not.</p>'
  '<p>Don’t forget old sessions on devices you’ve sold or lent. Logging out of those is routine hygiene even if nothing is wrong.</p>'),
 ('pages', 'Check what the account can reach',
  '<p>If you manage Pages or ads, a compromised profile puts them at risk too. Open Meta Business Suite and look at who has access to each Page, then check payment methods and recent spending in Ads Manager. Remove people you don’t recognise.</p>')])

add('facebook-support-inbox-violations', [
 ('read', 'How to read a violation notice',
  '<p>A useful notice names the content, the policy area and the action. Write those three down. If the policy cited seems unrelated to what you posted, that’s worth noting in your review request, in a calm sentence. If it matches, remove or edit similar content so a pattern doesn’t build. For a Page, check whether the flagged item is old, since an old post can still count.</p>'
  '<p>Pay attention to the action as well. A removed post, a Page-level restriction and a feature limit are different things with different ways back.</p>'),
 ('team', 'When several people run the account',
  '<p>Agree on one person to check the inbox weekly and log what’s there. Repeated issues on a Page often come from several editors posting different kinds of content with no shared checklist. A short list of dos and don’ts for the team prevents more problems than any appeal.</p>')])

add('facebook-page-hacked-admin-removed', [
 ('why', 'How these takeovers usually happen',
  '<p>The common routes are a phished admin login, a reused password from another breached site, a malicious browser extension, and fake “policy violation” messages that ask admins to log in through a copied page. Attackers often add themselves as admins, remove everyone else and then run ads or change the Page name. Knowing the route helps you stop it recurring: each admin should use a unique password, an authentication app, and a clean device.</p>'),
 ('docs', 'Preparing documents for a dispute',
  '<p>Collect them while you wait, so you’re ready when asked: your government ID, business registration or trade licence, domain or website ownership records, invoices for ads or services connected to the Page, and a signed letter explaining your relationship to the Page. Names across documents should match.</p>')])

add('facebook-page-admin-access-lost', [
 ('cheat', 'A realistic order of attack',
  '<p>Work from the gentlest option upward. First, a polite written request to the admin. Second, a request to someone higher in that organisation, such as the agency’s director or your former employer’s manager. Third, Facebook’s access request. Fourth, the formal dispute. Keeping each step in writing gives you a clean record if you reach the dispute stage.</p>'
  '<p>If the person who holds access is simply unreachable, say a freelancer who has gone quiet, note the dates you tried contacting them. That helps a dispute make sense.</p>')])

add('facebook-marketplace-restricted', [
 ('habits', 'Habits that keep Marketplace selling healthy',
  '<ul><li>Use your own photos of the actual item, not catalogue images.</li><li>Price honestly. Placeholder prices such as $1 to attract clicks can be flagged.</li><li>Don’t post the same item many times; update the original listing.</li><li>Keep chats on Messenger where Facebook’s safety tools apply, and be cautious about overpayment requests or links to outside payment pages.</li><li>Reply to buyers. Unanswered messages and disputes are a common source of reports.</li></ul>'
  '<p>If you sell regularly, read the commerce policies once a quarter. They change, and the prohibited-items list is long.</p>')])

add('report-scam-ad-or-fake-page-facebook', [
 ('evidence', 'What to save before you report',
  '<ul><li>Screenshots showing the ad or Page, with the date visible.</li><li>The URL of the Page and of any website the ad sends people to.</li><li>The name of the advertiser (shown in the ad’s three-dot menu or the Page transparency section).</li><li>Payment details, order numbers and messages if anyone was scammed.</li></ul>'
  '<p>Keep these in one folder. They’re useful for Facebook, your bank and, if money was lost, your local police or consumer protection agency.</p>')])

# Instagram thin ones
add('instagram-fake-ban-or-copyright-emails', [
 ('anatomy', 'Anatomy of a fake ban email',
  '<p>Phishing messages tend to follow a script. They say your account will be disabled soon, give a short deadline, include a button labelled “Appeal” or “Verify now”, and point to a page that asks for your username and password, sometimes your two-factor code as well. The sender address may look close, such as support@instagram-help.example, and the page address often uses an odd domain or a shortened link.</p>'
  '<p>Genuine Instagram notices don’t need your password to be typed anywhere other than the Instagram login screen, and they never ask you to pay to avoid a ban. If you’re unsure, open the app and check Account Status and the Recent emails list. If the message isn’t there, you can treat it as a fake.</p>'),
 ('team', 'If you run an account for a business',
  '<p>Tell your team about these scams. A common version targets business accounts with a “copyright infringement” notice that links to a form. One tired admin entering the password is enough to lose the account. Agree on a rule that nobody enters Instagram credentials from an email link, ever.</p>')])

add('instagram-removed-post-or-reel-appeal', [
 ('writing', 'What to write if there is a text box',
  '<p>Not every flow offers one, but if it does, keep it to three sentences: what the content is, why it follows the guideline cited, and any context that wasn’t visible such as a news setting, an educational purpose or an item you own. Avoid anger and avoid long histories. Reviewers read many requests; a clear sentence is easier to act on.</p>'),
 ('re-upload', 'Should you re-upload instead?',
  '<p>Usually not. Re-posting the same content after removal can be treated as a repeat of the violation, and it can reduce your chances of a good outcome. If you edit a post to fix a genuine issue, such as removing a music clip or a link, that’s different from re-uploading unchanged material. Wait for the review result before you decide.</p>')])

add('instagram-business-vs-creator-account', [
 ('migrate', 'What changes when you switch, and how to switch safely',
  '<p>Switching account types is reversible, but a few things shift at the moment of change. Switching a private account to a professional one makes it public. Insights start collecting from the switch, not before. Features tied to a type, such as shopping or certain contact buttons, appear or disappear. If you rely on scheduled content or third-party tools, check that they still connect afterwards.</p>'
  '<p>Before switching, note your current settings and take a screenshot of your profile and contact options so you can restore them if needed.</p>'),
 ('team', 'Access, roles and security',
  '<p>If several people work on the account, a Meta Business portfolio gives clearer roles than sharing a password. Whichever type you use, turn on two-factor authentication and keep a record of who has access.</p>')])

add('instagram-reach-drop-recommendation-eligibility', [
 ('compare', 'Comparing before you panic',
  '<p>A reach drop is only meaningful against your own baseline. Compare at least four weeks of the same metrics, such as accounts reached from non-followers, in the same format. A single reel underperforming isn’t a signal. If several posts across formats all fall at once, check Account Status and look for recent changes: a new audio style, more outbound links, posting frequency, or a change in topic.</p>'
  '<p>Seasonality matters as well. Holidays, school terms and big news days move attention away from many accounts at once.</p>')])

add('instagram-check-account-status', [
 ('habit', 'Make it a monthly habit',
  '<p>Open Account Status on the first of each month and note what it says. Write down the date and any removed content. A quick routine means you see a problem within days instead of discovering weeks later that a feature was limited.</p>'
  '<p>For team accounts, add the check to the same list as posting schedules and give one person responsibility for it.</p>')])
