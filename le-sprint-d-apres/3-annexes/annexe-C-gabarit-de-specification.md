# Annexe C — Gabarit de spécification

*Annexes*

## À quoi sert cette annexe

Au chapitre 27, une testeuse qui vient d'arriver comprend une story le matin même : le fichier porte ses exigences, ses décisions, ce que fait le système existant, ses scénarios et son hors-périmètre. Personne n'a eu à le lui expliquer. C'est ce que le roman appelle une story autoportante, et c'est ce que cette annexe propose de reproduire.

Une story bien spécifiée tient en trois documents, qui n'ont ni le même auteur ni le même moment :

| Document | Ce qu'il dit | Qui en répond | Où il vit |
| --- | --- | --- | --- |
| Le fichier de story | Ce qu'il faut faire, et pourquoi | La Product Owner | `docs/stories/SIN-57.md` |
| Les scénarios d'acceptation | Comment on saura que c'est fait | La recette et le métier | `src/test/resources/scenarios/sin-57.feature` |
| La spécification d'implémentation | Comment on va le faire | Le développeur, qui l'approuve | `_bmad-output/implementation-artifacts/spec-sin-57.md` |

Les deux premiers existent avant le code ; ils sont la définition de « prêt » de l'annexe B. Le troisième naît au moment où l'agent commence, en mode plan ou par la skill d'implémentation du chapitre M9, et devient la trace de ce qui a été décidé.

Les trois gabarits qui suivent sont remplis avec une même story fictive, SIN-57 : permettre au déclarant de joindre jusqu'à dix photos à sa déclaration. Les crochets indiquent ce qu'on remplace ; le reste est la structure à garder.

Un principe vient du chapitre 25 : **une information, un seul endroit.** Le statut de la story vit dans Jira, pas dans le fichier ; la règle de gestion détaillée vit dans le wiki, et la story y renvoie.

## Le fichier de story

C'est le document du métier. L'agent peut le rédiger à partir d'un entretien, comme l'analyste du chapitre 22 ; la Product Owner le corrige et le valide. Il se lit sans aucun autre document ouvert.

```markdown
---
cle: SIN-57
titre: Joindre plusieurs photos à une déclaration
risque: orange                # vert, orange ou rouge
proprietaire: Nadia Benali
valide-par:                   # rempli par la Product Owner, et elle seule
---

# SIN-57 — Joindre plusieurs photos à une déclaration

## Intention
Le déclarant peut joindre jusqu'à dix photos à sa déclaration, pour que le
gestionnaire dispose des éléments visuels sans avoir à relancer l'assuré.

## Pour qui, et pourquoi
- Déclarant : il ne peut joindre qu'une photo ; les autres arrivent plus tard,
  par courrier ou par messagerie.
- Gestionnaire : [part des relances qui portent sur des photos manquantes,
  fournie par la Product Owner].

## Critères d'acceptation
1. Le déclarant peut joindre de zéro à dix photos.
2. Formats acceptés : JPEG, PNG et HEIC ; 10 Mo au plus par photo.
3. Au-delà de dix, l'ajout est refusé par un message qui donne la limite.
4. Une photo refusée n'empêche jamais l'envoi de la déclaration.
5. Le gestionnaire voit les photos dans l'ordre où elles ont été ajoutées.

## Exigences non fonctionnelles
- Aucune photo, aucun nom de fichier dans les journaux : l'identifiant technique
  du dossier seulement.
- Les données de localisation contenues dans les photos sont retirées avant stockage.

## Ce que fait le système existant
- Les pièces jointes sont stockées par la gestion documentaire, pas par le système
  des contrats : voir wiki/pages/notions/piece-jointe.md.
- La limite actuelle d'une photo vient de l'ancien formulaire, pas d'une règle
  de gestion (Gérard, séance 6).

## Décisions
| Décision | Qui | Quand |
| --- | --- | --- |
| Dix photos au plus : au-delà, le gestionnaire missionne un expert | Nadia | [date] |
| Format HEIC accepté : la plupart des photos viennent d'un téléphone | Nadia, Julien | [date] |

## Questions ouvertes
| Question | Qui peut répondre | Pour quand | Bloquante |
| --- | --- | --- | --- |
| Durée de conservation des photos d'une déclaration abandonnée | Le délégué à la protection des données | [date] | Non : la règle actuelle s'applique d'ici là |

## Hors périmètre
- Les vidéos : une story distincte, après mesure de l'usage des photos.
- La retouche ou le recadrage des photos dans le portail.
- Toute analyse automatique du contenu des photos.

## Vérification
- Scénarios : src/test/resources/scenarios/sin-57.feature (Émilie)
- Données de test : tests/donnees/photos/ (jeu synthétique)

## Dépendances
- SIN-41, stockage des pièces jointes dans la gestion documentaire : terminée.
```

