# M11 — Le wiki d'équipe à la Karpathy

*Partie II — Le manuel de référence*

## Ce que couvre ce chapitre

Le CLAUDE.md dit à l'agent comment travailler ; il ne peut pas contenir tout ce que l'équipe sait. Le savoir d'un système ancien, les raisons d'une règle de gestion, les décisions d'architecture et leurs alternatives écartées vivent ailleurs : dans des documents épars, des programmes, et surtout dans la tête de quelques personnes. Ce chapitre décrit une façon de les rassembler, que l'agent tient à jour lui-même : le wiki d'équipe, sur le modèle qu'Andrej Karpathy a publié en avril 2026 sous le nom de *LLM Wiki*.

Le roman en montre les deux usages. Au chapitre 17, l'absence d'un seul jour de Gérard, le dernier expert COBOL, coûte une journée à la story la plus critique du sprint : l'agent a lu le code et deviné le sens d'une lettre, plausiblement et à tort. L'équipe décide de traiter la dette de connaissance tout de suite, une heure par jour, en construisant un wiki. Au chapitre 24, l'agent architecte lit ce wiki avant même les exigences, et chaque décision d'architecture y entre sous une forme fixe.

Rien ici n'est propre à un outil : un wiki de ce type n'est qu'un dossier de fichiers Markdown dans le dépôt, des conventions écrites, et un agent qui les applique. Claude Code suffit ; aucune base de données, aucun moteur de recherche n'est nécessaire à l'échelle d'une équipe.

> **Ce que le chapitre n'est pas.** Ni une recette de recherche sémantique sur des documents, ni un remplacement de la documentation officielle de la maison. Le wiki est l'outil de travail de l'équipe et de ses agents ; il cite les sources officielles, il ne les remplace pas.

## Le principe

La façon la plus répandue de faire travailler un modèle sur des documents consiste à lui donner, à chaque question, les passages qui semblent pertinents. Il refait alors tout le travail de synthèse à chaque fois, et rien ne s'accumule. Karpathy propose l'inverse : l'agent lit chaque source une seule fois, en extrait ce qui compte, et l'intègre à un ensemble de pages qu'il tient à jour. Les liens entre pages sont déjà là, les contradictions déjà signalées. Le wiki s'enrichit à chaque source ajoutée et à chaque question posée.

> *Schéma non reproduit dans cette version Markdown : trois couches, trois opérations · d'après le LLM Wiki d'Andrej Karpathy.*

### Trois couches

| Couche | Ce que c'est | Qui l'écrit |
| --- | --- | --- |
| Les sources brutes | Les documents d'origine : programmes, spécifications anciennes, comptes rendus, entretiens transcrits. Ils ne sont jamais modifiés ; ils sont la référence. | Ceux qui les ont produits |
| Le wiki | Des pages Markdown courtes et reliées : une par notion, une par règle, une par décision, une par source. | L'agent, relu par les humains |
| Le schéma | Un fichier de consignes qui dit comment le wiki est organisé, quel format ont les pages, et ce que l'agent fait à chaque opération. | L'équipe et l'agent, ensemble, au fil de l'usage |

### Trois opérations

- **Ingérer** : une nouvelle source entre ; l'agent la résume, met à jour toutes les pages qu'elle touche, et note ce qu'elle contredit.
- **Interroger** : on pose une question ; l'agent répond à partir des pages, en citant ses sources. Une réponse utile devient une page.
- **Contrôler la cohérence** : régulièrement, l'agent cherche les contradictions, les affirmations périmées, les pages isolées, les notions sans page.

### Pourquoi cela tient

Les wikis d'équipe meurent rarement faute de contenu. Ils meurent parce que les tenir à jour coûte plus cher que ce qu'ils rapportent : mettre à jour les renvois, réviser les résumés, noter ce qu'une nouvelle information remet en cause. C'est précisément le travail qu'un agent fait sans se lasser, en touchant quinze fichiers d'un coup. Le partage des rôles suit : aux humains de choisir les sources, de poser les bonnes questions et de juger ce que tout cela signifie ; à l'agent, la tenue des registres.

### Ce que change le passage à l'équipe

Le modèle de Karpathy est d'abord personnel : il lit le wiki, l'agent l'écrit. Dans une équipe, trois règles s'ajoutent, toutes tirées du chapitre 17 :

