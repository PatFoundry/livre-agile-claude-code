# Chapitre 25 — Deux vérités

## Lundi 26 janvier, 9 heures

Le découpage aurait dû se terminer pendant la première itération. Il commençait le premier jour de la deuxième, avec quelques jours de retard dus à une adresse, et personne ne s'en plaignait.

C'était la dernière étape avant le code. Un agent devait lire le document d'exigences, l'architecture et ses décisions, puis découper le travail en epics et en stories. La méthode appelle cet agent le scrum master, ce qui avait fait sourire Sylvie. Il ne devait pas produire des stories au sens où nous l'entendions depuis septembre, trois lignes et un critère d'acceptation, mais des stories autoportantes : chacune un fichier dans le dépôt, contenant tout ce qu'il fallait pour la construire, sans relire les neuf pages d'exigences ni les quatorze pages d'architecture. Ni l'agent qui la coderait, ni l'humain qui la relirait n'auraient à chercher ailleurs.

Il a fallu une matinée à l'agent pour proposer six epics et trente-huit stories. Il a fallu le reste de la journée à Nadia, Émilie et Julien pour les relire. Nadia décidait si chaque story disait la bonne chose. Émilie y verrouillait ses scénarios, comme l'exigeait depuis octobre le huitième point de notre définition de « prêt ». Julien vérifiait le classement en vert, orange ou rouge. Celle que je montre encore aujourd'hui, quand on me demande ce qu'est une story autoportante, est la 3.4.

> **Story 3.4 — Choisir l'adresse du risque** · epic 3 : déclarer un bris de glace · propriétaire : Nadia Benali
>
> *Besoin.* En tant qu'assuré dont le contrat couvre plusieurs logements ou bâtiments, je choisis celui où le sinistre a eu lieu, afin que ma déclaration soit traitée à la bonne adresse.
>
> *Exigences :* EF-35 (source : test de caractérisation n° 23). *Décisions :* DA-02, DA-04.
>
> *Ce que fait le système des contrats :* l'adresse du risque est dans le segment des garanties ; l'ancienne Artois l'écrit sur deux lignes (test n° 7).
>
> *Scénarios d'acceptation (verrouillés) :* 3.4-a, une seule adresse, préremplie ; 3.4-b, trois adresses, choix obligatoire ; 3.4-c, aucune ne correspond, saisie libre signalée au gestionnaire ; 3.4-d, parcours au lecteur d'écran.
>
> *Hors périmètre :* modifier une adresse du contrat.
>
> *Dépendances :* aucune autre équipe. *Classement :* rouge (lecture du système des contrats).

Sylvie est arrivée à 11 heures, son ordinateur ouvert sur le tableau Jira de l'équipe. Elle l'avait construit le week-end du PI Planning, à partir des photos du mur : vingt-quatre stories, une par post-it. Elle l'a posé à côté de l'écran où défilaient les trente-huit fichiers de l'agent.

Nous avons comparé pendant une demi-heure. Onze stories se ressemblaient, à peu de chose près, sous des titres différents. Treize n'existaient que dans Jira : des découpages du mois de janvier que les exigences et l'architecture avaient rendus caducs. Vingt-sept n'existaient que dans le dépôt. Et une story de Jira s'intitulait toujours *Mandat d'un proche, six mois*, d'après un post-it du PI Planning, alors que Claire avait décidé un an.

— Il y a même une troisième liste, a dit Julien. La méthode tient son propre fichier de suivi dans le dépôt, avec un statut pour chaque story. Personne ne le regarde, mais l'agent le met à jour.

Sylvie a refermé à moitié son ordinateur.

— Depuis le 10 janvier, a-t-elle dit, je passe une heure chaque soir à recopier le dépôt dans Jira. Le comité lit Jira. Le bureau des projets lit Jira. L'audit interne lit Jira. Et chaque matin, ce que j'ai recopié la veille est déjà faux.

Personne n'a rien dit. Elle me l'avait laissé entendre deux fois, en décembre puis la semaine précédente, et deux fois je lui avais répondu que le contenu était dans le dépôt, comme si cela réglait la question. À l'automne, Nadia portait encore cent quatre dossiers sans que personne les compte, pendant que nous mesurions notre vélocité. En janvier, Sylvie recopiait chaque soir un dépôt pendant que nous écrivions des règles sur les sources. Nous n'avions pas appris à regarder ce que notre façon de travailler coûtait à ceux qui n'écrivaient pas de code.