### Ce que chaque rubrique apporte

- **L'en-tête** porte la clé, le niveau de risque et la propriétaire. Il ne porte pas le statut, qui vit dans Jira. Le champ `valide-par` n'est rempli que par la Product Owner ; la chaîne d'intégration peut vérifier qu'il l'est, comme pour la spécification (chapitre M10).
- **L'intention** dit ce qui doit être vrai à la fin, en une ou deux phrases. Si elle n'y tient pas, la story est trop grosse.
- **Les critères d'acceptation** sont numérotés, pour que les scénarios et la relecture puissent y renvoyer.
- **Ce que fait le système existant** cite le wiki et ses sources, au lieu de les recopier.
- **Les décisions** gardent le nom et la date : c'est ce qui permettra, au chapitre 16, de retracer une ligne de code jusqu'à celui qui l'a voulue.
- **Les questions ouvertes** disent si elles bloquent. Une question bloquante sans réponse renvoie la story en préparation.
- **Le hors-périmètre** est la rubrique que l'analyste du chapitre 22 a fait naître : *ce que le portail ne fera pas*. C'est souvent la plus utile à l'agent, qui sinon complète par générosité.

## Les scénarios d'acceptation

C'est le document de la recette. Au chapitre 10, Émilie réécrit ses cas de test sous une forme que la chaîne peut exécuter ; ils deviennent l'entrée de l'agent au lieu d'arriver après lui. La syntaxe Gherkin, en français, se lit comme une phrase et s'exécute comme un test.

```gherkin
# language: fr
# Story : SIN-57 — Joindre plusieurs photos à une déclaration
# Rédigés par Émilie (recette), relus par Nadia Benali

Fonctionnalité: Joindre des photos à une déclaration de sinistre

  Contexte:
    Étant donné un déclarant connecté avec le contrat de test "HAB-SYNTH-001"
    Et une déclaration de dégât des eaux en cours de saisie

  # Critère 1
  Scénario: Le déclarant joint dix photos
    Quand il joint 10 photos au format JPEG de 2 Mo chacune
    Alors la déclaration compte 10 photos
    Et il peut envoyer sa déclaration

  # Critère 3
  Scénario: Une onzième photo est refusée
    Étant donné une déclaration qui compte déjà 10 photos
    Quand il joint une photo de plus
    Alors l'ajout est refusé
    Et le message indique "10 photos au maximum"

  # Critères 2 et 4
  Plan du scénario: Une photo refusée ne bloque pas la déclaration
    Quand il joint le fichier "<fichier>"
    Alors le fichier est refusé pour la raison "<raison>"
    Et il peut envoyer sa déclaration

    Exemples:
      | fichier          | raison                    |
      | facture.pdf      | format non accepté        |
      | photo-24mo.jpg   | taille supérieure à 10 Mo |

  # Critère 5
  Scénario: Le gestionnaire voit les photos dans l'ordre d'ajout
    Étant donné une déclaration envoyée avec les photos "a.jpg", "b.jpg" et "c.jpg"
    Quand le gestionnaire ouvre le dossier
    Alors il voit les photos dans l'ordre "a.jpg", "b.jpg", "c.jpg"

  # Exigence non fonctionnelle
  Scénario: Les noms des photos n'apparaissent pas dans les journaux
    Quand il joint 3 photos et envoie sa déclaration
    Alors aucun journal ne contient le nom d'une photo
```

### Les règles d'écriture

- **Un scénario par critère**, au moins, avec le numéro du critère en commentaire : la relecture vérifie en un coup d'œil que rien n'est oublié.
- **Des comportements observables**, jamais l'implémentation : « l'ajout est refusé », pas « la méthode renvoie une erreur 413 ».
- **Des données synthétiques nommées**, comme le contrat `HAB-SYNTH-001`, tirées de `tests/donnees/` ; jamais un vrai dossier (chapitre 13).
- **Les cas limites explicites** : la dixième photo passe, la onzième non. C'est là que se cachent les écarts.
- **Écrits avant le code, et rouges d'abord** : l'agent les lance, constate qu'ils échouent, puis les fait passer sans les modifier (chapitre M13).

