# -*- coding: utf-8 -*-
"""Shared top-of-page block for the extra (country, reference, partner) pages, built from the same markup and
classes as the original service pages (instagram-account-recovery, instagram-username-claim):
service-hero + answer-first + service-editorial (3 cards). Used by build_oct25_pages.build() and by oct28d_patch_top.py."""
import html, re

def esc(s): return html.escape(s, quote=True)

def place_of(h1):
    m = re.search(r' in (.+?)\.$', h1)
    return m.group(1) if m else ''

IG_CARDS = lambda pl: [
 ('Disabled or suspended', 'Open the notice on the login screen and request a review. Go through every step, send one complete appeal, and tell us the date the notice appeared.'),
 ('Hacked or locked out', 'If the email, number or password was changed, start at instagram.com/hacked on a device you have used before. Tell us what changed and when.'),
 ('Checks for ' + pl, 'Phone formats, where to report fraud and any appeal rights differ by country. The sections below cover %s.' % pl)]
FB_CARDS = lambda pl: [
 ('Disabled or suspended', 'Open the notice and choose to disagree with the decision within the time it shows. Send one complete appeal and keep a copy of the notice.'),
 ('Hacked or locked out', 'If someone took over the account, start at facebook.com/hacked on a device you have used before. Tell us what changed and when.'),
 ('Checks for ' + pl, 'Phone formats, where to report fraud and any appeal rights differ by country. The sections below cover %s.' % pl)]
CLAIM_CARDS = lambda pl: [
 ('Registered trade mark', 'A registered mark that matches the handle is the strongest route. It goes through Meta’s intellectual property report.'),
 ('Impersonation', 'If an account is posing as you or your business, Instagram’s impersonation report applies.'),
 ('A handle that was yours', 'If you lost the handle in a hack or by mistake, recovery usually comes first. There is no public form for inactive handles.')]
HUB_CARDS = [
 ('The same official routes', 'Every country starts with a review on the notice, or the hacked-account tools after a takeover.'),
 ('Local details differ', 'Phone formats, fraud reporting routes and appeal rights change from country to country.'),
 ('Meta decides', 'Unbanz helps you appeal through Meta’s official process. Meta makes the final decision on every appeal.')]
CARDS = {
 'account-recovery-by-country': HUB_CARDS,
 'instagram-account-disabled-vs-suspended-vs-restricted': [
   ('Disabled or suspended', 'A notice at login and the account is offline. Open the notice and request a review.'),
   ('Restricted', 'The account still logs in, but some features are limited. Check Account Status first.'),
   ('Hacked or deleted', 'A hacked account usually shows no notice, just a password that stops working. A deleted account cannot be restored.')],
 'ways-to-get-a-banned-instagram-account-back': [
   ('Free routes first', 'The in-app review, or instagram.com/hacked if the account was hacked.'),
   ('Meta Verified', 'If you subscribe to Meta Verified, contact its support.'),
   ('An independent service', 'If those are closed or failed, Unbanz can prepare and handle the appeal. Meta makes the final decision.')],
 'instagram-username-claim-routes': [
   ('Trademark report', 'For a registered trademark that matches the handle.'),
   ('Impersonation report', 'For an account posing as you or your business.'),
   ('Squatted or freed handles', 'Abandoned handles and handles that get freed up. Some handles have no honest route at all.')],
 'meta-ad-account-restricted-vs-disabled': [
   ('Restricted', 'Limits on what you can do, such as spend or features. The ad account may still run.'),
   ('Disabled', 'The ad account cannot run ads until the decision changes.'),
   ('Find the asset', 'A restriction can sit on the business portfolio, the ad account, a Page or a personal profile. Open Account Quality.')],
 'instagram-appeal-checklist': [
   ('Before you submit', 'Screenshot the notice, read the deadline and secure your email.'),
   ('Finish the checks', 'Complete any identity check, then submit once with a short factual note.'),
   ('What not to do', 'Do not delete posts, share your password or file the same request repeatedly.')],
 'instagram-recovery-glossary': [
   ('Notice terms', 'Disabled, suspended, restricted, strike and appeal.'),
   ('Access and identity', 'Hacked and video selfie.'),
   ('Usernames and ads', 'Username claim, trademark report, Account Quality and ad account restriction.')],
}
H1 = {
 'account-recovery-by-country': 'Account recovery by country.',
 'instagram-account-disabled-vs-suspended-vs-restricted': 'Disabled vs suspended vs restricted.',
 'ways-to-get-a-banned-instagram-account-back': 'Ways to get a banned account back.',
 'meta-ad-account-restricted-vs-disabled': 'Restricted or disabled ad account.',
 'instagram-appeal-checklist': 'Instagram appeal checklist.',
 'instagram-recovery-glossary': 'Instagram and Meta recovery glossary.',
 'instagram-username-claim-routes': 'Instagram username claim routes, compared.',
}

def cards_for(slug, h1):
    if slug in CARDS: return CARDS[slug]
    pl = place_of(h1)
    if slug.startswith('instagram-username-claim-'): return CLAIM_CARDS(pl)
    if slug.startswith('facebook-account-recovery-'): return FB_CARDS(pl)
    return IG_CARDS(pl)

def top_v2(*, h1, hero_html, wa, ws, mail, answer, cards, username=False, crumb_label='Services'):
    """hero_html is already-escaped inner HTML of the hero paragraph; h1/answer are plain text."""
    ds = ' data-service="%s"' % ws + (' data-platform="Instagram"' if ws == 'username' else '')
    href = '/services/' if ws == 'username' else '/'
    hero = ('<main id="content"><section class="service-hero"><div class="container">'
            '<a class="crumb" href="%s">Home / %s</a><h1>%s</h1><p>%s</p><div class="hero-cta">'
            '<a class="button button-light" href="%s"%s>Message us on WhatsApp <span aria-hidden="true">↗︎</span></a>'
            '<a class="hero-email" href="%s">Prefer email? ↗︎</a></div></div></section>') % (href, esc(crumb_label), esc(h1), hero_html, wa, ds, mail)
    first, _, rest = answer.partition('. ')
    if rest: ans = '<strong>%s.</strong> %s' % (esc(first), esc(rest))
    else: ans = '<strong>%s</strong>' % esc(answer)
    af = ('<section class="answer-first container" id="answer" style="padding-top:48px"><p style="max-width:860px;font-size:19px;line-height:1.5;margin:0">%s</p></section>' % ans)
    ed = '<section class="service-editorial container">%s</section>' % ''.join(
        '<article><h2>%s</h2><p>%s</p></article>' % (esc(t), esc(d)) for t, d in cards)
    return hero + af + ed
