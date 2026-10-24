# M8 — Plugins et marketplaces

*Partie II — Le manuel de référence*

## Ce que couvre ce chapitre

Les chapitres M3 à M7 ont fabriqué des pièces : un CLAUDE.md, des règles, des skills, des sous-agents, des hooks, des connecteurs. Tant qu'elles vivent dans un seul dépôt, elles ne servent qu'à une équipe. Un plugin les réunit en un paquet installable ; une marketplace les publie dans un catalogue où d'autres équipes les trouvent ; les paramètres gérés peuvent en imposer certains à tous les postes.

Le roman en montre les deux usages. Au chapitre 16, les garde-fous de l'équipe vivent en cinq endroits et la directrice générale veut qu'ils deviennent la règle de toute la maison. Sofiane propose de les réunir dans un seul paquet, publié dans un catalogue interne et imposé par les paramètres gérés : une équipe qui démarre reçoit le socle en ouvrant l'outil, « comme on reçoit son badge le premier jour ». Au chapitre 18, il empaquette de la même façon les quatre savoir-faire de l'équipe, chacun avec sa propriétaire.

> **Version de référence.** Claude Code 2.1.301, publiée le 15 octobre 2026, avec la configuration Bedrock du chapitre M1. Le système de plugins évolue vite ; la [documentation officielle](https://code.claude.com/docs/en/plugins/overview) fait foi.

Deux distinctions guident le chapitre : un plugin qu'on propose et un plugin qu'on impose ; un catalogue qu'on ouvre et un catalogue qu'on ferme. La première relève de l'outillage, la seconde de la gouvernance.

## Ce qu'est un plugin

Un plugin est un dossier qui réunit des pièces déjà rencontrées dans ce manuel, accompagné d'un manifeste qui lui donne un nom et une version. L'outil l'installe et le charge d'un bloc.

| Dossier ou fichier | Ce qu'il apporte | Chapitre |
| --- | --- | --- |
| `.claude-plugin/plugin.json` | Le manifeste : nom, description, version, auteur | — |
| `skills/<nom>/SKILL.md` | Des skills | M5 |
| `agents/<nom>.md` | Des sous-agents | M5 |
| `hooks/hooks.json` | Des hooks, au même format que dans un fichier de paramètres | M6 |
| `.mcp.json` | Des serveurs MCP | M7 |

Un plugin peut aussi apporter des serveurs d'analyse de code pour un langage, des styles de réponse, et même du code JavaScript qui s'exécute dans l'outil lui-même ; ce dernier cas, appelé un *mod*, sort du cadre de ce manuel et relève d'une décision explicite de la DSI.

Ce qu'un plugin ne contient pas : un CLAUDE.md, ni des règles de permission. Les consignes d'entreprise vivent dans le CLAUDE.md géré du chapitre M3, les verrous dans les paramètres gérés du chapitre M4. Le socle du roman réunit en fait les trois, comme le montre la section consacrée au socle.

### Des noms préfixés

Les skills et les sous-agents d'un plugin prennent son nom en préfixe : la skill `prepare-relecture` du plugin `outils-sinistres` se lance avec `/outils-sinistres:prepare-relecture`, et son sous-agent s'appelle `outils-sinistres:relecteur`. Deux plugins peuvent ainsi proposer chacun une skill `relecture` sans conflit. Les outils de ses serveurs MCP prennent la forme `mcp__plugin_outils-sinistres_<serveur>__<outil>`, à utiliser tels quels dans les règles de permission et les filtres de hooks.

### Quand passer au plugin

Une skill rangée dans `.claude/skills/` d'un dépôt suffit tant qu'elle sert une équipe dans un dépôt. Le plugin devient utile dès que l'une de ces conditions apparaît :

- les mêmes pièces servent dans **plusieurs dépôts** ;
- **plusieurs équipes** doivent recevoir les mêmes outils, et leurs mises à jour ;
- il faut savoir **quelle version** tourne sur quel poste ;
- la DSI veut **imposer** un ensemble à tous.

### Ce que coûte un plugin activé

Un plugin activé est présent dans chaque session, qu'on s'en serve ou non. Le nom et la description de chacune de ses skills et de ses sous-agents occupent le contexte à chaque message ; ses serveurs MCP tournent ; ses hooks se déclenchent. Et tout ce qu'il exécute, il l'exécute avec vos droits. C'est pourquoi un socle doit rester court, et un catalogue se tient propre.

## Installer et gérer des plugins

Un plugin s'installe depuis une marketplace, c'est-à-dire un catalogue : un dépôt qui contient un fichier `.claude-plugin/marketplace.json` listant des plugins et l'endroit où trouver chacun. On déclare le catalogue une fois, puis on installe ses plugins par leur nom, sous la forme `plugin@catalogue`.

```bash
claude plugin marketplace add https://git.mutuelle.intra/outils/catalogue-agents.git
claude plugin install outils-sinistres@catalogue-agents --scope project
```

Dans une session, `/plugin` ouvre le gestionnaire : l'onglet *Discover* parcourt les catalogues déclarés, *Installed* liste les plugins installés et signale ceux qui ne servent plus, *Marketplaces* gère les catalogues, *Errors* dit pourquoi un plugin n'a pas pu se charger.

### Trois portées

| Portée | Option | Pour qui | Où c'est noté |
| --- | --- | --- | --- |
| Utilisateur | `--scope user` | Vous, dans tous vos projets | `~/.claude/settings.json` |
| Projet | `--scope project` | Toute l'équipe du dépôt | `.claude/settings.json`, versionné |
| Local | `--scope local` | Vous, dans ce dépôt | `.claude/settings.local.json` |

La portée projet a une subtilité : elle déclare le plugin dans les paramètres versionnés, mais chacun doit encore l'installer sur son poste. Un plugin tiré d'un catalogue par un chemin relatif s'installe de lui-même une fois le dossier approuvé ; un plugin qui vient d'un autre dépôt demande la commande d'installation à chaque développeur, et l'outil le rappelle par un message tant qu'elle n'a pas été lancée.

### Les commandes du quotidien

| Commande | Effet |
| --- | --- |
| `claude plugin list` | Les plugins installés et leur état |
| `claude plugin details <nom>` | Les skills, sous-agents, hooks et serveurs que le plugin apporte |
| `claude plugin disable <nom>` | Le désactive sans le désinstaller |
| `claude plugin uninstall <nom>` | Le retire |
| `claude plugin marketplace update <catalogue>` | Rafraîchit le catalogue et ses versions |
| `/reload-plugins` | Applique les changements dans la session en cours |

### Avec la configuration de référence

Au premier lancement interactif, l'outil déclare de lui-même le catalogue officiel de l'éditeur, hébergé sur GitHub. Sur les postes isolés du chapitre M4, il n'est pas joignable, et la politique d'entreprise doit de toute façon le refuser : la section sur le socle montre comment. Les plugins synchronisés depuis un compte claude.ai ne s'appliquent pas non plus avec Bedrock. Tout passe donc par le catalogue interne de la maison.

## Créer le plugin de l'équipe

Au chapitre 18, Sofiane réunit les quatre savoir-faire de l'équipe : préparer une story, écrire les scénarios d'acceptation, préparer les relectures, tenir le wiki. Ajoutons-y le sous-agent relecteur du chapitre M5 et le formateur du chapitre M6, et voici la boîte à outils de l'équipe.

```text
outils-sinistres/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── preparer-story/SKILL.md
│   ├── ecrire-scenarios/SKILL.md
│   ├── prepare-relecture/SKILL.md
│   └── tenir-wiki/SKILL.md
├── agents/
│   └── relecteur.md
├── hooks/
│   └── hooks.json
└── scripts/
    └── formater.sh
```

Seul `plugin.json` se range dans `.claude-plugin/` ; les autres dossiers sont à la racine du plugin. Le manifeste :

```json
{
  "name": "outils-sinistres",
  "description": "Boîte à outils de l'équipe portail sinistres : stories, scénarios, relectures, wiki",
  "version": "1.4.0",
  "author": { "name": "Équipe portail sinistres" }
}
```

Le nom devient le préfixe de toutes les commandes ; il ne contient pas d'espace. La version, quand elle est indiquée, fixe ce que reçoivent les postes : tant qu'elle ne change pas, ils gardent la même.

### Désigner ses propres fichiers

Dans les hooks et les serveurs MCP d'un plugin, `${CLAUDE_PLUGIN_ROOT}` désigne le dossier où le plugin est installé, et `${CLAUDE_PLUGIN_DATA}` un dossier de données qui survit aux mises à jour. Le hook de formatage s'écrit donc ainsi, dans `hooks/hooks.json` :

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/formater.sh",
            "args": [],
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

Pensez aussi aux références entre pièces : dans un plugin, la skill de préparation des relectures appelle le sous-agent sous son nom préfixé, `outils-sinistres:relecteur`. Et un sous-agent livré par un plugin ne peut pas déclarer ses propres hooks, serveurs MCP ou mode de permission : ces champs sont ignorés, par sécurité.

### Essayer sans publier

```bash
claude plugin validate ./outils-sinistres
claude --plugin-dir ./outils-sinistres
```

La première commande vérifie le manifeste et l'en-tête de chaque skill et sous-agent ; elle se termine par *Validation passed*. La seconde charge le plugin pour une session seulement, sans rien installer. Après une modification, `/reload-plugins` la prend en compte sans redémarrer ; l'onglet *Errors* de `/plugin` dit ce qui n'a pas pu se charger.

Si les pièces vivaient déjà dans le `.claude/` d'un dépôt, retirez les originaux une fois le plugin vérifié. Les skills ne se gêneraient pas, grâce au préfixe, mais un hook présent aux deux endroits s'exécuterait deux fois.

### Vérifier qu'il change vraiment le comportement

Un plugin qui se charge sans erreur peut ne rien changer à ce que fait l'agent. La commande `claude plugin eval` rejoue une série de cas, avec et sans le plugin, et mesure la différence : la skill de préparation des relectures produit-elle bien une fiche en quatre rubriques, et seulement quand on la lance ? C'est le test qui donne le droit de publier une nouvelle version.

## Une marketplace privée d'entreprise

Une marketplace n'est pas une boutique hébergée : c'est un dépôt Git, ici sur le Git interne de la maison, avec un fichier qui liste les plugins. Ceux qui y ont accès le déclarent une fois et installent ensuite par nom.

> *Schéma non reproduit dans cette version Markdown : du dépôt aux postes · un même catalogue sert les deux chemins.*

### Le fichier du catalogue

Dans `catalogue-agents/.claude-plugin/marketplace.json` :

```json
{
  "name": "catalogue-agents",
  "description": "Plugins approuvés pour les agents de développement de la maison",
  "owner": { "name": "DSI — outillage de développement" },
  "plugins": [
    {
      "name": "socle-agents",
      "source": "./plugins/socle-agents",
      "description": "Garde-fous communs à toutes les équipes"
    },
    {
      "name": "outils-sinistres",
      "source": {
        "source": "url",
        "url": "https://git.mutuelle.intra/sinistres/outils-sinistres.git",
        "ref": "v1.4.0"
      },
      "description": "Boîte à outils de l'équipe portail sinistres"
    }
  ]
}
```

Chaque entrée dit où trouver un plugin : un chemin relatif pour un plugin rangé dans le dépôt du catalogue lui-même, ou un dépôt à part, éventuellement figé sur une étiquette ou un commit. Deux règles évitent la plupart des pannes : écrire les chemins relatifs depuis la racine du catalogue, et donner à l'entrée exactement le même nom que dans le `plugin.json` du plugin. `claude plugin validate ./catalogue-agents` vérifie le fichier avant chaque publication.

### Proposer la boîte à outils à une équipe

Pour qu'une équipe reçoive ses outils sans que chacun les cherche, le `.claude/settings.json` de son dépôt déclare le catalogue et active le plugin :

```json
{
  "extraKnownMarketplaces": {
    "catalogue-agents": {
      "source": { "source": "git", "url": "https://git.mutuelle.intra/outils/catalogue-agents.git" }
    }
  },
  "enabledPlugins": {
    "outils-sinistres@catalogue-agents": true
  }
}
```

Le catalogue n'est déclaré qu'une fois le dossier approuvé par chaque développeur. Chacun reste libre de désactiver le plugin pour lui-même : c'est un outil proposé, pas imposé.

### Publier une nouvelle version

Le chapitre M5 a posé la règle pour une skill : une propriétaire, une porte, une version. Elle s'étend au plugin entier.

1. **Une demande de fusion** sur le dépôt du plugin, approuvée par la propriétaire de chaque pièce touchée ; un fichier `CODEOWNERS` rend cette approbation obligatoire.
2. **Les évaluations** passent : `claude plugin eval` sur les cas de référence.
3. **La version monte** dans `plugin.json`, et une note dit ce qui change.
4. **Le catalogue pointe** vers la nouvelle étiquette.
5. **Les postes la reçoivent** au démarrage suivant, si la mise à jour automatique est active pour ce catalogue, ou avec `claude plugin marketplace update`.

Pour faire essayer une version à quelques équipes avant toutes les autres, on tient deux catalogues, l'un stable et l'autre en avance, qui pointent vers des étiquettes différentes des mêmes plugins ; chaque groupe de postes reçoit le sien par ses paramètres gérés.

## Imposer un socle

Au chapitre 16, la règle est fixée avant d'écrire une ligne : le socle tiendra en deux pages. Dans les faits, ce « paquet unique » se compose de trois objets que la DSI livre ensemble, parce qu'un plugin ne peut pas tout porter.

| Pièce du socle | Où elle vit | Chapitre |
| --- | --- | --- |
| Les consignes communes : données synthétiques, conduite face à un secret | Le CLAUDE.md géré | M3 |
| Les verrous et les contrôles qui ne doivent jamais céder : interdictions, mode manuel, bac à sable, serveurs MCP approuvés, hook des journaux | Les paramètres gérés | M4, M7 |
| Les outils communs : le journal des actions, la skill des trois questions de sécurité | Le plugin `socle-agents` | M5, M6 |

### Les clés à ajouter aux paramètres gérés

Ce bloc s'ajoute au `managed-settings.json` du chapitre M4 :

```json
{
  "extraKnownMarketplaces": {
    "catalogue-agents": {
      "source": { "source": "git", "url": "https://git.mutuelle.intra/outils/catalogue-agents.git" },
      "autoUpdate": true
    }
  },
  "enabledPlugins": {
    "socle-agents@catalogue-agents": true
  },
  "strictKnownMarketplaces": [
    { "source": "hostPattern", "hostPattern": "^git\\.mutuelle\\.intra$" }
  ],
  "disableSideloadFlags": true
}
```

| Clé | Effet |
| --- | --- |
| `extraKnownMarketplaces` | Déclare le catalogue interne sur chaque poste, sans action de personne. |
| `enabledPlugins` | Installe le socle au démarrage de la session suivante. Le désactiver dans ses propres paramètres n'empêche pas son chargement : les paramètres gérés l'emportent. |
| `strictKnownMarketplaces` | N'accepte que les catalogues hébergés sur le Git interne. Le catalogue officiel de l'éditeur, comme tout autre, est refusé. |
| `disableSideloadFlags` | Refuse le chargement d'un plugin depuis un dossier ou une adresse avec `--plugin-dir` ou `--plugin-url`. |

Un plugin activé d'office ne se désinstalle pas, mais un développeur pourrait encore couper tous ses hooks avec `disableAllHooks` dans ses propres paramètres. Les contrôles qui doivent tenir à coup sûr, comme celui des journaux, restent donc déclarés directement dans les paramètres gérés, comme au chapitre M6 : là, aucun réglage du poste ne les désactive. Le plugin porte le reste. Inutile pour autant de poser `allowManagedHooksOnly`, qui couperait en plus les hooks des équipes, dont leur formateur : le socle impose ses contrôles sans interdire ceux des équipes.

Deux effets de bord sont à connaître. La liste des catalogues autorisés bloque aussi les plugins rangés dans les dossiers de skills personnels ; on les réautorise en ajoutant l'entrée `{ "source": "skills-dir" }`. Et `disableSideloadFlags` gêne les auteurs de plugins, qui essaient leurs versions avec `--plugin-dir` : ils travaillent alors avec le catalogue en avance, ou sur un poste dédié à l'outillage, qui reçoit d'autres paramètres gérés.

### Vérifier sur un poste

| Essai | Résultat attendu |
| --- | --- |
| `/plugin`, onglet *Installed* | Le socle est présent, signalé comme imposé. |
| `claude plugin disable socle-agents` puis nouvelle session | Le socle se charge quand même. |
| `/plugin marketplace add https://github.com/exemple/catalogue` | Refus, avec le message *is blocked by enterprise policy*. |
| `claude --plugin-dir ./essai` | L'outil refuse de démarrer et nomme `disableSideloadFlags`. |

### Une équipe qui arrive

Au chapitre 16, la directrice générale veut qu'une équipe du prestataire Horizon travaille avec le socle dès janvier, sur le compte AWS de la maison et avec les mêmes règles que le pilote. C'est tout l'intérêt du dispositif : rien à expliquer, rien à installer à la main. L'équipe reçoit ses postes avec les paramètres gérés, ouvre l'outil, et le socle est là, comme on reçoit son badge le premier jour. Le chapitre M12 détaille ce qu'une nouvelle équipe reçoit, et ce qu'elle apprend encore à faire seule.

## Sécurité et gouvernance

Installer un plugin, c'est accepter d'exécuter son code sur le poste, avec les droits de la personne : ses hooks, ses serveurs MCP locaux, et pour certains plugins une commande qui fabrique le plugin lui-même au moment de l'installation. Un catalogue approuvé est donc une liste de logiciels approuvés, et se gère comme telle.

### Ce qu'on vérifie avant d'accepter un plugin

| Question | Où regarder |
| --- | --- |
| Quels hooks lance-t-il, et sur quels événements ? | `hooks/hooks.json` et les scripts qu'il appelle |
| Quels serveurs MCP démarre-t-il, avec quelle commande ? | `.mcp.json` ; une commande `npx -y` sans version figée est un refus |
| Que disent ses skills et ses sous-agents ? | Les fichiers Markdown : ils deviennent des consignes pour l'agent |
| D'où vient-il, et qui le maintient ? | Le dépôt source, son historique, son propriétaire |
| Combien coûte-t-il en contexte ? | Le nombre et la longueur des descriptions de skills et de sous-agents |

### Les réglages qui limitent le risque

- **`strictKnownMarketplaces`** : seuls les catalogues internes sont acceptés, ce qui place chaque plugin derrière une relecture de la DSI.
- **Des versions figées** : le catalogue pointe vers une étiquette ou un commit, jamais vers une branche qui bouge.
- **`disableCommandPluginSources`** : refuse les plugins qui se fabriquent en exécutant une commande sur le poste.
- **Les mods** : un plugin qui embarque du JavaScript exécuté dans l'outil lui-même peut, sur certains postes, approuver une action qu'un hook aurait refusée. La clé `allowManagedModsOnly` n'autorise que ceux de l'organisation ; dans la configuration de référence, aucun n'est accepté.
- **La télémétrie** : les événements `plugin_installed` et `plugin_loaded` disent quels plugins tournent sur quels postes (chapitre M14).

### Qui décide de quoi

Au chapitre 16, la commission sécurité désigne une responsable du socle, Mathilde, et un référent technique, Julien. Le partage vaut pour tout le catalogue.

| Rôle | Responsabilité |
| --- | --- |
| Responsable du socle | Ce qui entre dans le socle, et ce qui en sort ; la règle des deux pages |
| Référent technique | Le fonctionnement des pièces, les tests, les versions |
| Propriétaire d'une skill | Le contenu de sa skill, et l'approbation de ses modifications (chapitre M5) |
| DSI, outillage | Le dépôt du catalogue, les paramètres gérés, la diffusion sur les postes |

### Tenir le catalogue propre

Un plugin activé coûte du contexte à chaque message, même inutilisé. L'onglet *Installed* de `/plugin` signale ceux qui n'ont pas servi récemment, et le bilan `/doctor` compare les skills, serveurs et plugins installés à ce qu'ils coûtent en contexte. Une revue trimestrielle retire du catalogue ce que personne n'appelle, et vérifie que le socle tient toujours en deux pages. Au chapitre 16, Julien y tenait plus que tout : un socle qui grossit finit par être contourné.

## Dans le roman

| Chapitre | Scène | Ce qu'elle illustre ici |
| --- | --- | --- |
| 16 — La sécurité au quotidien | Mathilde trouve les garde-fous de l'équipe éparpillés en cinq endroits ; Sofiane propose de les réunir dans un paquet unique, publié dans un catalogue interne et imposé par les paramètres gérés. | Le socle : un plugin, des paramètres gérés, un CLAUDE.md d'entreprise, livrés ensemble. |
| 16 — La sécurité au quotidien | Avant d'écrire une ligne, Julien impose que le socle tienne en deux pages. | Un plugin activé coûte à chaque message ; un socle qui grossit est contourné. |
| 16 — La sécurité au quotidien | La commission valide le socle pour toute la maison, y compris l'équipe d'Horizon qui démarre en janvier ; Mathilde en est la responsable, Julien le référent technique. | Imposer sans rien installer à la main ; désigner qui décide. |
| 18 — Les rôles bougent | Sofiane empaquette quatre savoir-faire en skills ; Nadia corrige la sienne et en devient propriétaire. | La boîte à outils d'équipe, proposée par les paramètres du projet, versionnée et relue. |

Pour aller plus loin : M3 (CLAUDE.md d'entreprise), M4 (paramètres gérés), M5 (skills et sous-agents), M6 (hooks), M7 (serveurs MCP), M12 (partager en équipe : ce qu'une nouvelle équipe reçoit le premier jour).

## Sources

Consultées le 21 octobre 2026.

- [Vue d'ensemble des plugins](https://code.claude.com/docs/en/plugins/overview)
- [Créer un plugin](https://code.claude.com/docs/en/plugins/create)
- [Créer une marketplace](https://code.claude.com/docs/en/plugins/create-marketplace)
- [Gérer les plugins pour une organisation](https://code.claude.com/docs/en/plugins/org)
- [Sécurité et confiance des plugins](https://code.claude.com/docs/en/plugins/security)
- [Tester un plugin avec des évaluations](https://code.claude.com/docs/en/plugin-evals)
