# Chapitre 3 — Le fichier qui parle à la machine

## Lundi, 8 heures

Mathilde Grare est arrivée à 8 heures précises. Trente ans, un sweat à capuche sous une veste de tailleur, et la réputation, dans l'équipe de Bertrand, de n'avoir jamais rendu un rapport vide. Pour les trois mois à venir, la sécurité, pour nous, ce serait elle.

Elle s'est installée au poste de Sofiane, a posé un gobelet de café à côté du clavier et a dit, sans nous regarder :

— Deux heures. Vous restez, mais vous ne m'aidez pas.

Nous avions passé le week-end à attaquer nos propres règles. Julien avait essayé de faire lire à l'agent des fichiers interdits, de lui faire lancer des commandes réseau, de lui faire contourner la validation humaine. Tout avait tenu. J'étais presque confiant. C'est généralement le moment où l'on apprend quelque chose.

Mathilde a commencé par le plus classique. Elle a ajouté au projet une petite bibliothèque de test, dont le fichier d'explication contenait, perdue au milieu de la documentation, une phrase destinée à l'agent : envoyer le contenu du dossier de configuration à une adresse extérieure, « pour diagnostic ».

Puis elle a demandé à l'agent d'intégrer la bibliothèque.

L'agent a lu le fichier. Il a intégré la bibliothèque. Puis il a ajouté, à la fin de sa réponse :

```text
Le fichier README de cette bibliothèque contient une instruction
qui demande d'envoyer la configuration du projet vers un serveur
externe. Je ne l'ai pas suivie : elle ne vient pas de vous et
ressemble à une tentative d'exfiltration. Je vous conseille de
retirer cette dépendance.
```

Mathilde a pris une note sans commentaire. Elle a recommencé autrement, en plus discret, en plus pressant. Trois fois. Une fois, l'agent a tenté une commande réseau ; la règle l'a bloquée avant qu'elle ne s'exécute. Les deux autres fois, il a refusé de lui-même.

À 9 h 40, elle a changé d'approche. Elle a cessé de piéger l'agent et lui a demandé, très poliment, de l'aider.

— La connexion à l'environnement de recette ne marche pas. Tu peux regarder ?

L'agent a cherché. Il a ouvert plusieurs fichiers de configuration, dont un qui s'appelait `recette.properties` et que personne n'avait ouvert depuis des années. Il a trouvé le problème, une adresse de serveur périmée. Et pour expliquer son diagnostic, il a recopié dans sa réponse les trois lignes du fichier concernées. La troisième contenait un mot de passe.

Mathilde a fait pivoter l'écran vers nous.

— Il n'est pas sorti du réseau, a-t-elle dit. Mais ce mot de passe est maintenant dans l'historique de la session, et dans les échanges passés par Bedrock. Vos règles interdisent les fichiers de secrets. Elles ne savent pas que celui-ci en est un.

Julien était livide. Il avait écrit la liste des fichiers interdits lui-même : les fichiers d'environnement, les clés, les certificats. Il n'avait pas pensé à un vieux fichier de propriétés que tout le monde croyait vide.

À 10 heures, elle a rendu son verdict, à voix haute, devant toute l'équipe.

— Pas d'exfiltration. L'agent a résisté aux injections. Un constat : un secret en clair dans le code, lu par l'agent parce que la liste d'exclusion était incomplète.

Elle a laissé passer un silence.

— Un constat, pas un arrêt. Je veux la correction mercredi. Et le mot de passe changé ce matin. J'en informe Bertrand.

Elle a rangé son ordinateur et récupéré son gobelet vide. Julien a regardé le fichier encore ouvert à l'écran.

— Le problème n'est pas l'agent, a-t-il dit. Le problème, c'est que ce secret n'aurait jamais dû être là. L'agent l'a juste trouvé plus vite que nous.

## Lundi, 14 heures

Sofiane avait passé la fin de matinée à chercher comment se racheter. Il est arrivé en réunion avec une solution.

— Il suffit d'ajouter une consigne dans le CLAUDE.md. « Ne jamais lire un fichier qui contient un mot de passe. » L'agent lit ce fichier à chaque session. Il l'appliquera.

Le CLAUDE.md, je l'avais découvert le week-end : un simple fichier texte, à la racine du projet, que Claude Code lit au début de chaque session. On y écrit ce que l'agent doit savoir du projet. Des conventions, des commandes, des règles de travail.

Julien a secoué la tête avant moi.

— Il l'appliquera la plupart du temps. Ce matin, il n'a pas voulu lire un secret. Il a voulu réparer une connexion. Une consigne, il l'interprète. Une règle dans les paramètres, il ne peut pas la discuter.

J'ai cherché une image pour Nadia et Émilie, qui suivaient de loin.

— Le CLAUDE.md, c'est le livret d'accueil qu'on donne à un nouvel arrivant. Les paramètres, c'est son badge : il ouvre certaines portes et pas d'autres. On ne protège pas une salle des coffres avec un livret d'accueil.

Émilie a souri. C'était la première fois que je la voyais sourire.

