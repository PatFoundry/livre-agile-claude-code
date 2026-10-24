# Annexe E — Politique d'usage sécurité

*Annexes*

## À quoi sert cette annexe

Au chapitre 16, la commission sécurité veut que les garde-fous du pilote deviennent la règle de toute la maison. Julien pose une condition avant qu'on écrive une ligne : le socle tiendra en deux pages. Cette annexe en donne la partie lisible par tous, la politique d'usage, telle qu'une direction peut la signer et qu'un nouvel arrivant peut la lire en dix minutes.

Elle complète, sans les répéter, les réglages techniques du manuel. La politique dit ce qui est permis et ce qui ne l'est pas ; les paramètres gérés, les hooks et la chaîne d'intégration le font respecter. Chaque article renvoie donc au contrôle qui le traduit, et un article sans contrôle possible doit au moins désigner qui le vérifie.

> **Un modèle, pas un texte juridique.** Cette politique est écrite pour la mutuelle fictive du roman et pour la configuration de référence. Elle s'adapte avec le RSSI, le délégué à la protection des données et le service juridique, et ne remplace aucun de leurs avis.

Trois choix d'écriture la rendent applicable :

- **Des articles courts**, à l'indicatif : « l'agent ne fusionne pas » plutôt que « il est recommandé de ne pas laisser l'agent fusionner ».
- **Peu d'interdits, tous vérifiables** : une règle qu'on ne peut pas contrôler devient une règle que personne ne respecte.
- **Une responsabilité humaine nommée à chaque étape** : l'outil prépare, une personne répond.

## La politique

### Politique d'usage des agents de développement

**Article 1 — Objet et périmètre.** La présente politique encadre l'usage des agents de développement assistés par l'intelligence artificielle dans le développement des applications de la mutuelle. Elle s'applique à toute personne qui les utilise, collaborateur ou prestataire, sur tout projet, quel que soit l'environnement.

**Article 2 — Outils autorisés.** Seule la configuration fournie par la DSI est autorisée : l'agent installé dans la version de référence, relié au service de modèles du compte cloud dédié, hébergé dans l'Union européenne. Aucun autre service d'intelligence artificielle ne reçoit de code, de document ou de donnée de la mutuelle. Aucun compte personnel n'est utilisé à titre professionnel.

**Article 3 — Données.** Les agents ne travaillent que sur des données synthétiques. Aucune donnée réelle d'adhérent ou d'assuré, aucune donnée de santé, aucun secret n'entre dans un dépôt, une consigne, un connecteur, un wiki ou une conversation avec l'agent. Toute base utilisée par un agent a vu son anonymisation vérifiée par la sécurité. Les journaux produits par le code ne contiennent aucune donnée personnelle.

**Article 4 — Ce que l'agent peut faire.** L'agent lit et modifie le code dans le dépôt où il travaille, exécute les commandes autorisées dans un environnement isolé, et consulte les connecteurs approuvés. Il ne pousse pas sur la branche principale, ne fusionne pas, ne modifie pas les scénarios d'acceptation, n'accède pas à internet hors des hôtes autorisés, et ne fonctionne jamais sans demande d'autorisation.

**Article 5 — Responsabilité humaine.** Tout changement produit avec un agent est relu, approuvé et assumé par une personne. Celle qui fusionne répond du changement comme si elle l'avait écrit, et sait l'expliquer. Toute spécification est approuvée nommément avant l'implémentation.

**Article 6 — Extensions.** Les skills, sous-agents, hooks, plugins et connecteurs partagés proviennent du catalogue interne. Chacun a un propriétaire, une version figée, et a été relu par la sécurité avant publication. L'installation d'une extension extérieure au catalogue est interdite.

**Article 7 — Traçabilité.** Chaque changement porte la clé du ticket qui l'a motivé et indique la contribution d'un agent. On doit pouvoir retracer, en quelques minutes, l'origine de toute ligne de code : la demande, la spécification, la personne qui a approuvé, la relecture. Les actions des agents sont journalisées sans le contenu des échanges.

