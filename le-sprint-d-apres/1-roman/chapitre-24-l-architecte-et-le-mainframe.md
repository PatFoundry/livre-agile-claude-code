# Chapitre 24 — L'architecte et le mainframe

## Lundi 19 janvier, 9 heures

Gérard est arrivé à 8 h 55, avec un sac de toile de la médiathèque de Roubaix. Dedans, il y avait ses huit cahiers, ceux dont le wiki avait tiré l'essentiel en novembre. Il les a posés sur la table de la salle Scarpe, dans l'ordre, du plus ancien au plus récent.

— Vous m'avez dit d'apporter mes cahiers, a-t-il dit à Julien. Je ne sais pas à quoi ils serviront. Tout ce qu'il y a dedans est déjà dans votre wiki.

— Tout ce que vous y avez écrit, a dit Julien. Pas tout ce que vous savez.

C'était la troisième étape de la méthode : l'agent architecte devait dire comment le portail ferait ce que le document d'exigences demandait. Julien en était le propriétaire, et il avait pris sa première décision le vendredi soir, avant même d'ouvrir une session : l'agent lirait le wiki d'abord, les exigences ensuite.

— S'il lit d'abord les exigences, il dessine le portail idéal, puis il découvre le mainframe et il bricole, m'avait-il expliqué. S'il lit d'abord le mainframe, il dessine le portail possible.

Antoine Lambrecht était là, avec Mathilde et Sofiane. Didier Vermeersch avait promis de passer en fin de matinée. L'agent a lu le wiki pendant vingt minutes, puis le document d'exigences, puis les décisions déjà prises pendant la phase 1. Une heure plus tard, il proposait un document d'architecture de vingt pages : les composants du portail, les échanges avec l'espace adhérent et le centre de relation, le mécanisme unique pour déclarer au nom d'un autre, la quarantaine des photos, le mode de nuit hérité de la phase 1.

Et, au milieu, une proposition en gras. *Copier chaque nuit le système des contrats dans une base de données moderne, afin de découpler le portail du mainframe, de réduire la consommation facturée et de faciliter les évolutions.*

Sur le papier, c'était séduisant. Sofiane a hoché la tête. Antoine, lui, a ri doucement.

— Horizon l'a proposé aussi, en 2023. Le chantier a duré dix-huit mois, et il a été arrêté avant d'avoir copié la moitié des fichiers.

— Une copie de la nuit, c'est une copie d'hier, a dit Gérard. Un avenant saisi ce matin n'y est pas. Votre règle F2 serait fausse jusqu'au lendemain.

— Et ce serait une copie de plus de toutes les données personnelles de nos assurés, a ajouté Mathilde. Nous avons passé trois jours, en décembre, à corriger le script qui anonymisait la dernière.

Julien n'a pas discuté. Il a demandé à l'agent de rédiger la décision, et il en a imposé la forme, qui servirait pour toutes les suivantes : le contexte, les options envisagées, le choix, ce qu'il coûtait, et un nom. L'agent pouvait rédiger les quatre premières rubriques. La cinquième, jamais. *Décision d'architecture DA-02 : pas de copie du système des contrats. Le portail lit le contrat une fois, au début de la déclaration, et le garde jusqu'à la fin, comme depuis le test de montée en charge de décembre.* En face, Julien a écrit son nom, et en dessous, ceux de Gérard, de Mathilde et d'Antoine, comme relecteurs.

L'agent a repris son document autour de cette décision. Puis il a fait ce que l'analyste avait fait avant lui : il a dressé la liste de ce que le wiki ne disait pas. Quatorze questions sur le système des contrats, ses transactions, ses champs, ses horaires. Gérard a répondu à onze sans ouvrir un cahier. Pour les trois autres, il a dit : *il faudrait vérifier*, et il est allé chercher le cahier de 2003.

Je me suis dit, ce soir-là, que nous avions tout prévu. Je ne savais pas encore que la question qui allait compter ne figurait pas parmi les quatorze.

## Mercredi 21 janvier, 10 h 15

Le mercredi, à 10 h 15, Martine a appelé Sofiane, qui était de garde cette semaine-là. Elle avait retrouvé son poste au service des sinistres après les formations, et elle traitait, comme ses collègues, les déclarations arrivées par le portail.

— J'ai un vol à Wimereux, a-t-elle dit. Une maison de vacances, cambriolée pendant l'hiver, découverte par le voisin. Le portail me dit que le vol a eu lieu à Lille, rue Solférino. C'est l'adresse où l'assuré habite. Ce n'est pas celle de la maison cambriolée.

