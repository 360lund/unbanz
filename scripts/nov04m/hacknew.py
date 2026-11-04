import sys;sys.path.insert(0,'scripts/nov04m');from clone import make;from loc import add
B='https://unbanz.com';EN='instagram-account-disabled-after-hack-appeal'
HF='<p>Si la demande n’aboutit pas ou si aucune option n’est proposée, voyez notre page <a href="/fr/recuperer-compte-instagram/">récupérer un compte Instagram</a>. Le prix vous est indiqué avant le début du travail, et votre mot de passe reste chez vous.</p>'
f=make('fr','faire-appel-instagram-desactive-delai','instagram-pirate-puis-desactive',EN,
 'Instagram piraté puis désactivé : que faire ? | Unbanz',
 'Votre compte Instagram a été piraté puis désactivé pour une activité que vous n’avez pas faite ? Les étapes pour sécuriser, faire appel et expliquer le piratage.',
 'Piraté puis désactivé','Compte Instagram piraté puis désactivé : que faire ?',
 'Si un pirate a utilisé votre compte et qu’Instagram l’a ensuite désactivé, sécurisez d’abord votre e-mail, puis faites appel une seule fois depuis l’écran de désactivation en expliquant brièvement que le compte a été piraté, avec la date. Gardez des captures d’écran des e-mails de sécurité.',
 [('ordre','Dans quel ordre agir','<ol><li>Sécurisez la boîte e-mail liée au compte : nouveau mot de passe, déconnexion des autres appareils.</li><li>Cherchez l’e-mail de sécurité d’Instagram signalant un changement, et utilisez son lien si possible.</li><li>Faites appel depuis l’écran de désactivation, une seule fois.</li></ol>'),
  ('ecrire','Quoi écrire','<p>Restez court et factuel : la date approximative du piratage, ce que vous avez constaté (changement d’e-mail, publications que vous n’avez pas faites) et que vous avez repris le contrôle de votre e-mail. N’accusez personne et n’ajoutez pas de détails inutiles.</p>'),
  ('preuves','Les preuves à garder','<ul><li>Les e-mails de sécurité d’Instagram (changement d’e-mail ou de mot de passe).</li><li>Des captures d’écran de la décision et de sa date.</li><li>Si possible, un dépôt de plainte ou un signalement, voir <a href="/fr/compte-pirate-porter-plainte-signaler/">porter plainte après un piratage</a>.</li></ul>'),
  ('apres','Ensuite','<p>Meta ne publie aucun délai. Voyez <a href="/fr/faire-appel-instagram-desactive-delai/">le délai d’un appel Instagram</a> et, en cas de refus, <a href="/fr/instagram-appel-refuse/">que faire après un refus</a>.</p>')],HF,
 [('Instagram peut-il désactiver un compte à cause d’un pirate ?','Oui. Si le pirate publie du spam ou des arnaques, le compte peut être désactivé même si vous n’y êtes pour rien.'),
  ('Faut-il dire dans l’appel que le compte a été piraté ?','Oui, brièvement et avec la date. C’est souvent l’élément le plus utile.'),
  ('Que faire si le pirate a changé l’e-mail ?','Cherchez l’e-mail de sécurité envoyé à l’ancienne adresse ; il contient souvent un lien pour annuler le changement.')],
 [('/fr/compte-instagram-pirate-que-faire/','Compte Instagram piraté'),('/fr/instagram-pirate-publications-crypto/','Publications crypto après piratage'),('/fr/compte-instagram-desactive-comment-recuperer/','Compte Instagram désactivé'),('/fr/compte-pirate-porter-plainte-signaler/','Porter plainte')])
