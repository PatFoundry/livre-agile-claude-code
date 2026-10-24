# Chapitre 27 — Le sprint d'après

## Mardi 13 janvier, 6 heures

J'avais promis de revenir sur cette journée. Il faut le faire maintenant, avant que tout le reste ne la recouvre, parce qu'elle est la plus importante du projet, et qu'il ne s'y est presque rien passé.

Le comité avait donné son accord le vendredi précédent, par un courriel de deux lignes de Catherine Duhamel, reçu en plein PI Planning. Le procès-verbal d'homologation portait la signature de Philippe Wattebled depuis le mercredi. Didier Vermeersch avait fixé l'heure : 6 heures, une heure après la réouverture du système des contrats, trois heures avant l'arrivée des gestionnaires.

J'étais dans la salle Lys à 5 h 45. Julien, Sofiane et Didier y étaient déjà, avec un sachet de croissants que personne n'avait ouvert. Didier avait imprimé sa liste : vingt-deux étapes, chacune avec son responsable, son temps prévu et son retour arrière. Il l'a déroulée à voix haute, une ligne après l'autre, sans hausser le ton, comme un pilote avant le décollage.

À 6 h 31, le portail était en production. Il n'était ouvert qu'aux salariés de la maison assurés chez elle, pour une heure. À 7 h 40, Didier a relu les journaux, Mathilde a vérifié qu'ils ne contenaient aucune donnée personnelle, et Julien a confirmé que le système des contrats n'avait été appelé qu'une fois par déclaration. À 9 heures, le lien est apparu dans l'espace adhérent, sans campagne, sans communiqué, à la demande de Claire. Elle voulait que les premiers assurés trouvent le portail par eux-mêmes.

La première vraie déclaration est arrivée à 9 h 14. Un dégât des eaux à Douai : un lave-vaisselle, une cuisine inondée, quatre photos. Martine l'a ouverte à 9 h 40, a appelé l'assurée pour lui dire que son dossier était complet, et l'avait déjà fait avancer avant 10 heures. Nadia a imprimé l'accusé de réception, sans le nom de l'assurée, et l'a punaisé sur le mur de la salle Lys, à côté du ruban rouge.

Puis il ne s'est plus rien passé. Les déclarations sont arrivées une par une, à quelques minutes d'intervalle. Les tableaux de Didier sont restés verts. Le centre de relation a appelé une fois, à 11 heures, pour demander ce que voulait dire *dès que notre système sera de nouveau disponible*, et Nadia a répondu en deux phrases. À midi, Julien a fini par ouvrir le sachet de croissants. Ils étaient froids.

— C'est la journée la plus ennuyeuse du projet, a-t-il dit.

— C'est la meilleure, a dit Didier. Une mise en production réussie, c'est une mise en production dont personne ne se souvient.

J'ai écrit à Claire à 13 heures. Trois lignes, comme toujours. *En production depuis 6 h 31. Trente et une déclarations, aucune perdue, aucun incident. Rien à signaler, et c'est le résultat de quatre mois.* Sa réponse est arrivée dans la minute.

*Ne changez rien.*

Je n'en ai pas parlé plus tôt dans ce récit parce qu'il n'y avait rien à raconter. Il n'y avait rien à raconter parce que tout avait été raconté avant : le Mercredi noir, les garde-fous, les tests de résilience, le gestionnaire qui voyait avec ses oreilles, les onze mille contrats de l'Artois, le script de 2014. Une mise en production sans histoire n'est pas une chance. C'est la somme de toutes les histoires qui ont eu lieu avant.

## Lundi 9 février, 9 heures

Le lundi 9 février, il n'y avait plus qu'une colonne au tableau de la salle Lys. Julien avait effacé lui-même celle de gauche. La production avait sa garde, ses tableaux de bord et Didier ; elle n'avait plus besoin d'une moitié de mur. Toute l'équipe était sur la phase 2, et c'était la première itération que nous allions mener entièrement avec la méthode, du fichier de story jusqu'à la production.