## Mercredi 28 janvier, 10 heures

Le mercredi matin se tenait le point de synchronisation du train : une demi-heure, debout, devant le mur du PI Planning, qu'Isabelle Delattre avait fait reconstituer dans un couloir du deuxième étage. Un représentant par équipe. Chacun disait où il en était de ses objectifs et de ses dépendances.

Céline Dufour, la product owner de l'espace adhérent, a parlé la quatrième. Son équipe était en avance. Le mandat d'un proche serait prêt dès le milieu de l'itération : enregistrement, consentement de l'assuré, révocation, et une date de fin calculée automatiquement, six mois après la création.

— Un an, ai-je dit. La durée a été décidée le 15 janvier par Claire Vasseur. C'est dans le document d'exigences.

Céline m'a regardé sans comprendre.

— Je n'ai pas accès à votre document d'exigences. J'ai votre story dans Jira. Elle dit six mois.

Isabelle a laissé passer deux secondes de silence, ce qui, dans un point de synchronisation, est très long. La correction coûterait une demi-journée à l'équipe de Céline : un paramètre, ses tests, une relecture. Découverte en homologation, au printemps, elle aurait coûté la reprise de tous les mandats déjà enregistrés.

— Combien de vérités avez-vous, exactement ? m'a demandé Isabelle quand les autres sont repartis.

— Trois, ai-je dit. C'est deux de trop.

À 14 heures, Sylvie m'a transféré un courriel d'Hélène Carpentier, la responsable du bureau des projets de la DSI. Il était courtois, court et sans appel. *Conformément à la procédure, l'ensemble des stories du projet doit être saisi dans Jira, description et critères d'acceptation compris, avant la revue de portefeuille de vendredi. L'audit interne s'appuiera sur Jira pour sa revue de conformité DORA en mars.*

J'ai lu le courriel à voix haute dans la salle Lys. Julien a posé son café.

— Alors on écrit deux fois chaque story ?

— Pas *on*, a dit Sylvie. Moi.

— Le dépôt trace mieux que Jira, a dit Julien. Chaque modification d'une story a un auteur, une date et une relecture. Dans Jira, n'importe qui change un critère d'acceptation, et personne ne le voit.

— Personne au comité ne sait ouvrir un dépôt, a répondu Sylvie. Ni au bureau des projets. Ni à l'audit. Ils veulent un endroit, pas deux.

Ils avaient raison tous les deux, et ils le savaient. C'est Mathilde, depuis le bout de la table, qui a déplacé la question.

— L'audit ne veut pas un endroit, a-t-elle dit. Il veut une trace qu'il peut suivre. Il se moque de l'outil, à condition de ne jamais tomber sur deux versions de la même chose.

J'ai proposé une réunion le lendemain, à 14 heures, avec Isabelle et Hélène Carpentier. Sylvie a demandé si elle pouvait, en attendant, ne pas recopier le dépôt ce soir-là. J'ai dit oui. C'était la moindre des choses.

## Jeudi 29 janvier, 14 heures

Hélène Carpentier est arrivée à l'heure, avec un carnet et sans ordinateur. Je m'attendais à une gardienne de procédure. J'ai trouvé une femme qui pilotait quarante projets et qui n'avait qu'un seul endroit pour les comparer.

— Je ne demande pas Jira par amour de Jira, a-t-elle dit avant même de s'asseoir. Je le demande parce que c'est le seul outil où je peux mettre quarante projets côte à côte. Si chacun invente le sien, je ne pilote plus rien.

Isabelle Delattre, Sylvie, Julien, Nadia, Mathilde et Sofiane étaient autour de la table. J'avais tracé au tableau trois colonnes : *l'information*, *qui l'écrit*, *qui la lit*. Je n'avais rien préparé d'autre.

Nous avons rempli le tableau ligne par ligne, et la discussion a changé de nature dès la deuxième. Le contenu d'une story, ses exigences, ses scénarios : écrits par Nadia et l'agent, relus par Julien et Émilie, lus par l'agent qui code, par les relecteurs, par l'équipe de l'espace adhérent, et par l'audit. Son statut : produit par le travail lui-même, lu par Sylvie, Isabelle, Hélène et le comité. Sa priorité et son itération : décidées par Nadia, lues par tout le monde. Les dépendances entre équipes et les objectifs du PI : tenus par le train, lus par le train. Les anomalies de production : écrites par les gestionnaires et le support, lues par nous.

