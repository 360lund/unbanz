import re, os, sys
R = [
 (r'A WhatsApp or email click is not a paid job', 'An email click is not a paid job'),
 (r'Prefer email\?\s{1,3}WhatsApp or email\. You hear', 'Prefer email?  By email. You hear'),
 (r'(?m)^WhatsApp or email\.$', 'By email.'),
 (r'WhatsApp https://wa\.me/19342012490 , team@unbanz\.com', 'team@unbanz.com'),
 (r'Only contacts: unbanz\.com, WhatsApp \+1 934 201 2490, team@unbanz\.com', 'Only contacts: unbanz.com, team@unbanz.com'),
 (r'; WhatsApp \+1 934 201 2490, team@unbanz\.com', '; team@unbanz.com'),
 (r'WhatsApp: \+1 934 201 2490 Email: team@unbanz\.com', 'Email: team@unbanz.com'),
 (r'Official email: team@unbanz\.com\. WhatsApp: \+1 934 201 2490\.', 'Official email: team@unbanz.com.'),
 (r'Contact: WhatsApp https://wa\.me/19342012490 or team@unbanz\.com', 'Contact: team@unbanz.com'),
 (r'\+1 934 201 2490\. Our email is team@unbanz\.com\.', 'Email team@unbanz.com. That is our only contact address.'),
 (r"What is Unbanz's official WhatsApp number\?", 'How do I contact Unbanz officially?'),
]
R = [(re.compile(a), b) for a, b in R]
n = 0
for root in sys.argv[1:]:
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in ('.git', 'node_modules', 'users', 'scripts', 'docs')]
        for f in fn:
            if not f.endswith(('.html', '.txt', '.xml')): continue
            p = os.path.join(dp, f); t = open(p, encoding='utf-8').read(); o = t
            for r, s in R: t = r.sub(s, t)
            if t != o: open(p, 'w', encoding='utf-8').write(t); n += 1
print(n)
