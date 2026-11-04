import sys;sys.path.insert(0,'scripts/nov04m');from clone import make;from loc import add
B='https://unbanz.com';EN='why-was-my-facebook-ad-account-disabled-without-warning'
HF='<p>Si la demande de réexamen n’aboutit pas, voyez notre page <a href="/fr/compte-publicitaire-meta-restreint/">compte publicitaire Meta restreint</a>. Le prix vous est indiqué avant le début du travail, et votre mot de passe reste chez vous.</p>'
f=make('fr','faire-appel-instagram-desactive-delai','compte-publicitaire-desactive-sans-raison',EN,
 'Compte publicitaire désactivé sans prévenir : pourquoi ? | Unbanz',
 'Votre compte publicitaire Meta a été désactivé sans avertissement ? Les raisons les plus fréquentes, où lire le motif et comment demander un réexamen.',
 'Désactivé sans prévenir','Compte publicitaire Meta désactivé sans avertissement : pourquoi ?',
 'Meta désactive parfois un compte publicitaire sans prévenir lorsqu’un contrôle automatique repère un risque : moyen de paiement, activité inhabituelle, publicité refusée ou lien avec un compte déjà restreint. Ouvrez l’Account Quality du portefeuille business pour lire le motif, puis demandez un réexamen une seule fois.',
 [('raisons','Les raisons les plus fréquentes','<ul><li>Un problème de paiement ou un moyen de paiement signalé.</li><li>Une hausse soudaine des dépenses ou un changement de pays de facturation.</li><li>Des publicités refusées à répétition.</li><li>Un lien avec un profil, une page ou un portefeuille déjà restreint.</li><li>Un accès suspect, par exemple après un piratage.</li></ul>'),
  ('ou','Où lire le motif','<p>Dans Meta Business Suite, ouvrez Account Quality : la restriction, son motif et le bouton de demande de réexamen y figurent en général. Les intitulés peuvent varier selon la langue.</p>'),
  ('faire','Quoi faire maintenant','<ol><li>Faites une capture d’écran du motif et de la date.</li><li>Corrigez ce qui peut l’être : paiement, accès, publicité concernée.</li><li>Demandez un réexamen une seule fois, voir <a href="/fr/compte-publicitaire-meta-demande-de-reexamen-quoi-ecrire/">quoi écrire</a>.</li></ol>'),
  ('pas','Ce qu’il vaut mieux éviter','<ul><li>Créer un nouveau compte publicitaire pour contourner la décision.</li><li>Envoyer plusieurs demandes de réexamen.</li><li>Confier vos accès à quelqu’un qui promet un résultat.</li></ul>')],HF,
 [('Meta prévient-il avant de désactiver un compte publicitaire ?','Pas toujours. Beaucoup de restrictions viennent de contrôles automatiques et arrivent sans avertissement.'),
  ('Où voir pourquoi mon compte publicitaire est désactivé ?','Dans Account Quality, dans Meta Business Suite. Le motif y est en général indiqué, avec l’option de réexamen.'),
  ('Combien de temps prend le réexamen ?','Meta ne publie aucun délai. Ne renvoyez pas la demande pendant l’attente.')],
 [('/fr/compte-publicitaire-meta-restreint/','Compte publicitaire restreint'),('/fr/compte-publicitaire-restreint-probleme-de-paiement/','Problème de paiement'),('/fr/compte-publicitaire-desactive-hausse-soudaine-depenses/','Hausse des dépenses'),('/fr/compte-publicitaire-meta-demande-de-reexamen-quoi-ecrire/','Quoi écrire')])