1. **Chaque affirmation cite sa source** : un programme et sa ligne, un document et sa page, un entretien et sa date.
2. **Un humain relit tout ce qui explique un pourquoi.** Gérard relit chaque page qui donne la raison d'une règle ; l'agent peut décrire ce que fait le code, pas décider pourquoi.
3. **Le wiki vit dans le dépôt**, et chaque modification passe par une demande de fusion, comme le code.

## Organiser le dépôt du wiki

Le wiki est un dossier du dépôt de l'équipe. Il se relit dans GitHub, se modifie par demande de fusion, et son historique est celui de Git.

```text
wiki/
├── CLAUDE.md          le schéma : conventions et opérations
├── index.md           le catalogue : une ligne par page
├── journal.md         l'historique : une entrée par opération
├── sources/           les sources brutes, jamais modifiées
│   ├── documents/     spécifications anciennes, notes, dossiers reçus
│   └── entretiens/    transcriptions relues des séances avec l'expert
└── pages/
    ├── notions/       contrat, avenant, adresse du risque…
    ├── regles/        une règle de gestion par page
    ├── programmes/    une page par programme COBOL
    ├── decisions/     une décision d'architecture par page
    └── resumes/       une page de résumé par source ingérée
```

Les programmes COBOL ne sont pas copiés : ils restent dans leur propre dépôt, ouvert à l'agent en lecture seule par une règle de permission (chapitre M4). La page d'un programme cite son nom et ses lignes.

### Le schéma

Le fichier `wiki/CLAUDE.md` est un CLAUDE.md de sous-dossier au sens du chapitre M3 : l'agent le charge dès qu'il travaille dans le wiki, et seulement là. Il décrit les types de pages, leur format, et le déroulé de chaque opération. Le CLAUDE.md principal du projet n'en garde qu'une ligne : « Avant de toucher un programme COBOL ou une règle de gestion, lis `wiki/index.md`. »

### Le format d'une page

Une page est courte, une notion par page, et commence par un en-tête qui permet à l'agent comme aux humains de savoir ce qu'elle vaut :

```markdown
---
titre: Indicateur de statut du contrat (zone CT-STAT)
type: regle
statut: relu            # brouillon, relu ou contesté
relu-par: Gérard
sources:
  - programme CTR010, lignes 212 à 240
  - entretien avec Gérard, séance 3
---

## Ce que fait le code
…

## Pourquoi
…  (rédigé d'après l'entretien, relu par Gérard)

## Exceptions connues
…

## Voir aussi
- [Avenant](../notions/avenant.md)
- [Programme CTR010](../programmes/ctr010.md)
```

L'exemple est fictif ; la structure est celle que le schéma impose. Les liens sont des liens Markdown relatifs, que GitHub affiche et que l'agent suit.

### L'index et le journal

Deux fichiers aident à s'y retrouver quand le wiki grandit. Ils n'ont pas le même rôle.

| Fichier | Organisé par | Contenu | Qui s'en sert |
| --- | --- | --- | --- |
| `index.md` | Type de page | Chaque page, son lien, une ligne de résumé, son statut | L'agent le lit en premier pour savoir quelles pages ouvrir |
| `journal.md` | Date | Une entrée par opération : ingestion, question, contrôle | L'équipe, pour savoir ce qui a changé ; l'agent, pour savoir ce qu'il a déjà fait |

Une astuce de Karpathy : commencer chaque entrée du journal par un préfixe constant, par exemple `## [date] ingestion | Programme CTR010`, pour qu'une simple commande `grep` retrouve les dernières opérations.

À l'échelle d'une équipe, une centaine de sources et quelques centaines de pages, l'index suffit à l'agent pour trouver ce qu'il cherche. Aucun moteur de recherche n'est nécessaire avant longtemps.

## Ingérer une source

Ingérer, c'est faire entrer une source dans le wiki. Une source à la fois, en restant présent : c'est ainsi que Karpathy procède, et c'est encore plus vrai pour une équipe, où chaque ingestion engage ce que d'autres liront ensuite.

### Le déroulé

1. **Lire le schéma, puis l'index**, pour savoir ce qui existe déjà.
2. **Lire la source en entier.**
3. **En parler avant d'écrire.** L'agent présente ce que la source apprend, les pages qu'elle touche, ce qu'elle contredit, et les questions qu'elle soulève. L'humain oriente : ce qui compte, ce qui est accessoire.
4. **Écrire**, une fois l'accord donné : une page de résumé de la source, la mise à jour de chaque page touchée, et les pages qui manquent. Une seule source touche souvent dix à quinze pages.
5. **Tenir les registres** : l'index, le journal, et la liste des questions ouvertes.
6. **Proposer** le tout dans une demande de fusion, que relisent les propriétaires.

