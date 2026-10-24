# M13 — Bonnes pratiques

*Partie II — Le manuel de référence*

## Ce que couvre ce chapitre

Les chapitres précédents décrivent des outils ; celui-ci décrit des habitudes. Six pratiques reviennent dans toutes les équipes qui tirent parti d'un agent sans en payer le prix plus tard : planifier avant de coder, garder le contexte court, découper finement, écrire les tests d'abord, relire toujours, et savoir ce que tout cela coûte. Une septième les tient ensemble dans la durée : des registres, des rétrospectives, une communauté de pratique.

Aucune n'est nouvelle. Ce qui change avec un agent, c'est le prix de leur absence. Au chapitre 9, l'agent produit plus de demandes de fusion qu'un seul relecteur ne peut en lire, et la file passe de dix-neuf à quarante en quatre jours. Au chapitre 10, la testeuse relève quarante-sept anomalies en cinq semaines alors que tous les tests de l'agent sont verts. Au chapitre 26, l'équipe découvre que sa vélocité a culminé au moment exact où son taux de retouche culminait aussi. Trois fois, le même constat : l'agent accélère ce qu'on lui donne, y compris les mauvaises habitudes.

> **Version de référence.** Claude Code 2.1.301, publiée le 15 octobre 2026, avec la configuration Bedrock du chapitre M1. Ces pratiques ne dépendent d'aucune version ; les commandes citées, si.

Chaque section suit le même ordre : la pratique, ce qui se passe quand on l'oublie, et les gestes concrets qui la rendent facile.

## 1. Planifier avant de coder

Laisser l'agent coder d'emblée, c'est risquer qu'il résolve avec soin le mauvais problème. La séquence recommandée tient en quatre temps : explorer, planifier, implémenter, commiter. Les deux premiers se font en mode plan, où l'agent lit et propose sans rien modifier.

### Quand on l'oublie

Au chapitre 17, l'agent lit un programme, trouve une lettre dans une zone, et en déduit un sens. La déduction est plausible, fausse, et coûte une journée à la story la plus critique du sprint. Un plan aurait affiché l'hypothèse noir sur blanc, et quelqu'un l'aurait vue.

### Les gestes

1. **Commencer chaque story en mode plan** : `Maj+Tab` jusqu'à l'indicateur du mode plan, ou `claude --permission-mode plan`.
2. **Faire dire à l'agent ce qu'il ne sait pas** avant qu'il propose quoi que ce soit : « Avant de proposer un plan, liste ce que la story ne dit pas et que le code ne permet pas de trancher. » C'est la règle du CLAUDE.md du chapitre M3, appliquée au moment où elle compte : ne jamais inventer une règle de gestion.
3. **Lire le plan comme on lirait celui d'un collègue**, et le corriger directement : `Ctrl+G` l'ouvre dans l'éditeur.
4. **Approuver, puis laisser coder.** L'agent vérifie son travail contre son propre plan.
5. **Pour un travail plus large**, faire interroger l'humain par l'agent jusqu'à obtenir une spécification écrite, puis l'exécuter dans une session neuve, au contexte propre. C'est ce que fait la méthode du chapitre M9.

### Un plan qui se lit en deux minutes

Un bon plan répond à cinq questions, et l'équipe le demande sous cette forme dans son CLAUDE.md :

| Rubrique | Question |
| --- | --- |
| Ce que je n'ai pas compris | Qu'est-ce qui reste à confirmer, et auprès de qui ? |
| Fichiers touchés | Où vais-je intervenir, et pourquoi là ? |
| Démarche | Dans quel ordre, avec quels choix ? |
| Vérification | Quels scénarios doivent passer, quels tests j'ajoute ? |
| Hors périmètre | Qu'est-ce que je ne toucherai pas ? |

Les lignes correspondantes, à placer dans la rubrique *Façon de travailler* du CLAUDE.md (chapitre M3) :

