"""One-time redesign of the 21 existing guide pages (idempotent: skips pages already marked guide-v2)."""
import re, glob, sys
sys.path.insert(0, '/workspace/site/scripts/guides')
from common import *

SHORT = {
 'ad-account-circumventing-systems': "fix whatever in your setup looks like it is hiding things from ad review (landing page, redirects, domains, creative), then request a review from Account Quality. Don’t open a new ad account to get around it.",
 'ad-account-unacceptable-business-practices': "it means Meta thinks your ads look deceptive or scam-like. Make your business and landing page easy to trust, fix what triggered it, then request a review once from Account Quality.",
 'facebook-account-disabled-appeal': "use the “Disagree” or appeal option on the notice, confirm your identity and submit once, before the deadline shown on it.",
 'facebook-account-locked': "a lock is a security step, not a ban. Follow the prompts to confirm it’s you (code, selfie or ID) and Facebook lets you back in.",
 'facebook-page-restricted': "check Page Status first. If an admin unpublished the Page you can republish it yourself; if Meta restricted it, appeal from Page Status.",
 'hacked-facebook-account-recovery': "go to facebook.com/hacked, follow the prompts to confirm it’s you, then change your password and review your security settings once you’re back in.",
 'instagram-account-disabled-for-no-reason': "there is usually a trigger you can’t see. Look for the reason in Account Status and your email, then appeal once from the notice with calm, factual wording.",
 'instagram-account-disabled': "screenshot the notice, request a review from it, complete any identity check and submit once. Don’t create a new account while you wait.",
 'instagram-account-integrity': "“account integrity” is about authentic identity and behaviour, not one post. Appeal from the notice, keep it factual and don’t resubmit repeatedly.",
 'instagram-account-locked': "a lock is protective, not a ban. Follow Instagram’s prompts to confirm it’s you and the account is usually yours to unlock.",
 'instagram-community-guidelines-strikes': "a strike is added when Meta removes content for breaking its rules, and strikes add up to restrictions. Check your strikes in Account Status and disagree with any removal that is a mistake.",
 'instagram-disabled-for-impersonation': "appeal from the notice, show clearly that the account is really yours, and have proof of your identity ready.",
 'instagram-disabled-no-appeal-button': "the button usually disappears for a specific reason. Try the official routes in this guide before assuming the decision is final.",
 'instagram-video-selfie-verification': "record in good light with your whole face visible, follow the on-screen prompts exactly and submit once. If it fails you can try again.",
 'meta-ad-account-disabled-payment': "fix the payment method or the security problem, then request a review from Account Quality.",
 'meta-ad-account-restricted': "open Account Quality, find which asset is restricted, fix the cause, then request a review once.",
 'meta-business-portfolio-restricted': "find exactly what is restricted, request the review at the top level (the portfolio) first, then work down to ad accounts and Pages.",
 'snapchat-account-locked': "read the in-app message to see which lock you have. Temporary locks end on their own and you unlock in the Snapchat Accounts Portal; permanent locks allow one in-app appeal.",
 'why-instagram-bans-accounts': "most bans come from the Community Guidelines and automated spam signals. Keep your login private, stay off third-party apps and check Account Status regularly.",
}