Léa Vandenberghe est arrivée à 9 heures. Elle venait des équipes de test d'Horizon, et elle faisait partie du premier groupe qu'Émilie formait le jeudi depuis la mi-janvier. Elle avait demandé à nous rejoindre la semaine où Dewitte avait accepté de la détacher.

Émilie ne lui a fait aucune présentation. Elle lui a donné un fichier, celui de la story 3.2, *Déclarer un bris de glace*.

— Lis ça. Si tu dois me poser une question pour comprendre ce qu'elle doit faire, c'est que la story est mal écrite, et c'est mon problème, pas le tien.

Léa l'a lue en vingt minutes. Elle a posé une seule question, sur la franchise, et la réponse se trouvait dans la règle F1, à laquelle la story renvoyait. À l'automne, une story ne devenait claire qu'après une heure et demie de préparation avec Nadia et Émilie. Celle-ci l'était pour quelqu'un qui arrivait le matin même, parce qu'elle ne supposait plus rien de ce que le lecteur ne savait pas.

J'avais demandé à Sylvie, ce lundi-là, de ne pas regarder la story 3.2 avec ses yeux de coordinatrice, mais de noter heure par heure ce que Jira et GitHub enregistreraient d'elle. Je voulais savoir à quoi ressemblait, vu de l'extérieur, le cycle que nous avions mis cinq mois à construire. Le soir, elle m'a remis une demi-page.

> **Story 3.2 — Déclarer un bris de glace** · ce que Jira et GitHub ont enregistré, lundi 9 février
>
> 9 h 30 — L'agent lit la priorité dans Jira et ouvre une branche portant la clé du ticket, dans sa propre copie isolée du dépôt.
>
> 9 h 50 — Il lit la story et ce qu'elle cite : exigences EF-21 à EF-24, décisions DA-02 et DA-04, règle F1. Les sept scénarios d'Émilie échouent : le code n'existe pas encore.
>
> 10 h 40 — Les sept scénarios passent. Demande de fusion ouverte ; le ticket passe à *en cours*.
>
> 10 h 45 — Prérelecture automatique : deux remarques, dont un message d'erreur muet pour un lecteur d'écran. L'agent corrige.
>
> 11 h 15 — Relecture de Julien, classement orange (photos). Une question, dont la réponse est dans la décision DA-06. Approuvée à 11 h 58.
>
> 14 h — Tests exploratoires d'Émilie et de Léa en recette : un libellé corrigé.
>
> 14 h 30 — Démonstration à Sabine.

Julien m'a dit le soir qu'il n'avait jamais relu une demande de fusion aussi vite, ni aussi tranquillement. Il n'avait eu à se demander qu'une chose : le code faisait-il ce que disait la story ? Ce que la story devait dire, d'autres l'avaient déjà décidé, avec leur nom en face. À l'automne, il relisait le soir des demandes dont il devait deviner l'intention.

La dernière ligne de la demi-page de Sylvie tenait en trois mots. Elle allait nous occuper jusqu'au lendemain midi.

## Lundi 9 février, 14 h 30

Sabine était venue avec un dossier qu'elle connaissait par cœur. Un samedi soir, un ballon dans une baie vitrée, des enfants désolés et un assuré qui ne pouvait pas laisser sa maison ouverte pour la nuit. Le vitrier était venu en urgence poser un panneau de protection. Il avait facturé la mise en sécurité le soir même, puis, quinze jours plus tard, une fois le verre commandé et livré, le remplacement.

Elle a rejoué le dossier sur le portail de recette, devant nous. Elle a déclaré le bris, joint les photos, joint la facture de la mise en sécurité. Le portail lui a répondu que sa déclaration était complète. Elle a ouvert la page de suivi, quinze jours plus tard dans son scénario, avec la seconde facture à la main. Elle pouvait ajouter des photos. Elle ne pouvait pas ajouter de facture.

