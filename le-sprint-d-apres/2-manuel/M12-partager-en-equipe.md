# M12 — Partager en équipe

*Partie II — Le manuel de référence*

## Ce que couvre ce chapitre

Un agent bien réglé sur le poste d'un seul développeur ne fait pas une équipe outillée. Les chapitres précédents ont produit des fichiers : un CLAUDE.md, des règles, des paramètres, des skills, des sous-agents, des hooks, des connecteurs, un wiki. Ce chapitre dit lesquels se partagent et lesquels restent personnels, comment les faire vivre à plusieurs sans qu'ils se dégradent, comment accueillir quelqu'un qui arrive, et comment un savoir-faire passe d'une personne à une équipe, puis à toute la maison.

Le roman en montre le mouvement. Au chapitre 18, l'équipe découvre que ses rôles ont bougé, et Sofiane empaquette ses savoir-faire en skills partageables, chacune avec une propriétaire ; Nadia relit la sienne, la trouve fausse, la corrige, et en devient responsable. Au chapitre 22, une équipe du prestataire Horizon s'apprête à travailler avec les mêmes outils, et Émilie, plutôt que le poste qu'on lui offre, propose de former leurs testeurs. Au chapitre 27, une testeuse qui vient d'arriver comprend une story le matin même.

> **Version de référence.** Claude Code 2.1.301, publiée le 15 octobre 2026, avec la configuration Bedrock du chapitre M1.

La question de fond n'est pas technique : un fichier partagé est un engagement. Quelqu'un en répond, quelqu'un le relit, et quelqu'un le retire quand il ne sert plus.

## Ce qui se partage, et à quel niveau

Chaque fichier de configuration a sa place naturelle, à l'un de trois niveaux. La règle tient en une phrase : **une obligation va dans les paramètres gérés, une consigne utile à tous va dans le dépôt, une préférence reste sur le poste.**

> *Schéma non reproduit dans cette version Markdown : où vit chaque fichier · le dépôt porte ce que l'équipe partage.*

### Le détail, fichier par fichier

| Fichier | Versionné | Qui en répond | Chapitre |
| --- | --- | --- | --- |
| `CLAUDE.md` et `.claude/rules/` | Oui | Le référent technique ; la Product Owner pour le glossaire | M3 |
| `.claude/settings.json` | Oui | Le référent technique, avec la sécurité | M4 |
| `.claude/skills/` | Oui | La propriétaire de chaque skill | M5 |
| `.claude/agents/` | Oui | Le référent technique | M5 |
| `.claude/agent-memory/` | Oui, par défaut : à décider | Le référent technique | M5 |
| Hooks du projet, dans `.claude/settings.json` | Oui | Le référent technique, avec la sécurité | M6 |
| `.mcp.json` | Oui, sans aucun secret | Le référent technique | M7 |
| `.worktreeinclude` | Oui | Le référent technique | M5 |
| `_bmad/` et `_bmad/custom/` | Oui, sauf deux fichiers | Le référent technique | M9 |
| `wiki/` | Oui | Le propriétaire du wiki | M11 |
| `CLAUDE.local.md` | Non | Chacun | M3 |
| `.claude/settings.local.json` | Non | Chacun | M4 |
| `~/.claude/` : réglages, skills et consignes personnels | Non | Chacun | M3 à M5 |
| `~/.claude/projects/` : mémoire automatique et transcriptions | Jamais | Chacun | M2, M3 |
| Paramètres gérés, CLAUDE.md géré, plugin du socle | Hors du dépôt | La DSI | M4, M8 |

Une ligne mérite attention. Un sous-agent qui déclare une mémoire de projet écrit ses notes dans `.claude/agent-memory/`, que l'outil considère comme destiné à être versionné. Ces notes deviennent alors du contexte pour toute l'équipe, sans relecture humaine préalable. La configuration de référence les fait passer par une demande de fusion comme le reste, ou choisit la mémoire locale, qui reste sur le poste.

### Comment les niveaux se combinent

Les consignes, CLAUDE.md et règles, s'additionnent : l'agent lit celles de l'entreprise, de l'équipe et de la personne. Les paramètres, eux, se superposent selon l'ordre du chapitre M4, et ce qu'impose l'entreprise ne peut pas être levé par l'équipe ni par la personne. Une préférence personnelle peut donc ajouter une autorisation pour son confort ; elle ne peut pas lever une interdiction.

