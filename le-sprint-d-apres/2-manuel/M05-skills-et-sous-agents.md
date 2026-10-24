# M5 — Skills et sous-agents

*Partie II — Le manuel de référence*

## Ce que couvre ce chapitre

Les chapitres M2 à M4 ont installé une session, ses consignes et ses verrous. Celui-ci montre comment sortir du tête-à-tête avec un seul agent. Trois mécanismes y suffisent : la skill, qui range une méthode qu'on répète ; le sous-agent, qui confie une tâche à un agent au contexte séparé ; la copie isolée du dépôt, qui permet à plusieurs agents de travailler en même temps sans se marcher dessus.

Le roman en montre les deux faces. Au chapitre 8, quatre agents codent quatre stories en parallèle, et l'équipe découvre que l'isolement des copies ne protège pas le produit. Au chapitre 9, le goulot n'est plus la production du code mais sa relecture, et c'est une skill de préparation des relectures qui commence à le desserrer. Au chapitre 18, les savoir-faire de l'équipe deviennent des skills qui ont chacune une propriétaire, et les rôles bougent autour de ces outils.

> **Version de référence.** Claude Code 2.1.301, publiée le 15 octobre 2026, avec la configuration Bedrock du chapitre M1. Les skills suivent le standard ouvert Agent Skills ; les champs propres à Claude Code sont signalés.

Un avertissement d'emblée : multiplier les agents multiplie aussi la consommation de jetons et le travail à relire. Le parallélisme n'est un gain que si l'équipe sait absorber ce qu'il produit.

## Trois outils, trois problèmes

On confond facilement les trois. Ils répondent pourtant à des besoins différents, et la bonne question n'est pas « lequel est le plus puissant », mais « quel est mon problème ».

|  | Skill | Sous-agent | Copie isolée |
| --- | --- | --- | --- |
| Le problème | Une méthode qu'on réexplique sans cesse | Une tâche qui encombrerait la conversation, ou qui demande un regard neuf | Plusieurs tâches en même temps sur le même dépôt |
| Ce que c'est | Un dossier avec un fichier `SKILL.md` : des instructions, et parfois des fichiers d'appui | Un agent avec son propre contexte, ses propres outils, éventuellement son propre modèle | Une copie Git du dépôt, sur sa propre branche, dans un dossier séparé |
| Comment il se déclenche | Par `/nom-de-la-skill`, ou par l'agent quand la description correspond à la demande | Par l'agent quand la description correspond, ou à votre demande | Au lancement de la session, ou à la création d'un sous-agent |
| Ce qui revient dans la conversation | Les instructions, qui y restent | Le résumé final seulement | Rien : c'est un autre espace de travail |
| Dans le roman | La préparation des relectures (chapitre 9) | La relecture par un agent qui n'a pas écrit le code (chapitre 9) | Quatre agents sur quatre stories (chapitre 8) |

Les trois se combinent. Une skill peut s'exécuter dans un sous-agent pour ne pas encombrer la conversation ; un sous-agent peut charger des skills dès son démarrage ; un sous-agent peut travailler dans sa propre copie isolée. Les sections suivantes les prennent un par un.

### Skill ou CLAUDE.md ?

Le chapitre M3 posait la règle, qu'on retrouve ici sous un autre angle. Le CLAUDE.md est lu à chaque session, en entier ; une skill n'apporte que sa description, en une ligne, jusqu'au moment où elle sert. Ce qui doit être su en permanence va dans le CLAUDE.md. Ce qui sert une fois par jour ou par semaine, une procédure, une liste de contrôle, un guide de référence, va dans une skill.

Le signe qui ne trompe pas : la troisième fois que vous collez la même consigne dans une conversation, c'est une skill qui manque.

## Écrire une skill

Une skill est un dossier qui porte son nom et contient un fichier `SKILL.md`. Ce fichier a deux parties : un en-tête YAML entre deux lignes `---`, qui dit quand s'en servir, puis des instructions en Markdown, que l'agent suit quand la skill est déclenchée.