— La moitié des bris de glace ont deux factures, a-t-elle dit. La mise en sécurité, puis le remplacement. Je ne l'ai dit à personne en décembre. Pour moi, c'était évident.

Gérard aurait reconnu la phrase. Sofiane était déjà au clavier.

— Je l'ajoute en dix minutes. Un bouton *ajouter une facture* sur la page de suivi.

— Non, a dit Julien. D'abord la spec.

— C'est dix minutes contre deux heures.

— Si tu corriges le code sans corriger la story, la prochaine fois que l'agent relira la 3.2, pour une évolution ou une correction, il remettra le code d'accord avec la story. Il effacera ta correction, avec des tests tout verts, et personne ne s'en apercevra avant qu'un assuré se retrouve avec sa facture à la main. La spec, c'est ce qui reste vrai. Le code, c'est ce qu'on en tire.

Sofiane a lâché le clavier. Il ne discutait plus avec Julien depuis longtemps quand Julien avait raison, et il savait le reconnaître plus vite qu'en septembre.

Nadia a écrit l'exigence elle-même : l'assuré pourrait joindre plusieurs factures, y compris après sa déclaration, tant que son dossier resterait ouvert. *Source : S. Dumortier, démonstration du 9 février. Décidé par : N. Benali.* Émilie a ajouté un huitième scénario, deux factures à quinze jours d'écart. La modification de la story est passée par une demande de fusion, comme du code, relue par Nadia et Émilie. Puis l'agent a relu la story 3.2, vu son nouveau scénario échouer, et écrit ce qui manquait. Julien a relu. La correction a été fusionnée le mardi à 11 h 40.

C'est la question suivante de Nadia qui a justifié les deux heures.

— Quelles autres stories supposent une seule facture ?

L'agent en a trouvé trois. La story 4.3, celle des petits incendies, qui demandait *une facture ou un devis* : Nadia l'a corrigée avant que la moindre ligne de code n'existe. L'annexe des dommages électriques, restée au niveau du brief : une note y a été ajoutée pour le jour où on la détaillerait. Et la story des dégâts des eaux de la phase 1, en production depuis un mois.

— La recherche de fuite, puis la réparation, a dit Sabine. Deux factures, là aussi.

Nadia a ouvert un ticket pour la phase 1, et elle l'a placé à l'itération suivante, après le mois sans incident sérieux que Claire avait exigé avant de toucher au portail en production. Le mois s'achèverait le vendredi.

À l'automne, nous aurions corrigé le code en dix minutes, et l'erreur serait revenue trois fois, à trois endroits, chaque fois découverte par quelqu'un d'autre. Cette fois, la correction avait pris une journée. Mais elle était arrivée, sans que personne ait à s'en souvenir, à trois endroits où personne ne l'avait cherchée.

## Vendredi 20 février, 16 heures

À la revue de fin d'itération, Sylvie a affiché le tableau de bord tel qu'il s'était calculé le lundi, sans une ligne de saisie. Quinze stories terminées en deux semaines. Un jour et demi de temps de traversée. Une seule retouche, un libellé mal lu par un lecteur d'écran. Et une cinquième ligne, ajoutée le mardi après une discussion d'une demi-heure entre Sylvie, Nadia et moi : les écarts de spécification découverts après le code. Les deux factures n'étaient pas une retouche, puisque le code faisait exactement ce que disait la story. C'était la story qui ne disait pas tout. Nous voulions les compter à part, pour savoir si nos questions s'amélioraient aussi vite que notre code.

Un écart, cette itération-là. Personne ne prétendait qu'il n'y en aurait plus.

Le bris de glace partirait en production le mardi suivant. Ce serait le premier sinistre de la phase 2. Didier avait déjà imprimé sa liste ; elle ne comptait plus que onze étapes.

Isabelle Delattre assistait à la revue. Elle a attendu la fin pour parler.

— Votre fourchette tient, a-t-elle dit à Sylvie. Six à huit par semaine, deux itérations de suite. Je la présenterai à l'Inspect & Adapt.

