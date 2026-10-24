# Chapitre 21 — Rien de neuf

## Lundi, 8 h 30

Le lundi, j'ai effacé le grand tableau de la salle Lys pour la première fois depuis le sprint 0. Seuls sont restés, sur le mur d'à côté, la carte des stories avec son ruban rouge, le registre de la dette et le parking des bonnes idées. Sur le tableau vide, j'ai tracé deux colonnes.

À gauche, *Homologation, phase 1*. Quatre semaines, avec les fêtes au milieu, pour passer de « fini » à « en production ». La recette des gestionnaires sur des dossiers rejoués. La montée en charge. L'audit d'accessibilité. Les tests de résilience. La formation des gestionnaires et du centre d'appels. Et toutes les corrections que cela produirait.

À droite, *Phase 2*. L'analyse de tous les sinistres avec la nouvelle méthode, la préparation du premier incrément du train, et l'essai sur la story du proche.

Puis j'ai écrit trois règles au-dessus des deux colonnes, parce que je savais exactement ce qui allait se passer sans elles.

*La production passe avant tout. Une anomalie d'homologation interrompt n'importe quel travail de la phase 2.*

*Chaque front a sa limite de travail en cours. Personne ne travaille sur plus d'un sujet par front à la fois.*

*Pas de héros. Une garde par semaine pour les anomalies, et personne ne corrige seul le soir.*

J'ai réparti l'équipe. Julien et Sofiane à gauche le matin, pour les corrections. Nadia et Émilie à droite, avec Sofiane l'après-midi pour l'essai. Julien passerait à droite dès que l'homologation le laisserait respirer, pour l'architecture. Martine mènerait la recette des gestionnaires et la formation. Mathilde suivrait les deux.

— Et toi ? a demandé Julien.

— Au milieu. Je surveille la frontière.

Il a hoché la tête. Depuis la semaine précédente, il ne me posait plus la question pour me mettre en difficulté.

Nous n'avons pas tenu une heure.

À 9 h 40, Mathilde est entrée avec la demande de copie des données pour la préproduction. L'environnement d'homologation devait recevoir, comme pour chaque projet de la maison depuis toujours, une copie du système des contrats, pour que les gestionnaires puissent rejouer des dossiers réalistes. La demande était partie le vendredi. Mathilde l'avait refusée.

— Le socle n'entre en vigueur pour toute la maison qu'au premier janvier. Pour nous, il s'applique depuis le Mercredi noir. Il dit : aucune donnée de production dans un environnement de test sans anonymisation validée. Le script d'anonymisation est toujours celui de 2014. Celui qui laisse passer les téléphones et les courriels. C'est écrit en toutes lettres dans le registre de la dette, avec la date du 11 avril.

— C'est notre propre règle, a dit Julien.

— Justement, a dit Mathilde. Si nous ne la respectons pas la première fois qu'elle nous gêne, personne d'autre ne la respectera.

Personne n'a contesté. Il n'y avait rien à contester. La règle avait été écrite pour un cas exactement comme celui-là, et elle avait été écrite par nous.

Sans données, pas de recette des gestionnaires. Sans recette, pas d'homologation. Sylvie a calculé en silence, et j'ai vu sur son visage que le calcul n'était pas bon.

Gérard est monté à 10 heures, appelé par Julien. Il a lu la demande refusée, puis le motif, puis la ligne du registre qui portait son nom.

— Donnez-moi trois jours, a-t-il dit. Et le machin de Sofiane.

— Le ticket de 2019 ? En trois jours ? a demandé Sylvie.

— En 2019, j'aurais mis trois mois. Il fallait d'abord retrouver tous les champs qui contiennent quelque chose de personnel, dans deux cent quarante programmes. Aujourd'hui, ils sont dans le wiki. J'ai relu la page la semaine dernière.

## Jeudi, 16 heures

Gérard a travaillé trois jours avec Sofiane, dans la salle Scarpe, la porte fermée. Il ne s'agissait pas du portail, ni de la phase 2. Il s'agissait d'un programme de 2014 que personne n'avait touché depuis dix ans, écrit dans un langage que Sofiane lisait à peine, et qui tournait chaque mois sur la base de recette sans que personne ne regarde ce qu'il faisait.

Le premier jour, l'agent a interrogé le wiki, et non les programmes. *Quels champs du système des contrats contiennent une donnée personnelle ?* La réponse citait trente-sept champs, répartis dans onze fichiers, avec pour chacun le programme qui l'écrivait et l'année où il avait été ajouté. Le script de 2014 en anonymisait vingt et un. Gérard a relu la liste des seize manquants. Il en connaissait quatorze. Il en avait oublié deux, ajoutés en 2020 pour le prélèvement mensuel.