```markdown
---
name: resume-modifs
description: Résume les modifications non commitées et signale ce qui est risqué. À utiliser quand on demande ce qui a changé ou un message de commit.
---

## Modifications en cours

!`git diff HEAD`

## Consignes

Résume les modifications en trois points au plus, puis liste les risques :
gestion d'erreur absente, valeur codée en dur, test à mettre à jour.
```

La ligne `` !`git diff HEAD` `` est exécutée avant que l'agent lise la skill, et remplacée par son résultat : l'agent reçoit le vrai diff, pas une consigne pour aller le chercher.

### Où la ranger

| Emplacement | Chemin | Pour qui |
| --- | --- | --- |
| Projet | `.claude/skills/<nom>/SKILL.md` | Toute l'équipe, une fois versionnée avec le code |
| Personnel | `~/.claude/skills/<nom>/SKILL.md` | Vous, dans tous vos projets |
| Entreprise | Le dossier `.claude/skills/` du répertoire des paramètres gérés (chapitre M1) | Tous les postes, sans possibilité de la retirer |
| Plugin | `<plugin>/skills/<nom>/SKILL.md` | Ceux qui installent le plugin (chapitre M8) |

Une skill ajoutée ou modifiée est prise en compte sans redémarrer la session ; `/skills` liste celles qui sont disponibles. Avec Bedrock, les skills synchronisées depuis un compte claude.ai ne s'appliquent pas : tout passe par les fichiers.

### Qui la déclenche

Par défaut, vous la déclenchez en tapant `/resume-modifs`, et l'agent peut aussi la charger seul quand sa description correspond à la demande. Deux réglages changent cela :

- `disable-model-invocation: true` réserve la skill à vos mains. C'est le bon choix pour tout ce qui a un effet : commiter, déployer, ouvrir une demande de fusion. On ne veut pas que l'agent décide seul que le moment est venu.
- `user-invocable: false` la réserve à l'agent. C'est le bon choix pour un savoir de fond, comme le fonctionnement du système des contrats, qui n'a pas de sens comme commande.

La description fait tout le travail de sélection. Mettez le cas d'usage principal en premier et employez les mots que l'équipe emploie vraiment : l'outil tronque l'ensemble au-delà de 1 536 caractères.

### Les champs utiles

| Champ | Effet |
| --- | --- |
| `name`, `description` | Le nom de la commande, et quand s'en servir. Seule la description est vraiment nécessaire. |
| `argument-hint`, `arguments` | L'aide affichée à la saisie, et des noms pour les arguments. |
| `allowed-tools` | Des outils que l'agent peut utiliser sans demander, pendant le tour qui déclenche la skill. |
| `model`, `effort` | Le modèle et le niveau d'effort pendant que la skill est active. |
| `context: fork`, `agent` | Exécuter la skill dans un sous-agent, au contexte séparé. |
| `paths` | Ne proposer la skill que pour certains fichiers. |

Les arguments tapés après la commande remplacent `$ARGUMENTS` dans le texte, ou `$0`, `$1` pour les prendre un à un : `/prepare-relecture 482` place `482` là où la skill attend le numéro de la demande de fusion.

### Rester court

Une fois déclenchée, une skill reste dans la conversation jusqu'à la fin de la session : chaque ligne se paie à chaque message. Gardez `SKILL.md` sous cinq cents lignes, écrivez ce qu'il faut faire plutôt que pourquoi, et déplacez les références longues dans des fichiers à côté, que l'agent ouvrira quand il en aura besoin. Après une compaction, seuls les premiers milliers de jetons de chaque skill sont repris : l'essentiel va en tête.

### Une précaution de sécurité

Le champ `allowed-tools` d'une skill de projet s'applique même dans un dépôt dont vous n'avez pas encore accepté le contenu. Relisez ce champ dans toute skill que vous recevez d'un dépôt tiers. Une organisation qui impose `allowManagedPermissionRulesOnly` (chapitre M4) neutralise ces autorisations ; elle peut aussi interdire l'exécution des lignes `` !`commande` `` avec le paramètre `disableSkillShellExecution`.

## Un exemple complet : préparer une relecture

