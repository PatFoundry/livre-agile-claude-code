# M6 — Hooks

*Partie II — Le manuel de référence*

## Ce que couvre ce chapitre

Un hook est un programme que l'outil déclenche lui-même, à un moment précis du travail de l'agent : avant une modification, après une commande, à la fin d'une réponse. L'agent ne décide pas de le lancer, ne peut pas l'oublier et ne peut pas le négocier. C'est le troisième étage de la maison, après la consigne du CLAUDE.md (chapitre M3) et le verrou des permissions (chapitre M4) : le contrôle qui examine le contenu de ce que l'agent s'apprête à faire.

Le roman lui donne sa scène la plus dure. Au chapitre 13, une ligne de journalisation approuvée à une heure et demie du matin a écrit pendant vingt-cinq jours les coordonnées réelles de mille trois cent douze assurés dans une plateforme lisible par des centaines de comptes. Mathilde refuse d'ajouter une simple consigne : « Il nous faut quelque chose qui arrête tout le monde. » Le soir même, un hook refuse toute modification qui journalise un objet complet. Au chapitre 16, ce contrôle entre dans le socle imposé à toute la maison.

> **Version de référence.** Claude Code 2.1.301, publiée le 15 octobre 2026, avec la configuration Bedrock du chapitre M1. Les événements et les formats d'échange des hooks évoluent souvent ; la [référence officielle](https://code.claude.com/docs/en/hooks) fait foi.

Un hook s'exécute avec vos droits, hors du bac à sable. C'est ce qui le rend puissant, et c'est pourquoi la fin du chapitre traite de leur gouvernance autant que de leur écriture.

## Un événement, une action certaine

Un hook associe un événement à une action. Quand l'événement survient, l'outil exécute l'action, à chaque fois, quelle que soit la décision de l'agent. C'est ce qui le distingue des deux étages précédents.

|  | Consigne (M3) | Règle de permission (M4) | Hook |
| --- | --- | --- | --- |
| Qui l'applique | L'agent, s'il y pense | L'outil | L'outil |
| Ce qu'elle regarde | Rien : c'est une intention | Le nom de l'outil et la forme de la demande | Tout le contenu de l'action : le code à écrire, la commande complète, le résultat |
| Ce qu'elle peut faire | Orienter | Autoriser, demander, refuser | Refuser avec une explication, ajouter du contexte, agir à côté : formater, journaliser, prévenir |

Au chapitre 13, aucune règle de permission n'aurait suffi : il fallait lire le code que l'agent s'apprêtait à écrire pour y reconnaître une journalisation dangereuse. C'est exactement ce qu'un hook sait faire.

> *Schéma non reproduit dans cette version Markdown : les événements les plus utiles · il en existe une trentaine.*

### Les événements à connaître

L'outil en propose une trentaine. Ceux-ci couvrent l'essentiel des besoins d'une équipe.

| Événement | Quand | Peut-il arrêter ? | Usage typique |
| --- | --- | --- | --- |
| `SessionStart` | Ouverture, reprise, après une compaction | Non | Donner du contexte vivant : la branche, les tickets ouverts |
| `UserPromptSubmit` | Avant que la demande parte vers le modèle | Oui | Refuser une demande qui contient un secret collé par erreur |
| `PreToolUse` | Avant chaque action de l'agent | Oui | Refuser une modification ou une commande dangereuse |
| `PostToolUse` | Après chaque action réussie | Non : l'action a eu lieu | Formater, lancer les tests, journaliser |
| `Stop` | Quand l'agent termine sa réponse | Oui : il reprend le travail | Vérifier que la suite de tests passe avant de rendre la main |
| `Notification` | Quand l'agent attend une réponse | Non | Prévenir sur le bureau |
| `ConfigChange` | Quand un fichier de paramètres change en cours de session | Oui | Tracer ou refuser une modification de configuration |
| `SessionEnd` | Fermeture | Non | Archiver, nettoyer |

### Cinq sortes d'actions

