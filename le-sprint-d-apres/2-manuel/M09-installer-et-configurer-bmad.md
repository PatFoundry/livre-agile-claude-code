# M9 — Installer et configurer BMAD

*Partie II — Le manuel de référence*

## Ce que couvre ce chapitre

BMAD, pour *Breakthrough Method for Agile AI-Driven Development*, est une méthode libre qui installe dans l'agent des rôles et des déroulés de travail : un analyste, un chef de produit, un architecte, un développeur, un designer d'expérience, et les étapes qui mènent d'une intention floue à du code relu. Ce chapitre explique comment l'installer dans un projet, choisir la quantité de méthode qu'un travail mérite, la plier aux usages de la maison, et la faire évoluer sans perdre ce qu'on y a ajouté.

Le roman y consacre sa dernière partie. Au chapitre 20, Sofiane présente la méthode à la rétrospective de fin de phase, et l'équipe découvre que les deux tiers de ce qu'elle demande existent déjà sous d'autres noms. Au chapitre 22, la sécurité lit les fichiers de la méthode avant qu'ils entrent dans le dépôt, et l'agent analyste pose quatre-vingt-sept questions à deux gestionnaires. Les chapitres 23 et 24 suivent le chef de produit et l'architecte ; le chapitre 25 supprime une vérité de trop ; le chapitre 27 fait le bilan.

> **Version de référence.** BMAD 6.12.2, publiée le 11 octobre 2026, avec Claude Code 2.1.301 et la configuration Bedrock du chapitre M1. La branche 6.12 est figée, hors corrections. La version 7, annoncée pour la mi-octobre, était encore en préversion à la date de rédaction ; elle change le mode d'installation et renomme plusieurs skills. La dernière section dit comment préparer ce passage.

BMAD évolue plus vite que tout le reste de ce manuel : la plupart des guides en circulation décrivent une version que l'installateur ne fournit plus. D'où le fil de ce chapitre : figer une version, la lire, l'adapter, et ne la changer que délibérément.

## Ce qu'est BMAD

Techniquement, BMAD est un ensemble de skills, au sens du chapitre M5 : des fichiers de consignes, de modèles de documents et de listes de contrôle, accompagnés de quelques scripts. L'installateur les dépose dans le projet ; l'agent les charge quand on les appelle. La méthode est publiée sous licence MIT, gratuite, sans version payante.

Sur le fond, elle repose sur une idée simple : un agent de code transforme volontiers des hypothèses non dites en code. BMAD l'oblige à les rendre explicites et à les écrire, pour que chaque décision serve de contexte à la suivante au lieu d'être réexpliquée dans chaque conversation.

### Quatre phases, des documents à chaque étape

| Phase | Question | Ce qu'elle produit |
| --- | --- | --- |
| Analyse | Qu'essaie-t-on de résoudre, et pour qui ? | Un brief produit, des notes de recherche |
| Planification | Que doit faire le produit ? | Un document d'exigences, le PRD ; une description de l'expérience |
| Conception | Comment les parties tiennent-elles ensemble ? | Une architecture ; des epics et des stories |
| Implémentation | Comment livrer chaque story ? | Une spécification par story, le code, ses tests, sa relecture |

Tout est écrit en fichiers, dans le dépôt, relus et validés par des humains avant l'étape suivante. C'est ce que Sofiane dessine au tableau, au chapitre 20.

### Ce que BMAD ne fait pas

- **Il ne remplace pas votre cadre agile.** Pas de cérémonies, pas de rôles humains : la méthode outille le travail de l'équipe Scrum et du train, elle ne le réorganise pas.
- **Il ne décide pas à la place du métier.** L'analyste pose des questions ; il ne tranche pas. Une question sans réponse reste une question, avec le nom de qui peut répondre.
- **Il ne garantit pas ses propres étapes.** Les points d'arrêt de la méthode, comme l'approbation d'une spécification, sont des consignes ; elles tiennent tant que l'agent les suit. Les verrous restent ceux des chapitres M4 et M6.
- **Il ne passe pas au-dessus du socle.** Au chapitre 22, Mathilde le formule ainsi : si une consigne de la méthode contredit un garde-fou, c'est le garde-fou qui gagne, parce que ce n'est pas l'agent qui décide.

