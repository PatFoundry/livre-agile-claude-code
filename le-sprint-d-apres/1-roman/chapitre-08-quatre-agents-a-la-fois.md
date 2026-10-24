# Chapitre 8 — Quatre agents à la fois

## Lundi, 8 h 30

Le rapport de Laurent Dewitte est arrivé dans ma boîte à 7 h 12, transféré par Claire avec trois mots : *Pour information. Jeudi.*

Quatre pages, une police élégante, pas une faute. Je l'ai lu deux fois en cherchant la phrase injuste. Il n'y en avait aucune. Le pilote était « prometteur ». Son périmètre se limitait « au portail, sans impact à ce stade sur le cœur de gestion ». L'équipe présentait « une dépendance critique à une ressource unique ». Et en bas de la troisième page, dans un paragraphe intitulé *Engagements pris en séance*, figuraient le vol avant la campagne de janvier et l'ensemble des sinistres d'ici l'été, attribués nommément à la DSI adjointe. La recommandation finale tenait en une ligne : point d'étape au comité de décembre, afin d'« étudier les conditions d'une intégration au programme Horizon ».

C'était un rapport parfait. Il suffisait de nous laisser faire pour qu'il devienne prophétique.

À 9 heures, nous avons lancé le sprint 2. Vingt-huit stories, dont neuf pour le vol. Nadia les avait préparées pendant le week-end avec l'agent. Je l'ai compris en regardant les dates de création dans Jira : samedi soir, dimanche après-midi, dimanche 23 h 40.

Elle nous a présenté le vol comme elle avait présenté le dégât des eaux, en partant des gens.

— Un vol, ce n'est pas un dégât des eaux avec d'autres photos. L'assuré a deux jours ouvrés pour nous prévenir, pas cinq. Il doit porter plainte et nous envoyer le récépissé. Il ne connaît pas toujours la date du vol, seulement le moment où il s'en est aperçu, en rentrant de vacances par exemple. Et il doit lister ce qu'on lui a pris, avec les factures quand il les a.

— Personne n'a jamais ses factures, a dit Émilie.

— Personne. C'est pour ça que la moitié de mes stories parle des autres preuves : photos, relevés bancaires, notices.

Sofiane avait déjà préparé son poste. Deux écrans, quatre fenêtres. Dans chacune, un agent travaillait sur sa propre copie isolée du dépôt, sa propre branche, sa propre story. Ils ne pouvaient pas se marcher sur les pieds, nous a-t-il expliqué : chacun avait son bac à sable.

— Comment avez-vous réparti les stories entre les quatre ? ai-je demandé.

— Dans l'ordre du backlog. Les quatre premières, puis les quatre suivantes. Elles sont indépendantes, Nadia les a découpées comme ça.

Nadia a hoché la tête. Elle les avait découpées pour qu'un assuré voie quelque chose de nouveau à chaque livraison. Elle ne les avait pas découpées pour qu'un logiciel puisse les écrire en même temps. Personne ne lui avait jamais demandé de le faire, et je ne l'ai pas fait non plus ce matin-là. J'avais décidé, le vendredi, de laisser l'équipe vivre ses propres mises en garde. Je m'y suis tenu. C'est plus difficile qu'il n'y paraît.

Toute la matinée, j'ai regardé Sofiane travailler. Il passait d'une fenêtre à l'autre comme un joueur d'échecs dans une partie simultanée : il répondait à une question d'un agent sur le format des numéros de contrat, validait le plan d'un deuxième, relançait un troisième qui s'était arrêté sur un test, puis revenait au premier. Il ne tapait presque plus de code. Il arbitrait.

À 11 h 40, la première demande de fusion est apparue sur GitHub. À midi et quart, la deuxième. À 17 heures, il y en avait six.

Julien a regardé les six notifications sur son écran, l'une après l'autre. Il n'a rien dit. Il a pris la première.

## Mardi, 14 heures

Les deux premières demandes de fusion étaient passées sans encombre. La troisième s'est arrêtée net : GitHub signalait un conflit sur le modèle de la déclaration et sur le fichier des libellés de l'écran d'accueil.

Deux agents avaient travaillé, chacun dans son bac à sable, sur le même objet. Le premier ajoutait au vol une date de découverte. Le second ajoutait, en tête du parcours, le choix du type de sinistre. Tous les deux avaient modifié la déclaration, et ni l'un ni l'autre ne pouvait savoir que l'autre existait.

