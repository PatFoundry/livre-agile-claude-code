# Annexe D — Grille de métriques

*Annexes*

## À quoi sert cette annexe

Les mesures sont dispersées dans le manuel : le flux au chapitre M10, les signes d'alerte au chapitre M13, la consommation et le coût complet au chapitre M14, la dette de connaissance au chapitre M11. Cette annexe les rassemble en une seule grille, avec pour chacune sa définition, sa source, sa fréquence, un seuil d'alerte de départ et la personne qui la lit.

Le roman montre ce que vaut une bonne mesure, et ce que coûte une mauvaise. Au chapitre 11, l'agent tire en dix minutes les vrais chiffres d'un sprint, et ils contredisent ce que chacun croyait. Au chapitre 26, l'équipe découvre que sa vélocité a culminé au moment où sa retouche culminait aussi : la mesure qu'on lui demandait récompensait exactement ce qu'il fallait éviter.

### Cinq règles

Chaque indicateur de la grille les respecte, et un indicateur qui en enfreint une n'y entre pas.

1. **Défini par écrit**, avant d'être calculé : ce qu'on compte, à partir de quand, ce qu'on exclut.
2. **Calculé sans saisie**, à partir de ce que Jira, GitHub et la télémétrie enregistrent déjà. Personne ne remplit de feuille de temps.
3. **Mesurant un système, pas des personnes** : par équipe et dans le temps, jamais par développeur.
4. **Lu par quelqu'un** qui sait ce qu'il en fera. Un indicateur sans lecteur est un indicateur de trop.
5. **Vérifié à la main**, sur un échantillon, avant qu'on s'y fie, puis chaque trimestre.

## La grille

Les seuils d'alerte sont des points de départ, à ajuster après trois ou quatre itérations de mesure. Un seuil franchi n'est pas une faute : c'est une question à poser en rétrospective.

### Le flux

| Indicateur | Source | Fréquence | Alerte de départ | Lu par |
| --- | --- | --- | --- | --- |
| Débit : stories terminées par semaine | Jira | Hebdomadaire | Baisse trois semaines de suite | L'équipe, la Product Owner |
| Temps de traversée : de la création du ticket à la fusion | Jira, GitHub | Par itération | Le 85e centile monte deux itérations de suite | L'équipe |
| Attente avant relecture | GitHub | Quotidienne | Médiane au-delà d'un jour ouvré | Le tech lead |
| Demandes en revue | GitHub, tableau Jira | En continu | Plus de six | Toute l'équipe |

### La qualité

| Indicateur | Source | Fréquence | Alerte de départ | Lu par |
| --- | --- | --- | --- | --- |
| Taux de retouche | Jira | Par itération | Hausse deux itérations de suite | L'équipe, en rétrospective |
| Anomalies après fusion, par story | Jira | Par itération | Une story rouge avec une anomalie | Le tech lead, la testeuse |
| Écarts de spécification révélés en démonstration | Jira, par étiquette | Par itération | Plus d'un par itération | La Product Owner |

### Le coût

| Indicateur | Source | Fréquence | Alerte de départ | Lu par |
| --- | --- | --- | --- | --- |
| Coût complet par story, médiane | Télémétrie, GitHub, Jira, forfaits | Par itération | Hausse deux itérations de suite | L'équipe, le contrôle de gestion |
| Coût du modèle par story | Télémétrie | Par itération | Une story au-delà du double de la médiane | Le référent technique |
| Écart entre la télémétrie et la facture AWS | Télémétrie, AWS | Mensuelle | Plus de 10 % | La DSI |
| Quotas atteints | Télémétrie, CloudWatch | Hebdomadaire | Des abandons après réessais, plusieurs jours de suite | La DSI |

### La soutenabilité

| Indicateur | Source | Fréquence | Alerte de départ | Lu par |
| --- | --- | --- | --- | --- |
| Travail du soir : part des commits faits entre 20 h et 7 h, ou le week-end | Git | Par itération | Plus de 10 % | Le directeur de projet |

### La connaissance

| Indicateur | Source | Fréquence | Alerte de départ | Lu par |
| --- | --- | --- | --- | --- |
| « Pourquoi » encore à confirmer dans le wiki | Le wiki | Hebdomadaire | Stable ou en hausse quatre semaines de suite | Le propriétaire du wiki |
| Programmes anciens touchés par les prochaines stories, sans page relue | Le wiki, Jira | Par itération | Un seul, pour une story rouge | Le référent technique |

### La sécurité et l'outillage

| Indicateur | Source | Fréquence | Alerte de départ | Lu par |
| --- | --- | --- | --- | --- |
| Secrets détectés par la chaîne d'intégration | La chaîne | En continu | Un seul | La sécurité |
| Blocages par les hooks du socle | Télémétrie | Mensuelle | Une hausse soudaine | La sécurité, le référent |
| Skills et plugins installés mais inutilisés | Télémétrie, `/doctor` | Trimestrielle | Tout élément inutilisé depuis trois mois | Leurs propriétaires |