### Deux tiers déjà là

Au chapitre 20, l'équipe confronte la méthode à ce qu'elle pratique déjà. La vision, le glossaire, les stories préparées avec le métier, les scénarios d'acceptation, la relecture préparée par un agent qui n'a pas écrit le code : les deux tiers existent, sous d'autres noms. Ce qui manque, c'est l'ordre, et un endroit unique où tout se tient. La décision qui suit est le premier conseil de ce chapitre : adapter la méthode aux artefacts existants, plutôt que l'inverse.

## Choisir son niveau

BMAD ne demande pas la même quantité de documents pour une correction de libellé et pour un nouveau produit. Les premières versions 6 proposaient trois niveaux nommés, rapide, méthode et entreprise ; le roman en garde le vocabulaire. Depuis, les noms ont disparu au profit d'une question unique : quelle est la taille du travail, et combien de personnes doivent s'accorder sur ce qu'il faut faire ?

| Le travail | Ce qu'on lance | Ce qu'on obtient |
| --- | --- | --- |
| Une coquille, un changement évident | Rien : on le demande directement à l'agent | Le changement, relu comme d'habitude |
| Un changement clair, qui tient en une session | `bmad-build` | Une spécification, des questions, une approbation, le code, trois relectures, un commit |
| Un résultat qui demande plusieurs sessions | `bmad-spec`, puis le découpage en stories | Une spécification d'epic, des stories, puis un `bmad-build` par story et une rétrospective |
| Un produit, ou un travail que plusieurs personnes doivent approuver | `bmad-prd`, `bmad-architecture`, epics et planification | Les documents que l'organisation signe, puis le chemin précédent pour chaque epic |
| Une intention encore floue | `bmad-forge-idea`, `bmad-brainstorming`, `bmad-deep-recon` | Une idée éprouvée, ou une note de recherche sourcée |

La documentation de la méthode estime une session à environ cinq cents lignes de code, tests non compris. Au-delà, on découpe.

### Choisir d'après ses obligations

Au chapitre 22, l'équipe choisit le niveau le plus complet, celui qu'on appelait entreprise. Pas à cause de la taille de la phase 2, qui ne l'exigerait pas, mais à cause de ses obligations : le règlement européen sur la résilience numérique du secteur financier, DORA, demande de pouvoir montrer ce qui a été décidé et par qui ; et les échanges avec deux autres équipes du train exigent des documents que d'autres liront.

C'est la bonne façon de trancher. Le niveau se choisit d'après ce que l'organisation doit pouvoir prouver et coordonner, pas d'après l'ampleur apparente de la fonctionnalité.

### La règle qui empêche la paperasse

Un niveau complet fabrique beaucoup de documents. L'équipe y ajoute une règle, qui vaut pour tous les niveaux : **pas de document sans propriétaire ni lecteur.** Avant de lancer un déroulé, on écrit qui validera le document produit et qui s'en servira ensuite. Si personne ne le lira, on ne le produit pas. Le tableau des propriétaires du dépôt reçoit une colonne de plus, *Lu par*.

## Installer BMAD dans un projet

### D'abord, lire

Au chapitre 22, rien n'entre dans le dépôt avant que Mathilde ait lu les fichiers que l'agent chargera : des centaines de consignes, de déroulés et de modèles, aucun programme caché. « Des consignes, ça s'exécute aussi. Seulement, ça s'exécute dans la tête de l'agent. » Elle fait retirer les modules dont l'équipe ne se servira pas, et pose quatre réserves, qui se traduisent toutes en réglages.

