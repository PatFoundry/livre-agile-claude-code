# M14 — Dépannage et coûts

*Partie II — Le manuel de référence*

## Ce que couvre ce chapitre

Ce dernier chapitre du manuel sert quand quelque chose ne va pas : un agent qui refuse de démarrer, une règle qui ne s'applique pas, un connecteur muet, une facture qui surprend. Il propose un ordre de diagnostic, les erreurs les plus fréquentes avec la configuration de référence, la façon de lire la consommation à trois niveaux, le calcul du coût complet d'une story, le choix des modèles, et les limites de débit de Bedrock.

Le roman y touche deux fois. Au chapitre 11, la veille d'une rétrospective tendue, Thomas demande à l'agent de tirer les vrais chiffres du sprint de Jira et de GitHub ; il lui faut dix minutes, et ils contredisent ce que chacun croyait. Au chapitre 26, le contrôle de gestion veut comparer la vélocité de l'équipe à celle d'Horizon ; l'équipe découvre que le coût du modèle pèse peu face au temps humain de chaque erreur, et remplace les points d'effort par quatre indicateurs, dont le coût complet par story.

> **Version de référence.** Claude Code 2.1.301, publiée le 15 octobre 2026, avec la configuration Bedrock du chapitre M1 : région `eu-west-3`, profils d'inférence européens, compte AWS dédié. Les messages d'erreur cités sont ceux de cette version ; ils évoluent, leur logique beaucoup moins.

Une règle traverse tout le chapitre : on diagnostique de bas en haut. Avant de soupçonner l'agent, on vérifie la version, le fournisseur, l'identité, les réglages ; la plupart des pannes s'arrêtent là.

## Dépanner avec méthode

Quand l'outil ne fait pas ce qu'on attend, la tentation est de reformuler la consigne. C'est rarement la bonne piste : la cause se trouve presque toujours dans une couche plus basse, et une même consigne reformulée trois fois ne répare pas une identité AWS expirée.

> *Schéma non reproduit dans cette version Markdown : l'ordre du diagnostic · les trois couches les plus fréquentes en couleur.*

### Ce que l'on regarde à chaque couche

1. **Le poste et la version.** `claude --version` doit afficher la version de référence ; les paramètres gérés refusent de démarrer une version plus ancienne que le minimum fixé (chapitre M1).
2. **Le fournisseur.** `/status` affiche le fournisseur, la région résolue et sa provenance, les modèles en usage. `aws sts get-caller-identity` confirme l'identité AWS, et donc que la session SSO n'a pas expiré.
3. **Les réglages.** `/status` liste aussi les sources de réglages appliquées ; les paramètres gérés doivent y figurer. `/permissions` montre chaque règle et le fichier d'où elle vient ; `/memory` les CLAUDE.md chargés.
4. **Les extensions.** `/hooks`, `/mcp` et l'onglet *Errors* de `/plugin` disent ce qui est en place et ce qui a échoué (chapitres M6 à M8).
5. **Le contexte.** `/context` montre ce qui occupe la place ; une session trop longue explique bien des comportements étranges (chapitre M13).
6. **Le journal.** Lancé avec `claude --debug-file /tmp/claude-debug.log`, ou après `/debug` dans la session, l'outil écrit le détail de ce qu'il a fait : réglages lus, hooks déclenchés et leurs codes de sortie, connexions, erreurs de télémétrie.

### Le bilan automatique

`/doctor` passe en revue l'installation, les erreurs de réglages, les extensions installées mais inutilisées et le CLAUDE.md du projet, et propose des corrections. C'est le premier réflexe quand on ne sait pas par où commencer.

### À qui remonter

| La cause est dans | On s'adresse à | Avec |
| --- | --- | --- |
| Les paramètres gérés, le socle, le compte AWS | La DSI | La sortie de `/status` et l'extrait du journal |
| Les fichiers du dépôt | Le référent technique | Le fichier en cause et le comportement observé |
| L'outil lui-même | L'éditeur, par l'intermédiaire de la DSI | `/feedback`, qui prépare avec un fournisseur tiers une archive expurgée de la session dans `~/.claude/feedback-bundles/` |

Avant de transmettre un journal ou une archive, on le relit : un journal peut contenir des chemins, des noms de serveurs, des extraits de commandes.

