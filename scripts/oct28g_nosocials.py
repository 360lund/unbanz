#!/usr/bin/env python3
"""Remove unbanz's own social profile links/icons/handles (Instagram + X @unbanzhq): social-links blocks, sameAs entries, twitter:site/creator, alternateName handle. Idempotent."""
import glob, re, sys
A = r'<a [^>]*href="https://(?:www\.)?(?:instagram\.com|x\.com|twitter\.com)/unbanzhq/?"[^>]*>.*?</a>'
def clean(t):
    t = re.sub(A, '', t, flags=re.S)
    t = re.sub(r'<(div|span) class="social-links"></\1>', '', t)
    t = re.sub(r'<meta name="twitter:(?:site|creator)" content="@[^"]*">', '', t)
    t = re.sub(r'"https://(?:www\.)?(?:instagram\.com|x\.com|twitter\.com)/unbanzhq/?",?', '', t)
    t = re.sub(r'"sameAs":\[,', '"sameAs":[', t)
    t = t.replace(',"UnbanzHQ"', '').replace('"UnbanzHQ",', '')
    return t
if __name__ == '__main__':
    n = 0
    for f in glob.glob('**/*.html', recursive=True):
        t = open(f, encoding='utf-8').read(); c = clean(t)
        if c != t: open(f, 'w', encoding='utf-8').write(c); n += 1
    print('pages changed', n)
