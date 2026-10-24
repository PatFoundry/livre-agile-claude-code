# Chapitre 26 — La vélocité est morte

## Lundi 2 février, 9 heures

Hélène Carpentier avait dit « la semaine prochaine ». Elle est arrivée le lundi à 9 heures, avec Quentin Desmet, le contrôleur de gestion de la DSI : la trentaine, une voix douce, et aucun carnet, parce qu'il retenait les chiffres.

— Le comité de jeudi veut un bilan des premières semaines de production, a-t-il dit. Et Catherine Duhamel a demandé à Hervé Delcourt une comparaison entre votre phase 1 et Horizon. Hervé me l'a demandée vendredi soir.

— Les équipes d'Horizon publient leur vélocité dans Jira à chaque sprint, a ajouté Hélène. Quentin connaît leur coût par point. Il lui faut le vôtre. Et depuis vendredi, vos nouveaux tickets n'ont plus de points du tout.

C'était vrai. Sylvie avait cessé d'estimer à la deuxième itération, sans que personne le décide vraiment, parce que plus personne ne regardait le résultat.

— Nos points ne sont pas les leurs, ai-je dit. Et ils ne sont même plus les nôtres. En septembre, une story de cinq points nous prenait trois jours. En décembre, une story de cinq points prenait une matinée, dont la moitié en relecture. Le chiffre est resté le même ; ce qu'il mesurait a changé sous nos yeux.

— Alors donnez-moi quelque chose qui se compare, a dit Quentin, sans hausser la voix.

— Je ne sais pas encore quoi. Laissez-moi jusqu'à demain.

L'après-midi, j'ai demandé à l'agent de reconstituer l'histoire de chaque story depuis le premier sprint, à partir de Jira et de GitHub, qu'il lisait depuis l'automne : les points estimés, la date de création, le début du travail, la demande de fusion, les relectures, les retours, la fusion, la mise en recette, les anomalies rattachées. J'y ai ajouté la facture du modèle. Depuis l'alerte budgétaire de novembre, chaque session de l'agent portait la clé de sa story, et nous pouvions dire ce que chacune avait coûté en calcul, au centime près.

Il lui a fallu quarante minutes. Il m'a fallu la soirée pour vérifier. J'ai tiré dix stories au hasard et je les ai reconstituées à la main, écran par écran. Huit correspondaient. Pour les deux autres, l'agent avait compté comme une retouche une story rouverte pour une faute d'orthographe dans un libellé, et une autre rouverte parce que Nadia avait changé d'avis sur une règle. Ni l'une ni l'autre n'était une retouche au sens où je l'entendais. J'ai donc écrit la définition que j'aurais dû écrire en premier : *une story retouchée est une story déclarée finie qui retourne en développement parce qu'elle ne faisait pas ce qu'elle devait faire.* Pas parce qu'on a changé d'avis ; pas pour une virgule. L'agent a recalculé.

À minuit, j'avais sous les yeux une courbe que je n'avais jamais vue, alors que tous ses chiffres étaient là depuis septembre.

## Mardi 3 février, 14 heures

J'ai réuni l'équipe dans la salle Lys et j'ai affiché deux courbes, l'une au-dessus de l'autre, sans rien dire.

La première était notre vélocité, sprint par sprint, telle que Sylvie l'avait reportée chaque quinzaine au comité : cinquante-deux points au sprint 1, soixante et onze au sprint 2, puis quarante-neuf, trente-sept, trente et un. Une montée, un sommet, une longue descente. Présentée seule, c'était l'histoire d'une équipe qui s'était essoufflée.

La seconde était le taux de retouche, avec la définition de la veille : vingt-deux pour cent des stories au sprint 1, quarante et un au sprint 2, puis vingt-six, quatorze, sept. La même forme. Le même sommet.

Personne n'a parlé pendant un long moment. C'est Julien qui a rompu le silence.

— Le sprint 2. Les quarante demandes de fusion. Les approbations du samedi soir.

— Le sprint dont j'étais le plus fier, a dit Sofiane.

— Celui où j'ai trouvé le plus d'anomalies, a dit Émilie.

— Celui que mon tableau de bord affichait en vert, a dit Sylvie.

J'ai ajouté la troisième courbe, le temps de traversée, du début du travail sur une story à sa mise en recette : neuf jours de médiane au sprint 2, deux jours au sprint 5. Pendant que la vélocité baissait, les stories allaient plus vite d'un bout à l'autre de la chaîne, et revenaient de moins en moins. Nous avions passé trois sprints à nous améliorer, et notre principal indicateur nous avait dit, chaque quinzaine, que nous ralentissions.