| Réserve de la sécurité | Traduction |
| --- | --- |
| Pas de recherche sur internet | Les déroulés de recherche ne servent qu'à partir des documents internes ; l'outil de lecture web est déjà retiré par les paramètres gérés (chapitre M4). |
| Aucun dossier réel | Une consigne permanente ajoutée aux agents de la méthode (section sur la personnalisation). |
| Une version figée, au catalogue interne | Une version précise, installée une fois, versionnée dans le dépôt, et changée seulement par la procédure de la dernière section. |
| Le socle au-dessus de tout | Rien à régler : les verrous des paramètres gérés s'appliquent aux skills de la méthode comme au reste. |

### Les prérequis

Node.js 20.12 ou plus récent, Python 3.10 ou plus récent, et `uv`, le gestionnaire qui exécute les scripts Python de la méthode. Le dernier est indispensable : la skill d'implémentation commence par lancer un script qui prépare son déroulé, et s'arrête net si `uv` est absent. Sur les postes isolés du chapitre M4, `npm` et `uv` doivent passer par le miroir interne des bibliothèques.

### La commande

Le référent technique installe une fois, avec une version explicite et sans questions :

```bash
npx bmad-method@6.12.2 install --yes --modules bmm --tools claude-code
npx bmad-method status
```

Le module `bmm` est la méthode elle-même ; d'autres modules existent, pour la conception de tests ou la créativité, et ne s'ajoutent qu'après la même lecture. `--tools claude-code` produit des skills au format de Claude Code. La seconde commande vérifie l'installation.

### Ce qui apparaît dans le dépôt

```text
.claude/skills/
├── bmad-build/          la skill d'implémentation
├── bmad-help/           dit quoi faire ensuite
├── bmad-agent-analyst/  et les autres rôles
└── …                    une trentaine de skills
_bmad/
├── config.toml          réglages de l'installateur, régénérés à chaque installation
├── config.user.toml     votre nom et votre langue
├── custom/              vos personnalisations, jamais touchées par l'installateur
├── scripts/             les scripts Python de la méthode
└── render/              fichiers de travail
_bmad-output/
├── planning-artifacts/        briefs, PRD, architecture
└── implementation-artifacts/  une spécification par story
```

L'installateur n'écrit ni CLAUDE.md ni AGENTS.md, et ne touche pas au code.

### Ce qu'on versionne

On versionne tout ce qui fait la méthode de l'équipe : les skills de `.claude/skills/bmad-*`, le dossier `_bmad/` et ses personnalisations, les documents de `_bmad-output/`. C'est ce qui permet à chacun de recevoir exactement la version lue par la sécurité, sans réinstaller. On exclut deux choses dans le `.gitignore` : `_bmad/render/`, qui contient des fichiers de travail, et `_bmad/config.user.toml`, qui porte les préférences de chacun et que l'installateur n'exclut pas de lui-même.

### Deux réglages pour Claude Code

La skill d'implémentation lance ses scripts avec `uv run`. Pour éviter une demande d'autorisation à chaque story, l'équipe ajoute la règle `"Bash(uv run _bmad/scripts/*)"` aux autorisations du projet (chapitre M4). Et cette skill refuse de démarrer sur un dépôt qui contient des modifications non commitées : on commite l'installation elle-même avant la première story.

## Les agents et les phases

Chaque phase a son rôle, incarné par un agent qui porte un prénom, un ton et un menu. Ce sont des personnages au sens propre : la même session de Claude Code, chargée d'une skill qui lui donne un point de vue et des déroulés.

> *Schéma non reproduit dans cette version Markdown : quatre phases, quatre rôles principaux · Sally, la designer, rejoint la planification.*

