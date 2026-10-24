EXPAND = {}
def add(slug, secs, faq=None):
    d = dict(secs=secs)
    if faq: d['faq'] = faq
    EXPAND[slug] = d

add('protect-your-business-from-an-instagram-ban', [
 ('audit', 'A quarterly continuity audit',
  '<ol><li>Can you name every person with access, and do they still need it?</li><li>Is the recovery email a business-owned mailbox with two-factor authentication on it?</li><li>When did you last export your data, and where is the file?</li><li>If Instagram disappeared tomorrow, how would your best 100 customers hear from you?</li><li>Have you used any tool that asks for your Instagram password?</li></ol>'
  '<p>Five questions, ten minutes. If you can’t answer one, that’s the next thing to fix.</p>')])

add('instagram-account-restored-next-steps', [
 ('why', 'Why a restored account can fail again',
  '<p>If the account was hacked, the attacker may have tried to leave a way back in: a connected app, a forwarding rule on the email, or a saved device session. If it was restricted for activity, the same behaviour, such as rapid follows or repeated links, will trigger the same system again. Thinking about the cause is more useful than any single setting.</p>'
  '<p>Keep a note of the date it was restored and what you changed. If something odd happens in the next few weeks, you’ll know where to start looking.</p>')])

add('instagram-harassment-dms-what-to-do', [
 ('evidence', 'Building a record that helps later',
  '<p>A tidy record turns a messy situation into something police, a school, an employer or a platform can act on. Put screenshots in one folder named by date. Note the username, profile link, date and time, and what each message said. Keep the originals; don’t crop out usernames. If a message disappears, note that it did. If the person is someone you know, note how.</p>')])

add('instagram-scam-dm-what-to-do', [
 ('checks', 'Ten-second checks before you respond to any offer',
  '<ul><li>Does the username match the real brand’s verified profile, character for character?</li><li>Did they contact you first about something you never applied for?</li><li>Does it ask you to leave Instagram for another app or a link?</li><li>Is there urgency, a deadline or a penalty?</li><li>Is payment requested by transfer, gift card or crypto?</li></ul>'
  '<p>Two or more “yes” answers is enough reason to stop. Contact the brand through the contact details on its official website, not the ones in the message.</p>')])

add('sextortion-what-to-do-on-instagram', [
 ('pattern', 'How these threats usually unfold',
  '<p>Sextortion often starts with a friendly new account, sometimes using attractive photos, that quickly moves the chat to a more private setting, shares an intimate image first and asks for one in return. The moment an image is sent, the tone changes to threats: pay, send more or the image goes to your followers and family. Time pressure is part of the technique. Knowing the pattern helps you step out of it, because the threats are designed to make you panic rather than think.</p>'),
 ('parents', 'If you’re a parent or carer',
  '<p>Stay calm and make it clear the young person isn’t in trouble. Help them stop contact, save evidence and report. For under-18s, NCMEC’s Take It Down service and the police are the main routes. Blame shuts conversations down, and the first reaction you give often decides whether they tell you the whole story.</p>')])

add('snapchat-account-hacked', [
 ('signs', 'Signs someone else is in your account',
  '<ul><li>Snaps or Stories you didn’t send.</li><li>New friends or removed friends you didn’t change.</li><li>A password-changed or login email you didn’t trigger.</li><li>Being logged out and unable to log back in.</li><li>Friends telling you they got odd links or requests for money from you.</li></ul>'
  '<p>If you’re logged out and can’t get back in, work through the official account-access help first, and keep note of the date you lost access.</p>')])

add('snapchat-device-banned-appeal', [
 ('why', 'Why device-level restrictions exist',
  '<p>Snapchat applies some restrictions to the device so that someone whose account has been removed can’t simply start again on the same phone. It’s also why a second-hand phone can arrive with a problem. Snapchat’s terms don’t allow unofficial apps and running several accounts to get around enforcement, and those are the kinds of behaviour that can lead to device-level action. Keeping to one account, using the official app and not buying or selling accounts keeps you well clear.</p>'),
 ('ask', 'Before you buy a used phone',
  '<p>Open Snapchat on the phone in the shop, if the seller allows it, and try logging in. If you see an error, don’t buy it. It’s a thirty-second test that avoids a problem you can’t easily fix afterwards.</p>')])

add('snapchat-change-username-and-delete-account', [
 ('compare', 'Which change is right for you?',
  '<ul><li><strong>Want a different name that friends see:</strong> change your display name. It doesn’t affect your username or friends.</li><li><strong>Want a new handle:</strong> change the username, once, if the yearly limit allows.</li><li><strong>Want a break:</strong> log out and delete the app, or mute notifications. Deletion is not a pause.</li><li><strong>Want a fresh start:</strong> download your memories, delete the account and wait out the 30 days before creating a new one.</li></ul>')])

add('threads-deactivate-or-delete', [
 ('export', 'What to save before you go',
  '<p>Download your Threads information from Accounts Center, including posts and replies, should you want them later. Note down links you’ve shared in posts or your bio that people may still follow, and consider adding a pointer on your Instagram profile if you want followers to find you elsewhere. If you use Threads for work, tell customers where else to reach you.</p>'),
 ('link', 'How Threads and Instagram are linked',
  '<p>A Threads profile is created from an Instagram account, so the two share some details like username and bio by default. Actions on one can touch the other, which is why the delete screens spell out what will be removed. Slow down on those screens and read each line; they’re the only guard against deleting more than you intended.</p>')])

add('account-recovery-scams-fake-hackers-warning', [
 ('script', 'A typical scam conversation',
  '<p>It begins with a comment under your post or a DM from an account with a name like “Account Recovery Expert”, offering to get the account back. The first request is small, perhaps a screenshot, then your username, then “verification” through a code sent to your phone, which is really the login code for your own account. Next comes a fee in crypto or gift cards. After payment, there’s a second fee for “release”. Each step feels reasonable because the previous one cost you something. Recognising that escalation pattern is the best defence.</p>')])
