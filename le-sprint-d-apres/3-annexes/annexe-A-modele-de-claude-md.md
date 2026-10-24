# Annexe A — Modèle de CLAUDE.md

*Annexes*

## À quoi sert cette annexe

Le chapitre M3 montre le CLAUDE.md du portail sinistres tel qu'il est au chapitre 10 : une vingtaine de lignes. Au fil du roman et du manuel, il s'est enrichi : le wiki de Gérard, les scénarios verrouillés, les conventions de branche, le plan en cinq rubriques, la règle sur l'adresse du risque. Cette annexe en donne la version complète, telle qu'elle est à la fin de la phase 2, au chapitre 27, avec pour chaque rubrique la raison d'être et le chapitre d'où elle vient.

C'est un modèle, pas un fichier à copier tel quel. Il est écrit pour un projet précis, une mutuelle, un portail, un système ancien sur mainframe ; ce qui se transpose, c'est sa structure et sa discipline :

- **moins de deux cents lignes** : celui-ci en compte une centaine ;
- **chaque ligne vérifiable** : on peut dire, en lisant ce que l'agent a fait, s'il l'a suivie ;
- **chaque ligne justifiée par une erreur réelle**, ou par une obligation : rien de ce que l'agent fait déjà bien sans consigne ;
- **deux propriétaires nommés**, et une modification seulement par demande de fusion (chapitre M12).

Le fichier ne contient ni verrou ni secret. Ce qui doit tenir à coup sûr vit dans les paramètres et les hooks des chapitres M4 et M6 ; le CLAUDE.md dit à l'agent comment travailler, il ne garantit rien.

## Le fichier

À la racine du dépôt du portail, versionné :

```markdown
# Portail sinistres — consignes pour l'agent

Portail de déclaration de sinistre habitation. Vision : @docs/vision.md
Propriétaires : Julien (technique), Nadia Benali (vocabulaire et principes métier).
Toute modification de ce fichier passe par une demande de fusion.

## Vocabulaire métier (validé par Nadia Benali)
- Déclarant : remplit la déclaration ; pas forcément l'assuré.
- Assuré : personne couverte ; pas forcément le souscripteur.
- Adresse du risque : adresse du bien assuré. À ne jamais confondre avec
  l'adresse de correspondance.
- Avenant : modification du contrat, avec une date d'effet.
- Franchise, plafond : jamais codés en dur, toujours lus dans le contrat.
- Les autres notions : wiki/pages/notions/

## Principes métier
- Une déclaration n'est jamais rejetée automatiquement : le gestionnaire décide.
- On ne bloque jamais une déclaration ; on la complète.
- Tout préremplissage d'adresse utilise l'adresse du risque.

## Données
- Uniquement les jeux synthétiques de tests/donnees/. Aucune donnée réelle
  d'assuré, y compris en recette.
- Aucune donnée personnelle dans les journaux : l'identifiant technique du
  dossier seulement.
- Si tu rencontres un secret (mot de passe, clé, certificat) : arrête-toi,
  ne le recopie nulle part, et préviens.

## Système des contrats
- Tout appel passe par adaptateur-contrats ; jamais d'accès direct.
- Avant de toucher un programme COBOL ou une règle de gestion, lis wiki/index.md.
- Le code dit ce qui se passe, jamais pourquoi. Un « pourquoi » absent du wiki
  est une question pour Gérard, pas une hypothèse.

## Façon de travailler : le plan
- Toute story commence en mode plan. Aucun fichier n'est modifié avant que le
  plan soit approuvé.
- Avant de proposer un plan, liste ce que la story ne dit pas et que le code ne
  permet pas de trancher. N'invente jamais une règle de gestion : pose la
  question, en nommant qui peut répondre.
- Le plan suit toujours ces cinq rubriques, dans cet ordre :
  1. Ce que je n'ai pas compris : ce qui reste à confirmer, et auprès de qui.
  2. Fichiers touchés : chaque fichier, et pourquoi là.
  3. Démarche : l'ordre des étapes et les choix faits.
  4. Vérification : les scénarios qui doivent passer, les tests ajoutés.
  5. Hors périmètre : ce que je ne toucherai pas.
- Une rubrique sans objet s'écrit « rien à signaler » ; elle ne disparaît pas.
- Pendant l'implémentation, signale tout écart au plan approuvé avant de le faire.
- Exception : une modification qui se décrit en une phrase (coquille, libellé,
  renommage) se fait sans plan.

## Tests
- Les scénarios de src/test/resources/scenarios/ sont écrits par le métier et
  la recette. Ne les modifie jamais.
- Lance d'abord les scénarios de la story : ils doivent échouer. Implémente
  ensuite jusqu'à ce qu'ils passent.
- Termine en montrant la sortie des scénarios et des tests, pas un résumé.
- Commandes du projet : @docs/commandes.md

## Branches, commits, demandes de fusion
- Une story = une branche = une demande de fusion.
- Branche : la clé Jira puis quelques mots, par exemple SIN-57-photos-multiples.
- Commit : la clé Jira en tête de la première ligne, puis ce que fait le
  changement, à l'indicatif. Le corps dit pourquoi et renvoie vers la spécification.
- Demande de fusion : la clé et le titre de la story ; dans la description, les
  liens vers la story, la spécification et les scénarios, et l'étiquette de risque.
- Ne pousse jamais sur main. Ne fusionne jamais.

## Jira
- Avant de commencer une story, lis son ticket : priorité, itération,
  dépendances. Si elle n'est pas dans l'itération en cours, ou si une
  dépendance n'est pas terminée, arrête-toi et dis-le.
- Tu ne crées un ticket que lorsque Nadia a validé la story. Tu ne changes
  jamais un statut.

## Compaction
- Quand tu compactes, garde la clé de la story, la liste des fichiers modifiés,
  les commandes de test et les questions ouvertes.

## Ne jamais
- Inventer une règle de gestion. Poser la question.
- Contourner une interdiction ou un contrôle. Si une action est refusée,
  explique pourquoi tu en avais besoin, et attends.
- Modifier ce fichier, .claude/, .github/ ou wiki/CLAUDE.md sans qu'on te le demande.
```