**Article 8 — Incidents.** Toute personne qui constate qu'un agent a vu un secret ou une donnée réelle, a agi hors du périmètre attendu, ou a été détourné par un contenu qu'il a lu, arrête la session et prévient la sécurité sans délai, selon la fiche réflexe en vigueur. On ne supprime aucune trace avant l'accord de la sécurité.

**Article 9 — Formation.** L'accès aux agents est ouvert après une formation qui couvre cette politique, les limites des agents et la fiche réflexe. Un rappel a lieu à chaque évolution majeure du socle.

**Article 10 — Exceptions.** Une exception se demande par écrit à la sécurité, avec sa raison, son périmètre et sa durée. Elle est accordée pour une durée limitée et inscrite au registre des exceptions.

**Article 11 — Gouvernance.** La commission sécurité adopte et révise la politique. Une responsable du socle et un référent technique en assurent l'application. La politique est revue tous les six mois, et à chaque changement majeur de l'outil ou du cadre réglementaire.

*Adoptée par la commission sécurité le \[date\]. Responsable du socle : \[nom\]. Référent technique : \[nom\].*

## Ce que chaque article devient techniquement

Une politique qu'aucun réglage ne soutient repose sur la bonne volonté. Le tableau suivant relie chaque article aux contrôles décrits dans le manuel. Là où aucun contrôle n'existe, la dernière colonne nomme qui vérifie.

| Article | Contrôles techniques | Vérifié aussi par | Chapitre |
| --- | --- | --- | --- |
| 1 — Périmètre | La télémétrie recense les sessions par équipe | La DSI, chaque mois | M14 |
| 2 — Outils autorisés | Fournisseur imposé, modèles et version figés, mises à jour coupées ; compte cloud dédié dont les règles d'organisation interdisent les régions hors de l'Union ; postes qui ne joignent pas les services d'IA extérieurs | La DSI | M1, M4 |
| 3 — Données | Interdictions de lecture des fichiers de secrets ; lecture bloquée hors des dossiers de travail ; identifiants masqués dans le bac à sable ; hook qui refuse les données personnelles ; test des journaux et détection de secrets dans la chaîne ; transcriptions effacées après quatorze jours ; aucun contenu d'échange dans la télémétrie | La sécurité, pour toute base utilisée par un agent | M4, M6, M7, M10, M12, M14 |
| 4 — Ce que l'agent peut faire | Mode avec demande d'autorisation imposé, modes sans demande désactivés ; scénarios protégés en écriture ; bac à sable avec liste d'hôtes gérée ; lecture web limitée aux hôtes internes ; branche principale protégée | Le référent technique | M4, M10 |
| 5 — Responsabilité humaine | Approbation des propriétaires obligatoire ; contrôle de la ligne *Approuvé par* dans la chaîne | Le relecteur, qui sait expliquer | M10, M13 |
| 6 — Extensions | Catalogues autorisés limités au Git interne ; chargement de plugins hors catalogue refusé ; serveurs MCP limités à la liste gérée ; plugins à commande et modules extérieurs refusés | La sécurité, à chaque publication au catalogue | M7, M8 |
| 7 — Traçabilité | Mention de l'agent dans chaque commit ; clé Jira contrôlée par la chaîne ; journal des actions par hook ; télémétrie | Le test des quatre minutes, chaque trimestre | M6, M10, M14 |
| 8 — Incidents | Journaux et télémétrie conservés ; hook qui signale tout changement de configuration en cours de session | La sécurité | M6, M14 |
| 9 — Formation | Accès ouvert par la DSI après la formation, par groupe d'annuaire | Le responsable de chaque équipe | M12 |
| 10 — Exceptions | Des paramètres gérés propres au groupe concerné, avec une date de fin | Le registre des exceptions, revu par la sécurité | M4 |
| 11 — Gouvernance | Les paramètres gérés et le socle versionnés, modifiés par demande de fusion relue par la sécurité | La commission, tous les six mois | M8 |

### Ce qu'aucun réglage ne garantit

Trois engagements de la politique échappent à tout contrôle automatique, et c'est assumé :

