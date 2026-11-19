"""Nov 19 2026 (b): pricing -> flat $1,000 (from $1,000 wording in EN), bank transfer instead of card/checkout,
6-month 're-ban cover' instead of guarantee, localized 'usually 7-14 days', no 'contacts at Meta' (all langs),
geo-neutral WhatsApp statements. Idempotent."""
import os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
changed = []

def files():
    for root, ds, fs in os.walk(ROOT):
        ds[:] = [d for d in ds if d not in ('.git', 'assets', 'scripts', 'node_modules', 'api', 'marketing', 'research', '.vercel', '.agents')]
        for f in fs:
            if f.endswith('.html') or f in ('llms.txt', 'llms-full.txt'):
                yield os.path.join(root, f)

AMT = r'(600|800|900|1[,.\u00a0\u202f ]?200|1[,.\u00a0\u202f ]?500)'
def fmt(sep):
    return '1' + sep + '000' if sep else None
def price_sub(s, lang):
    default_sep = {'en': ',', 'zh': ',', 'ar': ',', 'fr': '\u00a0', 'nl': '.', 'pt': '.', 'es': '.', 'de': '.', 'it': '.', 'tr': '.'}.get(lang, ',')
    def num(m_amt):
        a = m_amt
        sep = re.sub(r'\d', '', a)
        if sep == '' or len(a) == 3: sep = default_sep
        if sep == ' ': sep = '\u00a0' if lang == 'fr' else sep
        return '1' + sep + '000'
    # prefix forms: $800, US$ 800, $ 1,200
    s = re.sub(r'(?<![\w$])((?:US)?\$\s?)' + AMT + r'(?![\d])(?![,.]\d)', lambda m: m.group(1) + num(m.group(2)), s)
    # suffix forms: 800 $, 1.200 $, 1 200 $, 800 USD
    s = re.sub(r'(?<![\d.,\u00a0\u202f ])(?<!\d )' + AMT + r'(\s?)(\$|USD)(?!\w)', lambda m: num(m.group(1)) + m.group(2) + m.group(3), s)
    # JSON-LD offer prices
    s = re.sub(r'"price":(\s?)"(600|800|900|1200|1500)"', r'"price":\1"1000"', s)
    return s

EN_PRICE = [
 (r'\b[Ff]or (?:a )?(?:fixed |flat )(?:fee of )?\$1,000', 'from $1,000'),
 (r'\b(?:a |the )?(?:fixed|flat) (?:fee of )?\$1,000', 'from $1,000'),
 (r'\bFlat \$1,000', 'From $1,000'),
 (r'\bFixed \$1,000', 'From $1,000'),
 (r'\bfor \$1,000\b', 'from $1,000'),
 (r'\bcosts? \$1,000\b', 'costs from $1,000'),
 (r'\bfee for this service is \$1,000', 'fee for this service is from $1,000'),
 (r'separate scope at \$1,000', 'separate scope, priced from $1,000'),
 (r'from from', 'from'),
]

