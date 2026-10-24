# Chapitre 17 — Le savoir de Gérard

## Jeudi, 9 heures

Le jeudi qui a suivi la ligne rouge, Gérard n'était pas là. Sa fille avait accouché dans la nuit, à Arras, et il avait posé un jour de congé à 6 heures du matin par un courriel de deux lignes, dont une pour annoncer le prénom.

C'est ce jour-là, bien sûr, que Sofiane a eu besoin de lui.

La story de nuit devait savoir, au moment de traiter une déclaration en attente, si le contrat de l'assuré était bien en vigueur à la date du sinistre. Le système des contrats renvoyait pour cela un code de statut, une seule lettre. Sofiane a demandé à l'agent de lire les programmes COBOL qui manipulaient ce code et d'en déduire la signification de chaque valeur.

L'agent a lu onze programmes en quelques minutes. Il a rendu un tableau propre, avec une colonne de confiance. *A* : actif. *R* : résilié. *S* : suspendu, probablement pour défaut de paiement, confiance élevée. *X* : signification incertaine, valeur rare, à vérifier.

Sofiane a failli s'en contenter. C'est Julien qui a froncé les sourcils.

— La suspension pour défaut de paiement, c'est ce que Gérard a trouvé dans ta demande rouge, il y a plus d'un mois. Il avait dit que c'était dans un autre champ. Pas dans le statut.

Ils ont passé la matinée à chercher. L'agent a relu les programmes, croisé les valeurs avec la base de recette, proposé deux autres hypothèses, toutes plausibles. Julien a ouvert les vieilles documentations du répertoire partagé : un document de 2001 qui ne parlait pas du code, un autre de 2009 qui en parlait, mais pour dire qu'il était « documenté ailleurs ». Ailleurs, personne ne savait où. À 16 heures, ils ont décidé d'attendre le lendemain. La story de nuit, la plus critique du sprint, avait perdu une journée.

Le vendredi matin, Gérard est arrivé avec des croissants pour tout l'étage et des photos de sa petite-fille sur son téléphone. Julien lui a montré le tableau de l'agent avant même de le féliciter. Gérard a mis ses lunettes.

— *S*, ce n'est pas suspendu. C'est « sans effet » : un contrat annulé depuis l'origine, comme s'il n'avait jamais existé. Une fausse déclaration à la souscription, par exemple. Suspendu, c'est *X*.

— Pourquoi *X* ? a demandé Sofiane.

— Parce qu'en 2003, quand on a ajouté la suspension, le *S* était déjà pris. Et que le chef de projet de l'époque aimait bien les X. Il est parti en 2006. Il n'y a que moi qui m'en souviens.

Il a ri. Personne d'autre n'a ri.

L'agent n'avait pas mal lu. Il avait lu exactement ce que le code disait : une lettre, comparée à d'autres lettres, déclenchant tel ou tel traitement. Le code disait ce qu'il faisait. Il ne disait ni pourquoi, ni ce que ses lettres voulaient dire pour les gens qui les avaient choisies. Cela, c'était dans la tête de Gérard, et nulle part ailleurs.

Julien a ouvert le registre de la dette sur son écran et il l'a fait défiler jusqu'en bas. Ligne vingt-trois. *Savoir du système des contrats détenu par deux personnes, dont une part le 11 avril.*

— Elle vient de nous coûter une journée, a-t-il dit. Le 11 avril, elle nous coûtera tout.

Il s'est tourné vers moi.

— On ne peut plus la laisser dans le registre. Il faut la payer. Maintenant.

J'ai hésité. Nous étions dans le dernier sprint, et j'avais refusé deux jours plus tôt, à Sofiane comme à lui, tout ce qui ressemblait à un chantier nouveau. Mais ce n'était pas une nouvelle méthode pour le portail. C'était une dette, avec un responsable, et la seule échéance de tout le registre qui ne se négocierait pas.

— Une heure par jour, ai-je dit. Pas plus, jusqu'à la fin du sprint. Toi, Gérard, et Sofiane pour l'outil. Et rien qui touche au code du portail.

## Lundi, 14 heures