```markdown
## Façon de travailler : le plan
- Toute story commence en mode plan. Aucun fichier n'est modifié avant que le plan soit approuvé.
- Avant de proposer un plan, liste ce que la story ne dit pas et que le code ne permet pas
  de trancher. N'invente jamais une règle de gestion : pose la question, en nommant qui peut répondre.
- Le plan suit toujours ces cinq rubriques, dans cet ordre :
  1. Ce que je n'ai pas compris : ce qui reste à confirmer, et auprès de qui.
  2. Fichiers touchés : chaque fichier, et pourquoi là.
  3. Démarche : l'ordre des étapes et les choix faits.
  4. Vérification : les scénarios qui doivent passer, les tests ajoutés.
  5. Hors périmètre : ce que je ne toucherai pas.
- Une rubrique sans objet s'écrit « rien à signaler » ; elle ne disparaît pas.
- Pendant l'implémentation, signale tout écart au plan approuvé avant de le faire.
- Exception : une modification qui se décrit en une phrase (coquille, libellé, renommage) se fait sans plan.
```

Chaque ligne est vérifiable dans un plan rendu par l'agent, ce qui permet de savoir, à la relecture, si elle est suivie.

### Quand s'en passer

Le mode plan a un coût. Pour une coquille, une ligne de journal, un renommage, on demande directement. La règle de la documentation de l'éditeur est la bonne : si l'on peut décrire la modification en une phrase, on saute le plan.

## 2. Garder le contexte court

Le contexte est la ressource qui compte le plus. Il contient toute la conversation : chaque message, chaque fichier lu, chaque sortie de commande. Il se remplit vite, et la qualité du travail baisse à mesure qu'il se remplit : l'agent oublie une consigne donnée au début, mélange deux sujets, refait une erreur déjà corrigée. Le million de jetons disponible avec la configuration de référence (chapitre M2) n'y change rien : c'est une limite, pas un objectif.

### Quand on l'oublie

Quatre situations reviennent, et chacune a son remède.

| Situation | Ce qui se passe | Remède |
| --- | --- | --- |
| La session fourre-tout | On commence une story, on pose une question sans rapport, on revient à la story ; le contexte mélange tout | `/clear` entre deux tâches sans rapport |
| La correction sans fin | L'agent se trompe, on corrige, il se trompe encore ; le contexte est plein de tentatives ratées | Après deux corrections, `/clear` et une meilleure consigne de départ |
| L'exploration infinie | « Regarde comment ça marche » : l'agent lit des centaines de fichiers | Une question précise, ou un sous-agent qui explore à part |
| Le CLAUDE.md obèse | Trop de consignes : les importantes se perdent | Moins de deux cents lignes ; le reste en règles et en skills |

La deuxième ligne est la plus contre-intuitive. Une session neuve avec une consigne meilleure, qui intègre ce qu'on a appris, fait presque toujours mieux qu'une longue session chargée de corrections.

### Les gestes

- **Une story, une session.** Avant de passer à autre chose, `/rename` pour retrouver la session plus tard, puis `/clear`.
- **Explorer à part.** « Utilise un sous-agent pour trouver comment le portail calcule la franchise » : il lit vingt fichiers dans son propre contexte et ne rend qu'un résumé (chapitre M5).
- **Poser les questions de côté.** `/btw` répond à une question rapide sans que la réponse entre dans la conversation.
- **Compacter en disant quoi garder.** `/compact garde la liste des fichiers modifiés et les commandes de test` ; ou, dans le CLAUDE.md, une consigne permanente sur ce que la compaction doit préserver.
- **Revenir en arrière plutôt que s'enfoncer.** `Échap` deux fois, ou `/rewind`, ramène la conversation et le code à un point antérieur (chapitre M2).
- **Surveiller.** `/context` montre ce qui occupe la place ; une ligne d'état personnalisée peut afficher en permanence le taux de remplissage.

### Ce que l'équipe met en place une fois pour toutes

Un CLAUDE.md court, des consignes spécialisées en skills qui ne se chargent qu'à l'usage, les outils en ligne de commande plutôt qu'un connecteur quand ils suffisent (chapitre M7), et un hook qui filtre la sortie des tests pour ne rendre que les échecs. Chacun de ces choix retire des milliers de jetons à chaque message, pour toute l'équipe.