| Agent | Skill | Ce que son menu lance |
| --- | --- | --- |
| Mary, l'analyste | `bmad-agent-analyst` | Remue-méninges, recherche, brief produit, contexte du projet |
| John, chef de produit | `bmad-agent-pm` | PRD, epics et stories, vérification avant implémentation, correction de cap |
| Sally, designer d'expérience | `bmad-agent-ux-designer` | Description de l'expérience et des écrans |
| Winston, l'architecte | `bmad-agent-architect` | Architecture, vérification avant implémentation |
| Amelia, la développeuse | `bmad-agent-dev` | Implémentation, relecture de code, tests, planification de sprint, rétrospective |

Les versions précédentes avaient aussi un Scrum Master qui préparait chaque story et un agent de qualité ; ils ont été fondus dans le rôle de développeuse. Ce que Sofiane décrit au chapitre 20, un agent qui prépare la story, un autre qui la code, un autre qui la relit, vit désormais dans une seule skill, `bmad-build`, qui confie chaque étape à un sous-agent distinct.

### Trois façons de travailler avec eux

- **Demander quoi faire.** `/bmad-help` lit l'état du projet et nomme la prochaine étape. C'est la porte d'entrée quand on hésite.
- **Appeler un rôle.** `/bmad-agent-pm` charge John, qui se présente et affiche son menu ; on choisit une entrée par son code de deux lettres.
- **Appeler un déroulé.** Quand on sait ce qu'on veut, on appelle directement la skill : `/bmad-prd`, `/bmad-architecture`, `/bmad-build`. C'est ce que recommande la documentation de la méthode.

Un quatrième mode réunit plusieurs rôles autour d'un même problème : `bmad-party-mode` fait débattre l'analyste, l'architecte et le chef de produit, chacun avec son point de vue. Utile pour faire apparaître un désaccord, à condition qu'un humain tranche.

### Où vont les documents

Les documents de planification sont rangés dans `_bmad-output/planning-artifacts/`, une spécification par story dans `_bmad-output/implementation-artifacts/`. Dans le roman, chacun porte en tête le nom de qui l'a validé : au chapitre 22, Nadia et Sabine signent le brief de six pages, « chacune de son nom, dans le dépôt, à côté du code ».

### Une leçon de l'analyste

Le chapitre 22 montre la phase la moins spectaculaire et l'une des plus utiles. L'agent analyste lit d'abord tout ce que la maison sait déjà, pour ne poser aux gens que les questions auxquelles les documents ne répondent pas. Puis il interroge deux gestionnaires, une question à la fois, en notant qui a répondu : quatre-vingt-sept questions, dont onze restent à confirmer, chacune avec le nom de qui peut trancher. Et il ouvre une rubrique que personne n'avait jamais écrite : *Ce que le portail ne fera pas*, avec la raison de chaque refus.

## Une story de bout en bout

Une story déjà préparée avec le métier, qui tient en une session, passe par une seule skill. Sur une branche qui porte la clé Jira, dépôt propre :

```text
/bmad-build SIN-57 : le déclarant peut joindre jusqu'à dix photos par déclaration.
Critères d'acceptation : docs/stories/SIN-57.md
```

### Ce que fait la skill

1. **Elle enquête.** L'agent lit le code concerné, sans rien modifier.
2. **Elle rédige une spécification**, dans `_bmad-output/implementation-artifacts/`, et y note trois choses : ce que la demande ne dit pas et que le code ne tranche pas, les actions irréversibles, l'étendue de la modification.
3. **Elle pose ses questions.** Chaque point que la demande laisse ouvert devient une question, avec souvent une recommandation. La skill a pour consigne de ne jamais transformer un trou de la demande en hypothèse.
4. **Elle fige les réponses.** Elles entrent dans un bloc de la spécification marqué comme intangible après approbation : c'est la part humaine, que l'agent ne doit plus modifier.
5. **Elle attend l'approbation.** Un menu propose d'approuver et continuer, d'approuver et s'arrêter, ou de relire d'abord.
6. **Elle implémente**, par un sous-agent.
7. **Elle fait relire**, par trois sous-agents en parallèle : un qui voit le code sans connaître l'intention, un qui chasse les cas limites, un qui cherche les comportements qu'aucun test ne couvrirait. Chaque remarque est triée, retenue ou écartée avec sa raison, dans la spécification.
8. **Elle commite**, la spécification avec le code, en local.

