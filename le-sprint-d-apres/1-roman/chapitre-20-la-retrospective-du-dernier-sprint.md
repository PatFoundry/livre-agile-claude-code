# Chapitre 20 — La rétrospective du dernier sprint

## Vendredi, 11 h 45

La dernière story de la phase 1 n'avait rien de spectaculaire. Elle affichait à l'assuré, sur la page à trois états, la date à laquelle son dossier était passé de *reçue* à *en cours*. Nadia l'avait gardée au-dessus du ruban rouge parce que Martine recevait chaque semaine des appels d'assurés qui voulaient savoir une seule chose : si quelqu'un avait regardé leur dossier.

Émilie avait écrit trois scénarios. L'agent avait codé la story en vingt minutes. Sofiane avait relu, parce qu'elle était verte. Les tests de la chaîne étaient passés, y compris celui qui cherchait des données personnelles dans les journaux.

À 11 h 45, Julien a approuvé la demande de fusion. Il l'a fait sans cérémonie, puis il s'est ravisé et il a ajouté un commentaire, le premier commentaire inutile de toute sa carrière, je crois.

*Dernière de la phase 1. Merci à tous.*

Personne n'a applaudi. Sofiane a fusionné, la chaîne d'intégration a déployé la version en recette, et l'écran de Sylvie s'est mis à jour tout seul. La courbe des stories terminées a touché le trait horizontal. Seize sur seize.

Sylvie a fermé la version *Mise en production, phase 1* dans Jira. Elle l'a fait avec une solennité que je ne lui connaissais pas, en lisant à voix haute le message de confirmation, comme un greffier.

— Version close. Seize tickets terminés. Zéro en cours.

Puis elle a ajouté, sans lever les yeux :

— C'est rare que je ferme une version à la date prévue.

Le lundi suivant, le portail entrerait en homologation pour un mois. Les gestionnaires de Philippe Wattebled le testeraient sur des dossiers réels rejoués. L'équipe de production mesurerait sa tenue en charge. Un cabinet spécialisé vérifierait son accessibilité. Les tests de résilience exigés par DORA couperaient le système des contrats en pleine journée pour voir si les déclarations attendaient sagement leur tour. Tout ce que Laurent Dewitte avait demandé à la première revue, et que j'avais rangé dans le backlog avec un peu trop d'assurance.

Mais le code de la phase 1 ne bougerait plus que pour corriger ce que l'homologation trouverait. Les développements étaient finis.

Martine est montée à midi avec une boîte de merveilleux de chez le pâtissier de la rue de la Monnaie. Elle les a posés sur la table de la salle Lys, à côté de la carte des stories, et elle a regardé le mur longtemps.

— La dame de Roubaix, a-t-elle dit. Si elle avait eu ça en février, elle aurait déclaré à 22 heures, le soir même. Et le lundi, j'aurais su qu'elle existait.

Elle est repartie sans attendre de réponse. Nadia a regardé la porte se refermer, puis elle a pris un merveilleux et elle l'a mangé en silence, ce qui était, chez elle, la forme la plus aboutie de l'émotion.

## Vendredi, 14 heures

Pour la rétrospective de fin de phase, j'avais réservé la salle Escaut pour tout l'après-midi, et j'avais invité deux personnes qui n'étaient pas dans l'équipe et qui en faisaient pourtant partie : Gérard et Mathilde. Gérard est arrivé avec ses lunettes de lecture et un cahier à spirale neuf. Mathilde avec sa plante grasse, qu'elle avait décidé de ne plus laisser seule le vendredi.

La veille au soir, j'avais collé sur le grand mur une frise de treize semaines, faite de feuilles de paperboard mises bout à bout. J'y avais épinglé les photos des tableaux de toutes nos rétrospectives, de tous nos ateliers, de toutes nos crises. Le mur racontait la phase 1 de gauche à droite, et il fallait reculer jusqu'à la fenêtre pour la voir en entier.

Nous avons commencé comme toujours, par la phrase de Norm Kerth et par la météo. Puis par la question que nous avions ajoutée depuis la rétrospective sous tension : chacun disait lui-même s'il avait travaillé le soir ou le week-end pendant le sprint. Nadia a dit non, et elle a souri en le disant. Émilie et Julien ont dit non. Sofiane a hésité.

— Un soir. Mais c'était pour BMAD, chez moi, sur la cave à vin de mon père. Ça compte ?

— Ça compte, a dit Julien. Mais ça se pardonne.

J'ai donné à chacun trois post-it et une consigne : coller sur la frise le moment où il avait le plus appris, et une seule phrase pour dire quoi.

Nadia a collé le sien en semaine 10, sur la franchise et l'avenant. *Les règles ne sont écrites nulle part en entier. Il faut les écrire avant.*