## 3. Petites stories, travail en cours limité

Une story qui tient en une session de l'agent tient aussi en une relecture humaine. C'est la bonne taille : une seule intention, une branche, une demande de fusion, que le relecteur peut lire d'une traite et dont il peut juger le risque. La méthode du chapitre M9 l'estime à environ cinq cents lignes de code, tests non compris.

### Quand on l'oublie, et quand on exagère

Le chapitre 9 montre les deux excès. D'abord, l'agent produit plus de demandes de fusion qu'un seul relecteur ne peut en lire. Puis l'équipe découpe le travail en demandes plus petites, en pensant soulager le relecteur : le nombre de demandes augmente, mais le coût fixe de chaque relecture ne baisse pas. Lire le contexte d'une demande, comprendre son intention, vérifier ses tests prend le même temps pour vingt lignes que pour deux cents. En quatre jours, la file passe de dix-neuf à quarante, la qualité des relectures s'effondre, et le relecteur unique cède.

La bonne unité n'est donc pas la plus petite possible. C'est la story : un comportement utile, découpé par ce qu'il fait pour l'utilisateur, pas par couche technique.

### Ce que l'équipe a fait

1. **Arrêter de produire.** Tant que la file déborde, ouvrir une demande de plus ne fait qu'allonger l'attente de toutes les autres.
2. **Trier la file**, et fermer ce qui n'aurait pas dû être ouvert.
3. **Classer chaque demande par niveau de risque**, pour que la profondeur de la relecture suive le risque.
4. **Préparer chaque relecture** par une session neuve de l'agent (chapitres M5 et M10).
5. **Faire entrer un deuxième relecteur.**
6. **Plafonner** le nombre de demandes en revue : six au plus.

La vitesse affichée a chuté ; le temps d'attente aussi. C'est la loi de Little, bien connue des équipes de flux : à débit égal, le temps d'attente est proportionnel au nombre d'éléments en cours. Limiter le travail en cours est le moyen le plus direct de raccourcir l'attente.

### La profondeur de relecture suit le risque

| Niveau | Exemples | Relecture |
| --- | --- | --- |
| Vert | Libellé, documentation, configuration sans effet métier | Un relecteur, lecture rapide de la fiche de prérelecture |
| Orange | Règle de gestion, écran, intégration avec un autre système | Un relecteur, lecture complète, scénarios vérifiés |
| Rouge | Données personnelles, sécurité, paiement, système des contrats | Deux relecteurs, dont un qui connaît le cœur de gestion ; la sécurité si des données sont en jeu |

Le niveau se décide en préparant la story, s'inscrit dans la story et dans l'étiquette du ticket (chapitre M10), et la prérelecture peut proposer de le relever.

### Les gestes

- **La taille entre dans la définition de « prêt »** : une story qui ne tient pas en une session se redécoupe avant d'être prise.
- **La limite vit dans le tableau Jira** : la colonne *En revue* s'affiche en rouge au-delà de six.
- **« Arrêter de commencer, commencer à finir »** : quand la colonne est pleine, on relit avant d'ouvrir une nouvelle session.
- **Les agents en parallèle sur des stories indépendantes seulement** : le chapitre 8 montre ce que coûte la réunion de branches qui ont touché les mêmes notions.

## 4. Les tests d'abord

Un agent qui écrit le code puis les tests en relisant son code vérifie qu'il a fait ce qu'il a compris. Il ne vérifie pas qu'il a compris ce qu'il fallait. Pour que les tests disent quelque chose du besoin, ils doivent venir d'ailleurs, et arriver avant.

### Quand on l'oublie

Le chapitre 10 en donne la mesure. Émilie écrit ses plans de test comme toujours et les rattache aux stories dans Jira. Mais l'agent code à partir de la story seule, puis écrit ses propres tests en lisant son code ; les cas d'Émilie arrivent après, et ne s'exécutent qu'en fin de chaîne, à la main. En cinq semaines, elle relève quarante-sept anomalies alors que tous les tests de l'agent sont verts. Trente-huit sont révélées par un cas de son plan, et pour quinze d'entre elles, le cas était déjà dans Jira avant que l'agent commence à coder.