Sofiane a ouvert la déclaration. Le lieu du sinistre était prérempli : le portail proposait une adresse, et l'assuré pouvait la modifier. Il ne l'avait pas modifiée. Il avait sans doute pensé que le portail savait mieux que lui.

La première règle du tableau s'appliquait. Sofiane a appelé Julien, qui travaillait avec l'agent architecte dans la salle Scarpe, et Julien est descendu dans la minute. Il a laissé la session telle quelle, et personne n'a demandé à l'agent de continuer seul : sans Julien, il n'y avait personne pour décider. L'architecture a attendu un jour et demi.

Il a fallu dix minutes à l'agent, dans une autre session, pour trouver d'où venait l'adresse : le portail la prenait dans l'en-tête du contrat, tel que le renvoyait la transaction de 1997. Julien a appelé Gérard, qui est descendu à son tour, un cahier sous le bras.

— L'adresse en tête du contrat, c'est l'adresse de correspondance, a dit Gérard. Celle où on envoie le courrier. L'adresse du risque, celle du logement assuré, est dans le segment des garanties. Pour la plupart des gens, c'est la même. Pour une résidence secondaire, un propriétaire qui loue, une vieille dame dont le fils reçoit le courrier, ce n'est pas la même.

— Vous le saviez ? a demandé Julien.

Gérard a mis un moment à répondre.

— Je le sais depuis 1997. Je ne l'ai jamais écrit. Personne ne me l'a jamais demandé. Pour moi, c'était évident.

Martine a vérifié ses deux cents dossiers de recette pendant ce temps. Pas une résidence secondaire, pas un logement loué. Elle les avait choisis pour couvrir tout ce qu'elle avait vu passer en vingt-deux ans de dégâts des eaux et de vols, chez des gens qui habitaient leur maison.

L'agent a comparé, pour les quatre cent douze déclarations arrivées depuis le 13, l'adresse de l'en-tête et celle du risque. Elles différaient dans neuf cas. Six assurés avaient corrigé l'adresse eux-mêmes. Trois ne l'avaient pas fait : la maison de Wimereux, un dégât des eaux dans un appartement que son propriétaire louait, et un vol chez une dame de quatre-vingt-six ans dont le fils recevait le courrier à Tourcoing. Martine a corrigé les trois dossiers à la main avant midi. Aucun expert n'avait encore été missionné à la mauvaise adresse.

La correction tenait en peu de lignes : prendre l'adresse dans le segment des garanties, et, s'il y en avait plusieurs, demander à l'assuré laquelle. L'agent l'a écrite avec ses tests. Comme elle touchait à la lecture du système des contrats, elle était classée rouge. Julien et Antoine l'ont relue ensemble, l'après-midi, et Émilie a ajouté trois scénarios, un par cas réel.

— Chez Horizon, on a mis trois mois à découvrir la même chose, a dit Antoine. Sur les nouveaux écrans de gestion, l'adresse du risque est dans un onglet à part. Je n'avais jamais compris pourquoi.

Personne n'a corrigé seul, et personne n'a déployé le soir. Didier Vermeersch a passé la correction en changement standard le jeudi à 7 heures.

J'ai rédigé la fiche d'incident l'après-midi, sans chercher de coupable, comme depuis le Mercredi noir. La cause n'était ni Gérard, ni l'agent, ni Martine. C'était un savoir évident pour celui qui le détenait, et invisible pour tous les autres. Puis j'ai rouvert le document d'architecture du lundi, celui que nous trouvions complet. Pour envoyer l'expert après un incendie, il prévoyait de prendre l'adresse en tête du contrat.

## Jeudi 22 janvier, 14 heures

Le jeudi, Julien est revenu dans la salle Scarpe avec une idée qu'il avait eue dans la nuit, et qu'il a résumée en une phrase avant même de s'asseoir.

— On ne demande plus à Gérard ce que fait le système des contrats. On le demande au système.

C'était une vieille technique, bien plus ancienne que les agents, qu'on enseigne à ceux qui doivent toucher à du code qu'ils n'ont pas écrit : les tests de caractérisation. On ne teste pas ce que le programme devrait faire. On enregistre ce qu'il fait vraiment, sur des cas choisis, et on s'en sert comme d'un filet. Julien voulait en écrire pour chaque transaction du système des contrats dont le portail se servirait, avant que l'agent architecte ne construise quoi que ce soit dessus.

— Il me faut des contrats, a-t-il dit à Gérard. Pas des contrats moyens. Les pires que vous connaissiez.

Gérard a ouvert ses cahiers. En une heure, il a dressé une liste de quarante contrats de la base de recette, anonymisée depuis décembre : des résidences secondaires, des propriétaires qui louaient, des contrats de l'ancienne Mutuelle de l'Artois avec leur numéro en 7, des contrats suspendus en *X*, des avenants saisis avec une date d'effet à venir, un contrat qui avait changé trois fois de formule en un an. Pour chacun, il a noté à la main ce que la transaction devait renvoyer, selon lui.

