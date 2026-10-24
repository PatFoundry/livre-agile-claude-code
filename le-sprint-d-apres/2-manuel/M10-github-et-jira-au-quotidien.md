# M10 — GitHub et Jira au quotidien

*Partie II — Le manuel de référence*

## Ce que couvre ce chapitre

L'agent écrit du code dans un dépôt ; l'équipe le pilote dans Jira ; la maison le livre par GitHub. Ce chapitre décrit le circuit qui relie les trois : les conventions qui permettent de retrouver d'où vient chaque ligne, les protections qui empêchent qu'une branche principale bouge sans relecture, la revue automatique et les contrôles de la chaîne d'intégration, et la façon dont Jira reste à jour sans que personne le recopie.

Le roman en montre la construction pas à pas. Au chapitre 8, quatre agents produisent en parallèle plus de branches que l'équipe ne sait en réunir. Au chapitre 9, quarante demandes de fusion attendent un seul relecteur. Au chapitre 25, une coordinatrice recopie chaque soir le dépôt dans Jira depuis trois semaines, et l'équipe pose une règle : une information, un seul endroit, partout ailleurs un lien. Au chapitre 27, une story passe de son ticket à la fusion en une journée, par un circuit que personne ne remarque plus.

> **Version de référence.** Claude Code 2.1.301, publiée le 15 octobre 2026, et l'action GitHub `anthropics/claude-code-action@v1`, avec la configuration Bedrock du chapitre M1. Le dépôt de la maison est sur une instance GitHub Enterprise Server interne, et les tickets dans Jira ; les différences avec github.com sont signalées.

Rien dans ce chapitre n'est propre aux agents : une bonne convention de branche ou une branche protégée servent tout autant aux humains. C'est précisément le point. Le circuit ne distingue pas qui a écrit le code ; il garantit que quelqu'un l'a relu.

## Le circuit d'une story

Au chapitre 27, une story de bris de glace passe en une journée de son ticket à la fusion : scénarios rouges puis verts, prérelecture, relecture humaine, tests exploratoires. Aucune étape n'est nouvelle. Ce qui a changé depuis le chapitre 8, c'est qu'elles s'enchaînent toujours dans le même ordre, et que chacune laisse une trace reliée aux autres par la clé du ticket.

> *Schéma non reproduit dans cette version Markdown : le circuit d'une story · la relecture humaine reste le passage obligé.*

| Étape | Qui | Ce qui la rend possible | Chapitre |
| --- | --- | --- | --- |
| Ticket Jira | L'agent le crée quand Nadia valide la story | Le connecteur Jira | M7 |
| Branche | Le développeur, ou l'agent | La convention de nommage | M10 |
| Code et commits | L'agent, en local | Le mode plan, la skill d'implémentation | M2, M9 |
| Demande de fusion | Le développeur | La convention de titre | M10 |
| Contrôles | La chaîne d'intégration | Les tests, les scénarios, les contrôles du socle | M10 |
| Prérelecture | Un agent qui n'a pas écrit le code | La skill de préparation des relectures | M5 |
| Relecture humaine | Les propriétaires des fichiers touchés | La branche protégée, le fichier des propriétaires | M10 |
| Exploration | La testeuse | Les scénarios d'acceptation et son jugement | — |
| Fusion | Le développeur, une fois tout vert | La branche protégée | M10 |
| Jira à jour | Personne | L'intégration entre GitHub et Jira | M10 |

### Retracer une ligne en quatre minutes

Au chapitre 16, la commission sécurité vérifie qu'on peut retracer l'origine d'une ligne de code en moins de quatre minutes. C'est le test qui dit si le circuit tient :

1. `git blame` donne le commit qui a écrit la ligne ;
2. le message du commit porte la clé du ticket, et dit si un agent y a contribué ;
3. la clé mène au ticket Jira, et au fichier de la story dans le dépôt ;
4. la story mène à sa spécification, et au nom de qui l'a approuvée ;
5. la demande de fusion dit qui a relu, et quels contrôles sont passés.

