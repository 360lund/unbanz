EXPAND = {}

EXPAND['instagram-suspicious-login-alert'] = dict(secs=[
 ('signs', 'Signs the account is already compromised',
  '<p>Sometimes the alert arrives after the damage. Look for a handful of signals: posts or Stories you didn’t make, DMs sent to people you don’t talk to, a changed bio or link, new accounts followed in bulk, or emails from Instagram about a changed email address or phone number. Any one of these means you should treat the account as taken over, even if you can still log in. Change the password, log out all sessions, and tell followers through another channel so they don’t click links sent from your account.</p>'
  '<p>If you run the account with a team, ask each person to check their own devices and email. A single infected laptop or a reused password on one team member’s other account is a common way in.</p>'),
 ('email', 'Step 5: Secure the email behind the account',
  '<p>An Instagram password reset goes to your email, so a hijacked mailbox is a hijacked Instagram. Change that password too, turn on two-factor authentication on the email itself, and check the mailbox for forwarding rules or filters you didn’t create. Attackers sometimes add a rule that hides messages from Instagram so you never see the warnings.</p>')],
 faq=[('Should I uninstall and reinstall the app?', 'It won’t fix a compromised password on its own. Do it only as housekeeping after you have changed your password and logged out other sessions.')])

EXPAND['instagram-download-your-data-backup'] = dict(secs=[
 ('read', 'What’s inside the file and how to use it',
  '<p>An HTML export opens in a browser like a small website, with folders for content, messages, followers and ads information. The JSON version is the same data in a form that scripts and spreadsheets can read. Photos and videos sit in media folders. Messages appear as conversations. Followers and following lists appear as lists of usernames with the time they were added.</p>'
  '<p>Two practical uses: a follower and following list gives you a record of who your audience was if the account is lost, and a messages export lets you find customer details and agreed prices. If you run a business, keep these in your own system, not just in the file.</p>'),
 ('keep', 'What a business should keep outside Instagram',
  '<p>For a business account, treat Instagram as rented space. Keep original media in cloud storage, a customer contact list in your own tool, a record of who has admin access to the linked Page and ad account, and a list of your bio links and highlights. If Meta restricts an account, this is what lets you keep trading while you appeal.</p>')],
 faq=[('How often should I export my data?', 'Every few months, and before any major change. Date the files so you know which is newest.')])

EXPAND['instagram-cant-log-in-password-incorrect'] = dict(secs=[
 ('msgs', 'Reading the error message',
  '<ul><li><strong>“The password you entered is incorrect.”</strong> Wrong password or wrong login method. Use a login link.</li><li><strong>“We can’t find an account with that username.”</strong> A typo, a changed username or an account that no longer exists. Try your email or phone, and ask a friend to look for your profile.</li><li><strong>“Please wait a few minutes before you try again.”</strong> Too many attempts. Wait and try once.</li><li><strong>“Your account was disabled / suspended / locked.”</strong> A different problem with its own appeal route. See the guides on disabled, suspended and locked accounts.</li><li><strong>“Sorry, there was a problem with your request.”</strong> Often a temporary error. Update the app and try again from another network.</li></ul>'
  '<p>Reading the exact wording first saves you from fixing the wrong thing. A password reset can’t solve a disabled account, and an appeal can’t solve a mistyped password.</p>')])

EXPAND['instagram-change-email-or-phone-securely'] = dict(secs=[
 ('team', 'If a team or agency uses the account',
  '<p>Don’t hand your login details to a freelancer or agency. For a business account, give people access through the Page, Business portfolio or the account’s professional tools where possible, so you can remove them without changing the recovery email. If a team member’s email is currently the account’s recovery address, move it to one you own now. People change jobs and mailboxes get deleted, and recovery is hardest when the only inbox that could confirm ownership belongs to someone who has left.</p>'),
 ('mistakes', 'Three mistakes that cause lockouts',
  '<ol><li>Removing the old contact before confirming the new one, leaving no valid method.</li><li>Typing the new email with a small typo, so the confirmation message goes nowhere.</li><li>Changing a number while two-factor codes still go to the old one.</li></ol>'
  '<p>Check each address twice and keep the old inbox open until the new one has confirmed.</p>')])

EXPAND['instagram-id-verification-request'] = dict(secs=[
 ('name', 'If the name on your ID doesn’t match the account',
  '<p>This is common: a stage name, a business name or a married name. Instagram’s help page asks for documents where the name matches the account, but you can send documents that show the name you use. Two non-government documents, such as a bank statement and a utility bill, can together show the name and your photo or date of birth. Choose ones that are current and clearly readable, and follow the on-screen wording about what is acceptable in your country.</p>'
  '<p>If the account name is a brand and the ID is your personal name, explain the link in any free-text box the form provides. Keep it factual and short.</p>')])

EXPAND['instagram-deactivate-or-delete-account'] = dict(secs=[
 ('compare', 'A quick comparison',
  '<ul><li><strong>Deactivate:</strong> hidden profile, nothing erased, undone by logging in.</li><li><strong>Delete:</strong> a countdown (about 30 days, varying by region), cancellable by logging in during it, then permanent.</li><li><strong>Disabled by Instagram:</strong> not something you chose. It’s a decision by Instagram, with its own appeal route.</li></ul>'),
 ('biz', 'Before deleting a business account',
  '<p>Check three things: whether the account is linked to a Facebook Page and ad account you still want, whether any scheduled posts or tools depend on it, and whether customers use your handle in print. Export your data, announce the change on another channel, and give it a week or two before you press delete.</p>')])