Le point 3 est la vraie valeur de la méthode, et c'est le même réflexe que la consigne « ne jamais inventer une règle de gestion ; poser la question » du chapitre M3.

### Ce que l'équipe ajoute autour

La skill s'arrête au commit local. La suite reste celle des chapitres précédents : la clé Jira dans la branche et le commit (chapitre M10), la préparation de la relecture par un agent qui n'a pas écrit le code et la relecture humaine (chapitre M5), les scénarios d'acceptation verrouillés (chapitre M4), les hooks du socle (chapitre M6). BMAD s'insère dans ce circuit ; il ne le remplace pas.

### Un point d'arrêt qui tient… tant qu'on le respecte

L'approbation de la spécification est une consigne, pas un verrou. Une phrase comme « j'approuve d'avance, implémente directement » suffit à faire prendre à la skill un chemin court : plus de questions, plus d'approbation, un seul relecteur au lieu de trois. Et les changements d'état de la spécification, de *brouillon* à *terminé*, sont écrits par l'agent lui-même.

Pour que l'approbation laisse une trace qu'un programme peut vérifier, l'équipe ajoute au modèle de spécification une ligne *Approuvé par*, que seule une personne remplit, et la chaîne d'intégration refuse une demande de fusion dont la spécification ne la porte pas (chapitre M10). C'est la même logique que partout dans ce manuel : ce qui doit tenir à coup sûr ne repose pas sur une consigne.

### Pour un travail plus large

Un résultat qui demande plusieurs sessions passe d'abord par `bmad-spec`, qui condense l'intention en une spécification d'epic et la découpe en stories ; chacune passe ensuite par `bmad-build`, et `bmad-retrospective` juge le résultat d'ensemble à la fin. Le chemin complet ajoute en amont le PRD, l'architecture, puis les epics et la planification des itérations.

Ce dernier chemin crée un fichier de suivi propre à la méthode, qui dit où en est chaque story. Au chapitre 25, l'équipe découvre qu'elle entretient ainsi trois vérités : les stories du dépôt, les tickets de Jira, et ce fichier. Elle supprime le fichier : Jira reste le seul endroit qui dit où en est le travail, l'agent y crée le ticket quand Nadia valide une story, et lit sa priorité avant de la prendre.

### Ce que ça coûte

Une story simple, du lancement au commit, consomme l'équivalent de quelques dollars de jetons. Le chemin complet, avec brief, PRD, architecture et découpage, est fait de longues conversations successives, et coûte bien davantage. Mesurez avant de généraliser (chapitre M14).

## Personnaliser sans casser les montées de version

La règle est absolue : on ne modifie jamais les fichiers installés. L'installateur réécrit les skills de `.claude/skills/bmad-*` et le fichier `_bmad/config.toml` à chaque passage ; une modification faite là disparaît à la mise à jour suivante. Tout ce qui adapte la méthode à la maison va dans `_bmad/custom/`, que l'installateur ne touche jamais.

### Trois niveaux de personnalisation

| Niveau | Fichier | Portée |
| --- | --- | --- |
| Un agent | `_bmad/custom/bmad-agent-<rôle>.toml` | Suit l'agent dans tous les déroulés qu'il lance |
| Un déroulé | `_bmad/custom/<skill>.toml` | Une seule skill : la forme de son document, son modèle |
| L'ensemble | `_bmad/custom/config.toml` | La liste des agents, les réglages communs comme la langue |

Chaque fichier existe en deux versions : la version d'équipe, versionnée, et une version `.user.toml`, personnelle, exclue de Git. Les deux se superposent aux valeurs livrées par la méthode, qui restent visibles dans le fichier `customize.toml` de chaque skill : c'est la liste de ce qu'on peut changer.

### Laisser la méthode écrire ses propres réglages