## Les fichiers personnels

### Le bloc du .gitignore

Le `.gitignore` du dépôt écarte, pour tout le monde, les fichiers qui ne doivent pas être partagés :

```text
# Claude Code : fichiers personnels
CLAUDE.local.md
.claude/settings.local.json
.claude/agent-memory-local/
.claude/worktrees/

# BMAD : préférences de chacun et fichiers de travail
_bmad/config.user.toml
_bmad/custom/*.user.toml
_bmad/render/

# Secrets
.env
.env.*
```

Deux précisions. Quand l'outil enregistre un réglage dans `.claude/settings.local.json`, il ajoute ce fichier aux exclusions Git personnelles du développeur, pas au `.gitignore` du dépôt : seul ce dernier protège toute l'équipe, y compris le jour où quelqu'un crée le fichier à la main. Et `CLAUDE.local.md` n'est jamais créé par l'outil ; on l'écarte avant que quelqu'un en ait besoin.

### Ce qui ne quitte jamais le poste

Le dossier `~/.claude/projects/` contient la mémoire automatique de l'agent et la transcription intégrale de chaque session : chaque message, chaque commande, chaque contenu de fichier lu. Ces fichiers sont en clair. Trois règles en découlent :

1. **On ne les copie nulle part** : ni dans le dépôt, ni dans un ticket, ni dans une messagerie. Pour partager ce qu'une session a appris, on écrit une ligne dans le CLAUDE.md ou une page dans le wiki, relue comme le reste.
2. **On les garde peu de temps.** L'outil efface les transcriptions au-delà de trente jours par défaut ; les paramètres gérés de la configuration de référence ramènent ce délai à quatorze jours avec `"cleanupPeriodDays": 14`.
3. **On les efface à la fin d'un projet.** `claude purge <chemin du projet>` supprime les transcriptions, la mémoire automatique et l'historique propres à ce projet, après avoir affiché ce qui sera effacé.

### Vérifier que rien ne s'échappe

Un fichier personnel versionné par erreur ne se voit pas : il se charge chez tout le monde, sans bruit. Le contrôle des conventions du chapitre M10 reçoit donc une ligne de plus, qui échoue si l'un de ces fichiers est suivi par Git :

```bash
test -z "$(git ls-files CLAUDE.local.md .claude/settings.local.json _bmad/config.user.toml)" \
  || { echo "Un fichier personnel est versionné."; exit 1; }
```

## Faire vivre les fichiers partagés

### Le propriétaire est celui qui sait

Au chapitre 18, Sofiane a écrit la skill qui décrit comment un gestionnaire recueille une déclaration. Nadia la lit et l'arrête net : elle ne pose jamais les questions dans cet ordre. Parler des pièces justificatives trop tôt, c'est laisser croire à l'assuré qu'on le soupçonne ; elle commence par ce qui s'est passé, puis par ce qu'il a déjà fait pour limiter les dégâts. Elle corrige la skill, et en devient la propriétaire.

La règle est là : le propriétaire d'un fichier partagé n'est pas celui qui l'a écrit, mais celui qui sait si ce qu'il dit est juste. L'agent ou le développeur rédigent ; le métier, la recette, la sécurité répondent du contenu qui les concerne.

### Le registre des propriétaires

Un tableau, versionné à la racine du dépôt, dit qui répond de quoi. Le chapitre 22 lui ajoute une colonne : qui le lit.

| Fichier | Propriétaire | Lu par | Dernière revue |
| --- | --- | --- | --- |
| `CLAUDE.md` | Julien | Toute l'équipe, tous les agents | Septembre |
| Glossaire, dans `CLAUDE.md` | Nadia | Toute l'équipe, tous les agents | Septembre |
| Skill `preparer-story` | Nadia | Sofiane, l'agent | Octobre |
| Skill `ecrire-scenarios` | Émilie | L'équipe, l'agent | Octobre |
| Skill `prepare-relecture` | Julien | Les relecteurs | Octobre |
| Hooks et `.claude/settings.json` | Julien | Mathilde | Octobre |
| `wiki/` | Julien | L'équipe, les agents, Horizon | Octobre |

Un fichier sans propriétaire est retiré ou attribué ; un fichier sans lecteur n'aurait pas dû être écrit. Le fichier des propriétaires du chapitre M10 traduit ce tableau en approbations obligatoires.

### Chaque changement se relit et se dit

