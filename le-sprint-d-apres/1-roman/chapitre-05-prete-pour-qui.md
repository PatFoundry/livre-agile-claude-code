# Chapitre 5 — Prête, pour qui ?

## Mercredi, 9 heures

J'ai distribué un post-it à chacun.

— Une seule question. Quand une story est-elle prête ? Vous écrivez votre réponse, sans regarder celle du voisin.

J'ai ramassé les post-it et je les ai collés au mur, l'un sous l'autre.

*Quand j'ai écrit tous les exemples.* C'était Nadia.

*Quand l'agent ne pose plus de questions.* Sofiane.

*Quand je peux écrire le test avant le code.* Émilie.

*Quand les tests passent et que j'ai relu le code.* Julien.

Julien a vu les trois autres et a grimacé.

— Je n'ai pas répondu à la même question que vous.

— Non, ai-je dit. Et c'est exactement le problème. Hier, quand tu as demandé si SIN-14 était prête, tu voulais savoir si elle était terminée. Nadia a compris : peut-on la commencer ? Ce sont deux portes différentes. L'une à l'entrée du sprint, l'autre à la sortie.

J'ai tracé deux colonnes au tableau. À gauche, *Prête* : ce qu'il faut pour commencer. À droite, *Terminée* : ce qu'il faut pour livrer.

La colonne de droite s'est remplie en dix minutes. Les équipes connaissent bien la Definition of Done : tests au vert, revue humaine, exemples validés par Émilie, Jira à jour, déploiement en recette. Personne n'a discuté.

La colonne de gauche a pris toute la matinée.

Sofiane a ouvert le feu.

— Le guide officiel de Scrum ne parle même pas de Definition of Ready. Il y a des articles entiers qui expliquent que c'est un piège : une porte de plus, de la bureaucratie, et un PO qui ne livre plus rien parce que rien n'est jamais assez prêt.

— Vous avez raison sur le guide, ai-je répondu. Et sur le risque. Mais avec une équipe humaine, une story à moitié prête se termine quand même : le développeur pose ses questions en cours de route. Avec l'agent, une story à moitié prête produit du code complet, propre et faux. Nous l'avons vu avec la franchise.

— Alors ce n'est pas une porte, a dit Nadia. C'est une liste de vérification.

— Oui. Si une story ne passe pas, elle n'est pas refusée. Elle vous revient avec la liste de ce qui manque.

Ils ont construit la liste ensemble. Émilie a imposé que chaque exemple devienne un test sans interprétation. Julien a exigé de connaître les modules touchés avant qu'on commence. Sofiane, qui avait cessé de résister, a proposé la règle la plus utile.

— Le test de la session neuve. On ouvre une session vierge, on donne la story à l'agent, et on lui demande s'il a des questions métier. S'il en a, elle n'est pas prête. Il est meilleur que nous pour trouver les trous.

À midi, la liste tenait sur un écran. Nadia l'a affichée au mur, et Julien l'a versée dans le dépôt, à côté du CLAUDE.md, par une demande de fusion.

```text
DEFINITION OF READY — une story entre dans un sprint si :
1. Sa valeur pour l'assuré tient en une phrase (le « afin de »).
2. Ses exemples couvrent le cas courant et au moins deux cas limites.
3. Chaque exemple peut devenir un test sans interprétation.
4. Aucune question ouverte, ou chacune a un nom et une date.
5. Les données personnelles touchées sont identifiées.
6. Les modules impactés sont connus et validés par Julien.
7. Elle se livre en moins de deux jours, agent compris.
Test final : une session neuve de l'agent la lit
et ne pose aucune question métier.
```

Nadia a relu la règle 7 deux fois.

— Moins de deux jours. La moitié de mes stories ne tiendront pas.

— Alors on les coupera, a dit Julien. Une petite story, l'agent la réussit. Une grosse, il la réussit aussi, mais personne n'arrive à la relire.

## Mercredi, 14 heures

Sofiane voulait attaquer les neuf stories dès l'après-midi. Julien l'a arrêté d'une phrase.

— Avant de construire neuf pièces, on vérifie que la maison tient debout.

Il a dessiné au tableau ce qu'il appelait un squelette qui marche. Le chemin le plus mince possible à travers tout le système, de l'écran de l'assuré jusqu'au gestionnaire. Une page de déclaration réduite à trois champs. Un service qui la reçoit. Un appel au système des contrats, à travers l'adaptateur, pour vérifier que le contrat existe. Un stockage pour les photos. Une transmission du dossier vers la boîte de travail des gestionnaires. Un accusé de réception par courrier électronique. Chaque étape sommaire, mais réelle, et déployée en recette par l'intégration continue, sans aucune intervention manuelle.

— Pas une fonctionnalité de plus, a-t-il dit. Mais si ce chemin marche, tout le reste n'est que du remplissage. S'il ne marche pas, on le saura maintenant, et pas dans six semaines.