— Les critères d'acceptation, a dit Hélène en regardant la première ligne, je ne les lis jamais. Je veux savoir où en est chaque story, et si elle est en retard.

— L'audit, lui, les lira, a dit Mathilde. Pour chaque changement mis en production, il voudra remonter jusqu'à l'exigence, savoir qui l'a décidée, qui a relu le code, et quel test l'a vérifié. Le dépôt garde tout cela mieux que n'importe quel outil de la maison. Il faut seulement que l'auditeur sache par où entrer.

C'est à ce moment que Julien a lâché ce qu'il défendait depuis la veille.

— Le statut dans Jira, je peux vivre avec, a-t-il dit. Tant que personne n'y écrit un critère d'acceptation.

Et Sylvie a lâché le sien.

— Le contenu dans le dépôt, je peux vivre avec. Tant que je ne recopie plus une seule ligne.

La règle tenait en une phrase, que j'ai écrite au-dessus du tableau : *une information, un seul endroit ; partout ailleurs, un lien.* Nous l'avons déclinée en quatre lignes avant 15 heures.

*Le contenu d'une story vit dans le dépôt. Il ne se modifie que par une demande de fusion relue.*

*Le pilotage vit dans Jira : statut, priorité, itération, dépendances, anomalies.*

*Chaque story a un fichier et un ticket. Le ticket porte un résumé de deux lignes et un lien vers le fichier, jamais le texte.*

*Personne ne recopie. Ce qui passe d'un outil à l'autre passe tout seul.*

Restait à rendre la dernière ligne vraie. Sofiane a expliqué comment, et c'était moins compliqué qu'on ne le craignait. Quand Nadia validait un fichier de story dans le dépôt, l'agent créerait le ticket dans Jira, par le connecteur qu'il utilisait déjà en lecture depuis l'automne, avec le titre, le résumé, le lien et le rattachement à la feature du train. La clé du ticket figurerait dans le nom de la branche, dans chaque commit et dans la demande de fusion ; l'intégration entre GitHub et Jira ferait alors avancer le statut toute seule, de *en cours* à *en relecture*, puis à *terminé* quand la fusion était faite et les scénarios verts. Avant de prendre une story, l'agent lirait sa priorité et son itération dans Jira. Le fichier de suivi de la méthode, la troisième vérité, serait supprimé.

— Et les vingt-quatre tickets du PI Planning ? a demandé Isabelle.

— Clôturés, a dit Nadia, chacun avec un lien vers ce qui le remplace. Je ne veux pas qu'on les perde. Je veux qu'on arrête de les croire.

Mathilde a accordé un accès en lecture au dépôt aux équipes du train et à l'audit interne, rien de plus. Hélène a refermé son carnet.

— Vendredi, à la revue de portefeuille, je veux voir vos trente-huit tickets, a-t-elle dit. Si je les vois sans que Sylvie ait tapé une ligne, je présenterai votre règle aux autres projets.

## Vendredi 30 janvier, 17 heures

Sofiane avait écrit la passerelle le jeudi après-midi, avec l'agent, et Julien l'avait relue avant 18 heures. Le vendredi à 9 heures, Nadia a validé les trente-huit fichiers de stories. À 9 h 12, il y avait trente-huit tickets dans Jira. Chacun portait un titre, deux lignes de résumé, un lien vers son fichier, et une mention en tête de la description : *Le contenu fait foi dans le dépôt. Ne pas le modifier ici.*

Il y a eu une erreur, une seule, et elle tombait bien. L'agent avait rattaché trois stories à la mauvaise feature du train : il en existait deux aux noms presque identiques, *Déclaration accompagnée* et *Déclaration assistée*, créées par deux équipes différentes au PI Planning. Sylvie a corrigé les trois rattachements dans Jira, en deux minutes. C'était du pilotage ; c'était donc à Jira, et à elle. Elle n'avait rien eu à recopier.