La plupart des hooks lancent une commande, un script qui lit l'événement et répond. Quatre autres formes existent : envoyer l'événement à une adresse web, ce qui convient à un service central de journalisation ; appeler un outil d'un serveur MCP ; demander à un modèle de juger en une question ; ou confier la vérification à un sous-agent, une forme encore expérimentale.

Pour un garde-fou, préférez la commande : elle donne toujours la même réponse au même cas, elle ne coûte rien en jetons, et un auditeur peut la relire. Un jugement par modèle peut compléter, jamais remplacer.

## Écrire un premier hook

Un hook se déclare dans un fichier de paramètres, sous la clé `hooks`, en trois niveaux : l'événement, un filtre qui dit pour quels outils, puis la ou les actions. Celui-ci refuse tout `git push` forcé :

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "if": "Bash(git push *)",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/refuser-push-force.sh",
            "args": []
          }
        ]
      }
    ]
  }
}
```

Le filtre `matcher` retient les commandes du shell ; le champ `if`, écrit comme une règle de permission, ne lance le script que pour un `git push`. `${CLAUDE_PROJECT_DIR}` désigne la racine du projet, d'où que la session ait été lancée. La présence de `args`, même vide, fait lancer le script directement, sans passer par un shell, ce qui évite les soucis de guillemets dans les chemins.

Le script, rangé dans `.claude/hooks/` et rendu exécutable avec `chmod +x` :

```bash
#!/bin/bash
COMMANDE=$(jq -r '.tool_input.command')

if echo "$COMMANDE" | grep -qE -- '--force|--force-with-lease| -f( |$)'; then
  echo "Refusé : pas de push forcé. Ouvrez une demande de fusion." >&2
  exit 2
fi

exit 0
```

### Ce que le script reçoit

L'outil transmet l'événement en JSON sur l'entrée standard. On y trouve toujours l'identifiant de la session, le dossier de travail et le nom de l'événement. Pour une action de l'agent s'ajoutent `tool_name` et `tool_input`, dont le contenu dépend de l'outil :

| Outil | Champs utiles de `tool_input` |
| --- | --- |
| `Bash` | `command` : la commande complète |
| `Edit` | `file_path`, `old_string` (le texte remplacé), `new_string` (le texte qui le remplace) |
| `Write` | `file_path`, `content` (le fichier entier) |

### Ce que le script répond

| Sortie | Effet |
| --- | --- |
| Code 0 | Rien à signaler. L'action suit son cours normal, y compris les demandes d'autorisation : ce n'est pas une approbation. |
| Code 2 | Refus. Le texte écrit sur la sortie d'erreur est transmis à l'agent, qui peut corriger sa copie. |
| Tout autre code | Erreur du hook, signalée mais **non bloquante** : l'action continue. |
| Code 0 et un objet JSON | Contrôle plus fin : refuser, faire demander, ajouter du contexte. |

Le troisième cas est le piège classique : un script qui échoue avec le code 1, l'usage habituel sous Unix, laisse passer l'action. Un garde-fou doit sortir avec le code 2, et se protéger contre ses propres pannes (section sur la gouvernance).

La forme JSON permet par exemple de refuser en expliquant, ou de renvoyer la décision à l'humain :

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "ask",
    "permissionDecisionReason": "Cette commande touche à la base de recette."
  }
}
```

### Où le déclarer

| Emplacement | Portée |
| --- | --- |
| `~/.claude/settings.json` | Vous, dans tous vos projets |
| `.claude/settings.json` | Le projet, pour toute l'équipe une fois versionné |
| `.claude/settings.local.json` | Vous, dans ce projet |
| Paramètres gérés | Tous les postes ; personne ne peut les retirer |
| Un plugin | Ceux qui l'installent (chapitre M8) |
| L'en-tête d'une skill ou d'un sous-agent | Le temps de leur utilisation (chapitre M5) |

Les hooks de tous les niveaux s'additionnent ; quand plusieurs répondent au même événement, ils s'exécutent en parallèle, et le refus l'emporte.