# category defaults: platform, mid(kicker,title,text), close(kicker,title,text), wa, subject
CATS = {
 'hacked': dict(pl='{P}', wa='Hey Unbanz, my {P} account was hacked and I need help getting it back', sub='Hacked {P} account',
   mid=('Locked out of it?', 'Hacked and not getting anywhere?', 'Send us your username and what you can see on screen. We’ll tell you the next step. Your password stays with you.'),
   close=('Still stuck?', 'Want us to handle the recovery?', 'Message us the username, when it happened and any security emails you got. We never ask for your password or login codes.')),
 'ig_disabled': dict(wa='Hey Unbanz, my Instagram account was disabled and I want to appeal', sub='Disabled Instagram account',
   mid=('Account disabled?', 'Want us to handle the appeal?', 'Send us your username and a screenshot of the notice. We’ll tell you where it stands. No password needed.'),
   close=('Rather not do it alone?', 'Let’s get the appeal sorted', 'Message us your username and the notice you’re seeing. We work through Meta’s official appeal process and never ask for your password.')),
 'ig_locked': dict(wa='Hey Unbanz, my Instagram account is locked and I need help unlocking it', sub='Locked Instagram account',
   mid=('Verification going in circles?', 'Want a hand getting back in?', 'Tell us what the screen says and we’ll point you to the right step. Your password stays with you.'),
   close=('Still locked out?', 'Message us what you’re seeing', 'Send your username and a screenshot of the prompt. We’ll go through the official options with you.')),
 'fb_disabled': dict(wa='Hey Unbanz, my Facebook account was disabled and I want to appeal', sub='Disabled Facebook account',
   mid=('Account disabled?', 'Want us to handle the appeal?', 'Send us the notice and the dates on it. We’ll tell you what the appeal window looks like. No password needed.'),
   close=('Rather not do it alone?', 'Let’s get the appeal sorted', 'Message us the profile link and a screenshot of the notice. We use Meta’s official appeal process and never ask for your password.')),
 'fb_locked': dict(wa='Hey Unbanz, my Facebook account is locked and I need help confirming my identity', sub='Locked Facebook account',
   mid=('Stuck on “confirm your identity”?', 'Want a hand getting back in?', 'Tell us which prompt you’re on and what you’ve tried. We’ll point you to the next step.'),
   close=('Still locked out?', 'Message us what you’re seeing', 'Send the profile link and a screenshot of the lock screen. We’ll go through the official options with you.')),
 'fb_page': dict(wa='Hey Unbanz, my Facebook Page is restricted or unpublished and I need help', sub='Restricted Facebook Page',
   mid=('Page offline?', 'Want us to look at your Page?', 'Send the Page link and a screenshot of Page Status. We’ll tell you whether it was unpublished or restricted and what to do next.'),
   close=('Customers can’t find you?', 'Let’s get the Page back up', 'Message us the Page link, a screenshot of the notice and when it started. We never ask for passwords or login codes.')),
 'ad': dict(wa='Hey Unbanz, my Meta ad account is restricted and I need help', sub='Meta ad account help',
   mid=('Ads stopped?', 'Want us to handle the ad account?', 'Send us the ad account ID and a screenshot of Account Quality. We’ll tell you where it stands. Your login stays with you.'),
   close=('Campaigns on hold?', 'Let’s get your ads moving again', 'Message us the ad account ID, the notice and what changed before it stopped. We use Meta’s official review process and never ask for passwords.')),
 'snap': dict(wa='Hey Unbanz, my Snapchat account is locked and I need help', sub='Locked Snapchat account',
   mid=('Appeal button missing?', 'Want us to take a look?', 'Send your username and what the lock message says. We’ll tell you which route fits. No password needed.'),
   close=('Only one appeal per lock', 'Let’s make it count', 'Message us your username and the lock message before you appeal. We never ask for your password.')),
}
CATMAP = {
 'hacked-instagram-account-recovery': ('hacked', 'Instagram'),
 'hacked-facebook-account-recovery': ('hacked', 'Facebook'),
 'instagram-account-disabled': ('ig_disabled', 'Instagram'),
 'instagram-account-disabled-for-no-reason': ('ig_disabled', 'Instagram'),
 'instagram-disabled-no-appeal-button': ('ig_disabled', 'Instagram'),
 'instagram-disabled-for-impersonation': ('ig_disabled', 'Instagram'),
 'instagram-account-integrity': ('ig_disabled', 'Instagram'),
 'instagram-account-suspended-appeal': ('ig_disabled', 'Instagram'),
 'instagram-community-guidelines-strikes': ('ig_disabled', 'Instagram'),
 'why-instagram-bans-accounts': ('ig_disabled', 'Instagram'),
 'instagram-account-locked': ('ig_locked', 'Instagram'),
 'instagram-video-selfie-verification': ('ig_locked', 'Instagram'),
 'facebook-account-disabled-appeal': ('fb_disabled', 'Facebook'),
 'facebook-account-locked': ('fb_locked', 'Facebook'),
 'facebook-page-restricted': ('fb_page', 'Facebook'),
 'ad-account-circumventing-systems': ('ad', None),
 'ad-account-unacceptable-business-practices': ('ad', None),
 'meta-ad-account-disabled-payment': ('ad', None),
 'meta-ad-account-restricted': ('ad', None),
 'meta-business-portfolio-restricted': ('ad', None),
 'snapchat-account-locked': ('snap', 'Snapchat'),
}
OVERRIDE = {
 'instagram-video-selfie-verification': dict(wa='Hey Unbanz, Instagram keeps failing my video selfie and I need help', sub='Instagram video selfie help',
   mid=('Selfie keeps failing?', 'Want a hand with verification?', 'Tell us what the screen says and when it failed. We’ll point you to the next step. Your password stays with you.'),
   close=('Stuck on verification?', 'Message us what you’re seeing', 'Send your username and a screenshot of the prompt. We’ll go through the official options with you.')),
 'instagram-disabled-for-impersonation': dict(wa='Hey Unbanz, my Instagram account was disabled for impersonation and it is really mine', sub='Instagram disabled for impersonation'),
 'instagram-community-guidelines-strikes': dict(wa='Hey Unbanz, my Instagram account has strikes and I need help', sub='Instagram strikes help',
   mid=('Strikes piling up?', 'Want someone to look at it with you?', 'Send us your username and a screenshot of Account Status. We’ll tell you what it means.'),
   close=('Worried about a ban?', 'Message us your Account Status', 'Send your username and what Instagram shows. No password needed.')),
 'why-instagram-bans-accounts': dict(wa='Hey Unbanz, my Instagram account was banned and I want to know my options', sub='Banned Instagram account',
   mid=('Already banned?', 'Want us to take a look?', 'Send us your username and the notice. We’ll tell you where it stands. No password needed.'),
   close=('Not sure why it happened?', 'Message us the notice', 'Send your username and a screenshot of what Instagram shows. We’ll talk through the official options.')),
 'instagram-account-suspended-appeal': dict(wa='Hey Unbanz, my Instagram account was suspended and I want to appeal', sub='Suspended Instagram account'),
 'meta-ad-account-disabled-payment': dict(wa='Hey Unbanz, my Meta ad account was disabled over payment or unusual activity', sub='Disabled Meta ad account'),
 'meta-business-portfolio-restricted': dict(wa='Hey Unbanz, my Meta Business Portfolio is restricted and I need help', sub='Restricted Business Portfolio'),
 'ad-account-circumventing-systems': dict(wa='Hey Unbanz, my Meta ad account was flagged for circumventing systems', sub='Meta ad account flagged'),
 'ad-account-unacceptable-business-practices': dict(wa='Hey Unbanz, my Meta ad account was restricted for unacceptable business practices', sub='Meta ad account restricted'),
}
# extra "Related guides" pills for pages that have fewer than 3 guide links
EXTRA_REL = {
 'snapchat-account-locked': [('/guides/instagram-account-locked/','Instagram account locked'),('/guides/facebook-account-locked/','Facebook account locked'),('/snapchat-unban-service/','Snapchat unban service')],
 'facebook-page-restricted': [('/guides/meta-ad-account-restricted/','Meta ad account restricted'),('/guides/facebook-account-locked/','Facebook account locked')],
 'hacked-facebook-account-recovery': [('/guides/facebook-account-locked/','Facebook account locked')],
 'instagram-disabled-for-impersonation': [('/guides/instagram-account-disabled/','Instagram account disabled')],
 'meta-business-portfolio-restricted': [('/guides/meta-ad-account-restricted/','Meta ad account restricted')],
}