La question décisive vient d'elle : son travail peut-il servir d'entrée à l'agent ?

### La réponse en trois temps

| Temps | Ce qui change | Comment |
| --- | --- | --- |
| 1. Une condition pour être prête | Une story sans cas de test n'entre pas dans l'itération | La définition de « prêt » de l'équipe |
| 2. Des scénarios exécutables | Les cas sont réécrits en scénarios que la chaîne peut jouer | Des fichiers de scénarios dans `src/test/resources/scenarios/`, écrits par Émilie et le métier |
| 3. Rouge, puis vert, sans y toucher | L'agent doit voir les scénarios échouer, puis les faire passer, sans pouvoir les modifier | Une interdiction d'écriture (M4), le fichier des propriétaires (M10) |

Le rouge d'abord n'est pas un rite. Un scénario qui passe avant que le code existe ne teste rien ; le voir échouer prouve qu'il mesure bien ce qu'on va construire.

### La consigne type

```text
Lance les scénarios de SIN-57. Ils doivent échouer : montre-moi la sortie.
Implémente ensuite jusqu'à ce qu'ils passent, sans modifier aucun fichier
de src/test/resources/scenarios/. Ajoute les tests unitaires utiles.
Termine en montrant la sortie complète des scénarios et des tests.
```

La dernière ligne compte : on demande une preuve, pas une affirmation. Relire une sortie de test est plus rapide que relancer soi-même la vérification, et cela fonctionne pour une session qu'on n'a pas suivie.

### Donner à l'agent de quoi se vérifier seul

Un agent qui dispose d'un contrôle qu'il peut lancer, et qui renvoie vrai ou faux, travaille jusqu'à ce que le contrôle passe. Sans lui, c'est l'humain qui devient la boucle de vérification. Trois niveaux, du plus souple au plus strict :

- **Dans la consigne** : « lance les tests et corrige jusqu'à ce qu'ils passent ».
- **Par un hook de fin de tour** : le hook `Stop` du chapitre M6 lance les tests et empêche l'agent de conclure tant qu'ils échouent.
- **Par un regard neuf** : un sous-agent relit le résultat sans avoir vu le raisonnement qui l'a produit.

### Et après le vert

Les scénarios disent que la story fait ce qui était prévu ; ils ne disent pas qu'elle ne fait rien d'autre. Au chapitre 27, Émilie explore chaque story après le vert, et c'est là qu'elle trouve ce que personne n'avait prévu. Pour le code ancien, les tests de caractérisation du chapitre M11 jouent le même rôle : enregistrer ce que le système fait réellement, avant d'y toucher.

## 5. Une relecture humaine, toujours

Aucun code n'entre dans la branche principale sans qu'une personne l'ait lu et compris. La règle est inscrite dans la configuration depuis le chapitre M10 : branche protégée, approbation des propriétaires, aucune exception pour les automates. Ce chapitre parle de ce qui ne se configure pas : comment relire bien, et comment tenir quand la relecture devient le goulot.

### L'agent prépare, il ne signe pas

La phrase vient du chapitre 9. La prérelecture par un agent neuf, qui n'a pas écrit le code et ne connaît pas le raisonnement qui l'a produit, est précieuse : elle repère les cas oubliés, les incohérences, les écarts au plan. Mais un relecteur à qui l'on demande de trouver des problèmes en trouve presque toujours, même quand le travail est bon. Sa fiche se trie ; elle ne se suit pas aveuglément. Et la décision de fusionner reste à une personne.

### Cinq questions

Un humain qui relit le code d'un agent n'a pas à vérifier la syntaxe ni le style : la chaîne d'intégration et la prérelecture s'en chargent. Il se pose cinq questions.