Le lundi suivant, Sofiane a réuni Julien et Gérard dans la salle Scarpe pour leur présenter une idée qu'il avait lue au printemps. Elle venait d'Andrej Karpathy, un chercheur que les développeurs de sa génération lisaient comme d'autres lisaient autrefois les revues spécialisées. Karpathy l'appelait le LLM Wiki : un wiki écrit et entretenu par le modèle lui-même.

Sofiane l'a dessinée au tableau, en trois couches.

En bas, les sources brutes. Tout ce qui existait déjà, tel quel, sans jamais le modifier : les programmes COBOL, les descriptions de fichiers, les notes de service, les anciennes documentations, l'historique des tickets. Au milieu, le wiki lui-même : des pages courtes, en français, une par notion, par programme, par décision, reliées entre elles par des liens. C'est l'agent qui les écrivait et les tenait à jour. En haut, un fichier de règles, qui disait à l'agent comment tenir ce wiki : quelles pages créer, comment les nommer, comment citer ses sources.

— Et trois opérations, a dit Sofiane. Ingérer : on lui donne une nouvelle source, il la lit, il met à jour toutes les pages qu'elle concerne, il ajoute les liens. Interroger : on lui pose une question, il répond à partir du wiki, en citant les pages, et si la réponse est bonne, elle devient une page à son tour. Contrôler : il relit tout le wiki et cherche ce qui se contredit, ce qui n'est relié à rien, ce qui n'a pas de source.

— La différence avec ce qu'on fait déjà ? a demandé Julien. L'agent sait lire le COBOL. Il l'a lu jeudi.

— Jeudi, il a tout relu depuis le début, et il a deviné. Il refera la même chose demain, et il devinera peut-être autrement. Avec le wiki, ce qui a été compris une fois reste compris. Il ne repart plus de zéro. Et surtout, on peut y mettre ce que le code ne dit pas.

Il a regardé Gérard en disant cela, et Gérard l'a bien vu.

Julien a ajouté ses propres règles au fichier, avant même que le wiki existe. Il les a écrites au tableau, sous le schéma de Sofiane.

*Chaque phrase cite sa source : un programme, un document, ou un entretien daté.*

*Tout ce qui explique un pourquoi reste marqué « à confirmer » tant que Gérard ne l'a pas relu.*

*Quand deux sources se contredisent, on ne choisit pas : on écrit la contradiction sur une page à part.*

*L'agent n'invente jamais. S'il ne sait pas, il écrit qu'il ne sait pas.*

Mathilde, qui passait par là, s'est arrêtée sur le seuil et a ajouté deux conditions. Aucune donnée d'assuré dans les sources : pas d'extrait de fichier réel, pas d'exemple tiré de la production. Et tout restait dans la maison : le dépôt de la DSI, le compte AWS, le socle de la commission.

Gérard n'avait rien dit depuis le début. Il regardait le schéma, les trois couches, et la petite flèche que Sofiane avait dessinée entre le mot *entretien* et le mot *wiki*.

— Si je comprends bien, a-t-il dit, vous voulez me mettre en bouteille.

Il l'a dit sur un ton léger, mais personne ne s'y est trompé. Quarante et un ans de maison. Il partait dans quatre mois, et on lui demandait de vider sa tête dans une machine, comme on vide un bureau.

Julien a pris son temps pour répondre. Il connaissait Gérard depuis vingt ans ; c'est Gérard qui lui avait appris le système des contrats, à son arrivée.

— Non. On veut que ce que tu sais continue à servir quand tu seras dans ton jardin. Aujourd'hui, la seule façon de savoir ce que veut dire un *X*, c'est de t'appeler. Dans un an, il n'y aura plus personne à appeler. Et le jeune qui tombera sur un *X* fera exactement ce que l'agent a fait jeudi. Il devinera.

Gérard a retiré ses lunettes et les a essuyées avec un pan de sa chemise, longuement.

— Et c'est moi qui relis ?

— C'est toi qui relis tout ce qui dit pourquoi. Rien ne passe sans toi.

— Alors d'accord, a dit Gérard. Mais je veux pouvoir le corriger quand il dit des bêtises. Et il en dira.