Le deuxième jour, l'agent a proposé la correction du script, champ par champ, et Gérard l'a relue ligne par ligne. Il a refusé deux propositions, parce que l'agent remplaçait des numéros de téléphone par des numéros au hasard qui pouvaient appartenir à de vraies personnes. Il a exigé des numéros réservés, de ceux qu'on ne peut attribuer à personne. L'agent a corrigé sans discuter.

Le troisième jour, Mathilde a fait ce qu'elle faisait toujours : elle n'a pas lu le code, elle a vérifié le résultat. Sur une copie isolée, elle a fait tourner le nouveau script, puis elle a tiré au hasard mille contrats anonymisés et les a confrontés à l'annuaire des assurés, comme le jour du Mercredi noir.

Aucun téléphone ne correspondait. Aucun courriel. Aucune adresse.

Puis elle a regardé le seul champ que personne n'avait mentionné : le commentaire libre, où les gestionnaires notaient depuis trente ans ce qui ne rentrait dans aucune case. Dans dix-neuf des mille contrats, il contenait un nom, un numéro de portable, et une fois l'adresse d'un fils qui gérait les papiers de sa mère.

— Le wiki ne le classait pas comme personnel, a dit Sofiane. C'est un champ de texte.

— C'est un champ où des gens écrivent, a dit Gérard. Donc il est personnel.

L'agent a proposé de repérer les noms et les numéros dans ce texte libre et de les masquer un par un. Gérard a secoué la tête.

— On ne nettoie pas du texte libre. On le remplace. Tout entier. Personne n'a besoin de lire les commentaires de Martine pour tester un portail.

Il a ajouté lui-même une ligne à la page du wiki : *Commentaire libre : personnel par nature. Ne jamais copier tel quel hors de la production.* Puis il l'a validée, avec son nom.

Mathilde a refait son tirage le jeudi à 15 heures. Mille contrats, zéro correspondance. Elle a signé la validation à 16 heures, et le ticket de mars 2019 est passé en *terminé*, avec quatre mois d'avance sur la date du registre. Sylvie l'a fermé elle-même. Elle avait l'air d'avoir attendu ce moment depuis le Mercredi noir.

La copie a tourné dans la nuit. La recette des gestionnaires pourrait commencer le vendredi, avec trois jours de retard sur le planning d'homologation.

J'ai écrit à Claire à 16 h 30. Trois lignes, comme le soir du sprint 0. *Homologation décalée de trois jours. Cause : nous avons appliqué notre propre règle sur les données de recette, et corrigé au passage le script d'anonymisation de 2014. Date de fin d'homologation inchangée, en réduisant la marge de la dernière semaine.*

Sa réponse est arrivée dix minutes plus tard.

*Bonne raison. Gardez-la pour le comité.*

## La semaine suivante

La recette des gestionnaires a commencé le vendredi, dans une salle du troisième étage que Philippe Wattebled avait fait équiper de six postes. Martine et cinq collègues y ont rejoué deux cents dossiers de l'année précédente, anonymisés : dégâts des eaux et vols, choisis par Martine pour couvrir tout ce qu'elle avait vu passer en vingt-deux ans. Chaque gestionnaire jouait l'assuré sur le portail, puis traitait le dossier dans son propre outil, comme un lundi ordinaire.

En cinq jours, elles ont trouvé quatorze anomalies. Douze étaient mineures. Deux étaient bloquantes, et aucune n'aurait été trouvée par un test automatique.

La première concernait les contrats de l'ancienne Mutuelle de l'Artois. Leur numéro commençait par un 7 et comptait un chiffre de plus que les autres. Le formulaire du portail refusait de les reconnaître. Il y en avait encore onze mille en portefeuille. Sofiane a ouvert le wiki : la page sur la fusion de 1995 le disait en toutes lettres, depuis deux semaines. Personne n'avait pensé à la relire en écrivant le formulaire, qui datait du sprint 1.

La seconde concernait l'accusé de réception par SMS. Beaucoup d'assurés âgés n'avaient qu'un téléphone fixe. Le portail n'envoyait rien, et ne le disait à personne. Nadia a écrit la règle en dix minutes : sans portable, un courriel ; sans courriel, une lettre, envoyée par la chaîne d'édition de la maison.

Le mardi, Didier Vermeersch, le responsable de la production, a fait lancer le test de montée en charge. Le test avait reconstitué le pic d'un lundi matin d'hiver, trois fois le volume moyen d'une journée concentré sur deux heures. Le portail a tenu sans broncher. C'est le système des contrats qui a calé, au bout de vingt minutes. Julien a trouvé pourquoi avec l'agent dans l'heure : pour chaque déclaration, le portail interrogeait six fois la transaction de 1997, une fois par écran, pour relire le même contrat. La correction tenait en une demi-journée : lire le contrat une fois, au début, et le garder pendant toute la déclaration. Au second essai, le jeudi, le système des contrats ne s'est même pas aperçu du pic.