Émilie en semaine 9, sur le vélo sans facture. *Mon travail servait, il arrivait juste trop tard.*

Sofiane en semaine 7, sur les quarante demandes. *Le code n'a jamais été le problème.*

Julien a hésité entre le Mercredi noir et autre chose. Il a choisi autre chose : le jeudi où nous avions tout arrêté. *On peut s'arrêter. Personne ne meurt.*

Mathilde a collé le sien en semaine 12, sur la première story qu'elle avait préparée avec l'équipe, celle des photos. *La sécurité coûte moins cher avant qu'après.*

Gérard a mis longtemps. Il a fini par coller son post-it le plus à droite possible, sur la veille. *Le jour où la machine a trouvé ce que je ne savais pas.*

J'ai collé le mien en semaine 5, sur une photo du parking du personnel que personne d'autre n'aurait comprise. *Frapper à la vitre.*

Julien l'a lu. Il n'a rien dit, mais il a posé la main sur mon épaule une seconde en passant.

Puis nous avons fait la liste de ce que nous gardions. Elle était longue, et chaque ligne avait une histoire sur la frise. La limite de six demandes en revue. Les étiquettes de risque et la relecture du rouge par quelqu'un qui connaît le système. Les trois amis, devenus quatre pour les stories rouges. Les scénarios écrits avant le code et verrouillés pour l'agent. Le dossier des règles. Le socle. Le wiki. Le registre de la dette. La ligne rouge quand le temps manque. Le parking des bonnes idées. La météo, et la question des soirs et des week-ends.

— Tout ça, on l'a inventé en cours de route, a dit Émilie en relisant la liste. Aucune de ces règles n'existait le premier jour.

— Et chacune nous a coûté quelque chose, a dit Julien. Une nuit, un incident, une semaine d'arrêt.

Il ne se plaignait pas. Il faisait l'inventaire, comme on compte ce qu'on emporte avant un déménagement.

## Vendredi, 15 h 30

Après la pause, j'ai écrit au tableau le cadre que le train nous avait fixé la veille, mot pour mot. Chaque fonctionnalité renvoie à une spécification versionnée dans le dépôt. Chaque règle de gestion a sa source et ses validateurs. Les formats d'échange avec les autres équipes sont des contrats signés des deux côtés. En dessous, j'ai écrit une seule question.

*Comment ?*

Puis j'ai décollé du parking la première ligne, celle de Sofiane, et je la lui ai tendue.

Il a présenté BMAD en vingt minutes, sans démonstration, au tableau. Il avait compris, je crois, que l'enthousiasme ne convaincrait personne dans cette salle. Il a dessiné les quatre phases de la méthode. L'analyse, où un agent analyste interroge le métier et rédige un brief. La planification, où un agent chef de produit en tire un document d'exigences, fonctionnelles et non fonctionnelles. La conception, où un agent architecte écrit l'architecture, avant qu'on découpe le travail en epics et en stories autoportantes. Puis l'implémentation, story par story, avec un agent qui prépare chaque story, un autre qui la code, un autre qui la relit. Tout ce que produisaient ces agents était écrit en fichiers, dans le dépôt, relu et validé par des humains avant de passer à l'étape suivante.

— Et quand le code est faux, a-t-il conclu, on ne corrige pas le code. On corrige la spécification, puis on refait la story.

Personne n'a applaudi. Julien a pris un feutre d'une autre couleur et il a tracé deux colonnes à côté du schéma. À gauche, ce que la méthode demandait. À droite, ce que nous avions déjà.

Le document d'exigences ? Nous avions le dossier des règles, avec la franchise, les avenants, la date d'un vol. Les critères d'acceptation ? Les scénarios d'Émilie, écrits avant le code et verrouillés. L'architecture ? Le wiki de Gérard pour l'existant, et le format d'échange signé avec Horizon. Les stories autoportantes ? Notre définition de « prête », avec ses neuf points, et la story fondation du sprint 2. Les agents spécialisés ? Nos skills, celle de Nadia pour préparer une story, celle d'Émilie pour les scénarios, celle des relectures.

Quand il a eu fini, la colonne de droite était presque aussi remplie que celle de gauche.

— On a fait les deux tiers du chemin sans le savoir, a dit Julien. Ce qui nous manque, c'est l'ordre. Et un seul endroit où tout se tient.

Les objections sont venues ensuite, et c'est ce que j'attendais d'eux.

Julien a parlé le premier.

— On ne jette rien de ce qui marche. Si la méthode veut ses propres fichiers, on les relie aux nôtres. Les règles restent dans le dossier des règles. Le wiki reste le wiki. On adapte la méthode à nous, pas l'inverse.

Émilie a posé la question qui l'inquiétait depuis la veille.