## Pourquoi chaque rubrique

Chaque rubrique répond à une erreur que l'agent a faite, ou aurait faite, dans le roman. C'est ce qui lui donne sa place : une ligne qu'on ne sait pas justifier est une ligne à retirer.

| Rubrique | Ce qu'elle évite | D'où elle vient |
| --- | --- | --- |
| En-tête : vision, propriétaires | Un fichier qui dérive sans que personne en réponde | M12 ; chapitres 18 et 22 |
| Vocabulaire métier | Un code qui confond le déclarant et l'assuré, ou qui code une franchise en dur | Le premier CLAUDE.md du chapitre M3, validé par Nadia |
| Adresse du risque | Un préremplissage avec l'adresse de correspondance | Chapitre 24, la première anomalie de production |
| Principes métier | Un rejet automatique, une déclaration bloquée par une validation trop stricte | M3 |
| Données | Des données réelles dans un test ou un journal ; un secret recopié | Chapitres 3 et 13 ; M4 et M6 pour les verrous |
| Système des contrats | Un sens deviné dans un programme ancien | Chapitre 17 ; M11 |
| Le plan | Une hypothèse découverte en recette | M13 |
| Tests | Des tests verts et des anomalies en recette | Chapitre 10 ; M13 |
| Branches, commits, demandes de fusion | Des branches qui divergent ; une ligne impossible à retracer | Chapitres 8, 9 et 16 ; M10 |
| Jira | Une story commencée hors itération, ou bloquée par une dépendance ; un statut modifié à la main | Chapitres 22 et 25 ; M10 |
| Compaction | Une session qui oublie la story en cours après un résumé automatique | M13 |
| Ne jamais | Les trois erreurs qui coûtent le plus cher | M3, M4 |

### Trois choix d'écriture

**Des phrases courtes, à l'impératif ou à l'indicatif.** « Tout appel passe par adaptateur-contrats » se vérifie ; « il est préférable de passer par l'adaptateur » ne se vérifie pas.

**Le pourquoi seulement quand il change la décision.** La ligne sur l'adresse du risque dit pourquoi elle existe, parce que l'agent rencontrera d'autres adresses et doit comprendre laquelle compte. La ligne sur les commits n'explique rien : la convention suffit.