| Question | Où regarder |
| --- | --- |
| Le changement fait-il ce que la story demande, et seulement cela ? | La spécification approuvée, son intention figée, les critères d'acceptation |
| Qu'est-ce qui a bougé hors du plan ? | Les fichiers touchés, les dépendances ajoutées, la configuration |
| Les tests prouvent-ils quelque chose ? | Les scénarios, qui ne doivent pas avoir changé ; les tests ajoutés, et ce qu'ils vérifient vraiment |
| Qu'est-ce qui pourrait casser en production ? | Le niveau de risque, les données touchées, les appels au système ancien |
| Saurais-je l'expliquer à un collègue ? | Si la réponse est non, on ne fusionne pas : on demande, ou on fait expliquer par l'agent |

La dernière question est la plus importante. Une équipe qui fusionne du code qu'elle ne comprend plus construit une dette que personne ne pourra rembourser.

### Quand la relecture devient le goulot

Au chapitre 18, l'équipe mesure qu'une story prend environ cinq heures de bout en bout, dont trente-cinq minutes d'écriture de code. Le reste, c'est préciser, vérifier, relire. Quand le train propose cinq développeurs de plus pour la phase 2, elle refuse, et demande à la place une personne du métier, une testeuse et un relecteur qui connaît le cœur de gestion.

C'est la conséquence logique : avec un agent, la capacité de relecture fixe le rythme de l'équipe. Les leviers sont connus :

- **Former des relecteurs.** Au chapitre 18, le tech lead relit, tranche, et forme ; la relecture en binôme, sur les stories rouges, sert aussi à former le deuxième relecteur.
- **Préparer chaque relecture** par la skill du chapitre M5, pour que l'humain commence par l'essentiel.
- **Adapter la profondeur au risque**, comme à la section 3.
- **Limiter le travail en cours**, pour qu'aucune demande n'attende assez longtemps pour que son auteur ait oublié ce qu'elle contient.

### Les signes d'une relecture qui ne relit plus

Une approbation donnée en une minute sur une demande de trois cents lignes ; des commentaires qui ne portent que sur la forme ; une prérelecture recopiée telle quelle ; des anomalies qui reviennent sur des stories pourtant approuvées. Quand ces signes apparaissent, ce n'est pas le relecteur qu'il faut blâmer, c'est la file qu'il faut réduire.

## 6. Maîtriser les coûts

### Le vrai coût n'est pas là où on le cherche

Au chapitre 26, le contrôle de gestion demande la vélocité de l'équipe pour la comparer à celle d'Horizon. En reconstituant l'histoire de chaque story, l'équipe découvre deux choses. Sa vélocité a culminé au sprint 2, au moment même où son taux de retouche culminait : on livrait vite ce qu'il faudrait refaire. Et le coût du modèle se révèle négligeable à côté du temps humain que coûte chaque erreur : une anomalie trouvée en recette, rouverte, recorrigée, relue et retestée vaut bien plus que les jetons de toutes les sessions de la story.

La première façon de maîtriser les coûts, ce sont donc les cinq pratiques précédentes. Une story bien préparée, testée d'abord et relue sérieusement coûte moins cher qu'une story rapide qui revient.

### Les jetons, quand même

Le coût des jetons reste à surveiller, ne serait-ce que pour éviter les dérives. L'éditeur donne un ordre de grandeur pour les déploiements en entreprise : environ treize dollars par développeur et par jour d'activité, cent cinquante à deux cent cinquante par mois, et moins de trente dollars par jour pour neuf utilisateurs sur dix. Ce qui fait varier la facture tient en peu de leviers :

| Levier | Le bon réflexe |
| --- | --- |
| Le contexte | La section 2 : une story, une session ; `/clear` entre deux tâches. Chaque message renvoie toute la conversation. |
| Le modèle | Sonnet pour l'essentiel du travail ; Opus pour la planification, l'architecture, les problèmes difficiles. `/model` change en cours de session. |
| L'effort | `/effort` règle la profondeur de raisonnement ; un effort bas suffit à une tâche simple. Les paramètres gérés peuvent plafonner l'effort avec `maxEffortLevel`. |
| Les sous-agents | Chacun consomme ses propres jetons ; un modèle plus léger suffit souvent à une recherche simple, si la configuration le permet. |
| Les pauses | Après une pause plus longue que la durée de vie du cache, le premier message relit tout le contexte au plein tarif. |
| L'automatisation | Les exécutions dans la chaîne d'intégration se bornent avec `--max-turns`, une durée maximale, et `--max-budget-usd`. |