Modifier une ligne de CLAUDE.md ou d'une skill change le comportement de tous les agents de l'équipe. Cela passe donc par une demande de fusion, approuvée par le propriétaire, avec dans la description une phrase de plus que pour du code : **ce qui change pour l'agent**. Par exemple : « l'agent demandera désormais la date de survenance avant les pièces justificatives ».

Pour une skill importante, on vérifie le changement avant de le fusionner : une story rejouée avec l'ancienne et la nouvelle version, ou les évaluations du chapitre M8 quand la skill vit dans un plugin.

### Une revue mensuelle de trente minutes

Les fichiers partagés se dégradent comme le code, en silence. Une fois par mois, l'équipe passe le registre en revue :

- **Ce qui ne sert plus** : une skill que personne n'appelle, une règle que personne ne sait expliquer. Le bilan `/doctor` signale les extensions inutilisées.
- **Ce qui manque** : une erreur que l'agent a refaite deux fois appelle une ligne nouvelle, au bon niveau.
- **Ce qui se contredit** : deux fichiers qui disent l'inverse, ou une règle d'équipe qui heurte le socle.
- **Ce qui grossit** : un CLAUDE.md qui dépasse deux cents lignes se découpe en règles, chapitre M3.

La date de la revue s'inscrit dans la dernière colonne du registre. C'est elle qui dit, à un nouveau venu, si ce qu'il lit est encore vrai.

## Accueillir un nouveau

Au chapitre 27, une testeuse qui vient d'arriver comprend une story le matin même. Ce n'est pas un hasard : la story porte ses exigences, ses décisions, ce que fait le système existant, ses scénarios et son hors-périmètre. Tout ce qu'un nouveau doit savoir pour travailler est écrit, versionné, et lisible par lui comme par l'agent. L'accueil consiste surtout à lui montrer où.

### Ce qu'il reçoit sans rien faire

| De | Ce qui arrive | Chapitre |
| --- | --- | --- |
| La DSI, avec son poste | L'outil à la version de référence, la configuration Bedrock, les paramètres gérés, le CLAUDE.md géré, le plugin du socle, les serveurs MCP fournis | M1, M4, M7, M8 |
| Le dépôt, au premier clonage | Le CLAUDE.md et les règles, les skills, les sous-agents, les hooks, le wiki, la méthode | M3, M5, M6, M9, M11 |

### Ce qu'il fait le premier jour

1. **Cloner le dépôt et ouvrir l'outil.** À la première ouverture, l'outil demande s'il fait confiance au dossier : les autorisations, les hooks et les serveurs du projet ne s'appliquent qu'après. On lit `.claude/settings.json` avec le référent avant d'accepter.
2. **Se connecter à Jira**, par `/mcp`, avec sa propre identité.
3. **Vérifier que tout est là** : `/status` doit citer les paramètres gérés parmi les sources de réglages, `/memory` liste les CLAUDE.md chargés, `/plugin` montre le socle, `claude mcp list` les serveurs connectés.
4. **Lire trois documents** : le registre des propriétaires, l'index du wiki, et la story qu'il va prendre.
5. **Faire sa première story en binôme**, en mode plan, avec le référent ou un développeur de l'équipe. Il voit l'agent poser ses questions, relit son plan, regarde la prérelecture.

Ses préférences viendront après une semaine, dans `CLAUDE.local.md` et `.claude/settings.local.json`, jamais dans les fichiers partagés.

### Une skill d'accueil

Le déroulé se prête à une skill, que le nouveau lance lui-même :

```markdown
---
name: accueil
description: Présente l'outillage de l'équipe à une personne qui arrive. À lancer à la main.
disable-model-invocation: true
---

Une personne arrive dans l'équipe. En t'appuyant sur CLAUDE.md, le registre des
propriétaires et wiki/index.md :

1. Explique en une page comment l'équipe travaille avec toi : le circuit d'une
   story, ce que tu fais, ce que tu ne fais pas, qui relit quoi.
2. Liste les skills de l'équipe, chacune avec sa propriétaire et son usage.
3. Vérifie avec moi que les paramètres gérés, le socle et Jira sont en place.
4. Propose trois pages du wiki à lire en premier, d'après la story qu'on m'a confiée.

Ne modifie aucun fichier.
```

Elle ne remplace pas le binôme ; elle lui évite de passer la matinée à expliquer où sont les fichiers.

### Ce que le nouveau doit entendre d'un humain