— Si un agent écrit les exigences et qu'un autre propose les tests, qui garantit qu'ils sont justes ? On a déjà vu ce que donne un agent qui écrit le code et les tests qui le vérifient.

— Moi, a dit Nadia. Chaque exigence passe par moi, ou par la gestionnaire des incendies quand elle arrivera. Et les scénarios restent les tiens. L'agent peut en proposer. C'est toi qui décides, et le verrou reste en place.

Gérard a posé la question qu'il avait déjà posée la veille au soir, sur le pas de la porte.

— Qui tient le cahier à jour ?

— Tout le monde, a dit Sofiane, et Julien a secoué la tête.

— Tout le monde, c'est personne. Chaque document a un propriétaire, comme nos skills. On le modifie par une demande de fusion, que le propriétaire approuve. Et on se donne une règle simple : on ne touche jamais au code d'une story sans que sa spécification dise déjà ce qu'on va faire. Tant que la spécification est le seul chemin vers le code, elle ne pourra pas mourir.

Gérard a réfléchi, puis il a noté quelque chose dans son cahier neuf. Je n'ai jamais su quoi.

Mathilde a parlé en dernier.

— Les fichiers de cette méthode, ce sont des instructions écrites par d'autres, que nos agents vont suivre à la lettre. Je les lirai avant qu'ils entrent dans le dépôt, et on figera la version. Le socle s'applique. Et le document d'exigences contiendra les données personnelles manipulées et mes trois questions, comme exigences à part entière.

Personne ne s'y est opposé.

Restait à décider comment essayer. J'ai rappelé la règle que nous nous étions donnée au début de la phase 1 : on ne change pas de méthode pendant une livraison. Le portail partait en homologation lundi, et pendant un mois, son code ne bougerait que pour des corrections. La nouvelle méthode ne toucherait pas la phase 1.

C'est Nadia qui a trouvé le terrain d'essai. Elle est allée au mur, sous le ruban rouge, et elle a décollé un post-it qu'elle avait elle-même placé juste en dessous de la ligne, à peine deux semaines plus tôt, pour qu'il soit le premier à remonter.

*Déclarer pour le compte d'un proche.*

— Celle-là, a-t-elle dit. On la connaît par cœur, Philippe y tient, et elle est assez petite pour qu'on voie la différence.

Nous avons décidé ensemble, en une demi-heure, ce qui me reste aujourd'hui comme la meilleure décision de la phase 1. Pendant l'homologation, Sofiane, Nadia et Émilie feraient passer cette story par toute la chaîne de la méthode, du brief au code, sur une branche à part, qui ne serait fusionnée qu'après la mise en production. Une heure par jour chacun, pas plus. En même temps commencerait l'analyse de la phase 2. Nous mesurerions la même chose qu'en phase 1 : le temps de préparation, les questions posées par l'agent, les retouches après relecture, les anomalies trouvées par Émilie. Et nous nous donnions une condition d'arrêt : si, à la fin du premier incrément, les spécifications n'étaient plus à jour, ou si elles ralentissaient l'équipe sans réduire les anomalies, nous arrêterions, et nous le dirions au train.

— Et Jira ? a demandé Julien. Si les stories naissent dans le dépôt, Sylvie et Sandrine vont vouloir savoir où est la vérité.

— On en parlera avec elles, ai-je dit. Ce n'est pas une décision qu'on prend sans ceux qui la vivront.

J'ai noté la question dans un coin du tableau. Je savais qu'elle reviendrait.

À 17 h 30, trois post-it avaient quitté le parking des bonnes idées : la méthode dirigée par les spécifications, les règles écrites avant les stories, les données de test artificielles, qu'Émilie préparerait pour la phase 2. Il en restait deux. La réorganisation du code de Julien, rangée dans la future architecture. Et les mesures de flux de Sylvie, que nous porterions au train.

## Vendredi, 19 heures

C'est Julien qui a choisi l'endroit : un estaminet du Vieux-Lille, derrière la Grand-Place, avec des tables en bois sombre, des jeux de bistrot accrochés au mur et une carte écrite à la craie. Il y venait avec Gérard depuis vingt ans, le jour de chaque mise en production. Il a dit que la fin des développements comptait, cette fois.

Nous étions huit autour de deux tables rapprochées. L'équipe, Gérard, Mathilde, et Sylvie, que Nadia était allée chercher à son bureau et qui avait accepté à condition de partir à 20 heures. Elle est partie à 22 heures.

Il y avait du welsh, de la carbonade, du potjevleesch pour Gérard, qui en commandait depuis 1985, et des bières dont Sofiane connaissait toutes les brasseries. Pendant la première heure, personne n'a parlé du projet. On a parlé de la petite-fille de Gérard, du judo de la fille de Julien, de la ville natale d'Émilie, que je découvrais après trois mois à travailler avec elle. Sofiane a raconté la cave à vin de son père, et le jour où l'agent analyste lui avait demandé si un rosé de Provence devait être rangé avec les blancs ou avec les rouges.

