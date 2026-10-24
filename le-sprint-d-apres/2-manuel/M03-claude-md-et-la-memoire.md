# M3 — CLAUDE.md et la mémoire

*Partie II — Le manuel de référence*

## Ce que couvre ce chapitre

Chaque session commence la tête vide. Deux mécanismes transportent le savoir d'une session à l'autre : les fichiers CLAUDE.md, que vous écrivez, et la mémoire automatique, que l'agent tient lui-même. Ce chapitre explique où ils vivent, ce qu'on y écrit, ce qu'on n'y écrit surtout pas, et comment les garder justes dans la durée.

C'est le chapitre le plus important de la partie II pour une Product Owner ou un tech lead. Au chapitre 3 du roman, la première demande de fusion du projet ne contient pas une ligne de code : elle contient le CLAUDE.md, écrit avec le métier et relu par lui. Tout ce que l'agent fera ensuite en dépend.

> **Version de référence.** Claude Code 2.1.301, publiée le 15 octobre 2026, avec la configuration Bedrock du chapitre M1. La lecture directe des fichiers AGENTS.md demande la version 2.1.281 ou plus récente sur Bedrock.

Un principe traverse tout le chapitre, et Julien le formule au chapitre 3 : un CLAUDE.md est une consigne, pas un verrou. L'agent le lit et s'efforce de le suivre ; il peut l'interpréter. Ce qui doit être impossible relève des paramètres, au chapitre M4.

## Le livret d'accueil de l'agent

Un CLAUDE.md est un simple fichier Markdown. L'outil le lit au démarrage de chaque session et le transmet au modèle comme un premier message, juste après ses instructions internes. L'agent commence donc chaque conversation en sachant ce que vous y avez écrit : le vocabulaire du métier, les frontières du code, la façon de travailler de l'équipe.

Thomas en donne la meilleure image au chapitre 3 : le CLAUDE.md, c'est le livret d'accueil qu'on remet à un nouvel arrivant ; les paramètres, c'est son badge. Le livret explique ce qu'on attend de lui. Le badge ouvre certaines portes et pas d'autres. On ne protège pas une salle des coffres avec un livret d'accueil.

La conséquence est pratique : l'agent suit le CLAUDE.md la plupart du temps, pas toujours. Il l'interprète, surtout quand une consigne est vague ou en contredit une autre. Au chapitre 10, l'agent bloqué sur un scénario propose de modifier le scénario, alors qu'aucune consigne ne l'y autorise ; seule une règle dans les paramètres l'en empêche vraiment.

### Où ranger quoi

Avant d'écrire une ligne dans un CLAUDE.md, demandez-vous si elle n'a pas sa place ailleurs.

| Ce que vous voulez | Le bon outil | Chapitre |
| --- | --- | --- |
| Que l'agent sache quelque chose à chaque session | CLAUDE.md | M3 |
| Que l'agent retienne vos corrections sans que vous l'écriviez | Mémoire automatique | M3 |
| Qu'une consigne ne s'applique qu'à une partie du code | Règle liée à un dossier | M3 |
| Qu'une action soit impossible | Paramètres : interdictions | M4 |
| Qu'une procédure en plusieurs étapes soit disponible à la demande | Skill | M5 |
| Qu'une vérification ait lieu à coup sûr, à un moment précis | Hook | M6 |

Deux erreurs reviennent sans cesse. La première consiste à confier à un CLAUDE.md ce qui relève d'un verrou : « ne jamais lire un fichier qui contient un mot de passe », la solution que propose Sofiane au chapitre 3. La seconde consiste à y déverser une procédure entière, qui encombre chaque session alors qu'elle ne sert qu'une fois par semaine : sa place est dans un skill.

## Les niveaux

Les CLAUDE.md s'empilent. L'outil lit tous ceux qui s'appliquent, du plus général au plus proche du dossier de travail, et les additionne : aucun ne remplace l'autre. S'ils se contredisent, l'agent peut suivre l'un ou l'autre ; c'est pourquoi on évite de dire deux fois la même chose à deux niveaux.

> *Schéma non reproduit dans cette version Markdown : ordre de lecture · le CLAUDE.md du projet est celui de l'équipe.*

**Entreprise.** Le fichier géré par la DSI s'applique à toutes les sessions du poste, dans tous les dépôts, et aucun réglage individuel ne peut l'exclure. On le déploie comme les paramètres gérés du chapitre M1, au même endroit :