## Les erreurs fréquentes

Les tableaux qui suivent rassemblent les pannes les plus courantes avec la configuration de référence. Les pannes propres aux hooks, aux serveurs MCP et aux plugins sont détaillées dans leurs chapitres, M6, M7 et M8.

### Démarrage et version

| Symptôme | Cause probable | Remède |
| --- | --- | --- |
| L'outil refuse de démarrer et cite une version minimale | Le poste a une version plus ancienne que celle exigée par les paramètres gérés | Mettre à jour par le canal de la DSI ; les mises à jour automatiques sont coupées (M1) |
| L'outil refuse de démarrer et cite un fichier de paramètres gérés illisible | Le JSON déployé est invalide | Corriger le fichier ; une seule entrée invalide, elle, est ignorée sans bloquer le reste |
| L'outil refuse de démarrer faute de bac à sable | Sur Linux, `bubblewrap` ou `socat` manque, et `failIfUnavailable` est actif | Installer les deux paquets (M4) |

### Bedrock et identité

| Symptôme | Cause probable | Remède |
| --- | --- | --- |
| *AWS authentication failed*, ou erreur d'identifiants expirés | La session SSO a expiré | `aws sso login --profile <profil>` ; `awsAuthRefresh` peut le faire automatiquement (M1) |
| Des onglets de connexion s'ouvrent en boucle | Un proxy ou un VPN interrompt le parcours SSO dans le navigateur | Retirer `awsAuthRefresh` et se connecter à la main avant de lancer l'outil |
| *AWS default-chain credential resolve timed out* | Une étape de la chaîne d'identifiants attend une saisie qu'elle ne peut pas recevoir | Se connecter avant ; ou relever `CLAUDE_CODE_AWS_CHAIN_RESOLVE_TIMEOUT_MS` |
| `AccessDeniedException` | La politique IAM ne couvre pas l'appel : `InvokeModelWithResponseStream`, les profils d'inférence, ou les deux actions d'abonnement | Comparer avec la politique du chapitre M1 |
| Le modèle n'est pas accessible | Le formulaire d'usage n'a pas été soumis pour ce compte, ou le modèle n'est pas activé | Le soumettre dans la console Bedrock, une fois par compte |
| *on-demand throughput isn't supported* | Un identifiant de modèle nu au lieu d'un profil d'inférence | Utiliser le profil européen, `eu.anthropic.…` |
| Erreur 400 sur un identifiant `eu.` | Le profil européen n'est pas activé dans toutes les régions de son groupe | Vérifier avec `aws bedrock list-inference-profiles --region eu-west-3` |
| *Switched to … because … is not available* | Le modèle a été désactivé en cours de session ; l'outil bascule sur un modèle voisin | Vérifier l'accès au modèle ; ou fixer une chaîne de repli explicite (section sur les modèles) |
| *unable to get local issuer certificate* | Un proxy d'inspection TLS dont le certificat racine n'est pas connu de l'outil | Déclarer le certificat de la maison avec `NODE_EXTRA_CA_CERTS` |

### Réglages et permissions

| Symptôme | Cause probable | Remède |
| --- | --- | --- |
| Un réglage du projet n'a aucun effet | Le dossier n'a pas été approuvé, ou un réglage géré le contredit | Accepter la confiance du dossier ; `/status` et `/permissions` disent quelle source l'emporte |
| Une action est refusée sans demande | Une règle `deny`, souvent issue des paramètres gérés | `/permissions` nomme la règle et son fichier ; une interdiction gérée ne se lève pas localement |
| Une commande échoue sur le réseau | Le bac à sable n'autorise pas cet hôte | Demander l'ajout de l'hôte à la liste gérée (M4) |
| Une variable de télémétrie du dépôt est ignorée | Les variables d'export ne se règlent pas depuis les fichiers du projet | Les placer dans les paramètres gérés (section suivante) |

### Contexte et débit

| Symptôme | Cause probable | Remède |
| --- | --- | --- |
| L'agent oublie une consigne, refait une erreur corrigée | Le contexte est trop chargé | `/clear` et une meilleure consigne de départ (M13) |
| Les réponses ralentissent, puis des erreurs 429 ou *ThrottlingException* | Le quota de débit Bedrock est atteint | L'outil réessaie seul ; si cela persiste, voir la section sur les quotas |
| Les jetons de cache restent à zéro dans `/usage` | Le cache de requêtes n'est pas disponible pour ce modèle ou cette région | Vérifier la disponibilité dans la documentation de Bedrock |
| La skill d'implémentation de BMAD s'arrête net | `uv` est absent du poste | Installer `uv` (M9) |

