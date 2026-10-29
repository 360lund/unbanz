# -*- coding: utf-8 -*-
"""Oct 29: rewrite two appeal guides as self-serve (steps first, paid option only near the end). Idempotent: rewrites hero copy + article."""
import re, os
ROOT = '/workspace/site'
EXT = lambda u, t: '<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>' % (u, t)

def toc(items):
    return '<nav class="guide-toc" aria-label="Contents"><p>In this guide</p><ol>' + ''.join('<li><a href="#%s">%s</a></li>' % i for i in items) + '</ol></nav>'

def sec(i, t, body): return '<h2 id="%s">%s</h2>%s' % (i, t, body)
def ol(*xs): return '<ol>' + ''.join('<li>%s</li>' % x for x in xs) + '</ol>'
def ul(*xs): return '<ul>' + ''.join('<li>%s</li>' % x for x in xs) + '</ul>'

IG = dict(
 quick='tap the appeal option on the suspension notice, complete any identity check, and submit once before the deadline on your screen. Then watch your email and the app.',
 intro='You can do this yourself in a few minutes. The steps below follow Instagram’s own flow.',
 secs=[
  ('before', 'Before you start', ul(
    'Screenshot the full notice, including the deadline and any policy named.',
    'Make sure you can receive codes on the email and phone linked to the account.',
    'Use your usual phone, the latest app version and your normal network.',
    'Stop any automation or scheduling tool that logs in with your password.')),
  ('steps', 'How to appeal, step by step', ol(
    '<strong>Log in.</strong> Open the Instagram app or instagram.com and log in to the suspended account. The appeal option only shows once you are logged in.',
    '<strong>Read the notice.</strong> Note the reason given and the number of days left.',
    '<strong>Tap the appeal option.</strong> It is usually labelled <em>Appeal</em> or <em>Disagree with decision</em>. Go through every screen until you see a confirmation.',
    '<strong>Confirm it is you.</strong> You may be asked for a code or a video selfie. Do the selfie in good light with nothing covering your face. Instagram’s ' + EXT('https://help.instagram.com/1053588012132894', 'video selfie help page') + ' explains the check.',
    '<strong>Add a short note if there is a box.</strong> Two or three factual sentences are enough (see below).',
    '<strong>Wait.</strong> Check the email on the account, including spam, and the app. Instagram does not publish a review time.')),
  ('what-to-write', 'What to write', '<p>If you get a text box, keep it short and factual:</p>' + ul(
    'You own the account and how you use it (personal, creator, business).',
    'Why the reason given does not fit, for example a misread post or a login that was not you.',
    'Anything you already removed or fixed.') + '<p>No threats, templates, all-caps or long emotional messages. Never include your password or codes.</p>'),
  ('deadline', 'The deadline', '<p>The countdown on your screen is a deadline to appeal, not a waiting period. The account does not come back by itself when it ends. Facebook’s Help Center describes the same window for suspended accounts: you can ' + EXT('https://www.facebook.com/help/103873106370583', 'appeal within 180 days') + ', and if you don’t, or the appeal fails, the account is permanently disabled. Instagram does not print one fixed number for every account, so go by your own notice and appeal early.</p>'),
  ('avoid', 'What to avoid', ul(
    '<strong>Waiting.</strong> Appeal early so verification is not rushed.',
    '<strong>Making a new account.</strong> Meta disables accounts created to get around restrictions.',
    '<strong>Stopping halfway.</strong> Only a confirmation screen means the appeal was sent.',
    '<strong>Appeal links from DMs or emails.</strong> Fake appeal pages steal logins. Start from the app or help.instagram.com.',
    '<strong>Sharing your login.</strong> No genuine helper needs your password or codes.')),
  ('why', 'Why accounts get suspended', '<p>Common reasons named on notices include impersonation, hateful conduct, threats, graphic content and spam-like or inauthentic activity. Some suspensions come from automated systems, and some follow a hack. See ' + '<a href="/guides/why-instagram-bans-accounts/">why Instagram bans accounts</a> and the ' + EXT('https://help.instagram.com/477434105621119', 'Community Guidelines') + '.</p>'),
  ('after', 'After a decision', '<p><strong>Approved:</strong> remove what likely triggered it (automation apps, bought engagement, repeated messages) and review your security settings.</p><p><strong>Rejected:</strong> Meta treats the decision as final and the in-app option usually disappears. If the account was hacked before the suspension, try ' + EXT('https://www.instagram.com/hacked/', 'instagram.com/hacked') + '. In the EU, the notice may mention out-of-court dispute bodies under the Digital Services Act. Our <a href="/guides/instagram-account-disabled/">disabled Instagram account</a> guide covers the other options.</p>'),
  ('help', 'Prefer someone else to handle it?', '<p>Most people can appeal on their own with the steps above. If you would rather hand it over, Unbanz is a paid, independent service for <a href="/instagram-unban-service/">suspended Instagram accounts</a>. We never need your password.</p>'),
 ],
 sources=[('https://help.instagram.com/', 'Instagram Help Center'), ('https://help.instagram.com/477434105621119', 'Instagram Community Guidelines'), ('https://www.facebook.com/help/103873106370583', 'Facebook Help: suspended or disabled accounts'), ('https://transparency.meta.com/enforcement/taking-action/disabling-accounts/', 'Meta Transparency Center: Disabling accounts')],
)

