# Chapitre 18 — Les rôles bougent

## Lundi, 9 heures

Le courriel d'Isabelle Delattre est arrivé le lundi de la dernière semaine de développement, à 7 h 45. La Release Train Engineer du train Indemnisation écrivait comme on fait un plan de vol : sans adjectifs, avec des pièces jointes.

L'équipe de direction du train nous recevrait le jeudi, à 14 heures, pour préparer l'arrivée de la phase 2. Elle souhaitait, d'ici mercredi soir, un bilan de la phase 1 et la composition de l'équipe pour la suite. Pour la composition, elle avait joint le modèle que remplissaient toutes les équipes du train. Un tableau d'une page. Une ligne par personne, et trois colonnes : le nom, le rôle, le pourcentage d'affectation. La colonne des rôles proposait une liste déroulante. *Product Owner. Scrum Master. Développeur. Testeur. Autre.*

J'ai commencé à le remplir moi-même, à mon bureau, avec mon café. J'ai écrit *Nadia Benali*, et j'ai choisi *Product Owner*. C'était exact, et ce n'était pas vrai. J'ai écrit *Sofiane Haddad*, et j'ai choisi *Développeur*. Je me suis arrêté là. Sofiane n'avait pas écrit trente lignes de code à la main depuis un mois.

J'ai fermé le fichier, et j'ai demandé à l'équipe un quart d'heure dans la salle Lys, après le point du matin.

— Le train veut savoir qui fait quoi, ai-je dit. Avant de remplir les cases, je voudrais que chacun me dise ce qu'il fait vraiment. Pas ce qui est écrit sur son contrat de travail. Ce qu'il a fait la semaine dernière.

Nadia a commencé, parce qu'elle était la plus proche du tableau.

— Au début, j'écrivais des stories. Maintenant, j'en écris moins, et elles sont plus courtes. Je passe mes journées à répondre aux questions de l'agent, à arbitrer des règles avec Gérard, à dire ce qui est vrai quand deux documents ne disent pas la même chose. Je ne suis plus celle qui décrit le besoin. Je suis celle qui dit ce qui est juste.

Émilie a parlé ensuite, plus brièvement.

— Je n'exécute presque plus de tests. J'écris le contrat avant le code, avec Nadia. Et après le code, je cherche ce que personne n'a pensé à demander.

Sofiane a hésité. Je crois que c'était la première fois qu'il se posait la question.

— Je ne code presque plus. Je prépare les sessions de l'agent, je découpe le travail en zones, je relis le vert et l'orange. Et j'écris les outils de l'équipe : les contrôles automatiques, les consignes de relecture, le wiki de Gérard. Je suis… je ne sais pas comment ça s'appelle.

— Un chef d'orchestre qui fabrique aussi les instruments, a dit Émilie.

Il a eu l'air d'aimer ça.

Julien a parlé en dernier, du fond de la salle.

— Je relis le rouge. Je tranche l'architecture quand l'agent propose deux solutions. Je forme Sofiane à relire ce qui touche aux contrats. Et à partir de mercredi, si la commission dit oui, je serai le référent technique du socle pour toute la maison. Je n'ai plus le temps de coder. C'est peut-être aussi bien.

J'ai noté au tableau, en face de chaque nom, ce que chacun venait de dire. Puis j'ai ajouté deux noms qui n'étaient pas dans l'équipe et qui en faisaient pourtant partie. *Gérard Vandamme : relecture du rouge, mémoire du système des contrats, jusqu'au 11 avril.* *Mathilde Grare : sécurité intégrée, deux jours par semaine.*

Nous avons regardé le tableau, puis la liste déroulante du modèle, projetée à côté. Product Owner, Scrum Master, Développeur, Testeur, Autre.

— Tout le monde est dans « Autre », a dit Sofiane.

— Non, ai-je dit. Tout le monde est à sa place. Ce sont les cases qui n'ont pas bougé.