## Lire la consommation

La consommation se lit à trois niveaux, qui ne répondent pas à la même question.

| Niveau | Question | Outil |
| --- | --- | --- |
| Le poste | Que coûte la session en cours, et pourquoi ? | `/usage`, `/context` |
| L'équipe et la maison | Qui consomme quoi, sur quels modèles, pour quelles tâches ? | La télémétrie de l'outil, exportée vers l'observabilité de la maison |
| La facture | Combien la maison paie-t-elle, et à qui l'imputer ? | Les outils de coût d'AWS, sur le compte dédié du chapitre M1 |

### Sur le poste

Le bloc *Session* de `/usage` donne le coût estimé de la session, le détail des jetons par modèle et une ligne sur le cache de requêtes : la part des jetons d'entrée servie depuis le cache, les ratés, et si le cache est encore chaud. Un taux de cache bas sur une longue session signale souvent des pauses trop longues ou un contexte qui change sans cesse. L'estimation est calculée au prix public, sauf si les paramètres gérés fixent les tarifs de la maison avec `modelPricing`.

Pour comprendre une habitude plutôt qu'une session, `/insights` analyse les sessions récentes du poste et produit un rapport sur les points de friction : demandes mal comprises, corrections répétées. Il consomme lui-même des jetons ; on le lance avant une rétrospective, pas tous les jours.

### Par la télémétrie

L'outil exporte des métriques et des événements au format OpenTelemetry. Avec Bedrock, c'est le seul moyen d'obtenir des chiffres par équipe et par tâche : les tableaux de bord de l'éditeur ne voient pas cette consommation. Ces lignes s'ajoutent au bloc `env` des paramètres gérés du chapitre M4 :

```json
{
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp",
    "OTEL_LOGS_EXPORTER": "otlp",
    "OTEL_EXPORTER_OTLP_PROTOCOL": "grpc",
    "OTEL_EXPORTER_OTLP_ENDPOINT": "https://otel.mutuelle.intra:4317",
    "OTEL_RESOURCE_ATTRIBUTES": "team.id=portail-sinistres,cost_center=IND-042",
    "OTEL_METRICS_INCLUDE_REPOSITORY": "true",
    "OTEL_LOG_TOOL_DETAILS": "1"
  }
}
```

| Donnée | Ce qu'elle donne |
| --- | --- |
| `claude_code.cost.usage` | Le coût estimé, en dollars, par modèle, par équipe, et selon l'origine de la requête : conversation principale, sous-agent ou tâche de fond |
| `claude_code.token.usage` | Les jetons, distingués en entrée, sortie, lecture et écriture du cache |
| L'événement `api_request` | Chaque appel au modèle, avec son coût et ses jetons |
| Les événements `api_error` et `api_retries_exhausted` | Les échecs et les quotas atteints |
| L'événement `tool_result` | Chaque outil utilisé ; avec `OTEL_LOG_TOOL_DETAILS`, la branche et le commit des `git commit` |

Les noms d'agents, de skills, de plugins et de serveurs MCP figurent sur ces données quand `OTEL_LOG_TOOL_DETAILS` est actif : c'est ce que les chapitres M7 et M8 utilisent pour savoir quels connecteurs et quels plugins servent vraiment. La même variable fait apparaître des commandes et des chemins de fichiers ; le collecteur est donc interne, son accès restreint, et la décision revient au RSSI.

Trois réglages restent à leur valeur par défaut, c'est-à-dire désactivés : `OTEL_LOG_USER_PROMPTS`, `OTEL_LOG_ASSISTANT_RESPONSES` et `OTEL_LOG_RAW_API_BODIES`. Ils feraient entrer dans la télémétrie le contenu des conversations, et donc potentiellement des données que le chapitre 13 a appris à tenir à distance.

### Côté AWS

Le compte AWS dédié rend la facture lisible : tout ce que Bedrock y facture vient de l'outil. Les outils de suivi des coûts d'AWS donnent le total par jour et par modèle ; les métriques Bedrock de CloudWatch, le nombre d'appels, de jetons et de rejets pour dépassement de quota.