### Savoir ce qu'on dépense

- **Pour soi** : `/usage` affiche l'estimation de la session en cours. Le chiffre est calculé au prix public ; les paramètres gérés peuvent y appliquer les tarifs négociés de la maison avec `modelPricing`.
- **Pour la maison** : avec Bedrock, la facture est celle du compte AWS dédié du chapitre M1, visible dans les outils de suivi des coûts d'AWS.
- **Par personne et par story** : la télémétrie de l'outil, exportée vers l'observabilité de la maison (chapitre M14).

### Le coût complet par story

Pour la phase 2, l'équipe du chapitre 26 abandonne les points d'effort et les remplace par quatre indicateurs définis par écrit et calculés sans saisie : le débit, le temps de traversée, le taux de retouche, et le coût complet par story. Ce dernier additionne les jetons et le temps humain passé à préparer, relire, tester et corriger. C'est la seule mesure qui dise si l'agent fait gagner de l'argent, et elle répond souvent autrement que la facture du modèle. Le chapitre M14 en donne le calcul.

## 7. Tenir la pratique dans la durée

Les six pratiques précédentes s'usent. Une équipe pressée saute un plan, laisse une session gonfler, fusionne une demande relue trop vite. Trois rendez-vous les entretiennent.

### Une erreur qui revient monte d'un cran

Quand l'agent refait une erreur, la question n'est pas seulement « comment la corriger ? », mais « à quel niveau l'empêcher ? ».

| Fois | Ce que l'on fait | Chapitre |
| --- | --- | --- |
| La première | On corrige dans la session | M2 |
| La deuxième | Une ligne vérifiable dans le CLAUDE.md, ou une règle limitée aux fichiers concernés | M3 |
| Si elle persiste | Une skill qui encode la bonne procédure, ou un hook qui la contrôle | M5, M6 |
| Si elle met en danger | Une interdiction dans les paramètres, ou un contrôle obligatoire de la chaîne d'intégration | M4, M10 |
| Si elle menace toute la maison | Le socle | M8 |

### Le registre des dettes

Certaines faiblesses ne se corrigent pas en une story. On les inscrit dans un registre, avec un propriétaire et une échéance, pour qu'elles ne disparaissent pas des mémoires.

| Dette | Exemple | Ce qui la rembourse |
| --- | --- | --- |
| De connaissance | Le savoir du système des contrats repose sur Gérard seul | Le wiki et les séances quotidiennes (M11) |
| De vérification | Une partie du portail n'a pas de scénarios d'acceptation | Des scénarios écrits avant toute nouvelle story dans cette partie |
| D'outillage | Une skill sans propriétaire ; un CLAUDE.md qui dépasse deux cents lignes | La revue mensuelle des fichiers partagés (M12) |
| De sécurité | Un jeu de données de recette dont l'anonymisation n'a pas été vérifiée | La vérification par la sécurité, avant tout usage par un agent |

Au chapitre 17, c'est l'inscription de la dette de connaissance au registre qui permet de la traiter tout de suite, une heure par jour, plutôt qu'« un jour ».

### La rétrospective, avec des faits

Chaque fin d'itération, la rétrospective ordinaire reçoit un point de plus : ce que l'agent a fait de travers deux fois, et à quel niveau on l'empêche désormais. Les chiffres arrivent avant la réunion. Au chapitre 11, l'agent les tire de Jira et de GitHub en dix minutes, et ils changent la conversation : l'attente avant relecture, les anomalies après fusion, la part du travail faite le soir.