À 10 heures, l'agent a commencé la story 3.4 sur une branche qui portait la clé de son ticket. Sylvie avait gardé Jira ouvert sur son écran. Quand la demande de fusion s'est ouverte, le statut est passé à *en cours*. Quand Antoine a commencé sa relecture, il est passé à *en relecture*. Sylvie n'avait touché à rien. Elle a regardé l'écran un long moment, comme on regarde un appareil qu'on soupçonne de tricher.

La revue de portefeuille avait lieu à 15 heures. Sylvie y est allée seule. Elle est revenue à 16 h 30 et m'a raconté la séance en trois phrases. Hélène Carpentier avait affiché nos trente-huit tickets devant les chefs de projet de la DSI, puis la règle, mot pour mot. Deux projets avaient demandé si elle était obligatoire ; Hélène avait répondu que non. Et à la fin, elle avait posé une question à laquelle Sylvie n'avait pas su répondre.

— Elle m'a demandé notre vélocité, a dit Sylvie. Elle ne la trouve nulle part dans Jira. Je lui ai dit que nous n'en avions plus vraiment. Elle a dit qu'on en reparlerait la semaine prochaine, et que le contrôle de gestion voudrait en parler aussi.

Je n'ai pas répondu. C'était une autre histoire, et elle viendrait à son heure.

À 17 h 30, Sylvie a éteint son ordinateur et pris son manteau. C'était la première fois depuis le 10 janvier qu'elle partait avant la nuit. Elle s'est arrêtée à mon bureau, a sorti son carnet, et l'a ouvert à la page du 18 décembre. Il n'y avait qu'une ligne, de son écriture serrée : *Brief → Jira ?*

Elle l'a barrée devant moi, d'un seul trait, et elle est partie.

Deux vérités, ce n'est pas une de trop par principe. C'est une de trop parce que quelqu'un, quelque part, paie l'écart entre les deux. Ce mois-là, c'était Sylvie, chaque soir, sans que nous le voyions. Et c'était l'équipe de Céline Dufour, sans le savoir.

## Le carnet de Thomas

**Ce qui s'est passé.** À partir des exigences et de l'architecture, un agent a découpé le travail en six epics et trente-huit stories autoportantes, chacune dans un fichier du dépôt, avec ses exigences, ses décisions, ce que fait le système existant, ses scénarios verrouillés, son hors-périmètre et son classement de risque. En les comparant au tableau Jira construit au PI Planning, l'équipe a découvert trois listes divergentes, en comptant le fichier de suivi de la méthode, et une coordinatrice qui recopiait chaque soir le dépôt dans Jira depuis trois semaines. Une équipe voisine avait construit un mandat de six mois d'après Jira, alors que la sponsor avait décidé un an. Le bureau des projets a exigé toutes les stories dans Jira, le tech lead a défendu le dépôt, et tous deux avaient raison. Une réunion a rempli un tableau simple, qui écrit et qui lit chaque information, et en a tiré une règle : une information, un seul endroit, partout ailleurs un lien. Le contenu vit dans le dépôt, le pilotage dans Jira, et la passerelle entre les deux est automatique.

**La leçon.** Une méthode pilotée par les spécifications produit des documents dans le dépôt ; l'entreprise, elle, pilote dans ses outils. Ne choisissez pas l'un contre l'autre : pour chaque information, demandez qui l'écrit et qui la lit, puis donnez-lui une seule maison. Le contenu d'une story gagne à vivre avec le code, relu comme lui, tracé comme lui ; le statut, la priorité et les dépendances appartiennent à l'outil que lisent ceux qui pilotent. Tout ce qui doit passer de l'un à l'autre passe automatiquement, sinon quelqu'un le paiera chaque soir, et vous ne le verrez pas. Une story autoportante sert d'abord l'agent qui la code ; elle sert aussi l'équipe voisine et l'auditeur, à condition qu'ils puissent la lire.

**Trois questions à poser à votre équipe**

1. Combien d'endroits disent aujourd'hui ce que doit faire une même story ?
2. Qui, dans notre entourage, recopie une information d'un outil à l'autre, et depuis quand ?
3. Une équipe voisine qui dépend de nous lit-elle la même version que nous ?

**Pour aller plus loin.** Manuel, chapitres M7 (MCP : le connecteur Jira de l'agent), M9 (BMAD : stories autoportantes, remplacer le fichier de suivi de la méthode) et M10 (GitHub et Jira au quotidien : la clé du ticket dans la branche, le statut qui avance tout seul).