— Six appels pour la même chose, a dit Didier Vermeersch. Le mainframe nous est facturé à la consommation. Vous venez de m'économiser un petit budget.

L'audit d'accessibilité a été mené par un cabinet extérieur, comme la loi l'imposait désormais à une entreprise de la taille de la maison. Il a relevé vingt-trois non-conformités, dont quatre bloquantes. Mais c'est Bruno Delannoy qui nous a vraiment appris quelque chose.

Bruno était gestionnaire au service des recours depuis douze ans. Il avait perdu la vue à vingt ans, et il travaillait avec un lecteur d'écran et une plage braille. Martine lui avait demandé s'il voulait bien déclarer un sinistre sur le portail, comme un assuré. Il est venu le mercredi, avec son ordinateur portable et ses écouteurs, et il s'est installé dans la salle Lys pendant que nous le regardions, ce qui le faisait sourire.

Il a franchi les trois premiers écrans sans difficulté. Au quatrième, celui des photos, il s'est arrêté.

— Il me dit « bouton », a-t-il dit. Juste « bouton ». Il y en a trois sur la page. Je ne sais pas lequel ajoute une photo.

Puis il a envoyé une photo trop lourde, exprès, pour voir. Le message d'erreur s'est affiché en rouge à l'écran. Son lecteur d'écran n'en a rien dit. Pour lui, il ne s'était rien passé.

Émilie a pris des notes pendant une heure, sans l'interrompre. Le soir, elle a écrit des scénarios d'un genre nouveau : *Étant donné un assuré qui utilise un lecteur d'écran, quand il envoie une photo trop lourde, alors le message d'erreur lui est annoncé.* L'agent a corrigé les vingt-trois non-conformités en deux jours, en suivant le rapport du cabinet et les scénarios d'Émilie. Sofiane et Julien ont relu.

Bruno est revenu le vendredi. Il a déclaré un dégât des eaux de bout en bout, en quatorze minutes. Nadia en mettait six.

— Quatorze minutes, c'est très bien, a-t-il dit en retirant ses écouteurs. D'habitude, sur les sites des assureurs, je n'y arrive pas du tout. J'appelle.

Personne n'a rien dit pendant un moment. Puis Nadia lui a demandé s'il accepterait de tester aussi la phase 2. Il a dit oui avant qu'elle ait fini sa phrase.

Le dernier test était celui de la résilience, celui que DORA exigeait. Le mercredi à 14 heures, Didier Vermeersch a coupé volontairement le système des contrats pendant une heure, en pleine journée. Le portail a basculé comme la nuit : il a enregistré les déclarations, les a gardées chiffrées, puis les a traitées une par une à la réouverture. Aucune n'a été perdue. Didier a chronométré le retour à la normale, et il l'a noté pour le registre.

Il n'y a eu qu'un détail. Pendant l'heure de coupure, le portail avait répondu aux assurés de test : *Vous recevrez votre accusé de réception par SMS ce matin.* Il était 14 h 20.

Émilie a ri la première. Nadia a réécrit la phrase en trente secondes : *dès que notre système sera de nouveau disponible.* Nous avions conçu ce mode pour la nuit, et nous avions écrit le message pour la nuit. La résilience, au fond, c'est d'abord ça : imaginer que la panne arrivera aussi au moment où on ne l'attend pas.

## Vendredi 19 décembre

Le vendredi 19 décembre commençait le gel de fin d'année. Comme chaque hiver depuis toujours, plus rien ne serait mis en production dans la maison jusqu'au 5 janvier, sauf urgence signée par Hervé Delcourt en personne. Nous n'avions rien à mettre en production. Mais le gel avait un effet que je n'avais pas anticipé : il donnait à tout le monde, le temps d'une journée, l'envie de faire le point.

La dernière réunion de l'année de l'instance commune s'est tenue à 10 heures, dans la salle Marque. Claire et Laurent Dewitte la co-présidaient, assis côte à côte, et il n'y avait plus eu besoin d'échanger des courriels sur la disposition des chaises.

J'ai présenté l'état de l'homologation en cinq minutes. La recette des gestionnaires terminée : quatorze anomalies, toutes corrigées, dont les deux bloquantes. La montée en charge tenue au second essai. L'audit d'accessibilité soldé, et un gestionnaire non-voyant qui avait déclaré un sinistre en quatorze minutes. Le test de résilience réussi, à un message près. Restaient la formation des gestionnaires et du centre d'appels, que Martine assurerait pendant les deux semaines des fêtes, et le procès-verbal d'homologation, que Philippe Wattebled signerait début janvier si rien ne bougeait. La mise en production était prévue le mardi 13 janvier, après la levée du gel et la décision du comité.

Dewitte m'a laissé finir. Puis il a ouvert son carnet en cuir, à une page que j'ai reconnue à sa place dans le carnet. C'était celle de la première revue, au sprint 1.