PAY = [
 # EN
 (r'Can I pay by card\?', 'How do I pay?'),
 (r'Yes\. Card is how you pay\. Card gives you your bank’s buyer protection\. ', 'Payment is by bank transfer. '),
 (r' ?Paying by card (?:also )?keeps your bank’s buyer protection[^.]*\.', ''),
 (r'Card gives you your bank’s buyer protection\. ?', ''),
 (r'You pay upfront by card through a secure checkout link we send you\.', 'You pay by bank transfer; we send the details in writing.'),
 (r'the full fee is paid upfront through a secure card checkout link', 'the full fee is paid upfront by bank transfer'),
 (r'(?:through|via|with) a secure (?:card )?checkout link(?: we send you)?', 'by bank transfer'),
 (r'secure (?:card )?checkout link', 'bank transfer details'),
 (r'Card payment accepted\.', 'Payment is by bank transfer.'),
 (r'Unbanz takes card payment\.', 'Unbanz takes payment by bank transfer.'),
 (r'[Pp]aid upfront by card', lambda m: ('P' if m.group(0)[0] == 'P' else 'p') + 'aid by bank transfer'),
 (r'[Pp]ayment is upfront by card', lambda m: ('P' if m.group(0)[0] == 'P' else 'p') + 'ayment is upfront by bank transfer'),
 (r'[Pp]ay upfront by card', lambda m: ('P' if m.group(0)[0] == 'P' else 'p') + 'ay upfront by bank transfer'),
 (r'upfront by card', 'upfront by bank transfer'),
 (r'Payment is by card', 'Payment is by bank transfer'),
 (r'\bBy card\.', 'By bank transfer.'),
 (r'\b([Pp])ay(ing)? by card', r'\1ay\2 by bank transfer'),
 (r'\bby card\b', 'by bank transfer'),
 (r'\bcard payment\b', 'bank transfer'),
 (r'"paymentAccepted":(\s?)"Credit Card"', r'"paymentAccepted":\1"Bank transfer"'),
 # DE
 (r'im Voraus per Karte bezahlt', 'im Voraus per Banküberweisung bezahlt'),
 (r'im Voraus über einen sicheren Kartenlink', 'im Voraus per Banküberweisung'),
 (r'einen sicheren Zahlungslink für deine Karte', 'die Daten für die Banküberweisung'),
 (r'per Karte', 'per Banküberweisung'),
 # FR
 (r'payés d’avance par carte', 'payés d’avance par virement bancaire'),
 (r'payé d’avance par carte', 'payé d’avance par virement bancaire'),
 (r'(?<!-)par carte(?! cadeau|-cadeau)', 'par virement bancaire'),
 (r'un lien de paiement sécurisé par carte', 'les coordonnées pour le virement bancaire'),
 # ES
 (r'pagados por adelantado con tarjeta', 'pagados por adelantado por transferencia bancaria'),
 (r'[Pp]ago por adelantado con tarjeta', lambda m: m.group(0)[0] + 'ago por adelantado por transferencia bancaria'),
 (r'con tarjeta(?!s)', 'por transferencia bancaria'),
 (r'un enlace de pago seguro (?:con|para la) tarjeta', 'los datos para la transferencia bancaria'),
 # PT
 (r'pagos antecipadamente no cartão', 'pagos antecipadamente por transferência bancária'),
 (r'pagamento antecipado no cartão', 'pagamento antecipado por transferência bancária'),
 (r'enviamos um link de pagamento seguro no cartão', 'enviamos os dados para a transferência bancária'),
 (r'(?:no|com|por) cartão(?![-\w])', 'por transferência bancária'),
 # IT
 (r'pagat([oi]) in anticipo con carta', r'pagat\1 in anticipo con bonifico bancario'),
 (r'Paghi in anticipo con carta tramite un link sicuro che ti inviamo\.', 'Paghi in anticipo con bonifico bancario; ti inviamo i dati per iscritto.'),
 (r'ti inviamo un link di pagamento sicuro per la carta', 'ti inviamo i dati per il bonifico bancario'),
 (r'con carta(?! regalo)\b', 'con bonifico bancario'),
 # NL
 (r'Vooraf betalen per kaart', 'Vooraf betalen per bankoverschrijving'),
 (r'vooraf per kaart', 'vooraf per bankoverschrijving'),
 (r'sturen we een veilige betaallink voor je kaart', 'sturen we de gegevens voor de bankoverschrijving'),
 (r'per kaart(?!nummer)', 'per bankoverschrijving'),
 # TR
 (r'kartla peşin ödenir', 'banka havalesiyle peşin ödenir'),
 (r'kart için güvenli bir ödeme bağlantısı göndeririz', 'banka havalesi bilgilerini göndeririz'),
 (r'\bkartla\b', 'banka havalesiyle'),
 # AR
 (r'مقدّماً بالبطاقة', 'مقدّماً بالتحويل البنكي'),
 (r'بالبطاقة', 'بالتحويل البنكي'),
]

GUAR = [
 # 6-month cover
 (r'6-month guarantee after we unban', '6-month re-ban cover after we unban'),
 (r'6-month guarantee(?=:)', '6-month re-ban cover'),
 (r'6-month guarantee', '6-month re-ban cover'),
 (r'6 Monate Garantie nach der Entsperrung', '6 Monate Schutz bei erneuter Sperre'),
 (r'6 Monate Garantie', '6 Monate Schutz bei erneuter Sperre'),
 (r'Garantía de 6 meses tras el desbaneo', 'Cobertura de 6 meses si vuelve a ser baneada'),
 (r'Garantía de 6 meses', 'Cobertura de 6 meses si vuelve a ser baneada'),
 (r'Garantie de 6 mois après le déblocage', 'Couverture de 6 mois en cas de nouveau bannissement'),
 (r'Garantie de 6 mois', 'Couverture de 6 mois en cas de nouveau bannissement'),
 (r'Garantia de 6 meses após o desbanimento', 'Cobertura de 6 meses se a conta for banida de novo'),
 (r'Garantia de 6 meses', 'Cobertura de 6 meses se a conta for banida de novo'),
 (r'Garanzia di 6 mesi[^<"]*?(?=[<".·])', 'Copertura di 6 mesi in caso di nuovo ban'),
 (r'6 maanden garantie na het herstel', '6 maanden dekking bij een nieuwe ban'),
 (r'6 maanden garantie', '6 maanden dekking bij een nieuwe ban'),
 (r'Açıldıktan sonra 6 ay garanti', 'Açıldıktan sonra 6 ay yeniden ban koruması'),
 (r'6 ay garanti', '6 ay yeniden ban koruması'),
 (r'ضمان 6 أشهر بعد فك الحظر', 'تغطية 6 أشهر إذا حُظر الحساب مجددًا'),
 (r'ضمان 6 أشهر', 'تغطية 6 أشهر إذا حُظر الحساب مجددًا'),
 # timing
 (r'Garantiert in 7–14 Tagen', 'Meist 7–14 Tage'),
 (r'Garantizado en 7–14 días', 'Normalmente 7–14 días'),
 (r'Garanti en 7 à 14 jours', 'En général 7 à 14 jours'),
 (r'Garantido em 7–14 dias', 'Normalmente 7–14 dias'),
 (r'Garantito in 7–14 giorni', 'Di solito 7–14 giorni'),
 (r'7–14 günde garantili', 'Genellikle 7–14 gün'),
 (r'مضمون خلال 7–14 يومًا', 'عادةً خلال 7–14 يومًا'),
]