### Vérifier et tester

`/hooks` liste tous les hooks en vigueur, avec leur origine. Pour tester un script sans attendre que l'agent le déclenche, donnez-lui un événement à la main :

```bash
echo '{"tool_name":"Bash","tool_input":{"command":"git push -f origin main"}}' \
  | .claude/hooks/refuser-push-force.sh; echo "code : $?"
```

Le résultat attendu est le message de refus, suivi de `code : 2`. Les modifications des fichiers de paramètres sont prises en compte sans redémarrer la session.

## Formater et vérifier à chaque modification

Le premier usage d'un hook n'a rien de sécuritaire : il évite que l'équipe passe ses relectures à commenter des espaces et des imports. Après chaque modification de fichier par l'agent, un hook `PostToolUse` lance le formateur du projet sur ce fichier.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/formater.sh",
            "args": [],
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
FICHIER=$(jq -r '.tool_input.file_path')

case "$FICHIER" in
  *.java)            google-java-format --replace "$FICHIER" ;;
  *.ts|*.tsx|*.json) npx prettier --write "$FICHIER" ;;
esac

exit 0
```

Le script ne bloque jamais : il sort toujours avec le code 0. Quand il réussit, rien ne s'affiche ; on le constate dans le fichier, reformaté.

### Rendre les erreurs à l'agent

Un hook `PostToolUse` ne peut pas défaire une action, puisqu'elle a déjà eu lieu. Il peut en revanche signaler un problème : s'il sort avec le code 2, son message d'erreur est transmis à l'agent, qui corrige dans la foulée. C'est la bonne place pour un contrôle rapide sur le seul fichier modifié, comme l'analyse statique du projet :

```bash
#!/bin/bash
FICHIER=$(jq -r '.tool_input.file_path')
[[ "$FICHIER" == *.java ]] || exit 0

if ! SORTIE=$(checkstyle -c config/checkstyle.xml "$FICHIER" 2>&1); then
  echo "$SORTIE" >&2
  exit 2
fi
exit 0
```

### Ne pas rendre la main tant que les tests échouent

Un hook `Stop` intervient quand l'agent s'apprête à terminer sa réponse. S'il sort avec le code 2, l'agent reprend le travail avec le message reçu. On s'en sert pour exiger que les tests unitaires passent avant que la main revienne à l'humain.

```bash
#!/bin/bash
ENTREE=$(cat)
# Deuxième passage d'affilée : laisser l'agent s'arrêter.
if [ "$(echo "$ENTREE" | jq -r '.stop_hook_active')" = "true" ]; then
  exit 0
fi

if ! SORTIE=$(mvn -q test 2>&1); then
  echo "Des tests échouent. Corrige-les avant de terminer :" >&2
  echo "$SORTIE" | tail -40 >&2
  exit 2
fi
exit 0
```

La vérification de `stop_hook_active` évite une boucle sans fin : quand l'agent a déjà été relancé une fois par ce hook, on le laisse s'arrêter et rendre compte. L'outil force d'ailleurs l'arrêt après huit relances consécutives.

### Garder la boucle rapide

Un hook bloquant s'exécute à chaque action concernée, et l'agent l'attend. Trois règles :

- **Viser le fichier, pas le projet.** Formater ou analyser un fichier prend une fraction de seconde ; relancer toute la construction à chaque modification ralentit tout.
- **Réserver les contrôles longs à `Stop`.** Les tests passent une fois par réponse, pas après chaque ligne.
- **Lancer en arrière-plan ce qui n'a pas à décider.** Avec `"async": true`, une notification ou un envoi de statistiques s'exécute sans retenir l'agent.

Une limite à garder en tête : `Edit|Write` ne voit que les outils d'édition. Un fichier modifié par une commande du shell, un `sed` par exemple, passe à côté. Pour un contrôle qui doit tout voir, un hook `Stop` peut examiner l'ensemble des fichiers modifiés avec `git status --porcelain`.

## Arrêter les données personnelles et les secrets

C'est le hook du chapitre 13. Il examine le code que l'agent s'apprête à écrire et refuse toute instruction de journalisation qui manipule un objet complet ou un champ de données personnelles. Le refus arrive avant que le fichier soit modifié, et son message dit à l'agent quoi faire à la place.

### Le script

Écrit en Python pour fonctionner à l'identique sur tous les postes :

```python
#!/usr/bin/env python3
import json, re, sys