**Des renvois plutôt que des copies.** Les commandes sont dans `docs/commandes.md`, importé par `@` ; les notions détaillées dans le wiki. Le CLAUDE.md reste court, et chaque information n'a qu'un seul endroit, la règle du chapitre 25.

## Ce qui n'y figure pas, et où le mettre

Un CLAUDE.md qui grossit est presque toujours un CLAUDE.md qui accueille ce qui devrait vivre ailleurs. Le tableau suivant dit où va chaque chose.

| Ce qu'on voudrait écrire | Où le mettre | Pourquoi | Chapitre |
| --- | --- | --- | --- |
| « Ne lis jamais les fichiers `.env` » | Une règle `deny` dans les paramètres | Une consigne peut être ignorée ; une interdiction, non | M4 |
| « Ne pousse jamais sur main » | Aussi une branche protégée | La ligne du CLAUDE.md guide l'agent ; la branche protégée arrête tout le monde | M10 |
| « Formate chaque fichier modifié », « aucune donnée personnelle dans les journaux » | Un hook | Ce qui doit se produire à chaque fois, sans exception | M6 |
| La façon de préparer une story ou une relecture | Une skill | Une procédure longue ne se charge que quand on s'en sert | M5 |
| Les conventions des scénarios, des migrations de base | Une règle de `.claude/rules/` limitée à ces chemins | Elle ne se charge que quand l'agent touche ces fichiers | M3 |
| Le savoir sur le système ancien, les décisions d'architecture | Le wiki | Trop volumineux, et il a ses propres propriétaires | M11 |
| Les consignes propres à la méthode BMAD | Les personnalisations de `_bmad/custom/` | Elles suivent les agents de la méthode, et survivent aux mises à jour | M9 |
| Ce qui vaut pour toute la maison | Le CLAUDE.md géré par la DSI | Une seule source pour toutes les équipes | M3, M8 |
| Ses préférences de travail | `CLAUDE.local.md` ou `~/.claude/CLAUDE.md` | Elles ne regardent pas l'équipe | M3, M12 |
| La liste des commandes du projet | `docs/commandes.md`, importé par `@` | Elle sert aussi aux humains, et change souvent | M3 |

Un réglage accompagne ce fichier : `"includeGitInstructions": false` dans `.claude/settings.json`. Il retire les consignes de commit intégrées à l'outil, pour que seules celles de la rubrique *Branches, commits, demandes de fusion* s'appliquent (chapitre M10).

## Les fichiers compagnons

Le CLAUDE.md principal ne travaille pas seul. Quatre fichiers l'accompagnent dans le dépôt du portail ; les trois premiers sont versionnés, le dernier ne l'est pas.

### Une règle pour les scénarios

Dans `.claude/rules/scenarios.md`, chargée seulement quand l'agent touche aux scénarios :

```markdown
---
paths:
  - "src/test/resources/scenarios/**"
---

# Scénarios d'acceptation
- Ces fichiers appartiennent au métier et à la recette. Tu peux les lire,
  jamais les modifier.
- Un scénario qui te semble faux se signale dans le plan, rubrique
  « Ce que je n'ai pas compris ».
- Leurs données viennent de tests/donnees/, jamais d'une base.
```

La règle explique ; l'interdiction d'écriture des paramètres (M4) et le fichier des propriétaires (M10) garantissent.

### Une règle pour les migrations de base

Dans `.claude/rules/migrations.md` :

```markdown
---
paths:
  - "src/main/resources/db/migration/**"
---

# Migrations de base
- Une migration fusionnée ne se modifie jamais : on en ajoute une nouvelle.
- Nommage : V<numéro>__<description>.sql, numéro suivant le dernier existant.
- Toute migration est relue par l'équipe base de données.
```

Le hook du chapitre M6 bloque la modification d'une migration existante ; la règle évite que l'agent essaie.

### Le schéma du wiki

Dans `wiki/CLAUDE.md`, chargé quand l'agent travaille dans le wiki (chapitre M11) :

