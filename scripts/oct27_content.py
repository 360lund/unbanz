# -*- coding: utf-8 -*-
"""Country pages added 2026-10-27 (rendered by build_oct27_pages.py via build_oct25_pages.build)."""
DATE = "2026-10-27"

def A(href, label):
    return '<a href="%s">%s</a>' % (href, label)
def sec(id_, h2, body):
    return '<h2 id="%s">%s</h2>%s' % (id_, h2, body)
def ul(items): return '<ul>%s</ul>' % ''.join('<li>%s</li>' % i for i in items)
def ol(items): return '<ol>%s</ol>' % ''.join('<li>%s</li>' % i for i in items)

def how(plat):
    return ('<h2 id="how">How it works with Unbanz</h2><ol>'
            '<li>Message us on WhatsApp or email with the %s name or profile link, the email or phone on the account, and a screenshot of the notice.</li>'
            '<li>We tell you honestly whether we can help and what it would cost.</li>'
            '<li>We prepare everything and handle the appeal through the platform’s official process.</li>'
            '<li>We keep you posted until there’s a result. Meta makes the final decision.</li></ol>') % plat

def who(items):
    return '<h2 id="who">Who this is for</h2><ul>%s</ul>' % ''.join('<li>%s</li>' % i for i in items)

PASSWORD_IG = ('Do I need to share my Instagram password?', 'No. Your password and login codes stay with you. Anyone who asks for them is not someone to work with.')
PASSWORD_FB = ('Do I need to share my Facebook password?', 'No. Your password and login codes stay with you. Anyone who asks for them is not someone to work with.')
CONTACT_FAQ = ('How do I contact Unbanz?', 'WhatsApp +1 934 201 2490 or team@unbanz.com.')
CAN_FAQ = ('Can Unbanz recover my account?', 'We help you submit a clean appeal through Meta’s official process and handle it end to end. Meta makes the final decision, so we tell you upfront whether we think it’s doable.')
IG_WA = 'Hey%20Unbanz%2C%20I%20need%20help%20recovering%20my%20Instagram%20account'
FB_WA = 'Hey%20Unbanz%2C%20I%20need%20help%20recovering%20my%20Facebook%20account'

IG_REL = [('/instagram-account-recovery/','Instagram account recovery'),('/instagram-account-disabled-appeal/','Instagram disabled appeal'),('/instagram-hacked-account-recovery-service/','Hacked Instagram recovery'),('/hacker-changed-my-instagram-email-and-password/','Hacker changed email and password'),('/instagram-appeal-denied/','Appeal denied'),('/guides/instagram-appeal-sent-no-response/','Appeal sent, no response'),('/unban-pricing/','Unban cost and timing'),('/services/','All services')]
FB_REL = [('/facebook-account-recovery/','Facebook account recovery'),('/facebook-account-disabled-appeal-help/','Facebook disabled appeal help'),('/facebook-account-suspended-180-days/','Suspended, 180 days to appeal'),('/facebook-hacked-account-recovery-service/','Hacked Facebook recovery'),('/guides/hacker-changed-facebook-email-and-password/','Hacker changed email and password'),('/guides/facebook-disabled-appeal-rejected/','Facebook appeal rejected'),('/unban-pricing/','Unban cost and timing'),('/services/','All services')]

PAGES = []

def ig_hf(place):
    return ('How do I recover a hacked Instagram account in %s?' % place,
            'Use the undo link in Instagram’s email about the change if there is one, then go to instagram.com/hacked on a device you used before and follow the steps. Instagram may ask for a code or a video selfie. If you see a disabled notice, request a review once.')
def fb_hf(place):
    return ('How do I recover a hacked Facebook account in %s?' % place,
            'Go to facebook.com/hacked on a device and browser you have used before, or search for your account at facebook.com/login/identify and choose the option for no longer having access. Check the email on the account first for a message from Facebook with a link to undo a change.')

def country(slug, cc, plat, title, desc, h1, crumb, hero, answer, first, local_h, local, extra, who_items, faq, related, relq):
    fb = plat == 'Facebook'
    PAGES.append(dict(
     slug=slug, lang='en-US' if cc == 'us' else 'en', title=title, desc=desc, h1=h1, crumb=crumb, svc=crumb,
     hero=hero, wa=FB_WA if fb else IG_WA, ws='unban', subj='%s%%20account%%20recovery' % plat, answer=answer,
     body=[
      sec('first', 'Official steps that come first', ol(first)),
      sec('local', local_h, ul(local)) + extra,
      sec('avoid', 'What not to do', ul([
        'Don’t pay or message anyone from a DM who says they can “open” your account.',
        'Don’t share your password or login codes with anyone, including us.',
        'Don’t create new accounts to plead with %s, and don’t send the same appeal over and over.' % plat])),
      sec('help', 'How Unbanz helps', '<p>We work out whether the account is disabled, hacked or both, gather the notice, the old email and phone and the dates, and handle the appeal through Meta’s official process. Main page: ' +
          (A('/facebook-account-recovery/', 'Facebook account recovery') if fb else A('/instagram-account-recovery/', 'Instagram account recovery')) + '.</p>'),
      how(plat),
      who(who_items),
     ],
     faq=faq + [PASSWORD_FB if fb else PASSWORD_IG, CONTACT_FAQ], related=related, relq=relq))

# The five low-income-country pages first built here were removed again on 2026-10-27 (301 to the main recovery pages); see oct27b_content.py for the replacements.
