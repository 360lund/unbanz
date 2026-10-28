import re, sys, os, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
BAN = [r'\bcases?\b', r'\bwe review\b', r'fixed[- ]price', r'fast turnaround', r'\bfast\b', r'guarante', r'garantie', r'garant[ií]a', r'garantia', r'garantie',
       r'trustpilot', r'aggregaterating', r'ratingvalue', r'reviewcount', r'"@type":"review"', r'\+44', r'7723', r'rrweb', r'\bmeta partner', r'insider',
       r'within (a|\d+) ?(week|day|hour)', r'\b\d+\s?[-–]\s?\d+ days', r'\b\d+ days\b', r'[$£€]\s?\d', r'\d\s?(usd|eur|gbp)\b', r'instagram\.com/|facebook\.com/|twitter\.com|x\.com/|tiktok\.com|linkedin\.com',
       r'\bpartners? (of|with) meta', r'meta (rep|representative|employee)', r'\bwe know someone', r'bypass', r'\bcas\b', r'\bcasos?\b', r'\bgevall?en\b', r'\bgeval\b', r'\bzaak\b', r'rapide', r'r[áa]pid[oa]', r'\bsnel\b', r'forfait', r'prix fixe', r'precio fijo', r'pre[çc]o fixo', r'vaste prijs', r'nous examinons', r'revisamos', r'we beoordelen', r'sans délai', r'\d+ (jours|dagen|días|dias)', r'partenaire (officiel )?de meta', r'workaround for']
EMOJI = re.compile('[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B50\u2705]')
def check(path):
    s = open(path, encoding='utf-8').read()
    probs = []
    vis = re.sub(r'<script[^>]*>.*?</script>', lambda m: m.group(0) if 'ld+json' in m.group(0) else '', s, flags=re.S)
    vis = re.sub(r'<section class="vt .*?</ul></section>', '', vis, flags=re.S)
    low = vis.lower()
    low = re.sub(r'<link[^>]*>|<meta name="viewport"[^>]*>', '', low)
    for b in BAN:
        for m in re.finditer(b, low):
            ctx = low[max(0, m.start() - 40): m.end() + 40].replace('\n', ' ')
            probs.append((b, ctx))
    if EMOJI.search(s): probs.append(('emoji', ''))
    wa = set(re.findall(r'wa\.me/(\d+)', s)); 
    if wa - {'19342012490'}: probs.append(('bad whatsapp', str(wa)))
    if '<h1' in s and len(re.findall(r'<h1[ >]', s)) != 1: probs.append(('h1 count', ''))
    t = re.search(r'<title>(.*?)</title>', s, re.S)
    if t and len(t.group(1)) > 60: probs.append(('title>60', t.group(1)))
    d = re.search(r'<meta name="description" content="([^"]*)"', s)
    if d and len(d.group(1)) > 160: probs.append(('desc>160', str(len(d.group(1)))))
    if not re.search(r'affili|verbonden|afiliad|affilié', s): probs.append(('footer disclaimer missing', ''))
    return probs
if __name__ == '__main__':
    files = sys.argv[1:] or [os.path.join(ROOT, s.strip(), 'index.html') for s in open('/tmp/adacct_new_slugs.txt').read().split()]
    bad = 0
    for f in files:
        pr = check(f)
        if pr:
            bad += 1; print(os.path.relpath(f, ROOT))
            for p in pr[:6]: print('   ', p)
    print('files', len(files), 'with problems', bad)