— En octobre, je vous avais posé trois questions, a-t-il dit. La tenue en charge un jour de pointe. L'accessibilité pour les assurés malvoyants. Les tests de résilience exigés par DORA. Vous m'aviez répondu que c'était dans le backlog.

— C'était vrai, ai-je dit. Ce n'était pas une réponse.

— Aujourd'hui, c'en est une. Les trois.

Il a rayé sa page, proprement, d'un seul trait de stylo-plume.

— Une chose encore. Vos contrats en 7, ceux de l'ancienne Artois. Franck a vérifié hier. Les nouveaux écrans de gestion d'Horizon les refusent aussi. Nous ne les avions pas vus. Votre wiki nous épargne une anomalie de production.

Franck Ryckebusch, au bout de la table, a confirmé d'un signe de tête. Il avait l'air moins déconcerté qu'au mois de novembre. Il s'habituait.

L'après-midi, nous avons organisé les fêtes. Une garde par semaine, comme prévu : Julien la première, Sofiane la seconde, avec Mathilde joignable pour tout ce qui toucherait aux données. Pas de correction le soir, pas de correction seul. Nadia et Émilie partiraient les deux semaines ; la phase 2 attendrait leur retour, et personne n'aurait le droit de la faire avancer en leur absence. Martine a affiché dans la salle Lys le calendrier de ses sessions de formation, quarante gestionnaires et douze conseillers du centre d'appels, en petits groupes, entre deux réveillons.

Avant de partir, j'ai regardé la colonne de gauche du tableau, celle de l'homologation. Pendant deux semaines, nous n'avions pas ajouté une seule fonctionnalité au portail. Pas une story. Rien de neuf. Et pourtant, le portail avait changé davantage qu'au cours de n'importe quel sprint. Il reconnaissait onze mille contrats qu'il ignorait. Il appelait le système des contrats six fois moins. Il parlait à ceux qui ne voient pas l'écran. Il savait attendre en plein jour. Il prévenait les assurés qui n'avaient pas de portable.

Le 5 décembre, nous avions dit que les développements étaient finis, et c'était vrai. Mais « fini » voulait dire que le portail faisait ce que nous avions prévu. « En production » voudrait dire qu'il faisait ce dont les gens avaient besoin, y compris ceux auxquels nous n'avions pas pensé. Entre les deux, il y avait eu ce mois-là. Et personne, au début du projet, ne l'avait compté dans les quatorze semaines.

## Le carnet de Thomas

**Ce qui s'est passé.** Les développements terminés, le portail est entré en homologation pour un mois, pendant que la phase 2 démarrait en parallèle. L'équipe s'est organisée sur deux fronts, avec une priorité claire à la production, une limite de travail par front et une garde. Le premier jour, l'équipe s'est vu refuser par sa propre règle la copie de données dont elle avait besoin : le script d'anonymisation de 2014 a été corrigé en trois jours grâce au wiki, après cinq ans d'attente. La recette des gestionnaires sur des dossiers rejoués, la montée en charge, l'audit d'accessibilité avec un gestionnaire non-voyant et le test de résilience ont fait apparaître des défauts qu'aucun test automatique n'avait vus : onze mille contrats non reconnus, des assurés sans portable, six appels au lieu d'un, des boutons sans nom, un message pensé pour la nuit. Pas une fonctionnalité nouvelle n'a été ajoutée en deux semaines ; le portail n'avait jamais autant changé.

**La leçon.** « Fini » veut dire que le produit fait ce que l'équipe a prévu ; « en production » veut dire qu'il fait ce dont les gens ont besoin, y compris ceux auxquels personne n'a pensé. Comptez ce dernier kilomètre dans le planning dès le premier jour. Faites tester par les vrais utilisateurs, dans leurs vrais outils, sur des cas qu'ils choisissent eux-mêmes, et faites venir ceux que vos tests ne représentent pas. Mesurez la charge sur les systèmes qui vous entourent, pas seulement sur le vôtre. Appliquez vos propres règles la première fois qu'elles vous gênent : c'est à ce moment qu'elles prennent leur valeur. Enfin, un agent corrige vite ce que l'homologation trouve, mais il ne trouve pas à la place de ceux qui vivront avec le produit.

**Trois questions à poser à votre équipe**

1. Combien de temps notre planning prévoit-il entre « fini » et « en production » ?
2. Quels utilisateurs nos tests ne représentent-ils pas, et les avons-nous invités ?
3. Quelle règle que nous nous sommes donnée serions-nous tentés de contourner la première fois qu'elle nous ralentira ?

**Pour aller plus loin.** Manuel, chapitres M11 (le wiki d'équipe : interroger le savoir existant avant d'écrire) et M13 (bonnes pratiques : homologuer un produit construit avec des agents).