### La règle qui aurait évité le chapitre 17

L'agent du chapitre 17 a lu le code, trouvé une lettre dans une zone, et en a déduit un sens plausible. Il s'est trompé, et la story a perdu une journée. La règle qui en découle est la plus importante du schéma : **le code dit ce qui se passe, jamais pourquoi.** Quand une page a besoin d'un pourquoi que les sources ne donnent pas, l'agent écrit « Pourquoi : à confirmer » et ajoute la question à `wiki/questions.md`, avec le nom de qui peut répondre.

Ce fichier devient l'ordre du jour des séances avec l'expert. Au chapitre 17, Gérard y consacre une heure par jour : l'agent prépare les questions que le code laisse ouvertes, Gérard répond, la transcription relue devient une source, et son ingestion remplace les « à confirmer » par des réponses signées.

### Une skill pour ne rien oublier

Le déroulé est assez stable pour devenir une skill, au sens du chapitre M5 :

```markdown
---
name: ingerer-source
description: Ingère une source dans le wiki d'équipe selon wiki/CLAUDE.md. À lancer à la main.
disable-model-invocation: true
argument-hint: [chemin de la source ou nom du programme]
---

Ingère $ARGUMENTS dans le wiki.

1. Lis wiki/CLAUDE.md, puis wiki/index.md.
2. Lis la source en entier. Avant d'écrire, présente-moi : ce qu'elle apprend,
   les pages qu'elle touche, ce qu'elle contredit, les questions qu'elle soulève.
3. Après mon accord : écris la page de résumé, mets à jour les pages touchées,
   crée celles qui manquent.
4. Chaque affirmation cite sa source. N'écris aucun « pourquoi » déduit du code :
   écris « Pourquoi : à confirmer » et ajoute la question à wiki/questions.md.
5. Signale chaque contradiction dans les deux pages concernées, statut « contesté ».
6. Mets à jour l'index et ajoute une entrée au journal.
```

### Ce qui n'entre pas

Le wiki est une source de contexte pour tous les agents de l'équipe ; ce qui y entre finit dans leurs conversations. Il ne reçoit donc ni extrait de base de données, ni capture d'écran d'un dossier réel, ni secret : les règles du chapitre 13 s'appliquent aux sources comme au code. Un exemple a besoin d'un contrat ? On le prend dans les jeux de données synthétiques.

Au chapitre 17, le programme d'Horizon demande à verser son propre dossier de rétro-documentation dans le wiki. La réponse est la bonne : il entre comme une source de plus, ingérée, citée, et confrontée aux autres. Il n'écrase rien.

## Interroger le wiki

Une question au wiki suit toujours le même chemin : l'agent lit l'index, ouvre les pages utiles, répond en citant ce qu'il a lu. Il ne va aux sources brutes que pour vérifier un point précis.

### Qui pose les questions

| Qui | Exemple | Ce que la réponse change |
| --- | --- | --- |
| La Product Owner | « Un avenant qui change l'adresse du risque prend effet le jour du sinistre : quelle adresse vaut ? » | Un critère d'acceptation juste du premier coup |
| La testeuse | « Quels contrats font exception à la règle de franchise ? » | Des scénarios qui couvrent les cas réels |
| Le développeur, ou son agent | « Que fait CTR010 quand la zone CT-STAT est vide ? » | Un code qui reproduit le comportement attendu |
| L'agent architecte | Il lit tout le wiki avant les exigences | Une architecture qui part de ce qui existe |

### La forme d'une réponse

Le schéma impose une forme simple, qui distingue ce qui est établi de ce qui ne l'est pas :

```text
Réponse : …
Pages lues : regles/adresse-du-risque.md (relu), notions/avenant.md (relu)
Ce qui reste à confirmer : le cas des avenants rétroactifs (question 14, pour Gérard)
```

Une page au statut *brouillon* ou *contesté* se signale dans la réponse. Et quand le wiki ne sait pas, l'agent le dit et ajoute la question à la liste ; il ne comble pas le trou avec une hypothèse plausible.

### Garder les bonnes réponses