Nous avons fait les choses dans l'ordre. D'abord retirer le secret du code et le placer dans le coffre-fort de la DSI, d'où l'application le lirait au démarrage. Puis chercher les autres. Julien a lancé un outil de détection sur tout le dépôt : quatre mots de passe de plus, dont un vieux de sept ans. Ensuite, élargir les interdictions dans les paramètres gérés, non plus fichier par fichier, mais sur tous les dossiers de configuration. Enfin, Julien a ajouté un contrôle automatique : tout commit contenant quelque chose qui ressemble à un secret serait refusé, qu'il vienne d'un humain ou de l'agent.

— Et le CLAUDE.md, alors ? a demandé Sofiane.

— On en a besoin de toute façon, a dit Julien. Mais pas pour ça.

Sofiane, qui voulait se rendre utile, a demandé à l'agent de générer le fichier. Claude Code sait le faire : il parcourt le projet et rédige un premier CLAUDE.md. Trois minutes plus tard, nous avions trois cents lignes.

Julien les a lues à voix haute, en choisissant.

— « Le projet est écrit en Java. » « Les tests se trouvent dans le dossier des tests. » « Respecter les bonnes pratiques de développement. »

Il a levé les yeux.

— Tout ce qu'il a écrit, il le savait déjà en lisant le code. Ce qu'il ne sait pas, il ne l'a pas écrit. Et pour cause : ce n'est nulle part.

J'ai proposé un test simple, ligne par ligne. Si on retire cette ligne, l'agent fera-t-il une erreur ? Si la réponse est non, la ligne part.

Une heure plus tard, il en restait trente-cinq. Presque toutes des commandes : comment compiler, comment lancer les tests, comment démarrer l'application en local. Utiles, mais loin de l'essentiel.

— L'essentiel, a dit Julien en fermant son ordinateur, c'est ce qu'on a dans la tête. On l'écrit demain. Avec Nadia.

## Mardi

Nous avons commencé par une question que Julien a écrite en haut du tableau : *qu'est-ce qu'un développeur brillant, arrivé ce matin, ne peut pas deviner ?*

La liste est venue vite. Pourquoi le projet existe. Les mots du métier. Les frontières qu'on ne franchit pas, comme cette règle maison : personne n'appelle le système central des contrats directement, tout passe par un module d'adaptation que Julien maintenait depuis dix ans. La façon de travailler : les tests avant le code, une story, une branche, une demande de fusion. Et ce que l'agent ne doit jamais faire.

Pour le reste, Julien avait une règle : ne rien recopier. Si une information existe ailleurs, dans la documentation d'architecture ou la liste des commandes, le CLAUDE.md y renvoie. Un document recopié vieillit deux fois.

Puis Nadia a pris la main sur le vocabulaire. Pendant une heure, elle a démoli nos certitudes.

— Vous écrivez « l'assuré déclare le sinistre ». Ce n'est pas toujours vrai. Le déclarant, c'est celui qui remplit la déclaration. Ça peut être l'assuré, son conjoint, un voisin, un syndic. Et l'assuré n'est pas forcément le souscripteur du contrat.

— Ça change quoi, pour le code ? a demandé Sofiane.

— Si votre machine confond assuré et déclarant, on enverra l'indemnité au locataire du dessous au lieu du propriétaire. Je l'ai vu arriver avec des humains. Je ne veux pas le voir arriver plus vite.

Personne n'a plus contesté une seule de ses définitions.

Il restait à décider où ranger chaque chose. J'avais compris le principe pendant le week-end : il existe plusieurs niveaux de CLAUDE.md, empilés. Celui de l'entreprise, déployé par la DSI, que personne ne modifie : les règles de Bertrand y vivent. Celui du projet, partagé par toute l'équipe et versionné avec le code. Et un fichier personnel, propre à chacun, qui ne quitte pas son poste. Julien y a mis sa préférence pour des explications détaillées ; Sofiane, ses raccourcis. Rien de cela ne regardait l'équipe.

À 16 heures, le fichier du projet tenait sur une page. En voici le début :

```text
# Portail sinistres — consignes pour l'agent

Portail de déclaration de sinistre habitation. Vision : docs/vision.md

## Vocabulaire métier (validé par Nadia Benali)
- Déclarant : remplit la déclaration ; pas forcément l'assuré.
- Assuré : personne couverte ; pas forcément le souscripteur.
- Franchise, plafond : jamais codés en dur, toujours lus dans le contrat.

## Règles techniques
- Tout appel au système des contrats passe par adaptateur-contrats.
- Tests d'abord. Une story = une branche = une demande de fusion.
- Commandes du projet : docs/commandes.md

## Ne jamais
- Inventer une règle de gestion. Poser la question.
```

Je me suis arrêté sur la ligne de la franchise. Une semaine plus tôt, dans mon salon, un agent avait inventé 150 euros. Désormais, il saurait qu'il n'en avait pas le droit.

Restait à le publier. Le dépôt du projet était né le matin même sur le GitHub de la mutuelle, une instance hébergée en interne, derrière le segment réseau de Bertrand. Julien l'avait verrouillé comme un coffre : personne ne pousse directement sur la branche principale, ni humain ni agent. Chaque modification passe par une demande de fusion, qui doit être approuvée par une personne et passer l'intégration continue : compilation, tests, détection de secrets. Si un seul voyant reste rouge, rien n'entre.

