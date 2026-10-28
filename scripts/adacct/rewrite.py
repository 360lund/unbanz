# -*- coding: utf-8 -*-
import html, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from lib import ROOT, DATE
import hub
from existing import EXISTING
esc = lambda t: html.escape(t, quote=True)
NEW = {p['slug']: p for p in hub.all_pages()}
HUB = 'meta-ad-account-help'
M = {
 'facebook-ad-account-disabled': 'ad-account-disabled-circumventing-systems-help ad-account-disabled-unacceptable-business-practices-help ad-account-disabled-by-mistake ad-account-disabled-after-adding-new-card disabled-ad-account-unpaid-balance meta-ad-account-appeal-what-to-write ad-account-reinstated-then-disabled-again ad-account-restricted-payment-issue',
 'facebook-ad-account-disabled-uk': 'ad-account-disabled-circumventing-systems-help ad-account-restricted-payment-issue ad-account-identity-verification-loop meta-ad-account-appeal-what-to-write disabled-ad-account-unpaid-balance ad-account-disabled-by-mistake meta-ad-account-disabled-ireland',
 'facebook-ad-account-disabled-australia': 'ad-account-disabled-circumventing-systems-help ad-account-restricted-payment-issue meta-ad-account-appeal-what-to-write meta-ad-account-disabled-new-zealand meta-ad-account-disabled-singapore disabled-ad-account-unpaid-balance ad-account-disabled-by-mistake',
 'facebook-ad-account-disabled-canada': 'ad-account-disabled-circumventing-systems-help ad-account-restricted-payment-issue meta-ad-account-appeal-what-to-write ad-account-disabled-by-mistake disabled-ad-account-unpaid-balance ad-account-identity-verification-loop',
 'facebook-ad-account-restricted-help': 'ad-account-restricted-payment-issue ad-account-identity-verification-loop ad-account-ads-rejected-repeatedly-restricted ad-account-restricted-misleading-claims ad-account-restricted-landing-page-issue ad-account-spending-limit-stuck ad-account-restricted-special-ad-category ad-account-restricted-personal-attributes',
 'facebook-ad-account-restricted-us-business': 'meta-business-portfolio-restricted-help meta-business-suite-restricted-help facebook-page-restricted-cannot-advertise meta-pixel-restricted-or-disabled-help ad-account-restricted-ads-for-ecommerce-stores ad-account-restricted-ads-for-local-service-businesses ad-account-restricted-ads-for-coaches-and-course-creators ad-account-restricted-ads-for-real-estate-agents',
 'meta-ad-account-restricted': 'ad-account-ads-rejected-repeatedly-restricted ad-account-restricted-misleading-claims ad-account-restricted-landing-page-issue ad-account-restricted-personal-attributes ad-account-restricted-special-ad-category ad-account-restricted-payment-issue ad-account-identity-verification-loop ad-account-spending-limit-stuck',
 'business-manager-disabled': 'meta-business-portfolio-restricted-help business-manager-restricted-cant-add-ad-account ad-account-lost-admin-after-employee-left ad-account-disabled-after-adding-admin facebook-profile-restricted-ad-account-affected meta-business-suite-restricted-help client-ad-account-disabled-agency-help',
 'ad-account-policy-violation-appeal': 'meta-ad-account-appeal-what-to-write ad-account-ads-rejected-repeatedly-restricted ad-account-restricted-misleading-claims ad-account-restricted-personal-attributes ad-account-restricted-special-ad-category ad-account-restricted-landing-page-issue ad-account-disabled-unacceptable-business-practices-help ad-account-reinstated-then-disabled-again',
 'ad-account-unusual-activity': 'ad-account-disabled-after-login-from-new-country ad-account-disabled-after-adding-admin ad-account-disabled-after-adding-new-card ad-account-disabled-after-domain-change ad-account-disabled-after-hack ad-account-disabled-by-mistake ad-account-disabled-circumventing-systems-help facebook-profile-restricted-ad-account-affected',
 'ad-account-request-review-not-showing': 'ad-account-identity-verification-loop disabled-ad-account-unpaid-balance facebook-profile-restricted-ad-account-affected meta-business-portfolio-restricted-help meta-ad-account-appeal-what-to-write ad-account-lost-admin-after-employee-left ad-account-restricted-payment-issue',
 'ad-account-disabled-after-hack': 'ad-account-disabled-after-login-from-new-country ad-account-disabled-after-adding-admin ad-account-lost-admin-after-employee-left facebook-profile-restricted-ad-account-affected ad-account-disabled-by-mistake meta-ad-account-appeal-what-to-write ad-account-unusual-activity',
 'meta-ad-account-appeal-rejected-what-next': 'meta-ad-account-appeal-what-to-write ad-account-reinstated-then-disabled-again ad-account-disabled-by-mistake ad-account-disabled-unacceptable-business-practices-help ad-account-disabled-circumventing-systems-help ad-account-restricted-misleading-claims ad-account-restricted-landing-page-issue',
 'why-was-my-facebook-ad-account-disabled-without-warning': 'ad-account-disabled-by-mistake ad-account-disabled-circumventing-systems-help ad-account-restricted-payment-issue ad-account-disabled-unacceptable-business-practices-help ad-account-disabled-after-login-from-new-country ad-account-disabled-after-domain-change ad-account-disabled-after-adding-new-card ad-account-disabled-after-advantage-plus-campaign',
 'how-long-does-meta-ad-account-review-take': 'ad-account-identity-verification-loop disabled-ad-account-unpaid-balance meta-ad-account-appeal-what-to-write ad-account-lost-admin-after-employee-left meta-business-portfolio-restricted-help facebook-profile-restricted-ad-account-affected',
 'how-much-does-ad-account-recovery-cost': 'client-ad-account-disabled-agency-help ad-account-restricted-ads-for-ecommerce-stores ad-account-restricted-ads-for-freelance-media-buyers ad-account-restricted-ads-for-saas-and-b2b-companies ad-account-restricted-ads-for-local-service-businesses ad-account-restricted-ads-for-coaches-and-course-creators meta-ad-account-appeal-what-to-write',
 'can-i-make-a-new-ad-account-after-ban': 'ad-account-disabled-circumventing-systems-help ad-account-disabled-unacceptable-business-practices-help ad-account-reinstated-then-disabled-again ad-account-disabled-by-mistake ad-account-lost-admin-after-employee-left client-ad-account-disabled-agency-help ad-account-disabled-after-domain-change',
 'meta-ad-account-restricted-vs-disabled': 'ad-account-restricted-payment-issue ad-account-spending-limit-stuck ad-account-ads-rejected-repeatedly-restricted ad-account-disabled-circumventing-systems-help ad-account-reinstated-then-disabled-again ad-account-restricted-special-ad-category meta-business-portfolio-restricted-help',
 'meta-business-verification-rejected': 'meta-business-portfolio-restricted-help ad-account-disabled-after-domain-change ad-account-identity-verification-loop meta-business-suite-restricted-help business-manager-restricted-cant-add-ad-account ad-account-lost-admin-after-employee-left meta-pixel-restricted-or-disabled-help',
 'who-can-recover-a-disabled-facebook-ad-account': 'meta-ad-account-appeal-what-to-write client-ad-account-disabled-agency-help ad-account-restricted-ads-for-freelance-media-buyers ad-account-disabled-by-mistake ad-account-disabled-unacceptable-business-practices-help ad-account-lost-admin-after-employee-left',
 'agency-ad-account-recovery': 'client-ad-account-disabled-agency-help ad-account-restricted-ads-for-freelance-media-buyers ad-account-lost-admin-after-employee-left business-manager-restricted-cant-add-ad-account meta-business-portfolio-restricted-help ad-account-restricted-ads-for-ecommerce-stores ad-account-restricted-ads-for-dropshipping-stores',
 'ad-account-recovery': 'ad-account-restricted-payment-issue ad-account-identity-verification-loop ad-account-disabled-circumventing-systems-help ad-account-disabled-by-mistake meta-ad-account-appeal-what-to-write meta-business-portfolio-restricted-help client-ad-account-disabled-agency-help ad-account-ads-rejected-repeatedly-restricted',
 'guides/meta-ad-account-restricted': 'ad-account-restricted-payment-issue ad-account-identity-verification-loop ad-account-ads-rejected-repeatedly-restricted ad-account-restricted-special-ad-category ad-account-restricted-misleading-claims ad-account-restricted-landing-page-issue ad-account-restricted-personal-attributes ad-account-spending-limit-stuck',
 'instagram-ads-account-restricted': 'facebook-page-restricted-cannot-advertise ad-account-disabled-after-boosting-post facebook-profile-restricted-ad-account-affected meta-business-suite-restricted-help ad-account-restricted-misleading-claims ad-account-restricted-personal-attributes',
 'best-facebook-ad-account-recovery-service': 'meta-ad-account-appeal-what-to-write client-ad-account-disabled-agency-help ad-account-disabled-circumventing-systems-help ad-account-restricted-payment-issue ad-account-restricted-ads-for-ecommerce-stores ad-account-restricted-ads-for-freelance-media-buyers',
}
def A(slug, text=None): return '<a href="/%s/">%s</a>' % (slug, text or NEW[slug]['h1'].rstrip('?').strip())
POOL = [
 ('Should I open a new ad account while I wait?', 'new ad account', lambda: 'Usually not. A new account opened after a restriction can look like an attempt to get around Meta’s systems and can put the new account at risk too. Read %s before you decide.' % A('ad-account-disabled-circumventing-systems-help', 'ad account disabled for circumventing systems') if False else 'Usually not. A new account opened after a restriction can look like an attempt to get around Meta’s systems and can put the new account at risk too. Read <a href="/can-i-make-a-new-ad-account-after-ban/">can I make a new ad account after a ban</a> before you decide.'),
 ('What should I avoid while a review is open?', 'while', lambda: 'Do not send repeated requests, add new cards or admins to the account, or run ads from another account tied to the same business. Pay any unpaid balance, answer any request for documents, and keep screenshots of every notice.'),
 ('Which details should I send first?', 'details', lambda: 'The ad account ID, the Business Portfolio ID, a screenshot of the notice from Account Quality and a short timeline of what changed before it happened. Never a password or a login code.'),
 ('What if Meta turns the review down?', 'turns the review|rejected|denied|rejection', lambda: 'Read the reason in Account Quality and do not resend the same request unchanged. Some notices still have a next step. See <a href="/meta-ad-account-appeal-rejected-what-next/">what to do after a rejected appeal</a>. Meta makes the final decision.'),
 ('What does Account Quality show?', 'account quality', lambda: 'It lists the assets Meta has limited, the reason given and whether a review can still be requested. Take a screenshot before you change anything on the account.'),
 ('Can an agency or freelancer handle this for a client?', 'agency|freelanc|client', lambda: 'Yes. The client stays the account owner. Send the ad account ID, the portfolio ID and the notice. See <a href="/client-ad-account-disabled-agency-help/">a client ad account was disabled</a> for how that works.'),
 ('Is Unbanz affiliated with Meta?', 'affiliated|partner', lambda: 'No. Unbanz is an independent service. Meta makes the final decision on every ad account, and nobody outside Meta can promise the outcome.'),
]
def title_of(slug, s=None):
    if slug in NEW: return NEW[slug]['h1'].rstrip('?').strip()
    s = open(os.path.join(ROOT, slug, 'index.html'), encoding='utf-8').read()
    return re.sub(r'<[^>]+>', ' ', re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S).group(1)).replace('  ', ' ').strip().rstrip('?.')