def cfg(slug):
    cat, plat = CATMAP[slug]
    c = dict(CATS[cat])
    c.update(OVERRIDE.get(slug, {}))
    P = plat or 'Meta'
    f = lambda s: s.replace('{P}', P)
    return dict(wa=f(c['wa']), sub=f(c['sub']), mid=c['mid'], close=c['close'], plat=plat)

def run():
    n = 0
    for fpath in sorted(glob.glob(ROOT + '/guides/*/index.html')):
        slug = fpath.split('/')[-2]
        h = open(fpath, encoding='utf-8').read()
        if 'guide-v2' in h:
            continue
        c = cfg(slug)
        # service value from the existing top CTA
        top = re.search(r'<p class="guide-cta-top"[^>]*>.*?</p>', h, re.S)
        sv = re.search(r'data-service="([\w-]+)"', top.group(0)).group(1) if top and 'data-service' in top.group(0) else None
        assert top, slug
        body_class_old = '<body class="service-page guide-page">'
        assert body_class_old in h, slug
        h = h.replace(body_class_old, body_class_old)  # unchanged; guide-page already present
        # hero: quick answer + top cta
        hero_m = re.search(r'(<section class="service-hero"><div class="container"><a class="crumb"[^>]*>[^<]*</a><h1>.*?</h1>)(.*?)(</div></section>)', h, re.S)
        pre, hero_rest, post = hero_m.groups()
        hero_rest = hero_rest.replace(top.group(0), '')
        if 'quick-answer' not in hero_rest:
            hero_rest = f'<p class="quick-answer"><strong>Short answer:</strong> {SHORT[slug]}</p>' + hero_rest
        newhero = pre + hero_rest + top_cta(c['wa'], c['sub'], sv, c['plat']) + post
        h = h.replace(hero_m.group(0), newhero)
        # article
        art_m = re.search(r'<article class="guide-body container">(.*?)</article>', h, re.S)
        art = art_m.group(1)
        toc_m = re.search(r'<nav class="guide-toc"[^>]*><p>In this (?:guide|article)</p>(<ol>.*?</ol>)</nav>', art, re.S)
        assert toc_m, slug
        rest = art[toc_m.end():]
        src_i = rest.index('<div class="guide-sources"')
        body, sources = rest[:src_i], rest[src_i:]
        secs = convert_body(body)
        mid = cta_card('mid', c['mid'][0], c['mid'][1], c['mid'][2], c['wa'], c['sub'], sv, c['plat'])
        close = cta_card('close', c['close'][0], c['close'][1], c['close'][2], c['wa'], c['sub'], sv, c['plat'])
        pos = 3 if len(secs) >= 6 else 2
        secs.insert(pos, mid)
        main_html = ''.join(secs) + close + sources
        new_art = '<article class="guide-body guide-v2 container">' + toc_html(toc_m.group(1)) + '<div class="guide-main">' + main_html + '</div></article>'
        h = h.replace(art_m.group(0), new_art)
        # related pills
        rel_m = re.search(r'<nav class="related-services container" aria-label="Related pages">(.*?)</nav>', h, re.S)
        links = rel_m.group(1)
        for href, label in EXTRA_REL.get(slug, []):
            if f'href="{href}"' not in links:
                links = links.replace('<a href="/guides/">All guides</a>', f'<a href="{href}">{label}</a><a href="/guides/">All guides</a>') if '<a href="/guides/">All guides</a>' in links else links + f'<a href="{href}">{label}</a>'
        h = h.replace(rel_m.group(0), '<nav class="related-services container" aria-label="Related pages"><p class="rel-label">Related guides</p>' + links + '</nav>')
        open(fpath, 'w', encoding='utf-8').write(h)
        n += 1
        print('ok', slug, len(secs))
    print('changed', n)

if __name__ == '__main__':
    run()