Au chapitre 9, l'équipe croule sous quarante demandes de fusion et un seul relecteur. Sofiane propose qu'avant chaque relecture, un agent qui n'a pas écrit le code la prépare : il vérifie le vocabulaire, les tests et le périmètre, puis rédige une fiche d'une page en français. L'agent prépare, il ne signe pas. Voici cette skill, telle qu'elle pourrait être rangée dans `.claude/skills/prepare-relecture/SKILL.md`.

```markdown
---
name: prepare-relecture
description: Prépare la relecture humaine d'une demande de fusion du portail sinistres. Vérifie glossaire, tests et périmètre, puis rédige une fiche d'une page.
argument-hint: [numéro de la demande de fusion]
disable-model-invocation: true
context: fork
agent: relecteur
allowed-tools: Bash(gh pr view *) Bash(gh pr diff *)
metadata:
  proprietaires: Julien, Mathilde
  version: "1.3"
---

# Préparer la relecture de la demande $ARGUMENTS

1. Lis la demande avec `gh pr view $ARGUMENTS` et `gh pr diff $ARGUMENTS`,
   puis la story Jira dont la clé figure dans le titre.
2. Vérifie :
   - les termes du métier, contre le glossaire du CLAUDE.md ;
   - que chaque exemple de la story a un test ;
   - les fichiers modifiés hors de la zone prévue par le plan ;
   - pour une demande étiquetée rouge, les trois questions de sécurité :
     quelles données, qui les voit et combien de temps, que se passe-t-il si quelqu'un ment.
3. Rédige une fiche d'une page, en français, avec quatre rubriques :
   Ce que la demande change ; La règle appliquée ; À regarder en premier ;
   Écarts constatés.
4. Ne donne aucun avis d'approbation. Tu prépares ; un humain signe.
```

On la lance avec `/prepare-relecture 482`. Chaque choix de l'en-tête répond à une leçon du roman.

| Choix | Pourquoi |
| --- | --- |
| `disable-model-invocation: true` | Une relecture se prépare quand quelqu'un s'apprête à relire, pas quand l'agent le décide. |
| `context: fork` et `agent: relecteur` | La préparation se fait dans un sous-agent qui n'a pas écrit le code et ne voit pas la conversation qui l'a produit : c'est le regard neuf du chapitre 9. Le sous-agent `relecteur` est défini plus bas, en lecture seule. |
| `allowed-tools` | Seules les commandes de lecture de GitHub passent sans demander. |
| La dernière consigne | La signature reste humaine. La skill ne doit jamais devenir un tampon automatique. |
| `metadata` | Le champ est libre ; l'équipe y note les propriétaires et la version, que l'outil ignore mais que les humains lisent. |

La lecture de la story suppose que l'agent accède à Jira, par un connecteur MCP (chapitre M7).

### Faire vivre une skill d'équipe

Au chapitre 18, Sofiane empaquette quatre savoir-faire de l'équipe en skills : préparer une story, écrire les scénarios d'acceptation, préparer les relectures, tenir le wiki. Nadia lit la première et y reconnaît sa façon de travailler, avec une erreur : elle ne parle jamais des pièces justificatives en premier. Julien empêche Sofiane de corriger lui-même : « Si tu le corriges, c'est encore ta version de sa façon de faire. »

De là, trois règles qui valent pour toute skill partagée :

1. **Une propriétaire** : la personne dont la skill décrit le métier. C'est elle qui accepte ou refuse les modifications.
2. **Une porte** : toute modification passe par une demande de fusion, approuvée par la propriétaire. Un fichier `CODEOWNERS` sur `.claude/skills/<nom>/` rend cette approbation obligatoire dans GitHub (chapitre M10).
3. **Une version** : chaque modification l'incrémente, pour que les équipes qui l'utilisent sachent quand elle a changé, et pourquoi.

Une skill bien écrite finit par circuler au-delà de l'équipe : le chapitre M8 montre comment la distribuer dans un plugin, et le chapitre M12 comment la partager.

## Les skills fournies avec l'outil

