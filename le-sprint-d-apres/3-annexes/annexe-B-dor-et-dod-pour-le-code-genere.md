# Annexe B — DoR et DoD pour le code généré

*Annexes*

## À quoi sert cette annexe

La définition de « prêt » (*Definition of Ready*, DoR) dit quand une story peut entrer dans une itération ; la définition de « terminé » (*Definition of Done*, DoD) dit quand elle peut en sortir. La seconde est un engagement du cadre Scrum ; la première est une pratique répandue, que beaucoup d'équipes formalisent.

Avec un agent, les deux changent de poids. La définition de « prêt » devient la vraie porte d'entrée : une story mal préparée n'est plus codée lentement, elle est codée vite et de travers. La définition de « terminé » doit, elle, rester exigeante au moment même où produire du code ne coûte presque plus rien. Le roman le montre trois fois : au chapitre 9, l'agent produit plus que l'équipe ne peut relire ; au chapitre 10, des tests verts cachent quarante-sept anomalies ; au chapitre 17, une hypothèse silencieuse coûte une journée.

Cette annexe donne les deux définitions telles que l'équipe du portail les applique à la fin de la phase 2, au format d'une liste à cocher qu'on peut copier dans `docs/definition-pret.md` et `docs/definition-termine.md`. Chaque critère renvoie au chapitre qui l'a fait naître.

Deux principes les traversent :

- **Un critère se vérifie.** « Story claire » ne se vérifie pas ; « hors-périmètre écrit » si.
- **Ce qui peut se vérifier par un programme se vérifie par un programme.** Le reste revient à une personne nommée. La section *Qui vérifie quoi* fait le partage.

## La définition de « prêt »

Une story n'entre dans l'itération que si chaque case est cochée. Une seule case vide, et elle retourne en préparation.

```markdown
# Définition de « prêt » — portail sinistres

## Ce que la story demande
- [ ] L'intention est écrite en une ou deux phrases : ce qui doit être vrai une fois la story finie.
- [ ] Les critères d'acceptation sont écrits, et validés nommément par la Product Owner.
- [ ] Le hors-périmètre est écrit : ce que la story ne fera pas, et pourquoi.

## Ce qui la vérifiera
- [ ] Les scénarios d'acceptation existent, écrits par le métier et la recette, et s'exécutent.
- [ ] Les données de test nécessaires existent dans les jeux synthétiques.

## Ce qui pourrait la bloquer
- [ ] Aucune question ouverte ne bloque le travail ; chaque question restante a un nom et une date.
- [ ] Les dépendances sont liées dans Jira, et terminées ou planifiées avant elle.
- [ ] Si elle touche le système des contrats : les pages du wiki concernées sont relues par l'expert.

## Sa taille et son risque
- [ ] Elle tient en une session de l'agent ; sinon, elle est redécoupée par comportement.
- [ ] Son niveau de risque est attribué : vert, orange ou rouge.

## Son ticket
- [ ] Le ticket Jira existe, porte l'étiquette de risque, la priorité et l'itération.
```

### D'où viennent ces critères

| Critère | Ce qu'il évite | D'où il vient |
| --- | --- | --- |
| Intention, critères validés, hors-périmètre | Une story que l'agent complète par des hypothèses | Chapitres 22 et 23 ; M9 |
| Scénarios exécutables avant le code | Des tests écrits par l'agent d'après son propre code | Chapitre 10 ; M13 |
| Données synthétiques disponibles | La tentation de tester sur un vrai dossier | Chapitre 13 |
| Questions ouvertes nommées et datées | Une question qui reste sans réponse jusqu'à la recette | Chapitre 22 ; M3 |
| Dépendances liées | Une story codée qui attend sur sa branche | Chapitre 22 ; M10 |
| Pages du wiki relues | Un sens deviné dans un programme ancien | Chapitre 17 ; M11 |
| Une session au plus | Une demande de fusion trop grosse pour être relue | Chapitre 9 ; M13 |
| Niveau de risque | Une relecture trop légère sur une story sensible | Chapitre 16 ; M13 |
| Ticket Jira complet | Une story invisible pour le pilotage | Chapitre 25 ; M10 |

Le critère des scénarios est le plus coûteux à tenir, et le plus rentable. Au chapitre 10, pour quinze des anomalies relevées par Émilie, le cas de test existait déjà dans Jira avant que l'agent commence à coder ; il manquait seulement qu'il serve d'entrée.

## La définition de « terminé »

Une story n'est terminée que lorsque toutes les cases sont cochées. « Le code est écrit » n'en est qu'une parmi d'autres.