Sofiane n'a pas hésité. Il a demandé à l'un des agents de résoudre le conflit. Deux minutes plus tard, tout compilait et tous les tests passaient. Il a poussé, satisfait, et il a envoyé la demande à Julien.

Julien l'a ouverte à 15 heures. À 15 h 05, il a fait pivoter son écran vers nous.

— Regardez la déclaration.

Elle portait désormais deux champs pour dire la même chose. L'un s'appelait *nature du sinistre*, le terme exact de notre glossaire, celui que Nadia avait fait valider pendant le sprint 0, quand nous avions réécrit à la main le fichier de consignes de l'agent. L'autre s'appelait *type de sinistre*. C'était le terme de la story, écrite un dimanche à 23 h 40, et l'agent l'avait repris fidèlement. Pour résoudre le conflit, l'agent avait gardé les deux. Il avait fait comme un diplomate : il avait donné raison à tout le monde.

— Dans six mois, a dit Julien, quelqu'un remplira l'un et quelqu'un d'autre lira l'autre. Et on passera une semaine à comprendre pourquoi les vols apparaissent comme des dégâts des eaux dans les statistiques.

Nadia est devenue toute rouge. Elle a corrigé sa story sans un mot.

À 16 heures, Sofiane a fusionné la quatrième demande, puis la cinquième. L'environnement de recette a refusé de redémarrer. Émilie, qui avait prévu sa campagne de tests pour la fin d'après-midi, a attendu une heure, puis deux, puis elle est venue s'asseoir à côté de Julien. Il a trouvé à 18 h 50. Chacun dans sa copie, deux agents avaient créé un script de mise à jour de la base de données. Chacun avait pris le numéro suivant, le même. La base ne savait plus lequel exécuter en premier.

— Chaque demande passait ses tests, a dit Sofiane.

— Chacune toute seule, a répondu Julien. Pas les deux ensemble.

La correction lui a pris dix minutes. La recherche en avait pris trois heures.

Le pire n'est arrivé que le lendemain, et c'est Émilie qui l'a trouvé. Elle testait à la main, comme elle le faisait toujours, en se mettant à la place d'une assurée. Elle a déclaré un dégât des eaux survenu cinq jours ouvrés plus tôt, la dernière journée dans les délais. Sur le poste de Martine, le dossier est arrivé avec un drapeau rouge : *Déclaration tardive*.

Il nous a fallu deux heures pour comprendre. Pour le vol, une story avait transformé la date du sinistre en date et heure, puisqu'on note le moment où l'assuré a découvert le vol. Une autre story, livrée la veille par un autre agent, calculait l'indicateur de retard pour les gestionnaires. Elle comptait les jours sur l'ancienne date. Ensemble, une déclaration faite le cinquième jour à 14 heures devenait tardive. Les deux stories touchaient des fichiers différents. Git n'avait vu aucun conflit. Chacune avait ses tests, et ses tests passaient.

— Et même tardive, a dit Nadia d'une voix blanche, une déclaration n'est pas perdue. Pour refuser, il faut prouver que le retard nous a causé un préjudice. Si Martine voit ce drapeau, elle va appeler une assurée dans les délais pour lui dire qu'elle ne l'est pas.

Julien s'est tourné vers Sofiane.

— Les conflits que Git te montre, ce sont les gentils. Il te prévient, il t'oblige à choisir. Les méchants, il ne les voit pas.

## Mercredi, 18 heures

J'ai réservé la salle Deûle, celle qui a le plus grand tableau blanc, et j'ai demandé à Julien de me montrer où les stories se touchaient.

Il restait dix-huit stories dans le sprint. J'ai tracé une colonne par zone du code, telles que Julien me les dictait : la déclaration, les pièces jointes, la recherche du contrat, les notifications, l'écran des gestionnaires, la base de données. Puis une ligne par story. Pour chaque croisement, Julien disait oui ou non, et je dessinais une croix.

Sofiane nous a rejoints à 18 h 30. Il a regardé le tableau à moitié rempli, il est reparti chercher son portable, et il est revenu avec une meilleure idée que la nôtre.

