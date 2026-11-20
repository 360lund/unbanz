"""Nov 20 2026 (d): link the agency program from every page: header nav + mobile nav ("For agencies"), footer
("White-label for agencies", + Agency resources in English), and one quiet contextual line on service/Q&A pages
("Handling this for a client? ..."). Localized hubs for fr/nl/es/pt-br, the English hub for other languages.
No contact details are added, so the 3-tier contact rule is untouched. Idempotent. Prints changed files to /tmp/sitewide_changed.txt."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from agency_1200 import agency_dirs, NEW
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')); os.chdir(ROOT)
EN = '/white-label-agency/'; GU = '/white-label-agency/guides/'
L = {
 'en': (EN, 'For agencies', 'White-label for agencies', 'Handling this for a client? <a href="/white-label-agency/">White-label recovery for agencies</a> runs under your brand. <a href="/white-label-agency/guides/">Agency resources</a>'),
 'fr': ('/fr/white-label-agences/', 'Agences', 'Marque blanche pour agences', 'Vous gérez ce dossier pour un client ? La <a href="/fr/white-label-agences/">récupération en marque blanche pour agences</a> se fait sous votre marque.'),
 'nl': ('/nl/white-label-bureau/', 'Bureaus', 'White-label voor bureaus', 'Regel je dit voor een klant? <a href="/nl/white-label-bureau/">White-label herstel voor bureaus</a> loopt onder jouw merk.'),
 'es': ('/es/white-label-agencias/', 'Agencias', 'Marca blanca para agencias', '¿Gestionas esto para un cliente? La <a href="/es/white-label-agencias/">recuperación en marca blanca para agencias</a> funciona con tu marca.'),
 'pt': ('/pt-br/white-label-agencias/', 'Agências', 'White-label para agências', 'Cuidando disso para um cliente? A <a href="/pt-br/white-label-agencias/">recuperação white-label para agências</a> funciona com a sua marca.'),
 'de': (EN, 'Agenturen', 'White-Label für Agenturen (EN)', 'Du kümmerst dich für einen Kunden darum? <a href="/white-label-agency/" hreflang="en">White-Label-Wiederherstellung für Agenturen</a> läuft unter deiner Marke (Seite auf Englisch).'),
 'it': (EN, 'Agenzie', 'White-label per agenzie (EN)', 'Gestisci questo caso per un cliente? Il <a href="/white-label-agency/" hreflang="en">recupero white-label per agenzie</a> lavora con il tuo marchio (pagina in inglese).'),
 'tr': (EN, 'Ajanslar', 'Ajanslar için white-label (EN)', 'Bunu bir müşteri için mi yürütüyorsunuz? <a href="/white-label-agency/" hreflang="en">Ajanslar için white-label kurtarma</a> sizin markanızla çalışır (sayfa İngilizce).'),
 'ar': (EN, 'الوكالات', 'العلامة البيضاء للوكالات (EN)', 'تتولى هذه الحالة لصالح عميل؟ <a href="/white-label-agency/" hreflang="en">الاستعادة بالعلامة البيضاء للوكالات</a> تعمل باسم علامتك التجارية، بسعر 1,200 دولار لكل حالة (الصفحة بالإنجليزية).'),
}
SKIP_CTX = set(agency_dirs()) | NEW | {'white-label-agency', 'white-label-agency/guides', '.', 'fr', 'nl', 'es', 'pt-br', 'de', 'it', 'tr', 'ar', 'zh-tw', 'zh-hk'}
CTX = re.compile(r'<p class="ag-ctx[^"]*"[^>]*>.*?</p>', re.S)
def add_nav(s, cls, href, label):
    m = re.search(r'(<nav[^>]*class="' + cls + r'"[^>]*>)(.*?)(</nav>)', s, re.S)
    if not m or 'white-label' in m.group(2): return s
    inner = m.group(2); a = f'<a href="{href}">{label}</a>'
    links = list(re.finditer(r'<a [^>]*href="([^"]*)"[^>]*>.*?</a>', inner, re.S))
    if links and re.search(r'contact|kontakt|contato|contacto|iletisim|%D8', links[-1].group(1)): inner = inner[:links[-1].start()] + a + inner[links[-1].start():]
    else: inner = inner + a
    return s[:m.start(2)] + inner + s[m.end(2):]
def add_footer(s, k, href, label):
    m = re.search(r'(<div class="footer-links">)(.*?)(</div>)', s, re.S)
    if not m: return s
    inner = m.group(2); add = ''
    if f'href="{href}"' not in inner: add += f'<a href="{href}">{label}</a>'
    if k in ('fr', 'nl', 'es', 'pt') and f'href="{EN}"' not in inner: add += f'<a href="{EN}" hreflang="en" lang="en">White-label for agencies</a>'
    if k == 'en' and f'href="{GU}"' not in inner: add += f'<a href="{GU}">Agency resources</a>'
    if not add: return s
    i = re.search(r'<a [^>]*hreflang=', inner)
    inner = inner[:i.start()] + add + inner[i.start():] if i else inner + add
    return s[:m.start(2)] + inner + s[m.end(2):]
def add_ctx(s, k, d):
    s = CTX.sub('', s)
    if d in SKIP_CTX: return s
    txt = L[k][3]
    m = re.search(r'<section class="answer-first[^"]*"[^>]*>', s)
    if m:
        j = s.index('</section>', m.end())
        return s[:j] + f'<p class="ag-ctx" style="margin:18px 0 0;font-size:15px;line-height:1.5;color:#5b7690;max-width:860px">{txt}</p>' + s[j:]
    i = s.find('<section class="faq-section"')
    if i > 0: return s[:i] + f'<p class="ag-ctx container" style="margin-top:32px;font-size:15px;line-height:1.5;color:#5b7690">{txt}</p>' + s[i:]
    return s
if __name__ == '__main__':
    ch = []
    for r, ds, fs in os.walk('.'):
        ds[:] = [x for x in ds if x not in ('.git', 'node_modules', 'scripts', 'assets', 'users')]
        for fn in fs:
            if not fn.endswith('.html'): continue
            p = os.path.join(r, fn); s = open(p, encoding='utf8').read()
            lang = (re.search(r'<html[^>]*\blang="([^"]+)"', s) or [None, 'en'])[1].lower()
            k = 'pt' if lang.startswith('pt') else lang[:2]
            if k not in L: continue  # zh pages already link their own agency page
            href, nav, foot, _ = L[k]
            t = add_nav(s, 'desktop-nav', href, nav); t = add_nav(t, 'mobile-nav', href, nav); t = add_footer(t, k, href, foot)
            if fn == 'index.html': t = add_ctx(t, k, os.path.relpath(r, '.'))
            if t != s: open(p, 'w', encoding='utf8').write(t); ch.append(os.path.relpath(p, '.'))
    open('/tmp/sitewide_changed.txt', 'w').write('\n'.join(ch)); print('changed', len(ch))
