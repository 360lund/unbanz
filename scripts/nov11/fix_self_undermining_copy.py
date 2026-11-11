#!/usr/bin/env python3
"""Nov 11: remove copy that undermines Unbanz as a paid recovery service.
Text-level replacements, tolerant of HTML entities / JSON escaping / nbsp."""
import os, re, sys

CEN = "For Facebook and Instagram cases we work through our contacts at Meta"
PAY = "payment is upfront, with a 100% refund if the case fails"

R = [
# ---------- EN: the screenshot block ----------
("Don’t pay anyone who claims a special way in.</strong> Nobody outside Meta can reverse a final decision, and “recovery” offers aimed at disabled accounts are a common scam.",
 "Don’t trust strangers who message you first.</strong> Unbanz never cold-messages people. If someone reaches out unprompted after you post about a ban, ignore them."),
("Don’t pay anyone who claims a special way in. Nobody outside Meta can reverse a final decision, and “recovery” offers aimed at disabled accounts are a common scam.",
 "Don’t trust strangers who message you first. Unbanz never cold-messages people. If someone reaches out unprompted after you post about a ban, ignore them."),
("to anyone offering to “try again” for you.", "to anyone. Unbanz never asks for them, and nobody needs them to help you."),
("Where an outside helper fits", "How Unbanz can help"),
("When the self-service route has ended, there is not much a helper can honestly do, and anyone promising a result is not being straight with you. What we can do is look at the facts with you: whether the notice really is final, whether the hacked-account route applies, which Pages and ad accounts need protecting, and what to gather. We handle the process through Meta’s official channels only. Meta makes the final decision, and we tell you plainly if we don’t think it is doable.",
 "When the self-service route has ended, this is where Unbanz comes in. We are an independent, paid recovery service, not affiliated with Meta. We look at the facts with you: whether the notice really is final, whether the hacked-account route applies, which Pages and ad accounts need protecting, and what to gather. Then we work the case through Meta’s official channels and our contacts at Meta. Payment is upfront, with a 100% refund if the case fails. Most cases take 3–7 days, though that is not guaranteed, and Meta makes the final decision. If we don’t think it is doable, we tell you plainly before you pay."),
# ---------- EN: shared "Staying safe" block ----------
("or claims to have a special way in, walk away. Unbanz never asks for logins and has no special access. We use the same official routes that are open to you.",
 "or wants to be paid in gift cards, walk away. Unbanz never asks for logins. We are an independent paid service, not affiliated with Meta: " + PAY + ". " + CEN + ", and Meta makes the final decision."),
("or claims to have a special way in, walk away. Unbanz never asks for logins and doesn’t claim any special access. We use the same official routes that are open to you, we just know them well and do the legwork properly.",
 "or wants to be paid in gift cards, walk away. Unbanz never asks for logins. We are an independent paid service, not affiliated with Meta: " + PAY + ". " + CEN + ", and Meta makes the final decision."),
("Unbanz never asks for logins and has no special access. We use the same official routes that are open to you.",
 "Unbanz never asks for logins. We are an independent paid service, not affiliated with Meta: " + PAY + ". " + CEN + ", and Meta makes the final decision."),
("We use the same official routes that are open to you.", CEN + ", and Meta makes the final decision."),
# ---------- EN: other lines ----------
("Don’t pay or message anyone from a DM who says they can “open” your account.",
 "Ignore strangers who DM you first saying they can “open” your account. Unbanz never cold-messages people and never asks for your password."),
("Never pay anyone who says they have inside access.",
 "Never give your password or login codes to anyone. Unbanz never asks for them."),
("Never pay anyone for a “private” or “direct” appeal link. There is none.",
 "There is no “private” or “direct” appeal link. Use the official links on this page, or send us your case."),
("4) It does not claim insider access or a special contact at Meta.",
 "4) It is clear about how it works and never promises a guaranteed result."),
("No. Unbanz is independent and has no special access at Meta. Every claim goes through the same public reports and processes Instagram offers everyone. What you pay for is knowing which route fits your handle and filing it properly.",
 "No. Unbanz is an independent service, not affiliated with Meta. We work through the standard reports and processes and, for Instagram and Facebook cases, our contacts at Meta. What you pay for is knowing which route fits your case and getting it handled properly, with payment upfront and a 100% refund if it fails."),
("Do not pay anyone who contacts you offering to get it back.",
 "Ignore strangers who contact you offering to get it back, and never give them your password or codes."),
("Do not pay anyone in a DM who says they can open your account and do not share your password or codes with anyone.",
 "Ignore strangers in your DMs who say they can open your account, and do not share your password or codes with anyone."),
("Independent service. Not affiliated with Meta. No special access at Meta.",
 "Independent paid service. Not affiliated with Meta. Works through contacts at Meta for Facebook and Instagram cases. Payment upfront, 100% refund if a case fails."),
("Unbanz is independent and has no special access at Meta. Claims go through the same public reports and processes Instagram offers everyone.",
 "Unbanz is independent and not affiliated with Meta. For Instagram and Facebook cases it works through contacts at Meta alongside the standard reports and processes."),
("Do not pay anyone who says they can reverse a final decision through a contact at Meta.",
 "Do not share your password or codes with anyone who says they can reverse a decision for you. A real service never needs them."),
("Avoid anyone who asks for a client’s password, offers to “buy back” an account or talks about insiders.",
 "Avoid anyone who asks for a client’s password or offers to “buy back” an account."),
("A request for the client’s password or login codes, talk of insiders at Meta, buying or selling accounts, and any promise of a sure result.",
 "A request for the client’s password or login codes, buying or selling accounts, and any promise of a sure result."),
(" If someone tells you chat staff can be paid to switch an account back on, that is a scam.", ""),
("No direct line is open to the public, and we do not have one. We use the same official routes.",
 "No direct line is open to the public. " + CEN + "."),
("Do not pay anyone in your DMs who says they know someone at Meta. Nobody can buy a reinstatement.",
 "Ignore strangers in your DMs who ask for your password or codes. Nobody can guarantee a reinstatement."),
("Unbanz never asks for passwords and only uses the platform’s own routes.",
 "Unbanz never asks for passwords and never cold-messages clients."),
("Never share login codes, never pay a stranger who offers to get the account back and never hand over a password.",
 "Never share login codes or hand over a password, and ignore strangers who message first offering to get the account back."),
("and do not pay anyone in your DMs.", "and ignore strangers in your DMs who ask for your login."),
("Do not pay anyone claiming to be a Meta employee.", "Do not share your login with anyone in your DMs claiming to be a Meta employee."),
("No. Anyone offering a “Meta insider” or inside access is a red flag. Every claim we handle goes through the platform’s own reports and processes, and Instagram makes the final call.",
 "No. Unbanz is independent and not affiliated with Meta. We handle claims through the platform’s reports and processes and, for Instagram and Facebook cases, our contacts at Meta. Instagram makes the final call."),
("A “private” Meta appeal link or an insider who can unban for a fee.", "A “private” Meta appeal link."),
("Work through the platform’s own processes, not “insider” claims.", "Work with a service that is clear about price, refunds and process."),
("“Meta insider” or “TikTok employee” claims.", "Requests for your password or login codes."),
("Don’t pay a “hacker” or “recovery expert” who contacts you, or who asks for your password.",
 "Ignore “hackers” who contact you first, and never give anyone your password."),
("Don’t pay a “hacker” or “recovery expert” who contacts you.",
 "Ignore “hackers” who contact you first, and never give anyone your password."),
("Anyone who claims to work at Meta or know an insider.", "Anyone who contacts you first and asks for your password or codes."),
("and do not pay anyone who claims a “private TikTok link”.", "and ignore anyone selling a “private TikTok link”."),
("Paying “TikTok insiders”.", "Sharing your password or codes with strangers."),
("Do not pay anyone for a “private” appeal link. There is none.", "There is no “private” appeal link."),
("Do not pay for a “private Meta link”. There is none.", "There is no “private Meta link”."),
("Do not pay anyone who claims they can restore a badge through a contact.",
 "Be careful with strangers who offer to restore a badge and ask for your login."),
("Don’t pay anyone who claims they can “unlock” a deceased person’s account.",
 "Never share a deceased person’s password or codes with anyone offering to “unlock” the account."),
("Short answer: any helper who asks for your password, a code, an upfront payment in gift cards or crypto, or claims to have special access to your account is a scam. Recovery only happens through official routes.",
 "Short answer: any helper who asks for your password or a login code, or wants payment in gift cards, is a scam. A real service like Unbanz never needs your login, gives you the price and refund terms in writing, and refunds 100% if the case fails."),
("Don’t pay to “unlock” a recovery.", "Don’t pay a stranger an extra “release” or “unlock” fee."),
("Don’t pay anyone who says they have a secret appeal route.", "Don’t share your login with anyone who says they have a secret appeal route."),
("No. Nobody outside Meta can. We can help you work out which route applies and prepare a clean submission through the official process.",
 "No. Only Meta controls its forms. What we can do is take on the case: we work out which route applies and handle it through the official process and our contacts at Meta, with payment upfront and a 100% refund if it fails."),
("Don’t pay for a “code workaround.” No outside party can change what Facebook asks for.",
 "Don’t trust a “code workaround” that needs your password or codes."),
("Don’t pay a “2FA unlock” service that asks for your password or a code.", "Avoid any “2FA unlock” offer that asks for your password or a code."),
("No one outside Meta can edit Account Status.", "Meta makes the final decision on Account Status."),
("Don’t pay anyone who claims to be inside Instagram and promises to push the appeal. No outside party can.",
 "Don’t give your login to anyone who claims to work inside Instagram."),
("Don’t pay anyone who offers access to a deceased person’s account.", "Be wary of anyone who offers access to a deceased person’s account."),
("Don’t pay anyone who promises to “recover” the portfolio.", "Don’t trust anyone who guarantees to “recover” the portfolio or asks for admin logins."),
("Don’t pay a “Page recovery agent” who contacts you or hands you a Telegram contact. It’s a known scam pattern.",
 "Ignore “Page recovery agents” who message you first or push you to Telegram."),
("Paying anyone who asks for your password or codes. A real service never needs your password. Up-front promises from strangers are a common scam.",
 "Sharing your password or codes with anyone. A real service never needs your password."),
("Don’t pay a “hacker recovery” service that contacts you first, or a person who offers to hack the hacker back.",
 "Ignore anyone who contacts you first offering “hacker recovery”, or offers to hack the hacker back."),
("Paying a stranger who says they know someone at Meta. No one outside Meta can change a decision.",
 "Giving your password or codes to a stranger who messages you first."),
("Can I pay someone at Meta to restore my Instagram account?", "Can someone with contacts at Meta help restore my Instagram account?"),
("No. Anyone offering a Meta insider or a private channel is not offering something real. Decisions are made by Meta through its official process.",
 "It can help, but nobody can guarantee a decision, because Meta makes it. Unbanz is independent and not affiliated with Meta. For Facebook and Instagram cases we work through our contacts at Meta, with payment upfront and a 100% refund if it fails."),
("Do not send the same appeal over and over, pay anyone who claims to reach Instagram staff, or share your password.",
 "Do not send the same appeal over and over, or share your password with anyone."),
("Don’t pay anyone who says they can reach “Instagram staff” or open a hidden form.",
 "Don’t share your login with anyone who says they can open a hidden form."),
("Can anyone outside Meta lift a restriction?", "Can Unbanz help lift a restriction?"),
("Do not pay for a ban remover; they are scams.", "Avoid “ban remover” tools that ask for your login or to change your phone."),
("Do not tell a client you have a contact at Meta. Do not promise a result. Do not take a client’s password. These three rules protect your reputation more than any marketing. Unbanz works the same way: official routes, honest answers, no insiders.",
 "Do not promise a result. Do not take a client’s password. These rules protect your reputation more than any marketing. Unbanz works the same way: honest answers, no guarantees, no passwords."),
("Unbanz never asks for passwords or codes, uses only official routes, does not buy",
 "Unbanz never asks for passwords or codes, does not buy"),
("No. Unbanz has no special access. We use the same official routes available to you.",
 "Unbanz is independent and not affiliated with Meta. " + CEN + ", alongside the official routes. Payment is upfront with a 100% refund if it fails."),
("Do not pay anyone offering a private restore.", "Do not give your login to anyone offering a private restore."),
("Claims of inside access at Meta. Nobody outside Meta can switch an account back on. Unbanz is independent and works only through Meta's own processes.",
 "Guaranteed results. Nobody can promise Meta will switch an account back on. Unbanz is independent, never guarantees an outcome, and refunds 100% if a case fails."),
("Claims of inside access at Meta. Nobody outside Meta can switch an account back on. Unbanz is independent and works only through Meta’s own processes.",
 "Guaranteed results. Nobody can promise Meta will switch an account back on. Unbanz is independent, never guarantees an outcome, and refunds 100% if a case fails."),
("We prepare your appeal or report properly and handle it through Meta’s official channels, then follow up",
 "We prepare your appeal or report properly and handle it through Meta’s official channels and our contacts at Meta, then follow up"),
("We prepare your appeal properly and handle it through Meta’s official channels, then follow up",
 "We prepare your appeal properly and handle it through Meta’s official channels and our contacts at Meta, then follow up"),
("We prepare appeals and reports and handle them through Meta's official channels.",
 "We prepare appeals and reports and handle them through Meta's official channels and our contacts at Meta."),
("We prepare appeals and reports and handle them through Meta’s official channels.",
 "We prepare appeals and reports and handle them through Meta’s official channels and our contacts at Meta."),
("We prepare your appeal and handle it through Meta’s official channels.",
 "We prepare your appeal and handle it through Meta’s official channels and our contacts at Meta."),

# ---------- FR ----------
("ou prétend connaître quelqu’un chez Meta, passez votre chemin. Unbanz ne demande jamais vos identifiants et ne prétend à aucun accès spécial : nous passons par les mêmes voies officielles que vous.",
 "ou veut être payé en cartes cadeaux, passez votre chemin. Unbanz ne demande jamais vos identifiants. Nous sommes un service payant indépendant, sans affiliation avec Meta : paiement d’avance, remboursé à 100 % si le dossier échoue, et pour les cas Facebook et Instagram nous passons par nos contacts chez Meta."),
("ou dit avoir un contact chez Meta, ne donnez pas suite. Unbanz ne demande jamais vos identifiants et n’a aucun accès particulier : nous utilisons les mêmes procédures officielles que vous.",
 "ou veut être payé en cartes cadeaux, ne donnez pas suite. Unbanz ne demande jamais vos identifiants. Nous sommes un service payant indépendant, sans affiliation avec Meta : paiement d’avance, remboursé à 100 % si le dossier échoue, et pour les cas Facebook et Instagram nous passons par nos contacts chez Meta."),
("Méfiez-vous : ces offres sont souvent des arnaques. Les voies officielles (instagram.com/hacked, contestation) sont gratuites.",
 "Méfiez-vous des inconnus qui vous écrivent en premier ou demandent vos codes. Les voies officielles (instagram.com/hacked, contestation) sont gratuites ; si elles ne suffisent pas, Unbanz prend le dossier en charge, avec paiement d’avance et remboursement à 100 % en cas d’échec."),
("Payer quelqu’un qui prétend avoir un contact chez Meta : personne ne peut le prouver.",
 "Donner votre mot de passe ou vos codes à un inconnu qui vous écrit en premier."),
("Nous ne prétendons à aucun accès spécial chez Meta.",
 "Pour les cas Facebook et Instagram, nous passons par nos contacts chez Meta, sans affiliation officielle."),
("Ne payez personne qui promet une réponse « immédiate ».", "Méfiez-vous de quiconque promet une réponse « immédiate »."),
("Ne payez jamais un « lien d’appel privé » : il n’en existe pas.", "Il n’existe pas de « lien d’appel privé »."),
("Nous ne sommes pas Meta et nous n’avons pas de pouvoir sur ses décisions. Nous passons par les mêmes voies officielles que vous : demandes de réexamen, signalements, formulaires. C’est la plateforme qui décide, et aucun service extérieur ne peut vous assurer un résultat.",
 "Nous ne sommes pas Meta et c’est Meta qui décide. Nous passons par les voies officielles (demandes de réexamen, signalements, formulaires) et, pour les cas Facebook et Instagram, par nos contacts chez Meta. Paiement d’avance, remboursé à 100 % si le dossier échoue ; aucun résultat n’est garanti."),
("promettent un résultat assuré ou prétendent connaître quelqu’un chez Meta.", "ou promettent un résultat assuré."),
("Pas de service extérieur qui ait une ligne directe avec Meta. Unbanz non plus : nous passons par les mêmes voies officielles que vous.",
 "Aucune ligne directe n’est ouverte au public. Pour les cas Facebook et Instagram, Unbanz passe par ses contacts chez Meta, sans affiliation officielle."),
("Non. Nous ne prétendons à aucun accès spécial : nous utilisons les mêmes voies officielles que vous.",
 "Pour les cas Facebook et Instagram, nous passons par nos contacts chez Meta, sans affiliation officielle avec Meta et sans garantie de résultat. Paiement d’avance, remboursé à 100 % si le dossier échoue."),
("Ne payez personne qui promet un accès spécial.", "Ne donnez vos codes à personne qui vous contacte en premier."),
("Non. Personne en dehors de la plateforme ne peut bannir un compte.", "Non. Seule la plateforme peut bannir un compte."),
("et aucun service sérieux ne vous demandera de payer à l’aveugle ou de vous connecter via son lien.",
 "et un service sérieux annonce son prix et sa politique de remboursement par écrit et ne vous demande jamais de vous connecter via son lien."),

# ---------- ES ----------
("o dice tener un contacto en Meta, no sigas adelante. Unbanz nunca te pide tus datos de acceso y no finge tener un acceso especial: usamos las mismas vías oficiales que tú.",
 "o quiere cobrarte con tarjetas regalo, no sigas adelante. Unbanz nunca te pide tus datos de acceso. Somos un servicio de pago independiente, sin afiliación con Meta: pago por adelantado, con reembolso del 100 % si el caso no sale, y en casos de Facebook e Instagram trabajamos a través de nuestros contactos en Meta."),
("Pagar a alguien que dice tener \"un contacto en Meta\".", "Dar tu contraseña o tus códigos a un desconocido que te escribe primero."),
("No pagues a quien promete un acceso especial.", "No des tus códigos a nadie que te escriba primero."),
("Unbanz no tiene afiliación con Meta y no tiene acceso especial a sus empleados.", "Unbanz no tiene afiliación con Meta; en casos de Facebook e Instagram trabaja a través de sus contactos en Meta."),
("No presumen de un contacto en Meta.", "Dejan claros el precio y el reembolso por escrito."),
("No. Unbanz es un servicio independiente y usa las mismas vías oficiales que tú.",
 "No. Unbanz es un servicio independiente, sin afiliación con Meta. En casos de Facebook e Instagram trabajamos a través de nuestros contactos en Meta, con pago por adelantado y reembolso del 100 % si el caso no sale."),
("Quien dice tener \"un contacto en Meta\".", "Quien te escribe primero y te pide códigos."),
("No. Unbanz es independiente y usa las mismas vías oficiales que tú. La decisión siempre es de la plataforma.",
 "No. Unbanz es independiente, sin afiliación con Meta. En casos de Facebook e Instagram trabajamos a través de nuestros contactos en Meta. La decisión siempre es de la plataforma."),
("No pagues a nadie que te prometa un resultado seguro: nadie puede hacerlo.", "Desconfía de quien te prometa un resultado seguro: nadie puede hacerlo."),
("Quien los pide, te promete un resultado seguro o dice tener un contacto en Meta es un estafador.", "Quien los pide o te promete un resultado seguro es un estafador."),
("Te prometen un resultado seguro o dicen tener un contacto en Meta.", "Te prometen un resultado seguro."),
("No se puede comprobar y es una historia típica de estafa.",
 "Unbanz trabaja a través de sus contactos en Meta en casos de Facebook e Instagram, sin afiliación oficial y sin garantizar resultados. Desconfía de quien te escribe primero o te pide la contraseña."),

# ---------- PT-BR ----------
("ou diz ter um contato na Meta, não siga em frente. A Unbanz nunca pede seus dados de acesso e não finge ter um acesso especial: usamos os mesmos caminhos oficiais que você.",
 "ou quer receber em vale-presente, não siga em frente. A Unbanz nunca pede seus dados de acesso. Somos um serviço pago independente, sem vínculo com a Meta: pagamento adiantado, com reembolso de 100% se o caso não der certo, e em casos de Facebook e Instagram trabalhamos por meio dos nossos contatos na Meta."),
("Quem diz ter \"um contato na Meta\".", "Quem escreve primeiro e pede códigos."),
("Não. A Unbanz é independente e usa os mesmos caminhos oficiais que você. A decisão é sempre da plataforma.",
 "Não. A Unbanz é independente, sem vínculo com a Meta. Em casos de Facebook e Instagram trabalhamos por meio dos nossos contatos na Meta. A decisão é sempre da plataforma."),
("Não pague a ninguém que prometa um resultado certo: ninguém pode.", "Desconfie de quem prometa um resultado certo: ninguém pode."),
("A Unbanz não tem vínculo com a Meta e não tem acesso especial aos funcionários deles.", "A Unbanz não tem vínculo com a Meta; em casos de Facebook e Instagram trabalha por meio dos seus contatos na Meta."),
("Não se gabam de ter um contato na Meta.", "Deixam preço e reembolso claros por escrito."),
("Não. A Unbanz é um serviço independente e usa os mesmos caminhos oficiais que você.",
 "Não. A Unbanz é um serviço independente, sem vínculo com a Meta. Em casos de Facebook e Instagram trabalhamos por meio dos nossos contatos na Meta, com pagamento adiantado e reembolso de 100% se o caso não der certo."),
("Não pague quem promete um acesso especial.", "Não passe seus códigos para quem escreve primeiro."),
("Quem pede, promete resultado certo ou diz ter um contato na Meta é golpista.", "Quem pede ou promete resultado certo é golpista."),
("Prometem resultado certo ou dizem ter um contato na Meta.", "Prometem resultado certo."),
("Não dá para comprovar, e é uma história típica de golpe.",
 "A Unbanz trabalha por meio dos seus contatos na Meta em casos de Facebook e Instagram, sem vínculo oficial e sem garantir resultados. Desconfie de quem escreve primeiro ou pede sua senha."),
("Pagar a alguém que diz ter \"um contato na Meta\".", "Passar sua senha ou seus códigos para um desconhecido que escreve primeiro."),

# ---------- NL ----------
("of zegt iemand een contact bij Meta te hebben? Ga er niet op in. Unbanz vraagt nooit om je inloggegevens en doet zich niet voor alsof we een speciale toegang hebben: we gebruiken dezelfde officiële routes als jij.",
 "of wil iemand betaald worden met cadeaukaarten? Ga er niet op in. Unbanz vraagt nooit om je inloggegevens. We zijn een onafhankelijke betaalde dienst, niet verbonden aan Meta: je betaalt vooraf en krijgt 100% terug als de zaak mislukt, en bij Facebook- en Instagram-zaken werken we via onze contacten bij Meta."),
("Betaal niemand die een zeker resultaat belooft: niemand kan dat.", "Wees voorzichtig met iemand die een zeker resultaat belooft: niemand kan dat."),
("Iemand die zegt \"een contact bij Meta\" te hebben.", "Iemand die je als eerste benadert en om codes vraagt."),
("Betaal nooit voor een “privé bezwaarlink”: die bestaat niet.", "Een “privé bezwaarlink” bestaat niet."),
("Nee. Unbanz is onafhankelijk en gebruikt dezelfde officiële routes als jij. Het platform beslist altijd zelf.",
 "Nee. Unbanz is onafhankelijk en niet verbonden aan Meta. Bij Facebook- en Instagram-zaken werken we via onze contacten bij Meta. Het platform beslist altijd zelf."),
("Betalen aan iemand die zegt \"een contact bij Meta\" te hebben.", "Je wachtwoord of codes geven aan een onbekende die je als eerste benadert."),
("Wie daarom vraagt, belooft een zeker resultaat of zegt een contact bij Meta te hebben, is een oplichter.", "Wie daarom vraagt of een zeker resultaat belooft, is een oplichter."),
("Ze beloven een zeker resultaat of zeggen een contact bij Meta te hebben.", "Ze beloven een zeker resultaat."),
("Dat kun je niet controleren en het is een bekend oplichtingsverhaal.",
 "Unbanz werkt bij Facebook- en Instagram-zaken via eigen contacten bij Meta, zonder officiële band en zonder garantie op resultaat. Wantrouw wie je als eerste benadert of om je wachtwoord vraagt."),
("Unbanz is niet verbonden aan Meta en heeft geen speciale toegang tot hun medewerkers.", "Unbanz is niet verbonden aan Meta; bij Facebook- en Instagram-zaken werkt Unbanz via eigen contacten bij Meta."),
("Ze doen geen uitspraken over een contact bij Meta.", "Ze zetten prijs en terugbetaling duidelijk op papier."),
("Nee. Unbanz is een onafhankelijke dienst en gebruikt dezelfde officiële routes als jij.",
 "Nee. Unbanz is een onafhankelijke dienst, niet verbonden aan Meta. Bij Facebook- en Instagram-zaken werken we via onze contacten bij Meta; je betaalt vooraf en krijgt 100% terug als de zaak mislukt."),

# ---------- IT / TR / AR ----------
("Non pagare chi dice di lavorare in Meta.", "Non dare password o codici a chi dice di lavorare in Meta."),
("Non pagare mai per un “link di ricorso privato”: non esiste.", "Non esiste un “link di ricorso privato”."),
("Meta çalışanı olduğunu söyleyen kimseye para ödemeyin.", "Meta çalışanı olduğunu söyleyen kimseyle şifrenizi veya kodlarınızı paylaşmayın."),
("Meta çalışanı olduğunu söyleyen kimseye ödeme yapmayın.", "Meta çalışanı olduğunu söyleyen kimseyle şifrenizi veya kodlarınızı paylaşmayın."),
("لا تدفع أبداً لمن يعدك بـ«رابط اعتراض خاص». لا يوجد شيء كهذا.", "لا يوجد «رابط اعتراض خاص»."),
("لا تدفع لأي شخص يدّعي أنه موظف في ميتا.", "لا تشارك كلمة المرور أو الرموز مع أي شخص يدّعي أنه موظف في ميتا."),
("لا تدفع لمن يدّعي أنه موظف في ميتا.", "لا تشارك كلمة المرور أو الرموز مع من يدّعي أنه موظف في ميتا."),
]