— L'agent peut le faire. En mode plan, il lit le code et propose ce qu'il ferait, sans rien modifier. Je lui donne chaque story, il me dit quels fichiers il toucherait.

Il l'a fait pour les dix-huit. Cela lui a pris vingt minutes. Julien a vérifié la liste ligne par ligne et n'a corrigé que deux croix. Quand nous avons eu fini, le tableau racontait une histoire que personne n'avait voulu voir le lundi : onze stories sur dix-huit touchaient la déclaration.

— Ce ne sont pas quatre chantiers, ai-je dit. C'est un seul chantier, avec quatre ouvriers devant le même mur.

Julien a posé son feutre.

— Le vrai problème est en dessous. La déclaration a été construite pour le dégât des eaux. Elle ne connaît qu'une date, pas de plainte, pas de liste d'objets. Chaque story du vol essaie de l'agrandir à sa manière. Tant qu'on ne l'a pas refaite une fois, proprement, chaque agent la refera dans son coin.

Nous avons donc écrit, ce soir-là, une story que Nadia n'aurait jamais pensé à écrire, parce qu'aucun assuré ne la verrait : rendre la déclaration capable d'accueillir plusieurs natures de sinistre. Une date de survenance et une date de découverte. Les termes du glossaire, et aucun autre. Elle serait faite d'abord, par un seul agent, relue par Julien, fusionnée avant que quiconque ne touche à nouveau à la déclaration. Nous l'avons appelée la story fondation.

Puis j'ai écrit cinq règles dans le coin du tableau.

*Répartir le travail par zone du code, pas par ordre du backlog. Les fondations d'abord, et seules. Jamais deux agents sur la même zone en même temps. Des demandes de fusion petites, fusionnées le jour même, et chaque copie remise à jour tous les matins. Une recette où l'on teste les stories ensemble, pas seulement chacune de son côté.*

Sofiane a compté les colonnes, puis les croix.

— Avec ces règles, je ne peux faire tourner que deux agents en même temps. On va ralentir.

— On va produire moins de code, ai-je dit. Ce n'est pas la même chose que livrer moins.

— Et les bacs à sable ? Ils ne servent à rien, alors ?

— Ils servent à protéger les agents les uns des autres. Ils ne protègent pas le produit. Ça, c'est le découpage.

Julien n'avait rien dit depuis un moment. Il regardait le tableau, les croix, les cinq règles.

— Du code, on en a trop, a-t-il dit enfin. Ce qui manque, ce sont des gens pour le lire.

Personne n'a répondu à cela. Sofiane est parti à 20 heures. Je suis resté pour photographier le tableau, et Julien est resté pour l'effacer, ce qui était une façon de rester tous les deux.

— Tu veux un café ? a-t-il demandé. Il est infect, mais il est chaud.

C'était la première fois qu'il me tutoyait. Je n'ai pas relevé. Dans cette maison, on ne relève pas ces choses-là. On les rend.

— Volontiers. Et toi, la relecture, tu tiens ?

— Je tiens.

Il a jeté son gobelet, il a pris sa veste, et il est reparti vers son bureau. Pas vers l'ascenseur.

## Vendredi, 17 heures

La story fondation a été fusionnée le jeudi à midi. Julien avait passé deux heures à la relire, ce qui était beaucoup pour lui et peu pour elle. Ensuite, Sofiane a refermé deux de ses quatre fenêtres. Il l'a fait sans enthousiasme, mais il l'a fait.

Les règles ont tenu. Le vendredi, pas un seul conflit. Émilie a lancé pour la première fois une campagne de tests sur toutes les stories de la semaine réunies, et elle n'a rien trouvé de nouveau. Sur le poste de Martine, le drapeau rouge avait disparu des déclarations faites à temps. Sofiane a fini par admettre, à la machine à café, que deux agents bien répartis allaient presque aussi vite que quatre mal répartis. Venant de lui, c'était une déclaration d'amour.

Le jeudi après-midi, j'avais eu ma demi-heure avec Claire. Elle n'avait pas parlé du rapport de Dewitte. Elle m'avait posé une seule question.

— Le vol avant janvier, c'est tenable ?

— Écrire le code, oui. Le relire, je ne sais pas.

— Alors trouvez des relecteurs.

Elle l'avait dit comme on demande d'acheter des trombones.