L'outil arrive avec une série de skills prêtes à l'emploi. Ce sont des instructions détaillées, comme les vôtres, que l'agent suit avec ses outils habituels. Les plus utiles pour une équipe :

| Skill | Ce qu'elle fait | Bon usage |
| --- | --- | --- |
| `/code-review` | Relit le diff en cours, une branche ou une demande de fusion, à la recherche d'erreurs ; `--fix` applique les corrections, `--comment` les publie sur la demande de fusion. Alias `/review`. | Un premier passage avant la relecture humaine, jamais à sa place. |
| `/simplify` | Fait relire les changements par quatre sous-agents en parallèle : réutilisation de l'existant, simplification, performance, bon niveau d'abstraction. | Après une story livrée par l'agent, pour éviter que le code s'épaississe. |
| `/security-review` | Analyse les changements de la branche à la recherche de failles : injection, authentification, exposition de données. | Toute story étiquetée rouge. |
| `/batch` | Découpe un grand changement en cinq à trente unités indépendantes, puis confie chacune à un sous-agent dans sa propre copie isolée. | Les changements mécaniques et vastes : une migration de bibliothèque, un renommage général. |
| `/verify`, `/run` | Construisent et lancent l'application pour constater qu'un changement fonctionne vraiment, au-delà des tests. | Les écrans et les parcours, où un test vert ne suffit pas. |
| `/debug` | Active le journal de débogage et l'analyse. | Quand l'outil lui-même se comporte mal. |
| `/loop` | Répète une consigne à intervalle régulier tant que la session reste ouverte. | Surveiller une chaîne d'intégration, attendre un déploiement. |
| `/fewer-permission-prompts` | Propose des autorisations pour les commandes de lecture que vous validez sans cesse. | Une fois les premières semaines passées, à relire avant d'accepter. |

Quelques skills fournies ne fonctionnent pas avec Bedrock, parce qu'elles reposent sur des services de l'éditeur : la relecture approfondie dans le cloud (`/code-review ultra`), la recherche sur le web (`/deep-research`), ou les pages publiées comme `/slides` et `/design`.

### Remplacer ou retirer une skill fournie

Une skill de projet qui porte le même nom qu'une skill fournie la remplace. C'est utile pour `/verify` : l'équipe y inscrit comment construire et lancer son application, et l'outil s'en sert. Une skill de projet nommée `verify` ou `simplify` a d'ailleurs un effet de plus : l'agent la lance avant chaque commit qui touche au code.

Pour retirer une skill fournie, le paramètre `skillOverrides` la masque, par exemple `"skillOverrides": { "loop": "off" }` ; le paramètre `disableBundledSkills` les retire toutes.

## Déléguer à un sous-agent

Un sous-agent est un agent que l'agent principal lance pour une tâche précise. Il a son propre contexte, ses propres consignes, ses propres outils, et ne voit pas la conversation en cours : il part de la mission qu'on lui confie. Quand il a fini, seul son résumé revient. Tout ce qu'il a lu pour y arriver reste chez lui.

C'est utile dans deux cas. Le premier : une tâche qui noierait la conversation sous des résultats qu'on ne relira pas, comme parcourir cinquante fichiers ou lancer toute la suite de tests. Le second : une tâche qui demande un regard que la conversation a perdu, comme relire un code sans avoir assisté à son écriture.

### Les sous-agents intégrés

| Sous-agent | Ce qu'il fait | Particularités |
| --- | --- | --- |
| Explore | Cherche et lit dans le code, sans rien modifier | Démarre sans le CLAUDE.md, pour rester rapide. Sur Bedrock, il utilise le modèle de la session. |
| Plan | Rassemble ce qu'il faut savoir pendant le mode plan | En lecture seule, lui aussi sans le CLAUDE.md. |
| general-purpose | Mène une tâche en plusieurs étapes, en lisant et en modifiant | Dispose de tous les outils permis aux sous-agents. |

L'agent principal y recourt de lui-même. Vous pouvez aussi le demander : « confie à un sous-agent l'exécution des tests et ne me rapporte que les échecs ».

### Écrire un sous-agent sur mesure