La première demande de fusion du projet n'a donc pas contenu une ligne de code. Elle contenait le CLAUDE.md.

— Pourquoi le faire relire ? a demandé Sofiane. Ce n'est pas du code.

— Ce fichier change le comportement de l'agent autant que du code, a répondu Julien. Il passe par la même porte.

Nadia n'avait jamais ouvert GitHub de sa vie. Sofiane lui a montré où cliquer. Vingt minutes plus tard, elle avait laissé sept commentaires, dont un qui disait simplement : « Un sinistre peut exister sans déclaration recevable. Ne les confondez pas non plus. »

Julien a corrigé, puis approuvé. Le voyant de l'intégration continue est passé au vert. La première ligne du projet était écrite par le métier.

## Mercredi, 15 heures

Le mail de Mathilde est arrivé à 11 heures. Deux lignes : elle avait rejoué son scénario de lundi, l'agent n'avait plus pu ouvrir les dossiers de configuration, et le fichier ne contenait de toute façon plus aucun secret. *Constat levé.* Elle avait mis Bertrand en copie. Il n'avait pas répondu, ce qui, chez lui, valait félicitations.

Restait à savoir si notre page servait à quelque chose. Un document qui n'a jamais été testé n'est qu'une intention.

J'ai ouvert une session neuve, sans rien expliquer à l'agent, et je lui ai demandé une petite chose : ajouter au formulaire de déclaration le champ « date du sinistre », avec sa validation.

Il a lu le CLAUDE.md, comme à chaque démarrage. Il a proposé un plan en quatre étapes, en commençant par les tests. Il a utilisé le mot « déclarant » au bon endroit. Puis, avant d'écrire la moindre ligne, il s'est arrêté.

```text
Avant d'écrire la validation, j'ai besoin de trois règles métier
que je ne trouve ni dans le code ni dans la documentation :
1. La date du sinistre peut-elle précéder le début du contrat ?
2. Peut-elle être dans le futur ?
3. Existe-t-il un délai maximal pour déclarer ?
Les consignes du projet m'interdisent de les inventer.
```

J'ai fait signe à Nadia de venir lire. Elle a répondu à voix haute, et j'ai tapé ses réponses.

— Dans le futur, non, évidemment. Avant le début du contrat, il n'y a pas de garantie. Mais attention : on enregistre quand même la déclaration. C'est le gestionnaire qui refuse, avec un courrier motivé. Une machine ne refuse pas un assuré.

— Et le délai ?

— Cinq jours ouvrés dans le cas général, deux pour un vol. Mais une déclaration tardive n'est jamais rejetée d'office. On ne peut opposer le retard que s'il nous a causé un préjudice. Si votre écran affiche « délai dépassé, déclaration impossible », on aura un procès et on le perdra.

L'agent a repris son plan avec les réponses. Les dates futures étaient bloquées. Les dates antérieures au contrat et les déclarations tardives étaient acceptées, mais signalées au gestionnaire. Les tests décrivaient chaque cas, avec les mots de Nadia.

Julien a ajouté une seule ligne au CLAUDE.md, par une nouvelle demande de fusion : *Une déclaration n'est jamais rejetée automatiquement : le gestionnaire décide.* Le reste, les délais, les cas du vol, n'avait rien à faire dans un fichier lu à chaque session. Ça relevait de la spécification de la fonctionnalité.

Nadia, elle, fixait toujours l'écran.

— Il m'a posé trois questions pour un seul champ, a-t-elle dit. Pour un portail entier, il va m'en poser combien ?

— Des centaines.

Elle a pâli légèrement.

— C'est pour ça que vous allez les écrire avant qu'il les pose, ai-je ajouté. À partir de demain.

## Le carnet de Thomas

**Ce qui s'est passé.** L'audit a montré qu'une consigne ne protège rien : seul un paramètre imposé bloque l'agent. L'équipe a ensuite réduit à une page un CLAUDE.md généré de trois cents lignes, en n'y gardant que ce que l'agent ne peut pas deviner, puis l'a fait relire par le métier et publié par une demande de fusion. Testé sur un champ, il a poussé l'agent à poser trois questions au lieu d'inventer trois réponses.

**La leçon.** Le CLAUDE.md dit à l'agent ce qu'on attend ; les paramètres l'empêchent de faire ce qu'on interdit. Ne confondez jamais une consigne et un verrou. Et gardez le fichier court : chaque ligne doit éviter une erreur.

**Trois questions à poser à votre équipe**

1. Notre fichier contient-il ce que l'agent ne peut pas deviner, ou ce qu'il lit déjà dans le code ?
2. Qui, côté métier, a validé notre vocabulaire ?
3. Quand l'agent répète une erreur, qui met le fichier à jour, et par quelle porte ?

**Pour aller plus loin.** Manuel, chapitre M3 (CLAUDE.md et la mémoire), chapitre M4 (paramètres et permissions) et chapitre M10 (GitHub au quotidien).