Pour imputer la dépense à chaque équipe sans dépendre de la télémétrie, on crée un profil d'inférence applicatif par équipe, étiqueté pour l'imputation des coûts, et les paramètres gérés de chaque groupe de postes orientent les modèles vers lui avec `modelOverrides`.

### Rapprocher les deux

La télémétrie estime ; AWS facture. Une fois par mois, on rapproche le total de la télémétrie et la facture du compte dédié. Un écart persistant vient le plus souvent des tarifs : on règle alors `modelPricing` sur la grille Bedrock de la région, pour que les chiffres vus par les équipes correspondent à ce que paie la maison.

## Le coût complet par story

Au chapitre 26, l'équipe abandonne les points d'effort et adopte quatre indicateurs, définis par écrit et calculés sans saisie. Trois viennent du circuit décrit au chapitre M10 ; le quatrième est celui de ce chapitre.

| Indicateur | Définition | Source |
| --- | --- | --- |
| Débit | Stories terminées par semaine | Jira |
| Temps de traversée | De la création du ticket à la fusion | Jira et GitHub |
| Taux de retouche | Part des stories rouvertes ou suivies d'une anomalie reliée | Jira |
| Coût complet par story | Le coût du modèle plus le temps humain passé sur la story | La télémétrie, GitHub, Jira, et des forfaits convenus |

### Le coût du modèle d'une story

Une story laisse deux traces dans la télémétrie. Les sessions de développement ont commité sur sa branche : avec `OTEL_LOG_TOOL_DETAILS`, l'événement `tool_result` de chaque `git commit` porte le nom de la branche, et donc la clé du ticket. Les exécutions de la chaîne d'intégration, comme la prérelecture, reçoivent la clé dans `OTEL_RESOURCE_ATTRIBUTES`, que le workflow tire du nom de la branche. Le coût du modèle d'une story est la somme des événements `api_request` de ces sessions et de ces exécutions.

### Le temps humain, sans feuille de temps

Personne ne saisit ses heures par story, et personne ne le fera. On estime le temps humain à partir de ce que les outils enregistrent déjà, avec des forfaits convenus entre l'équipe et le contrôle de gestion :

| Activité | Ce qu'on compte | Forfait, par exemple |
| --- | --- | --- |
| Préparation | Une story prête | 1 h 30, plus pour une story rouge |
| Relecture | Le nombre de tours de relecture dans GitHub | 30 min par tour, 1 h en rouge |
| Exploration | Une story fusionnée | 30 min, 1 h en rouge |
| Retouche | Le nombre d'anomalies reliées après la fusion | 2 h par anomalie |

Les forfaits sont faux pour chaque story prise isolément, et justes en moyenne. Au chapitre 26, l'équipe vérifie sa reconstitution à la main sur un échantillon de stories avant de s'y fier ; c'est la même vérification qu'on refait chaque trimestre pour ajuster les forfaits.

### Un exemple

Les chiffres sont illustratifs ; l'ordre de grandeur est celui que l'équipe découvre au chapitre 26.

| Poste | Calcul | Montant |
| --- | --- | --- |
| Modèle | Sessions et prérelecture de la branche | 6 € |
| Préparation | 1 h 30 | 120 € |
| Relecture | 2 tours × 30 min | 80 € |
| Exploration | 30 min | 40 € |
| Retouche | 1 anomalie × 2 h | 160 € |
| **Total** | Temps humain à 80 € de l'heure | **406 €** |

Le modèle compte pour moins de 2 % du total. L'anomalie, à elle seule, coûte plus de vingt-cinq fois toutes les sessions de la story. C'est le constat du chapitre 26 : le coût du modèle se révèle négligeable à côté du temps humain que coûte chaque erreur, et la façon la plus sûre de faire baisser le coût complet est de faire baisser la retouche.

### Ce que l'indicateur ne doit pas devenir

Le coût complet par story mesure un système de travail, pas des personnes. On le suit par équipe et dans le temps, jamais par développeur : un relecteur qui demande un deuxième tour sur une story rouge fait monter le coût et baisser le risque. Et l'on compare avec prudence : au chapitre 26, la comparaison avec Horizon, sur un périmètre comparable, n'attribue à l'agent qu'un tiers de l'écart ; le reste tient à l'équipe, à ses pratiques et à son périmètre.