— La vélocité n'est pas morte aujourd'hui, a dit Julien. Elle est morte au sprint 2. Nous ne l'avions pas encore enterrée.

Restait le coût. Devant l'ART Leadership Team, à la fin de l'automne, j'avais annoncé de trois à quinze euros de modèle par story. La fourchette était juste pour les sprints 4 et 5. Elle ne l'était pas pour le sprint 2, où les quatre agents en parallèle avaient porté la médiane à vingt-sept euros. Mais ce n'était pas le vrai coût. Le vrai coût, l'agent l'avait trouvé en croisant les retouches avec le temps passé par chacun : une story retouchée coûtait en moyenne quatre heures et demie de travail humain, entre la relecture, le nouveau test, la question à Nadia et la nouvelle relecture. Le modèle coûtait le prix d'un sandwich. Ce qu'il coûtait vraiment, c'était le temps des gens quand il se trompait.

La décision a pris moins d'un quart d'heure. Pour la phase 2, nous n'estimerions plus en points. Nous suivrions quatre indicateurs, calculés chaque lundi à partir de ce que la passerelle faisait déjà remonter dans Jira, sans une ligne de saisie. Nadia a demandé qu'on écrive les règles avant les chiffres.

> **Tableau de bord de l'équipe** · tenu par Sylvie · calculé chaque lundi, sans saisie
>
> *Débit.* Stories terminées par semaine, scénarios verts en recette. Sprint 5 : huit.
>
> *Temps de traversée.* Du début du travail à la recette, en médiane. Sprint 2 : neuf jours. Sprint 5 : deux jours.
>
> *Taux de retouche.* Stories déclarées finies qui retournent en développement parce qu'elles ne faisaient pas ce qu'elles devaient faire. Sprint 2 : 41 %. Sprint 5 : 7 %.
>
> *Coût complet par story.* Les heures humaines, plus le modèle. Une retouche : quatre heures et demie de travail humain en moyenne.
>
> *Phase 2, itération 2 :* quatre stories terminées, aucune retouche. Trop peu pour conclure.
>
> *Règles.* Aucun objectif sur le débit. Aucun chiffre ne sert à juger une personne. Chaque chiffre a une définition écrite.

— Pourquoi aucun objectif sur le débit ? a demandé Antoine. Chez nous, c'est le premier qu'on fixe.

— Parce que le jour où on nous demandera dix stories par semaine, nous en livrerons dix, a dit Nadia. Plus petites, ou plus fausses. Nous l'avons déjà fait une fois. C'était le sprint 2.

Isabelle Delattre est arrivée à 16 heures, comme convenu, avec le tableur du train. Elle a regardé les trois courbes un long moment.

— Le train additionne des points pour planifier, a-t-elle dit. Si vous n'en avez plus, comment je planifie avec vous ?

— Avec notre débit, en stories, et une fourchette, a dit Sylvie. Six à huit par semaine. C'est ce que je vous avais écrit au crayon en janvier, sous les points.

Isabelle a souri, pour la première fois de la journée.

— Mon tableur et moi, nous avions dit que nous en reparlerions. Je vous note en stories jusqu'à l'Inspect & Adapt. Si la fourchette tient, je la proposerai aux autres équipes. Si elle ne tient pas, vous reviendrez aux points.

## Mercredi 4 février, 16 heures

Quentin Desmet est revenu le mercredi avec trois pages. Il avait pris nos quatre indicateurs, les données qu'Horizon publiait dans Jira et les budgets des deux programmes. Il n'avait pas fait ce que je craignais : il n'avait pas divisé un budget par un autre.

— Je ne compare que ce qui se compare, a-t-il dit en posant les feuilles devant Claire et moi. Horizon construit lui aussi un parcours de déclaration pour les dégâts des eaux et les vols, du côté des gestionnaires. Deux équipes, quatorze mois de spécifications et de développement, mise en production prévue en octobre. Vous : huit personnes, dix-huit semaines en comptant le sprint 0 et l'homologation, et c'est en production. Rapporté à ce qui fonctionne réellement, le pilote a coûté à peu près cinq fois moins.

Il a laissé passer un temps.

— Mais je ne présenterai pas ce chiffre seul. Il y a trois raisons à l'écart, et l'agent n'est pas la première.

