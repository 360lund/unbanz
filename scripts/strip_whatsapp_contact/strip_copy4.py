import re, os, sys
R = [
 (r'Send it on  or to <a', 'Send it to <a'),
 (r'Message us on  or email <a', 'Email <a'),
 (r'link on  or to <a', 'link to <a'),
 (r'Contact:  or <a', 'Contact: <a'),
 (r'Écrivez-nous sur  ou à <a', 'Écrivez-nous à <a'),
 (r'Stuur het via  of naar <a', 'Stuur het naar <a'),
 (r'<p>WhatsApp  or email <a', '<p>Email <a'),
 (r'or message us on  or at <a', 'or email us at <a'),
 (r'\b(on|via|sur|por|pelo|op|by)  (or|ou|o|of) (to |at |à |a |para |naar )?<a', r'\3<a'),
]
R = [(re.compile(a), b) for a, b in R]
n = 0
for root in sys.argv[1:]:
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in ('.git', 'node_modules', 'users', 'scripts', 'docs')]
        for f in fn:
            if not f.endswith(('.html', '.txt')): continue
            p = os.path.join(dp, f); t = open(p, encoding='utf-8').read(); o = t
            for r, s in R: t = r.sub(s, t)
            if t != o: open(p, 'w', encoding='utf-8').write(t); n += 1
print(n)
