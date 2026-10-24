# Annexe F — Glossaire

*Annexes*

## Comment lire ce glossaire

Le livre parle trois langues à la fois : celle de l'assurance, celle de l'agilité, celle des agents. Ce glossaire les rassemble, en six familles, et donne pour chaque terme une définition courte et l'endroit du livre où il compte le plus.

Les renvois suivent une convention simple : un numéro seul désigne un chapitre du roman, par exemple *17* ; un numéro précédé de M désigne un chapitre du manuel, par exemple *M11* ; une lettre désigne une annexe.

Quand le livre traduit un terme anglais d'usage courant, le terme anglais figure entre parenthèses, pour qu'on le reconnaisse dans la documentation des outils. Quelques mots sont restés en anglais parce que la profession les emploie ainsi : *story*, *skill*, *hook*, *plugin*, *sprint*.

Les définitions sont celles du livre, pas celles d'un dictionnaire. Elles disent ce que le terme veut dire *ici*, dans une mutuelle qui travaille avec des agents de développement.

## Le métier de l'assurance

| Terme | Définition | Où |
| --- | --- | --- |
| Adresse du risque | L'adresse du bien assuré. À ne pas confondre avec l'adresse de correspondance de l'assuré : c'est la première anomalie de production du portail | 24 ; A |
| Assuré | La personne couverte par le contrat. Elle n'est pas forcément le souscripteur, ni le déclarant | M3 ; A |
| Avenant | Une modification du contrat, qui prend effet à une date donnée. Deux programmes anciens appliquent cette date différemment depuis 2011 | 17 ; M11 |
| COBOL | Le langage dans lequel est écrit le système des contrats, sur l'ordinateur central de la mutuelle | 17 ; M11 |
| Déclarant | La personne qui remplit la déclaration de sinistre. Elle n'est pas forcément l'assuré | M3 ; A |
| Déclaration de sinistre | La démarche par laquelle on signale un dommage à l'assureur ; le portail du roman la met en ligne | 1 ; C |
| Franchise | La part du dommage qui reste à la charge de l'assuré. Jamais codée en dur : toujours lue dans le contrat | M3 ; A |
| Gestion documentaire | Le système qui conserve les pièces jointes des dossiers, distinct du système des contrats | C |
| Gestionnaire | La personne qui instruit le dossier de sinistre et décide. Une déclaration n'est jamais rejetée automatiquement : le gestionnaire tranche | 22 ; A |
| Mutuelle | La société d'assurance à but non lucratif, appartenant à ses adhérents, où se déroule le roman | 1 |
| Plafond | Le montant maximal que l'assureur prend en charge pour un sinistre. Comme la franchise, il se lit dans le contrat | M3 ; A |
| Sinistre | L'événement qui cause le dommage couvert : dégât des eaux, bris de glace, incendie | 1 |
| Souscripteur | La personne qui a signé le contrat et en paie la cotisation | M3 |
| Système des contrats | Le système ancien, sur ordinateur central, qui tient les contrats et leurs avenants. Le portail l'interroge sans jamais le contourner | 17, 24 ; M11 |

## L'agilité et le pilotage