Un sous-agent sur mesure est un fichier Markdown, rangé dans `.claude/agents/` pour l'équipe ou dans `~/.claude/agents/` pour vous seul. L'en-tête le configure ; le texte qui suit devient ses consignes. Voici le relecteur qu'appelle la skill de la section précédente :

```markdown
---
name: relecteur
description: Relit une demande de fusion qu'il n'a pas écrite. À utiliser pour préparer une relecture humaine.
tools: Read, Grep, Glob, Bash
model: opus
memory: project
---

Tu relis du code du portail sinistres que tu n'as pas écrit. Tu ne
modifies aucun fichier. Tu signales ce que tu constates, avec le fichier
et la ligne, et tu distingues ce qui est certain de ce qui est probable.
Avant de commencer, consulte ta mémoire : les erreurs déjà relevées sur
ce projet. Quand tu as fini, ajoute-y ce que tu as appris.
```

| Champ | Effet |
| --- | --- |
| `name`, `description` | Son nom, et quand l'agent principal doit lui déléguer. |
| `tools`, `disallowedTools` | Les outils permis, ou retirés. Ici, aucun outil d'écriture. Les règles de permission du chapitre M4 continuent de s'appliquer. |
| `model` | `sonnet`, `opus`, `haiku`, `inherit` ou un identifiant complet. Avec la configuration de référence, `opus` désigne le modèle européen figé au chapitre M1. |
| `skills` | Des skills chargées dès son démarrage, en entier. |
| `memory` | Un dossier de mémoire propre au sous-agent. Avec `project`, il est dans `.claude/agent-memory/` et se versionne : le relecteur accumule ce qu'il a appris, pour toute l'équipe. |
| `isolation: worktree` | Le faire travailler dans sa propre copie du dépôt (section suivante). |
| `maxTurns`, `effort` | Borner son travail, régler son niveau d'effort. |

### Le lancer, le suivre, l'arrêter

Trois façons de faire appel à un sous-agent, de la plus souple à la plus ferme :

- le nommer dans la demande : « demande au relecteur d'examiner mes changements » ;
- le citer avec `@`, ce qui garantit que c'est bien lui qui s'exécute ;
- lancer toute la session en son nom, avec `claude --agent relecteur`.

Dans une session interactive, les sous-agents tournent en arrière-plan : vous continuez à travailler, et leur résultat arrive quand ils ont fini. S'ils ont besoin d'une autorisation, la demande apparaît dans votre session et nomme le sous-agent qui la pose. Un panneau sous la zone de saisie les liste ; `/tasks` montre ceux qui tournent, et Ctrl+X Ctrl+K, deux fois, les arrête tous.

Pour une tâche annexe qui a besoin de tout ce qui a été dit, `/subtask` lance une copie de la conversation en sous-agent : elle sait tout ce que vous savez, travaille de son côté, et rapporte son résultat.

### Ce qu'il faut savoir avant d'en abuser

Chaque sous-agent consomme ses propres jetons, et chaque résumé revient dans votre contexte. Dix sous-agents en parallèle, c'est dix fois la facture et dix résumés à lire. L'outil limite d'ailleurs à vingt le nombre de sous-agents qui tournent en même temps, et à trois niveaux la délégation en cascade. Pour un sous-agent qui travaille, la règle reste celle du chapitre M2 : on relit ce qu'il produit.

## Travailler en parallèle sur des copies isolées

Deux sessions ouvertes dans le même dossier se marchent dessus : elles modifient les mêmes fichiers, et le retour arrière de l'une ignore les changements de l'autre (chapitre M2). La réponse est une copie isolée du dépôt, ce que Git appelle un *worktree* : un dossier à part, avec ses propres fichiers et sa propre branche, qui partage l'historique du dépôt principal.

> *Schéma non reproduit dans cette version Markdown : copies isolées · la relecture reste le passage obligé.*

### Lancer une session dans sa copie

```bash
claude --worktree sin-42
```