C'est l'idée la plus féconde de Karpathy : une bonne réponse ne doit pas disparaître dans l'historique d'une conversation. Une comparaison entre deux programmes, la liste des exceptions à une règle, l'explication d'un enchaînement : chacune devient une page, proposée par demande de fusion comme le reste. Les questions de l'équipe enrichissent ainsi le wiki autant que les sources.

### Brancher le wiki sur le reste du travail

Le wiki ne sert que s'il est lu au bon moment. Trois branchements suffisent :

- **Le CLAUDE.md du projet** renvoie vers l'index avant toute modification qui touche un programme ancien ou une règle de gestion.
- **La skill de préparation des stories** (chapitre M5) consulte les pages des règles concernées et cite leurs liens dans la story.
- **L'agent architecte de BMAD** reçoit l'index du wiki parmi ses consignes permanentes, par une personnalisation (chapitre M9). Au chapitre 24, c'est la décision de Julien : l'architecte lit le wiki avant les exigences.

### Ménager le contexte

Une question large peut amener l'agent à ouvrir trente pages. Pour qu'elles n'encombrent pas la conversation principale, on confie la recherche à un sous-agent en lecture seule, au sens du chapitre M5 : il lit, synthétise, et ne rend que la réponse et ses références.

## Contrôler la cohérence

Un wiki qui grandit se dégrade : des pages se contredisent, d'autres sont dépassées par une source plus récente, certaines ne sont reliées à rien. Le contrôle de cohérence est la troisième opération, celle qui garde le tout en état.

### Ce que l'on cherche

| Problème | Exemple | Qui le trouve |
| --- | --- | --- |
| Lien cassé | Une page renvoie vers une page renommée | Un script |
| Page orpheline | Aucune page ne renvoie vers elle | Un script |
| En-tête incomplet | Pas de source, pas de statut | Un script |
| Source introuvable | La page cite un programme ou une séance qui n'existe pas | Un script |
| Contradiction | Deux pages, ou deux sources, disent l'inverse | L'agent |
| Affirmation périmée | Une source récente a remplacé une ancienne règle | L'agent |
| Notion sans page | Un terme revient dans dix pages sans être défini | L'agent |
| « Pourquoi » non relu | Une explication rédigée par l'agent attend toujours l'expert | Un script, d'après le statut |

Le partage est celui du chapitre M10 : ce qui peut se vérifier par un programme se vérifie par un programme, à chaque demande de fusion qui touche le wiki ; le jugement est confié à l'agent, lors d'un contrôle périodique.

### Le contrôle périodique

Une fois par semaine, l'agent parcourt le wiki et rend un rapport, sans rien corriger lui-même :

```text
Contrôle la cohérence du wiki selon wiki/CLAUDE.md. Cherche les contradictions
entre pages et entre sources, les affirmations qu'une source plus récente
contredit, les notions sans page, les renvois manquants. Pour chaque point :
les pages concernées, les sources, et la personne qui peut trancher.
N'en corrige aucun. Ajoute une entrée au journal.
```

Le rapport est relu en équipe. Les corrections évidentes passent par une demande de fusion ; les autres deviennent des questions.

### La contradiction de 2011

Le premier contrôle du chapitre 17 fait apparaître ce que personne ne savait : deux programmes appliquent différemment la date d'effet d'un avenant, et ce depuis 2011. Ce n'est pas une erreur du wiki, c'est une découverte sur le système. La conduite à tenir suit :

1. Les deux pages passent au statut *contesté*, chacune renvoyant vers l'autre, avec les lignes de code en cause.
2. La question va à Gérard pour l'histoire, et au métier pour la règle : laquelle des deux applications est juste ?
3. La réponse devient une décision, avec son auteur et sa date, et la story qui corrigera l'un des programmes, si on le corrige.

L'agent n'a pas à choisir. Son travail était de la trouver, et il l'a trouvée là où quinze ans de lectures humaines ne l'avaient pas vue.

## Application au legacy : le savoir de Gérard

Dans beaucoup de maisons, le système central tient sur quelques personnes qui savent pourquoi il fait ce qu'il fait. Le jour où l'une d'elles est absente, l'agent lit le code et devine. Au chapitre 17, il devine une lettre, plausiblement et à tort, et la story la plus critique du sprint perd une journée. L'équipe inscrit alors au registre une dette de connaissance, et décide de la traiter sans attendre.

### La méthode en quatre temps