Le reste du chapitre installe chacun de ces maillons.

## Conventions de branches et de commits

Une convention n'a de valeur que si elle est suivie à chaque fois, par tout le monde. L'agent la suit mieux qu'un humain pressé, à condition qu'elle soit écrite là où il la lit, et vérifiée là où personne ne peut l'oublier.

### Les règles de l'équipe

| Objet | Convention | Exemple |
| --- | --- | --- |
| Branche | La clé du ticket, puis quelques mots | `SIN-57-photos-multiples` |
| Commit | La clé en tête de la première ligne, puis ce que fait le changement, à l'indicatif | `SIN-57 Limite à dix les photos d'une déclaration` |
| Corps du commit | Pourquoi, en quelques lignes ; le renvoi vers la spécification | `Spécification : _bmad-output/implementation-artifacts/spec-sin-57.md` |
| Demande de fusion | La clé et le titre de la story ; dans la description, les liens vers la story, la spécification et les scénarios, et l'étiquette de risque | `SIN-57 — Joindre plusieurs photos` |
| Découpage | Une story, une branche, une demande de fusion | — |

La clé en majuscules est ce qui permet à Jira de rattacher d'office la branche, les commits et la demande de fusion au ticket. Elle est aussi ce qui rend possible le test des quatre minutes.

### Les écrire là où l'agent les lit

Ces règles prennent trois lignes dans la rubrique *Façon de travailler* du CLAUDE.md (chapitre M3). Claude Code a aussi ses propres consignes de commit et de demande de fusion, intégrées. Si elles contredisent celles de l'équipe, l'agent risque de choisir au hasard : le paramètre `"includeGitInstructions": false` les retire, et ne laisse que celles du CLAUDE.md.

### Dire qui a écrit

Par défaut, l'outil signe ses commits d'une ligne `Co-Authored-By` et ses descriptions de demande de fusion d'une mention. L'équipe garde cette signature : c'est elle qui dit, au deuxième maillon du test des quatre minutes, qu'un agent a contribué. Le paramètre `attribution` permet d'en adapter le texte, jamais de la supprimer dans la configuration de référence :

```json
{
  "attribution": {
    "commit": "Co-Authored-By: Claude <noreply@anthropic.com>",
    "pr": "Préparé avec Claude Code, relu par une personne de l'équipe."
  }
}
```

### Les vérifier là où personne ne peut les oublier

Une consigne suffit à l'agent dans la plupart des cas. Pour que la règle tienne dans tous les cas, et pour les humains aussi, la chaîne d'intégration refuse une demande de fusion dont le titre ou un commit ne porte pas de clé valide. C'est un contrôle de quelques lignes, décrit avec les autres à la section sur la chaîne d'intégration.

### Une branche courte

Au chapitre 8, quatre agents ouvrent quatre branches en une matinée ; deux d'entre elles vivent assez longtemps pour diverger, et leur réunion fabrique deux champs pour une seule notion. La convention la plus utile n'est pas dans le nom : une branche vit le temps d'une story, rarement plus de deux jours, et se réunit à la branche principale dès qu'elle est relue.

## Protéger la branche principale

Les verrous du chapitre M4 agissent sur le poste : ils empêchent l'agent de toucher à certains fichiers. Ceux de cette section agissent sur le serveur : ils empêchent quiconque, humain ou automate, de faire entrer une modification dans la branche principale sans la relecture prévue. Les deux se complètent. Le premier évite l'erreur ; le second garantit qu'elle ne passe pas.

### Les règles de la branche principale

Sur GitHub Enterprise Server, une règle de protection de branche, ou un *ruleset*, s'applique à `main` :

| Règle | Effet |
| --- | --- |
| Demande de fusion obligatoire | Personne ne pousse directement sur la branche principale. |
| Une approbation au moins | Et l'auteur de la demande ne peut pas s'approuver lui-même. |
| Approbation des propriétaires des fichiers | Voir le fichier des propriétaires, ci-dessous. |
| Approbations annulées à chaque nouveau commit | Une relecture porte sur ce qui sera fusionné, pas sur une version antérieure. |
| Contrôles obligatoires | La fusion attend que la chaîne d'intégration soit verte. |
| Pas de poussée forcée, pas de suppression | L'historique ne se réécrit pas. |
| Aucune exception | Les administrateurs et les comptes d'automatisation sont soumis aux mêmes règles. |

La dernière ligne compte pour les agents. L'identité qu'utilise l'action GitHub de la section suivante peut commenter et pousser des commits sur une branche de travail ; elle ne doit ni approuver, ni contourner une règle. Aucun agent ne fusionne dans la branche principale.

### Le fichier des propriétaires

Le fichier `.github/CODEOWNERS` dit qui doit approuver une modification, selon les fichiers touchés. C'est la traduction côté serveur des règles du roman : les scénarios appartiennent au métier et à la recette, le socle à la sécurité, chaque skill à sa propriétaire.

```text
# .github/CODEOWNERS
*                                       @mutuelle/portail-sinistres
/src/test/resources/scenarios/          @mutuelle/metier-sinistres @mutuelle/recette
/CLAUDE.md                              @mutuelle/portail-sinistres @nbenali
/.claude/                               @mutuelle/portail-sinistres @mutuelle/securite
/.claude/skills/preparer-story/         @nbenali
/_bmad/custom/                          @mutuelle/portail-sinistres @mutuelle/securite
/.github/                               @mutuelle/securite
/src/main/resources/db/migration/       @mutuelle/dba
```

La dernière ligne qui correspond à un fichier l'emporte ; l'ordre va donc du plus général au plus précis. Avec la règle d'approbation des propriétaires, une demande de fusion qui touche un scénario attend l'accord du métier ou de la recette, quel que soit son auteur.

### Les deux verrous des scénarios

Au chapitre 10, les scénarios d'acceptation sont devenus inaccessibles en écriture pour l'agent, par une règle de permission. Cette section ajoute le second verrou : même si quelqu'un les modifie, à la main ou depuis un poste mal configuré, la modification n'entre pas sans Nadia ou Émilie. Le premier verrou protège la session ; le second protège le produit.

### Ce que GitHub ne fait pas

La limite de travail en cours du chapitre 9, six demandes en revue au plus, ne se règle pas dans GitHub. Elle vit dans la colonne *En revue* du tableau Jira, qui l'affiche en rouge quand elle est dépassée, et dans la discipline de l'équipe : quand la colonne est pleine, on relit avant de commencer quoi que ce soit.

## La revue automatique des demandes de fusion

Au chapitre 9, la préparation des relectures se lance à la main, depuis le poste d'un développeur. L'étape suivante consiste à la lancer d'office, à l'ouverture de chaque demande de fusion, pour que la fiche attende le relecteur au lieu que le relecteur l'attende. C'est le rôle de l'action GitHub `anthropics/claude-code-action`, qui exécute Claude Code dans la chaîne d'intégration.

### Ce qui s'applique à la configuration de référence

L'éditeur propose aussi un service de revue automatique géré, sans fichier de workflow ; il suppose une organisation claude.ai et une forge joignable depuis ses serveurs. Ni l'un ni l'autre ne correspond à la configuration de référence. Reste l'action GitHub, qui fonctionne avec GitHub Enterprise Server et avec Bedrock, à quatre conditions :

| Condition | Pourquoi |
| --- | --- |
| Des exécuteurs auto-hébergés, sur le réseau interne | Ils joignent le Git interne, le miroir des bibliothèques et Bedrock, et rien d'autre. |
| Une application GitHub propre à la maison | L'installation guidée ne vaut que pour github.com ; sur l'instance interne, on crée une application avec les seuls droits utiles. |
| Une fédération d'identité vers AWS | L'exécuteur échange son jeton OIDC contre des identifiants AWS temporaires, sans aucune clé stockée. Le rôle IAM n'accepte que ce dépôt et reprend la politique du chapitre M1. |
| Les paramètres gérés sur l'image des exécuteurs | Le socle s'applique dans la chaîne d'intégration comme sur les postes. |

### Le workflow

```yaml
# .github/workflows/prerelecture.yml
name: Prérelecture
on:
  pull_request:
    types: [opened, ready_for_review, synchronize]