## Mardi et mercredi, 8 heures

La première nuit, l'agent a ingéré les deux cent quarante programmes du système des contrats, les descriptions de fichiers, et les trois documentations qu'on avait retrouvées dans le répertoire partagé. Le mardi matin, le wiki comptait cent douze pages. La plupart étaient courtes et prudentes. Beaucoup portaient la mention *à confirmer*. Une page à part, intitulée *Questions ouvertes*, en listait soixante-trois.

C'est cette page que Gérard a ouverte en premier.

Nous avions décidé de commencer par des entretiens, une heure chaque matin, à 8 heures, avant que la journée ne dévore tout le monde. L'agent préparait les questions à partir de ce qu'il avait lu et de ce qu'il n'avait pas compris. Sofiane les posait, enregistrait les réponses de Gérard avec son accord, et l'agent les transcrivait, puis les ingérait comme n'importe quelle source, avec la date et le nom de celui qui parlait.

La première question était la plus innocente de la liste.

*Pourquoi les contrats dont le numéro commence par 7 suivent-ils un traitement différent dans quatorze programmes ?*

Gérard a souri, comme on sourit à un souvenir.

— La fusion avec la Mutuelle de l'Artois. Ils avaient leur propre numérotation, leurs propres règles d'échéance, et un directeur général qui ne voulait rien changer pour ses sociétaires. On a gardé leurs numéros, on a mis un 7 devant, et on a ajouté des exceptions partout où c'était nécessaire. C'était provisoire. C'était il y a trente ans.

Il a parlé vingt minutes. De la fusion, des réunions de l'époque, du chef de projet qui aimait les X, d'un week-end de migration où il avait dormi sur deux chaises dans la salle des machines. Une bonne partie n'avait aucun intérêt pour le système des contrats. L'agent a fait le tri sans qu'on le lui demande : une page de décision, *Numérotation des contrats de l'ex-Mutuelle de l'Artois*, avec la cause, la date, les programmes concernés et les quatorze exceptions, chacune reliée au programme qui l'appliquait.

Le lendemain, Gérard a relu la page. Il y a corrigé une seule chose : la fusion avait été votée en 1994, mais elle avait pris effet le 1er janvier 1995. L'agent avait retenu la date du vote. Gérard a eu l'air satisfait de l'avoir pris en défaut.

— Vous voyez. Il dit des bêtises.

— Une bêtise sur quarante lignes, a dit Sofiane.

— C'est exactement ce que je disais.

Le mercredi, il est arrivé avec un sac en toile. Il en a sorti trois cahiers à spirale, à la couverture défraîchie. Il en avait trente et un chez lui, de 1986 à aujourd'hui, et il avait passé la soirée à choisir. Mathilde avait posé une condition : il ne prendrait que des pages techniques, sans aucun nom d'assuré, et c'est lui qui les choisirait. Il en avait marqué une trentaine avec des papillons jaunes.

Sofiane les a photographiées une par une. L'agent a lu l'écriture de Gérard mieux que je ne l'aurais fait. Sur une double page de 1997, il y avait un schéma dessiné au crayon : la transaction qui lisait un contrat à une date donnée, celle qui nous avait sauvés le jour de la franchise. Des flèches, des boîtes, et, dans un coin, une note soulignée deux fois : *attention avenants du jour même*.

— Je l'avais oubliée, celle-là, a dit Gérard. Je me demande bien ce que je voulais dire.

L'agent ne le savait pas non plus. Il l'a écrit, honnêtement, dans les questions ouvertes.

Ce soir-là, Julien m'a montré l'une des pages que Gérard avait relues et validées. Elle tenait sur un écran.

> **Statut du contrat**
>
> *A* : actif. *R* : résilié. *S* : sans effet, c'est-à-dire annulé depuis l'origine, par exemple pour fausse déclaration à la souscription. *X* : suspendu, depuis 2003, à la suite d'une vente du logement ou d'un changement de situation.
>
> Pourquoi *X* : en 2003, la lettre *S* était déjà prise. Source : entretien avec Gérard Vandamme. *Confirmé.*
>
> Attention : la suspension pour impayé ne figure pas dans ce statut. Voir *Suspension pour impayé*, champ distinct.
>
> Lu par quatorze programmes. Voir aussi : *Contrat en vigueur à une date*, *Avenant*, *Fusion avec la Mutuelle de l'Artois*.