| Temps | Ce que fait l'agent | Ce que fait l'expert |
| --- | --- | --- |
| 1. Inventaire | Ingère les programmes et la documentation existante ; une page par programme, purement descriptive : entrées, sorties, zones, appels | Rien encore |
| 2. Questions | Liste tout ce que le code laisse ouvert, classé par urgence : d'abord les programmes que touchent les prochaines stories | Relit l'ordre de priorité |
| 3. Séances | Pose les questions une à une, demande des exemples, transcrit | Répond, une heure par jour, puis relit la transcription |
| 4. Ingestion | Remplace chaque « à confirmer » par la réponse, signée et datée | Relit chaque page qui explique un pourquoi |

L'ordre compte. L'agent arrive aux séances en ayant déjà lu tout ce que le code et les documents disent ; il ne fait perdre à l'expert aucune minute sur ce qui est écrit quelque part. C'est la même discipline que celle de l'analyste du chapitre 22, qui lit tout ce que la maison sait avant d'interroger les gestionnaires.

### Ce que le wiki ne contient pas encore

Au chapitre 24, une gestionnaire repère la première anomalie de production : le portail préremplit l'adresse de correspondance au lieu de l'adresse du risque. Gérard le savait depuis trente ans, sans l'avoir jamais écrit, et personne ne le lui avait demandé. L'architecture proposée le lundi reproduisait la même erreur.

La leçon est double. Un wiki ne contient que les réponses aux questions qu'on a posées ; le savoir tacite remonte par les incidents, et chaque incident de ce genre devient aussitôt une source, une page, et une question de plus. Et le wiki dit ce que l'équipe croit du système ; il faut autre chose pour savoir ce que le système fait.

### Les tests de caractérisation

Cette autre chose, Julien l'impose au retour : des tests de caractérisation. On choisit quarante contrats parmi les pires, ceux qui cumulent avenants, exceptions et historiques tordus, en version synthétique ; on enregistre, champ par champ, la réponse réelle du système ancien ; et le nouveau code doit donner la même. Ces tests en font sortir trois surprises, dont une exigence que personne n'avait imaginée.

|  | Le wiki | Les tests de caractérisation |
| --- | --- | --- |
| Ce qu'il dit | Ce que l'équipe croit, et pourquoi | Ce que le système fait réellement |
| Sa force | Les raisons, l'histoire, les exceptions expliquées | Aucune interprétation : des faits |
| Sa limite | Ne contient que ce qu'on a demandé | Ne dit jamais pourquoi |

Les deux se nourrissent : chaque surprise des tests devient une question pour l'expert, et chaque page du wiki suggère des contrats à ajouter aux tests.

### Mesurer la dette

La dette de connaissance se suit comme une autre : le nombre de « pourquoi » encore à confirmer, la part des pages relues par l'expert, le nombre de programmes que touchent les prochaines stories sans page relue. Quand ces chiffres baissent, l'absence d'un jour de Gérard redevient un simple jour d'absence.

## Les décisions, et qui tient le wiki

### Une décision par page

Au chapitre 24, l'agent architecte propose en une heure une architecture complète. Il y glisse une idée séduisante et courante : une copie nocturne du système des contrats. Julien la refuse, en écrivant pourquoi. À partir de là, chaque décision prend une forme fixe, rédigée par l'agent, sauf le nom de qui décide.

```markdown
---
titre: Pas de copie nocturne du système des contrats
type: decision
statut: acceptée        # proposée, acceptée ou remplacée
decide-par: Julien
---

## Contexte
Le portail a besoin des contrats et de leurs avenants à jour.

## Décision
Le portail interroge le système des contrats au moment de la déclaration.

## Alternatives écartées
- Copie nocturne : avenants vieux d'un jour au moment du sinistre ; données
  personnelles copiées une fois de plus ; échec d'un chantier comparable.

## Conséquences
…

## Sources
- [Avenant](../notions/avenant.md), [Adresse du risque](../regles/adresse-du-risque.md)
```

Trois règles accompagnent ce format :

- **L'agent rédige, une personne décide.** Le champ `decide-par` n'est rempli que par un humain, et la chaîne d'intégration refuse une décision acceptée qui ne le porte pas, comme pour les spécifications du chapitre M9.
- **On ne supprime pas une décision.** Une décision remplacée passe au statut *remplacée* et renvoie vers celle qui la remplace. L'histoire des raisons fait partie du savoir.
- **Les alternatives écartées comptent autant que la décision.** La prochaine fois qu'un agent sera tenté par une copie nocturne, il lira pourquoi elle a été refusée. C'est ce qui empêche une équipe de rejouer le même débat tous les six mois.