Trois choses ne se délèguent pas à une skill, parce qu'elles engagent la confiance : on n'utilise que des données synthétiques ; quand l'agent rencontre un secret, on s'arrête et on prévient ; et l'on ne fusionne jamais ce qu'on n'a pas relu soi-même. Le socle les impose techniquement ; le référent les dit, le premier jour, à voix haute.

## De la personne au socle

Une skill naît presque toujours sur le poste de quelqu'un, pour régler un problème à lui. Certaines restent là. D'autres servent à un collègue, puis à l'équipe, puis à une équipe voisine. Le chemin est toujours le même, et chaque marche a sa porte.

> *Schéma non reproduit dans cette version Markdown : les quatre niveaux de diffusion · chacun a sa porte.*

### Les portes

| Pour passer | Il faut | Le geste technique | Chapitre |
| --- | --- | --- | --- |
| De personnelle à d'équipe | Qu'une deuxième personne s'en serve ; qu'une propriétaire l'accepte ; qu'elle ait été relue par celui qui sait | Déplacer le dossier dans `.claude/skills/`, par demande de fusion | M5 |
| D'équipe au catalogue | Qu'une autre équipe en ait besoin ; qu'elle ne dépende plus d'un détail propre à l'équipe d'origine ; qu'elle ait des évaluations | L'empaqueter dans un plugin, l'inscrire au catalogue interne | M8 |
| Du catalogue au socle | Qu'elle protège tout le monde ; que la commission sécurité l'accepte ; que le socle tienne toujours en deux pages | L'ajouter au plugin du socle, activé d'office par les paramètres gérés | M8 |

La deuxième porte est celle qu'on oublie. Une skill d'équipe parle souvent du glossaire, des dossiers, des personnes de l'équipe ; avant de la proposer à d'autres, on retire ces détails ou on les transforme en paramètres.

### Ne pas copier

Le réflexe naturel, quand une équipe voisine veut la skill de préparation des relectures, est de copier le dossier dans son dépôt. Trois mois plus tard, il existe deux versions, chacune corrigée de son côté. Dès qu'une skill sert à deux équipes, elle passe par le catalogue : une seule source, une seule propriétaire, et des versions que chaque équipe reçoit.

### Descendre aussi

Le chemin se parcourt dans les deux sens. Une skill du catalogue que plus personne n'appelle se retire ; une règle du socle devenue inutile en sort, pour que le socle reste court. La revue mensuelle de l'équipe et la revue trimestrielle du catalogue sont les moments prévus pour cela.

### Ce qui ne monte pas

Tout ne gagne pas à être partagé. Une skill qui encode la façon de travailler d'une personne, ses raccourcis, ses habitudes de rédaction, reste personnelle. Une skill qui encode le savoir d'un domaine, la déclaration de sinistre ou la règle de franchise, monte jusqu'à l'équipe, rarement au-delà : d'autres équipes ont d'autres domaines. Ce qui monte jusqu'au catalogue, ce sont surtout les savoir-faire de métier de développement : préparer une relecture, écrire des scénarios, tenir un wiki.

## Plusieurs équipes, un prestataire, un train

À partir du chapitre 22, l'équipe n'est plus seule. Elle entre dans le train Indemnisation, avec ses dépendances envers d'autres équipes, et une équipe du prestataire Horizon s'apprête à travailler avec les mêmes outils. Partager entre équipes pose les mêmes questions qu'au sein d'une équipe, avec une difficulté de plus : personne n'a autorité sur tout.

### Ce qui se partage à l'échelle du train

| Objet | Où il vit | Qui en répond |
| --- | --- | --- |
| Le socle : verrous, consignes communes, contrôles | Paramètres gérés, CLAUDE.md géré, plugin du socle | La commission sécurité ; Mathilde et Julien |
| Les outils communs | Le catalogue interne | Leurs propriétaires, sous l'œil de la DSI |
| Le savoir sur les systèmes communs | Un wiki partagé, à part, pour le système des contrats | Son propriétaire, avec Gérard pour les pourquoi |
| Les conventions de chaque équipe | Le dépôt de chaque équipe | Chaque équipe |
| Les dépendances et le calendrier | Jira, par les liens entre tickets | Les Product Owners du train |

La troisième ligne naît d'une question concrète : le savoir que Gérard transmet sur le système des contrats sert à toutes les équipes qui y touchent. Le laisser dans le wiki d'une seule équipe obligerait les autres à le copier. Il gagne à vivre dans un dépôt à part, que chaque wiki d'équipe cite comme une source.