Les rôles de Scrum n'étaient pas faux. Il y avait toujours quelqu'un pour dire ce qu'on construit et pourquoi, des gens pour construire, quelqu'un pour veiller à ce que l'équipe puisse travailler. Mais ce que chacun faisait à l'intérieur de son rôle avait changé de nature en trois mois. Le travail s'était déplacé vers les deux bouts de la chaîne : dire ce qui est juste avant le code, vérifier ce qui est juste après. Au milieu, là où autrefois se trouvait presque tout le monde, il restait l'agent, et quelqu'un pour le diriger.

J'ai décidé de ne pas utiliser la liste déroulante. J'ai gardé les rôles du modèle, et j'ai ajouté une quatrième colonne, sans demander la permission : *ce que fait réellement la personne*.

Julien m'a regardé la remplir.

— Et toi, a-t-il demandé, tu mets quoi ?

J'ai laissé ma ligne vide. Je n'avais pas de réponse, et je n'avais pas envie d'en inventer une devant eux.

## Mardi, 14 heures

Isabelle Delattre m'a appelé le mardi, pour préparer le jeudi. Elle avait lu notre page du comité, le registre de la dette, et le compte rendu de la revue d'incident. Elle avait tout lu, en réalité, et elle le disait sans s'en vanter.

— Tous les sinistres pour l'été, c'est un autre volume que le dégât des eaux et le vol, a-t-elle dit. Je peux vous renforcer. Le train a cinq développeurs qui finissent un chantier en janvier. Je peux vous les donner pour la phase 2.

C'était une offre généreuse, et c'était la réponse que la maison donnait depuis toujours à un projet qui grossit : plus de développeurs. Je lui ai demandé vingt-quatre heures pour en parler à l'équipe. Elle a eu l'air surprise, puis intéressée.

J'ai posé la question telle quelle, dans la salle Lys, à 14 heures. Sofiane a souri. Julien n'a pas souri.

— Cinq développeurs de plus, avec chacun son agent, a-t-il dit. C'est cinq fois plus de code à relire. Qui relit ?

Personne n'a eu besoin de répondre. L'épisode de la relecture, nous l'avions tous vécu.

J'ai affiché les mesures que nous tenions depuis le sprint 3, celles que Sylvie avait fini par mettre dans son tableau de bord à la place des points. Pour une story, de sa préparation à sa mise en recette, où passait le temps ? La préparation avec Nadia et Émilie : une heure et demie. Le développement par l'agent : trente-cinq minutes. La relecture : une heure, et deux pour le rouge. Les tests exploratoires d'Émilie : une heure. L'attente entre les étapes : quelques heures, depuis la limite de six.

— Le code, c'est trente-cinq minutes sur cinq heures, ai-je dit. Si on double le nombre de développeurs, on gagne peut-être quinze minutes par story. Et on double la file devant Julien et Gérard.

— Alors il nous faut quoi ? a demandé Sofiane.

Nous avons cherché la réponse dans l'autre sens. Pas « combien de personnes pour aller plus vite », mais « qu'est-ce qui va manquer, quand on passera à tous les sinistres ? ».

Nadia a répondu la première, et elle a eu le courage de parler d'elle.

— Moi. Je connais le dégât des eaux et le vol par cœur. L'incendie, la responsabilité civile, les catastrophes naturelles, je les connais comme une gestionnaire qui n'en a pas traité depuis six ans. Si je prends tout, je redeviens le goulot. Il nous faut une deuxième personne du métier, qui connaît les autres sinistres. Pas pour écrire des stories. Pour dire ce qui est juste.

Émilie a enchaîné.

— Une testeuse pour un sinistre, ça tient. Pour six, ça ne tiendra pas. Il me faut quelqu'un pour écrire les scénarios avec la deuxième personne du métier.

Julien a parlé de Gérard sans le nommer.

— Et dans quatre mois, il n'y aura plus personne pour relire le rouge avec moi. Il nous faut quelqu'un qui connaît le cœur de gestion. Il y en a chez Horizon. Franck a deux développeurs qui relèvent notre COBOL programme par programme depuis dix-huit mois. Ils connaissent le COBOL mieux que n'importe qui ici, sauf Gérard.

J'ai écrit au tableau ce que nous venions de dire. Une personne du métier, spécialiste des autres sinistres. Une deuxième testeuse. Un relecteur qui connaît le cœur de gestion, venu d'Horizon. Trois personnes, et pas un seul développeur de plus.