La skill `bmad-customize` évite d'écrire ces fichiers à la main. On lui dit en français ce qu'on veut changer ; elle choisit le bon niveau, écrit le fichier sous `_bmad/custom/` et vérifie le résultat. Par exemple :

```text
/bmad-customize Pour tous les déroulés de la développeuse : aucune donnée réelle
d'assuré, seulement les jeux synthétiques de tests/donnees ; Jira est la seule
source de l'état des stories ; le glossaire est dans docs/glossaire.md.
```

Le résultat ressemble à ceci :

```toml
# _bmad/custom/bmad-agent-dev.toml
[agent]
persistent_facts = [
  "Aucune donnée réelle d'assuré : uniquement les jeux synthétiques de tests/donnees.",
  "Jira est la seule source de l'état des stories ; ne crée aucun fichier de suivi.",
  "file:{project-root}/docs/glossaire.md",
]
```

C'est ainsi que la deuxième réserve du chapitre 22, aucun dossier réel, entre dans la méthode, et que la décision du chapitre 25 survit aux mises à jour.

### Où ranger une règle

| La règle vaut… | Elle va dans |
| --- | --- |
| pour toute session, avec ou sans BMAD | Le CLAUDE.md du projet (chapitre M3) |
| pour un rôle, dans tous ses déroulés | La personnalisation de l'agent |
| pour un seul déroulé : la forme d'un brief, le modèle d'une spécification | La personnalisation du déroulé |
| à coup sûr, quoi que décide l'agent | Les paramètres ou un hook (chapitres M4 et M6) |

Le glossaire, par exemple, reste dans le CLAUDE.md : il sert aussi quand personne n'appelle la méthode. En revanche, « les PRD de la maison commencent par la rubrique *Ce que le produit ne fera pas* » est une personnalisation du déroulé PRD.

### Qui relit les personnalisations

Un fichier de `_bmad/custom/` change le comportement de l'agent autant qu'une ligne de CLAUDE.md. Il passe donc par une demande de fusion, relue par le référent technique et, pour tout ce qui touche aux données ou aux outils, par la sécurité : la colonne *Lu par* du chapitre 22 vaut aussi pour ces fichiers.

## Monter de version

En un an, BMAD a fondu trois rôles en un, renommé sa skill d'implémentation, rendu `uv` obligatoire, puis annoncé une version 7 qui change jusqu'au mode d'installation. Une équipe qui suit chaque version passe son temps à réapprendre la méthode. Une équipe qui n'en suit aucune finit par utiliser une version que personne ne maintient. Le juste milieu : rester sur une version lue et figée, appliquer ses correctifs, et ne changer de version majeure que par une procédure.

### La procédure

C'est celle que l'équipe applique au chapitre 20 pour essayer la méthode elle-même : une story, une branche, des mesures, une condition d'arrêt.

1. **Lire les notes de version.** Repérer les skills renommées ou retirées, les nouveaux prérequis, les changements de format des personnalisations.
2. **Installer sur une branche**, avec la nouvelle version explicite : `npx bmad-method@<version> install --yes --modules bmm --tools claude-code`. L'installateur ne supprime pas les skills des modules retirés : on efface à la main les dossiers `bmad-*` qui ne figurent plus dans la nouvelle version.
3. **Faire lire la différence.** `git diff --stat .claude/skills _bmad` montre l'étendue du changement ; la sécurité lit les fichiers modifiés, comme au chapitre 22, et la colonne *Lu par* se remplit.
4. **Vérifier les personnalisations.** `/bmad-customize` liste les surcharges en place et contrôle qu'elles s'appliquent toujours.
5. **Essayer sur une story réelle**, en mesurant ce qui compte : le temps, le coût, le nombre de questions posées, les anomalies trouvées ensuite. On fixe avant l'essai ce qui ferait renoncer.
6. **Fusionner**, prévenir les équipes de ce qui change pour elles, et mettre à jour la version de référence du catalogue interne.