Le vendredi à 17 heures, j'ai ouvert GitHub. Vingt-trois demandes de fusion attendaient une relecture. La plus ancienne datait du lundi. Les quatre agents du début de semaine en avaient produit plus que l'équipe n'en relirait jamais en cinq jours, et les deux agents de la fin de semaine continuaient, plus sagement, d'en ajouter.

J'ai fait un calcul que j'aurais dû faire le lundi. Une relecture prenait une heure quarante en moyenne. Julien en faisait six par jour. Six fois une heure quarante, cela faisait dix heures, sans compter ses réunions, ses questions à Gérard sur le COBOL, et les quinze fois par jour où quelqu'un venait lui demander si un champ s'appelait comme ceci ou comme cela.

Sylvie est passée à mon bureau avec son ordinateur ouvert.

— Dans Jira, vos stories sont toutes « en revue ». Pour le tableau de bord du comité, je les compte comme terminées ou comme en cours ?

— En cours.

— Votre vélocité va s'effondrer.

— Elle va dire la vérité. Ce n'est pas la même chose.

Elle a noté, sans commentaire. J'ai appris depuis que Sylvie ne commentait jamais une réponse qu'elle trouvait juste.

À 19 heures, en partant, je suis passé devant le bureau de Julien. Il était là, évidemment.

— Rentre chez toi. On regardera la file lundi, tous ensemble.

— Je vais en avancer quelques-unes ce week-end. Ce sera plus calme.

## Samedi, 22 h 47

Mon téléphone a vibré sur la table du salon. Une notification de GitHub : Julien venait d'approuver une demande de fusion. Puis une autre à 23 h 20. Une à minuit cinq. Une à 0 h 41.

Depuis le début du projet, Julien laissait sur chaque demande trois ou quatre commentaires précis, souvent ironiques, toujours justes. Ce soir-là, les commentaires raccourcissaient d'une approbation à l'autre. À 1 h 12, il n'en restait qu'une ligne. À 1 h 34, la neuvième demande approuvée portait un seul mot : *OK*.

J'ai écrit trois messages, je les ai effacés. Puis j'en ai envoyé un quatrième, le plus court.

*Va dormir.*

À 1 h 41, il m'a répondu par un pouce levé.

À 1 h 52, mon téléphone a vibré de nouveau. La dixième.

## Le carnet de Thomas

**Ce qui s'est passé.** Pour tenir la promesse faite au comité, Sofiane a fait travailler quatre agents en parallèle, chacun sur une copie isolée du dépôt, avec des stories réparties dans l'ordre du backlog. Les copies isolées ont évité que les agents se gênent pendant le travail, mais pas que leurs résultats se contredisent à la fusion : deux champs pour un même concept, deux scripts de base de données portant le même numéro, et surtout un calcul de délai faussé par deux stories qui ne se touchaient pas en apparence. Une carte des dépendances a révélé que onze stories sur dix-huit modifiaient la même zone. L'équipe a ajouté une story fondation et réduit le parallélisme. Les conflits ont disparu ; la file des relectures, elle, a continué de grossir.

**La leçon.** Le travail en parallèle est un problème de découpage, pas d'outil. Une copie isolée protège les agents les uns des autres ; elle ne protège pas le produit. Avant de lancer plusieurs agents, demandez-leur un plan sans modification pour savoir ce que chaque story toucherait, faites d'abord les fondations communes, et ne mettez jamais deux agents sur la même zone en même temps. Méfiez-vous surtout des conflits que l'outil de gestion de versions ne voit pas : seuls des tests sur l'ensemble des changements réunis les attrapent. Enfin, multiplier les agents multiplie le code à relire. Si la relecture ne suit pas, vous n'avez pas accéléré, vous avez déplacé la file d'attente.

**Trois questions à poser à votre équipe**

1. Comment répartissons-nous le travail entre nos agents : par ordre du backlog, ou par zone du code ?
2. Testons-nous nos changements réunis, ou chacun de son côté ?
3. Combien de demandes de fusion attendent une relecture en ce moment, et depuis combien de temps attend la plus ancienne ?

**Pour aller plus loin.** Manuel, chapitres M10 (GitHub et Jira : branches, copies isolées du dépôt et fusions) et M13 (bonnes pratiques : faire travailler plusieurs agents sans se marcher dessus).
