"""Classic (pre-redesign) presentation for guides. Restores the 21 originals + hub from 5b529e7^
and rebuilds the new guides with the original template/markup (stylesheet site.7c2d3ae502c9.css)."""
import re, json, html, os, subprocess, sys, glob
sys.path.insert(0, '/workspace/site/scripts/guides')
import build_new as bn
from common import ROOT, wa_link, mail_link, attrs

BASE = '5b529e7^'
CSS = 'site.7c2d3ae502c9.css'
smart, plain = bn.smart, bn.plain

def git_show(path):
    return subprocess.run(['git', 'show', f'{BASE}:{path}'], cwd=ROOT, capture_output=True, check=True).stdout.decode('utf-8')

def top_cta(wa_text, svc, plat):
    return ('<p class="guide-cta-top" style="margin-top:16px"><strong>Rather have us handle it for you?</strong> '
            f'<a href="{wa_link(wa_text)}"{attrs(svc, plat)}>Message us on WhatsApp ↗︎</a></p>')

def shell_parts():
    h = git_show(f'guides/{bn.TEMPLATE_SLUG}/index.html')
    first_ld = h.find('<script type="application/ld+json">')
    org = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S).group(1)
    nodes = [n for n in json.loads(org)['@graph'] if n['@type'] in ('Organization', 'WebSite')]
    for n in nodes:
        if n['@type'] == 'Organization':
            n['sameAs'] = [u for u in n['sameAs'] if 'trustpilot' not in u.lower()]
    return h[:first_ld], nodes, h[h.find('<link rel="preload"'):h.find('<main id="content">') + len('<main id="content">')], h[h.find('</main>'):]

def build_page(g, parts):
    pre_head, nodes, mid, post = parts
    slug = g['slug']; url = f'https://unbanz.com/guides/{slug}/'
    # reuse schema/head generation from the current builder, then swap the body
    full = bn.build_page(g, (pre_head, nodes, mid, post), CSS)
    head_end = full.index('<main id="content">') + len('<main id="content">')
    head = full[:head_end]
    svc = g.get('svc', 'unban'); plat = g.get('plat'); cta = g['cta']
    body = ''.join(f'<h2 id="{sid}">{smart(h)}</h2>{smart(b)}' for sid, h, b in g['secs'])
    toc_items = ''.join(f'<li><a href="#{sid}">{smart(h)}</a></li>' for sid, h, _ in g['secs'])
    toc_items += '<li><a href="#faq">Frequently asked questions</a></li><li><a href="#sources">Official sources</a></li>'
    toc = f'<nav class="guide-toc" aria-label="Contents"><p>In this guide</p><ol>{toc_items}</ol></nav>'
    src = ''.join(f'<li><a href="{u}" target="_blank" rel="noopener noreferrer">{html.escape(l)}</a></li>' for l, u in g['src'])
    sources = (f'<div class="guide-sources" id="sources"><h2>Official sources</h2><ul>{src}</ul><p>Meta and Snap update their help pages and flows often. '
               'Always follow the wording on your own screen and the current official Help Center. Unbanz is an independent service and is not affiliated with Meta, Instagram, Facebook or Snapchat.</p></div>')
    article = f'<article class="guide-body container">{toc}{body}{sources}</article>'
    hero = ('<section class="service-hero"><div class="container"><a class="crumb" href="/guides/">Home / Guides</a>'
            f'<h1>{smart(html.escape(g["h1"], quote=False))}</h1><p class="quick-answer"><strong>Short answer:</strong> {smart(g["short"])}</p><p>{smart(g["intro"])}</p>'
            f'<p class="guide-meta">By the Unbanz team · Published <time datetime="{bn.DATE_ISO}">{bn.DATE_TXT}</time> · Updated <time datetime="{bn.DATE_ISO}">{bn.DATE_TXT}</time></p>'
            + top_cta(cta['top_wa'], svc, plat) + '</div></section>')
    faqh = ''.join(f'<details><summary>{smart(q)}<span aria-hidden="true">+</span></summary><p>{smart(a)}</p></details>' for q, a in g['faq'])
    faqs = ('<section class="faq-section" id="faq"><div class="container faq-layout"><div class="faq-intro"><p class="eyebrow">YOUR QUESTIONS</p><h2>Frequently asked questions</h2></div>'
            f'<div class="simple-faq">{faqh}</div></div></section>')
    gsvc = bn.GROUP_SVC[g['group']]
    proof = ('<section class="service-proof container"><h2>Want it done for you?</h2><p>Want us to handle it? Get a quote and send us the details. Your password stays with you.</p>'
             f'<div class="cta-pair"><a class="button button-blue" href="{wa_link(cta["wa"])}"{attrs(svc, plat)}>Get a quote on WhatsApp <span aria-hidden="true">↗︎</span></a>'
             f'<a class="button button-light" href="{mail_link(cta["subject"])}">Email us</a></div></section>')
    pills = ''.join(f'<a href="{h}">{html.escape(l)}</a>' for h, l in g['rel'])
    pills += f'<a href="{gsvc[0]}">{gsvc[1]}</a><a href="/guides/">All guides</a><a href="/contact/">Contact</a>'
    rel = f'<nav class="related-services container" aria-label="Related pages">{pills}</nav>'
    return head + hero + article + faqs + proof + rel + post

def restore_existing():
    n = 0
    for p in subprocess.run(['git', 'ls-tree', '-r', '--name-only', BASE, 'guides/'], cwd=ROOT, capture_output=True).stdout.decode().split():
        if not p.endswith('/index.html'): continue
        open(f'{ROOT}/{p}', 'w', encoding='utf-8').write(git_show(p)); n += 1
    print('restored', n)

def main():
    restore_existing()
    guides = bn.load_guides()
    parts = shell_parts()
    new = {g['slug'] for g in guides}
    for g in guides:
        page = build_page(g, parts)
        t = re.sub(r'<script.*?</script>', '', page, flags=re.S); t = re.sub(r'<[^>]+>', ' ', t)
        bad = bn.BAN.findall(t.replace('Independent service. Not affiliated with Meta.', ''))
        if bad: print('BANNED', g['slug'], bad)
        open(f'{ROOT}/guides/{g["slug"]}/index.html', 'w', encoding='utf-8').write(page)
    # inbound links into the restored originals' related-services nav
    for g in guides:
        for href in g.get('inbound', []):
            if not href.startswith('/guides/'): continue
            p = ROOT + href + 'index.html'
            h = open(p, encoding='utf-8').read()
            new_h = f'/guides/{g["slug"]}/'
            if f'href="{new_h}"' in h: continue
            m = re.search(r'(<nav class="related-services[^>]*>.*?)(<a href="/guides/">All guides</a>|</nav>)', h, re.S)
            assert m, p
            h = h[:m.end(1)] + f'<a href="{new_h}">{html.escape(g.get("pill") or g["h1"])}</a>' + h[m.end(1):]
            open(p, 'w', encoding='utf-8').write(h)
    print('guides', len(guides))

if __name__ == '__main__':
    main()