META = [
 # EN FAQ with implied contacts
 (r'Can someone with contacts at Meta help restore my Instagram account\?', 'Can an outside service restore my Instagram account?'),
 (r'Can someone with contacts at Meta help\?', 'Can an outside service help?'),
 (r'It can help, but nobody can guarantee a decision, because Meta makes it\.', 'An independent service can prepare and handle the appeal, but nobody can guarantee a decision, because Meta makes it. Unbanz has no special access to Meta.'),
 # ES
 (r', y en casos de Facebook e Instagram trabajamos a través de nuestros contactos en Meta\.', '.'),
 (r' En casos de Facebook e Instagram trabajamos a través de nuestros contactos en Meta, con pago por adelantado', ' Pago por adelantado'),
 (r' En casos de Facebook e Instagram trabajamos a través de nuestros contactos en Meta\.', ''),
 (r'; en casos de Facebook e Instagram trabaja a través de sus contactos en Meta\.', '.'),
 (r'Unbanz trabaja a través de sus contactos en Meta en casos de Facebook e Instagram, sin afiliación oficial y sin garantizar resultados\.', 'Unbanz es independiente: no está afiliada a Meta, no tiene acceso especial y no garantiza resultados.'),
 (r'¿Alguien tiene de verdad un contacto en Meta\?', '¿Alguien tiene acceso especial a Meta?'),
 # PT
 (r', e em casos de Facebook e Instagram trabalhamos por meio dos nossos contatos na Meta\.', '.'),
 (r' Em casos de Facebook e Instagram trabalhamos por meio dos nossos contatos na Meta, com pagamento adiantado', ' Pagamento adiantado'),
 (r' Em casos de Facebook e Instagram trabalhamos por meio dos nossos contatos na Meta\.', ''),
 (r'; em casos de Facebook e Instagram trabalha por meio dos seus contatos na Meta\.', '.'),
 (r'A Unbanz trabalha por meio dos seus contatos na Meta em casos de Facebook e Instagram, sem vínculo oficial e sem garantir resultados\.', 'A Unbanz é independente: não tem vínculo com a Meta, não tem acesso especial e não garante resultados.'),
 (r'Alguém tem mesmo um contato na Meta\?', 'Alguém tem acesso especial à Meta?'),
 # FR
 (r', et pour les cas Facebook et Instagram nous passons par nos contacts chez Meta\.', '.'),
 (r'Pour les cas Facebook et Instagram, nous passons par nos contacts chez Meta, sans affiliation officielle avec Meta et sans garantie de résultat\.', 'Unbanz est indépendant : aucune affiliation avec Meta, aucun accès privilégié et aucune garantie de résultat.'),
 (r'Pour les cas Facebook et Instagram, nous passons par nos contacts chez Meta, sans affiliation officielle\.', 'Unbanz est indépendant, sans affiliation avec Meta ni accès privilégié.'),
 (r' et, pour les cas Facebook et Instagram, par nos contacts chez Meta', ''),
 (r'Unbanz a-t-il un contact chez Meta \?', 'Unbanz a-t-il un accès privilégié à Meta ?'),
]

