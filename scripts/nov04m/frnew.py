import sys;sys.path.insert(0,'scripts/nov04m');from clone import make
H='<p>Si la demande n’aboutit pas ou si aucune option n’est proposée, voyez notre page <a href="/fr/compte-facebook-desactive/">compte Facebook désactivé</a>. Le prix vous est indiqué avant le début du travail, et votre mot de passe reste chez vous.</p>'
u=make('fr','faire-appel-instagram-desactive-delai','delai-appel-facebook-desactive','how-long-does-a-facebook-appeal-take',
 'Appel Facebook : combien de temps attendre ? | Unbanz',
 'Facebook ne publie aucun délai pour les appels : la réponse peut arriver en quelques jours comme en plusieurs semaines. Que faire pendant l’attente.',
 'Délai d’un appel Facebook','Compte Facebook désactivé : combien de temps dure l’appel ?',
 'Facebook ne publie aucun délai de traitement pour les appels : la réponse peut arriver en quelques jours comme en plusieurs semaines, et une vérification d’identité peut allonger l’attente. Ne renvoyez pas la demande, surveillez l’e-mail du compte (spams compris) et gardez une capture d’écran de la confirmation.',
 [('delai','Combien de temps faut-il attendre ?','<p>Il n’existe pas de durée officielle. L’attente dépend du motif, de la vérification d’identité demandée et de la charge de traitement. Personne ne peut s’engager sur une date.</p>'),
  ('ou','Où suivre la demande','<p>Connectez-vous à Facebook : l’écran de désactivation indique en général où en est la demande. Regardez aussi l’Espace Comptes et l’e-mail lié au compte, y compris les spams.</p>'),
  ('selfie','Si une vidéo selfie ou une pièce d’identité est demandée','<p>Envoyez-la une seule fois, avec un bon éclairage et un document lisible au nom du compte. Si l’écran reste bloqué, attendez avant de recommencer : plusieurs envois n’accélèrent rien.</p>'),
  ('pendant','Pendant l’attente','<ul><li>Ne renvoyez pas la demande.</li><li>Ne créez pas de nouveau compte pour contourner la décision.</li><li>Méfiez-vous de quiconque promet une réponse « immédiate ».</li></ul>'),
  ('trop','Et si rien ne se passe ?','<p>Si l’appel est refusé ou si rien n’arrive après plusieurs semaines, voyez <a href="/fr/compte-facebook-desactive-faire-appel/">faire appel d’un compte Facebook désactivé</a>. En Europe, vous pouvez aussi examiner le <a href="/fr/droit-de-recours-dsa-meta/">recours prévu par le DSA</a>.</p>')],H,
 [('Combien de temps dure un appel Facebook ?','Facebook ne publie pas de délai. Cela peut aller de quelques jours à plusieurs semaines, et personne ne peut s’engager sur une date précise.'),
  ('Dois-je renvoyer ma demande si je n’ai pas de réponse ?','Non. Renvoyer la demande n’accélère pas le traitement. Gardez la capture d’écran de la confirmation et surveillez vos e-mails.'),
  ('Où vais-je recevoir la réponse ?','En général par e-mail à l’adresse liée au compte, et à la connexion sur Facebook. Vérifiez aussi les spams.'),
  ('Un service payant peut-il accélérer la réponse ?','Aucun service extérieur ne peut imposer un délai à Meta. Méfiez-vous de ceux qui promettent une réponse immédiate.')],
 [('/fr/compte-facebook-desactive-faire-appel/','Faire appel (Facebook)'),('/fr/compte-facebook-desactive/','Compte Facebook désactivé'),('/fr/faire-appel-instagram-desactive-delai/','Délai d’un appel Instagram'),('/fr/droit-de-recours-dsa-meta/','Recours DSA (Europe)')])
print(u)
