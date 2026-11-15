# -*- coding: utf-8 -*-
"""Email-only contact + email CTA pass (Nov 15 2026). Idempotent.
apply_page(html, rel_path, brand, css_href) -> html        (rel_path like 'faq/index.html')
apply_llms(text, brand) -> text
Contact is team@unbanz.com only. No phone, no WhatsApp. Prices untouched."""
import re, json
from urllib.parse import quote

EMAIL = 'team@unbanz.com'
ORG_TYPES = {'Organization', 'ProfessionalService', 'LocalBusiness', 'Corporation', 'OnlineBusiness', 'ProfessionalOrganization'}

S = {
 'en': dict(hdr='Email us', btn='Email us', eye='GET HELP BY EMAIL', h='Tell us what happened.',
   p='Email {E} with the platform, your username or profile link, and what happened. Email is our only contact channel.',
   note='Never send your password or login codes.',
   only='Email is our only contact channel: {E}. We don’t use phone or WhatsApp. Include the platform, your username or profile link, and what happened.',
   q='How do I contact {B}?', a='By email only: {E}. Include the platform, your username or profile link, and what happened. We don’t take phone calls or WhatsApp messages, and we never need your password.',
   body='Hi {B},\n\nPlatform: \nUsername or profile link: \nWhat happened: \nCountry: \n\nThanks', subj='Account help'),
 'fr': dict(hdr='Écrivez-nous', btn='Écrivez-nous', eye='AIDE PAR E-MAIL', h='Dites-nous ce qui s’est passé.',
   p='Écrivez à {E} en indiquant la plateforme, votre nom d’utilisateur ou le lien du profil, et ce qui s’est passé. L’e-mail est notre seul moyen de contact.',
   note='N’envoyez jamais de mot de passe ni de code de connexion.',
   only='L’e-mail est notre seul moyen de contact : {E}. Nous n’utilisons ni téléphone ni WhatsApp. Indiquez la plateforme, votre nom d’utilisateur ou le lien du profil, et ce qui s’est passé.',
   q='Comment contacter {B} ?', a='Uniquement par e-mail : {E}. Indiquez la plateforme, votre nom d’utilisateur ou le lien du profil, et ce qui s’est passé. Nous ne prenons ni appels ni messages WhatsApp, et nous n’avons jamais besoin de votre mot de passe.',
   body='Bonjour {B},\n\nPlateforme : \nNom d’utilisateur ou lien du profil : \nCe qui s’est passé : \nPays : \n\nMerci', subj='Aide pour un compte'),
 'es': dict(hdr='Escríbenos', btn='Escríbenos', eye='AYUDA POR CORREO', h='Cuéntanos qué ha pasado.',
   p='Escribe a {E} con la plataforma, tu nombre de usuario o enlace del perfil, y qué ha pasado. El correo es nuestro único canal de contacto.',
   note='Nunca envíes tu contraseña ni códigos de acceso.',
   only='El correo es nuestro único canal de contacto: {E}. No usamos teléfono ni WhatsApp. Indica la plataforma, tu nombre de usuario o enlace del perfil, y qué ha pasado.',
   q='¿Cómo contacto con {B}?', a='Solo por correo: {E}. Indica la plataforma, tu nombre de usuario o enlace del perfil, y qué ha pasado. No atendemos llamadas ni mensajes de WhatsApp, y nunca necesitamos tu contraseña.',
   body='Hola, {B}:\n\nPlataforma: \nNombre de usuario o enlace del perfil: \nQué ha pasado: \nPaís: \n\nGracias', subj='Ayuda con una cuenta'),
 'pt': dict(hdr='E-mail', btn='Envie um e-mail', eye='AJUDA POR E-MAIL', h='Conte o que aconteceu.',
   p='Escreva para {E} com a plataforma, seu nome de usuário ou link do perfil e o que aconteceu. O e-mail é nosso único canal de contato.',
   note='Nunca envie sua senha nem códigos de acesso.',
   only='O e-mail é nosso único canal de contato: {E}. Não usamos telefone nem WhatsApp. Informe a plataforma, seu nome de usuário ou link do perfil e o que aconteceu.',
   q='Como entro em contato com a {B}?', a='Somente por e-mail: {E}. Informe a plataforma, seu nome de usuário ou link do perfil e o que aconteceu. Não atendemos ligações nem mensagens de WhatsApp, e nunca precisamos da sua senha.',
   body='Olá, {B}\n\nPlataforma: \nNome de usuário ou link do perfil: \nO que aconteceu: \nPaís: \n\nObrigado', subj='Ajuda com uma conta'),
 'nl': dict(hdr='Mail ons', btn='Mail ons', eye='HULP PER E-MAIL', h='Vertel ons wat er is gebeurd.',
   p='Mail {E} met het platform, je gebruikersnaam of profiellink en wat er is gebeurd. E-mail is ons enige contactkanaal.',
   note='Stuur nooit wachtwoorden of inlogcodes.',
   only='E-mail is ons enige contactkanaal: {E}. We gebruiken geen telefoon of WhatsApp. Vermeld het platform, je gebruikersnaam of profiellink en wat er is gebeurd.',
   q='Hoe neem ik contact op met {B}?', a='Alleen per e-mail: {E}. Vermeld het platform, je gebruikersnaam of profiellink en wat er is gebeurd. We nemen geen telefoontjes of WhatsApp-berichten aan en we hebben nooit je wachtwoord nodig.',
   body='Hoi {B},\n\nPlatform: \nGebruikersnaam of profiellink: \nWat er is gebeurd: \nLand: \n\nBedankt', subj='Hulp met een account'),
 'de': dict(hdr='E-Mail', btn='E-Mail schreiben', eye='HILFE PER E-MAIL', h='Schreiben Sie uns, was passiert ist.',
   p='Schreiben Sie an {E}: die Plattform, Ihren Benutzernamen oder Profillink und was passiert ist. E-Mail ist unser einziger Kontaktweg.',
   note='Senden Sie niemals Passwörter oder Anmeldecodes.',
   only='E-Mail ist unser einziger Kontaktweg: {E}. Wir nutzen weder Telefon noch WhatsApp. Nennen Sie die Plattform, Ihren Benutzernamen oder Profillink und was passiert ist.',
   q='Wie erreiche ich {B}?', a='Nur per E-Mail: {E}. Nennen Sie die Plattform, Ihren Benutzernamen oder Profillink und was passiert ist. Wir nehmen keine Anrufe oder WhatsApp-Nachrichten an und brauchen nie Ihr Passwort.',
   body='Hallo {B},\n\nPlattform: \nBenutzername oder Profillink: \nWas passiert ist: \nLand: \n\nDanke', subj='Hilfe mit einem Konto'),
 'it': dict(hdr='Scrivici', btn='Scrivici', eye='AIUTO VIA EMAIL', h='Raccontaci cosa è successo.',
   p='Scrivi a {E} indicando la piattaforma, il tuo nome utente o link del profilo e cosa è successo. L’email è il nostro unico canale di contatto.',
   note='Non inviare mai password o codici di accesso.',
   only='L’email è il nostro unico canale di contatto: {E}. Non usiamo telefono né WhatsApp. Indica la piattaforma, il tuo nome utente o link del profilo e cosa è successo.',
   q='Come contatto {B}?', a='Solo via email: {E}. Indica la piattaforma, il tuo nome utente o link del profilo e cosa è successo. Non rispondiamo a chiamate né a messaggi WhatsApp e non ci serve mai la tua password.',
   body='Ciao {B},\n\nPiattaforma: \nNome utente o link del profilo: \nCosa è successo: \nPaese: \n\nGrazie', subj='Aiuto per un account'),
 'tr': dict(hdr='E-posta', btn='E-posta gönderin', eye='E-POSTA İLE YARDIM', h='Ne olduğunu bize anlatın.',
   p='{E} adresine platformu, kullanıcı adınızı veya profil bağlantınızı ve ne olduğunu yazın. E-posta tek iletişim kanalımızdır.',
   note='Şifrenizi veya giriş kodlarınızı asla göndermeyin.',
   only='E-posta tek iletişim kanalımızdır: {E}. Telefon veya WhatsApp kullanmıyoruz. Platformu, kullanıcı adınızı veya profil bağlantınızı ve ne olduğunu yazın.',
   q='{B} ile nasıl iletişime geçerim?', a='Yalnızca e-posta ile: {E}. Platformu, kullanıcı adınızı veya profil bağlantınızı ve ne olduğunu yazın. Telefon araması veya WhatsApp mesajı kabul etmiyoruz ve şifrenize asla ihtiyacımız yoktur.',
   body='Merhaba {B},\n\nPlatform: \nKullanıcı adı veya profil bağlantısı: \nNe oldu: \nÜlke: \n\nTeşekkürler', subj='Hesap yardımı'),
 'ar': dict(hdr='راسلنا', btn='راسلنا عبر البريد', eye='المساعدة عبر البريد الإلكتروني', h='أخبرنا بما حدث.',
   p='راسل {E} واذكر المنصة واسم المستخدم أو رابط الملف الشخصي وما حدث. البريد الإلكتروني هو وسيلة التواصل الوحيدة لدينا.',
   note='لا ترسل كلمة المرور أو رموز الدخول أبدًا.',
   only='البريد الإلكتروني هو وسيلة التواصل الوحيدة لدينا: {E}. لا نستخدم الهاتف ولا واتساب. اذكر المنصة واسم المستخدم أو رابط الملف الشخصي وما حدث.',
   q='كيف أتواصل مع {B}؟', a='عبر البريد الإلكتروني فقط: {E}. اذكر المنصة واسم المستخدم أو رابط الملف الشخصي وما حدث. لا نستقبل مكالمات ولا رسائل واتساب، ولا نحتاج أبدًا إلى كلمة المرور.',
   body='مرحبًا {B}،\n\nالمنصة: \nاسم المستخدم أو رابط الملف الشخصي: \nما حدث: \nالبلد: \n\nشكرًا', subj='مساعدة في حساب'),
 'zh': dict(hdr='電郵聯絡', btn='寄電子郵件給我們', eye='以電子郵件取得協助', h='告訴我們發生了什麼事。',
   p='請寄信至 {E}，說明平台、您的使用者名稱或個人檔案連結，以及發生的情況。電子郵件是我們唯一的聯絡管道。',
   note='請勿傳送密碼或登入驗證碼。',
   only='電子郵件是我們唯一的聯絡管道：{E}。我們不使用電話或 WhatsApp。請說明平台、您的使用者名稱或個人檔案連結，以及發生的情況。',
   q='如何聯絡 {B}？', a='僅限電子郵件：{E}。請說明平台、您的使用者名稱或個人檔案連結，以及發生的情況。我們不接聽電話，也不使用 WhatsApp，且絕不需要您的密碼。',
   body='您好 {B}，\n\n平台：\n使用者名稱或個人檔案連結：\n發生的情況：\n國家／地區：\n\n謝謝', subj='帳號協助'),
}