Dix-sept indicateurs, c'est beaucoup pour une équipe. Ceux qui se lisent à chaque itération sont les quatre du chapitre 26 : débit, temps de traversée, taux de retouche, coût complet par story. Les autres attendent qu'on en ait besoin, ou qu'un seuil se déclenche.

## Les définitions exactes

Deux équipes qui mesurent « le temps de traversée » sans l'avoir défini comparent deux choses différentes. Au chapitre 26, les quatre indicateurs sont définis par écrit avant le premier calcul ; voici ces définitions, et celles des deux indicateurs qu'on consulte le plus souvent ensuite.

| Indicateur | Ce qu'on compte | Bornes | Ce qu'on exclut |
| --- | --- | --- | --- |
| Débit | Les stories dont le ticket passe à *Terminé* dans la semaine | Du lundi 0 h au dimanche 24 h | Les anomalies, comptées à part ; une story redécoupée compte pour autant de stories |
| Temps de traversée | La durée entre la création du ticket, c'est-à-dire la validation de la story, et la fusion de sa dernière demande | En jours calendaires ; on publie la médiane et le 85e centile | Les stories abandonnées |
| Taux de retouche | La part des stories terminées qui ont été rouvertes, ou auxquelles une anomalie a été reliée dans les trente jours suivant la fusion | Calculé trente jours après la fin de l'itération | Les anomalies qui relèvent d'une autre story ou d'un autre système |
| Coût complet par story | Le coût du modèle, plus le temps humain estimé par forfaits, multiplié par le taux interne | Par story terminée ; on publie la médiane | Rien : c'est sa raison d'être |
| Attente avant relecture | La durée entre l'ouverture de la demande de fusion, hors brouillon, et la première relecture humaine | En heures ouvrées | Le commentaire de prérelecture de l'agent |
| Travail du soir | La part des commits dont l'heure d'auteur, à l'heure de Paris, tombe entre 20 h et 7 h, ou le week-end | Par itération, pour l'équipe entière | Les commits des automates ; aucun chiffre par personne |

### Quelques précisions

**Le taux de retouche arrive en retard.** Il faut attendre trente jours pour savoir si une story est revenue. On le publie donc avec une itération de décalage, et l'on n'en tire rien sur l'itération en cours.

**Le temps de traversée se lit au 85e centile autant qu'à la médiane.** La médiane dit ce que vit une story ordinaire ; le 85e centile dit ce que vivent celles qui coincent, et c'est sur elles que l'équipe peut agir.

**Les forfaits du coût complet** sont ceux du chapitre M14 : préparation, tours de relecture, exploration, anomalies. Ils sont convenus avec le contrôle de gestion, vérifiés à la main chaque trimestre sur un échantillon, et ajustés s'ils dérivent.

**Les commits de l'agent** portent comme auteur la personne qui l'a lancé, et l'agent en co-auteur (chapitre M10). Ils comptent donc dans le travail du soir de l'équipe : un agent lancé à 22 h reste un signe que quelqu'un travaillait à 22 h.

### La prévision

Le débit des huit dernières semaines alimente la prévision en fourchette du chapitre M10 : on simule de nombreuses fois le nombre de semaines nécessaires pour finir le reste du périmètre, et l'on publie la durée atteinte dans la moitié des simulations et celle atteinte dans 85 % d'entre elles. Au chapitre 26, la sponsor refuse de donner une date avant deux itérations mesurées : il faut un débit observé pour que la simulation dise quelque chose.

## Lire les indicateurs ensemble

Un indicateur isolé se laisse interpréter dans le sens qui arrange. La leçon du chapitre 26 tient en une matrice : le débit ne dit rien tant qu'on ne sait pas ce qu'il a coûté en retouche.

> *Schéma non reproduit dans cette version Markdown : débit et retouche · quatre situations, une seule à viser.*

### D'autres signaux combinés

| Ce qu'on observe | Ce que cela signifie souvent | Ce qu'on fait | Chapitre |
| --- | --- | --- | --- |
| L'attente avant relecture et le nombre de demandes en revue montent ensemble | La relecture est devenue le goulot | Arrêter de produire, préparer chaque relecture, faire entrer un deuxième relecteur, plafonner la file | 9 ; M13 |
| Le débit tient, le travail du soir monte | Le rythme est tenu au prix des soirées | Réduire l'engagement de l'itération suivante | 11 |
| Le coût du modèle monte, la retouche ne bouge pas | Des sessions trop longues, ou un modèle surdimensionné | Revoir les habitudes de contexte et le choix des modèles | M13, M14 |
| Les écarts de spécification et la retouche montent ensemble | Les stories entrent mal préparées | Durcir la définition de « prêt » ; plus de temps avec le métier | 22 ; annexe B |
| Des anomalies sur les stories qui touchent le système ancien, des « pourquoi » qui ne baissent pas | Le savoir de l'expert ne passe pas assez vite | Prioriser les séances sur les programmes des prochaines stories | 17 ; M11 |
| Le 85e centile du temps de traversée monte, la médiane ne bouge pas | Quelques stories restent coincées | Regarder leurs dépendances dans Jira | 22 ; M10 |