L'outil crée la copie dans `.claude/worktrees/sin-42/`, sur une nouvelle branche `worktree-sin-42`, et y démarre la session. Une autre story, dans un autre terminal, avec un autre nom : les deux sessions ne se voient pas. Ajoutez `.claude/worktrees/` au `.gitignore` du projet.

Par défaut, la copie part de la branche principale du dépôt distant, à jour. Pour partir de votre travail en cours, réglez `"worktree": { "baseRef": "head" }`. Pour partir d'une demande de fusion existante, donnez son numéro : `claude --worktree "#482"`.

Une copie neuve n'a pas les dépendances installées ni les fichiers exclus de Git. Demandez à l'agent d'installer les dépendances. Un fichier `.worktreeinclude`, écrit comme un `.gitignore`, peut recopier certains fichiers exclus dans chaque nouvelle copie ; avec la configuration de référence, n'y mettez jamais un fichier de secrets, puisque ceux-ci vivent dans le coffre-fort (chapitre M4).

### Ce qui est partagé, ce qui ne l'est pas

| Partagé avec le dépôt principal | Propre à chaque copie |
| --- | --- |
| L'historique Git et les branches | Les fichiers de travail et la branche courante |
| Les plugins installés pour le projet | Les dépendances installées |
| Les autorisations « ne plus demander » | Les fichiers exclus de Git, sauf ceux du `.worktreeinclude` |
| Les skills et sous-agents non versionnés du dépôt principal | Le CLAUDE.md, tel qu'il est sur la branche de la copie |

### Fermer et reprendre

En quittant la session, l'outil vérifie la copie. Si elle ne contient rien de nouveau, il la supprime, après vous l'avoir demandé si la session porte un nom. Si elle contient du travail, il demande s'il faut la garder ; on la reprend ensuite avec `claude --worktree sin-42 --resume`.

Pendant ce temps, l'outil veille à l'isolement : depuis une copie, l'agent ne peut ni modifier un fichier du dépôt principal, ni y lancer une commande, ni y rediriger Git. Une commande qui écrirait là-bas par une simple copie de fichier échappe à ce contrôle ; c'est le rôle du bac à sable.

### Des sous-agents dans leur propre copie

Un sous-agent peut lui aussi travailler dans une copie à lui. Il suffit d'ajouter `isolation: worktree` à son en-tête, ou de demander à l'agent « utilise des copies isolées pour tes sous-agents ». La copie est supprimée d'office si le sous-agent n'a rien modifié. C'est ainsi que fonctionne `/batch` : une copie et un sous-agent par unité de travail.

### L'isolement ne protège pas le produit

Au chapitre 8, Sofiane lance quatre agents sur quatre stories, chacun dans sa copie. Aucun ne casse le travail d'un autre. Mais deux d'entre eux ajoutent chacun un champ pour la même notion, et au moment de réunir les branches, l'agent chargé du conflit garde les deux : tout compile, et le code garde deux champs pour une seule notion.

Les copies isolent les fichiers, pas les décisions. Trois pratiques comblent l'écart :

1. **Dresser la carte avant de lancer.** En mode plan, demander à l'agent quels fichiers chaque story toucherait ; au chapitre 8, onze stories sur dix-huit touchent la même zone.
2. **Découper par zones, pas par stories.** Deux agents ne travaillent jamais en même temps dans la même zone du code.
3. **Réunir souvent.** Plus une branche vit longtemps, plus son retour coûte cher, en conflits et en relecture.

## Les limites du parallélisme

Tout ce chapitre permet de produire plus, plus vite. Le roman passe ses chapitres 9 et 18 à montrer pourquoi ce n'est pas forcément une bonne nouvelle.

### La contrainte s'est déplacée

Avec des agents, écrire le code n'est plus ce qui limite l'équipe. Au chapitre 18, Thomas mesure une story de bout en bout : une heure et demie de préparation, trente-cinq minutes de développement par l'agent, une heure de relecture, deux pour une story rouge, une heure de tests exploratoires. Le code pèse trente-cinq minutes sur cinq heures. Doubler le nombre d'agents en ferait gagner peut-être quinze, et doublerait la file devant les relecteurs.

