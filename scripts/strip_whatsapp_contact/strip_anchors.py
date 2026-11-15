# Remove our own WhatsApp contact links (wa.me) from static HTML, keeping email as the route.
import re, sys, os
from html.parser import HTMLParser

VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
WA_HREF = re.compile(r'href="https?://(?:api\.)?wa\.me/[^"]*"|href="https?://api\.whatsapp\.com/send[^"]*"', re.I)

class P(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=False)
        self.text = text
        self.ls = [0]
        for m in re.finditer('\n', text): self.ls.append(m.end())
        self.stack = []  # [tag, start, children_list]
        self.root = {'tag': '#root', 's': 0, 'e': len(text), 'kids': [], 'attrs': {}}
        self.stack = [self.root]
        self.nodes = []
    def off(self):
        l, c = self.getpos(); return self.ls[l-1] + c
    def handle_starttag(self, tag, attrs):
        s = self.off(); raw = self.get_starttag_text() or ''
        n = {'tag': tag, 's': s, 'oe': s+len(raw), 'e': None, 'kids': [], 'attrs': dict(attrs), 'parent': self.stack[-1]}
        self.stack[-1]['kids'].append(n); self.nodes.append(n)
        if tag in VOID or raw.endswith('/>'):
            n['e'] = n['oe']
        elif tag in ('script', 'style'):
            self.stack.append(n)
        else:
            self.stack.append(n)
    def handle_endtag(self, tag):
        s = self.off(); e = self.text.find('>', s) + 1
        for i in range(len(self.stack)-1, 0, -1):
            if self.stack[i]['tag'] == tag:
                for j in range(len(self.stack)-1, i, -1):
                    self.stack[j]['e'] = s  # implicitly closed
                self.stack[i]['e'] = e; self.stack[i]['ce'] = s
                del self.stack[i:]
                return

def is_wa(n):
    return n['tag'] == 'a' and re.match(r'https?://(?:api\.)?(?:wa\.me/|whatsapp\.com/send)', n['attrs'].get('href') or '', re.I)
def is_mail(n):
    return n['tag'] == 'a' and (n['attrs'].get('href') or '').lower().startswith('mailto:')
def desc(n):
    out = []
    for k in n['kids']:
        out.append(k); out.extend(desc(k))
    return out

def relabel(inner):
    t = inner
    rep = [
        (r'Send us the notice on WhatsApp', 'Send us the notice by email'),
        (r'Get it done on WhatsApp', 'Get it done by email'),
        (r'(?:Message|Chat with|Text|Write to) us on WhatsApp', 'Email us'),
        (r'Chat on WhatsApp', 'Email us'),
        (r'Continue on WhatsApp', 'Continue by email'),
        (r'Open WhatsApp', 'Email us'),
        (r'Écrivez-nous sur WhatsApp', 'Écrivez-nous par e-mail'),
        (r'Stuur ons een bericht op WhatsApp', 'Mail ons'),
        (r'Escríbenos por WhatsApp', 'Escríbenos por correo'),
        (r'Mande uma mensagem no WhatsApp', 'Envie um e-mail'),
        (r'\s+(?:on|via|over|by) WhatsApp', ' by email'),
        (r'WhatsApp', 'email'),
    ]
    for a, b in rep:
        t = re.sub(a, b, t)
    return t

def process(text):
    p = P(text); p.feed(text); p.close()
    first_mail = None
    for n in p.nodes:
        if is_mail(n):
            first_mail = n['attrs']['href']; break
    if not first_mail:
        first_mail = 'mailto:team@unbanz.com?subject=Account%20help'
    edits = []  # (s, e, replacement)
    stats = {'removed': 0, 'converted': 0, 'pref_removed': 0}
    for n in p.nodes:
        if not is_wa(n) or n['e'] is None: continue
        par = n['parent']
        sib = [d for d in desc(par) if d is not n]
        mails = [d for d in sib if is_mail(d)]
        pcls = par['attrs'].get('class') or ''
        btnmail = [m for m in mails if re.search(r'\b(button|hx-start|mc-mail|cm-mail)\b', m['attrs'].get('class') or '') or 'mobile-contact' in pcls or 'mc-actions' in pcls]
        has_hx = any('hx-start' in (d['attrs'].get('class') or '') for d in sib)
        if btnmail or has_hx or (mails and not any('hero-email' in (m['attrs'].get('class') or '') for m in mails)):
            edits.append((n['s'], n['e'], '')); stats['removed'] += 1
            continue
        pref = [m for m in mails if 'hero-email' in (m['attrs'].get('class') or '')]
        href = pref[0]['attrs']['href'] if pref else first_mail
        open_tag = text[n['s']:n['oe']]
        open_tag = WA_HREF.sub('href="%s"' % href.replace('"', '&quot;'), open_tag, count=1)
        open_tag = re.sub(r'\s+(target="_blank"|rel="noopener(?: noreferrer)?"|data-direct(?:="[^"]*")?)(?=[\s>/])', '', open_tag)
        inner = text[n['oe']:n['ce']]
        new = open_tag + relabel(inner) + '</a>'
        edits.append((n['s'], n['e'], new)); stats['converted'] += 1
        for m in pref:
            edits.append((m['s'], m['e'], '')); stats['pref_removed'] += 1
    edits.sort(key=lambda x: x[0], reverse=True)
    last = None
    for s, e, r in edits:
        if last is not None and e > last: continue
        text = text[:s] + r + text[e:]; last = s
    return text, stats

if __name__ == '__main__':
    tot = {'files': 0, 'removed': 0, 'converted': 0, 'pref_removed': 0}
    for root in sys.argv[1:]:
        for dp, dn, fn in os.walk(root):
            dn[:] = [d for d in dn if d not in ('.git', 'node_modules', 'users', 'scripts', 'assets', 'api')]
            for f in fn:
                if not f.endswith('.html'): continue
                path = os.path.join(dp, f)
                t = open(path, encoding='utf-8').read()
                if 'wa.me' not in t and 'whatsapp.com/send' not in t: continue
                nt, st = process(t)
                if nt != t:
                    open(path, 'w', encoding='utf-8').write(nt); tot['files'] += 1
                    for k in st: tot[k] += st[k]
    print(tot)