Ces lectures sont des hypothèses, pas des conclusions. Elles disent où regarder en rétrospective ; c'est l'équipe, chiffres sous les yeux, qui dit ce qui s'est vraiment passé.

## Ce qu'il ne faut pas mesurer

Avec un agent, tout se compte : les lignes, les sessions, les jetons, les demandes de fusion. La plupart de ces chiffres sont faciles à obtenir et trompeurs dès qu'on les prend pour des objectifs. C'est la loi de Goodhart : une mesure qui devient une cible cesse d'être une bonne mesure.

| Mesure tentante | Pourquoi elle trompe | À la place |
| --- | --- | --- |
| La vélocité en points d'effort | Avec un agent, les points disent de moins en moins le temps qu'il faudra ; au chapitre 26, elle culmine avec la retouche | Le débit, lu avec le taux de retouche |
| Les lignes de code produites, la part de code écrite par l'agent | Récompensent le volume ; un code plus long n'est pas un code meilleur | Le débit et la retouche |
| Le nombre de demandes de fusion | Au chapitre 9, découper plus fin multiplie les demandes sans réduire le coût de chaque relecture | Le débit en stories |
| Les jetons, les sessions ou le temps passé dans l'outil, par personne | Mesurent l'usage, pas la valeur ; et transforment l'outil en surveillance | Le coût complet par story, par équipe |
| Un classement des développeurs | Pousse chacun à optimiser son chiffre au détriment de l'équipe, et à éviter les stories difficiles | Rien : la grille mesure un système |
| La couverture des tests comme objectif | On écrit des tests qui exécutent le code sans rien vérifier | Un seuil plancher dans la chaîne, et des scénarios écrits par la recette |
| Une comparaison brute entre équipes | Périmètres, systèmes anciens et pratiques diffèrent ; au chapitre 26, l'agent n'explique qu'un tiers de l'écart avec Horizon | Chaque équipe comparée à elle-même, dans le temps |

La télémétrie de l'outil sait produire certains de ces chiffres, comme les lignes de code ou le temps actif. Qu'ils existent ne veut pas dire qu'il faut les afficher. Le tableau de bord de l'équipe ne montre que la grille ; le reste sert, au besoin, à comprendre une anomalie de la grille.

## Mettre en place la grille

### En six étapes

1. **Commencer par les quatre du chapitre 26** : débit, temps de traversée, taux de retouche, coût complet par story. Les autres viennent quand une question les appelle.
2. **Écrire les définitions** de la section précédente dans `docs/mesures.md`, avec un propriétaire, et les faire valider par l'équipe et le contrôle de gestion.
3. **Faire calculer une première fois par l'agent**, comme au chapitre 11, à partir de Jira, de GitHub et de la télémétrie, en lecture seule.
4. **Figer le calcul** dans un script relu et versionné, que l'on relance ensuite à chaque itération (chapitre M10). L'agent invente la mesure ; le script la reproduit.
5. **Vérifier à la main** sur un échantillon de stories, comme le fait l'équipe au chapitre 26, avant de publier quoi que ce soit.
6. **Publier une page**, pas un portail : les quatre indicateurs sur les huit dernières itérations, les seuils visibles, et la date du calcul.

La consigne de départ peut tenir en quelques lignes :

```text
Écris un script qui calcule, pour les huit dernières itérations, le débit,
le temps de traversée (médiane et 85e centile), le taux de retouche et le coût
complet par story, selon les définitions de docs/mesures.md. Sources : Jira et
GitHub en lecture seule, et l'export de télémétrie. Aucun chiffre par personne.
Range-le dans outils/mesures/ avec un README qui explique chaque calcul.
```

### Le calendrier

| Rythme | Ce qu'on regarde | Où, et qui |
| --- | --- | --- |
| Chaque jour | Les demandes en revue, l'attente avant relecture | Au point quotidien, toute l'équipe |
| Chaque itération | Les quatre indicateurs, le travail du soir, les écarts de spécification | En rétrospective, l'équipe et la Product Owner |
| Chaque mois | L'écart avec la facture AWS, les quotas, les blocages du socle | La DSI et la sécurité |
| Chaque trimestre | Les forfaits du coût complet, les seuils, les indicateurs et les outils inutilisés | L'équipe et le contrôle de gestion |

La revue trimestrielle a aussi pour rôle de retirer. Un indicateur que personne n'a regardé depuis trois mois sort de la grille ; s'il manque un jour, on saura le recalculer.

## Renvois

- M10 — GitHub et Jira : mesurer le flux, prévoir en fourchette
- M11 — Le wiki : la dette de connaissance
- M13 — Bonnes pratiques : les signes d'alerte, la loi de Little
- M14 — Dépannage et coûts : la télémétrie, le coût complet par story, les quotas
- Annexe B — Définitions de « prêt » et de « terminé »

Source, consultée le 24 octobre 2026 : [Loi de Goodhart](https://fr.wikipedia.org/wiki/Loi_de_Goodhart).
