import re, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'adacct'))
import lint as L
EXTRA = [r'price', r'upfront|up front|in advance', r'turnaround', r'\bquick(ly)?\b', r'instant', r'asap|same day|same-day', r'\bpay(ment)? (before|after|first|upfront)',
         r'we (will )?(get|restore|recover|unban|fix) (it|your|the)', r'success rate|\bsuccessful\b', r'\bpartner\b', r'trust ?pilot|\b\d(\.\d)?\s?/\s?5\b|stars?\b',
         r'\bwe guarantee|promise (you|to)', r'\bfree\b', r'\bsocial links\b', r'clarity', r'tiktok|linkedin|youtube|instagram\.com']
def check(f, username=False):
    pr = L.check(f)
    s = open(f, encoding='utf-8').read()
    vis = re.sub(r'<script[^>]*>.*?</script>|<section class="vt .*?</ul></section>|<link[^>]*>|<meta[^>]*>', '', s, flags=re.S).lower()
    vis = re.sub(r'<footer.*?</footer>', '', vis, flags=re.S).replace('quick answers', '')
    ex = list(EXTRA)
    if not username: ex.append(r'refund')
    for b in ex:
        for m in re.finditer(b, vis):
            pr.append((b, vis[max(0, m.start() - 40): m.end() + 40].replace('\n', ' ')))
    if 'href="/white-label-agency/">For agencies' not in s and '/fr/' not in f and '/pt-br/' not in f and '/es/' not in f: pr.append(('no For agencies link', ''))
    if s.count('class="vt-card"') != 5: pr.append(('testimonial cards', str(s.count('class="vt-card"'))))
    return pr
if __name__ == '__main__':
    root = L.ROOT; bad = 0
    files = sys.argv[1:]
    for f in files:
        pr = check(f, '/instagram-username-' in f or 'username' in f)
        if pr:
            bad += 1; print(os.path.relpath(f, root))
            for p in pr[:6]: print('   ', p)
    print('files', len(files), 'with problems', bad)