| Terme | Définition | Où |
| --- | --- | --- |
| Débit | Le nombre de stories terminées par semaine. Avec le taux de retouche, il remplace la vélocité | 26 ; M10, D |
| Définition de « prêt » (*Definition of Ready*) | Les conditions qu'une story remplit avant d'entrer dans une itération | 10 ; B |
| Définition de « terminé » (*Definition of Done*) | Les conditions qu'une story remplit avant d'être considérée comme finie | B |
| Demande de fusion (*pull request*) | La proposition d'intégrer une branche à la branche principale, qui porte la relecture et les contrôles | 9 ; M10 |
| Epic | Un ensemble de stories qui forment un résultat cohérent, livré en plusieurs itérations | 23 ; M9 |
| Itération, sprint | La période fixe au terme de laquelle l'équipe livre un incrément | 1 |
| Loi de Little | À débit égal, le temps d'attente est proportionnel au nombre d'éléments en cours. D'où la limite du travail en cours | 9 ; M13 |
| PI Planning | La séance de planification commune à toutes les équipes d'un train, en début d'incrément de programme | 22 |
| Prévision en fourchette | Une estimation de date donnée avec ses probabilités, calculée sur le débit observé plutôt que sur des estimations | 27 ; M10, D |
| Product Owner | La personne qui porte le besoin, priorise et valide les stories. Dans le roman, Nadia | B, C |
| Registre des dettes | La liste des faiblesses qui ne se corrigent pas en une story : connaissance, vérification, outillage, sécurité | 17 ; M13 |
| Rétrospective | La réunion de fin d'itération où l'équipe examine sa façon de travailler. Celle de fin de phase décide de la suite | 11, 20 ; M13 |
| Story | Un besoin formulé du point de vue de l'utilisateur, assez petit pour tenir en une itération et, avec un agent, en une session | M13 ; C |
| Story autoportante | Une story qui se comprend sans aucun autre document ouvert : exigences, décisions, système existant, scénarios, hors-périmètre | 27 ; C |
| Taux de retouche | La part des stories rouvertes, ou suivies d'une anomalie, dans les trente jours qui suivent la fusion | 26 ; D |
| Temps de traversée | La durée entre la création du ticket et la fusion de la story | 26 ; D |
| Train (*Agile Release Train*) | Le groupe d'équipes qui planifient et livrent ensemble, au rythme commun du cadre SAFe. Ici, le train Indemnisation | 22 ; M12 |
| Travail en cours, limite du | Le nombre maximal d'éléments à une étape. Ici, six demandes de fusion en revue au plus | 9 ; M13 |
| Vélocité | Le nombre de points d'effort livrés par itération. Avec des agents, elle dit de moins en moins le temps qu'il faudra | 26 ; M13, D |

## L'agent et ses outils

| Terme | Définition | Où |
| --- | --- | --- |
| Agent de développement | Un modèle de langage qui lit le code, exécute des commandes et modifie des fichiers pour accomplir une tâche, sous le contrôle d'une personne | M1, M2 |
| Bac à sable (*sandbox*) | L'isolement imposé aux commandes de l'agent : fichiers et hôtes réseau accessibles limités par le système | M4 |
| Catalogue interne (*marketplace*) | Le dépôt qui liste les plugins approuvés par la maison et d'où les postes les installent | 16 ; M8 |
| CLAUDE.md | Le fichier de consignes que l'agent lit au début de chaque session : vocabulaire, principes, façon de travailler | 3 ; M3, A |
| CLAUDE.local.md | Les consignes personnelles d'un développeur pour un projet, jamais versionnées | M3, M12 |
| Compaction | Le résumé automatique d'une conversation devenue trop longue, pour libérer du contexte | M2, M13 |
| Connecteur (serveur MCP) | Un programme qui donne à l'agent accès à un autre système, comme Jira, selon le protocole MCP | 11, 25 ; M7 |
| Contexte | Tout ce que l'agent a sous les yeux dans une session : consignes, messages, fichiers lus, sorties de commandes. La ressource la plus précieuse | M2, M13 |
| Copie isolée (*worktree*) | Une copie de travail séparée du dépôt, qui permet à plusieurs agents de travailler en parallèle sans se gêner | 8 ; M5 |
| Effort | Le réglage de la profondeur de raisonnement du modèle, de bas à maximal | M14 |
| Hook | Une action exécutée à coup sûr à un moment précis du travail de l'agent : avant une commande, après une modification, en fin de tour | 13 ; M6 |
| Mémoire automatique | Les notes que l'agent tient lui-même d'une session à l'autre, sur le poste | M3 |
| Mode plan | Le mode où l'agent lit et propose un plan sans rien modifier | M2, M13 |
| Paramètres gérés | Les réglages déployés par la DSI sur tous les postes, qu'aucun réglage local ne peut lever | M4 |
| Permission, règle de | Une règle qui autorise, fait demander ou interdit une action de l'agent | M4 |
| Plugin | Un paquet installable qui réunit skills, sous-agents, hooks et connecteurs | 16, 18 ; M8 |
| Prérelecture | La préparation de la relecture par un agent qui n'a pas écrit le code ; il prépare, il ne signe pas | 9 ; M5, M10 |
| Profil d'inférence | L'identifiant qui achemine les appels au modèle vers un groupe de régions, ici européennes | M1, M14 |
| Règle par chemin | Une consigne de `.claude/rules/` qui ne se charge que lorsque l'agent touche certains fichiers | M3, A |
| Session | Une conversation de travail avec l'agent, avec son propre contexte | M2 |
| Skill | Un savoir-faire écrit, que l'agent charge quand il en a besoin ou qu'on appelle par son nom | 18 ; M5 |
| Socle | L'ensemble des garde-fous communs à toute la maison : consignes, verrous, contrôles, livrés ensemble par la DSI | 16 ; M8, E |
| Sous-agent | Un agent lancé par l'agent principal, avec son propre contexte et ses propres outils, pour une tâche délimitée | M5 |
| Télémétrie | Les métriques et événements que l'outil exporte vers l'observabilité de la maison | M14 |
| Transcription | L'enregistrement complet d'une session, conservé en clair sur le poste, puis effacé | M12 |