| Système | Emplacement |
| --- | --- |
| macOS | `/Library/Application Support/ClaudeCode/CLAUDE.md` |
| Linux et WSL | `/etc/claude-code/CLAUDE.md` |
| Windows | `C:\Program Files\ClaudeCode\CLAUDE.md` |

Le même texte peut aussi vivre dans la clé `claudeMd` du fichier `managed-settings.json`, ce qui évite de déployer deux fichiers. Dans le roman, c'est là que vivent les règles de Bertrand : par exemple, des rappels sur les données personnelles ou la conduite à tenir face à un secret. Les interdictions proprement dites, elles, vont dans les paramètres.

**Utilisateur.** `~/.claude/CLAUDE.md` porte vos préférences pour tous vos projets ; personne d'autre ne le lit. Julien y demande des explications détaillées, Sofiane y range ses raccourcis.

**Projet.** `./CLAUDE.md`, ou `./.claude/CLAUDE.md` si vous préférez garder la racine propre, est le fichier de l'équipe. Il est versionné avec le code et change par demande de fusion, comme le code : il modifie le comportement de l'agent autant qu'une ligne de Java.

**Local.** `./CLAUDE.local.md` porte vos notes pour ce projet seulement : l'adresse de votre environnement de test, vos jeux de données. Déclarez-le dans `.gitignore`. Il est lu juste après le CLAUDE.md du même dossier.

**Dossiers parents et sous-dossiers.** Lancé dans `portail/back`, l'outil lit aussi `portail/CLAUDE.md` s'il existe. Les CLAUDE.md des sous-dossiers, eux, ne se chargent qu'au moment où l'agent lit ou modifie un fichier de ce sous-dossier. Dans un grand dépôt partagé entre plusieurs équipes, le paramètre `claudeMdExcludes` permet d'ignorer les fichiers des autres.

**Vérifier ce qui est chargé.** `/context` liste les fichiers lus au démarrage sous *Memory files* ; `/memory` les affiche tous et ouvre celui que vous choisissez dans votre éditeur, en le créant s'il n'existe pas encore.

## Écrire le premier CLAUDE.md

La commande `/init` produit un premier jet en quelques minutes : l'agent parcourt le dépôt et rédige un CLAUDE.md avec les commandes de compilation, de test et les conventions qu'il découvre. Si un fichier existe déjà, elle propose des améliorations au lieu de l'écraser. Elle reprend aussi les consignes laissées pour d'autres outils, comme `.cursorrules` ou `.github/copilot-instructions.md`.

Pour une version guidée, définissez la variable `CLAUDE_CODE_NEW_INIT` à `1` avant de lancer `/init` : l'agent vous demande quoi mettre en place, explore le code, vous pose des questions sur ce qu'il n'a pas trouvé, puis soumet une proposition avant d'écrire quoi que ce soit.

**Un premier jet n'est qu'un point de départ.** Au chapitre 3, `/init` livre trois cents lignes. Julien les lit à voix haute : « Le projet est écrit en Java. » « Les tests se trouvent dans le dossier des tests. » Tout ce que l'agent a écrit, il le savait déjà en lisant le code ; ce qu'il ne sait pas, il ne l'a pas écrit, puisque ce n'est écrit nulle part.

### La méthode en cinq temps

1. **Générer, puis élaguer.** Passez chaque ligne du premier jet au test de Thomas : *si on retire cette ligne, l'agent fera-t-il une erreur ?* Si la réponse est non, la ligne part. Dans le roman, il en reste trente-cinq sur trois cents.
2. **Écrire l'essentiel avec le métier.** Une heure d'atelier, autour de la question que Julien écrit au tableau : *qu'est-ce qu'un développeur brillant, arrivé ce matin, ne peut pas deviner ?* La réponse tient presque toujours en cinq rubriques : pourquoi le projet existe, les mots du métier, les frontières qu'on ne franchit pas, la façon de travailler, ce qu'on ne fait jamais.
3. **Renvoyer plutôt que recopier.** Si une information existe déjà, dans la documentation d'architecture ou la liste des commandes, le CLAUDE.md indique où la trouver, et l'agent l'ouvrira quand il en aura besoin. Un document recopié vieillit deux fois.
4. **Publier par demande de fusion.** Le fichier change le comportement de l'agent autant que du code ; il passe par la même porte et se fait relire par le métier. Au chapitre 3, Nadia y laisse sept commentaires.
5. **Tester avec une session neuve.** Ouvrez une session sans rien expliquer et confiez-lui une petite tâche réelle. Écoutez ses questions : chacune révèle soit une lacune du fichier, soit une règle métier qui relève de la spécification.