WA = [
 (r'Email is our only contact channel: team@unbanz\.com\. We don’t use phone or WhatsApp\.', 'The fastest way to reach us is email at team@unbanz.com; in some countries you’ll also see a WhatsApp button on this page.'),
 (r'We don’t use phone or WhatsApp\.', 'In some countries you’ll also see a WhatsApp button on this page.'),
 (r'There is no phone line and no WhatsApp\.', 'There is no phone line; in some countries you’ll also see a WhatsApp button on this page.'),
 (r'Não atendemos ligações nem mensagens de WhatsApp, e nunca precisamos da sua senha\.', 'O jeito mais rápido é o e-mail; em alguns países você também verá um botão de WhatsApp nesta página. Nunca precisamos da sua senha.'),
 (r'O e-mail é nosso único canal de contato: team@unbanz\.com\. Não usamos telefone nem WhatsApp\.', 'O jeito mais rápido de falar conosco é pelo e-mail team@unbanz.com; em alguns países você também verá um botão de WhatsApp nesta página.'),
 (r'Não usamos telefone nem WhatsApp\.', 'Em alguns países você também verá um botão de WhatsApp nesta página.'),
 (r'Um único site \(unbanz\.com\), um e-mail \(team@unbanz\.com\) e um número de WhatsApp\.', 'Um único site (unbanz.com) e um e-mail (team@unbanz.com).'),
 (r'Nous ne prenons ni appels ni messages WhatsApp, et nous n’avons jamais besoin de votre mot de passe\.', 'Le plus rapide est l’e-mail ; dans certains pays, vous verrez aussi un bouton WhatsApp sur cette page. Nous n’avons jamais besoin de votre mot de passe.'),
 (r'Nous n’utilisons ni téléphone ni WhatsApp\.', 'Dans certains pays, vous verrez aussi un bouton WhatsApp sur cette page.'),
 (r'un site, un e-mail, un numéro WhatsApp, des témoignages', 'un site, un e-mail, des témoignages'),
 (r'un seul site, une seule adresse e-mail et un seul numéro WhatsApp\.', 'un seul site et une seule adresse e-mail.'),
 (r'Un seul numéro WhatsApp', 'Une seule adresse e-mail'),
 (r'No atendemos llamadas ni mensajes de WhatsApp, y nunca necesitamos tu contraseña\.', 'Lo más rápido es el correo; en algunos países también verás un botón de WhatsApp en esta página. Nunca necesitamos tu contraseña.'),
 (r'No usamos teléfono ni WhatsApp\.', 'En algunos países también verás un botón de WhatsApp en esta página.'),
 (r'Un solo sitio web \(unbanz\.com\), un correo \(team@unbanz\.com\) y un número de WhatsApp\.', 'Un solo sitio web (unbanz.com) y un correo (team@unbanz.com).'),
 (r'We nemen geen telefoontjes of WhatsApp-berichten aan en we hebben nooit je wachtwoord nodig\.', 'Mailen is het snelst; in sommige landen zie je op deze pagina ook een WhatsApp-knop. We hebben nooit je wachtwoord nodig.'),
 (r'We gebruiken geen telefoon of WhatsApp\.', 'In sommige landen zie je op deze pagina ook een WhatsApp-knop.'),
 (r'Wir nehmen keine Anrufe oder WhatsApp-Nachrichten an und brauchen nie Ihr Passwort\.', 'Am schnellsten geht es per E-Mail; in einigen Ländern sehen Sie auf dieser Seite auch einen WhatsApp-Button. Wir brauchen nie Ihr Passwort.'),
 (r'Telefon araması veya WhatsApp mesajı kabul etmiyoruz ve şifrenize asla ihtiyacımız yoktur\.', 'En hızlı yol e-postadır; bazı ülkelerde bu sayfada bir WhatsApp düğmesi de görürsünüz. Şifrenize asla ihtiyacımız yoktur.'),
]

EXTRA = [
 (r'Card payment</td>', 'Bank transfer</td>'),
 (r'Kartla peşin ödeme', 'Banka havalesiyle peşin ödeme'),
 (r'Pour les cas Facebook et Instagram, Unbanz passe par ses contacts chez Meta, sans affiliation officielle\.', 'Unbanz est indépendant, sans affiliation avec Meta ni accès privilégié.'),
 (r'Yes\. (Most cases are done within 7–14 days)', r'Not on the outcome, because the platform decides. \1'),
]
RULES = [(re.compile(a), b) for a, b in PAY + GUAR + META + WA + EXTRA]
ENP = [(re.compile(a), b) for a, b in EN_PRICE]

def main():
    for p in files():
        s = open(p, encoding='utf-8').read(); old = s
        m = re.search(r'<html[^>]*\blang="([a-zA-Z]{2})', s)
        lang = m.group(1).lower() if m else 'en'
        s = price_sub(s, lang)
        for rx, rep in ENP: s = rx.sub(rep, s)
        for rx, rep in RULES: s = rx.sub(rep, s)
        if s != old:
            open(p, 'w', encoding='utf-8').write(s); changed.append(os.path.relpath(p, ROOT))
    print('changed', len(changed))

if __name__ == '__main__':
    main()