FB = dict(
 quick='use the “Disagree” or appeal option on the notice, confirm your identity, and submit once before the deadline shown on it.',
 intro='Facebook gives most suspended accounts a window to disagree. You can do it yourself; here is how.',
 secs=[
  ('suspended-disabled', 'Suspended or disabled?', '<p>Facebook’s Help Center page ' + EXT('https://www.facebook.com/help/103873106370583', 'My personal Facebook account is suspended or disabled') + ' explains the two notices:</p>' + ul(
    '<strong>We suspended your account:</strong> you can appeal, usually within 180 days. Nobody can see or use the account meanwhile.',
    '<strong>We disabled your account:</strong> the permanent stage, after the window ends or an appeal fails. You can’t request another review.') + '<p>The window varies by region, so trust the date on your own screen. Meta may also disable an account without suspending it first for severe violations.</p>'),
  ('before', 'Before you start', ul(
    'Screenshot the notice, including the date and any policy named.',
    'Make sure you can receive codes on the email or phone linked to the account.',
    'Have a government ID ready and check the name matches the profile.',
    'Download your information if the notice offers it.')),
  ('steps', 'How to appeal, step by step', ol(
    '<strong>Check it really is a suspension.</strong> If your password or email changed without you, it is a hack: go to ' + EXT('https://www.facebook.com/hacked', 'facebook.com/hacked') + ' instead.',
    '<strong>Log in</strong> on your usual device and network and open the notice.',
    '<strong>Tap <em>Disagree with decision</em></strong> (or the appeal option shown).',
    '<strong>Confirm your identity.</strong> Enter the code, take the video selfie or upload ID if asked.',
    '<strong>Add a short note if there is a box:</strong> you own the account, how you use it, and why the reason does not fit. Mention a hack if there was one.',
    '<strong>Submit once</strong> and wait for the confirmation screen.',
    '<strong>Watch your email</strong>, including spam, and the app. Facebook does not publish a review time.')),
  ('why', 'Why Facebook suspends accounts', '<p>The help page lists content that breaks the Community Standards, misrepresenting your identity (including impersonation), and contacting people to harass or promote in ways that are not allowed. Some regions also apply age rules. Hacked accounts are sometimes suspended for activity the owner did not do, and automated systems make mistakes.</p>'),
  ('pages', 'Pages, groups and ads', '<p>A <a href="/facebook-unban-service/">disabled profile</a> can affect Pages and <a href="/ad-account-recovery/">ad accounts</a> where you are the only admin. A Page with no one left in full control is deactivated and scheduled for deletion, so add a trusted second admin now. See <a href="/guides/facebook-page-restricted/">restricted Facebook Page</a> and <a href="/guides/meta-ad-account-restricted/">Meta ad account restricted</a>.</p>'),
  ('mistakes', 'What to avoid', ul(
    '<strong>Letting the window run out.</strong> After it ends you can’t request another review.',
    '<strong>Making a second profile.</strong> Meta disables accounts created to get around restrictions.',
    '<strong>Appeal “email addresses” from forums.</strong> They are not an appeal route. Use the notice.',
    '<strong>Sharing your password or codes,</strong> or replying to “Meta support” messages on Messenger. Facebook does not run appeals that way.')),
  ('help', 'Prefer someone else to handle it?', '<p>Most people can appeal on their own with the steps above. If you would rather hand it over, Unbanz offers paid, independent <a href="/facebook-account-recovery/">Facebook account recovery</a>. We never need your password, and Meta makes the final decision.</p>'),
 ],
 sources=[('https://www.facebook.com/help/103873106370583', 'Facebook Help: suspended or disabled accounts'), ('https://transparency.meta.com/policies/community-standards/', 'Meta Community Standards'), ('https://transparency.meta.com/enforcement/taking-action/disabling-accounts/', 'Meta Transparency Center: Disabling accounts'), ('https://www.facebook.com/hacked', 'Facebook: hacked accounts')],
)

def build(slug, d):
    f = os.path.join(ROOT, 'guides', slug, 'index.html')
    h = open(f, encoding='utf-8').read()
    m = re.search(r'(<section class="service-hero"><div class="container"><a class="crumb"[^>]*>[^<]*</a><h1>.*?</h1>)(.*?)(</div></section>)', h, re.S)
    meta = re.search(r'<p class="guide-meta">.*?</p>', m.group(2), re.S).group(0)
    meta = re.sub(r'Updated <time datetime="[^"]*">[^<]*</time>', 'Updated <time datetime="2026-10-29">29 October 2026</time>', meta)
    hero = m.group(1) + '<p class="quick-answer"><strong>Short answer:</strong> %s</p><p>%s</p>' % (d['quick'], d['intro']) + meta + m.group(3)
    h = h.replace(m.group(0), hero)
    items = [(i, t) for i, t, _ in d['secs']] + [('faq', 'Frequently asked questions'), ('sources', 'Official sources')]
    src = '<div class="guide-sources" id="sources"><h2>Official sources</h2><ul>' + ''.join('<li>%s</li>' % EXT(u, t) for u, t in d['sources']) + '</ul><p>Meta updates its help pages and flows often. Always follow the wording on your own notice and the current official Help Center. Unbanz is an independent service and is not affiliated with Meta, Instagram or Facebook.</p></div>'
    art = toc(items) + ''.join(sec(*s) for s in d['secs']) + src
    h = re.sub(r'(<article class="guide-body container">).*?(</article>)', lambda x: x.group(1) + art + x.group(2), h, count=1, flags=re.S)
    h = re.sub(r'"dateModified":"[^"]*"', '"dateModified":"2026-10-29"', h)
    open(f, 'w', encoding='utf-8').write(h)

build('instagram-account-suspended-appeal', IG)
build('facebook-account-disabled-appeal', FB)
print('ok')