Mathilde a vérifié que les quarante contrats venaient bien de la copie anonymisée. Les adresses étaient fausses. Mais, comme l'a fait remarquer Sofiane, elles étaient fausses au bon endroit, et c'était tout ce qui comptait.

L'agent a écrit les tests dans l'après-midi : quarante cas, la réponse complète de la transaction enregistrée champ par champ. Puis il les a fait tourner sur l'environnement de recette, et il a comparé les réponses aux prédictions de Gérard.

Trente-sept correspondaient.

La première surprise venait des contrats de l'ancienne Artois. Leur adresse du risque tenait sur deux lignes au lieu de quatre, le code postal collé au nom de la commune. Gérard a froncé les sourcils, puis il a hoché la tête.

— La fusion de 1995. On avait gardé leur format pour ne pas réécrire leurs éditions. Je l'avais oublié.

La deuxième venait d'un contrat suspendu. Son segment des garanties revenait vide. Un programme pressé en aurait conclu que l'assuré n'avait plus aucune garantie, alors qu'un sinistre survenu avant la suspension restait couvert. Le portail ne refuserait rien : il enregistrerait la déclaration et la signalerait au gestionnaire, comme le voulait le brief.

La troisième venait d'un contrat d'agriculteur, à Bailleul. Il assurait trois bâtiments : la maison, une grange, un hangar. Trois adresses du risque dans le même contrat.

— Celui-là, je l'avais complètement oublié, a dit Gérard. Il ne doit pas y en avoir cinquante.

Didier les a fait compter en production le soir même. Il y en avait deux cent douze. Le document d'exigences n'en disait rien, puisque personne n'y avait pensé. Julien n'a pas tranché à la place de Nadia. Il lui a envoyé la question, avec le numéro du test qui l'avait révélée. Elle a répondu dans l'heure : l'assuré choisirait parmi les adresses de son contrat, et, si aucune ne correspondait, il pourrait en saisir une, signalée au gestionnaire. Une exigence de plus, avec une source qu'aucun document d'exigences n'avait jamais citée : *test de caractérisation n° 23.*

Gérard a relu les trois surprises une dernière fois.

— Trente-sept sur quarante, a-t-il dit. À mon âge, je prends.

Puis il a écrit lui-même quatre pages du wiki : les trois surprises, et une quatrième, intitulée *Adresse de correspondance et adresse du risque*, qui manquait depuis 1997. Il les a validées de son nom, comme le commentaire libre en décembre.

Julien a inscrit la décision DA-07 : aucune construction sur une transaction du système des contrats sans tests de caractérisation. Émilie l'a reportée dans sa stratégie de test, avec une règle de plus : les quarante tests tourneraient chaque nuit en recette. Le système des contrats évoluait encore, entre les mains d'une équipe que nous ne connaissions presque pas. Le jour où quelqu'un modifierait un programme de 1997, nous le saurions le lendemain matin.

## Vendredi 23 janvier, 17 heures

Le vendredi, le document d'architecture tenait en quatorze pages, six de moins que le premier jet du lundi. Il comptait neuf décisions, chacune avec son contexte, ses options, son choix, son coût et un nom. Trois documents l'accompagnaient, ceux du niveau entreprise : la sécurité, que Mathilde avait réécrite aux deux tiers ; l'exploitation, que Julien et Didier avaient ramenée à six pages ; la stratégie de test, où Émilie avait ajouté un chapitre que la méthode ne prévoyait pas, sur les tests de caractérisation.

La décision que nous relisions le plus souvent était la quatrième.

> **Décision d'architecture DA-04 — Adresse du risque** · propriétaire : Julien Morel · 22 janvier
>
> *Contexte.* La lecture du contrat renvoie deux adresses : en tête, l'adresse de correspondance ; dans le segment des garanties, l'adresse du ou des risques assurés. Le portail prenait la première. Incident du 21 janvier : trois déclarations sur quatre cent douze.
>
> *Options.* 1. Garder l'adresse de correspondance et la faire confirmer. 2. Prendre l'adresse du risque ; s'il y en a plusieurs, faire choisir l'assuré. 3. Ne rien préremplir.
>
> *Choix.* Option 2. L'option 3 allongerait chaque déclaration pour un cas sur quarante-cinq.
>
> *Conséquences.* Aucun appel supplémentaire au système des contrats. Format de l'ancienne Artois à traiter (test n° 7). Exigence ajoutée pour les contrats à plusieurs adresses (test n° 23).
>
> *Décidé par :* J. Morel. *Relu par :* G. Vandamme, A. Lambrecht, N. Benali. *Sources :* wiki, page « Adresse de correspondance et adresse du risque » ; tests de caractérisation 1 à 40.