### Écrire des consignes vérifiables

Une consigne précise est mieux suivie qu'une consigne vague. Écrivez-en que l'on pourrait vérifier.

| Plutôt que | Écrire |
| --- | --- |
| Respecter les bonnes pratiques. | Tests d'abord : écrire le test, le voir échouer, puis le code. |
| Faire attention au système des contrats. | Tout appel au système des contrats passe par `adaptateur-contrats`. |
| Utiliser le bon vocabulaire. | Déclarant : remplit la déclaration ; pas forcément l'assuré. |
| Bien tester avant de livrer. | Lancer `mvn verify` avant chaque commit. |

Groupez les consignes sous des titres Markdown et en listes courtes : l'agent les suit mieux qu'un texte dense, et un relecteur repère plus vite une contradiction.

## Ce qu'on y met, ce qu'on n'y met pas

| On y met | On n'y met pas |
| --- | --- |
| La raison d'être du projet, en une phrase, avec un renvoi vers la vision | Ce que le code dit déjà : le langage, l'arborescence, les dépendances |
| Le vocabulaire du métier, validé par le métier | Un secret, quel qu'il soit : le fichier part au modèle à chaque session |
| Les frontières de l'architecture | Une interdiction qui doit tenir à coup sûr : sa place est dans les paramètres |
| La façon de travailler : tests d'abord, une story par branche, la forme des commits | Les règles détaillées d'une fonctionnalité : elles relèvent de sa spécification |
| Les « ne jamais » de comportement, comme inventer une règle de gestion | Une procédure en dix étapes : elle fera un skill |
| L'erreur que l'agent a déjà commise deux fois | Vos préférences personnelles : elles vont au niveau utilisateur ou local |
| Les commandes qui ne se devinent pas, ou un renvoi vers leur liste | L'état du sprint en cours : il sera faux la semaine prochaine |

La quatrième ligne de droite demande du discernement. Au chapitre 3, l'agent apprend de Nadia trois règles sur la date du sinistre. Julien n'en garde qu'une dans le CLAUDE.md, la plus générale : *une déclaration n'est jamais rejetée automatiquement ; le gestionnaire décide.* Les délais et les cas du vol vont dans la spécification de la fonctionnalité. Un principe qui vaut pour tout le portail a sa place dans le fichier lu à chaque session ; un détail qui ne vaut que pour un écran n'y a pas la sienne.

### Un exemple commenté

Voici le CLAUDE.md du portail sinistres, tel qu'il est au chapitre 10, après deux ajouts du métier.

```markdown
# Portail sinistres — consignes pour l'agent

Portail de déclaration de sinistre habitation. Vision : docs/vision.md

## Vocabulaire métier (validé par Nadia Benali)
- Déclarant : remplit la déclaration ; pas forcément l'assuré.
- Assuré : personne couverte ; pas forcément le souscripteur.
- Franchise, plafond : jamais codés en dur, toujours lus dans le contrat.

## Principes métier
- Une déclaration n'est jamais rejetée automatiquement : le gestionnaire décide.
- On ne bloque jamais une déclaration ; on la complète.

## Règles techniques
- Tout appel au système des contrats passe par adaptateur-contrats.
- Tests d'abord. Une story = une branche = une demande de fusion.
- Commandes du projet : docs/commandes.md

## Ne jamais
- Inventer une règle de gestion. Poser la question.
```

| Rubrique | Pourquoi elle est là |
| --- | --- |
| Titre et vision | Une phrase suffit à orienter chaque décision ; le détail est un clic plus loin. |
| Vocabulaire métier | Confondre assuré et déclarant, c'est verser l'indemnité au mauvais tiers. Le code ne peut pas l'apprendre à l'agent. |
| Principes métier | Deux phrases que Nadia appliquait depuis douze ans sans les avoir jamais écrites. Elles valent pour tout le portail. |
| Règles techniques | La frontière de l'adaptateur n'est visible nulle part dans le code ; la méthode de travail non plus. |
| Ne jamais | Une seule ligne, mais la plus rentable : elle transforme une invention en question. |