Puis elle s'est tournée vers Julien et Nadia.

— Au prochain PI Planning, en avril, je voudrais que vous soyez deux équipes. Vous l'aviez écrit vous-mêmes en novembre : au-delà de six ou sept, une équipe augmentée se coordonne plus qu'elle ne travaille. Vous êtes onze.

Personne n'a protesté. La règle était la nôtre. Julien a dit qu'il resterait référent technique pour les deux. Nadia a dit qu'elle voulait garder les déclarations, et que Sabine prendrait l'accompagnement, si Philippe Wattebled la lui laissait à plein temps. Il l'avait déjà promis.

J'ai attendu que les autres soient partis pour annoncer ce que je savais depuis novembre. À partir de mars, je ne viendrais plus que trois jours par semaine ; en avril, deux ; en mai, plus du tout. Ma mission s'arrêtait là où elle devait s'arrêter, au moment où l'équipe n'aurait plus besoin de moi.

— Qui surveillera la frontière ? a demandé Nadia.

J'ai regardé le tableau, avec sa colonne unique.

— Il n'y a plus de frontière.

Gérard, lui, partait le 3 avril. Il avait demandé qu'on ne fasse pas de pot de départ. Nous en ferions un quand même.

## Jeudi 5 mars, 10 heures

Un mois après le bilan, Claire et Laurent Dewitte sont montés ensemble à la salle du conseil. Ils avaient préparé leurs pages séparément, puis ils les avaient relues l'un chez l'autre, comme le voulait la règle de l'instance commune. J'étais assis contre le mur, à la même place qu'en février. C'était l'un de mes trois jours de la semaine.

Claire a parlé la première. Elle avait promis une fourchette ; elle en apportait une, avec ses probabilités. L'agent avait rejoué mille fois la suite de la phase 2 à partir de nos débits réels, ceux des itérations 2 et 3, et de la liste des stories restantes. Il n'avait rien estimé ; il avait tiré au sort dans ce que nous avions vraiment fait. Claire avait arrondi les résultats et les avait écrits sur une page, en gros caractères.

Le bris de glace, en production depuis le 24 février. Les petits incendies et la déclaration accompagnée, fin mars, avec neuf chances sur dix. Les tempêtes et les dommages électriques, mi-mai, avec trois chances sur quatre. Tous les sinistres sauf les catastrophes naturelles et la responsabilité civile avant le 14 juillet, avec quatre chances sur cinq. Les catastrophes naturelles et la responsabilité civile en septembre, avec une chance sur deux, parce que la seconde attendait toujours l'avis d'Anne-Sophie Dhondt.

— Donc pas tous les sinistres avant l'été, a dit Catherine Duhamel.

— Pas tous, a dit Claire. Et c'est écrit.

La directrice générale a relu la page un long moment.

— C'est la première fois qu'on m'annonce un retard avant qu'il arrive, a-t-elle dit. Je préfère ça.

Puis Laurent Dewitte a présenté la proposition qu'il avait demandé un mois pour construire. Horizon garderait sa mission première, remplacer le cœur de gestion et le système des contrats, et son calendrier ne changerait pas. Il cesserait en revanche de construire les parcours destinés aux assurés, qui reviendraient aux équipes du train. Le module de déclaration pour les gestionnaires passerait de deux équipes de l'ESN à une seule, avec Antoine comme référent. Toutes les équipes d'Horizon écriraient leurs scénarios avant le code, sur le modèle des jeudis d'Émilie. Elles poseraient des tests de caractérisation sur chaque transaction du mainframe qu'elles remplaçaient, et publieraient chaque mois leur taux de retouche, avec la définition de Quentin. Un cinquième du budget annuel d'Horizon serait réaffecté aux équipes du train.

— Je suis venu en octobre pour juger ce pilote, a-t-il conclu. Je repars avec sa méthode et un cinquième de mon budget en moins. Je crois que c'est une bonne affaire pour la maison.