En cas d'échec, la branche est abandonnée ; `npx bmad-method uninstall --yes` retire proprement une installation ratée.

### La version 7

| Ce qui change | En 6.12 | En 7 |
| --- | --- | --- |
| Installation | `npx bmad-method install` | `npx skills add`, ou une marketplace de plugins Claude Code |
| Porte d'entrée | `bmad-help` | Une skill `bmad` qui sert de point central |
| Epics et planification | Des skills dédiées et un fichier de suivi | Une skill de tickets, autour d'un rôle de Product Owner |
| Scripts | Un mélange d'appels à `uv` et à Python | `uv run` partout |

Trois conseils pour ce passage. Attendre une version publiée comme stable, pas la préversion. Passer par la marketplace interne du chapitre M8 : la voie plugin de la version 7 s'y prête, avec une version figée et la liste des catalogues autorisés. Et relire de près le nouveau suivi des tickets à la lumière du chapitre 25 : si la méthode recrée un fichier d'état à côté de Jira, l'équipe retrouverait ses trois vérités. La décision de garder Jira comme seule source se retranscrit alors dans une personnalisation.

## Dans le roman

| Chapitre | Scène | Ce qu'elle illustre ici |
| --- | --- | --- |
| 20 — La rétrospective du dernier sprint | Sofiane présente les quatre phases au tableau ; l'équipe constate que les deux tiers existent déjà, et décide d'essayer sur une seule story, sur une branche, avec des mesures et une condition d'arrêt. | Adapter la méthode aux artefacts existants ; la procédure d'essai, reprise pour chaque montée de version. |
| 22 — L'analyste qui pose les bonnes questions | Mathilde lit les fichiers de la méthode et pose quatre réserves ; l'équipe choisit le niveau le plus complet à cause de DORA, avec une règle : pas de document sans propriétaire ni lecteur. | Lire avant d'installer ; choisir son niveau d'après ses obligations. |
| 22 — L'analyste qui pose les bonnes questions | L'agent analyste interroge deux gestionnaires, une question à la fois : quatre-vingt-sept questions, onze à confirmer, et une rubrique *Ce que le portail ne fera pas*. | Le rôle de l'analyste, et des documents signés de noms. |
| 23 — Un PRD que personne n'avait écrit | Le chef de produit tire du brief le document d'exigences de la phase 2. | La phase de planification. |
| 24 — L'architecte et le mainframe | L'architecte confronte la conception au système des contrats. | La phase de conception. |
| 25 — Deux vérités | Stories du dépôt, tickets Jira, fichier de suivi de la méthode : l'équipe supprime la troisième vérité. | Jira seule source de l'état, inscrite dans une personnalisation. |
| 27 — Le sprint d'après | Le bilan de la méthode, une fois l'essai terminé. | Ce qu'une méthode change, et ce qu'elle laisse aux personnes. |

Pour aller plus loin : M3 (CLAUDE.md), M4 (verrous et paramètres gérés), M5 (skills), M8 (catalogue interne), M10 (GitHub et Jira au quotidien), M13 (bonnes pratiques : conduire une rétrospective de fin de phase), M14 (mesurer les coûts).

## Sources

Consultées le 21 octobre 2026.

- [BMAD Method, dépôt officiel](https://github.com/bmad-code-org/BMAD-METHOD)
- [Installer BMad](https://docs.bmad-method.org/start/install-bmad/)
- [Choisir un chemin de planification](https://docs.bmad-method.org/plan/choose-a-planning-path/)
- [Personnaliser BMad](https://docs.bmad-method.org/customize/customize-bmad/)
- [Notes de version](https://github.com/bmad-code-org/BMAD-METHOD/releases)
- [Felipe Fontoura, *BMAD Method: A Real Run in Claude Code*, 13 octobre 2026](https://felipefontoura.com/articles/bmad-method/) — un essai indépendant de la version 6.12.2 dans Claude Code