Trois remarques de forme. Le fichier tient sur une page, loin de la limite de deux cents lignes au-delà de laquelle l'agent suit moins bien ses consignes. Les chemins comme `docs/vision.md` sont de simples renvois : l'agent ouvre le fichier quand il en a besoin. Et les commentaires HTML, `<!-- comme celui-ci -->`, sont retirés avant l'envoi au modèle : c'est l'endroit pour noter, à l'usage des humains, qui a validé quoi et quand.

## Organiser au-delà d'un fichier

Un CLAUDE.md d'une page suffit longtemps. Trois mécanismes prennent le relais quand le projet grandit.

### Les imports

Une ligne `@chemin/vers/fichier.md` dans un CLAUDE.md insère le fichier désigné au démarrage, comme s'il y était écrit. Le chemin est relatif au fichier qui importe ; un fichier importé peut en importer d'autres, sur quatre niveaux au plus.

```markdown
## Façon de travailler
- Conventions Git : @docs/conventions-git.md
```

Un import organise, il n'allège pas : le fichier importé est envoyé au modèle à chaque session, comme le reste. Pour un document long qui ne sert que de temps en temps, écrivez simplement son chemin entre accents graves, `docs/architecture.md` : il n'est pas importé, et l'agent l'ouvrira quand il en aura besoin.

Quand un import vise un fichier hors du dépôt, l'outil demande votre accord la première fois. C'est une protection contre un fichier piégé glissé par un tiers dans un projet partagé. L'usage le plus courant est légitime : un `CLAUDE.local.md` qui importe `@~/.claude/portail-perso.md`, pour retrouver ses notes personnelles dans toutes les copies du dépôt.

### Les règles liées à un dossier

Le dossier `.claude/rules/` accueille des fichiers de consignes thématiques. Sans en-tête, une règle est chargée au démarrage, comme le CLAUDE.md du projet. Avec un en-tête `paths`, elle ne se charge que lorsque l'agent lit ou modifie un fichier correspondant. Au chapitre 10, la règle sur les scénarios d'acceptation pourrait s'écrire ainsi :

```markdown
---
paths:
  - "src/test/resources/scenarios/**/*.feature"
---
# Scénarios d'acceptation
- Écrits et validés par le métier et la recette. Ne jamais les modifier.
- Un scénario qui semble faux : s'arrêter et le signaler.
```

Cette règle ne coûte rien tant que l'agent ne touche pas aux scénarios. Elle reste pourtant une consigne : au chapitre 10, c'est le verrou posé dans les paramètres qui empêche réellement l'agent de réécrire un scénario. Les deux se complètent. La règle explique pourquoi ; le verrou garantit.

Deux précautions. Une règle liée à un dossier disparaît à la compaction et ne revient qu'au prochain fichier concerné ; une consigne vitale va donc dans le CLAUDE.md. Et vos règles personnelles, valables pour tous vos projets, se rangent dans `~/.claude/rules/`.

### AGENTS.md

AGENTS.md est un format partagé par plusieurs outils d'agents de code. Claude Code le lit à la place du CLAUDE.md quand aucun CLAUDE.md ni CLAUDE.local.md n'existe dans le dossier de travail ou au-dessus. Sur Bedrock, cette lecture directe demande la version 2.1.281 ou plus récente.

Le réglage *Project instructions*, dans `/config`, change ce comportement :

| Valeur | Ce que l'agent lit |
| --- | --- |
| `claude-md-or-agents-md` | Le CLAUDE.md, ou l'AGENTS.md s'il n'y a pas de CLAUDE.md. C'est la valeur par défaut. |
| `claude-md-and-agents-md` | Les deux, le CLAUDE.md d'abord. |
| `claude-md` | Le CLAUDE.md seulement. |
| `managed-only` | Seulement le fichier de l'entreprise et la mémoire automatique, au démarrage. |

Dans une équipe où chacun n'utilise pas le même outil, la solution la plus robuste tient en deux fichiers : un AGENTS.md partagé par tous, et un CLAUDE.md qui commence par `@AGENTS.md`, suivi des seules consignes propres à Claude Code. Chaque outil lit ce qui le concerne, et aucune règle n'est écrite deux fois.