- **Comprendre ce qu'on fusionne** (article 5). Le relecteur est seul juge ; la revue et la rétrospective le soutiennent.
- **Signaler un incident** (article 8). Aucune machine ne remplace la personne qui dit : l'agent vient de lire quelque chose qu'il n'aurait pas dû voir.
- **Ne pas contourner** : copier du code dans un outil non autorisé, depuis un autre poste. Les postes isolés le rendent difficile ; seule la formation, et la confiance, le rendent improbable.

## Ce que la politique demande à chacun

Une politique se lit mieux par rôle que par article. Chacun y trouve ce qu'on attend de lui, et ce qu'on lui garantit en retour.

| Rôle | Ce qu'on attend de lui | Ce qu'on lui garantit |
| --- | --- | --- |
| Développeur, collaborateur ou prestataire | Utiliser la seule configuration fournie ; ne travailler que sur des données synthétiques ; relire et assumer ce qu'il soumet ; signaler tout incident | Un outil dont les verrous le protègent de l'erreur la plus coûteuse ; le droit de s'arrêter et de prévenir sans reproche |
| Relecteur | Ne fusionner que ce qu'il sait expliquer ; relire à la profondeur que demande le risque | Des demandes de fusion préparées, une file plafonnée, le droit de refuser |
| Product Owner | Valider nommément les stories et les règles de gestion ; trancher les questions ouvertes | Un agent qui n'invente pas de règle et lui pose les questions |
| Testeuse | Écrire les scénarios avant le code ; explorer après le vert | Des scénarios que personne d'autre ne peut modifier |
| Référent technique | Tenir le CLAUDE.md, les règles et les hooks du projet ; vérifier l'article 4 | Le soutien de la sécurité pour tout réglage sensible |
| Responsable du socle | Garder le socle court, à jour et appliqué ; tenir le registre des exceptions | Un mandat de la commission, et le dernier mot sur ce qui entre dans le socle |
| DSI | Déployer la configuration, les paramètres gérés et le catalogue ; ouvrir les accès après formation | Une politique qui dit exactement ce qu'il faut verrouiller |
| Sécurité | Relire les extensions, les bases utilisées par un agent, les exceptions ; traiter les incidents | Des journaux et une traçabilité suffisants pour enquêter |
| Délégué à la protection des données | Valider la classification des données et les durées de conservation | Aucune donnée réelle dans les outils des agents |

La deuxième colonne de la première ligne compte plus qu'il n'y paraît. Au chapitre 13, la ligne fautive la plus ancienne avait été écrite à la main, sans agent : chercher un coupable aurait désigné la mauvaise cible, et rien appris. Une politique de sécurité qui punit le signalement obtient le silence.

## La fiche réflexe en cas d'incident

L'article 8 renvoie à une fiche qui doit tenir sur une page, être affichée, et pouvoir être suivie par quelqu'un qui n'a jamais eu d'incident. La voici.

> *Schéma non reproduit dans cette version Markdown : la fiche réflexe · à afficher près des postes.*

### Ce qu'on dit en prévenant

Quoi, quand, sur quel poste, dans quel dépôt et sur quelle branche, avec quelle story ; et ce qui a déjà été fait. Pas d'interprétation, pas de capture contenant la donnée en cause : la sécurité viendra la voir sur place.

### Selon la situation

| Situation | Premiers gestes, en plus des trois communs | Qui d'autre prévenir |
| --- | --- | --- |
| L'agent a lu ou affiché un secret | Considérer le secret comme exposé et le faire changer, même si rien n'est sorti du poste | Le propriétaire du secret |
| L'agent a rencontré une donnée réelle d'assuré | Ne pas pousser la branche ; noter d'où venait la donnée | Le délégué à la protection des données, qui apprécie s'il y a violation au sens du RGPD et les délais qui s'ensuivent |
| L'agent a modifié un fichier hors de son périmètre, ou lancé une commande inattendue | Ne rien pousser ; relever l'état du dépôt avec `git status` | Le référent technique |
| Un contenu lu par l'agent contenait des instructions qui l'ont détourné | Noter la source : ticket, page, fichier, demande de fusion | Le propriétaire de la source |
| Une consommation ou un coût anormal | Ce n'est pas un incident de sécurité : arrêter la session suffit | La DSI |