entree = json.load(sys.stdin)
outil = entree.get("tool_input", {})
if not outil.get("file_path", "").endswith(".java"):
    sys.exit(0)

texte = outil.get("new_string") or outil.get("content") or ""
APPEL = re.compile(r"\b(log|logger)\.(trace|debug|info|warn|error)\(", re.I)
SENSIBLE = re.compile(
    r"\b(declaration|contrat|assure|requete|reponse|nom|prenom|adresse"
    r"|telephone|email|courriel|iban|dateNaissance)\b", re.I)

for ligne in texte.splitlines():
    if APPEL.search(ligne) and SENSIBLE.search(ligne):
        print("Modification refusée : journalisation d'un objet susceptible "
              "de contenir des données personnelles. Journalisez l'identifiant "
              "technique de la déclaration et le code d'erreur.", file=sys.stderr)
        sys.exit(2)

sys.exit(0)
```

Il lit le texte nouveau, `new_string` pour une modification ou `content` pour un fichier entier, et cherche les lignes qui à la fois appellent le journal et nomment un objet ou un champ sensible. Un identifiant technique comme `idDeclaration` passe, puisqu'il ne forme pas le mot `declaration` à lui seul.

Le contrôle est volontairement grossier. Il refuse parfois à tort, et l'agent reformule ; il laisse passer un appel écrit sur plusieurs lignes. C'est acceptable parce qu'il n'est pas seul : au chapitre 13, Mathilde le place entre une consigne et un test de la chaîne d'intégration.

### Le déploiement

Le script est déposé par la DSI à côté du fichier de paramètres gérés, et déclaré dans ce fichier :

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3",
            "args": ["/etc/claude-code/hooks/journaux-sans-donnees.py"],
            "timeout": 10,
            "onFailure": "block"
          }
        ]
      }
    ]
  }
}
```

Deux détails comptent. Un hook des paramètres gérés ne peut être désactivé par aucun réglage du poste ou du projet. Et `onFailure: "block"` transforme toute panne du hook, script introuvable, Python absent, délai dépassé, en refus : un garde-fou qui tombe en panne ne doit pas laisser tout passer.

### Trois niveaux, trois portées

| Niveau | Où | Ce qu'il arrête |
| --- | --- | --- |
| Une consigne | Le CLAUDE.md : jamais de nom, d'adresse, de téléphone, de courriel ni de numéro de contrat dans un journal | L'agent qui la lit et la suit |
| Un hook | Les paramètres gérés | Toute modification faite par l'agent, sur tout poste |
| Un test | La chaîne d'intégration : les journaux des scénarios ne doivent contenir aucune donnée personnelle | Toute demande de fusion, qu'elle vienne d'un humain ou de l'agent (chapitre M10) |

Le troisième niveau est le seul qui arrête Julien. La faille la plus ancienne du chapitre 13, il l'avait écrite lui-même, sans agent, un mardi à 15 heures.

### Les secrets

Le même schéma vaut pour les secrets : un hook `PreToolUse` sur `Edit|Write` qui refuse un texte contenant une clé d'accès, un en-tête de clé privée ou un mot de passe en clair. Plutôt que d'écrire ses propres expressions, branchez-y le détecteur de secrets que la DSI utilise déjà dans la chaîne d'intégration : les deux contrôles parlent alors le même langage.

Un hook `UserPromptSubmit` peut aussi refuser une demande dans laquelle quelqu'un a collé un secret par erreur. Elle ne part pas vers le modèle, mais son texte reste dans l'historique local de la session : ce n'est pas un moyen d'effacer, seulement de ne pas transmettre.