def lang_of(html):
    m = re.search(r'<html[^>]*\blang="([^"]+)"', html)
    l = (m.group(1) if m else 'en').lower()
    return l[:2] if l[:2] in S else 'en'

def T(lang, key, brand):
    return S[lang][key].replace('{E}', EMAIL).replace('{B}', brand)

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

def mailto(lang, brand, subject=None):
    subj = subject if subject is not None else quote(T(lang, 'subj', brand), safe='')
    return 'mailto:%s?subject=%s&amp;body=%s' % (EMAIL, subj, quote(T(lang, 'body', brand), safe=''))

MAILTO_RE = re.compile(r'href="mailto:team@unbanz\.com([^"]*)"', re.I)

def prefill(html, lang, brand):
    def sub(m):
        q = m.group(1)
        if 'body=' in q:
            return m.group(0)
        sm = re.search(r'subject=([^&"]*)', q)
        return 'href="%s"' % mailto(lang, brand, sm.group(1) if sm else None)
    return MAILTO_RE.sub(sub, html)

# ---------- JSON-LD ----------
LD_RE = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.S)

def _types(n):
    t = n.get('@type')
    return set(t) if isinstance(t, list) else {t} if t else set()

def _is_ours(n, brand, host):
    name = str(n.get('name', '')).strip().lower()
    ident = str(n.get('@id', '')) + ' ' + str(n.get('url', ''))
    return name == brand.lower() or (host and host in ident)