### Après l'incident

La revue se fait sans recherche de coupable, et se termine par une seule question : à quel niveau empêche-t-on que cela se reproduise ? Une consigne dans le CLAUDE.md, un hook, une interdiction dans les paramètres, un contrôle de la chaîne, ou le socle, selon l'échelle du chapitre M13. Le chapitre 13 du roman en donne la forme : trois niveaux de protection superposés, la consigne, le hook et le contrôle de la chaîne.

## Le cadre réglementaire et la révision

### Les textes qui la fondent

Trois règlements européens au moins pèsent sur une politique de ce type dans une mutuelle. La liste n'est pas exhaustive : le secteur de l'assurance a ses propres autorités et ses propres exigences, que le service juridique ajoute.

| Texte | Ce qu'il demande, pour ce qui nous occupe | Articles de la politique |
| --- | --- | --- |
| Le RGPD | Ne traiter que les données nécessaires ; documenter les traitements ; notifier une violation de données à caractère personnel à l'autorité de contrôle dans les soixante-douze heures quand elle présente un risque | 3, 8 |
| DORA, règlement sur la résilience opérationnelle numérique du secteur financier, applicable depuis janvier 2025 | Gérer le risque lié aux technologies et aux prestataires tiers ; pouvoir retracer et expliquer les changements ; déclarer les incidents majeurs | 2, 7, 8, 11 |
| Le règlement européen sur l'intelligence artificielle, dont l'obligation de maîtrise de l'IA s'applique depuis février 2025 | Que les personnes qui utilisent des systèmes d'IA aient un niveau suffisant de compétence | 9 |

DORA a une conséquence pratique souvent oubliée : le fournisseur de cloud et le service de modèles sont des prestataires tiers de technologies, à inscrire comme tels dans le registre que tient la mutuelle. Au chapitre 22, c'est aussi DORA qui fait choisir à l'équipe le niveau le plus complet de la méthode : il faut pouvoir montrer ce qui a été décidé, et par qui.

### Réviser la politique

La politique est versionnée dans le dépôt du socle, à côté des paramètres gérés qu'elle justifie. Elle change par une demande de fusion relue par la sécurité et, pour les articles qui engagent des droits, par le service juridique. Outre la revue semestrielle de l'article 11, cinq événements déclenchent une révision :

- une version majeure de l'outil ou de son mode de déploiement ;
- un nouveau fournisseur de modèles, ou une nouvelle région ;
- un nouvel usage, comme un agent qui travaille sans personne devant l'écran dans la chaîne d'intégration ;
- un incident significatif ;
- une évolution du cadre réglementaire.

La règle de Julien vaut pour la politique comme pour le socle : si elle ne tient plus en deux pages, c'est qu'elle a commencé à décrire des réglages au lieu de dire ce qui est permis.

## Renvois

- M1 — Installer : la configuration de référence et le compte dédié
- M4 — Paramètres et permissions : les verrous et les paramètres gérés
- M6 — Hooks : données personnelles, secrets, journal des actions
- M7 — MCP : les connecteurs et leurs risques
- M8 — Plugins : le catalogue interne et le socle
- M10 — GitHub et Jira : branche protégée, contrôles obligatoires, traçabilité
- M12 et M13 — Partager en équipe, bonnes pratiques : formation, revue sans reproche
- M14 — Dépannage et coûts : la télémétrie sans contenu
- Annexe A — Modèle de CLAUDE.md ; Annexe B — Définitions de « prêt » et de « terminé »

## Sources

Consultées le 24 octobre 2026.

- [Règlement (UE) 2016/679, règlement général sur la protection des données](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [Règlement (UE) 2022/2554, résilience opérationnelle numérique du secteur financier (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)
- [Règlement (UE) 2024/1689, règlement sur l'intelligence artificielle](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [CNIL, notifier une violation de données personnelles](https://www.cnil.fr/fr/notifier-une-violation-de-donnees-personnelles)