HN='<p>Lukt het niet met de officiële stappen, of heb je liever hulp? Kijk op onze pagina <a href="/nl/instagram-account-terugkrijgen/">Instagram-account terugkrijgen</a>. We noemen de prijs in het gesprek, voordat het werk begint, en je wachtwoord blijft bij jou.</p>'
n=make('nl','hoe-lang-duurt-instagram-bezwaar','instagram-gehackt-en-uitgeschakeld',EN,
 'Instagram gehackt en daarna uitgeschakeld | Unbanz',
 'Is je Instagram-account gehackt en daarna uitgeschakeld voor iets wat je niet deed? De stappen om te beveiligen, bezwaar te maken en de hack uit te leggen.',
 'Gehackt en uitgeschakeld','Instagram gehackt en daarna uitgeschakeld: wat nu?',
 'Heeft een hacker je account gebruikt en heeft Instagram het daarna uitgeschakeld, beveilig dan eerst je e-mail en maak daarna één keer bezwaar vanaf het scherm van de uitschakeling. Leg kort uit dat het account gehackt was, met de datum, en bewaar screenshots van de beveiligingsmails.',
 [('volgorde','In welke volgorde','<ol><li>Beveilig de mailbox van het account: nieuw wachtwoord, andere apparaten uitloggen.</li><li>Zoek de beveiligingsmail van Instagram over een wijziging en gebruik de link daarin als dat kan.</li><li>Maak één keer bezwaar vanaf het scherm van de uitschakeling.</li></ol>'),
  ('schrijven','Wat je schrijft','<p>Kort en feitelijk: ongeveer wanneer de hack was, wat je zag (ander e-mailadres, berichten die je niet plaatste) en dat je je e-mail weer in handen hebt. Beschuldig niemand en voeg geen overbodige details toe.</p>'),
  ('bewijs','Wat je bewaart','<ul><li>De beveiligingsmails van Instagram over een gewijzigd e-mailadres of wachtwoord.</li><li>Screenshots van de beslissing en de datum.</li><li>Eventueel een aangifte, zie <a href="/nl/gehackt-account-aangifte-doen/">aangifte doen na een hack</a>.</li></ul>'),
  ('daarna','Daarna','<p>Meta noemt geen termijn. Lees <a href="/nl/hoe-lang-duurt-instagram-bezwaar/">hoe lang een Instagram-bezwaar duurt</a> en bij een afwijzing <a href="/nl/instagram-bezwaar-afgewezen/">bezwaar afgewezen</a>.</p>')],HN,
 [('Kan Instagram een account uitschakelen door een hacker?','Ja. Als de hacker spam of oplichting plaatst, kan het account worden uitgeschakeld, ook als jij niets fout deed.'),
  ('Moet ik in het bezwaar zeggen dat ik gehackt ben?','Ja, kort en met de datum. Dat is vaak het nuttigste wat je kunt noemen.'),
  ('Wat als de hacker het e-mailadres heeft veranderd?','Zoek de beveiligingsmail die naar het oude adres is gestuurd; daarin staat vaak een link om de wijziging ongedaan te maken.')],
 [('/nl/instagram-account-gehackt/','Instagram-account gehackt'),('/nl/instagram-gehackt-crypto-berichten/','Crypto-berichten na hack'),('/nl/instagram-account-uitgeschakeld/','Instagram-account uitgeschakeld'),('/nl/gehackt-account-aangifte-doen/','Aangifte doen')],twins={'fr':f})
p='fr/instagram-pirate-puis-desactive/index.html';s=open(p).read()
if n not in s: open(p,'w').write(s.replace('<link rel="alternate" hreflang="x-default"',f'<link rel="alternate" hreflang="nl" href="{n}"><link rel="alternate" hreflang="nl-NL" href="{n}"><link rel="alternate" hreflang="x-default"',1))
u=[f,n,B+'/'+EN+'/']
for sl in ['compte-instagram-pirate-que-faire','instagram-pirate-publications-crypto']:
    if add('fr',sl,'<h2 id="related-2026">Voir aussi (2026)</h2><p><a href="/fr/instagram-pirate-puis-desactive/">Compte piraté puis désactivé</a> : dans quel ordre agir et quoi écrire.</p>','related-2026'): u.append(f'{B}/fr/{sl}/')
for sl in ['instagram-account-gehackt','instagram-gehackt-crypto-berichten']:
    if add('nl',sl,'<h2 id="related-2026">Zie ook (2026)</h2><p><a href="/nl/instagram-gehackt-en-uitgeschakeld/">Gehackt en daarna uitgeschakeld</a>: in welke volgorde en wat je schrijft.</p>','related-2026'): u.append(f'{B}/nl/{sl}/')
open('/tmp/b18.txt','w').write('\n'.join(u));print(u)
