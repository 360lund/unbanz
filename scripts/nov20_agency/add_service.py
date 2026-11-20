"""Nov 20 2026 (d): every indexable agency page carries a Service node for the white-label program ($1,200 per case). Idempotent."""
import os, re, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')); os.chdir(ROOT)
B = 'https://unbanz.com/'
LD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
PAGES = ['agency-business-portfolio-disabled-all-client-ad-accounts-down', 'agency-client-account-banned-canada', 'agency-client-account-banned-france', 'agency-client-account-banned-netherlands',
         'agency-client-account-banned-uk', 'agency-client-account-banned-usa', 'client-ad-account-restricted-agency-is-admin', 'for-agencies-banned-client-accounts',
         'my-clients-instagram-got-disabled-what-do-i-do-as-their-agency', 'questions-agencies-ask-about-banned-client-accounts', 'white-label-recovery-fixed-fees-for-agencies']
for d in PAGES:
    f = d + '/index.html'; s = open(f, encoding='utf8').read(); url = B + d + '/'
    m = LD.search(s); g = json.loads(m.group(1)); graph = g.get('@graph')
    if graph is None: g = {"@context": "https://schema.org", "@graph": [{k: v for k, v in g.items() if k != '@context'}]}; graph = g['@graph']
    if any(n.get('@type') == 'Service' for n in graph): continue
    graph.append({"@type": "Service", "@id": url + "#service", "name": "White-label account recovery for agencies", "serviceType": "White-label social media account recovery and username claims",
                  "provider": {"@id": B + "#organization"}, "areaServed": "Worldwide", "url": B + "white-label-agency/",
                  "audience": {"@type": "BusinessAudience", "audienceType": "Marketing, PR, talent and reputation management agencies"},
                  "offers": {"@type": "Offer", "price": 1200, "priceCurrency": "USD", "description": "Per case (one account or one handle), paid upfront by bank transfer. Usually 7–14 days. 100% refund paid the same business day if not reinstated within 14 calendar days.", "url": B + "white-label-agency/"}})
    s = s[:m.start(1)] + json.dumps(g, ensure_ascii=False, separators=(',', ':')) + s[m.end(1):]
    open(f, 'w', encoding='utf8').write(s); print('service', d)