HN='<p>Lukt het verzoek om beoordeling niet, kijk dan op onze pagina <a href="/nl/advertentieaccount-terugkrijgen/">advertentieaccount terugkrijgen</a>. We noemen de prijs in het gesprek, voordat het werk begint, en je wachtwoord blijft bij jou.</p>'
n=make('nl','hoe-lang-duurt-instagram-bezwaar','advertentieaccount-uitgeschakeld-zonder-waarschuwing',EN,
 'Advertentieaccount zonder waarschuwing uitgeschakeld | Unbanz',
 'Is je Meta-advertentieaccount zonder waarschuwing uitgeschakeld? De meest voorkomende redenen, waar je de reden leest en hoe je om beoordeling vraagt.',
 'Uitgeschakeld zonder waarschuwing','Meta-advertentieaccount zonder waarschuwing uitgeschakeld: waarom?',
 'Meta schakelt een advertentieaccount soms zonder waarschuwing uit als een automatische controle een risico ziet: de betaalmethode, ongebruikelijke activiteit, afgekeurde advertenties of een koppeling met een al beperkt account. Open Accountkwaliteit in het bedrijfsportfolio om de reden te lezen en vraag één keer om beoordeling.',
 [('redenen','De meest voorkomende redenen','<ul><li>Een betaalprobleem of een gemarkeerde betaalmethode.</li><li>Een plotselinge stijging van de uitgaven of een ander factuurland.</li><li>Herhaaldelijk afgekeurde advertenties.</li><li>Een koppeling met een profiel, pagina of portfolio dat al beperkt is.</li><li>Verdachte toegang, bijvoorbeeld na een hack.</li></ul>'),
  ('waar','Waar je de reden leest','<p>Open in Meta Business Suite de pagina Accountkwaliteit: daar staan de beperking, de reden en meestal de knop om beoordeling te vragen. Namen kunnen per taal verschillen.</p>'),
  ('doen','Wat je nu doet','<ol><li>Maak een screenshot van de reden en de datum.</li><li>Los op wat kan: betaling, toegang, de betreffende advertentie.</li><li>Vraag één keer om beoordeling, zie <a href="/nl/advertentieaccount-bezwaar-wat-schrijven/">wat je schrijft</a>.</li></ol>'),
  ('niet','Wat je beter niet doet','<ul><li>Een nieuw advertentieaccount maken om de beslissing te omzeilen.</li><li>Meerdere verzoeken tegelijk insturen.</li><li>Je toegang geven aan iemand die een resultaat belooft.</li></ul>')],HN,
 [('Waarschuwt Meta voordat een advertentieaccount wordt uitgeschakeld?','Niet altijd. Veel beperkingen komen uit automatische controles en komen zonder waarschuwing.'),
  ('Waar zie ik waarom mijn advertentieaccount is uitgeschakeld?','In Accountkwaliteit in Meta Business Suite. Daar staat meestal de reden, met de optie om beoordeling te vragen.'),
  ('Hoe lang duurt de beoordeling?','Meta noemt geen termijn. Stuur het verzoek tijdens het wachten niet opnieuw.')],
 [('/nl/advertentieaccount-terugkrijgen/','Advertentieaccount terugkrijgen'),('/nl/advertentieaccount-beperkt-betalingsprobleem/','Betaalprobleem'),('/nl/facebook-advertentieaccount-uitgeschakeld/','Advertentieaccount uitgeschakeld'),('/nl/advertentieaccount-bezwaar-wat-schrijven/','Wat je schrijft')],twins={'fr':f})
for p,o in [('fr/compte-publicitaire-desactive-sans-raison/index.html',n),('nl/advertentieaccount-uitgeschakeld-zonder-waarschuwing/index.html',None)]:
    s=open(p).read().replace('data-service="unban"','data-service="ad"')
    if o and o not in s: s=s.replace('<link rel="alternate" hreflang="x-default"',f'<link rel="alternate" hreflang="nl" href="{o}"><link rel="alternate" hreflang="nl-NL" href="{o}"><link rel="alternate" hreflang="x-default"',1)
    open(p,'w').write(s)
u=[f,n,B+'/'+EN+'/']
for sl in ['compte-publicitaire-meta-restreint','compte-publicitaire-facebook-desactive']:
    if add('fr',sl,'<h2 id="related-2026">Voir aussi (2026)</h2><p><a href="/fr/compte-publicitaire-desactive-sans-raison/">Compte publicitaire désactivé sans prévenir</a> : raisons fréquentes et où lire le motif.</p>','related-2026'): u.append(f'{B}/fr/{sl}/')
for sl in ['facebook-advertentieaccount-uitgeschakeld','advertentieaccount-terugkrijgen']:
    if add('nl',sl,'<h2 id="related-2026">Zie ook (2026)</h2><p><a href="/nl/advertentieaccount-uitgeschakeld-zonder-waarschuwing/">Uitgeschakeld zonder waarschuwing</a>: veelvoorkomende redenen en waar je de reden leest.</p>','related-2026'): u.append(f'{B}/nl/{sl}/')
open('/tmp/b20.txt','w').write('\n'.join(u));print(u)
