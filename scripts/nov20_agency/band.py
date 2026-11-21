# Nov 20 2026: "Agencies & white-label" band on every page (above the footer), localized, linking the agency hub.
# Contact follows the 3-tier rule automatically: the email button is a normal mailto (hidden/removed for IN/PK/IR by
# the inline #ubz-noc guard); contact-policy.js adds a WhatsApp button only for US/CA/GB/NL/AE (IP + time zone).
# Not an <h2>, so page heading outlines are unchanged. Idempotent: replaces an existing band.
import os, re, urllib.parse
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
T = {
 'en': ('AGENCIES &amp; WHITE-LABEL', 'Run an agency? Offer account recovery under your own brand.', 'Instagram, Facebook, TikTok and X recoveries and username claims for your clients. You keep the client, we do the platform work quietly. Usually 7–14 days.', 'See the agency program', 'Email us', '/white-label-agency/', 'White-label agency enquiry', 'Hi Unbanz, I run an agency and want to offer account recovery under our brand.\n\nAgency name: \nWebsite: \nCases per month (approx.): \n\nThanks'),
 'fr': ('AGENCES &amp; MARQUE BLANCHE', 'Vous gérez une agence ? Proposez la récupération de comptes sous votre marque.', 'Récupération de comptes Instagram, Facebook et publicitaires, et noms d’utilisateur pour vos clients. Vous gardez le client, Unbanz s’occupe des plateformes en coulisses.', 'Voir le programme agences', 'Écrivez-nous', '/fr/white-label-agences/', 'Agence marque blanche - demande', 'Bonjour Unbanz, je gère une agence et je veux proposer la récupération de comptes sous notre marque.\n\nAgence : \nSite web : \nDossiers par mois (env.) : \n\nMerci'),
 'nl': ('BUREAUS &amp; WHITE-LABEL', 'Heb je een bureau? Bied accountherstel aan onder je eigen merk.', 'Herstel van Instagram-, Facebook- en advertentieaccounts en gebruikersnaamclaims voor je klanten. Jij houdt de klant, Unbanz doet het platformwerk achter de schermen.', 'Bekijk het bureauprogramma', 'Mail ons', '/nl/white-label-bureau/', 'White-label bureau - aanvraag', 'Hoi Unbanz, ik heb een bureau en wil accountherstel aanbieden onder ons merk.\n\nBureau: \nWebsite: \nZaken per maand (ong.): \n\nBedankt'),
 'es': ('AGENCIAS Y MARCA BLANCA', '¿Tienes una agencia? Ofrece recuperación de cuentas con tu propia marca.', 'Recuperación de cuentas de Instagram, Facebook y publicitarias, y nombres de usuario para tus clientes. Tú te quedas con el cliente; Unbanz hace el trabajo con la plataforma.', 'Ver el programa para agencias', 'Escríbenos', '/es/white-label-agencias/', 'Agencia marca blanca - consulta', 'Hola Unbanz, tengo una agencia y quiero ofrecer recuperación de cuentas con nuestra marca.\n\nAgencia: \nWeb: \nCasos al mes (aprox.): \n\nGracias'),
 'pt': ('AGÊNCIAS E WHITE-LABEL', 'Tem uma agência? Ofereça recuperação de contas com a sua marca.', 'Recuperação de contas do Instagram, Facebook e de anúncios, e nomes de usuário para seus clientes. Você fica com o cliente; a Unbanz faz o trabalho com a plataforma.', 'Ver o programa para agências', 'Envie um e-mail', '/pt-br/white-label-agencias/', 'Agência white-label - contato', 'Olá Unbanz, tenho uma agência e quero oferecer recuperação de contas com a nossa marca.\n\nAgência: \nSite: \nCasos por mês (aprox.): \n\nObrigado'),
 'de': ('AGENTUREN &amp; WHITE-LABEL', 'Du führst eine Agentur? Biete Kontowiederherstellung unter deiner Marke an.', 'Wiederherstellung von Instagram-, Facebook- und Werbekonten sowie Nutzernamen für deine Kunden. Du behältst den Kunden, Unbanz übernimmt die Plattformarbeit im Hintergrund.', 'Zum Agenturprogramm (EN)', 'E-Mail an uns', '/white-label-agency/', 'White-Label-Agentur - Anfrage', 'Hallo Unbanz, ich führe eine Agentur und möchte Kontowiederherstellung unter unserer Marke anbieten.\n\nAgentur: \nWebsite: \nFälle pro Monat (ca.): \n\nDanke'),
 'it': ('AGENZIE E WHITE-LABEL', 'Hai un’agenzia? Offri il recupero account con il tuo marchio.', 'Recupero di account Instagram, Facebook e pubblicitari e nomi utente per i tuoi clienti. Il cliente resta tuo, Unbanz lavora con la piattaforma dietro le quinte.', 'Programma agenzie (EN)', 'Scrivici', '/white-label-agency/', 'Agenzia white-label - richiesta', 'Ciao Unbanz, ho un’agenzia e voglio offrire il recupero account con il nostro marchio.\n\nAgenzia: \nSito: \nCasi al mese (circa): \n\nGrazie'),
 'tr': ('AJANSLAR VE WHITE-LABEL', 'Bir ajansınız mı var? Hesap kurtarmayı kendi markanızla sunun.', 'Müşterileriniz için Instagram, Facebook ve reklam hesabı kurtarma ile kullanıcı adı talepleri. Müşteri sizde kalır, platform işini Unbanz arka planda yapar.', 'Ajans programı (EN)', 'Bize yazın', '/white-label-agency/', 'White-label ajans - talep', 'Merhaba Unbanz, bir ajansım var ve hesap kurtarmayı kendi markamızla sunmak istiyorum.\n\nAjans: \nWeb sitesi: \nAylık vaka (yaklaşık): \n\nTeşekkürler'),
 'ar': ('الوكالات والعلامة البيضاء', 'تدير وكالة؟ قدّم استعادة الحسابات باسم علامتك التجارية.', 'استعادة حسابات إنستغرام وفيسبوك والإعلانات وأسماء المستخدمين لعملائك. يبقى العميل لك، وتتولى Unbanz العمل مع المنصة من خلف الكواليس.', 'برنامج الوكالات (بالإنجليزية)', 'راسلنا', '/white-label-agency/', 'White-label agency enquiry', 'Hi Unbanz, I run an agency and want to offer account recovery under our brand.\n\nAgency name: \nWebsite: \nCases per month (approx.): \n\nThanks'),
}
CSS = ('<style id="ag-band-css">.ag-band{margin:64px auto 8px}.ag-band .ag-in{position:relative;overflow:hidden;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:22px 40px;'
       'padding:36px 40px;border-radius:32px;background:radial-gradient(90% 160% at 100% 0%,#2a6489 0%,rgba(42,100,137,0) 60%),linear-gradient(135deg,#10344c 0%,#153d55 100%);color:#fff;box-sizing:border-box}'
       '.ag-band .ag-tx{flex:1 1 440px;min-width:0}.ag-band .ag-eye{margin:0 0 10px;font-size:12px;font-weight:600;letter-spacing:.12em;color:#9fc9e6}'
       '.ag-band .ag-h{margin:0 0 8px;font-size:clamp(22px,2.4vw,30px);font-weight:400;line-height:1.18;letter-spacing:-.035em;color:#fff}'
       '.ag-band .ag-p{margin:0;font-size:15px;line-height:1.55;color:#c9dfee;max-width:44em}.ag-band .ag-act{display:flex;flex-wrap:wrap;align-items:center;gap:10px}'
       '.ag-band .ag-act a{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:10px 22px;border-radius:999px;font-weight:600;font-size:15px;text-decoration:none;white-space:nowrap;gap:6px;transition:background .2s,box-shadow .2s}'
       '.ag-band .ag-more{background:#fff;color:#10344c}.ag-band .ag-more:hover{background:#e5eff6}.ag-band .ag-mail{background:transparent;color:#fff;box-shadow:inset 0 0 0 1px rgba(255,255,255,.38)}.ag-band .ag-mail:hover{box-shadow:inset 0 0 0 1px #fff}'
       '.ag-band .ag-res{flex-basis:100%;margin:2px 0 0;font-size:13px}.ag-band .ag-res a{color:#9fc9e6;text-decoration:underline;text-underline-offset:3px}'
       '.ag-ctx a{color:#2d719f;text-decoration:underline;text-underline-offset:3px}'
       '@media(max-width:650px){.ag-band{margin-top:44px}.ag-band .ag-in{padding:26px 22px;border-radius:24px}.ag-band .ag-act{width:100%}.ag-band .ag-act a{flex:1 1 100%}}</style>')