```markdown
# Wiki du portail — schéma
- Structure : sources/ (jamais modifiées), pages/ (notions, regles, programmes,
  decisions, resumes), index.md, journal.md, questions.md.
- Chaque page commence par son en-tête : titre, type, statut (brouillon, relu
  ou contesté), relu-par, sources.
- Chaque affirmation cite sa source : programme et lignes, document et page,
  entretien et séance.
- Le code dit ce qui se passe, jamais pourquoi. Écris « Pourquoi : à confirmer »
  et ajoute la question à questions.md, avec le nom de qui peut répondre.
- Une contradiction : les deux pages passent en « contesté » et se renvoient
  l'une à l'autre. Tu ne tranches pas.
- Ingestion : une source à la fois ; présente ce qu'elle apprend avant d'écrire ;
  mets à jour l'index et le journal.
- Journal : chaque entrée commence par « ## [date] opération | titre ».
- Décisions : le champ decide-par est rempli par une personne, jamais par toi.
```

### Les préférences de chacun

`CLAUDE.local.md`, à la racine, exclu de Git par le `.gitignore` du chapitre M12. Par exemple, celui de Sofiane :

```markdown
# Préférences de Sofiane — non versionné
- Explique en deux phrases chaque choix de conception que tu fais.
- Propose-moi la commande de test avant de la lancer.
```

Une préférence qui s'avère utile à tous ne reste pas là : elle monte dans le CLAUDE.md partagé, par une demande de fusion.

## L'adapter et le vérifier

### L'adapter à son projet

1. **Partir de son propre dépôt**, pas de ce modèle : `/init` produit une première version à partir du code (chapitre M3). On y reporte ensuite la structure de ce modèle, rubrique par rubrique.
2. **Écrire le vocabulaire avec la Product Owner.** C'est la rubrique que l'agent ne peut pas deviner, et celle dont les erreurs coûtent le plus cher.
3. **Ne garder que les rubriques qui servent.** Pas de système ancien ? La rubrique disparaît. Pas de Jira ? On la remplace par l'outil de l'équipe.
4. **Justifier chaque ligne** par une erreur constatée ou une obligation. Pour chacune, la question de la documentation de l'éditeur : l'agent ferait-il une erreur si on la retirait ? Si non, on la retire.
5. **Nommer deux propriétaires**, l'un pour la technique, l'autre pour le métier, et les inscrire dans le fichier des propriétaires (chapitre M10).

### Le vérifier

Un CLAUDE.md se teste comme du code : en observant si le comportement change.

| Essai | Consigne | Comportement attendu |
| --- | --- | --- |
| Chargement | `/memory`, puis `/context` | Le fichier, ses imports et ses règles sont listés ; la part du contexte reste modeste |
| Le plan | « Prépare SIN-57 » | Le mode plan, les cinq rubriques, des questions ouvertes nommant qui peut répondre |
| Une règle par chemin | « Ajoute une colonne en modifiant la migration V12 » | L'agent refuse de modifier une migration fusionnée et en propose une nouvelle |
| L'exception | « Corrige la coquille du libellé *Déclarant* » | La correction directe, sans plan |
| Les données | « Prends un vrai dossier pour tester » | Un refus, et la proposition d'un jeu synthétique |

On relance ces essais après chaque modification importante du fichier, et à chaque montée de version de l'outil. Le bilan `/doctor` propose aussi de retirer ce que l'agent peut déduire du code.

### Les signes d'un fichier trop long

L'agent ignore une règle pourtant écrite ; il pose une question dont la réponse est dans le fichier ; deux rubriques se contredisent. Dans les trois cas, le remède est le même : couper, déplacer vers une règle, une skill ou le wiki, et ne garder que ce qui change le comportement. C'est l'objet de la revue mensuelle du chapitre M12.

## Renvois

- M3 — CLAUDE.md et la mémoire : niveaux, imports, règles par chemin, `/init`
- M4 — Paramètres et permissions : ce qui doit être interdit plutôt que conseillé
- M5 et M6 — Skills, sous-agents et hooks : ce qui sort du CLAUDE.md
- M9 — BMAD : les personnalisations de la méthode
- M10 — GitHub et Jira : conventions et fichier des propriétaires
- M11 — Le wiki : son schéma
- M12 — Partager en équipe : propriétaires et revue mensuelle
- M13 — Bonnes pratiques : le plan, les tests d'abord, la compaction

Sources, consultées le 23 octobre 2026 : [Claude Code, la mémoire et les fichiers CLAUDE.md](https://code.claude.com/docs/en/memory) ; [Claude Code, bonnes pratiques](https://code.claude.com/docs/en/best-practices).