Il les avait écrites sur la deuxième page. Le pilote s'appuyait sur trente ans de COBOL qu'Horizon devait remplacer : ce n'était pas le même métier. Le pilote était une équipe de huit personnes qui décidaient dans la même pièce, quand Horizon passait par un contrat, des demandes de changement et deux comités par décision. Et le pilote avait profité d'Horizon : le document de quatre cents pages versé dans le wiki, Antoine, la vérification des contrats de l'Artois.

— J'ai essayé d'isoler la part de l'agent avec Thomas, a dit Quentin. Si je l'enlève et que je garde tout le reste, l'équipe réduite, le mainframe, les décisions prises sur place, j'estime que vous auriez mis à peu près deux fois plus de temps, pour un coût un peu plus élevé. L'agent explique peut-être un tiers de l'écart. Les deux autres tiers sont des choix d'organisation qu'Horizon aurait pu faire sans lui.

Il avait aussi tout compté, y compris ce que nous n'aurions pas montré : les trois jours d'équipe perdus après le Mercredi noir et le coût de la notification à la CNIL, les cent quatre dossiers que Nadia avait portés en plus de son travail, les soirées de Sylvie, le mois d'homologation, les retouches du sprint 2 converties en heures.

Claire a lu les trois pages deux fois. Puis elle a pris son téléphone.

— Laurent doit les voir avant jeudi, a-t-elle dit. Pas de surprise au comité. C'est la règle de l'instance commune, et c'est la sienne autant que la mienne.

Laurent Dewitte est monté à 17 heures. Il a lu les trois pages en silence, son stylo-plume à la main, sans rien écrire. Quand il a eu fini, il a reposé les feuilles bien à plat sur la table.

— C'est juste, a-t-il dit. Mais le chiffre de cinq va circuler, quoi que vous écriviez autour. Dans un mois, on dira dans les couloirs qu'Horizon coûte cinq fois trop cher.

— Je l'écrirai avec ses trois raisons sur la même ligne, a dit Quentin.

— Ça ne suffira pas. Mais c'est honnête.

Il a repris la troisième page, celle des retouches. Quentin y avait mis côte à côte notre taux, sprint par sprint, et celui d'Horizon, calculé avec la même définition sur les anomalies rouvertes de ses deux équipes : trente-cinq pour cent, stable depuis un an et demi.

— Ce n'est pas le cinq qui me gêne, a dit Dewitte. C'est celui-là. Nous sommes à votre sprint 2 depuis deux ans, et personne ne nous l'avait montré.

Il a rangé son stylo.

— Je vais demander un mois au comité. Pas pour me défendre. Pour proposer ce qu'Horizon doit garder, et ce qu'il doit cesser de faire.

## Jeudi 5 février, 10 heures

Le comité se réunissait dans la salle du conseil, au dernier étage, celle où Claire avait promis, à l'automne, une productivité multipliée par trois. Catherine Duhamel présidait. Hervé Delcourt était à sa droite, Philippe Wattebled et Laurent Dewitte face à face, Quentin Desmet en bout de table. J'étais assis contre le mur, derrière Claire.

Claire a présenté les trois premières semaines de production sur une seule page, comme en novembre. Mille sept cent quarante déclarations reçues par le portail. Un tiers des dégâts des eaux et des vols de la période, le reste arrivant toujours par téléphone, par courrier ou en agence. Une déclaration sur cinq faite la nuit, quand le système des contrats dormait. Aucune déclaration perdue. Un incident, l'adresse du risque, trois dossiers corrigés à la main avant midi. Un jour et demi en moyenne entre la déclaration et la première action du gestionnaire, contre quatre jours par téléphone, parce que les photos arrivaient avec la déclaration.

— Le centre de relation reçoit moins d'appels de déclaration, a-t-elle ajouté. Mais je ne vous donne pas de chiffre : l'hiver dernier était plus pluvieux, et je ne sais pas encore distinguer l'effet du portail de celui de la météo. Je vous le donnerai en avril, sur trois mois.

Catherine Duhamel a hoché la tête.

— Et tous les sinistres, pour l'été ?

C'était la question que Claire attendait. Elle n'a pas regardé ses notes.

— Je ne vous donnerai pas de date aujourd'hui. À la fin du mois, après deux itérations mesurées, je vous donnerai une fourchette, et la probabilité que nous la tenions. À l'automne, je vous ai promis une productivité multipliée par trois et tous les sinistres avant l'été. Personne ne l'avait estimé. Je ne recommencerai pas.