Claire est arrivée vers 20 h 30, en manteau, d'un dîner qu'elle avait écourté. Elle a accepté une bière et refusé une chaise. Elle a levé son verre, et tout le monde s'est tu, parce qu'on attendait un discours.

— Je ne vais rien promettre, a-t-elle dit. Je n'ai plus le droit, il paraît.

Il y a eu un rire autour des deux tables, et c'était le premier rire franc que je l'entendais provoquer.

— Je voulais seulement vous dire merci. Pour le portail, bien sûr. Mais surtout pour la page. La seule page.

Elle a bu une gorgée, elle a serré la main de Gérard en lui demandant des nouvelles de sa petite-fille, et elle est repartie dix minutes plus tard. En sortant, elle m'a fait signe de la suivre jusqu'à la porte.

— Lundi, l'homologation, a-t-elle dit. Et la phase 2 qui démarre en même temps. Deux fronts. Vous êtes sûr qu'ils tiendront ?

— Non, ai-je dit. Mais ils savent maintenant s'arrêter quand ils ne tiennent plus. C'est plus important.

Elle a hoché la tête et elle est partie dans le froid de décembre, vers la place du Théâtre.

Quand je suis revenu à la table, Gérard racontait à Sofiane comment on mettait en production en 1988, un samedi soir, avec des bandes magnétiques qu'on transportait à la main d'un étage à l'autre. Sofiane l'écoutait comme on écoute un récit d'expédition polaire. À un moment, Gérard s'est arrêté au milieu d'une phrase.

— Tu mettras ça dans le wiki ?

— Non, a dit Sofiane. Ça, je le garde pour moi.

Gérard a eu l'air plus content de cette réponse que de toutes les pages relues de la semaine.

Je suis rentré à pied, vers 23 heures, par les rues pavées qui descendent vers la Deûle. J'ai repensé à la règle que j'avais imposée dix jours plus tôt et qui avait tant coûté à Sofiane : on ne change pas de méthode pendant une livraison. Nous venions de changer de méthode, et c'était la bonne décision. Pas parce que l'idée était nouvelle. Parce qu'elle arrivait au bon moment, pour de bonnes raisons, et qu'elle sortait de ce que nous avions vécu plutôt que d'une démonstration.

Nous n'avions pas changé de méthode pendant la phase 1. Nous en changions entre les deux phases. Toute la différence était là.

## Le carnet de Thomas

**Ce qui s'est passé.** La dernière story de la phase 1 a été fusionnée le vendredi midi, et le portail est entré en homologation pour un mois. La rétrospective de fin de phase a rassemblé l'équipe et ceux qui en faisaient partie sans y figurer. Elle a d'abord fait l'inventaire de ce que chacun avait appris et de ce que l'équipe gardait : chaque pratique avait été inventée en cours de route, souvent à la suite d'un incident. Puis elle a confronté la méthode BMAD à ce qui existait déjà. Les deux tiers de ce que la méthode demandait étaient là, sous d'autres noms. Il manquait l'ordre et un endroit unique où tout se tient. L'équipe a décidé d'adapter la méthode à ses artefacts plutôt que l'inverse, de donner un propriétaire à chaque document, de faire relire les fichiers de la méthode par la sécurité, et de l'essayer pendant l'homologation sur une seule story, sur une branche à part, avec des mesures et une condition d'arrêt.

**La leçon.** Changez de méthode entre deux livraisons, jamais pendant. La rétrospective de fin de phase est le bon moment, parce qu'on y dispose de tout ce qu'on a vécu. Avant d'adopter une méthode, faites le rapprochement entre ce qu'elle demande et ce que vous avez déjà : vous en pratiquez souvent une bonne partie sans le savoir, et ce qui marche ne doit pas être jeté. Une spécification ne survit que si elle a un propriétaire et si elle reste le seul chemin vers le code. Les instructions d'une méthode tierce sont du code que vos agents exécuteront : relisez-les et figez leur version. Enfin, essayez petit, sur un sujet connu, en mesurant les mêmes choses qu'avant, avec une condition d'arrêt écrite d'avance.

**Trois questions à poser à votre équipe**

1. Qu'avons-nous inventé pendant cette phase que nous voulons absolument garder ?
2. Quelle part de la méthode que nous envisageons pratiquons-nous déjà, sous un autre nom ?
3. À quelle condition arrêterons-nous l'essai, et qui le dira ?

**Pour aller plus loin.** Manuel, chapitres M9 (installer et configurer BMAD : relier la méthode aux artefacts existants, figer sa version) et M13 (bonnes pratiques : conduire une rétrospective de fin de phase).