Comme les mesures de flux du chapitre M10, le calcul se confie une fois à l'agent, puis se fige dans un script relu et versionné, qu'on relance à chaque itération.

## Choisir les modèles et l'effort

La configuration de référence met deux modèles à disposition, par leurs profils d'inférence européens : Opus 5.5 et Sonnet 5.5. Les paramètres gérés les figent, et la liste `availableModels` interdit les autres (chapitre M1). Ce figeage a aussi un effet sur la facture : sans lui, l'outil prendrait par défaut le modèle Opus sur Bedrock, au tarif Opus, pour tout le travail.

### Quel modèle pour quel travail

| Travail | Modèle | Effort |
| --- | --- | --- |
| Questions sur le code, exploration | Sonnet | Moyen |
| Implémentation d'une story préparée | Sonnet | Haut |
| Prérelecture dans la chaîne d'intégration | Sonnet | Haut |
| Planification d'une story complexe, architecture, diagnostic difficile | Opus | Haut ou très haut |
| Recherche simple confiée à un sous-agent | Sonnet, ou un modèle plus léger si la DSI l'active | Bas |

Le réflexe recommandé : commencer avec Sonnet, passer à Opus pour planifier, ou quand Sonnet échoue deux fois sur le même problème. `/model` change de modèle en cours de session. L'alias `opusplan` automatise ce partage : Opus en mode plan, Sonnet pour l'exécution. C'est un bon choix par défaut pour une équipe qui planifie chaque story, comme le recommande le chapitre M13.

### L'effort

L'effort règle la profondeur de raisonnement : bas, moyen, haut, très haut, maximal. Les deux modèles de référence raisonnent toujours ; seul le niveau se règle, avec `/effort` en cours de session. Un effort bas suffit à renommer, reformater, répondre à une question simple ; un effort élevé se justifie pour planifier et pour les problèmes que le premier essai n'a pas résolus. Les paramètres gérés peuvent plafonner l'effort de toute la maison avec `maxEffortLevel`.

### Les tâches de fond

L'outil fait aussi de petites requêtes pour lui-même : titres de session, résumés. Sur Bedrock, il utilise pour cela le modèle Sonnet par défaut, faute de savoir si un modèle plus léger est activé. Si la DSI active un modèle Haiku dans le compte et le fixe avec `ANTHROPIC_DEFAULT_HAIKU_MODEL`, ces tâches coûtent moins cher, sans effet sur le travail lui-même.

### Quand un modèle n'est plus disponible

Si l'accès à un modèle est retiré en cours de session, l'outil bascule de lui-même sur une version voisine et le signale. Une chaîne de repli explicite, dans les paramètres, rend ce comportement prévisible :

```json
{
  "fallbackModel": ["sonnet"]
}
```

En cas de surcharge d'Opus, la session continue alors sur Sonnet pour le reste du tour, et revient à Opus au message suivant.

## Quotas et limites sur Bedrock

Bedrock limite le débit de chaque compte, modèle par modèle et région par région : un nombre de jetons et un nombre de requêtes par minute. Une équipe seule les atteint rarement ; un train entier, des agents en parallèle et une chaîne d'intégration qui lance une prérelecture à chaque commit, si.

### Reconnaître un quota atteint

- Dans la session, les réponses ralentissent ; l'outil réessaie seul, avec des délais croissants, après une erreur 429 ou *ThrottlingException*.
- Dans la télémétrie, l'événement `api_retries_exhausted` signale les requêtes abandonnées après plusieurs essais.
- Dans CloudWatch, la métrique des appels rejetés pour dépassement de quota monte, sur le modèle et la région concernés.

La façon dont Bedrock décompte les jetons sur les quotas n'est pas celle de la facture : une requête peut peser sur le quota davantage que ce qu'elle consomme réellement. La documentation de Bedrock sur le décompte des jetons et les quotas en donne les règles.

### Dimensionner

Pour une demande d'augmentation de quota, l'éditeur donne des repères par personne, qui diminuent avec la taille de l'équipe parce que tout le monde ne travaille pas au même moment :