— Avant, vous me donniez des dates, a dit Catherine Duhamel. Maintenant, vous me donnez des probabilités.

— Avant, je vous donnais des espoirs.

Il y a eu un silence, puis la directrice générale a souri, très légèrement, et elle a donné la parole à Quentin.

Il a présenté ses trois pages en dix minutes, avec le chiffre de cinq et ses trois raisons sur la même ligne, comme il l'avait promis. Quand il a dit qu'un tiers de l'écart tenait à l'agent et deux tiers à la manière de travailler, Hervé Delcourt a posé son stylo.

— Donc la question n'est pas de donner l'outil à tout le monde, a dit Catherine Duhamel.

— Non, a dit Hervé Delcourt. Mais il faudra le donner aussi. Avec le socle, depuis le premier janvier, c'est possible. Ce qui ne se distribue pas, c'est le reste.

Laurent Dewitte a demandé la parole. Il n'a pas contesté un seul chiffre. Il a parlé de la troisième page, celle des retouches, et il a dit devant le comité ce qu'il nous avait dit la veille : qu'Horizon était à notre sprint 2 depuis deux ans. Puis il a demandé un mois pour proposer ce qu'Horizon devait garder, et ce qu'il devait cesser de faire.

— Un mois, a dit Catherine Duhamel. Et vous viendrez avec Claire.

La séance a duré cinquante minutes. Personne n'y a prononcé le mot « vélocité ».

Dans le couloir, Claire s'est arrêtée devant la fenêtre, celle d'où l'on voyait le beffroi.

— Vous savez ce qui m'a le plus coûté, ce matin ? m'a-t-elle demandé. Ne pas dire « avant l'été ». Je l'avais sur le bout de la langue.

Le lendemain s'achevait la deuxième itération de la phase 2. La suivante serait la première menée de bout en bout avec la méthode, toute l'équipe enfin réunie du même côté du tableau. Et pour la première fois depuis septembre, personne ne savait combien de points elle vaudrait.

## Le carnet de Thomas

**Ce qui s'est passé.** Le contrôle de gestion a demandé la vélocité de l'équipe pour la comparer à celle d'Horizon. En reconstituant l'histoire de chaque story à partir de Jira et de GitHub, puis en la vérifiant à la main sur un échantillon, l'équipe a découvert que sa vélocité avait culminé au sprint 2, au moment exact où son taux de retouche culminait aussi. Pendant les trois sprints suivants, l'indicateur avait annoncé un ralentissement alors que l'équipe s'améliorait. Elle a abandonné les points pour la phase 2 et les a remplacés par quatre indicateurs définis par écrit et calculés sans saisie : débit, temps de traversée, taux de retouche, coût complet par story. Le coût du modèle s'est révélé négligeable à côté du temps humain que coûtait chaque erreur. Le contrôle de gestion a comparé la phase 1 à Horizon sur un périmètre comparable et n'a attribué à l'agent qu'un tiers de l'écart. Devant le comité, la sponsor a refusé de donner une date pour la phase 2 avant d'avoir mesuré deux itérations.

**La leçon.** La vélocité mesure ce qu'une équipe estime avoir fait, pas ce qui fonctionne. Quand le code ne coûte presque plus rien, elle récompense le volume au moment même où le volume produit des retouches. Mesurez plutôt le flux : combien de stories arrivent réellement au bout, en combien de temps, et combien en reviennent. Écrivez la définition de chaque indicateur avant de le calculer, vérifiez à la main ce que l'agent a reconstitué, et ne fixez jamais d'objectif sur le débit : une équipe sait toujours produire le chiffre qu'on lui demande. Le vrai coût d'un agent n'est pas sur la facture du modèle, il est dans les heures que les humains passent à reprendre ce qu'il a mal fait. Enfin, quand on compare deux façons de travailler, séparez la part de l'outil de celle de l'organisation : c'est souvent la seconde qui prèse le plus.

**Trois questions à poser à votre équipe**

1. Notre indicateur principal a-t-il déjà annoncé une bonne nouvelle au moment où nous allions mal ?
2. Combien d'heures humaines coûte, chez nous, une story qui revient après avoir été déclarée finie ?
3. Dans nos gains, quelle part revient à l'outil, et quelle part à notre façon de nous organiser ?

**Pour aller plus loin.** Manuel, chapitres M13 (bonnes pratiques : mesurer le flux et le taux de retouche plutôt que la vélocité) et M14 (dépannage et coûts : rattacher la consommation du modèle à chaque story, lire la facture).