L'agent a construit les pièces logicielles plus vite que nous n'arrivions à les relire. La page, le service, le stockage, les tests : deux heures. Sofiane a ensuite écrit avec lui le pipeline de déploiement vers la recette. À 17 heures, tout était vert sur GitHub.

Et rien ne marchait.

Le premier mur était un certificat expiré sur le serveur de recette de l'adaptateur. Le deuxième, une règle de pare-feu manquante entre notre segment réseau et la recette des contrats : la demande à l'équipe réseau prenait cinq jours ouvrés. Le troisième était plus étrange. L'adaptateur répondait parfaitement le matin, mais renvoyait une erreur entre midi et 14 heures, sans aucune explication.

L'agent a analysé les journaux, proposé des hypothèses, écrit un script de diagnostic. Il a trouvé la cause du certificat en trois minutes. Mais il ne pouvait ni renouveler un certificat qu'il n'avait pas le droit de toucher, ni ouvrir un pare-feu, ni savoir ce qui se passait à midi sur un mainframe qu'il ne voyait pas. Ses limites n'étaient pas techniques. Elles étaient organisationnelles.

Pour le pare-feu, j'ai appelé Mathilde. Elle a lu la demande, vérifié qu'elle correspondait au cadre signé par Bertrand et l'a fait passer en priorité. Une heure plus tard, la règle était ouverte. Avoir la sécurité de son côté, c'est aussi ça.

Pour le reste, Julien a décroché son téléphone.

— Gérard ? C'est Julien. J'ai besoin de toi.

Gérard Vandamme travaillait aux études centrales, deux étages plus bas. Soixante et un ans, quarante ans de COBOL, et le seul homme de la maison qui connaissait l'autre côté de l'adaptateur. Il est monté avec un vieux carnet à couverture noire.

— Le certificat ? Il expire tous les ans en novembre. Je le renouvelle à la main. Cette année, j'ai oublié.

— Et l'erreur entre midi et deux ?

— Le traitement de rapprochement des contrats tourne à midi en recette. Il verrouille les tables. En production, il tourne la nuit. Personne ne l'a jamais écrit nulle part, mais tout le monde le sait.

— Tout le monde ? a demandé Julien.

Gérard a haussé les épaules.

— Bon. Moi.

En dix minutes, il avait réglé ce que nous cherchions depuis trois heures. Avant de partir, il a ajouté, presque en passant :

— Profitez-en. Je pars en retraite en avril.

J'ai noté la phrase dans mon carnet. Sous la date, j'ai écrit : *Tout ce que sait Gérard n'existe que dans la tête de Gérard.* Et je l'ai soulignée deux fois.

## Jeudi, 17 h 40

Toute la journée avait été consacrée aux soudures. Un champ mal nommé entre le service et l'adaptateur. Un format de date que le mainframe lisait à l'américaine. Une boîte de travail des gestionnaires qui refusait les pièces jointes de plus de dix mégaoctets, ce qu'Émilie avait évidemment prévu sur un post-it rose dès la semaine précédente.

À 17 h 40, Julien a dit simplement :

— Essayez.

Émilie a pris le téléphone de test de la mutuelle, connecté au réseau interne. Elle a ouvert la page de recette. Trois champs sur fond blanc, sans logo, sans couleur, avec une police que personne n'avait choisie. Elle s'est connectée avec l'identité d'une assurée fictive de nos jeux de données synthétiques, Mme Lefort, et a déclaré un dégât des eaux daté de la veille. Elle a pris en photo la tasse de café de Sofiane, faute de mieux, et a appuyé sur *Envoyer*.

Nous avons regardé l'écran de Julien, où défilaient les journaux de la recette. Une ligne pour la réception. Une ligne pour l'appel à l'adaptateur. Une ligne, plus longue, pour la réponse du mainframe : le contrat de Mme Lefort existait et il était actif. Une ligne pour le stockage de la photo. Une ligne pour la transmission vers les gestionnaires.

Quarante et une secondes après l'envoi, le téléphone d'Émilie a vibré. *Votre déclaration de sinistre a bien été enregistrée sous le numéro SIN-2026-000001.*

Personne n'a applaudi. Ce n'était pas le genre de la maison. Mais Nadia a pris une photo de l'écran, Sofiane a levé les deux poings, et Julien a fait une chose que je ne l'avais jamais vu faire : il a souri sans rien ajouter.

Nadia a appelé une gestionnaire de son ancienne équipe, Martine, qui avait accepté de tester la boîte de travail en recette. Martine a rappelé deux minutes plus tard.

— J'ai un dossier Lefort avec une photo de tasse de café. C'est normal ?

— C'est parfait, a dit Nadia.

J'ai regardé la page de déclaration, d'une laideur parfaite.

— Rien de ce que nous avons fait cette semaine n'impressionnera le comité de direction, ai-je dit. C'est exactement pour ça que c'était important. Désormais, chaque story que nous livrerons arrivera au bout de la chaîne, chez une vraie gestionnaire, le jour même.