def links_block(slug):
    sl = M[slug].split()
    li = ''
    for x in sl:
        if x in NEW and x != HUB:
            li += '<li><a href="/%s/">%s</a>: %s</li>' % (x, esc(NEW[x]['h1']), esc(NEW[x]['desc']))
        else:
            li += '<li><a href="/%s/">%s</a></li>' % (x, esc(title_of(x)))
    li += '<li><a href="/%s/">All Meta ad account help, by notice, business type and country</a></li>' % HUB
    return '<h2 id="next-steps">Find your exact situation</h2><p>Ad account notices look alike but the cause is often different. These pages go through the common ones, with what to check and what to send.</p><ul>%s</ul>' % li
def fix_ld(s, fn):
    def rep(m):
        try: g = json.loads(m.group(1))
        except Exception: return m.group(0)
        fn(g); return '<script type="application/ld+json">' + json.dumps(g, ensure_ascii=False, separators=(',', ':')) + '</script>'
    return re.sub(r'<script type="application/ld\+json">(.*?)</script>', rep, s, flags=re.S)
def nodes(g): return g['@graph'] if isinstance(g, dict) and '@graph' in g else (g if isinstance(g, list) else [g])
def drop_faq(s, qname):
    s = re.sub(r'<details><summary>%s<span aria-hidden="true">\+</span></summary>.*?</details>' % re.escape(qname), '', s, flags=re.S)
    def f(g):
        for x in nodes(g):
            if x.get('@type') == 'FAQPage': x['mainEntity'] = [q for q in x['mainEntity'] if q['name'] != qname]
    return fix_ld(s, f)