```markdown
# Définition de « terminé » — portail sinistres

## Ce que l'agent a produit
- [ ] La spécification porte le nom de qui l'a approuvée.
- [ ] Les scénarios ont échoué, puis passé, sans avoir été modifiés ; la sortie est jointe.
- [ ] Les tests unitaires utiles sont ajoutés.
- [ ] Tout écart au plan approuvé a été signalé et accepté.
- [ ] Aucune dépendance n'est ajoutée sans accord du référent technique.

## Ce que la chaîne a vérifié
- [ ] Tous les contrôles obligatoires sont verts : construction, tests, scénarios, journaux
      sans données personnelles, détection de secrets, clé Jira, spécification approuvée,
      seuils de qualité.

## Ce que des personnes ont vérifié
- [ ] La prérelecture est faite, et chacun de ses points est retenu ou écarté avec sa raison.
- [ ] Les propriétaires des fichiers touchés ont approuvé, à la profondeur que demande le risque.
- [ ] Le relecteur sait expliquer le changement.
- [ ] La testeuse a exploré la story après le vert.

## Ce qui reste après la story
- [ ] Ce qu'on a appris sur une règle de gestion est versé au wiki ; une décision est enregistrée.
- [ ] La demande de fusion est fusionnée, la branche supprimée ; le ticket est passé à « Terminé »
      par l'intégration.
- [ ] La story est démontrable au métier, sur l'environnement de recette.
```

### D'où viennent ces critères

| Critère | Ce qu'il évite | D'où il vient |
| --- | --- | --- |
| Spécification approuvée par une personne nommée | Un point d'arrêt sauté par une phrase de la consigne | M9 |
| Scénarios rouges puis verts, intouchés, avec la sortie | Des tests qui ne prouvent rien ; une réussite affirmée sans preuve | Chapitre 10 ; M13 |
| Écarts au plan signalés | Une modification hors du périmètre approuvé | M13 |
| Aucune dépendance sans accord | Une bibliothèque que personne n'a choisie | M4 |
| Contrôles obligatoires | Une erreur qui passe parce qu'on était pressé, agent ou humain | Chapitre 13 ; M10 |
| Prérelecture triée | Une fiche suivie aveuglément, ou ignorée | Chapitre 9 ; M5 |
| Approbation des propriétaires, selon le risque | Un scénario ou un hook modifié sans son responsable | Chapitre 16 ; M10 |
| Le relecteur sait expliquer | Du code fusionné que plus personne ne comprend | M13 |
| Exploration après le vert | Ce que personne n'avait prévu | Chapitre 27 |
| Savoir versé au wiki | Une règle découverte puis oubliée | Chapitres 17 et 24 ; M11 |
| Ticket passé par l'intégration | Une double saisie, une deuxième vérité | Chapitre 25 ; M10 |
| Démontrable au métier | Une story techniquement finie qui ne répond pas au besoin | Chapitre 27 |

Trois critères sont propres au code produit par un agent, et n'existaient pas dans la définition de l'équipe avant l'arrivée de l'agent : la preuve jointe plutôt qu'une affirmation, le signalement des écarts au plan, et la capacité du relecteur à expliquer ce qu'il approuve.

## Qui vérifie quoi

Une liste à cocher que chacun coche de bonne foi finit par être cochée par habitude. La règle du chapitre M10 s'applique ici aussi : ce qu'un programme peut vérifier, un programme le vérifie, et bloque ; le reste revient à une personne nommée.

### La définition de « prêt »

| Critère | Vérifié par | Comment |
| --- | --- | --- |
| Ticket complet : étiquette de risque, priorité, itération | Jira | Une règle de flux refuse le passage à *Prêt* si un champ manque |
| Dépendances terminées ou planifiées | Jira | Les liens entre tickets, visibles au tableau du train |
| Scénarios existants et exécutables | La chaîne d'intégration | Un contrôle vérifie qu'un fichier de scénarios porte la clé de la story et se lit sans erreur |
| Intention, critères validés, hors-périmètre | La Product Owner | Sa validation nominative dans la story |
| Scénarios et données de test | La testeuse et le métier | Ils les écrivent ; leur nom figure dans le fichier des propriétaires |
| Questions ouvertes, pages du wiki relues | Le référent technique, l'expert | Au moment de la préparation |
| Taille | L'équipe | Lors de l'affinage, en se demandant si la story tient en une session |

### La définition de « terminé »

| Critère | Vérifié par | Comment |
| --- | --- | --- |
| Spécification approuvée | La chaîne d'intégration | Le contrôle de la ligne *Approuvé par* (M10) |
| Scénarios intouchés | Le poste et le serveur | L'interdiction d'écriture (M4) et le fichier des propriétaires (M10) |
| Contrôles obligatoires | La chaîne d'intégration | Les contrôles déclarés obligatoires sur la branche principale |
| Approbation des propriétaires | GitHub | La branche protégée |
| Ticket passé à *Terminé* | L'intégration GitHub et Jira | À la fusion, sans saisie |
| Prérelecture triée, écarts au plan | Le relecteur | En lisant la fiche et la spécification |
| Le relecteur sait expliquer | Le relecteur lui-même | La cinquième question du chapitre M13 |
| Exploration | La testeuse | Avant la fusion des stories orange et rouges, après pour les vertes |
| Savoir versé au wiki | Le développeur, avec l'expert | Une demande de fusion sur le wiki, liée à la story |
| Démontrable au métier | La Product Owner | À la démonstration de fin d'itération |