Tant que la relecture ne suit pas, chaque minute gagnée en amont grossit le stock devant elle. Au chapitre 9, la file passe de dix-neuf à quarante demandes en quatre jours, et le seul relecteur finit par approuver sans lire. La parade tient en une ligne au tableau : six demandes en revue au maximum ; quand la colonne est pleine, personne ne commence rien, on relit.

### Les pièges courants

| Piège | Le signe | La parade |
| --- | --- | --- |
| Découper plus fin pour relire plus vite | Les demandes rétrécissent, mais leur nombre explose | Chaque relecture a un coût fixe, environ vingt minutes au chapitre 9 : garder des demandes de la taille d'une story. |
| Approuver par lassitude | Plusieurs sessions attendent une autorisation, on dit oui sans lire | Moins de sessions à la fois ; le mode plan pour discuter avant d'agir. |
| Noyer la conversation | Les résumés de dix sous-agents remplissent le contexte | Demander des résumés courts ; regrouper les recherches. |
| Oublier la facture | Chaque sous-agent et chaque session consomment leurs propres jetons | Suivre `/usage` session par session, et le coût par story (chapitre M14). |
| Paralléliser ce qui dépend | Deux agents dans la même zone du code | Dresser la carte des dépendances avant de lancer (section précédente). |

### Trois questions avant de lancer un agent de plus

1. **Qui relira ce qu'il produit, et quand ?** Si la réponse est « on verra », ne le lancez pas.
2. **Sa zone du code est-elle libre ?** Si un autre agent y travaille, attendez qu'il ait fini.
3. **Le résultat sert-il avant la fin du sprint ?** Un travail terminé qui attend une semaine n'est qu'un stock de plus.

Le chapitre M13 revient sur la limite du travail en cours, et le chapitre M14 sur la mesure des coûts.

## Dans le roman

| Chapitre | Scène | Ce qu'elle illustre ici |
| --- | --- | --- |
| 8 — Quatre agents à la fois | Quatre agents codent quatre stories dans des copies isolées ; deux ajoutent un champ pour la même notion, et le conflit est résolu en gardant les deux. | Les copies isolent les fichiers, pas les décisions. |
| 8 — Quatre agents à la fois | En mode plan, l'agent dit pour chaque story quels fichiers il toucherait : onze stories sur dix-huit visent la même zone. | Dresser la carte avant de paralléliser. |
| 9 — Le goulot s'appelle Julien | Jeudi, 9 h 30 : quarante demandes en revue, un relecteur qui « tamponne ». | La contrainte n'est plus le code, mais la relecture. |
| 9 — Le goulot s'appelle Julien | Jeudi, 14 heures : une session neuve prépare chaque relecture avec une consigne enregistrée comme une skill ; l'agent prépare, il ne signe pas. | La skill de préparation des relectures, et le regard neuf d'un sous-agent. |
| 18 — Les rôles bougent | Mercredi, 11 heures : quatre savoir-faire empaquetés en skills ; Nadia corrige la sienne et en devient propriétaire. | Propriétaire, demande de fusion et version pour chaque skill partagée. |
| 18 — Les rôles bougent | Mardi, 14 heures : l'équipe refuse cinq développeurs de plus et demande un métier, une testeuse et un relecteur. | Dimensionner l'équipe sur sa contrainte. |

Pour aller plus loin : M6 (hooks), M7 (MCP, pour que l'agent lise Jira), M8 (plugins : distribuer une boîte à outils de skills), M12 (partager en équipe), M13 (limiter le travail en cours).

## Sources

Consultées le 19 octobre 2026.

- [Étendre Claude avec des skills](https://code.claude.com/docs/en/skills)
- [Créer des sous-agents](https://code.claude.com/docs/en/sub-agents)
- [Sessions parallèles et copies isolées](https://code.claude.com/docs/en/worktrees)
- [Quand utiliser CLAUDE.md, skills, sous-agents ou hooks](https://code.claude.com/docs/en/features-overview)
- [Référence des commandes et skills fournies](https://code.claude.com/docs/en/commands)
- [Le standard Agent Skills](https://agentskills.io)