def band(lang):
    k = 'pt' if lang.lower().startswith('pt') else lang.lower()[:2]
    e, h, p, more, mail, href, subj, body = T.get(k, T['en'])
    m = 'mailto:team@unbanz.com?subject=' + urllib.parse.quote(subj) + '&amp;body=' + urllib.parse.quote(body)
    return ('<aside class="ag-band container" data-ag="nov20" aria-label="' + e + '"><div class="ag-in"><div class="ag-tx">'
            '<p class="ag-eye">' + e + '</p><p class="ag-h">' + h + '</p><p class="ag-p">' + p + '</p></div><div class="ag-act">'
            '<a class="ag-more" href="' + href + '">' + more + ' <span aria-hidden="true">→</span></a>'
            '<a class="ag-mail" data-service="white-label" href="' + m + '">' + mail + ' <span aria-hidden="true">↗︎</span></a></div>'
            + ('<p class="ag-res"><a href="/white-label-agency/guides/">Agency resources and guides</a></p>' if k == 'en' else '') + '</div></aside>' + CSS)
OLD = re.compile(r'<aside class="ag-band container" data-ag="nov20".*?</aside><style id="ag-band-css">.*?</style>', re.S)
n = 0
for r, ds, fs in os.walk(ROOT):
    ds[:] = [d for d in ds if d not in ('.git', 'node_modules', 'scripts', 'assets', 'users')]
    for f in fs:
        if not f.endswith('.html'): continue
        p = os.path.join(r, f); s = open(p, encoding='utf8').read()
        m = re.search(r'<html[^>]*\blang="([^"]+)"', s); lang = m.group(1) if m else 'en'
        b = band(lang)
        if os.path.relpath(p, ROOT) in ('white-label-agency/index.html', 'fr/white-label-agences/index.html', 'nl/white-label-bureau/index.html',
                                        'es/white-label-agencias/index.html', 'pt-br/white-label-agencias/index.html'): b = ''  # onboarding pages themselves: no band
        if OLD.search(s): t = OLD.sub(lambda _: b, s, count=1)
        elif not b: t = s
        elif '<footer' in s: i = s.find('<footer'); t = s[:i] + b + s[i:]
        elif '</main>' in s: i = s.rfind('</main>') + 7; t = s[:i] + b + s[i:]
        else: i = s.rfind('</body>'); t = s[:i] + b + s[i:]
        if t != s: open(p, 'w', encoding='utf8').write(t); n += 1
print('pages', n)