— Ça fait huit, a compté Sofiane. Horizon en a quarante.

— Horizon refait le cœur, a dit Julien. Pas nous. Ne te trompe pas de comparaison, Dewitte aurait raison de te la reprocher.

J'ai ajouté une dernière ligne, sur laquelle nous nous sommes mis d'accord sans débat : si la phase 2 grossissait encore, nous ne ferions pas une équipe de douze. Nous ferions deux équipes de six, chacune avec son métier, sa testeuse et son relecteur, et les sinistres partagés entre elles. Au-delà de six ou sept, une équipe augmentée passait plus de temps à se coordonner qu'à travailler, et ses agents produisaient plus que ses relecteurs ne pouvaient lire.

Le soir, j'ai rappelé Isabelle Delattre et je lui ai lu le tableau. Il y a eu un silence au bout du fil, puis un petit rire.

— C'est la première fois qu'une équipe refuse des développeurs, a-t-elle dit. D'habitude, on se bat pour en obtenir.

— Nous ne les refusons pas. Nous demandons ce qui nous manque. Les développeurs du train pourraient faire une autre équipe, avec le socle, si vous trouvez le métier et le relecteur pour aller avec.

— Présentez-le jeudi, a-t-elle dit. Exactement comme ça. Marc Vanhoutte va adorer, et Philippe Wattebled va devoir trouver une gestionnaire. Ce sera intéressant.

## Mercredi, 11 heures

Le mercredi matin, Sofiane a montré à l'équipe ce qu'il appelait la boîte à outils.

Le socle de Mathilde et de Julien, celui que la commission examinerait l'après-midi, disait ce que toute équipe de la maison devait avoir pour travailler avec un agent en sécurité. La boîte à outils, elle, contenait ce que notre équipe avait appris à faire. Sofiane l'avait empaquetée de la même façon, dans un second paquet du catalogue interne, que chaque équipe serait libre d'installer ou non.

Il y avait mis quatre skills, une par savoir-faire. La préparation d'une story : la façon dont l'agent interrogeait le métier avant d'écrire quoi que ce soit, puis proposait des exemples à valider. L'écriture des scénarios d'acceptation à partir d'une story et de ses règles. La préparation des relectures, avec les étiquettes de risque et les trois questions de Mathilde. Et la tenue du wiki, avec les règles de Julien et de Gérard.

— L'équipe d'Horizon qui démarre en janvier pourra s'en servir dès le premier jour, a-t-il dit. Elle n'aura pas à perdre trois mois à tout redécouvrir comme nous.

Nadia a ouvert la première skill, celle de la préparation des stories. Elle l'a lue en silence. Elle a mis longtemps, parce qu'elle lisait tout, et j'ai vu son expression changer au fil des lignes.

C'était elle. Sa façon de travailler, celle qu'elle avait inventée pendant le sprint 0 avec la story des photos, puis affinée semaine après semaine. Commencer par le sinistre réel, pas par l'écran. Demander ce que l'assuré sait à ce moment-là et ce qu'il ne sait pas encore. Chercher le cas où il n'a pas le document. Ne jamais bloquer une déclaration. Tout y était, écrit par Sofiane à partir des sessions de l'agent, en phrases courtes, numérotées.

— C'est bizarre, a-t-elle dit enfin. De se voir dans un fichier.

Gérard, qui était monté relire une demande rouge, a levé les yeux de son écran.

— Bienvenue au club.

Nadia a souri, puis elle a repris la lecture avec un stylo, et le sourire a disparu.

— C'est faux, là. Je ne pose pas les questions dans cet ordre. Je ne commence jamais par les pièces justificatives. Si on parle de pièces trop tôt, l'assuré croit qu'on le soupçonne. Je commence par ce qui s'est passé, puis par ce qu'il a déjà fait pour limiter les dégâts. Les pièces viennent à la fin.

Sofiane a voulu corriger tout de suite. Julien l'a arrêté.

— Non. Si tu le corriges, c'est encore ta version de sa façon de faire. C'est à elle de le corriger.

