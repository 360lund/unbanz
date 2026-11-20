"""Nov 20 2026 (d): agency/white-label pages show the white-label rate, $1,200 per case (consumer pages stay $1,000),
and lose the Meta logo hero art (/redesign/assets/meta.webp). Idempotent. Prints the changed page dirs."""
import os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')); os.chdir(ROOT)
PAT = re.compile(r'white-label|agenc|agentur|bureau|reseller|partner|marca-blanca|marque-blanche', re.I)
# consumer problems that merely mention an agency/partner: not agency work, keep consumer pricing
EXCL = {'former-business-partner-controls-business-portfolio', 'facebook-page-owned-by-former-agency', 'client-fired-agency-removed-access',
        'guides/meta-agency-partner-access', 'ad-account-restricted-after-agency-shared-access', 'agency-business-manager-restricted-after-adding-a-client',
        'white-label-agency', 'white-label-agency/guides'}
NEW = {'how-does-white-label-instagram-account-recovery-work', 'can-pr-and-talent-agencies-outsource-instagram-tiktok-recovery', 'how-do-social-media-agencies-recover-hacked-client-instagram',
       'white-label-social-media-unbanning-cost-for-agencies', 'how-agencies-recover-client-business-manager-or-ad-account', 'can-reputation-firms-white-label-instagram-username-claims',
       'talent-agencies-false-copyright-impersonation-bans-client-accounts', 'white-label-whatsapp-business-unban-for-agencies', 'how-to-vet-an-account-recovery-partner-for-your-agency',
       'agencies-bulk-instagram-disablements-one-agreement'}
def agency_dirs():
    out = []
    for r, ds, fs in os.walk('.'):
        ds[:] = [d for d in ds if d not in ('.git', 'node_modules', 'scripts', 'assets', 'users')]
        if 'index.html' not in fs: continue
        d = os.path.relpath(r, '.')
        if d != '.' and PAT.search(d) and d not in EXCL and d not in NEW: out.append(d)
    return sorted(out)
SEP = r'[,.\u202f\u00a0 ]'
R = [
 (re.compile(r'(\$\s?|US\$\s?|USD\s?)1(' + SEP + r')000(?![\d]|[,.]\d)'), r'\g<1>1\g<2>200'),
 (re.compile(r'(?<![\d.,$])1(' + SEP + r')000(\s?)(\$|USD|US\$|dollars?|dólares|dollar)'), r'1\g<1>200\g<2>\g<3>'),
 (re.compile(r'(\$)1000(?!\d)'), r'\g<1>1200'),
 (re.compile(r'(?<![\d.,])1000(\s?)(USD|\$)'), r'1200\g<1>\g<2>'),
 (re.compile(r'("(?:price|minPrice|lowPrice|highPrice|maxPrice)"\s*:\s*"?)1000(?:\.0+)?(?=["},\s])'), r'\g<1>1200'),
]
ART = re.compile(r'<div aria-hidden="true" class="ub-hero-art"><img[^>]*/redesign/assets/meta\.webp[^>]*/?></div>')
if __name__ == '__main__':
    ch = []
    for d in agency_dirs():
        f = os.path.join(d, 'index.html'); s = open(f, encoding='utf8').read(); t = s
        for rx, rep in R: t = rx.sub(rep, t)
        t = ART.sub('', t)
        if t != s: open(f, 'w', encoding='utf8').write(t); ch.append(d)
    open('/tmp/agency_1200_changed.txt', 'w').write('\n'.join(ch))
    print('agency pages', len(agency_dirs()), 'changed', len(ch))
