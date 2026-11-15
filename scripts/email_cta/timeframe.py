"""Recovery timeframe normaliser (Nov 15 2026 rule: guaranteed 7–14 days,
100% refund if not reinstated within 14 days). Idempotent. Touches only the
old service-time ranges (3–7 days and translations) and the refund clause that
sits right next to the timeframe. Never touches prices or other numbers."""
import re

D = '–'
# 1) the range itself, every language form used on the sites
NUM = [
    (re.compile(r'\b3\s?[–-]\s?7(\s?)(days|jours|dagen|dias|días|giorni|gün|Tagen|Tage|天)'), r'7–14\1\2'),
    (re.compile(r'\b3 à 7 jours'), '7 à 14 jours'),
    (re.compile(r'\b3 a 7 (dias|días)'), r'7 a 14 \1'),
    (re.compile(r'\b3 to 7 days'), '7 to 14 days'),
    (re.compile(r'\b3\s?[–-]\s?7 أيام'), '7–14 يومًا'),
    (re.compile(r'\b3 إلى 7 أيام'), '7 إلى 14 يومًا'),
    (re.compile(r'(usual estimate is |Usual estimate is |With Unbanz the usual estimate is )3[–-]14 days'), r'\g<1>7–14 days'),
]
EN_NEW = '100% refund if not reinstated within 14 days'
SEP = r'(\s·\s|</li>\s*<li>|\s\|\s)'
# 2) refund clause next to the timeframe
REF = [
    # one sentence that used to state the refund twice: keep it once
    (re.compile(r'100% refund if (?:it|the case) fails\. (Guaranteed 7–14 days from the day (?:we start|work starts)), with a 100% refund if it fails\.'), EN_NEW + r'. \g<1>.'),
    # trust lines / mini lines, per language: "<timeframe> <sep> <old refund>"
    (re.compile(r'(Guaranteed 7–14 days)' + SEP + r'100% refund if it fails'), r'\g<1>\g<2>' + EN_NEW),
    (re.compile(r'(Garanti en 7 à 14 jours)' + SEP + r'Remboursement à 100 % en cas d’échec'), r'\g<1>\g<2>Remboursement à 100 % si le compte n’est pas rétabli sous 14 jours'),
    (re.compile(r'(Gegarandeerd binnen 7–14 dagen)' + SEP + r'100% terugbetaling als het mislukt'), r'\g<1>\g<2>100% terugbetaling als het niet binnen 14 dagen is hersteld'),
    (re.compile(r'(Garantido em 7–14 dias)' + SEP + r'Reembolso de 100% se não der certo'), r'\g<1>\g<2>Reembolso de 100% se a conta não for restabelecida em até 14 dias'),
    (re.compile(r'(Garantizado en 7–14 días)' + SEP + r'Reembolso del 100 % si no se consigue'), r'\g<1>\g<2>Reembolso del 100 % si la cuenta no se restablece en 14 días'),
    (re.compile(r'(Garantiert in 7–14 Tagen)' + SEP + r'100 % Rückerstattung, wenn es scheitert'), r'\g<1>\g<2>100 % Rückerstattung, wenn nicht binnen 14 Tagen wiederhergestellt'),
    (re.compile(r'(Garantito in 7–14 giorni)' + SEP + r'Rimborso del 100% se non riesce'), r'\g<1>\g<2>Rimborso del 100% se non viene ripristinato entro 14 giorni'),
    (re.compile(r'(7–14 günde garantili)' + SEP + r'Başarısız olursa %100 iade'), r'\g<1>\g<2>14 gün içinde geri açılmazsa %100 iade'),
    (re.compile(r'(مضمون خلال 7–14 يومًا)' + SEP + r'استرداد 100% إذا فشلت الحالة'), r'\g<1>\g<2>استرداد 100% إذا لم يُستعَد الحساب خلال 14 يومًا'),
    # English sentences
    (re.compile(r'([Gg]uaranteed (?:within )?7–14 days[^.<>"|]{0,45}?,\s*(?:with a |and a )?)100% refund if (?:it|the case) fails'), r'\g<1>' + EN_NEW),
    (re.compile(r'100% refund if the case fails\. Guaranteed 7–14 days\.'), 'Guaranteed 7–14 days. ' + EN_NEW + '.'),
    (re.compile(r'100% refund if (?:it|the case) fails([.;,]\s+(?:No passwords\.\s+)?(?:It is )?[Gg]uaranteed (?:within )?7–14 days)'), EN_NEW + r'\g<1>'),
    (re.compile(r'100% refund if a case fails, guaranteed 7–14 days'), '100% refund if a case is not reinstated within 14 days, guaranteed 7–14 days'),
]

def fix(t):
    if not t:
        return t
    for rx, rep in NUM:
        t = rx.sub(rep, t)
    if '14' in t:
        for rx, rep in REF:
            t = rx.sub(rep, t)
    return t

OLD = re.compile(r'\b3\s?[–-]\s?7\s?(?:days|jours|dagen|dias|días|giorni|gün|Tagen|Tage|天|أيام)|\b3 à 7 jours|\b3 a 7 d[ií]as|\b3 إلى 7 أيام|\b3 to 7 days|\b3[–-]14 days')