C'est ainsi que nous avons ajouté une règle que nous n'avions pas prévue. Chaque skill de la boîte à outils aurait une propriétaire ou un propriétaire : la personne dont elle décrivait le métier. Nadia pour la préparation des stories, Émilie pour les scénarios, Julien et Mathilde pour les relectures, Gérard puis Julien pour le wiki. Toute modification passerait par une demande de fusion, relue et approuvée par la propriétaire, exactement comme le code. Chaque skill porterait un numéro de version, pour que les équipes qui l'utilisaient sachent quand elle changeait, et pourquoi.

— Alors je deviens quoi ? a demandé Nadia. La gardienne de mon propre manuel ?

— La propriétaire de ta façon de faire, a dit Julien. Quand l'équipe d'Horizon s'en servira et qu'elle trouvera une meilleure façon de poser les questions pour la responsabilité civile, c'est à toi qu'elle proposera la modification. Et c'est toi qui diras oui ou non.

Nadia a réfléchi. Je savais à quoi elle pensait, parce que j'y pensais aussi. Un jour, une gestionnaire qu'elle ne connaîtrait pas préparerait une story pour un incendie à Valenciennes, avec une skill qui porterait son nom en bas de page. Elle ne saurait peut-être jamais qui avait décidé qu'on ne parle des pièces qu'à la fin.

Nadia a ouvert une demande de fusion, sa première, et elle a déplacé trois lignes. Sofiane l'a relue et approuvée. Puis Nadia a approuvé sa propre modification en tant que propriétaire, et elle a regardé l'écran un moment, comme on regarde sa signature sur un document officiel.

— Version 1.1, a-t-elle lu à voix haute. C'est moi qui l'ai faite.

## Mercredi, 19 heures

La commission avait validé le socle à 16 h 30. Julien en était revenu avec un titre de référent technique et l'air d'un homme qui se demande s'il a gagné quelque chose. À 19 heures, nous étions les deux derniers sur le plateau. Il est venu s'asseoir sur le bord de mon bureau, comme il ne l'avait jamais fait.

— Tu as laissé ta ligne vide, lundi.

— Je sais.

— Tu veux que je te dise ce que tu fais ?

Je lui ai dit oui, parce que c'était vrai.

— Tu ne pilotes plus rien. On se pilote. Nadia trace les lignes, Émilie écrit les contrats, Sofiane dirige les agents, Mathilde et moi tenons les verrous. Tu n'as pas écrit une story, pas relu une ligne de code, pas pris une seule décision technique depuis un mois.

Il a laissé passer un temps. Il savait ce qu'il faisait.

— Et pourtant, sans toi, on n'en serait pas là. Tu as arrêté toute la chaîne un jeudi après-midi, quand on était à quarante demandes. Tu as convaincu Claire de tout montrer au comité, y compris ce qui ne marchait pas. Tu as écrit au tableau qu'on coupait le périmètre et jamais la qualité. Tu as refusé BMAD à Sofiane et mon refactoring à moi, la même semaine. Tu as mis le parking des bonnes idées au mur. Ça, ce n'est dans aucune case de la liste déroulante.

— C'est la case Scrum Master, ai-je dit. En théorie. Protéger le flux. Enlever les obstacles. Faire respecter les règles que l'équipe s'est données. Dire non au bon moment.

— En théorie, a-t-il répété. Et dans six mois ? Le train a une Release Train Engineer. Isabelle fait ça pour huit équipes. Toi, tu fais quoi ?

Je n'ai pas répondu tout de suite. La question me suivait depuis le lundi, et je l'avais évitée avec soin. Je suis consultant indépendant depuis assez longtemps pour connaître la tentation de ce métier : devenir indispensable, et le rester. On y gagne des missions. On y perd, à la longue, le droit de se regarder dans une glace.

— Je fais en sorte de ne plus servir à rien, ai-je dit.

Julien a souri.

— C'est la meilleure réponse que j'aie entendue de toute la semaine. Mais Claire ne va pas l'aimer.