SP = r'(?:\s|&nbsp;|&#160;|&#xa0;|\u00a0|\u202f|\\u00a0|\\u202f)+'
APOS = r"(?:’|'|&#x27;|&#39;|&rsquo;|\\u2019)"
DQ = r'(?:"|&quot;|&#34;|\\")'
def pat(s):
    out=[]; i=0
    toks=re.split(r"(\s+|’|'|\")", s)
    for t in toks:
        if not t: continue
        if t.isspace(): out.append(SP)
        elif t in ("’","'"): out.append(APOS)
        elif t=='"': out.append(DQ)
        else:
            e=re.escape(t)
            e=e.replace('“',r'(?:“|&ldquo;|\\u201c)').replace('”',r'(?:”|&rdquo;|\\u201d)')
            out.append(e)
    return re.compile(''.join(out))

R += [
("Don’t pay for a “code workaround.”</strong> No outside party can change what Facebook asks for.",
 "Don’t trust a “code workaround”</strong> that needs your password or codes."),
("Don’t pay anyone who claims to be inside Instagram</strong> and promises to push the appeal. No outside party can.",
 "Don’t give your login to anyone who claims to work inside Instagram.</strong> Unbanz never asks for it."),
("Don’t pay anyone</strong> who offers access to a deceased person’s account.", "Be wary of anyone</strong> who offers access to a deceased person’s account."),
("Don’t pay anyone</strong> who claims they can “unlock” a deceased person’s account.", "Never share a deceased person’s password or codes</strong> with anyone offering to “unlock” the account."),
("Don’t pay a “Page recovery agent”</strong> who contacts you or hands you a Telegram contact. It’s a known scam pattern.",
 "Ignore “Page recovery agents”</strong> who message you first or push you to Telegram."),
("Paying anyone who asks for your password or codes.</strong> A real service never needs your password. Up-front promises from strangers are a common scam.",
 "Sharing your password or codes with anyone.</strong> A real service never needs your password."),
("Don’t pay a “hacker recovery” service</strong> that contacts you first, or a person who offers to hack the hacker back.",
 "Ignore “hacker recovery” offers</strong> from people who contact you first, or who offer to hack the hacker back."),
("Don’t pay a “2FA unlock” service</strong> that asks for your password or a code.", "Avoid any “2FA unlock” offer</strong> that asks for your password or a code."),
("Claims of inside access at Meta.</strong> Nobody outside Meta can switch an account back on. Unbanz is independent and works only through Meta's own processes.",
 "Guaranteed results.</strong> Nobody can promise Meta will switch an account back on. Unbanz is independent, not affiliated with Meta, never guarantees an outcome, and refunds 100% if a case fails."),
("No “inside access”.</strong> Claims go through the platform’s own reports and processes.",
 "A clear process.</strong> Claims go through the platform’s own reports and processes, with no guaranteed-result promises."),
("any helper who asks for your password, a code, an upfront payment in gift cards or crypto, or claims to have special access to your account is a scam. Recovery only happens through official routes.",
 "any helper who asks for your password or a login code, or wants payment in gift cards, is a scam. A real service like Unbanz never needs your login, gives you the price and refund terms in writing, and refunds 100% if the case fails."),
("They ask for payment in gift cards, crypto or by transfer before doing anything.", "They ask for payment in gift cards, with no written price or refund terms."),
("They claim to have an inside contact or a special tool.", "They guarantee a result, or claim a special tool that needs your login."),
("No outside party can force a platform’s decision. Anyone promising that they can is offering something that doesn’t exist.",
 "Nobody can force a platform’s decision, so be wary of anyone who guarantees one."),
("doesn’t claim a connection inside the platform and doesn’t promise outcomes.", "puts its price and refund terms in writing and doesn’t promise outcomes."),
("Can anyone at Meta help me for a fee?", "Can a paid service help me get my account back?"),
("No. Anyone who says so is not telling the truth. Use the official forms.",
 "A legitimate one can. Unbanz is independent and not affiliated with Meta; for Facebook and Instagram cases we work through our contacts at Meta. Payment is upfront with a 100% refund if it fails, and nobody can guarantee the outcome."),
("Not all, but the ones that ask for your password, promise results, or claim inside access are.",
 "No. The ones to avoid ask for your password, message you first, or guarantee results. Unbanz never asks for logins, puts its fees in writing and refunds 100% if a case fails."),
("No service, including ours, has special access.", "Nobody can reserve one for you, but Unbanz can work on a taken handle through the route that fits it."),
("Does not claim inside access at Meta or a special form.", "Puts the price and refund terms in writing before you pay."),
("it doesn’t sell “inside access” at Meta,", "it never guarantees a result,"),
("Unbanz does not sell inside access at Meta; Instagram makes the final call.", "Unbanz is not affiliated with Meta and never guarantees an outcome; Instagram makes the final call."),
("Avoid anyone who claims inside access or asks for login codes.", "Avoid anyone who asks for login codes."),
("Unbanz works only through Instagram’s own processes,", "Unbanz works through Instagram’s own processes,"),
("Unbanz works only through Instagram’s official processes.", "Unbanz works through Instagram’s official processes and never buys or sells handles."),
("Unbanz works only through official routes, onto your own profile.", "Unbanz works through official routes, onto your own profile."),
("Done in an hour, instant release, or I know someone at Meta are warning signs.", "Done in an hour or instant release are warning signs."),
("“Done in an hour”, “Instant release” or “I know someone at Meta” are the warning signs.", "“Done in an hour” or “Instant release” are the warning signs."),
("Claims inside access at Meta.", "Guarantees a result."),
("we do not create replacement accounts and we do not use any special access.", "and we do not create replacement accounts. For Facebook and Instagram cases we also work through our contacts at Meta."),
("Paying a stranger who wants your login or says they “know someone at Meta”.", "Paying a stranger who wants your login."),
("<li>“I know someone at Meta.”</li>", "<li>“This is guaranteed.”</li>"),
("Anyone claiming a contact at Meta.", "Anyone who messages you first and asks for your login."),
("Paying someone who says they have a contact at Meta.", "Paying a stranger who messages you first and asks for your login."),
("No legit service has special access. Be careful of anyone claiming otherwise.",
 "Nobody can guarantee a result. Unbanz is not affiliated with Meta, but for Instagram and Facebook cases we work through our contacts at Meta, and we know which route fits each handle."),
("Buying a second account, paying someone in a DM who claims special access, or filing the same appeal repeatedly.",
 "Buying a second account, giving your login to someone in a DM, or filing the same appeal repeatedly."),
("<li>Do not claim to have a contact at Meta.</li>", ""),
("Selling aged or agency ad accounts, asking you to log in through their link, or claiming special access inside Meta.",
 "Selling aged or agency ad accounts, or asking you to log in through their link."),
("Claiming special access inside Meta.", "Guaranteeing a result."),
("Claim special access inside Meta. We’re an independent service.", "Guarantee an outcome. We’re an independent service and Meta makes the final decision."),
("No. Such offers are often scams. Nobody needs your password or login codes.",
 "Never give anyone your password or login codes. Unbanz is independent and not affiliated with Meta; for Facebook and Instagram cases we work through our contacts at Meta, with payment upfront and a 100% refund if it fails."),
("Should I pay someone who says they know someone at Meta?", "Can someone with contacts at Meta help?"),
("No honest service can. Be wary of anyone who claims inside access.", "No honest service can promise it, because Meta decides. Unbanz never guarantees an outcome and refunds 100% if a case fails."),
("Anyone asking for your password or claiming inside access.", "Anyone asking for your password or login codes."),
("Walk away from anyone who asks for your password or codes, claims inside access at Meta, sells accounts, or wants gift cards.",
 "Walk away from anyone who asks for your password or codes, sells accounts, or wants gift cards."),
("We do not have special access at Meta and are not affiliated with it.", "We are not affiliated with Meta; for Facebook and Instagram cases we work through our contacts at Meta."),
("That is the official position, and no outside party can change what Facebook offers you.",
 "That is the official position. When that route has ended, Unbanz can still take on the case through our contacts at Meta, with payment upfront and a 100% refund if it fails."),
]
R += [
("passwords, inside contacts, crypto only and more", "passwords, account sales, gift-card-only payment and more"),
("promised results, password requests, inside contacts and more", "promised results, password requests, account sales and more"),
("it doesn't sell \"inside access\" at Meta,", "it never guarantees a result,"),
("It does not use shortcuts, inside contacts or tricks. Unbanz is independent and not affiliated with Meta.",
 "It does not use shortcuts or tricks. Unbanz is independent and not affiliated with Meta; for Facebook and Instagram cases it works through contacts at Meta."),
("<h2>Inside contacts</h2><p>Nobody legit has one.</p>", "<h2>Guarantees</h2><p>Nobody legit promises a sure result.</p>"),
("<li>Claims an “admin” or “plug” at Instagram.</li>", "<li>Pushes you to pay before giving written terms.</li>"),
("<tr><td>Claims of inside contacts at the platform</td><td>No outside provider has an inside route</td></tr>", ""),
("claims of inside contacts at the platform, ", ""),
("Unbanz uses the platform’s official routes only, never asks for passwords or codes, makes no claims of inside contacts, does not buy",
 "Unbanz uses the platform’s official routes and, for Facebook and Instagram cases, its contacts at Meta. It never asks for passwords or codes, does not buy"),
("<li>No claims of inside contacts at Meta.</li>", "<li>No guaranteed-result promises.</li>"),
("Appeals and claims go through the platform’s own process, with no tricks and no inside contacts.",
 "Appeals and claims go through the platform’s own process and, for Facebook and Instagram cases, our contacts at Meta, with no tricks."),
("Avoid anyone who promises results, asks for passwords or claims inside contacts.", "Avoid anyone who promises results or asks for passwords."),
("Does Unbanz sell inside access at Meta?", "Is Unbanz part of Meta?"),
]
R += [
("If someone offers a “plug” at the platform, asks you to log in through their link or wants to sell you an account, walk away.",
 "If someone asks you to log in through their link or wants to sell you an account, walk away."),
("say they have a “Meta plug” or special portal access, ", ""),
("claiming a \"Meta plug\" or special portal access, ", ""),
("claiming a “Meta plug” or special portal access, ", ""),
("fake Meta plugs, stolen OG handles, login links", "stolen OG handles, login links, account sales"),
("<li>“Meta plug” or portal access.</li>", "<li>Guaranteed results.</li>"),
]
R += [
("On prétend connaître quelqu’un chez Meta.", "On vous garantit un résultat."),
("Payer quelqu’un en message privé qui dit connaître quelqu’un chez Meta.", "Donner vos codes à quelqu’un qui vous écrit en message privé."),
("Non. C’est le plus souvent une arnaque.", "Pas un inconnu qui vous écrit en premier : c’est le plus souvent une arnaque. Unbanz ne demande jamais vos codes, annonce son prix par écrit et rembourse à 100 % si le dossier échoue."),
("No. Suele ser una estafa.", "No a un desconocido que te escribe primero: suele ser una estafa. Unbanz nunca pide tus códigos, da el precio por escrito y reembolsa el 100 % si el caso no sale."),
("Não. Em geral é golpe.", "Não a um desconhecido que escreve primeiro: em geral é golpe. A Unbanz nunca pede seus códigos, informa o preço por escrito e reembolsa 100% se o caso não der certo."),
("Betaal niemand die een direct antwoord belooft.", "Wees voorzichtig met wie een direct antwoord belooft."),
("Niet betalen aan iemand in je DM die zegt iemand bij Meta te kennen.", "Geef je codes niet aan iemand die je als eerste een DM stuurt."),
("Nie für einen „privaten Einspruchslink“ zahlen. Den gibt es nicht.", "Einen „privaten Einspruchslink“ gibt es nicht."),
("Niemanden bezahlen, der einen „internen Kontakt“ bei Meta verspricht.", "Niemandem Passwort oder Codes geben, der dich ungefragt anschreibt."),
("Jemanden bezahlen, der „internen Zugang“ verspricht.", "Passwort oder Codes an Fremde weitergeben."),
("Pagare chi promette un “accesso interno”.", "Dare password o codici a sconosciuti."),
("“Özel itiraz linki” için asla para ödemeyin: böyle bir şey yok.", "“Özel itiraz linki” diye bir şey yok."),
]
COMPILED=[(pat(o),n) for o,n in R]

def fix_text(t, json_ctx=False):
    total=0
    for p,n in COMPILED:
        t,k=p.subn(lambda m:n, t); total+=k
    return t,total

if __name__=='__main__':
    root=sys.argv[1] if len(sys.argv)>1 else '.'
    files=0; hits=0; per=[0]*len(R)
    for dp,dn,fn in os.walk(root):
        if any(x in dp for x in ('/node_modules','/.git','/.vercel')): continue
        for f in fn:
            if not f.endswith(('.html','.txt','.xml','.json','.js','.py','.md','.mjs')): continue
            if f=='fix_self_undermining_copy.py': continue
            p=os.path.join(dp,f)
            try: t=open(p,encoding='utf-8').read()
            except Exception: continue
            n=t; c=0
            for i,(pp,new) in enumerate(COMPILED):
                n,k=pp.subn(lambda m,new=new:new, n); per[i]+=k; c+=k
            if c:
                open(p,'w',encoding='utf-8').write(n); files+=1; hits+=c
    print('files changed',files,'replacements',hits)
    for i,(o,_) in enumerate(R):
        if per[i]==0: print('UNUSED:',o[:90])