À 16 heures, Isabelle Delattre était passée à notre revue de fin d'itération. Nous n'avions rien à lui montrer qui ressemble à un écran. Nous lui avons montré deux documents, quarante tests, quatre pages de wiki et une correction en production. Elle a demandé ce qui avait changé depuis le premier jet du lundi. Julien lui a montré la décision DA-04.

— Lundi, l'agent avait écrit une architecture complète, a-t-il dit. Elle aurait envoyé les experts à la mauvaise adresse.

— Et si vous l'aviez découvert en mars ?

— En mars, on l'aurait découvert après un incendie.

Isabelle n'a pas posé d'autre question. Elle a noté quelque chose sur son téléphone et elle est repartie vers la revue suivante.

Gérard a remis ses huit cahiers dans le sac de la médiathèque.

— Je les garde, a-t-il dit. Mais je n'en ouvrirai pas de neuvième. Ce que je sais, maintenant, je l'écris là où quelqu'un viendra le chercher.

Julien est resté après les autres, comme le vendredi précédent.

— En septembre, j'aurais écrit l'architecture tout seul, en deux semaines, m'a-t-il dit. Et j'aurais pris l'adresse en tête du contrat, comme l'agent. Ce n'est pas l'agent qui nous a évité ça. Ce n'est pas moi non plus. C'est Martine, qui a lu un dossier.

Le lundi, l'agent découperait le travail en epics et en stories, à partir des exigences et de l'architecture. En partant, Sylvie m'a rappelé qu'il faudrait les mettre dans Jira. Je lui ai répondu qu'elles seraient dans le dépôt. Cette fois, elle n'a rien noté. Elle m'a regardé un moment, puis elle a dit que nous en reparlerions lundi.

## Le carnet de Thomas

**Ce qui s'est passé.** Pour la troisième étape de la méthode, l'agent architecte a lu le wiki avant les exigences, sur décision du tech lead, puis il a proposé une architecture complète en une heure. Il y glissait une idée séduisante et courante, une copie nocturne du système des contrats, que le tech lead a refusée en écrivant pourquoi : fraîcheur des avenants, données personnelles copiées une fois de plus, échec d'un chantier comparable. Chaque décision a pris une forme fixe, rédigée par l'agent, sauf le nom de celui qui décide. Le mercredi, une gestionnaire a repéré la première anomalie de production : le portail préremplissait l'adresse de correspondance au lieu de l'adresse du risque. L'expert du système le savait depuis trente ans sans l'avoir jamais écrit, et l'architecture du lundi reproduisait la même erreur. L'architecture a attendu le retour du tech lead. Après une correction relue et déployée de jour, il a imposé des tests de caractérisation : quarante contrats choisis parmi les pires, la réponse réelle du système enregistrée champ par champ. Trois surprises en sont sorties, dont une exigence que personne n'avait imaginée.

**La leçon.** Un agent architecte propose volontiers l'architecture qu'on attend : moderne, découplée, et souvent étrangère au système qu'elle doit servir. Faites-lui lire l'existant avant les exigences. Exigez pour chaque décision le contexte, les options, le choix, le coût et le nom de celui qui décide ; l'agent rédige, il ne signe pas. Face à un système ancien, ne vous fiez ni à la documentation, ni à la mémoire de ses experts, ni à celle de l'agent : enregistrez ce que le système fait vraiment, sur les cas les plus tordus que vos experts connaissent, et faites tourner ces tests chaque nuit. Le savoir le plus dangereux est celui qui paraît évident à celui qui le détient : il ne l'écrit jamais, et personne ne pense à le lui demander. Enfin, quand la production appelle, l'architecture attend : un agent ne doit pas poursuivre seul une phase dont personne n'est là pour signer les décisions.

**Trois questions à poser à votre équipe**

1. Notre agent lit-il le système existant avant les exigences, ou après ?
2. Pour chaque transaction ancienne que nous utilisons, avons-nous enregistré ce qu'elle renvoie vraiment dans les cas les plus difficiles ?
3. Qu'est-ce qui est si évident pour nos experts qu'ils ne l'ont jamais écrit ?

**Pour aller plus loin.** Manuel, chapitres M9 (BMAD : la phase de conception, documenter les décisions d'architecture), M11 (le wiki d'équipe : faire lire l'existant à l'agent avant les exigences) et M13 (bonnes pratiques : des tests de caractérisation pour un système ancien).