concurrency:
  group: prerelecture-${{ github.event.pull_request.number }}
  cancel-in-progress: true
jobs:
  prerelecture:
    if: github.event.pull_request.draft == false
    runs-on: [self-hosted, linux, agents]
    timeout-minutes: 20
    permissions:
      contents: read
      pull-requests: write
      id-token: write
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0
      - id: app-token
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.APP_ID }}
          private-key: ${{ secrets.APP_PRIVATE_KEY }}
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.AWS_ROLE_TO_ASSUME }}
          aws-region: eu-west-3
      - uses: anthropics/claude-code-action@v1
        env:
          GH_HOST: git.mutuelle.intra
          GH_TOKEN: ${{ steps.app-token.outputs.token }}
        with:
          github_token: ${{ steps.app-token.outputs.token }}
          use_bedrock: "true"
          prompt: >-
            /prepare-relecture ${{ github.event.pull_request.number }}
            Publie la fiche en commentaire de la demande de fusion.
          claude_args: >-
            --model eu.anthropic.claude-sonnet-5-5
            --max-turns 30
            --allowedTools "Bash(gh pr view *),Bash(gh pr diff *),Bash(gh pr comment *)"
```

Les noms d'hôtes sont fictifs ; le fichier est à faire valider par l'équipe qui administre les exécuteurs.

| Ligne | Rôle |
| --- | --- |
| `types` et `if` | La prérelecture se lance à l'ouverture, au passage en relecture, et à chaque nouveau commit ; jamais sur un brouillon. |
| `concurrency` | Deux commits rapprochés ne lancent pas deux prérelectures : la première est annulée. |
| `timeout-minutes`, `--max-turns` | Bornent la durée et le coût d'une exécution. |
| `permissions` | Lire le code, commenter la demande de fusion, obtenir le jeton d'identité ; rien d'autre. |
| `prompt` | La skill de préparation des relectures du chapitre M5, qui produit la fiche d'une page. |
| `--allowedTools` | Les trois seules commandes autorisées sans demande : lire la demande, lire la différence, publier la fiche. |

### Ce que la prérelecture ne fait pas

Elle ne signe pas. L'application GitHub qu'elle utilise peut commenter, jamais approuver, et la branche protégée exige de toute façon l'approbation d'un propriétaire humain. C'est la phrase du chapitre 9, inscrite dans la configuration : l'agent prépare, il ne signe pas.

Elle lit aussi du contenu que n'importe qui peut écrire : la description de la demande de fusion, les commentaires, le code proposé. C'est exactement la situation du chapitre M7. La parade est la même : des outils réduits à la lecture et au commentaire, aucun accès au réseau au-delà des hôtes internes, et les paramètres gérés du socle sur l'exécuteur.

### Et sur le poste

Rien n'empêche un développeur de lancer la même relecture avant même d'ouvrir sa demande de fusion : `/code-review` sur sa branche, ou la skill de l'équipe. C'est souvent le meilleur moment, puisqu'il peut corriger avant que quiconque ait lu.

## Les contrôles de la chaîne d'intégration

La chaîne d'intégration est le seul endroit par où passe tout le code, quel qu'en soit l'auteur. C'est là que vivent les contrôles qui doivent arrêter aussi les humains : au chapitre 13, la ligne fautive la plus ancienne avait été écrite à la main, sans agent, et c'est un test de la chaîne qui l'a attrapée en quatre minutes.

### Les contrôles obligatoires

| Contrôle | Ce qu'il vérifie | D'où il vient |
| --- | --- | --- |
| Construction et tests | Le code compile, les tests unitaires passent | — |
| Scénarios d'acceptation | Les scénarios du métier passent tous | Chapitre 10 |
| Journaux sans données personnelles | Les journaux produits par les scénarios ne contiennent aucune des données synthétiques de test | Chapitre 13 |
| Détection de secrets | La différence ne contient ni clé, ni mot de passe, ni certificat | Chapitre 3 |
| Clé Jira | Le titre de la demande de fusion et chaque commit commencent par une clé | Ce chapitre |
| Spécification approuvée | Toute spécification ajoutée porte le nom de qui l'a approuvée | Chapitre M9 |
| Seuils de qualité | Couverture et analyse statique ne descendent pas sous le seuil | Chapitre M4 |

Tous sont déclarés comme contrôles obligatoires dans la règle de la branche principale : la fusion reste impossible tant que l'un d'eux est rouge.

### Un principe : un contrôle obligatoire est déterministe

La prérelecture de la section précédente n'est pas dans cette liste, et ce n'est pas un oubli. Un contrôle obligatoire doit donner la même réponse à la même demande de fusion ; un modèle ne le garantit pas. La prérelecture informe le relecteur ; elle ne bloque rien. Ce qui bloque est écrit en code, se relit, et se teste.

### Deux contrôles en quelques lignes

Les deux contrôles propres à ce manuel tiennent dans une étape du workflow :

```yaml
  conventions:
    runs-on: [self-hosted, linux]
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0
      - name: Clé Jira et spécification approuvée
        env:
          TITRE: ${{ github.event.pull_request.title }}
          BASE: ${{ github.event.pull_request.base.sha }}
        run: |
          echo "$TITRE" | grep -qE '^SIN-[0-9]+ ' \
            || { echo "Le titre ne commence pas par une clé Jira."; exit 1; }
          if git log --no-merges --format=%s "$BASE"..HEAD | grep -vqE '^SIN-[0-9]+ '; then
            echo "Un commit ne commence pas par une clé Jira."; exit 1
          fi
          for f in $(git diff --name-only --diff-filter=A "$BASE"...HEAD \
                     -- '_bmad-output/implementation-artifacts/spec-*.md'); do
            grep -qE '^Approuvé par : .+' "$f" \
              || { echo "$f : approbation manquante."; exit 1; }
          done