L'agent peut proposer des scénarios supplémentaires, dans une demande de fusion que la recette relit. Il ne modifie jamais un scénario existant : l'interdiction d'écriture du chapitre M4 et le fichier des propriétaires du chapitre M10 y veillent.

## La spécification d'implémentation

C'est le document du développeur. L'agent le rédige au début de la story, en mode plan ou par la skill d'implémentation de BMAD (chapitre M9) ; le développeur le corrige et l'approuve avant toute ligne de code. Ses rubriques sont les cinq du plan du chapitre M13, complétées de deux registres qui se remplissent pendant le travail.

```markdown
---
story: SIN-57
statut: en relecture     # brouillon, prête, en cours, en relecture, terminée
---

# Spécification — SIN-57

Approuvé par :           # rempli par une personne, jamais par l'agent

<!-- Partie figée après approbation : l'agent ne la modifie plus. -->
## Intention
Reprise de l'intention et des critères 1 à 5 de docs/stories/SIN-57.md.

## Ce que je n'ai pas compris
| Question | Réponse | Qui |
| --- | --- | --- |
| Une photo HEIC est-elle convertie au stockage ? | Non : stockée telle quelle, convertie à l'affichage | Julien |
| Le retrait de la localisation vaut-il pour les PNG ? | Oui, pour tous les formats | Nadia |
<!-- Fin de la partie figée. -->

## Fichiers touchés
- src/main/java/…/declaration/PiecesJointesService.java : limite et formats
- src/main/java/…/declaration/NettoyageMetadonnees.java : nouveau, retrait de la localisation
- src/main/resources/static/declaration/photos.js : ajout de plusieurs photos à l'écran
- src/main/resources/db/migration/V31__ordre_pieces_jointes.sql : colonne d'ordre

## Démarche
1. Lancer les scénarios de sin-57.feature : ils doivent échouer.
2. Limite et formats dans le service, puis à l'écran.
3. Retrait des métadonnées avant l'envoi à la gestion documentaire.
4. Colonne d'ordre, puis affichage côté gestionnaire.

## Vérification
- Les scénarios de sin-57.feature passent tous ; la sortie est jointe.
- Tests unitaires : 9, 10 et 11 photos ; chaque format ; 10 Mo et au-delà ;
  retrait de la localisation sur JPEG, PNG et HEIC.

## Hors périmètre
- Vidéos, retouche, analyse du contenu : exclues par la story.
- Aucune modification d'adaptateur-contrats.

## Écarts au plan
- [Aucun, ou : l'écart, sa raison, et qui l'a accepté]

## Journal de relecture
| Point soulevé | Retenu | Raison |
| --- | --- | --- |
| Aucune limite de taille totale pour dix photos | Non | Dix fois 10 Mo reste sous la limite de la gestion documentaire |
| Le message cite « 10 » en dur | Oui | Lu désormais depuis la configuration |
```

### Ce que chaque rubrique apporte

- **La ligne *Approuvé par*** est celle que vérifie le contrôle de la chaîne d'intégration du chapitre M10 : une spécification ajoutée sans nom ne peut pas être fusionnée.
- **La partie figée** reprend le mécanisme de BMAD décrit au chapitre M9 : ce que l'humain a décidé, l'agent ne le réécrit plus. Les réponses aux questions en font partie ; ce sont elles qui évitent l'erreur du chapitre 17.
- **Les fichiers touchés et le hors-périmètre** donnent au relecteur sa première question : qu'est-ce qui a bougé hors du plan ?
- **Les écarts au plan** se remplissent pendant l'implémentation. Une rubrique vide est une bonne nouvelle ; une rubrique absente, une alerte.
- **Le journal de relecture** garde chaque point de la prérelecture, retenu ou écarté, avec sa raison. Une fiche triée se relit ; une fiche ignorée ne laisse aucune trace.

La spécification est commitée avec le code, dans la même demande de fusion. Le relecteur lit d'abord l'intention figée et les réponses ; si elles sont fausses, le code n'a pas d'importance.

## Qui écrit quoi, et quand

Les trois documents ne naissent pas au même moment. Les deux premiers se préparent pendant l'affinage, avant l'itération ; la spécification naît le jour où l'on prend la story. Entre les deux passe la porte de l'annexe B.

> *Schéma non reproduit dans cette version Markdown : les six étapes d'une story · l'approbation humaine est la seconde porte.*

Au chapitre 27, les étapes 4 à 6 tiennent dans une journée. C'est possible parce que les étapes 1 à 3 ont été faites avant, sans précipitation.