def add_faq(s, pairs):
    det = ''.join('<details><summary>%s<span aria-hidden="true">+</span></summary><p>%s</p></details>' % (esc(q), a) for q, a in pairs)
    s = s.replace('</div></div></section><section class="service-proof', det + '</div></div></section><section class="service-proof', 1) if det not in s else s
    def f(g):
        for x in nodes(g):
            if x.get('@type') == 'FAQPage':
                have = {q['name'] for q in x['mainEntity']}
                for q, a in pairs:
                    if q not in have: x['mainEntity'].append({'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': re.sub(r'<[^>]+>', '', a)}})
    return fix_ld(s, f)
def common(s):
    def f(g):
        for x in nodes(g):
            if x.get('@type') == 'Organization' and 'sameAs' in x: x['sameAs'] = [u for u in x['sameAs'] if 'trustpilot' not in u.lower()]
            if x.get('@type') == 'WebPage': x['dateModified'] = DATE
    s = fix_ld(s, f)
    s = re.sub(r'<time datetime="[^"]*">[^<]*</time>', '<time datetime="%s">29 October 2026</time>' % DATE, s)
    if 'class="guide-meta"' not in s:
        s = s.replace('<div class="hero-cta">', '<p class="guide-meta">Updated <time datetime="%s">29 October 2026</time></p><div class="hero-cta">' % DATE, 1)
    if 'article:modified_time' not in s:
        s = re.sub(r'(<link rel="canonical" href="[^"]*">)', r'\1<meta property="article:modified_time" content="%s">' % DATE, s, 1)
    return s