```

Le titre de la demande de fusion passe par une variable d'environnement, jamais directement dans le script : un titre est écrit par quelqu'un, et pourrait contenir des commandes.

### Quand l'agent tourne dans la chaîne

L'action GitHub exécute Claude Code en mode non interactif. Les chapitres précédents ont signalé ce que ce mode change, et c'est ici que cela compte :

| Ce qui change | Parade |
| --- | --- |
| Les hooks du dépôt s'exécutent sans demande d'approbation (M6) | Sur ses propres dépôts, c'est voulu ; pour un dépôt tiers, `--settings '{"disableAllHooks": true}'` |
| Les serveurs MCP du dépôt se connectent sans demande (M7) | `--strict-mcp-config`, avec la seule liste voulue |
| Personne n'est là pour répondre à une demande d'autorisation | `--allowedTools` limité au strict nécessaire ; tout le reste est refusé |
| L'exécution peut boucler | `--max-turns` et une durée maximale pour le job |

## Jira au quotidien

Au chapitre 25, l'équipe découvre trois listes de stories qui ne disent plus la même chose : les fichiers du dépôt, le tableau Jira construit au PI Planning, et le fichier de suivi de la méthode. Une coordinatrice recopie chaque soir le dépôt dans Jira depuis trois semaines. Une équipe voisine a bâti un mandat de six mois d'après Jira, alors que la sponsor avait décidé un an. Le bureau des projets veut tout dans Jira, le tech lead défend le dépôt, et tous deux ont raison.

### Une information, un seul endroit

La réunion qui suit remplit un tableau simple : qui écrit, et qui lit, chaque information. La règle qui en sort tient en une ligne : **une information, un seul endroit, partout ailleurs un lien.**

| Information | Où elle vit | Qui l'écrit | Ailleurs |
| --- | --- | --- | --- |
| Texte de la story, critères, décisions, hors-périmètre | Le dépôt | L'agent rédige, Nadia valide | Un lien depuis le ticket |
| Scénarios d'acceptation | Le dépôt | Le métier et la recette | Un lien depuis le ticket |
| Classement de risque | Le dépôt, dans la story | L'équipe, avec la sécurité | Une étiquette dans Jira, posée à la création du ticket |
| Priorité, itération, assignation | Jira | La Product Owner et l'équipe | L'agent la lit |
| Dépendances entre équipes | Jira, par des liens entre tickets | Les Product Owners du train | — |
| Statut | Jira | Personne : l'intégration le fait avancer | — |
| Code, relecture, contrôles | GitHub | Les développeurs et les relecteurs | Le panneau *Développement* du ticket |

Le contenu vit dans le dépôt, le pilotage dans Jira, et la passerelle entre les deux est automatique.

### La passerelle

1. **Création.** Quand Nadia valide une story dans le dépôt, l'agent crée le ticket par le connecteur Jira (chapitre M7), avec le titre, l'étiquette de risque et le lien vers le fichier. C'est la seule écriture qu'il fait dans Jira.
2. **Rattachement.** La clé dans la branche, les commits et le titre de la demande de fusion suffit : l'intégration entre GitHub Enterprise et Jira affiche tout dans le panneau *Développement* du ticket.
3. **Avancement.** Des règles d'automatisation de Jira, déclenchées par les événements de la forge, font passer le ticket en *En revue* à l'ouverture de la demande de fusion, et en *Terminé* à la fusion.
4. **Rien d'autre.** Le fichier de suivi de la méthode est supprimé (chapitre M9), et plus personne ne recopie.

### Ce que l'agent lit avant de commencer

Le connecteur sert surtout en lecture. Une consigne du CLAUDE.md, ou de la personnalisation de la développeuse BMAD, le formalise :

```text
Avant de commencer une story, lis son ticket Jira : priorité, itération,
dépendances. Si elle n'est pas dans l'itération en cours, ou si un ticket
dont elle dépend n'est pas terminé, arrête-toi et dis-le.
```

Au chapitre 22, c'est exactement ce que la laine rouge du PI Planning rend visible : la story du proche dépend de l'espace adhérent d'une autre équipe, et reste sur sa branche quoi que fasse l'agent. Une équipe augmentée ne va pas plus vite que ses dépendances ; l'agent, au moins, doit le savoir avant de coder.

## Mesurer le flux

Une fois le circuit en place, chaque story laisse dans GitHub et Jira une série d'horodatages : création du ticket, première branche, ouverture de la demande de fusion, première relecture, fusion. Ces traces suffisent à mesurer ce qui compte, sans formulaire de plus.

### Les mesures utiles

| Mesure | Calculée à partir de | Ce qu'elle dit | Dans le roman |
| --- | --- | --- | --- |
| Attente avant relecture | Ouverture de la demande de fusion, première relecture | Où se trouve le goulot | Chapitre 9 |
| Demandes en revue | État des demandes de fusion ouvertes | Si la limite de travail en cours tient | Chapitre 9 |
| Délai de bout en bout | Création du ticket, fusion | Ce que vit le métier qui attend | Chapitre 27 |
| Débit | Stories terminées par semaine | La base de toute prévision | Chapitres 26 et 27 |
| Anomalies après fusion | Tickets d'anomalie reliés à une story | Si la vitesse se paie plus tard | Chapitre 11 |
| Écarts de spécification | Étiquette posée quand la démonstration révèle un malentendu | Si les stories disent ce que le métier veut | Chapitre 27 |
| Travail du soir | Heure des commits | Si l'équipe tient le rythme sans y laisser ses soirées | Chapitre 11 |
| Coût par story | Télémétrie de l'outil | Ce que coûte une story livrée | Chapitre M14 |

### Faire calculer, puis figer le calcul

Au chapitre 11, Thomas obtient les vrais chiffres du sprint en dix minutes, en demandant à l'agent de les tirer de Jira et de GitHub. C'est le bon usage pour une première fois. Pour la suite, une précaution : un chiffre recalculé à chaque sprint par une conversation peut l'être un peu différemment chaque fois. On demande donc à l'agent d'écrire le script qui fait le calcul, on le relit, on le versionne, et c'est ce script qu'on relance ensuite. L'agent invente la mesure ; le script la reproduit.

```text
Écris un script qui calcule, pour les quatre dernières itérations, l'attente
médiane avant première relecture, le débit hebdomadaire et le délai de bout
en bout, à partir de Jira et de GitHub, en lecture seule. Range-le dans
outils/mesures/ avec un README qui explique chaque calcul.
```

### Prévoir avec une fourchette

Au chapitre 27, la sponsor ne présente plus au comité une date, mais une fourchette assortie de probabilités, calculée sur le débit réel. La méthode est simple : à partir du débit des semaines passées, on simule de nombreuses fois le nombre de semaines nécessaires pour terminer le reste du périmètre, puis on lit le résultat comme une distribution, par exemple « huit semaines à 50 %, onze à 85 % ». Le même script de mesure peut produire cette simulation, à partir des seules données de Jira.

Le chapitre 26 en tire la conséquence jusque dans son titre : la vélocité est morte. Quand une part du travail passe par des agents, les points d'effort disent de moins en moins le temps qu'il faudra. Le débit observé, lui, intègre tout, y compris la relecture, qui reste la vraie contrainte.

## Dans le roman

| Chapitre | Scène | Ce qu'elle illustre ici |
| --- | --- | --- |
| 8 — Quatre agents à la fois | Quatre agents ouvrent quatre branches ; deux vivent assez longtemps pour diverger. | Une story, une branche, courte, réunie dès qu'elle est relue. |
| 9 — Le goulot s'appelle Julien | Quarante demandes de fusion pour un relecteur ; la limite de six en revue ; la préparation des relectures par un agent qui ne signe pas. | La prérelecture dans la chaîne d'intégration ; la branche protégée qui exige un humain. |
| 13 — Mercredi noir | Une ligne fautive écrite à la main, sans agent, attrapée par la chaîne en quatre minutes. | Les contrôles obligatoires arrêtent aussi les humains. |
| 16 — La sécurité au quotidien | La commission vérifie qu'on retrace une ligne de code en moins de quatre minutes. | Les conventions qui relient chaque maillon par la clé du ticket. |
| 25 — Deux vérités | Trois listes divergentes, une coordinatrice qui recopie chaque soir ; la règle « une information, un seul endroit ». | Le contenu dans le dépôt, le pilotage dans Jira, une passerelle automatique. |
| 27 — Le sprint d'après | Une story passe de son ticket à la fusion en une journée ; la sponsor présente une fourchette calculée sur le débit réel. | Le circuit complet ; mesurer et prévoir à partir des traces. |

Pour aller plus loin : M4 (verrous sur le poste), M5 (la skill de préparation des relectures), M6 (hooks), M7 (connecteur Jira), M9 (spécifications BMAD), M13 (limiter le travail en cours), M14 (coût par story).

## Sources

Consultées le 21 octobre 2026.

- [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions)
- [GitHub Actions avec Amazon Bedrock et les autres fournisseurs](https://code.claude.com/docs/en/github-actions-cloud-providers)
- [Claude Code et GitHub Enterprise Server](https://code.claude.com/docs/en/github-enterprise-server)
- [Référence des paramètres : attribution, includeGitInstructions](https://code.claude.com/docs/en/settings-reference)
- [Action `anthropics/claude-code-action` : sécurité](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md)
- [GitHub : propriétaires du code (CODEOWNERS)](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [GitHub : sécuriser les déploiements avec OpenID Connect](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