## La méthode et la connaissance

| Terme | Définition | Où |
| --- | --- | --- |
| Architecture, décision d' | Une décision technique écrite sous une forme fixe : contexte, décision, alternatives écartées, conséquences, et le nom de qui décide | 24 ; M11 |
| BMAD | Une méthode libre qui installe dans l'agent des rôles (analyste, chef de produit, architecte, développeuse) et des déroulés de l'idée au code relu | 20 à 27 ; M9 |
| Brief produit | Le document d'analyse qui dit quel problème on résout, pour qui, et ce que le produit ne fera pas | 22 ; M9 |
| Contrôle de cohérence | L'opération qui cherche dans le wiki les contradictions, les affirmations périmées et les notions sans page | 17 ; M11 |
| Gherkin | La syntaxe des scénarios d'acceptation, en phrases du type *Étant donné, Quand, Alors*, lisibles et exécutables | 10 ; C |
| Hors-périmètre | La rubrique d'une story qui dit ce qu'elle ne fera pas. Née avec l'analyste du chapitre 22 | 22 ; C |
| Ingestion | L'opération qui fait entrer une source dans le wiki : résumé, mise à jour des pages touchées, contradictions signalées | 17 ; M11 |
| Partie figée | La part d'une spécification que l'humain a décidée et que l'agent ne modifie plus après approbation | M9 ; C |
| PRD (*Product Requirements Document*) | Le document d'exigences d'un produit ou d'une phase, que plusieurs personnes doivent approuver | 23 ; M9 |
| Scénario d'acceptation | Un exemple exécutable de ce que la story doit faire, écrit avant le code par la recette et le métier, que l'agent ne modifie jamais | 10 ; M13, C |
| Schéma du wiki | Le fichier de consignes qui dit à l'agent comment le wiki est organisé et ce qu'il fait à chaque opération | M11 ; A |
| Sources brutes | Les documents d'origine que le wiki résume sans jamais les modifier : programmes, documents, entretiens | 17 ; M11 |
| Spécification d'implémentation | Le document rédigé par l'agent au début d'une story, approuvé par une personne : questions, fichiers, démarche, vérification, hors-périmètre | M9, M13 ; C |
| Tests de caractérisation | Des tests qui enregistrent ce que fait réellement un système ancien, pour vérifier que le nouveau fait pareil | 24 ; M11 |
| Wiki d'équipe (*LLM Wiki*) | Un ensemble de pages courtes et reliées, compilé et tenu à jour par l'agent à partir des sources, sur le modèle d'Andrej Karpathy | 17 ; M11 |

## La sécurité, la conformité et les coûts