Hervé Delcourt a demandé si ce n'était pas, au fond, l'abandon d'Horizon par étapes. Dewitte a secoué la tête.

— Le portail lit encore le mainframe tous les jours, et il le lira tant que quelqu'un ne l'aura pas remplacé. Ce quelqu'un, c'est Horizon. On ne l'abandonne pas. On lui retire ce qu'il faisait mal, pour qu'il fasse mieux ce que lui seul peut faire.

Le comité a validé les deux pages en vingt minutes. Catherine Duhamel a demandé qu'on lui présente la même chose en juin, avec les mêmes probabilités, pour voir si elles avaient tenu.

Claire et Dewitte sont sortis ensemble, en discutant déjà de la répartition des équipes. Je suis descendu seul par l'escalier et je suis sorti sur la place. Le beffroi sonnait 11 heures.

J'ai repensé au titre que je donnais, dans ma tête, à ce projet depuis septembre. Pendant longtemps, j'avais cru que le moment décisif serait la démonstration, puis la crise, puis la mise en production. Je m'étais trompé trois fois. Le moment décisif, c'est le sprint d'après : celui qui suit la crise, la décision ou le changement de méthode, quand plus personne ne regarde et que l'enthousiasme est retombé. Il ne fait pas de bruit. Il n'a pas de démonstration. C'est pourtant à lui qu'on reconnaît ce qui a vraiment changé. Le nôtre avait livré quinze stories, une seule retouche, un écart corrigé au bon endroit, et une équipe qui n'avait plus besoin de moi pour le savoir.

## Le carnet de Thomas

**Ce qui s'est passé.** La mise en production de la phase 1 n'a donné lieu à aucun incident, parce que tout ce qui pouvait mal tourner avait déjà été traité avant. Un mois plus tard, toute l'équipe a mené sa première itération entièrement avec la méthode. Une nouvelle testeuse a compris une story le matin même de son arrivée. Une story de bris de glace est passée en une journée de son ticket à la fusion, scénarios rouges puis verts, prérelecture, relecture humaine, tests exploratoires. La démonstration au métier a révélé un écart : un bris de glace a souvent deux factures. L'équipe a corrigé la spécification avant le code, puis a demandé à l'agent où la même hypothèse se cachait ailleurs : elle en a trouvé trois. Le tableau de bord a gagné une ligne pour les écarts de spécification. Devant le comité, la sponsor a présenté une fourchette assortie de probabilités, calculée sur le débit réel, et le directeur d'Horizon a recentré son programme sur ce que lui seul pouvait faire.

**La leçon.** Dans une équipe qui travaille à partir des spécifications, la spécification est ce qui reste vrai et le code n'est que ce qu'on en tire. Un écart se corrige donc d'abord dans la spécification, faute de quoi l'agent le réintroduira la prochaine fois qu'il la relira, avec des tests tout verts. Cette discipline coûte quelques heures, mais elle permet ensuite de propager une correction partout où la même hypothèse se cache. Une story autoportante sert aussi à accueillir quelqu'un. Remplacez les promesses par des fourchettes calculées sur ce que l'équipe a réellement fait, avec la probabilité de les tenir. Enfin, jugez un changement de méthode sur le sprint d'après, celui que personne ne regarde, et non sur la démonstration.

**Trois questions à poser à votre équipe**

1. Quand un écart apparaît, le corrigeons-nous d'abord dans la spécification, ou seulement dans le code ?
2. Un nouvel arrivant peut-il comprendre l'une de nos stories sans poser de question ?
3. Nos prévisions sont-elles des promesses, ou des fourchettes calculées sur ce que nous avons réellement fait ?

**Pour aller plus loin.** Manuel, chapitres M9 (BMAD : le cycle d'implémentation, corriger la spécification avant le code), M10 (GitHub et Jira au quotidien : suivre une story de bout en bout), M12 (partager en équipe : accueillir un nouvel arrivant) et M13 (bonnes pratiques : prévoir avec des fourchettes plutôt qu'avec des points).