## Bloquer les actions risquées

Le chapitre M4 a posé les interdictions qui se décrivent par un nom d'outil et un chemin. Un hook prend le relais quand la décision dépend d'autre chose : du contenu, de l'état du dépôt, de la branche courante.

| Besoin | Règle de permission | Hook |
| --- | --- | --- |
| Interdire un outil, une commande, un chemin | Oui, et c'est le plus simple | Possible, mais inutile |
| Décider selon le contenu de la modification | Non | Oui |
| Décider selon l'état du dépôt : le fichier existe-t-il, quelle est la branche ? | Non | Oui |
| Expliquer à l'agent comment faire autrement | Message générique | Message libre |
| Tenir quel que soit le mode de l'agent | Oui pour une interdiction | Oui pour un refus |

Un refus de hook tient dans tous les modes, y compris celui qui saute les demandes d'autorisation. En revanche, un hook qui répond « autoriser » ne lève jamais une interdiction posée dans les paramètres.

### Un exemple : les migrations de base

Dans un projet qui versionne son schéma de base de données, une migration déjà appliquée ne se modifie jamais : on en écrit une nouvelle. Aucune règle de permission ne sait l'exprimer, puisqu'il faut autoriser la création d'un fichier et interdire la modification du même chemin. Un hook le fait en quelques lignes :

```bash
#!/bin/bash
FICHIER=$(jq -r '.tool_input.file_path')

case "$FICHIER" in
  */db/migration/V*.sql)
    if [ -e "$FICHIER" ]; then
      echo "Refusé : une migration existante ne se modifie pas. Créez-en une nouvelle." >&2
      exit 2
    fi ;;
esac
exit 0
```

Déclaré sur `PreToolUse` avec le filtre `Edit|Write`, il laisse l'agent créer `V14__ajout_date_decouverte.sql` et l'empêche de retoucher `V13`.

### D'autres cas courants

| Situation | Ce que fait le hook |
| --- | --- |
| Une commande vise la base de recette (`psql`, `sqlplus`) | Renvoie la décision à l'humain, avec `permissionDecision: "ask"` |
| Un commit sur la branche principale | Refuse, et rappelle de créer une branche par story |
| Une suppression récursive hors du dossier de travail | Refuse |
| Un outil MCP qui écrit dans Jira | Renvoie à l'humain, avec le filtre `mcp__jira__.*` (chapitre M7) |
| Une modification en dehors de la zone prévue par le plan | Signale l'écart à l'agent, qui demande avant de continuer |

### Ce qu'un hook ne voit pas

Un hook examine ce que l'agent demande à un outil de faire. Il ne voit pas ce que fait ensuite un programme lancé par cette commande : un script Python qui écrit dans un fichier protégé passe sous son regard. Le bac à sable du chapitre M4 reste la seule protection qui agit au niveau du système.

Le filtre `if` est lui aussi une commodité, pas une frontière : quand l'outil ne sait pas analyser une commande, il lance le hook quoi qu'il arrive. Le script doit donc refaire sa propre vérification, comme ceux de ce chapitre.

## Journaliser : savoir après coup

La troisième question de Bertrand, au chapitre 16, est la plus difficile : comment sait-on, après coup, ce que l'agent a fait ? Plusieurs sources y répondent, chacune pour une part.

| Source | Ce qu'elle trace | Chapitre |
| --- | --- | --- |
| CloudTrail | Chaque appel au modèle : qui, quand, quel modèle | M1 |
| Un hook de journalisation | Chaque action de l'agent sur le poste : quel fichier, quelle commande | M6 |
| L'historique Git et GitHub | Chaque modification fusionnée, son auteur, son approbation | M10 |
| La télémétrie de l'outil | L'usage, les jetons, les coûts, par personne et par équipe | M14 |
| L'historique local des sessions | Toute la conversation, pendant trente jours, sur le poste | M2 |

Le hook comble le trou du milieu : entre l'appel au modèle et la demande de fusion, que s'est-il passé sur le poste ?