## La mémoire automatique

Le CLAUDE.md, c'est vous qui l'écrivez. La mémoire automatique, c'est l'agent qui la tient : au fil du travail, il note pour lui-même ce qui lui servira dans une prochaine session. Elle est active par défaut.

**Ce qu'il retient.** Quatre sortes de notes :

| Sorte | Exemple |
| --- | --- |
| Vous | « Julien préfère des explications détaillées avant chaque modification. » |
| Vos corrections | « Ne pas utiliser le mot sinistre pour une déclaration non recevable. » |
| Le projet | « La reprise des dossiers vol est prévue pour janvier. » |
| Les références | « Les codes retour du mainframe sont décrits dans le wiki de l'équipe contrats. » |

Il ne note pas ce qu'il peut retrouver dans le code ou l'historique Git, ni ce que le CLAUDE.md dit déjà. Et il ne note pas à chaque session : seulement ce qui lui paraît utile plus tard. Quand il le fait, le terminal l'indique par un message comme *Saved 2 memories* ; quand il relit ses notes, par *Recalled 2 memories*.

**Où elle vit.** Dans `~/.claude/projects/<projet>/memory/`, sur votre poste : un index `MEMORY.md`, dont les deux cents premières lignes sont lues à chaque session, et un fichier par sujet, que l'agent ouvre à la demande. Toutes les copies d'un même dépôt partagent la même mémoire. Elle n'est ni versionnée, ni partagée avec l'équipe, ni effacée par le nettoyage des sessions au bout de trente jours.

**Comment la piloter.**

| Pour | Faire |
| --- | --- |
| Lire ou corriger ce qu'il a retenu | `/memory`, puis ouvrir le dossier de la mémoire automatique : ce sont des fichiers Markdown ordinaires. |
| Lui faire retenir quelque chose | Le lui dire : « retiens que les tests d'API demandent un serveur Redis local ». |
| Mettre quelque chose dans le CLAUDE.md plutôt | Le dire aussi : « ajoute cela au CLAUDE.md ». |
| La couper pour vous | Le bouton de `/memory`, qui règle `autoMemoryEnabled` dans vos paramètres. |
| La couper pour un projet | `"autoMemoryEnabled": false` dans les paramètres du projet. |
| La couper pour toute l'entreprise | La variable `CLAUDE_CODE_DISABLE_AUTO_MEMORY` à `1`, dans le bloc `env` des paramètres gérés. |

### La mémoire de l'un n'est pas celle de l'équipe

La mémoire automatique est personnelle. Ce que Sofiane a appris à l'agent un mardi, Émilie ne le retrouve pas dans sa propre session. C'est sa limite pour une équipe : une correction qui compte pour tous doit remonter dans le CLAUDE.md, par une demande de fusion. Une bonne habitude consiste à relire sa mémoire en rétrospective : ce qui revient chez deux personnes a sa place dans le fichier partagé.

C'est aussi un sujet de sécurité. Ces fichiers sont du texte en clair sur le poste, comme l'historique des sessions. Une organisation qui traite des données sensibles doit décider en connaissance de cause : garder la mémoire et la faire relire, ou la couper par les paramètres gérés. Dans les deux cas, la règle du chapitre 3 tient toujours : un secret qui n'est pas dans le code ne se retrouvera dans aucune mémoire.

## Entretenir ses instructions

Un CLAUDE.md n'est jamais fini. Il vieillit comme une documentation, mais ses erreurs coûtent plus cher : l'agent les applique à la lettre, à chaque session.

### Quand y toucher

| Signe | Geste |
| --- | --- |
| L'agent commet la même erreur une deuxième fois | Ajouter la consigne qui l'aurait évitée. |
| Une relecture de demande de fusion relève ce que l'agent aurait dû savoir | Ajouter la consigne, dans la même demande de fusion si possible. |
| Vous retapez la même correction que la semaine dernière | La sortir de la conversation et l'écrire. |
| Une consigne n'a plus d'effet visible depuis des semaines | La retirer : chaque ligne coûte à chaque session. |
| Deux consignes se contredisent | Trancher ; l'agent choisirait au hasard. |
| Le fichier dépasse deux cents lignes | Déplacer ce qui ne vaut que pour un dossier vers une règle, et les procédures vers des skills. |