### Un dépôt partagé par plusieurs équipes

Quand plusieurs équipes travaillent dans le même dépôt, chacune garde ses conventions sans imposer les siennes aux autres : un CLAUDE.md par sous-dossier, au sens du chapitre M3, et des règles limitées à certains chemins par leur en-tête. Le CLAUDE.md racine ne contient que ce qui vaut pour tous, et chaque équipe est propriétaire de son sous-dossier dans le fichier des propriétaires.

### Un prestataire, les mêmes règles

Au chapitre 16, la directrice générale exige que l'équipe d'Horizon travaille sur le compte AWS de la maison, avec le même socle et les mêmes règles que le pilote. Concrètement :

- **Les mêmes postes ou les mêmes paramètres gérés**, et donc le même socle, la même configuration Bedrock, les mêmes interdictions.
- **Les mêmes circuits** : leurs skills passent par le même catalogue, leurs demandes de fusion par les mêmes relecteurs quand elles touchent le cœur de gestion.
- **Leurs sources dans le wiki**, comme au chapitre 17 : leur dossier de rétro-documentation entre comme une source, ingérée et confrontée aux autres.
- **Des accès à leur mesure** : les dépôts et les connecteurs auxquels ils ont besoin d'accéder, rien de plus, avec leurs propres identités.

### Ce qui ne se transmet pas par fichier

Au chapitre 22, on propose à Émilie un nouveau poste. Elle le refuse, et propose à la place de former les testeurs d'Horizon. Elle a raison sur un point que ce chapitre ne doit pas faire oublier : une skill transmet une procédure, pas un jugement. Écrire un scénario avant le code, explorer après, savoir quand une story est vraiment finie : cela s'apprend en travaillant à côté de quelqu'un.

Le dispositif qui en découle est simple. Chaque nouvelle équipe reçoit les fichiers par le socle et le catalogue, et une personne par métier, qui passe deux semaines avec elle. Une communauté de pratique réunit ensuite, une fois par mois, une personne de chaque équipe : les skills qui ont changé, les incidents et leurs leçons, les mesures. C'est là que se décide ce qui monte au catalogue, et ce qui en descend.

## Dans le roman

| Chapitre | Scène | Ce qu'elle illustre ici |
| --- | --- | --- |
| 16 — La sécurité au quotidien | L'équipe d'Horizon travaillera dès janvier sur le compte de la maison, avec le même socle ; elle le recevra en ouvrant l'outil. | Ce que fournit l'entreprise ; un prestataire, les mêmes règles. |
| 17 — Le savoir de Gérard | Horizon verse sa rétro-documentation dans le wiki, comme une source de plus. | Le savoir sur un système commun, partagé entre équipes. |
| 18 — Les rôles bougent | Sofiane empaquette les savoir-faire de l'équipe en skills ; Nadia trouve la sienne fausse, la corrige et en devient propriétaire. | Le propriétaire est celui qui sait ; le registre des propriétaires. |
| 22 — L'analyste qui pose les bonnes questions | La règle « pas de document sans propriétaire ni lecteur » ; Émilie refuse un poste et propose de former les testeurs d'Horizon. | La colonne *Lu par* ; ce qui ne se transmet pas par fichier. |
| 27 — Le sprint d'après | Une testeuse qui vient d'arriver comprend une story le matin même. | Un accueil qui repose sur ce qui est écrit et versionné. |

Pour aller plus loin : M3 (niveaux de CLAUDE.md), M4 (niveaux de paramètres), M5 (règles de vie d'une skill), M8 (catalogue et socle), M10 (fichier des propriétaires), M11 (wiki), M13 (communauté de pratique et rétrospectives).

## Sources

Consultées le 22 octobre 2026.

- [Explorer le dossier .claude](https://code.claude.com/docs/en/claude-directory) — ce qui se versionne, ce qui reste local, et les données que l'outil écrit sur le poste
- [Paramètres et ordre de priorité](https://code.claude.com/docs/en/settings)
- [Mémoire et fichiers CLAUDE.md](https://code.claude.com/docs/en/memory)
- [Sous-agents : mémoire persistante](https://code.claude.com/docs/en/sub-agents#enable-persistent-memory)
- [Gérer les plugins pour une organisation](https://code.claude.com/docs/en/plugins/org)