Les critères vérifiés par un programme ne se discutent pas : une demande de fusion qui ne les remplit pas ne peut pas être fusionnée. Les critères humains, eux, se discutent en rétrospective quand ils glissent ; c'est le rôle des signes d'alerte du chapitre M13.

## Selon le niveau de risque

Les deux définitions valent pour toutes les stories. Le niveau de risque, attribué en préparation, règle la profondeur de certaines vérifications ; il n'en supprime aucune.

|  | Vert | Orange | Rouge |
| --- | --- | --- | --- |
| Exemples | Libellé, documentation, configuration sans effet métier | Règle de gestion, écran, intégration avec un autre système | Données personnelles, sécurité, paiement, système des contrats |
| Préparation | La définition de « prêt » | La même, avec des scénarios qui couvrent les cas limites connus | La même, avec les pages du wiki relues par l'expert, et des tests de caractérisation si le système ancien est touché |
| Relecture | Un relecteur, lecture de la fiche de prérelecture | Un relecteur, lecture complète | Deux relecteurs, dont un qui connaît le cœur de gestion |
| Sécurité | — | — | La sécurité relit si des données personnelles sont en jeu |
| Exploration | Après la fusion, par sondage | Avant la fusion | Avant la fusion, avec un jeu de données dédié |
| Démonstration | À la fin de l'itération | À la fin de l'itération | À la Product Owner, avant la fusion |

La prérelecture peut proposer de relever le niveau, jamais de l'abaisser. Une story qui change de niveau en cours de route repasse par la définition de « prêt » du niveau supérieur.

### Le cas de l'urgence

Une correction de production ne dispense d'aucune case ; elle en change l'ordre. La story est préparée en quelques minutes, le scénario qui reproduit l'anomalie est écrit avant le correctif, et la relecture se fait en direct, à deux. Au chapitre 13, c'est un test de la chaîne qui a trouvé la ligne fautive en quatre minutes : les contrôles automatiques sont précisément ce qui permet d'aller vite sans aller à l'aveugle.

## Faire vivre ces définitions

### Qui en répond

La définition de « prêt » appartient à la Product Owner, avec l'équipe ; celle de « terminé », à l'équipe, avec le référent technique. Toutes deux sont versionnées dans `docs/`, inscrites au registre des propriétaires (M12), et ne changent que par une demande de fusion, discutée en rétrospective.

### Quand les changer

| Signal | Ce qu'on fait |
| --- | --- |
| Une anomalie trouvée en recette qu'un critère aurait arrêtée | On ajoute le critère, au bon niveau de risque |
| Un critère que personne ne sait vérifier | On le reformule pour qu'il se vérifie, ou on le retire |
| Un critère qu'un programme peut désormais vérifier | On l'automatise, et il passe dans la colonne de la chaîne |
| Des cases cochées par habitude | On en parle en rétrospective, chiffres à l'appui |

L'indicateur qui dit si la définition de « terminé » remplit son rôle est le taux de retouche du chapitre M14. Au début, le temps de traversée monte : c'est attendu, et c'est ce que montre le chapitre 9 quand la vitesse affichée baisse en même temps que l'attente.

### Faire vérifier par l'agent, faire décider par l'équipe

L'agent sait lire une liste à cocher. Deux lignes dans le CLAUDE.md lui font vérifier les deux définitions, sans lui en confier la décision :

```markdown
- Avant de commencer une story, vérifie docs/definition-pret.md. Si une case n'est
  pas remplie, arrête-toi et dis laquelle.
- Avant d'ouvrir la demande de fusion, vérifie docs/definition-termine.md et liste,
  dans la description, les cases qui restent à cocher par une personne.
```

L'agent signale ce qui manque ; il ne coche pas à la place des personnes qui en répondent.

## Renvois

- M9 — BMAD : la spécification et son approbation
- M10 — GitHub et Jira : contrôles obligatoires, branche protégée, fichier des propriétaires
- M11 — Le wiki : verser ce qu'on apprend
- M13 — Bonnes pratiques : petites stories, tests d'abord, relecture, niveaux de risque
- M14 — Dépannage et coûts : le taux de retouche
- Annexe A — Modèle de CLAUDE.md

Source, consultée le 23 octobre 2026 : [Le Guide Scrum, 2020](https://scrumguides.org/scrum-guide.html), pour la définition de « terminé » comme engagement de l'incrément.