### Qui peut modifier quoi, ensuite

| Document | Modifiable par | À quel moment |
| --- | --- | --- |
| Le fichier de story | La Product Owner, ou l'agent avec son accord | Jusqu'à l'approbation de la spécification ; ensuite, un changement de besoin devient une nouvelle story ou une décision datée |
| Les scénarios | La recette et le métier, jamais l'agent | À tout moment, par demande de fusion ; un scénario modifié pendant la story se signale au développeur |
| La partie figée de la spécification | Personne, une fois approuvée | Un changement d'intention repasse par une nouvelle approbation |
| Le reste de la spécification | L'agent et le développeur | Pendant l'implémentation : écarts au plan, journal de relecture |

Une fois la story fusionnée, les trois documents restent dans le dépôt, à côté du code. Ce sont eux qu'on relit quand, des mois plus tard, quelqu'un demande pourquoi le portail refuse la onzième photo.

## Bien remplir

Un gabarit bien structuré peut encore être mal rempli. Les formulations suivantes reviennent souvent, chez les humains comme chez l'agent ; la colonne de droite dit ce qu'on gagne à les reprendre.

### Dans le fichier de story

| À éviter | À préférer | Pourquoi |
| --- | --- | --- |
| « Améliorer la gestion des photos » | « Le déclarant peut joindre jusqu'à dix photos à sa déclaration » | Une intention se vérifie, une amélioration non |
| « Le système doit être rapide » | « L'envoi de dix photos de 2 Mo se termine en moins de \[n\] secondes sur la connexion de référence » | Une exigence non fonctionnelle sans seuil ne se teste pas |
| « On a décidé dix photos » | « Dix photos au plus : au-delà, le gestionnaire missionne un expert — Nadia, \[date\] » | Une décision sans nom ni raison se rediscute à chaque itération |
| « Voir le programme COBOL » | Un lien vers la page du wiki, qui cite le programme et ses lignes | Le lecteur, humain ou agent, n'a pas à refaire l'enquête |
| Pas de rubrique *Hors périmètre* | La liste de ce que la story ne fera pas | L'agent complète ce qu'on ne lui interdit pas |

### Dans les scénarios

| À éviter | À préférer | Pourquoi |
| --- | --- | --- |
| « Quand il clique sur le bouton btn-ajout » | « Quand il joint une photo » | Le scénario décrit un comportement, pas un écran ; il survit à une refonte |
| « Étant donné l'assuré M. Martin » | « Étant donné un déclarant avec le contrat de test HAB-SYNTH-001 » | Pas de nom qui ressemble à une vraie personne ; des données synthétiques nommées |
| « Alors ça fonctionne » | « Alors la déclaration compte 10 photos » | Un résultat observable, qu'un programme peut comparer |
| Un seul scénario « cas nominal » | Le cas nominal et ses limites : dix passe, onze non | Les écarts se cachent aux limites |

### Dans la spécification

| À éviter | À préférer | Pourquoi |
| --- | --- | --- |
| « Je suppose que le HEIC est converti » | La question, dans *Ce que je n'ai pas compris*, avec qui peut répondre | Une hypothèse écrite comme un fait est l'erreur du chapitre 17 |
| « Fichiers touchés : divers » | Chaque fichier, et pourquoi lui | Le relecteur repère d'un coup d'œil ce qui sort du plan |
| « Points de relecture corrigés » | Chaque point, retenu ou écarté, avec sa raison | Le tri se relit ; une mention vague ne prouve rien |
| Une ligne *Approuvé par* remplie par l'agent | Le nom écrit par la personne qui approuve | Une approbation que l'agent s'accorde n'en est pas une |

## Renvois

- M3 — CLAUDE.md : la règle « ne jamais inventer une règle de gestion »
- M4 — Paramètres : l'interdiction d'écriture sur les scénarios
- M9 — BMAD : la spécification de la skill d'implémentation, sa partie figée
- M10 — GitHub et Jira : le contrôle de la ligne *Approuvé par*, le fichier des propriétaires
- M11 — Le wiki : où vit ce que fait le système existant
- M13 — Bonnes pratiques : le plan en cinq rubriques, les tests d'abord
- Annexe A — Modèle de CLAUDE.md
- Annexe B — Définitions de « prêt » et de « terminé »

Source, consultée le 23 octobre 2026 : [Cucumber, les mots-clés Gherkin par langue](https://cucumber.io/docs/gherkin/languages/), pour la syntaxe française des scénarios.
