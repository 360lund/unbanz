#!/usr/bin/env python3
"""Remove @unbanzhq handle mentions from copy (pages, llms files, README, generator scripts). Ordered, idempotent."""
import glob, re
R = [
 (r'We(?:’|\')re @unbanzhq on Instagram and X, and our terms', 'Our terms'),
 (r'2490, team@unbanz\.com and @unbanzhq on Instagram and X', '2490 and team@unbanz.com'),
 (r'2490, team@unbanz\.com and @unbanzhq\.', '2490 and team@unbanz.com.'),
 (r' On social we(?:’|\')re @unbanzhq on Instagram and X\.', ''),
 (r' and our socials are @unbanzhq on Instagram and X', ''),
 (r' and our socials are @unbanzhq(?=\.)', ''),
 (r'; @unbanzhq on Instagram and X', ''),
 (r' Instagram and X: @unbanzhq\.', ''),
 (r'\s*(?:- |<li>)Instagram and X: @unbanzhq(?:</li>)?', lambda m: '' if m.group(0).strip().startswith('-') else ''),
 (r' ?Socials:? @unbanzhq on Instagram and X\.', ''),
 (r'\), @unbanzhq sur Instagram et X\.', ').'),
 (r', and you(?:’|\')ll find us as @unbanzhq on Instagram and @unbanzhq on X', ''),
 (r'unbanz\.com, notre adresse e-mail officielle team@unbanz\.com et nos réseaux @unbanzhq', 'unbanz.com et notre adresse e-mail officielle team@unbanz.com'),
 (r' ou via @unbanzhq\.', '.'),
 (r'[\s\u00a0\u202f]*Sur les réseaux[\s\u00a0\u202f]*: @unbanzhq \(Instagram et X\)\.', ''),
 (r'[\s\u00a0\u202f]*Réseaux[\s\u00a0\u202f]*: @unbanzhq\.', ''),
 (r'<div class="email-option"><h2>(?:Find us on social|Sur les réseaux|Ook te vinden op|Também em|También en)</h2><p>[^<]*</p></div>', ''),
 (r'(?m)^- (?:Instagram|X): https://(?:www\.instagram\.com|x\.com)/unbanzhq/?\n', ''),
 (r'(?m)^X: https://x\.com/unbanzhq\n', ''),
 (r'team@unbanz\.com, @unbanzhq\.', 'team@unbanz.com.'),
 (r'Estamos como @unbanzhq no Instagram e no X\. ', ''),
 (r'Nos encuentras como @unbanzhq en Instagram y X\. ', ''),
 (r'Je vindt ons als @unbanzhq op Instagram en X\. ', ''),
 (r',\s*"UnbanzHQ"', ''), (r'"UnbanzHQ",\s*', ''),
]
if __name__ == '__main__':
    n = 0
    for f in glob.glob('**/*', recursive=True):
        if not re.search(r'\.(html|txt|md|py)$', f) or 'oct28g' in f: continue
        t = open(f, encoding='utf-8', errors='surrogateescape').read(); c = t
        for p, r in R: c = re.sub(p, r, c)
        if c != t: open(f, 'w', encoding='utf-8', errors='surrogateescape').write(c); n += 1
    print('files changed', n)