def process(slug, idx):
    f = os.path.join(ROOT, slug, 'index.html'); s = open(f, encoding='utf-8').read()
    done = 'id="next-steps"' in s
    s = common(s)
    s = drop_faq(s, 'What do clients say about Unbanz?')
    # rule fixes
    if slug == 'how-long-does-meta-ad-account-review-take':
        s = drop_faq(s, 'How long does Unbanz take?')
        s = s.replace(' Usual estimate is 3–14 days from the day work starts.', ' Meta sets the timing and nobody outside Meta can promise it.')
    if slug == 'who-can-recover-a-disabled-facebook-ad-account':
        s = s.replace('Is Unbanz a Meta partner?', 'Is Unbanz affiliated with Meta?')
        s = s.replace('Anyone claiming to be a Meta employee or partner rep, renting', 'Anyone who says they can switch your account back on through a contact inside Meta, renting')
        s = s.replace('Anyone claiming to be a Meta employee or “partner rep” who can flip a switch,', 'Anyone who says they can switch your account back on through a contact inside Meta,')
    if slug in ('how-long-does-meta-ad-account-review-take',):
        pass
    qs = re.findall(r'<summary>(.*?)<span', s)
    low = ' || '.join(qs).lower(); picks = []
    for k in range(len(POOL)):
        q, key, a = POOL[(idx + k) % len(POOL)]
        if re.search(key, low): continue
        if slug.endswith('rejected-what-next') and q.startswith('What if Meta'): continue
        if 'new-ad-account' in slug and q.startswith('Should I open'): continue
        picks.append((q, a()))
        if len(picks) == 2: break
    if not done: s = add_faq(s, picks)
    blk = links_block(slug)
    if 'id="next-steps"' not in s:
        if '<h2 id="about-unbanz">' in s: s = s.replace('<h2 id="about-unbanz">', blk + '<h2 id="about-unbanz">', 1)
        elif '<h2 id="help">' in s: s = s.replace('<h2 id="help">', blk + '<h2 id="help">', 1)
        else: s = re.sub(r'(</article>)(<section class="vt)', lambda m: blk + m.group(1) + m.group(2), s, 1) if '<article class="guide-body' in s else s
    assert 'id="next-steps"' in s, slug
    # hub in the related nav
    if not done:
        s = re.sub(r'(<nav class="related-services[^"]*"[^>]*>)', r'\1<a href="/%s/">Meta ad account help</a>' % HUB, s, 1) if s.count('<nav class="related-services') else s
    open(f, 'w', encoding='utf-8').write(s)
if __name__ == '__main__':
    for i, slug in enumerate(EXISTING):
        if slug == 'ad-account-recovery': continue
        process(i, i) if False else process(slug, i)
    print('ok', len(EXISTING))