def _fix_org(n):
    ch = False
    if n.get('email') != EMAIL: n['email'] = EMAIL; ch = True
    if 'telephone' in n: n.pop('telephone'); ch = True
    cps = n.get('contactPoint')
    if isinstance(cps, dict): cps = [cps]
    if not cps:
        cps = [{'@type': 'ContactPoint', 'contactType': 'customer support'}]; ch = True
    for cp in cps:
        if not isinstance(cp, dict): continue
        if 'telephone' in cp: cp.pop('telephone'); ch = True
        if cp.get('email') != EMAIL: cp['email'] = EMAIL; ch = True
        cp.setdefault('@type', 'ContactPoint')
        cp.setdefault('contactType', 'customer support')
        if str(cp.get('url', '')).startswith(('https://wa.me', 'mailto:')) or 'url' not in cp:
            if cp.get('url') != 'mailto:' + EMAIL: cp['url'] = 'mailto:' + EMAIL; ch = True
    if n.get('contactPoint') != cps: n['contactPoint'] = cps
    return ch

def _walk(o, fn):
    if isinstance(o, dict):
        fn(o)
        for v in list(o.values()): _walk(v, fn)
    elif isinstance(o, list):
        for v in o: _walk(v, fn)

def fix_jsonld(html, brand, host, faq_q=None):
    """faq_q: (question, answer) to make sure the page's FAQPage carries. Returns (html, stats)."""
    st = {'blocks': 0, 'changed': 0, 'bad': 0, 'faq_added': 0}
    has_faq = [False]
    def sub(m):
        st['blocks'] += 1
        raw = m.group(2)
        try:
            data = json.loads(raw)
        except Exception:
            st['bad'] += 1; return m.group(0)
        ch = [False]
        def fn(n):
            ty = _types(n)
            if ty & ORG_TYPES and _is_ours(n, brand, host):
                if _fix_org(n): ch[0] = True
            if 'FAQPage' in ty and faq_q:
                has_faq[0] = True
                me = n.get('mainEntity')
                if isinstance(me, dict): me = [me]
                me = me or []
                if not any(isinstance(x, dict) and x.get('name') == faq_q[0] for x in me):
                    me.insert(0, {'@type': 'Question', 'name': faq_q[0], 'acceptedAnswer': {'@type': 'Answer', 'text': faq_q[1]}})
                    n['mainEntity'] = me; ch[0] = True; st['faq_added'] += 1
        _walk(data, fn)
        if not ch[0]: return m.group(0)
        st['changed'] += 1
        out = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
        return m.group(1) + out + m.group(3)
    html = LD_RE.sub(sub, html)
    if faq_q and not has_faq[0] and '</head>' in html:
        blk = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': faq_q[0], 'acceptedAnswer': {'@type': 'Answer', 'text': faq_q[1]}}]}
        html = html.replace('</head>', '<script type="application/ld+json">' + json.dumps(blk, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + '</script></head>', 1)
        st['faq_added'] += 1
    return html, st

# ---------- visible additions ----------
def add_header_btn(html, lang, brand):
    m = re.search(r'<header\b[^>]*>.*?</header>', html, re.S)
    if not m or 'ecta-hdr' in m.group(0):
        return html
    hdr = m.group(0)
    # header already has an email link (home pages): add a mobile-only button, since that link hides at 650px
    cls = 'ecta-hdr ecta-m' if 'mailto:' in hdr else 'ecta-hdr'
    btn = '<a class="%s" href="%s" data-service="email">%s</a>' % (cls, mailto(lang, brand), esc(T(lang, 'hdr', brand)))
    if '<button class="menu-button"' in hdr:
        new = hdr.replace('<button class="menu-button"', btn + '<button class="menu-button"', 1)
    else:
        new = hdr[:-len('</header>')] + btn + '</header>'
    return html[:m.start()] + new + html[m.end():]

def add_only_line(html, lang, brand):
    if 'class="ecta-only"' in html or '</h1>' not in html:
        return html
    return html.replace('</h1>', '</h1><p class="ecta-only">%s</p>' % esc(T(lang, 'only', brand)), 1)

def add_visible_faq(html, lang, brand, h3_ok=False):
    q = T(lang, 'q', brand)
    vis = re.sub(r'<script\b.*?</script>', '', html.split('</head>', 1)[-1], flags=re.S)
    if esc(q) in vis or q in vis:
        return html
    m = re.search(r'(<section[^>]*(?:class="[^"]*faq[^"]*"|id="faq")[^>]*>)', html)
    start = m.end() if m else 0
    d = re.compile(r'<details[^>]*>\s*<summary[^>]*>(.*?)</summary>', re.S).search(html, start)
    if not m or not d:
        if not h3_ok:
            return html
        i = html.find('</h1>'); j = html.find('<h3>', i) if i >= 0 else -1
        if j < 0 or j > html.rfind('</main>'):
            return html
        return html[:j] + '<h3>%s</h3><p>%s</p>' % (esc(q), esc(T(lang, 'a', brand))) + html[j:]
    tail = '<span aria-hidden="true">+</span>' if '<span aria-hidden="true">+</span>' in d.group(1) else ''
    item = '<details><summary>%s%s</summary><p>%s</p></details>' % (esc(q), tail, esc(T(lang, 'a', brand)))
    return html[:d.start()] + item + html[d.start():]

def add_band(html, lang, brand):
    if 'ecta-band' in html or '</main>' not in html:
        return html
    if any(k in html for k in ('service-proof', 'class="closing', 'contact-intro')):
        return html
    band = ('<section class="ecta-band container" aria-label="%s"><div class="ecta-card"><p class="ecta-eye">%s</p><h2>%s</h2><p>%s</p>'
            '<a class="ecta-btn" href="%s" data-service="email">%s <span aria-hidden="true">→</span></a><p class="ecta-note">%s</p></div></section>') % (
        esc(T(lang, 'eye', brand)), esc(T(lang, 'eye', brand)), esc(T(lang, 'h', brand)), esc(T(lang, 'p', brand)), mailto(lang, brand),
        esc(T(lang, 'btn', brand)), esc(T(lang, 'note', brand)))
    m = re.search(r'<section[^>]*(?:class="[^"]*faq[^"]*"|id="faq")[^>]*>', html)
    if m and m.start() < html.rfind('</main>'):
        return html[:m.start()] + band + html[m.start():]
    i = html.rfind('</main>')
    return html[:i] + band + html[i:]

def relabel(html, lang):
    # mobile sticky bar and guide top CTA: "Email" -> "Email us"
    if lang == 'en':
        html = re.sub(r'(<a class="mc-mail" href="mailto:[^"]*"[^>]*>)Email(</a>)', r'\1Email us\2', html)
        html = re.sub(r'(<div class="mobile-contact">(?:<div class="mc-actions">)?<a [^>]*href="mailto:[^"]*"[^>]*>)Email(<)', r'\1Email us\2', html)
    return html

TEXT_FIX = [
 ('Pick your issue to open a WhatsApp message.', 'Pick your issue to open an email.'),
 ('Choisissez votre situation pour ouvrir un message WhatsApp.', 'Choisissez votre situation pour ouvrir un e-mail.'),
 ('Kies wat je nodig hebt en we openen WhatsApp met een bericht dat al klaarstaat. Je kunt het nog aanpassen voordat je het verstuurt.', 'Kies wat je nodig hebt en je e-mail opent met een bericht dat al klaarstaat. Je kunt het nog aanpassen voordat je het verstuurt.'),
 ('Elige lo que necesitas y abrimos WhatsApp con un mensaje ya preparado. Puedes modificarlo antes de enviarlo.', 'Elige lo que necesitas y se abrirá tu correo con un mensaje ya preparado. Puedes modificarlo antes de enviarlo.'),
 ('Escolha o que você precisa e abrimos o WhatsApp com uma mensagem já pronta. Você pode editá-la antes de enviar.', 'Escolha o que você precisa e o seu e-mail abre com uma mensagem já pronta. Você pode editá-la antes de enviar.'),
 ('We work in English over WhatsApp and email.', 'We work in English by email.'),
 ('We work in English by WhatsApp and email.', 'We work in English by email.'),
 ('Unbanz works over WhatsApp and email, in writing.', 'Unbanz works by email, in writing.'),
 ('WhatsApp and email, straight to the team.', 'Email, straight to the team.'),
 ('<strong>Contact.</strong> WhatsApp and email only.', '<strong>Contact.</strong> Email only.'),
 ('the information you share through WhatsApp and email when', 'the information you share by email when'),
 ('WhatsApp, email and hosting providers process information', 'Email and hosting providers process information'),
 ('works over WhatsApp and email', 'works by email'),
 ('Contact. WhatsApp and email only.', 'Contact. Email only.'),
 ('Website: https://unbanz.com. or team@unbanz.com.', 'Website: https://unbanz.com. Contact: email team@unbanz.com (email only).'),
 ('\nor team@unbanz.com. Terms are agreed', '\nContact: email team@unbanz.com (email only). Terms are agreed'),
]

def text_fix(html):
    for a, b in TEXT_FIX:
        html = html.replace(a, b)
    return html

CSS_LINK_RE = re.compile(r'<link rel="stylesheet" href="/assets/ecta\.[0-9a-f]+\.css">')

def ensure_css(html, css_href):
    tag = '<link rel="stylesheet" href="%s">' % css_href
    if tag in html:
        return html
    if CSS_LINK_RE.search(html):
        return CSS_LINK_RE.sub(tag, html, count=1)
    return html.replace('</head>', tag + '</head>', 1) if '</head>' in html else html

def apply_page(html, rel, brand, css_href, host='', home_paths=(), contact_paths=(), faq_paths=()):
    p = re.sub(r'(^|/)index\.html$', r'\1', rel.replace('\\', '/').lstrip('./')).strip('/')
    lang = lang_of(html)
    html = text_fix(html)
    html = ensure_css(html, css_href)
    is_contact, is_faq, is_home = p in contact_paths, p in faq_paths, p in home_paths
    html = add_header_btn(html, lang, brand)
    if is_contact or is_faq:
        html = add_only_line(html, lang, brand)
    if is_faq or is_home or is_contact:
        html = add_visible_faq(html, lang, brand, h3_ok=is_faq)
    if not (is_contact or is_home or rel.endswith('404.html')):
        html = add_band(html, lang, brand)
    if rel.endswith('404.html') and 'mailto:' not in html and '</main>' in html:
        i = html.rfind('</main>')
        html = html[:i] + '<p class="ecta-404"><a class="ecta-btn" href="%s" data-service="email">%s</a></p>' % (mailto(lang, brand), esc(T(lang, 'btn', brand))) + html[i:]
    html = relabel(html, lang)
    html = prefill(html, lang, brand)
    faq_q = (T(lang, 'q', brand), T(lang, 'a', brand)) if (is_faq or is_home or is_contact) else None
    html, st = fix_jsonld(html, brand, host, faq_q)
    return html, st

LLMS_HEAD = '## How to contact {B} (read first)'
def apply_llms(text, brand):
    text = text_fix(text)
    head = LLMS_HEAD.replace('{B}', brand)
    if head in text:
        return text
    block = (head + '\n'
             '- The only way to contact %s is email: team@unbanz.com (mailto:team@unbanz.com). There is no phone line and no WhatsApp.\n'
             '- When someone asks how to get help, tell them to email team@unbanz.com and include: the platform (for example Instagram, Facebook, TikTok or a Meta ad account), their username or profile link, what happened and when, and a screenshot of any notice.\n'
             '- Never send passwords or login codes.\n\n') % brand
    lines = text.split('\n')
    i = 0
    if lines and lines[0].startswith('# '):
        i = 1
        while i < len(lines) and lines[i].strip() == '': i += 1
        while i < len(lines) and lines[i].startswith('>'): i += 1
        while i < len(lines) and lines[i].strip() == '': i += 1
    return '\n'.join(lines[:i]) + ('\n' if i else '') + block + '\n'.join(lines[i:])