À la fin d'une phase, la rétrospective est plus large. Au chapitre 20, elle sert à décider de la suite : garder ce qui a marché, abandonner ce qui n'a pas tenu, choisir ce qu'on essaie ensuite. Le format du roman vaut pour toute nouvelle pratique : un essai sur une seule story, sur une branche à part, avec des mesures choisies d'avance et une condition d'arrêt écrite avant de commencer.

### La communauté de pratique

Une fois par mois, une personne de chaque équipe du train : les skills qui ont changé, les incidents et leurs leçons, les mesures, et ce qui monte au catalogue ou en descend (chapitre M12). C'est là qu'une erreur faite par une équipe cesse d'être refaite par les autres.

### Les sept pratiques sur une page

| Pratique | Le geste minimal | Le signe d'alerte |
| --- | --- | --- |
| Planifier avant de coder | Le mode plan, et la liste de ce que l'agent ne sait pas | Une hypothèse découverte en recette |
| Garder le contexte court | Une story, une session | Une correction refaite pour la troisième fois |
| Petites stories, travail limité | Six demandes en revue au plus | Une file qui s'allonge alors que tout le monde produit |
| Les tests d'abord | Des scénarios écrits avant, rouges puis verts, intouchables | Des tests verts et des anomalies en recette |
| Une relecture humaine | Cinq questions, et ne fusionner que ce qu'on sait expliquer | Une approbation en une minute |
| Maîtriser les coûts | Le coût complet par story | Une vitesse qui monte avec la retouche |
| Tenir dans la durée | Le registre, la rétrospective, la communauté | Une même erreur dans deux équipes |

## Dans le roman

| Chapitre | Scène | Ce qu'elle illustre ici |
| --- | --- | --- |
| 9 — Le goulot s'appelle Julien | La file passe de dix-neuf à quarante demandes en quatre jours ; découper plus fin aggrave le problème ; l'équipe arrête de produire, trie, classe par risque, prépare chaque relecture, ajoute un relecteur et plafonne la file. | Petites stories, mais pas trop ; limiter le travail en cours ; la profondeur de relecture suit le risque. |
| 10 — Émilie ne suit plus | Quarante-sept anomalies en cinq semaines avec des tests verts ; trente-huit révélées par un cas du plan d'Émilie. | Les tests d'abord, écrits par d'autres, rouges puis verts, intouchables. |
| 11 — Rétro sous tension | L'agent calcule en dix minutes les vrais chiffres du sprint avant la rétrospective. | Une rétrospective qui part des faits. |
| 17 — Le savoir de Gérard | La dette de connaissance inscrite au registre, et traitée une heure par jour. | Le registre des dettes. |
| 18 — Les rôles bougent | Trente-cinq minutes de code sur cinq heures par story ; l'équipe refuse cinq développeurs et demande métier, testeuse et relecteur. | La relecture fixe le rythme. |
| 20 — La rétrospective du dernier sprint | Une méthode essayée sur une seule story, avec mesures et condition d'arrêt. | La rétrospective de fin de phase. |
| 26 — La vélocité est morte | La vélocité culmine avec la retouche ; le coût du modèle pèse peu face au temps humain de chaque erreur ; quatre indicateurs remplacent les points. | Le vrai coût ; le coût complet par story. |

Pour aller plus loin : M2 (sessions et retour arrière), M3 (CLAUDE.md), M4 (verrous), M5 (sous-agents et prérelecture), M6 (hooks de fin de tour), M10 (circuit et mesures), M11 (wiki et tests de caractérisation), M14 (télémétrie et coûts).

## Sources

Consultées le 22 octobre 2026.

- [Claude Code : bonnes pratiques](https://code.claude.com/docs/en/best-practices)
- [Claude Code : maîtriser les coûts](https://code.claude.com/docs/en/costs)
- [Claude Code : modes de permission et mode plan](https://code.claude.com/docs/en/permission-modes)
- [Claude Code : sous-agents](https://code.claude.com/docs/en/sub-agents)
- [John D. C. Little, *A Proof for the Queuing Formula L = λW*, Operations Research, 1961](https://doi.org/10.1287/opre.9.3.383) — la loi de Little