— Et le jour où quelque chose cassera, a ajouté Julien, on le verra en quarante secondes, pas en recette dans six mois.

## Vendredi, 14 heures

La revue du sprint 0 s'est tenue dans la salle Deûle. Mathilde était venue, comme convenu. Sylvie Caron aussi, son tableau de bord imprimé sous le bras. Nadia avait invité Martine et une autre gestionnaire. Claire s'était excusée le matin par un message : *Comité de direction prolongé. Envoyez-moi trois lignes.*

Émilie a refait la démonstration de la veille, avec une vraie photo de dégât des eaux cette fois, tirée de nos jeux d'essai. Quarante secondes plus tard, le dossier apparaissait dans la boîte de travail de Martine, projetée sur le second écran.

Martine l'a ouvert, a parcouru les champs, puis a croisé les bras.

— Si ça m'arrive comme ça lundi, je sais quoi en faire. Mais il manque le numéro de téléphone du déclarant. La moitié des dossiers, on rappelle les gens.

Nadia l'a noté sans discuter. Une nouvelle story était née d'une revue de sprint, exactement comme le voulait la méthode.

Mathilde a pris la parole ensuite. Elle avait épluché les journaux de la semaine.

— Aucun incident. Les règles ont refusé environ trente pour cent des commandes demandées par l'agent sur le poste de Sofiane.

Sofiane a rougi. Elle a levé la main avant qu'il ne se justifie.

— Ce n'est pas un reproche. Il teste les limites. Ça prouve qu'elles existent et qu'elles tiennent. Je préfère ça à des journaux trop propres.

Sylvie Caron a attendu la fin pour poser sa question.

— Combien de stories livrées ?

— Une, ai-je répondu. Et un squelette qui traverse tout le système. Zéro pour votre tableau, je sais.

— Et la charge ?

— Lundi, nous commençons à mesurer. Dans deux semaines, vous aurez de vrais chiffres.

Elle a noté quelque chose dans la marge, sans que je puisse lire quoi.

Après la revue, je me suis assis seul dans la salle pour écrire les trois lignes de Claire. Le sprint 0 devait durer deux semaines. Il en avait duré trois. La semaine de la sécurité n'avait été prévue par personne, moi compris.

```text
Sprint 0 terminé avec une semaine de retard (cadre de sécurité).
Une déclaration traverse tout le système en recette en 41 secondes.
Il reste 11 semaines : dégât des eaux tenable, vol encore incertain.
```

Claire a rappelé dix minutes plus tard.

— Pourquoi m'annoncez-vous un retard que personne ne vous a demandé ?

— Parce qu'un retard annoncé tôt est une information. Annoncé tard, c'est une faute.

Un silence.

— Le comité va me demander pourquoi.

— Dites-leur que nous avons une semaine de retard, un cadre de sécurité signé par le RSSI et un dossier qui arrive chez une gestionnaire en quarante secondes. Et demandez-leur ce qu'Horizon peut en dire.

Elle a ri, brièvement, pour la première fois depuis que je la connaissais.

En rentrant dans l'open space, j'ai trouvé Sofiane devant le tableau de Jira. Les neuf stories de la première tranche étaient alignées dans la colonne *Prêt*, chacune passée au test de la session neuve.

— Lundi, sprint 1, a-t-il dit. Neuf stories prêtes. Avec l'agent, je les fais en deux jours.

— On verra, a dit Julien sans lever les yeux.

Dans mon carnet, j'ai écrit une seule ligne : *Lundi, on mesure.*

## Le carnet de Thomas

**Ce qui s'est passé.** L'équipe a découvert que « prête » voulait dire cinq choses différentes. Elle a séparé la Definition of Ready de la Definition of Done, et construit une liste de vérification adaptée à l'agent, avec le test de la session neuve. Avant toute fonctionnalité, elle a monté un squelette qui traverse tout le système. Les obstacles n'étaient pas techniques, mais organisationnels : un certificat, un pare-feu, et un savoir détenu par un seul homme. Le sprint 0 a débordé d'une semaine, annoncée le jour même.

**La leçon.** Avec un agent, une story à moitié prête ne produit pas un travail à moitié fait. Elle produit un code complet et faux. La Definition of Ready n'est pas une porte, c'est une liste qui renvoie la story au Product Owner avec ce qui manque. Et l'agent est le meilleur testeur de cette liste.

**Trois questions à poser à votre équipe**

1. Quand nous disons « prête », parlons-nous de commencer ou de livrer ?
2. Une story passe-t-elle chez nous le test de la session neuve ?
3. Quel savoir indispensable n'existe que dans la tête d'une seule personne ?

**Pour aller plus loin.** Manuel, chapitre M2 (premiers pas : tester une story dans une session neuve), chapitre M10 (pipeline GitHub et déploiement) et chapitre M13 (bonnes pratiques).