| Terme | Définition | Où |
| --- | --- | --- |
| Branche protégée | La règle qui interdit de modifier la branche principale sans demande de fusion approuvée et contrôles verts | M10 |
| Commission sécurité | L'instance qui adopte la politique d'usage et valide le socle | 16 ; E |
| Contrôle obligatoire | Un contrôle de la chaîne d'intégration sans lequel une demande de fusion ne peut pas être fusionnée. Il est toujours déterministe | 13 ; M10 |
| Coût complet par story | Le coût du modèle plus le temps humain passé sur la story, estimé par forfaits | 26 ; M14, D |
| Données synthétiques | Des données fabriquées pour les tests, qui ressemblent aux vraies sans concerner personne. Les seules que les agents utilisent | 13 ; E |
| DORA | Le règlement européen sur la résilience opérationnelle numérique du secteur financier | 22 ; E |
| Fichier des propriétaires (*CODEOWNERS*) | Le fichier qui dit qui doit approuver une modification, selon les fichiers touchés | M10 |
| Fiche réflexe | Les six gestes à suivre en cas d'incident : arrêter, ne rien effacer, prévenir, contenir, comprendre, apprendre | E |
| Injection d'instructions | Un texte, lu par l'agent dans un ticket, une page ou un fichier, qui tente de lui donner des ordres | 3 ; M7 |
| Jeton (*token*) | L'unité dans laquelle se comptent le texte envoyé au modèle et celui qu'il produit, et donc le coût | M14 |
| Quota | La limite de débit que le fournisseur de modèles applique par compte, par modèle et par région | M14 |
| Registre des exceptions | La liste des dérogations accordées à la politique, chacune avec sa raison, son périmètre et sa date de fin | E |
| Règle des trois (*lethal trifecta*) | Le danger qui naît quand une même session réunit des données sensibles, un contenu non fiable et un moyen de faire sortir l'information | M7 |
| RGPD | Le règlement général sur la protection des données personnelles | 13 ; E |
| RSSI | Le responsable de la sécurité des systèmes d'information. Dans le roman, Bertrand | E |
| Test des quatre minutes | La vérification qu'on peut retracer l'origine d'une ligne de code, de sa demande à sa relecture, en moins de quatre minutes | 16 ; M10 |
| Traçabilité | La capacité à relier chaque changement à son ticket, sa spécification, son approbation et sa relecture | 16 ; M10, E |

## Les personnages et les organisations

Tous les personnages et toutes les organisations du roman sont fictifs. Les agents de la méthode BMAD portent les prénoms que leur donne la méthode elle-même.

### L'équipe et ses proches

| Nom | Rôle | Où on le voit surtout |
| --- | --- | --- |
| Thomas | Directeur de projet, narrateur du roman | Tout le roman |
| Julien | Tech lead ; relecteur principal, puis référent technique du socle | 9, 16, 24 |
| Sofiane | Développeur ; il empaquette les savoir-faire de l'équipe et présente la méthode BMAD | 16, 18, 20 |
| Nadia Benali | Product Owner ; propriétaire du vocabulaire métier et des stories | 18, 22, 25 |
| Émilie | Testeuse ; elle fait des scénarios l'entrée de l'agent, puis forme les testeurs d'Horizon | 10, 22, 27 |
| Gérard | Le dernier expert du système des contrats en COBOL | 17, 24 |
| Sabine | Gestionnaire de sinistres, interrogée par l'analyste avec Nadia | 22 |

### La sécurité et la direction

| Nom | Rôle | Où on le voit surtout |
| --- | --- | --- |
| Bertrand | Responsable de la sécurité des systèmes d'information | 16 |
| Mathilde | Auditrice sécurité ; elle met l'agent à l'épreuve, puis devient responsable du socle | 3, 16, 22 |
| La directrice générale | Elle veut que les garde-fous du pilote deviennent la règle de toute la maison | 16 |
| La sponsor | Elle porte le projet devant le comité, et y présente une prévision en fourchette | 26, 27 |

### Les organisations

| Nom | Ce que c'est | Où |
| --- | --- | --- |
| La mutuelle | L'assureur où se déroule le roman | Tout le roman |
| Le train Indemnisation | Le groupe d'équipes qui livrent ensemble, auquel le portail appartient en phase 2 | 22, 25 |
| Horizon | Le prestataire dont une équipe rejoint le programme en janvier, avec le même socle | 16, 17, 26 |
| La DSI | La direction des systèmes d'information : postes, paramètres gérés, catalogue, compte cloud | M1, M4, M8 |
| Le contrôle de gestion | Il demande la vélocité, et obtient quatre indicateurs | 26 |
| Le bureau des projets | Il veut tout dans Jira ; la règle « une information, un seul endroit » lui donne sa part | 25 |

### Les agents de la méthode BMAD

| Prénom | Rôle | Où |
| --- | --- | --- |
| Mary | L'analyste : recherche, brief produit | 22 ; M9 |
| John | Le chef de produit : PRD, epics et stories | 23 ; M9 |
| Sally | La designer d'expérience | M9 |
| Winston | L'architecte | 24 ; M9 |
| Amelia | La développeuse : implémentation, relecture, rétrospective | M9 |
