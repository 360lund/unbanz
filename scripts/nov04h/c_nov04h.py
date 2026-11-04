# -*- coding: utf-8 -*-
"""2026-11-04 (h): supporting pages for the two top lead clusters."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dd29'))
from fams import *
from lib import PAGES
NOPASS = ('Does anyone need my password to help?', 'No. Never share your password or login codes. Anyone who asks for them is a risk.')
IGAPP = A('/guides/instagram-account-suspended-appeal/', 'Instagram suspended: how to appeal')
FBAPP = A('/guides/facebook-account-disabled-appeal/', 'Facebook disabled: how to appeal')
FBREJ = A('/guides/facebook-disabled-appeal-rejected/', 'Facebook appeal rejected')
IGNR = A('/guides/instagram-appeal-sent-no-response/', 'Instagram appeal sent, no reply')
page('instagram-appeal-what-to-write', 'igsusp', 'What to Write in an Instagram Appeal',
 'What to write when you appeal an Instagram suspension or disabled account. A short structure, an example in plain words, and what to leave out.',
 'What to write in an Instagram appeal', 'Instagram appeal: what to write',
 'Short, calm and accurate works better than long and angry. Here is a simple structure you can write in your own words.',
 'In an Instagram appeal, say who you are, that the account is yours, and why you think the decision is wrong, in three or four sentences. If you were hacked first, say when. Do not copy templates from the internet, threaten legal action or admit to things you did not do. Then complete any selfie or ID check.',
 [('Three or four sentences', 'Short and specific.'), ('Facts, not anger', 'Dates and what happened.'), ('Then the ID step', 'Selfie or ID if asked.')],
 [S('A simple structure', ol(['Who you are and that this is your account, with the username.', 'What the account is used for: personal, a creator, or a small business.', 'Why you believe the decision is a mistake, in one or two plain sentences.', 'If it applies: the date you lost control after a hack.'])),
  S('What to leave out', ul(['Copied templates. Many people send the same text.', 'Threats, insults or legal demands.', 'Admitting to rules you did not break.', 'Passwords, codes or links.'])+'<p>Related: %s and %s.</p>' % (IGAPP, IGNR))],
 [('Can I write the appeal in my own language?', 'Yes. Clear and accurate matters more than the language.'),
  ('Should I mention followers or income?', 'Briefly, if it explains what the account is for. It does not change the rules.'), NOPASS],
 ['Instagram users writing a first appeal.', 'Creators and small businesses whose account is their shop.', 'People who were hacked and then suspended.'])
page('facebook-disabled-appeal-what-to-write', 'fbdis', 'What to Write in a Facebook Disabled Appeal',
 'What to write when you appeal a disabled Facebook account. A short structure, what to say about ID or a hack, and what to leave out.',
 'What to write in a Facebook disabled appeal', 'Facebook appeal: what to write',
 'A Facebook appeal is read quickly. Keep it short, true and in your own words.',
 'In a Facebook disabled appeal, confirm the profile is yours and uses your real name, say in one or two sentences why the decision looks wrong, and mention a hack with the date if there was one. Upload a clear ID with the same name if asked. Leave out templates, threats and anything untrue.',
 [('Real name, real ID', 'Name must match.'), ('One or two reasons', 'Plain and specific.'), ('Hack date', 'If it applies.')],
 [S('A simple structure', ol(['That this is your personal profile and the name is your real name.', 'What you use it for, including Pages or ads you manage.', 'Why the decision looks wrong, in one or two sentences.', 'If it applies: when the account was hacked and what changed.'])),
  S('What to leave out', ul(['Copied templates.', 'Threats or legal demands.', 'Statements that are not true.', 'Passwords, codes or links.'])+'<p>Related: %s and %s.</p>' % (FBAPP, FBREJ))],
 [('Does Facebook read the appeal text?', 'Some appeals have a text box and some only ask for ID. Where there is a box, keep it short.'),
  ('Which ID should I upload?', 'A government photo ID with the same name as the profile, such as a passport or driving licence.'), NOPASS],
 ['Facebook users writing a first appeal.', 'People who run Pages or ads from a disabled profile.', 'People who were hacked and then disabled.'])
page('facebook-appeal-sent-no-response', 'fbdis', 'Facebook Appeal Sent, No Response: What Now',
 'You appealed a disabled Facebook account and heard nothing. Where to check, how long it can take, and what not to do while you wait.',
 'Facebook appeal sent and no response?', 'Facebook appeal, no reply',
 'Silence after a Facebook appeal is common. Here is where to look and what to avoid while you wait.',
 'If you appealed a disabled Facebook account and heard nothing, check the email on the account including spam, your Support Inbox if you can log in, and the notice screen for a status. Meta does not publish a timeline. Do not open a new profile or send the same appeal many times.',
 [('Check email and spam', 'Replies often land there.'), ('Support Inbox', 'If you can still log in.'), ('No new profile', 'It can be removed too.')],
 [S('Where to check', ul(['The email address on the account, including spam and promotions.', 'The Support Inbox, if you can log in.', 'The disabled notice itself, for a status or deadline.'])),
  S('What to avoid', ul(['A new profile with the same name or photos.', 'Sending the same appeal again and again.', 'Paying anyone in DMs who says they can push it through.'])+'<p>Related: %s and %s.</p>' % (FBAPP, FBREJ))],
 [('How long does a Facebook appeal take?', 'Meta does not publish a timeline. Some replies come in days, others take weeks.'),
  ('Can Unbanz check where it stands?', 'Yes. We look at the notice and tell you honestly whether another official route fits. Terms are agreed with you before any work starts.'), NOPASS],
 ['Facebook users waiting on an appeal.', 'Small businesses whose Pages sit on the profile.', 'Anyone deciding whether to get help.'])