### Un journal sobre

Ce hook ajoute une ligne par action de l'agent dans un fichier local, que l'agent de collecte de la DSI envoie à la plateforme de journaux :

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write|Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -c '{date: (now|todate), session: .session_id, outil: .tool_name, fichier: .tool_input.file_path, commande: .tool_input.command}' >> ~/.claude/journal-actions.jsonl",
            "async": true
          }
        ]
      }
    ]
  }
}
```

Il ne retient que le nom de l'outil, le fichier et la commande. Pas le contenu des modifications, pas le résultat des commandes. Ce choix est délibéré : le chapitre 13 commence par une plateforme de journaux remplie de données personnelles. Un journal d'audit qui recopierait tout ce que l'agent lit et écrit deviendrait la prochaine fuite.

L'option `async` fait tourner le hook en arrière-plan : l'agent ne l'attend pas.

### Envoyer directement à un service central

Un hook de type `http` envoie l'événement à une adresse web, sans script. C'est pratique pour un service d'audit commun à toutes les équipes, mais l'événement part en entier, contenu des modifications et résultat des commandes compris : le service qui le reçoit doit filtrer avant de conserver. Dans les paramètres gérés, la clé `allowedHttpHookUrls` limite les adresses que les hooks ont le droit de joindre, et `httpHookAllowedEnvVars` les variables qu'ils peuvent glisser dans leurs en-têtes, un jeton d'accès par exemple.

### Tracer la configuration elle-même

L'événement `ConfigChange` survient quand un fichier de paramètres ou une skill change pendant une session. Un hook peut le consigner, ou refuser la modification en sortant avec le code 2, sauf pour les paramètres gérés, que rien ne bloque. C'est la réponse à la question de Bertrand appliquée à la configuration elle-même : savoir si quelqu'un a desserré les règles en cours de route.

## Gouverner les hooks

Un hook est du code qui s'exécute sur le poste, avec les droits de la personne, hors du bac à sable, à chaque événement. C'est ce qui le rend utile, et c'est ce qui le rend dangereux.

### Le hook d'un dépôt est du code exécuté chez vous

Un `.claude/settings.json` reçu avec un dépôt peut déclarer des hooks. Les hooks des fichiers de paramètres ne demandent pas la même approbation que les autorisations : ils s'appliquent dès qu'un dossier parent a été approuvé, et dans une exécution non interactive avec `claude -p`, même sans approbation. Avant de lancer l'outil dans un dépôt que vous n'avez pas écrit, lisez ses hooks comme vous liriez un script d'installation.

Dans la chaîne d'intégration, où l'outil tourne en mode non interactif sur des branches que n'importe qui peut proposer, trois options neutralisent les hooks du dépôt :

| Option | Effet |
| --- | --- |
| `--setting-sources user` | Ignore les fichiers de paramètres du projet. |
| `--bare` | Ne charge ni hooks, ni skills, ni plugins, ni serveurs MCP du projet. |
| `--settings '{"disableAllHooks": true}'` | Coupe tous les hooks pour cette exécution, sauf ceux des paramètres gérés. |

Le chapitre M10 y revient pour les relectures automatiques sur GitHub.

### Ce que l'entreprise impose

Les hooks des paramètres gérés s'exécutent toujours : aucun réglage du poste ni du projet ne les désactive. C'est là que vivent les garde-fous du socle, comme celui du chapitre 13.

La clé `allowManagedHooksOnly` va plus loin : elle bloque tous les autres hooks, personnels, de projet ou de plugin. Le poste devient prévisible, mais l'équipe perd au passage son formateur et ses contrôles rapides. La voie moyenne consiste à distribuer les hooks utiles dans un plugin que les paramètres gérés activent d'office : ses hooks restent autorisés. C'est ainsi que le socle du chapitre 16 atteint toutes les équipes de la maison (chapitre M8).

### Les pannes

| Situation | Effet par défaut | Parade |
| --- | --- | --- |
| Le script sort avec le code 1 | L'action continue | Sortir avec le code 2 pour refuser |
| Le script est introuvable, ou l'interpréteur absent | L'action continue | `"onFailure": "block"` sur tout hook de sécurité |
| Le hook dépasse son délai | L'action continue ; le délai par défaut est de dix minutes | Un `timeout` explicite, court, et `onFailure: "block"` |
| Une sortie JSON mal formée | Erreur non bloquante | Construire le JSON avec `jq` ou un vrai langage, jamais par concaténation |
| Un profil de shell qui affiche du texte | Le JSON du hook est ignoré | N'afficher du texte que dans les shells interactifs |

Pour voir ce qu'un hook a réellement fait, lancez l'outil avec `claude --debug` : le journal de débogage contient la sortie, les erreurs et le code de retour de chaque hook. Dans une session, Ctrl+O ouvre l'historique détaillé, où apparaissent les refus.

### Avant de déployer un hook de sécurité

1. **Il refuse avec le code 2**, et son message dit à l'agent quoi faire à la place.
2. **Il bloque s'il tombe en panne**, avec `onFailure: "block"` et un délai explicite.
3. **Il a été testé à la main** avec au moins deux événements : un qui passe, un qui est refusé.
4. **Il a des tests à lui**, dans le dépôt du socle, joués par la chaîne d'intégration : c'est du code.
5. **Il a une propriétaire**, Mathilde pour les hooks de sécurité, et change par demande de fusion, comme les skills du chapitre M5.
6. **Il ne journalise rien de sensible** lui-même.

## Dans le roman

| Chapitre | Scène | Ce qu'elle illustre ici |
| --- | --- | --- |
| 13 — Mercredi noir | Mercredi, 9 heures : vingt-cinq jours de coordonnées réelles dans les journaux de recette ; le CLAUDE.md interdisait les secrets dans le code et ne disait rien des journaux. | Une consigne ne couvre que ce à quoi on a pensé. |
| 13 — Mercredi noir | Mercredi, 15 heures : Mathilde refuse « une consigne de plus » et pose trois niveaux ; le hook arrête l'agent net, et l'agent réécrit sa ligne avec l'identifiant de la déclaration. | Le hook de contrôle des journaux, déployé dans les paramètres gérés. |
| 13 — Mercredi noir | Julien écrit à la main une ligne fautive ; le test de la chaîne d'intégration passe au rouge en quatre minutes. | Le niveau qui arrête aussi les humains. |
| 13 — Mercredi noir | Vendredi : six causes, dont quatre antérieures à l'agent ; Bertrand rend les trois niveaux obligatoires pour toute la maison. | Un garde-fou se pense pour tout le monde, pas pour l'agent seul. |
| 16 — La sécurité au quotidien | Mathilde recense les garde-fous ; le socle répond à trois questions : le droit, le verrou, la trace. | Le journal des actions, et des hooks distribués à toutes les équipes. |

Pour aller plus loin : M7 (MCP, et les hooks sur ses outils), M8 (plugins : distribuer les hooks du socle), M10 (GitHub : le contrôle de la chaîne d'intégration), M13 (bonnes pratiques : journaliser sans exposer), M14 (télémétrie et coûts).

## Sources

Consultées le 19 octobre 2026.

- [Automatiser des actions avec les hooks](https://code.claude.com/docs/en/hooks-guide)
- [Référence des hooks : événements, entrées, sorties, codes de retour](https://code.claude.com/docs/en/hooks)
- [Configurer les permissions : hooks et règles](https://code.claude.com/docs/en/permissions#extend-permissions-with-hooks)
- [Ce qui s'exécute avant l'approbation d'un dossier](https://code.claude.com/docs/en/permissions#what-runs-before-you-trust-a-folder)
- [Référence des paramètres : allowManagedHooksOnly, disableAllHooks](https://code.claude.com/docs/en/settings-reference)
- [Exemple de validation de commandes, dépôt officiel](https://github.com/anthropics/claude-code/blob/main/examples/hooks/bash_command_validator_example.py)