Claire m'a appelé vingt minutes plus tard, comme si elle avait entendu. Elle sortait d'un dîner de direction et elle marchait, à en juger par le bruit de ses talons sur le pavé du Vieux-Lille.

— Pour la phase 2, je voudrais vous garder. À plein temps, jusqu'à l'été.

— Pas à plein temps, ai-je dit. Trois jours par semaine en janvier et en février, pendant que la phase 2 démarre et que l'équipe s'intègre au train. Deux en mars. Un en avril, après le départ de Gérard. Et plus rien en mai.

Il y a eu un silence, puis le bruit des talons s'est arrêté.

— Vous organisez votre propre départ ?

— Pendant ce temps, je forme celles et ceux qui feront mon travail. Julien pour la technique. Nadia pour la ligne rouge. Isabelle Delattre et son coach d'équipe pour le reste. C'est le seul indicateur que je ne vous ai pas encore montré.

— Lequel ?

— Le jour où l'équipe n'a plus besoin de moi. Si je fais bien mon travail, ce sera en mai.

Elle a ri, pour la première fois depuis le comité.

— Vous êtes le premier consultant qui me négocie moins de jours. Je vais devoir l'expliquer aux achats.

Quand elle a raccroché, j'ai rouvert le modèle d'Isabelle Delattre et j'ai rempli ma ligne. Dans la colonne des rôles, j'ai choisi *Scrum Master* dans la liste déroulante, parce que c'était encore la case la plus proche. Dans la colonne que j'avais ajoutée, j'ai écrit : *protège le flux, dit non au bon moment, prépare son départ. Dégressif jusqu'en mai.*

J'ai relu le tableau entier avant de l'envoyer. Huit lignes pour la phase 2, dont trois personnes que nous n'avions pas encore. Aucun développeur de plus. Et une colonne qui n'existait pas dans le modèle du train, et qui était la seule vraiment intéressante.

## Le carnet de Thomas

**Ce qui s'est passé.** Pour préparer son entrée dans le train Indemnisation, l'équipe a dû remplir un modèle de composition aux rôles classiques. Personne n'y trouvait sa place : en trois mois, le travail s'était déplacé vers les deux bouts de la chaîne. La product owner dit désormais ce qui est juste plus qu'elle ne décrit le besoin. La testeuse écrit le contrat avant le code et explore après. Le développeur dirige les agents et fabrique les outils de l'équipe. Le tech lead relit, tranche et forme. Quand le train a proposé cinq développeurs de plus pour la phase 2, l'équipe a refusé : le code ne représentait que trente-cinq minutes sur cinq heures par story. Elle a demandé à la place une personne du métier, une testeuse et un relecteur qui connaît le cœur de gestion. Ses savoir-faire ont été empaquetés en skills partageables, chacune avec une propriétaire. Le directeur de projet, lui, a planifié son propre départ.

**La leçon.** Les rôles de Scrum restent valables, mais leur contenu change : avec des agents, le travail humain se concentre avant le code (dire ce qui est juste) et après (vérifier que c'est juste). Dimensionnez une équipe augmentée sur sa contrainte, pas sur le volume de code : ajouter des développeurs qui ont chacun un agent ajoute surtout du travail de relecture. Ce qui manque presque toujours, ce sont le métier, la vérification et l'expertise du système existant. Au-delà de six ou sept personnes, scindez l'équipe plutôt que de la grossir. Les savoir-faire que vous transformez en skills ont besoin d'une propriétaire, d'une version et d'une relecture, comme le code. Enfin, un bon accompagnateur mesure aussi le jour où l'on n'a plus besoin de lui.

**Trois questions à poser à votre équipe**

1. Que fait réellement chacun d'entre nous, et nos fiches de poste le disent-elles ?
2. Si l'on nous propose du renfort, savons-nous dire quel rôle nous manque vraiment ?
3. Qui est propriétaire de chacune de nos skills, et qui peut les modifier ?

**Pour aller plus loin.** Manuel, chapitres M5 (skills et sous-agents : écrire une skill à partir d'un savoir-faire), M8 (plugins et marketplaces : distribuer une boîte à outils d'équipe) et M12 (partager en équipe : propriétaires, versions et relectures des skills).