### Qui tient le wiki

| Rôle | Responsabilité | Dans le roman |
| --- | --- | --- |
| Le propriétaire du wiki | Le schéma, le contrôle hebdomadaire, la priorité des ingestions | Julien |
| L'expert du système ancien | Relit chaque page qui explique un pourquoi ; répond aux questions | Gérard |
| La Product Owner | Relit les pages de règles de gestion ; tranche quand deux règles s'opposent | Nadia |
| Celui qui décide | Signe chaque décision d'architecture | Julien, ou le comité d'architecture |
| Toute l'équipe | Propose des sources et des questions ; tout passe par une demande de fusion | — |

Le fichier des propriétaires du chapitre M10 traduit ce tableau : `wiki/pages/regles/` exige l'approbation de Nadia, `wiki/pages/decisions/` celle de Julien, `wiki/CLAUDE.md` celle du propriétaire du wiki.

### Quatre précautions

1. **Pas de données réelles, pas de secrets.** Le wiki est lu par tous les agents de l'équipe, et par ceux du prestataire quand il y contribue. Les règles du chapitre 13 s'y appliquent comme au code.
2. **Des pages courtes.** Une page de plus de deux écrans traite sans doute deux sujets ; le contrôle périodique le signale.
3. **Le schéma évolue.** Karpathy le dit : on le fait évoluer avec l'agent, au fil de l'usage. Chaque changement passe par une demande de fusion, et se note au journal.
4. **Le wiki ne remplace pas l'expert, il le prolonge.** Il garde ce que Gérard a dit, il ne sait pas ce qu'on ne lui a pas demandé. Tant que l'expert est là, les séances continuent.

## Dans le roman

| Chapitre | Scène | Ce qu'elle illustre ici |
| --- | --- | --- |
| 17 — Le savoir de Gérard | Un jour d'absence de Gérard coûte une journée : l'agent a deviné le sens d'une lettre. L'équipe traite la dette de connaissance tout de suite, une heure par jour. | Le code dit ce qui se passe, jamais pourquoi ; les questions ouvertes deviennent l'ordre du jour des séances. |
| 17 — Le savoir de Gérard | L'agent ingère les programmes et les documents, interroge Gérard, tient des pages courtes et reliées, chaque affirmation citant sa source ; Gérard relit tout ce qui explique un pourquoi. | Les trois couches et les trois opérations, adaptées à une équipe. |
| 17 — Le savoir de Gérard | Le premier contrôle révèle que deux programmes appliquent différemment la date d'effet d'un avenant depuis 2011 ; Horizon verse sa rétro-documentation comme une source de plus. | Contrôler la cohérence ; une source externe s'ingère, elle n'écrase rien. |
| 24 — L'architecte et le mainframe | L'architecte lit le wiki avant les exigences ; Julien refuse la copie nocturne en écrivant pourquoi ; chaque décision prend une forme fixe. | Les décisions d'architecture dans le wiki, signées par une personne. |
| 24 — L'architecte et le mainframe | L'adresse de correspondance préremplie au lieu de l'adresse du risque ; puis quarante contrats en tests de caractérisation, et trois surprises. | Ce que le wiki ne contient pas encore ; ce que seuls les tests disent. |

Pour aller plus loin : M3 (CLAUDE.md de sous-dossier), M5 (skills et sous-agents en lecture seule), M9 (personnaliser l'architecte BMAD), M10 (fichier des propriétaires, contrôles déterministes), M13 (bonnes pratiques : le registre des dettes de connaissance).

## Sources

Consultées le 21 octobre 2026.

- [Andrej Karpathy, *LLM Wiki*, 4 avril 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — le texte d'origine du modèle
- [Claude Code : la mémoire et les fichiers CLAUDE.md](https://code.claude.com/docs/en/memory)
- [Claude Code : les skills](https://code.claude.com/docs/en/skills)
- [Michael Feathers, *Working Effectively with Legacy Code*, Prentice Hall, 2004](https://www.oreilly.com/library/view/working-effectively-with/0131177052/) — l'origine des tests de caractérisation
- [Michael Nygard, *Documenting Architecture Decisions*, 2011](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — le format des décisions d'architecture