Gérard avait ajouté lui-même, à la main, la dernière ligne qui renvoyait vers la fusion. Il commençait, je crois, à considérer ce wiki comme le sien.

## Jeudi, 8 heures

Le jeudi matin, Sofiane a lancé pour la première fois la troisième opération, celle que Karpathy appelait le contrôle. L'agent a relu les cent soixante pages du wiki, une par une, en les confrontant entre elles et à leurs sources. Il a rendu une liste de sept contradictions.

Nous en connaissions cinq. La date retenue pour un vol, que la note de service de 2009 et le COBOL ne fixaient pas de la même façon, et que Nadia et Gérard avaient tranchée le jour de la franchise. La franchise unique ou par garantie quand un même sinistre en déclenche plusieurs, toujours en attente de la réponse de la direction technique. Deux libellés différents pour un même code. Une coquille dans une vieille documentation. Une règle d'échéance propre aux contrats de l'ex-Artois, déjà connue de Gérard.

La septième était sans importance, un libellé d'écran que Gérard a tranché en dix secondes. La sixième, en revanche, n'était connue de personne.

Deux programmes calculaient différemment le moment où un avenant prenait effet. Le programme d'indemnisation considérait que l'avenant s'appliquait dès 0 heure le jour de sa date d'effet. Un programme du système des contrats, modifié en mars 2011 lors d'une correction urgente, ne l'appliquait qu'à partir du lendemain. Et la transaction qui lisait un contrat à une date donnée, celle que le portail utilisait depuis le jour de la franchise, s'appuyait sur ce second programme.

Gérard a lu la page deux fois. Puis il a demandé à Sofiane d'afficher la modification de 2011, avec son auteur. C'était un prestataire, parti depuis longtemps.

— Je n'ai jamais vu ça, a-t-il dit lentement. En mars 2011, j'étais en congé trois semaines, pour le mariage de ma fille.

Il a sorti de son sac le cahier de 1997, l'a ouvert à la page du schéma, et il a posé le doigt sur la note soulignée deux fois. *Attention avenants du jour même.*

— Voilà ce que je voulais dire. Je l'avais écrit pour ne pas tomber dans le piège. Quelqu'un est tombé dedans quatorze ans plus tard, pendant que je dansais à Arras.

Nadia a ouvert les conditions générales. Elles étaient claires : l'avenant prend effet à 0 heure, le jour indiqué aux conditions particulières. Le programme de 2011 avait tort. Pour un sinistre survenu le jour même de la date d'effet d'un avenant, le portail aurait lu les anciennes conditions particulières, et le service indemnisation les nouvelles. Le cas était rare. Il existait pourtant depuis 2011, dans la gestion courante de la maison, et personne ne l'avait jamais vu, parce que personne n'avait jamais lu ces deux programmes en même temps.

L'agent non plus, d'ailleurs, jusqu'à ce qu'on lui demande de tout relire d'un coup. Il n'était pas plus intelligent que Gérard. Il avait seulement une mémoire où tout se trouvait au même endroit, et une consigne qui lui interdisait de choisir entre deux sources qui se contredisaient.

Nadia a écrit la règle F2 dans le dossier des règles du portail, avec Gérard comme second validateur. Sofiane a corrigé l'appel du portail dans la matinée : c'était une story au-dessus du ruban rouge, puisqu'elle touchait à la franchise. Pour le programme de 2011, en revanche, ce n'était pas à nous de le corriger. Le cœur de gestion appartenait à Horizon. Julien a envoyé la page du wiki à l'instance commune, avec la règle et la source.

Franck Ryckebusch est monté lui-même dans l'après-midi. Il tenait sous le bras un classeur de quatre cents pages, à l'en-tête de son ESN : le dossier de rétro-documentation du système des contrats, que ses équipes avaient écrit en dix-huit mois en relisant le COBOL programme par programme.