EXPAND['instagram-memorialized-account'] = dict(secs=[
 ('looks', 'What a memorialized account looks like',
  '<p>The word “Remembering” appears next to the name on the profile. The profile is protected: no one can log in, and the content stays visible to the people it was shared with. Existing posts, likes and followers remain as they were, so it works as a quiet place for people to look back.</p>'),
 ('privacy', 'Why Instagram won’t hand over the login',
  '<p>Instagram doesn’t share passwords with anyone, including close relatives. The reason is privacy: the account holds private messages with other people who never agreed to share them. Instead the help pages offer memorialization or removal. If a family member needs a specific photo or video, the Help Center is the place to ask about options, and a request for content from the account is handled separately from memorialization.</p>'),
 ('talk', 'A note on timing and tone',
  '<p>There’s no rush. The request forms are available whenever you’re ready, and Meta doesn’t publish a timeline for processing. If a profile is being used to spam friends or upset family in the meantime, use the report option on the profile to flag it.</p>')])

EXPAND['instagram-check-account-status'] = dict(secs=[
 ('scen', 'Four common results, and what to do',
  '<ul><li><strong>“Your content was removed.”</strong> Open the item, read the policy, and request a review only if you believe it was a mistake.</li><li><strong>“You can’t use this feature.”</strong> Read the end date. Avoid the activity that triggered it, such as mass following, until the limit lifts.</li><li><strong>“Your content isn’t eligible to be recommended.”</strong> Look for the item named and remove or edit it, or request a review where offered.</li><li><strong>Everything is clear.</strong> Then the problem is elsewhere: a login issue, a reach issue or an outage. Check Instagram’s status and your Insights.</li></ul>'),
 ('hist', 'Keep your own record',
  '<p>Screenshots of Account Status, with the date, build a record you can use later. If your account is ever restricted, a timeline showing earlier removals, limits and appeals makes your next appeal easier to write and helps you see patterns, such as a certain type of post that keeps being flagged.</p>')])

EXPAND['instagram-reach-drop-recommendation-eligibility'] = dict(secs=[
 ('audit', 'A 14-day audit routine',
  '<ol><li><strong>Days 1–2:</strong> check Account Status and screenshot it. Note the date reach fell in Insights.</li><li><strong>Days 3–5:</strong> review your last 10 posts. Mark any with watermarks, reposted clips, small or stretched video, or sensitive topics.</li><li><strong>Days 6–10:</strong> post two or three original pieces, with nothing borrowed, and a clear, specific caption.</li><li><strong>Days 11–14:</strong> compare non-follower reach on the new posts against the old ones.</li></ol>'
  '<p>If non-follower reach recovers, you found the problem. If it doesn’t, keep the pattern going; reach also moves with audience, season and platform changes that have nothing to do with you.</p>'),
 ('normal', 'When a drop is normal',
  '<p>Reach changes after Instagram updates how it ranks content, when trends shift, when your audience changes, or after a long period without posting. A dip across many creators at once points to a platform change, not a penalty. Only an Account Status notice means your account itself was limited.</p>')])

EXPAND['instagram-copyright-removed-content'] = dict(secs=[
 ('avoid', 'How to avoid claims in future',
  '<ul><li>Use <strong>original footage and audio</strong> wherever you can.</li><li>For music, use the in-app library as intended, and remember that licensing differs by account type.</li><li>Get <strong>written permission</strong> before reposting someone’s work, and credit them.</li><li>Keep a folder with licences or receipts for stock footage and fonts.</li><li>Keep clips of films, sport and TV off your account unless you hold the rights.</li></ul>'
  '<p>For brands, a short internal checklist before posting is cheaper than losing a campaign.</p>'),
 ('who', 'Who actually made the claim?',
  '<p>The notice names the person or company who reported the content. That matters. If it’s a record label, a photographer or a studio, the claim is likely automated and may be accurate. If it’s an individual, you may be able to resolve it directly with a polite message. Never contact them in a way that could look like harassment.</p>')])

EXPAND['instagram-removed-post-or-reel-appeal'] = dict(secs=[
 ('policy', 'Read the policy that was applied',
  '<p>Every removal cites a part of the Community Guidelines, such as nudity, bullying, spam, dangerous organisations or false information. Open that section and read it as if you’d never seen your post. Many removals involve context that automated systems cannot read: satire, news reporting or quoted language. If the policy clearly covers your post, don’t appeal; reshape the idea. If your post fits an exception the policy describes, an appeal is reasonable.</p>'),
 ('edit', 'Posting the idea again, properly',
  '<p>If the idea is fine and the execution wasn’t, you can share a new version that follows the rules. Change what actually triggered the removal, such as a caption, a thumbnail or a sound, and don’t post the identical file. Posting the same content again is the fastest way to turn one removal into a pattern.</p>'),
 ('track', 'Track your removals',
  '<p>Keep a simple note of each removal: date, policy, and whether you appealed. If you ever need to appeal a bigger decision, such as a restriction, you’ll be able to show that earlier issues were resolved or accepted.</p>')])

EXPAND['instagram-business-vs-creator-account'] = dict(secs=[
 ('pick', 'Quick decision checklist',
  '<ul><li>You sell products or services and want buttons for calls, directions or bookings: <strong>Business</strong>.</li><li>You plan to run ads regularly: <strong>Business</strong>, and set up a Page and ad account properly.</li><li>You are a person-led brand with a big inbox and collaborations: <strong>Creator</strong>.</li><li>You want the widest music choice for Reels: <strong>Creator</strong> may fit better.</li><li>You want a private account: <strong>Personal</strong>. Professional accounts are public.</li></ul>'),
 ('bothsides', 'Mixed accounts: a person who is also a brand',
  '<p>Many small brands are one person. If you post as yourself and sell sometimes, pick the type that matches your main use and put the other details in the bio. If you later need to run proper ads, switch and set up your Page and ad account then. Switching doesn’t remove your posts or followers.</p>')])