Au-delà de deux cents lignes, l'outil affiche d'ailleurs un avertissement au démarrage et dans `/status`.

### Par quelle porte

Le CLAUDE.md du projet change par demande de fusion, relue comme du code ; quand une modification touche au vocabulaire ou aux règles du métier, la Product Owner fait partie des relecteurs. C'est la réponse à la troisième question du carnet de Thomas, au chapitre 3 : quand l'agent répète une erreur, qui met le fichier à jour, et par quelle porte ?

Une pratique simple tient l'ensemble à jour : une rubrique de cinq minutes en rétrospective. Quelles lignes ajouter, d'après les erreurs du sprint ? Quelles lignes retirer ? Qu'ont retenu les mémoires automatiques de chacun qui mérite d'être partagé ?

### Les outils de contrôle

- **`/doctor prompt-audit`** fait relire vos fichiers d'instructions par l'agent : consignes périmées, renvois vers des fichiers ou des commandes qui n'existent plus, contradictions entre fichiers. Il produit un rapport avec des corrections proposées, et ne modifie rien sans votre accord.
- **`/doctor`** propose aussi d'élaguer un CLAUDE.md trop long, en retirant ce que l'agent peut déduire du code.
- **`/context`** confirme quels fichiers ont réellement été chargés.
- **Une session neuve** reste le meilleur test, après chaque modification importante : une petite tâche réelle, sans rien expliquer, et l'écoute de ses questions.

### Quand l'agent ne suit pas le fichier

Commencez par vérifier dans `/context` que le fichier est bien chargé. Cherchez ensuite une consigne trop vague, ou une autre qui la contredit, dans un autre niveau ou dans une règle. Si la consigne a été donnée en cours de conversation plutôt qu'écrite, elle a pu disparaître à la compaction. Et si elle doit s'appliquer à coup sûr, à chaque fois, c'est qu'elle n'avait pas sa place dans un CLAUDE.md : elle relève d'un paramètre (chapitre M4) ou d'un hook (chapitre M6).

## Dans le roman

| Chapitre | Scène | Ce qu'elle illustre ici |
| --- | --- | --- |
| 3 — Le fichier qui parle à la machine | Lundi, 14 heures : Sofiane veut interdire la lecture des secrets par une consigne ; Julien et Thomas expliquent la différence entre livret d'accueil et badge. | Un CLAUDE.md est une consigne, pas un verrou. |
| 3 — Le fichier qui parle à la machine | Lundi après-midi : trois cents lignes générées, trente-cinq gardées après le test de la suppression. | Générer, puis élaguer. |
| 3 — Le fichier qui parle à la machine | Mardi : l'atelier avec Nadia sur le vocabulaire, le choix des niveaux, la première demande de fusion du projet. | Écrire l'essentiel avec le métier ; publier par la même porte que le code. |
| 3 — Le fichier qui parle à la machine | Mercredi, 15 heures : dans une session neuve, l'agent pose trois questions au lieu d'inventer trois règles ; une seule entre dans le fichier. | Le test de la session neuve ; ce qui relève du CLAUDE.md et ce qui relève de la spécification. |
| 10 — Émilie ne suit plus | Mercredi, 9 heures : Nadia ajoute « on ne bloque jamais une déclaration ; on la complète » ; l'agent propose de modifier un scénario, et un verrou l'en empêche. | Un principe métier à sa place ; la consigne et le verrou qui se complètent. |

Pour aller plus loin : M4 (paramètres et permissions), M5 (skills et sous-agents), M6 (hooks), M12 (partager en équipe : ce qu'on versionne, ce qui reste local).

## Sources

Consultées le 16 octobre 2026.

- [Comment Claude se souvient de votre projet : CLAUDE.md, AGENTS.md, mémoire automatique](https://code.claude.com/docs/en/memory)
- [Étendre Claude Code : quand utiliser CLAUDE.md, règles, skills, hooks](https://code.claude.com/docs/en/features-overview)
- [Fenêtre de contexte et compaction](https://code.claude.com/docs/en/context-window)
- [Utilisation des données et stockage local](https://code.claude.com/docs/en/data-usage)
- [Déployer des paramètres gérés](https://code.claude.com/docs/en/managed-settings)
- [Notes de version de Claude Code](https://code.claude.com/docs/en/changelog)
