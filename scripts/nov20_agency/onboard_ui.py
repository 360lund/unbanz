"""Nov 20 2026: shared markup for the agency onboarding hero + 5-step card (en/fr/nl/es/pt). Used by hub.py and loc_hubs.py."""
import html, json
esc = lambda t: html.escape(t, quote=True)
U = {
 'en': dict(title='Agency onboarding', count='5 quick questions', q1='What kind of agency are you?', o1=['PR', 'Talent management', 'SMMA', 'Reputation', 'Legal', 'Other'],
   name='Agency name <span>(optional)</span>', ph='e.g. Northside Talent', next='Continue →', back='← Back',
   q2='How many client cases do you handle per month?', o2=['1–3 / month', '4–10 / month', '10+ / month'],
   q3='What do you need most?', o3=['Instagram & Facebook bans', 'TikTok / X bans', 'Username claims', 'Mix of all'],
   q4='Our white-label rate is $1,200 per case via upfront bank transfer. Are you okay with that?', o4=[('Yes, $1,200/case works', 'Yes, $1,200/case works'), ('Yes, need 5+/mo volume pricing', 'Yes, I need 5+/mo volume pricing')],
   q5='You’re all set. Send us your answers.', i18n=None,
   eye='WHITE-LABEL PARTNER PROGRAM', lead='You keep the client. We file the appeal or username claim quietly in the background, with no Unbanz name in front of your client.',
   terms=[('$1,200', 'per case'), ('7–14', 'days, usually'), ('100%', 'refund if not reinstated in 14 days')], fine='Upfront bank transfer · no cards · no passwords needed · official platform processes only.'),
 'fr': dict(title='Inscription agence', count='5 questions rapides', q1='Quel type d’agence êtes-vous ?', o1=['RP', 'Gestion de talents', 'SMMA', 'E-réputation', 'Juridique', 'Autre'],
   name='Nom de l’agence <span>(facultatif)</span>', ph='ex. Agence Nord', next='Continuer →', back='← Retour',
   q2='Combien de dossiers clients traitez-vous par mois ?', o2=['1–3 / mois', '4–10 / mois', '10+ / mois'],
   q3='De quoi avez-vous le plus besoin ?', o3=['Bannissements Instagram et Facebook', 'Bannissements TikTok / X', 'Récupération de pseudos', 'Un peu de tout'],
   q4='Notre tarif marque blanche est de 1 200 $ par dossier, par virement bancaire à l’avance. Cela vous convient ?', o4=[('Oui, 1 200 $/dossier me convient',) * 2, ('Oui, il me faut un tarif volume (5+/mois)',) * 2],
   q5='C’est prêt. Envoyez-nous vos réponses.',
   i18n=dict(step='Étape {n} sur {t}', wait='Un instant…', thanks='Merci pour vos réponses.', na='L’inscription directe des agences n’est pas disponible dans votre région pour le moment.', wa='Envoyer sur WhatsApp', em='Envoyer par email',
     fineWa='Vos réponses sont pré-remplies. Nous répondons sous un jour ouvré.', fineEm='Vos réponses sont pré-remplies dans l’email. Nous répondons sous un jour ouvré.', intro='Bonjour Unbanz, je souhaite devenir agence partenaire en marque blanche.',
     lType='Type d’agence', lName='Nom de l’agence', lVol='Dossiers clients par mois', lSvc='Besoins', lPrice='Tarif', lWeb='Site web', lReach='Meilleur moyen de me joindre', subj='Inscription agence'),
   eye='PROGRAMME PARTENAIRE MARQUE BLANCHE', lead='Vous gardez le client. Nous déposons l’appel ou la demande de pseudo en coulisses, sans le nom Unbanz face à votre client.',
   terms=[('1 200 $', 'par dossier'), ('7–14', 'jours en général'), ('100 %', 'remboursé si non rétabli sous 14 jours')], fine='Virement bancaire à l’avance · pas de carte · aucun mot de passe · uniquement les procédures officielles des plateformes.'),
 'nl': dict(title='Aanmelden als bureau', count='5 korte vragen', q1='Wat voor bureau ben je?', o1=['PR', 'Talentmanagement', 'SMMA', 'Reputatie', 'Juridisch', 'Anders'],
   name='Naam van het bureau <span>(optioneel)</span>', ph='bijv. Noord Media', next='Verder →', back='← Terug',
   q2='Hoeveel klantzaken behandel je per maand?', o2=['1–3 / maand', '4–10 / maand', '10+ / maand'],
   q3='Wat heb je het meest nodig?', o3=['Instagram- en Facebook-bans', 'TikTok- / X-bans', 'Gebruikersnaamclaims', 'Een mix van alles'],
   q4='Ons white-label tarief is $1.200 per zaak, vooraf per bankoverschrijving. Is dat oké?', o4=[('Ja, $1.200 per zaak is prima',) * 2, ('Ja, ik wil volumeprijzen (5+/maand)',) * 2],
   q5='Klaar. Stuur ons je antwoorden.',
   i18n=dict(step='Stap {n} van {t}', wait='Even geduld…', thanks='Bedankt voor je antwoorden.', na='Direct aanmelden als bureau is momenteel niet beschikbaar in jouw regio.', wa='Stuur via WhatsApp', em='Stuur per e-mail',
     fineWa='Je antwoorden staan al klaar. We reageren binnen één werkdag.', fineEm='Je antwoorden staan al in de e-mail. We reageren binnen één werkdag.', intro='Hoi Unbanz, ik wil me aanmelden als white-label bureaupartner.',
     lType='Type bureau', lName='Naam bureau', lVol='Klantzaken per maand', lSvc='Nodig', lPrice='Tarief', lWeb='Website', lReach='Beste manier om me te bereiken', subj='Aanmelding bureau'),
   eye='WHITE-LABEL PARTNERPROGRAMMA', lead='Jij houdt de klant. Wij dienen het bezwaar of de gebruikersnaamclaim achter de schermen in, zonder de naam Unbanz richting je klant.',
   terms=[('$1.200', 'per zaak'), ('7–14', 'dagen, meestal'), ('100%', 'terug als niet hersteld binnen 14 dagen')], fine='Vooraf per bankoverschrijving · geen creditcard · geen wachtwoorden · alleen officiële platformprocedures.'),
 'es': dict(title='Alta de agencia', count='5 preguntas rápidas', q1='¿Qué tipo de agencia tienes?', o1=['RR. PP.', 'Representación de talento', 'SMMA', 'Reputación', 'Legal', 'Otra'],
   name='Nombre de la agencia <span>(opcional)</span>', ph='p. ej. Norte Media', next='Continuar →', back='← Atrás',
   q2='¿Cuántos casos de clientes gestionas al mes?', o2=['1–3 / mes', '4–10 / mes', '10+ / mes'],
   q3='¿Qué necesitas sobre todo?', o3=['Bloqueos de Instagram y Facebook', 'Bloqueos de TikTok / X', 'Recuperación de nombres de usuario', 'Un poco de todo'],
   q4='Nuestra tarifa de marca blanca es de 1.200 $ por caso, por transferencia bancaria por adelantado. ¿Te parece bien?', o4=[('Sí, 1.200 $/caso me va bien',) * 2, ('Sí, necesito precio por volumen (5+/mes)',) * 2],
   q5='Listo. Envíanos tus respuestas.',
   i18n=dict(step='Paso {n} de {t}', wait='Un momento…', thanks='Gracias por tus respuestas.', na='El alta directa de agencias no está disponible en tu región por ahora.', wa='Enviar por WhatsApp', em='Enviar por email',
     fineWa='Tus respuestas ya van rellenadas. Respondemos en un día laborable.', fineEm='Tus respuestas ya van en el email. Respondemos en un día laborable.', intro='Hola, Unbanz: quiero darme de alta como agencia partner de marca blanca.',
     lType='Tipo de agencia', lName='Nombre de la agencia', lVol='Casos de clientes al mes', lSvc='Necesidades', lPrice='Tarifa', lWeb='Web', lReach='Mejor forma de contactarme', subj='Alta de agencia'),
   eye='PROGRAMA DE PARTNERS DE MARCA BLANCA', lead='Tú te quedas con el cliente. Nosotros presentamos la apelación o la solicitud del nombre de usuario en segundo plano, sin el nombre de Unbanz ante tu cliente.',
   terms=[('1.200 $', 'por caso'), ('7–14', 'días, normalmente'), ('100 %', 'reembolso si no se recupera en 14 días')], fine='Transferencia bancaria por adelantado · sin tarjeta · sin contraseñas · solo procesos oficiales de las plataformas.'),
 'pt': dict(title='Cadastro de agência', count='5 perguntas rápidas', q1='Que tipo de agência é a sua?', o1=['RP', 'Gestão de talentos', 'SMMA', 'Reputação', 'Jurídico', 'Outro'],
   name='Nome da agência <span>(opcional)</span>', ph='ex.: Norte Mídia', next='Continuar →', back='← Voltar',
   q2='Quantos casos de clientes você atende por mês?', o2=['1–3 / mês', '4–10 / mês', '10+ / mês'],
   q3='Do que você mais precisa?', o3=['Banimentos no Instagram e Facebook', 'Banimentos no TikTok / X', 'Resgate de nomes de usuário', 'Um pouco de tudo'],
   q4='Nosso valor white-label é US$ 1.200 por caso, por transferência bancária antecipada. Tudo bem para você?', o4=[('Sim, US$ 1.200/caso funciona',) * 2, ('Sim, preciso de preço por volume (5+/mês)',) * 2],
   q5='Tudo pronto. Envie suas respostas.',
   i18n=dict(step='Etapa {n} de {t}', wait='Um momento…', thanks='Obrigado pelas respostas.', na='O cadastro direto de agências não está disponível na sua região no momento.', wa='Enviar pelo WhatsApp', em='Enviar por e-mail',
     fineWa='Suas respostas já estão preenchidas. Respondemos em até um dia útil.', fineEm='Suas respostas já estão no e-mail. Respondemos em até um dia útil.', intro='Olá, Unbanz! Quero me cadastrar como agência parceira white-label.',
     lType='Tipo de agência', lName='Nome da agência', lVol='Casos de clientes por mês', lSvc='Necessidades', lPrice='Valor', lWeb='Site', lReach='Melhor forma de contato', subj='Cadastro de agência'),
   eye='PROGRAMA DE PARCEIROS WHITE-LABEL', lead='Você fica com o cliente. Nós cuidamos do recurso ou do pedido de nome de usuário nos bastidores, sem o nome Unbanz diante do seu cliente.',
   terms=[('US$ 1.200', 'por caso'), ('7–14', 'dias, em geral'), ('100%', 'de reembolso se não restaurar em 14 dias')], fine='Transferência bancária antecipada · sem cartão · sem senhas · apenas processos oficiais das plataformas.'),
}
def opts(vals): return ''.join(f'<button type="button" class="ob-opt" aria-pressed="false" data-v="{esc(v)}">{esc(l)}</button>' for v, l in vals)
def card(lang):
    L = U[lang]; back = f'<button type="button" class="ob-back">{L["back"]}</button>'
    data = f' data-i18n="{esc(json.dumps(L["i18n"], ensure_ascii=False))}"' if L['i18n'] else ''
    return (f'<div class="ob" id="ob" aria-label="{esc(L["title"])}"{data}><div class="ob-top"><p class="ob-t">{L["title"]}</p><p class="ob-count">{L["count"]}</p></div><div class="ob-bar" aria-hidden="true"><i></i></div>'
     f'<div class="ob-step" data-k="type"><p class="ob-q">{esc(L["q1"])}</p><div class="ob-opts">' + opts([(x, x) for x in L['o1']]) + '</div>'
     f'<label class="ob-lab" for="ob-name">{L["name"]}</label><input class="ob-in" id="ob-name" type="text" autocomplete="organization" placeholder="{esc(L["ph"])}" maxlength="80"/>'
     f'<div class="ob-nav"><span></span><button type="button" class="ob-next" disabled>{L["next"]}</button></div></div>'
     f'<div class="ob-step" data-k="volume"><p class="ob-q">{esc(L["q2"])}</p><div class="ob-opts ob-col">' + opts([(x, x) for x in L['o2']]) + '</div><div class="ob-nav">' + back + '</div></div>'
     f'<div class="ob-step" data-k="service"><p class="ob-q">{esc(L["q3"])}</p><div class="ob-opts ob-col">' + opts([(x, x) for x in L['o3']]) + '</div><div class="ob-nav">' + back + '</div></div>'
     f'<div class="ob-step" data-k="pricing"><p class="ob-q">{esc(L["q4"])}</p><div class="ob-opts ob-col">' + opts(L['o4']) + '</div><div class="ob-nav">' + back + '</div></div>'
     f'<div class="ob-step" data-k="done"><p class="ob-q">{esc(L["q5"])}</p><ul class="ob-sum"></ul><div class="ob-out"></div><div class="ob-nav">' + back + '</div></div></div>')
def hero(lang, crumb_html, h1):
    L = U[lang]
    return (f'<section class="wl-hero"><div class="container wl-grid"><div class="wl-copy">{crumb_html}<p class="wl-eye">{L["eye"]}</p>'
     f'<h1>{h1}</h1><p class="wl-lead">{L["lead"]}</p><ul class="wl-terms">' + ''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in L['terms']) + '</ul>'
     f'<p class="wl-fine">{L["fine"]}</p></div>' + card(lang) + '</div></section>')