— On n'avait pas trouvé ça, a-t-il dit. Ni le pourquoi du *X*, ni les avenants du jour même.

Il a posé le classeur sur la table.

— Laurent me demande si votre agent pourrait lire ce dossier. Comme une source de plus.

— Comme une source, oui, a dit Julien. Jamais comme la vérité. Le contrôle le comparera au reste, et on verra ce qui se contredit.

Ryckebusch a hoché la tête. Il avait l'air d'un homme qui vient d'apprendre qu'un travail de dix-huit mois servira enfin à quelque chose, et qui ne sait pas encore s'il doit s'en réjouir.

Avant de partir, ce soir-là, Sofiane a demandé à Gérard de faire un essai. Il a posé au wiki la question que tout le monde, dans la maison, avait un jour posée à Gérard. *Comment savoir si un contrat est en vigueur à une date donnée ?*

La réponse est arrivée en quarante secondes. Une demi-page, claire, qui citait six pages du wiki : le statut et ses quatre lettres, la suspension pour impayé dans son champ à part, les avenants et leur date d'effet à 0 heure, la règle F2, l'exception des contrats de l'ex-Artois, la transaction de 1997.

Gérard l'a lue deux fois, ses lunettes au bout du nez.

— C'est juste, a-t-il dit.

Il est resté un moment sans rien ajouter.

— Ça fait quarante ans qu'on me pose cette question. C'est la première fois que la réponse restera quand je ne serai plus là.

Julien a fait défiler la page des questions ouvertes jusqu'en bas. Il en restait trente et une. La dernière, l'agent l'avait trouvée dans un vieux ticket de 2008, et personne n'avait eu le cœur de la retirer.

*Où sont rangées les clés de l'armoire à listings ?*

Gérard a remis ses lunettes dans sa poche de chemise.

— Ça, a-t-il dit, il ne le saura jamais.

## Le carnet de Thomas

**Ce qui s'est passé.** Un jour d'absence du dernier expert COBOL a coûté une journée à la story la plus critique du sprint : l'agent avait lu le code et deviné le sens d'une lettre, plausiblement et à tort. La dette de connaissance inscrite au registre a donc été traitée tout de suite, une heure par jour. Sur le modèle du LLM Wiki d'Andrej Karpathy, l'agent a ingéré les programmes et les documentations existants, puis interrogé l'expert sur ce que le code ne dit pas, et tenu à jour un wiki de pages courtes et reliées, chaque affirmation citant sa source. L'expert relisait tout ce qui expliquait un pourquoi. Le premier contrôle de cohérence a fait apparaître une contradiction que personne ne connaissait : deux programmes appliquaient différemment la date d'effet d'un avenant depuis 2011. Le programme d'Horizon a demandé à verser son propre dossier de rétro-documentation dans le wiki, comme une source de plus.

**La leçon.** Le code dit ce qu'il fait ; il ne dit ni pourquoi, ni ce que ses conventions signifiaient pour ceux qui les ont choisies. Un agent qui relit le code à chaque question repart de zéro et devine ; un wiki qu'il tient à jour garde ce qui a déjà été compris. Organisez-le en trois couches : les sources brutes, jamais modifiées ; les pages du wiki, écrites par l'agent ; et des règles qui lui imposent de citer ses sources, d'avouer ce qu'il ne sait pas et de ne jamais trancher seul une contradiction. Commencez par ceux qui partent : un savoir qui s'en va à date fixe est une dette avec une échéance non négociable. Et faites de l'expert le relecteur de son propre savoir, pas sa source anonyme.

**Trois questions à poser à votre équipe**

1. Qui, chez nous, est le seul à savoir pourquoi une règle ou un code existe, et quand part-il ?
2. Quand notre agent ne sait pas, l'écrit-il, ou devine-t-il ?
3. Quelles sources se contredisent sans que personne ne les ait jamais lues ensemble ?

**Pour aller plus loin.** Manuel, chapitre M11 (le wiki d'équipe à la Karpathy : sources, pages, règles ; ingestion, interrogation, contrôle de cohérence ; application au legacy et aux décisions).