| Taille de l'équipe | Jetons par minute et par personne | Requêtes par minute et par personne |
| --- | --- | --- |
| 5 à 20 personnes | 100 000 à 150 000 | 2,5 à 3,5 |
| 20 à 50 personnes | 50 000 à 75 000 | 1,25 à 1,75 |
| 50 à 100 personnes | 25 000 à 35 000 | 0,62 à 0,87 |

Un train de quarante développeurs vise donc de l'ordre de deux à trois millions de jetons par minute, à répartir entre les modèles selon leur usage. Ces repères valent pour un usage courant ; une formation qui fait travailler trente personnes en même temps, ou un PI Planning où chaque équipe lance ses agents d'analyse, demande davantage.

### Les leviers

| Levier | Effet |
| --- | --- |
| Les profils d'inférence européens | Répartissent les requêtes entre les régions européennes du groupe, au lieu de tout faire peser sur `eu-west-3` |
| Une demande d'augmentation | Dans la console des quotas d'AWS, par modèle et par région, justifiée par l'usage mesuré |
| Les niveaux de service | `ANTHROPIC_BEDROCK_SERVICE_TIER` à `flex` pour les travaux qui peuvent attendre, comme le contrôle hebdomadaire du wiki ; `priority` pour ce qui ne le peut pas, à un tarif plus élevé. Leur disponibilité varie selon le modèle et la région |
| La concurrence dans la chaîne d'intégration | Les groupes de concurrence du chapitre M10 évitent deux prérelectures simultanées sur la même demande de fusion |
| Le contexte court | Une session au contexte chargé envoie de grosses requêtes ; la discipline du chapitre M13 soulage aussi les quotas |

### Une précaution de calendrier

Une augmentation de quota prend du temps. On la demande avant d'élargir l'usage à une nouvelle équipe, et l'on garde une marge pour les jours de forte activité : un quota atteint un matin de démonstration coûte plus cher, en temps humain, que toute la marge d'un mois.

## Dans le roman

| Chapitre | Scène | Ce qu'elle illustre ici |
| --- | --- | --- |
| 11 — Rétro sous tension | La veille de la rétrospective, l'agent tire en dix minutes les vrais chiffres du sprint de Jira et de GitHub : l'attente avant relecture, les anomalies après fusion, la part du travail faite le soir. | Lire ce que les outils enregistrent déjà, plutôt que ce que chacun croit. |
| 26 — La vélocité est morte | La vélocité a culminé avec la retouche ; le coût du modèle pèse peu face au temps humain de chaque erreur ; quatre indicateurs remplacent les points, vérifiés à la main sur un échantillon. | Le coût complet par story ; mesurer un système, pas des personnes. |
| 26 — La vélocité est morte | La comparaison avec Horizon n'attribue à l'agent qu'un tiers de l'écart ; la sponsor refuse de donner une date avant deux itérations mesurées. | Comparer avec prudence ; prévoir à partir de mesures. |

Pour aller plus loin : M1 (configuration Bedrock et figeage des modèles), M4 (paramètres gérés), M6 à M8 (pannes des hooks, des serveurs et des plugins), M10 (mesures de flux), M13 (contexte court, maîtrise des coûts).

## Pour finir

Le manuel s'arrête ici. Les outils de ces quatorze chapitres changeront plus vite que ce livre : les versions citées seront dépassées, des commandes renommées, des réglages remplacés. Ce qui devrait durer, ce sont les gestes qu'ils servent : écrire ce qui compte là où l'agent le lit, verrouiller ce qui doit tenir, relire ce qui entre, et mesurer avant de conclure.

## Sources

Consultées le 23 octobre 2026.

- [Claude Code sur Amazon Bedrock : configuration et dépannage](https://code.claude.com/docs/en/amazon-bedrock)
- [Claude Code : télémétrie OpenTelemetry](https://code.claude.com/docs/en/monitoring-usage)
- [Claude Code : maîtriser les coûts](https://code.claude.com/docs/en/costs)
- [Claude Code : configuration des modèles](https://code.claude.com/docs/en/model-config)
- [Amazon Bedrock : décompte des jetons et quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas-token-burndown.html)
- [Amazon Bedrock : profils d'inférence](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)
- [AWS : supervision de Claude Code avec Amazon Bedrock](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock/blob/main/assets/docs/MONITORING.md)
