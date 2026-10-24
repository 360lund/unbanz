import re, json, html, sys
sys.path.insert(0, '/workspace/site/scripts/guides')
from common import *

GROUPS = [('instagram', 'Instagram', 'Disabled, suspended, locked or hacked accounts, strikes, usernames and reporting.'),
          ('facebook', 'Facebook', 'Disabled profiles, locked or hacked accounts, restricted Pages and reporting.'),
          ('ads', 'Ad accounts', 'Restricted or disabled Meta ad accounts, payment problems and Business Portfolios.'),
          ('snapchat', 'Snapchat', 'Locked accounts, appeals, usernames and reporting.')]
EXISTING = {  # href -> (group, tag)
 '/guides/instagram-account-disabled/': ('instagram', 'Disabled'),
 '/guides/instagram-account-suspended-appeal/': ('instagram', 'Suspended'),
 '/guides/hacked-instagram-account-recovery/': ('instagram', 'Hacked'),
 '/guides/facebook-account-disabled-appeal/': ('facebook', 'Disabled'),
 '/guides/meta-ad-account-restricted/': ('ads', 'Restricted'),
 '/inactive-instagram-username/': ('instagram', 'Username'),
 '/taken-instagram-username/': ('instagram', 'Username'),
 '/snapchat-username-claim/': ('snapchat', 'Username'),
 '/facebook-username-claim/': ('facebook', 'Username'),
 '/guides/why-instagram-bans-accounts/': ('instagram', 'Rules'),
 '/guides/instagram-account-disabled-for-no-reason/': ('instagram', 'Disabled'),
 '/guides/instagram-disabled-no-appeal-button/': ('instagram', 'Disabled'),
 '/guides/instagram-account-integrity/': ('instagram', 'Suspended'),
 '/guides/instagram-account-locked/': ('instagram', 'Locked'),
 '/guides/facebook-account-locked/': ('facebook', 'Locked'),
 '/guides/meta-ad-account-disabled-payment/': ('ads', 'Payments'),
 '/guides/instagram-video-selfie-verification/': ('instagram', 'Verification'),
 '/guides/facebook-page-restricted/': ('facebook', 'Page'),
 '/guides/ad-account-circumventing-systems/': ('ads', 'Policy'),
 '/guides/ad-account-unacceptable-business-practices/': ('ads', 'Policy'),
 '/guides/instagram-community-guidelines-strikes/': ('instagram', 'Strikes'),
 '/guides/instagram-disabled-for-impersonation/': ('instagram', 'Disabled'),
 '/guides/meta-business-portfolio-restricted/': ('ads', 'Business Portfolio'),
 '/ban/': ('instagram', 'Report'),
 '/fake-account-takedown/': ('instagram', 'Report'),
 '/impersonation-account-removal/': ('facebook', 'Report'),
 '/guides/snapchat-account-locked/': ('snapchat', 'Locked'),
 '/snapchat-account-ban-service/': ('snapchat', 'Report'),
 '/guides/hacked-facebook-account-recovery/': ('facebook', 'Hacked'),
}

def cards():
    out = []
    for c in json.load(open(ROOT + '/scripts/guides/hub_existing.json')):
        g, t = EXISTING[c['href']]
        out.append(dict(href=c['href'], title=c['title'], desc=c['desc'], group=g, tag=t))
    try:
        for c in json.load(open(ROOT + '/scripts/guides/new_index.json')):
            out.append(dict(href=f"/guides/{c['slug']}/", title=html.escape(c['h1'], quote=False), desc=html.escape(c['desc'], quote=False), group=c['group'], tag=c['tag']))
    except FileNotFoundError:
        pass
    return out

def build():
    path = ROOT + '/guides/index.html'
    h = open(path, encoding='utf-8').read()
    allc = cards()
    sections = ''
    for gid, gname, gdesc in GROUPS:
        cs = [c for c in allc if c['group'] == gid]
        grid = ''.join(
            f'<a class="hub-card" href="{c["href"]}"><span class="hub-tag">{c["tag"]}</span><strong>{c["title"]}</strong>'
            f'<span class="hub-desc">{c["desc"]}</span><span class="hub-more">Read the guide →</span></a>' for c in cs)
        sections += f'<section class="hub-group" id="{gid}"><h2>{gname} <small>{len(cs)} guides</small></h2><div class="hub-grid">{grid}</div></section>'
    jump = '<nav class="hub-jump" aria-label="Jump to a platform">' + ''.join(f'<a href="#{g}">{n}</a>' for g, n, _ in GROUPS) + '</nav>'
    hero = ('<section class="service-hero"><div class="container"><a class="crumb" href="/">Home / Guides</a><h1>Account recovery guides.</h1>'
            '<p>Clear, practical guides based on Meta’s official help pages: what each notice means, how the official review routes work, and when to hand it to us. '
            'Clients share <a href="/reviews/">video reviews</a> of working with us.</p>' + jump + '</div></section>')
    cta = cta_card('close', 'Not sure which guide fits?', 'Tell us what you’re seeing',
                   'Send your username and a screenshot of the notice. We’ll point you to the right next step. We never ask for your password or login codes.',
                   'Hey Unbanz, I need help with an account and I am not sure which guide fits', 'Account help', 'unban', None)
    new_main = (hero + '<div class="guide-hub container">' + sections + '<div class="hub-cta">' + cta + '</div></div>')
    m = re.search(r'<main id="content">.*?</main>', h, re.S)
    old = m.group(0)
    rel = re.search(r'<nav class="related-services container" aria-label="Related services">.*?</nav>', old, re.S).group(0)
    h = h.replace(old, '<main id="content">' + new_main + rel + '</main>')
    h = h.replace('<body class="service-page">', '<body class="service-page guide-page">')
    # JSON-LD ItemList
    jm = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', h, re.S)
    data = json.loads(jm.group(2))
    for node in data['@graph']:
        if node.get('@type') == 'CollectionPage':
            items = node['mainEntity']['itemListElement']
            have = {i['url'] for i in items}
            for c in allc:
                u = 'https://unbanz.com' + c['href']
                if u not in have:
                    items.append({"@type": "ListItem", "position": len(items) + 1, "url": u, "name": html.unescape(c['title'])})
    h = h.replace(jm.group(0), jm.group(1) + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + jm.group(3))
    open(path, 'w', encoding='utf-8').write(h)
    print('hub built', len(allc))

if __name__ == '__main__':
    build()
