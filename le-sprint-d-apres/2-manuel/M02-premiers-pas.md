# M2 — Premiers pas

*Partie II — Le manuel de référence*

## Ce que couvre ce chapitre

Ce chapitre apprend à tenir une session de bout en bout : la lancer, décider ce que l'agent peut faire sans demander, lui faire proposer un plan, garder son contexte propre, revenir en arrière quand il se trompe, puis retrouver le fil le lendemain. Il suppose un poste installé et branché selon le chapitre M1.

Il s'adresse à toute l'équipe, pas seulement aux développeurs. Dans le roman, c'est en mode plan que Sofiane fait dresser par l'agent la carte des fichiers que chaque story toucherait (chapitre 8) ; c'est une session neuve qui sert à vérifier qu'une story est prête (chapitres 3 et 6). Une Product Owner ou une testeuse a donc autant besoin de ces gestes qu'un tech lead.

> **Version de référence.** Claude Code 2.1.301, publiée le 15 octobre 2026, avec la configuration Bedrock du chapitre M1. Les raccourcis et les commandes évoluent souvent : en cas d'écart, `/help` dans l'outil et la [documentation officielle](https://code.claude.com/docs/en/interactive-mode) font foi.

Les exemples utilisent le terminal. Dans VS Code, les mêmes fonctions passent par le panneau de l'extension ; les différences notables sont signalées.

## Anatomie d'une session

Une session, c'est une conversation entre vous et l'agent, ancrée dans un dossier. Elle commence quand vous lancez `claude` et se termine quand vous la quittez avec `/exit`, ou en appuyant deux fois sur Ctrl+D. Elle reste enregistrée : vous pourrez la reprendre plus tard (voir « Reprendre ses sessions »).

**Le dossier compte.** Lancez toujours l'outil à la racine du dépôt sur lequel vous travaillez. Ce dossier devient le répertoire de travail : l'agent y lit librement, y cherche et, selon le mode de permission, y modifie des fichiers. Pour lui donner accès à un second dossier, par exemple une bibliothèque partagée, tapez `/add-dir` suivi de son chemin.

**Ce que l'agent voit.** Au démarrage, il lit les fichiers CLAUDE.md du projet et de l'utilisateur (chapitre M3). Ensuite, il ne voit que ce qui entre dans la conversation : vos messages, les fichiers qu'il ouvre, le résultat des commandes qu'il lance et, dans un IDE, le fichier ouvert et le texte sélectionné. Il ne voit ni votre écran, ni vos autres sessions, ni le travail de vos collègues tant qu'il n'est pas dans le dépôt.

**Ce qu'il sait faire.** L'agent agit par des outils. Chacun a sa règle d'autorisation, que le mode de permission ajuste.

| Famille d'outils | Exemples | En mode manuel |
| --- | --- | --- |
| Lire et chercher | Ouvrir un fichier, chercher un mot dans le dépôt, lister des fichiers | Sans demander, dans le répertoire de travail |
| Modifier | Créer un fichier, remplacer un passage | Demande à chaque fois |
| Exécuter | Lancer une commande : compilation, tests, Git | Demande, sauf pour une liste de commandes en lecture seule comme `git status` |
| Lire une page web | Ouvrir une documentation dont vous donnez l'adresse | Demande |
| Déléguer | Confier une recherche à un sous-agent (chapitre M5) | Selon les outils du sous-agent |
| Vous interroger | Poser une question à choix multiple | Attend toujours votre réponse |

**La boucle.** Pour une demande non triviale, l'agent enchaîne quatre temps : il explore le code pour comprendre, il annonce ce qu'il va faire, il agit, puis il vérifie, en général en lançant les tests. S'ils échouent, il recommence le cycle. Votre rôle est d'intervenir au bon moment, sans attendre la fin.

Deux gestes suffisent pour cela. **Échap** interrompt l'agent à tout instant ; il garde le travail déjà fait et attend votre consigne. Et vous pouvez taper un message pendant qu'il travaille : il est mis en file et lui parvient dès que ses outils en cours ont fini, sans interrompre son tour. Reprendre la main tôt coûte toujours moins cher que corriger tard.

## Décider ce que l'agent fait sans demander

Le mode de permission fixe la frontière entre ce que l'agent fait seul et ce qu'il vous soumet. Il s'affiche sous la zone de saisie et change à chaque appui sur **Maj+Tab** : automatique, manuel, accepter les modifications, plan, puis retour au début.

| Mode | Indicateur | Passe sans demander | Pour quoi faire |
| --- | --- | --- | --- |
| Manuel (`default`) | ⏸ manual mode on | Les lectures | Code inconnu, travail sensible, premières semaines |
| Accepter les modifications (`acceptEdits`) | ⏵⏵ accept edits on | Lectures, modifications de fichiers et commandes de fichiers courantes, dans le répertoire de travail | Itérer vite sur une tâche cadrée, puis relire le diff |
| Plan (`plan`) | ⏸ plan mode on | Lectures et exploration ; aucune modification avant votre accord | Comprendre et proposer avant d'agir |
| Automatique (`auto`) | ⏵⏵ auto mode on | Tout, sous le contrôle d'un second modèle qui bloque les actions risquées | Tâches longues dans un cadre déjà maîtrisé |
| Ne pas demander (`dontAsk`) | ⏵⏵ don't ask on | Ce qui est explicitement autorisé ; le reste est refusé | Intégration continue, scripts |
| Contourner (`bypassPermissions`) | ⏵⏵ bypass permissions on | Presque tout | Conteneur ou machine virtuelle isolés, jamais un poste de travail |

**Le mode de départ.** Depuis la version 2.1.283, une session interactive démarre par défaut en mode automatique, y compris sur Bedrock, dès que le modèle le permet : Sonnet 5 ou plus récent, Opus 4.7 ou plus récent. C'est le cas de la configuration de référence. Une équipe qui a promis au RSSI une « validation humaine avant toute commande », comme celle du roman, doit donc imposer le mode manuel par les paramètres gérés, et peut retirer le mode automatique à tous ; le chapitre M4 montre comment. Notez aussi que, sur Bedrock, les vérifications du mode automatique consomment des jetons facturés.

Pour une seule session, choisissez le mode au lancement :

```bash
claude --permission-mode default   # manuel
claude --permission-mode plan
```

### Répondre à une demande d'autorisation

Quand l'agent veut modifier un fichier ou lancer une commande, il affiche l'action exacte et attend. Trois réponses sont possibles.

- **Oui** : l'action s'exécute, une seule fois.
- **Oui, et ne plus demander** : selon l'action, l'outil propose d'autoriser les actions semblables pour la session ou pour le projet. C'est une règle ; vous la retrouvez et la retirez avec `/permissions`.
- **Non** : l'action est refusée. Appuyez sur **Tab** avant de valider pour ajouter un commentaire ; l'agent le lit et ajuste son approche. Échap revient à répondre non, sans commentaire.

Un « non » commenté vaut mieux qu'un « oui » de lassitude. Si vous approuvez sans lire, le mode manuel ne vous protège plus de rien : passez plutôt en mode plan et discutez l'approche avant qu'il agisse.

### Ce qu'aucun mode n'approuve seul

Certaines écritures ne sont jamais approuvées d'office, même en mode accepter les modifications : celles qui visent `.git`, `.claude`, `.vscode`, `.idea` ou les fichiers de configuration du shell comme `.bashrc` et `.zshrc`. En mode manuel ou accepter les modifications, l'outil vous les soumet ; en mode automatique, elles passent obligatoirement par le second modèle. Une suppression qui vise la racine du disque, votre dossier personnel ou le répertoire de travail lui-même vous est toujours soumise, et elle est refusée quand personne ne peut répondre.

Et une règle d'interdiction posée par l'administrateur l'emporte sur tous les modes. C'est la différence entre une consigne et un verrou, que Julien explique à Sofiane au chapitre 3.

## Le mode plan

En mode plan, l'agent lit, explore et propose, mais ne modifie aucun fichier du projet tant que vous n'avez pas approuvé son plan. C'est le geste le plus rentable du manuel : dix minutes de plan relu évitent une heure de code à défaire.

**Y entrer.** Trois façons, au choix :

- appuyez sur Maj+Tab jusqu'à lire *plan mode on* ;
- préfixez une demande par `/plan`, par exemple `/plan ajouter la date de découverte au parcours vol` ;
- lancez la session avec `claude --permission-mode plan`.

**Ce qui se passe.** L'agent ouvre les fichiers utiles, cherche dans le dépôt, peut lancer des commandes de lecture, et vous pose ses questions. Il rédige ensuite un plan, puis vous demande comment continuer :

| Choix | Effet |
| --- | --- |
| Oui, en mode automatique | Le plan est approuvé ; l'agent l'exécute sans vous soumettre chaque action. Si le mode automatique est retiré, ce choix devient « Oui, accepter les modifications ». |
| Oui, en validant les modifications | Le plan est approuvé ; chaque modification vous est soumise. C'est le bon choix pour les premières semaines. |
| Non, continuer à planifier | Vous dites ce qui ne va pas ; l'agent révise son plan. |

Pour corriger le plan vous-même, appuyez sur **Ctrl+G** : il s'ouvre dans votre éditeur de texte, et l'agent travaillera sur la version que vous enregistrez. Dans VS Code, le plan s'ouvre directement comme un document où l'on ajoute des commentaires en marge.

### Relire un plan

Un plan se relit en cinq questions. Si l'une reste sans réponse, choisissez « continuer à planifier ».

1. **Le périmètre** : quels fichiers seront touchés ? Un fichier inattendu dans la liste est le premier signe d'un malentendu.
2. **L'ordre** : les tests viennent-ils avant le code ? Le CLAUDE.md du roman l'exige, et un bon plan le respecte.
3. **Les hypothèses** : l'agent a-t-il supposé une règle métier qu'il aurait dû demander ? C'est ainsi qu'un agent invente une franchise de 150 euros, dans le souvenir de Thomas au chapitre 3.
4. **Les limites** : qu'est-ce que le plan ne fait pas, et est-ce voulu ?
5. **La vérification** : comment l'agent saura-t-il qu'il a fini ? Quels tests, quelle commande ?

### D'autres usages que le code

Le mode plan sert aussi à voir sans toucher. Au chapitre 8, Sofiane donne chacune des dix-huit stories du sprint à l'agent, en mode plan, et lui demande quels fichiers il modifierait. En vingt minutes, l'équipe obtient la carte des dépendances qui montre que onze stories touchent la même zone du code.

C'est aussi le meilleur test de préparation d'une story : la confier à une session neuve, en mode plan. Si l'agent propose un plan complet sans poser de question, la story est prête ; s'il pose des questions, ce sont celles auxquelles la story aurait dû répondre. C'est le « test de la session neuve » qu'invoque Nadia au chapitre 6.

## Les commandes et raccourcis du premier jour

Une vingtaine de gestes couvrent l'essentiel du quotidien. Tapez `/` pour voir toutes les commandes disponibles, et `?` sur une saisie vide pour l'aide des raccourcis. Une commande n'est reconnue qu'au début d'un message.

### Raccourcis clavier

| Touche | Effet |
| --- | --- |
| Échap | Interrompt l'agent ; il garde le travail déjà fait. Ferme aussi une boîte de dialogue. |
| Échap deux fois | Saisie vide : ouvre le menu de retour arrière. Saisie remplie : l'efface, et Flèche haut la rappelle. |
| Maj+Tab | Change de mode de permission. |
| Entrée pendant que l'agent travaille | Met votre message en file ; il lui parvient sans interrompre son tour. |
| `\` puis Entrée, ou Ctrl+J | Passe à la ligne sans envoyer. Maj+Entrée fonctionne dans la plupart des terminaux récents. |
| `@` | Cite un fichier, avec complétion du chemin. |
| `!` en début de saisie | Lance vous-même une commande du shell ; sa sortie entre dans la conversation et l'agent la commente. |
| Ctrl+O | Affiche le détail des actions de l'agent. |
| Ctrl+R | Cherche dans l'historique de vos demandes. |
| Ctrl+B | Passe une commande longue en arrière-plan, par exemple un serveur de développement. |
| Ctrl+G | Ouvre votre saisie, ou le plan proposé, dans votre éditeur de texte. |
| Ctrl+V (Alt+V sous Windows) | Colle une image, par exemple une capture d'écran d'une erreur. |
| Ctrl+C | Interrompt ; sur une saisie vide, un second appui quitte l'outil. |

### Commandes

| Commande | Effet |
| --- | --- |
| `/status` | Version, modèle, fournisseur, région, sources de paramètres. Le premier réflexe en cas de doute. |
| `/model` | Change de modèle, parmi ceux que l'entreprise autorise. |
| `/plan [tâche]` | Passe en mode plan, et démarre la tâche si vous la donnez. |
| `/permissions` | Liste les règles d'autorisation et permet d'en retirer. |
| `/context` | Montre ce qui remplit la mémoire de travail de l'agent. |
| `/compact [consigne]` | Résume la conversation pour libérer de la place. |
| `/clear` | Démarre une conversation vierge ; l'ancienne reste reprenable. |
| `/rewind` | Revient en arrière dans le code et la conversation. |
| `/resume` | Reprend une session . |
| `/rename` | Donne un nom à la session en cours. |
| `/diff` | Montre les changements en cours dans le répertoire de travail. |
| `/btw question` | Pose une question annexe sans l'ajouter à la conversation. |
| `/usage` | Jetons consommés et coût de la session (alias `/cost`). |
| `/init`, `/memory` | Crée un premier CLAUDE.md, puis l'édite (chapitre M3). |
| `/code-review` | Fait relire le diff en cours par l'agent, à la recherche d'erreurs. |
| `/doctor` | Diagnostique l'installation et la configuration. |
| `/exit` | Quitte la session. |

Certaines commandes de la documentation n'apparaissent pas avec Bedrock, parce qu'elles exigent un compte chez l'éditeur : `/login`, `/logout`, `/remote-control` ou `/voice`, par exemple. Leur absence n'est pas une panne.

## Garder un contexte propre

Le contexte est la mémoire de travail de l'agent : tout ce qu'il sait de la session, renvoyé au modèle à chaque message. Il contient vos demandes, ses réponses, les fichiers qu'il a lus, la sortie des commandes, et ce qui se charge avant même votre premier mot : les fichiers CLAUDE.md, la description des skills disponibles, le nom des outils connectés.

Avec la configuration de référence, la fenêtre atteint un million de jetons : Sonnet 5.5 et Opus 5.5 l'ont par défaut sur Bedrock. C'est beaucoup, mais ce n'est pas gratuit. Chaque message renvoie tout le contexte, et une vieille conversation encombre l'attention de l'agent au moment où il a besoin des fichiers de la tâche suivante. Un contexte propre coûte moins cher et donne de meilleures réponses.

**Voir ce qui le remplit.** `/context` affiche une grille de l'occupation, par catégorie, avec des suggestions. Ce sont presque toujours les lectures de fichiers qui pèsent le plus ; une demande précise (« corrige la validation dans `DeclarationService` ») fait lire moins de fichiers qu'une demande vague.

**Les cinq gestes.**

| Situation | Geste |
| --- | --- |
| Vous passez à une tâche sans rapport | `/clear` : conversation vierge ; l'ancienne reste reprenable. |
| La tâche continue, mais l'historique s'alourdit | `/compact` avec une consigne, par exemple `/compact garde la règle de franchise et la liste des fichiers modifiés`. |
| Un long débogage est terminé, mais le début de la conversation compte | `/rewind`, choisir le message, puis *Summarize from here* : seule la fin est résumée. |
| Il faut fouiller une large partie du code | Demander à l'agent de confier la recherche à un sous-agent : ses lectures restent dans son propre contexte, seul son résumé revient (chapitre M5). |
| Une question annexe vous traverse l'esprit | `/btw` : la réponse n'entre pas dans la conversation. |

Une règle simple suffit dans la plupart des équipes : une story, une session. C'est le prolongement naturel de la règle du roman, « une story = une branche = une demande de fusion ».

### Ce que la compaction garde, et ce qu'elle perd

Quand la fenêtre approche de sa limite, l'outil compacte automatiquement : il remplace la conversation par un résumé structuré. La session continue, mais tout n'y survit pas de la même façon.

| Contenu | Après compaction |
| --- | --- |
| CLAUDE.md du projet et règles générales | Relus sur le disque, intacts |
| Le plan approuvé en mode plan | Réinjecté tel quel |
| Fichiers lus ou modifiés | Les cinq modifiés le plus récemment sont relus |
| Règles liées à un dossier, CLAUDE.md des sous-dossiers | Rechargés quand l'agent retouche les fichiers concernés |
| Vos consignes données en cours de conversation | Résumées avec le reste : elles peuvent perdre leurs nuances |
| Sorties de commandes, raisonnements intermédiaires | Remplacés par le résumé |

La cinquième ligne du tableau mérite une règle d'équipe. Une consigne importante, donnée une fois dans la conversation (« ne touche pas à l'adaptateur contrats »), peut s'effacer à la première compaction. Si elle compte, elle va dans le CLAUDE.md ou dans les paramètres, pas dans le fil de la discussion.

## Revenir en arrière

Avant chaque message qui lance un tour de travail, l'outil prend une photo des fichiers. Si l'agent part dans une mauvaise direction, vous revenez à l'une de ces photos en quelques secondes, sans Git.

**Ouvrir le menu.** Appuyez deux fois sur Échap quand la zone de saisie est vide, ou tapez `/rewind`. La liste de vos messages s'affiche ; choisissez le point de retour, puis l'action :

| Option du menu | Effet |
| --- | --- |
| *Restore code and conversation* | Fichiers et conversation reviennent à ce point. |
| *Restore conversation* | La conversation revient à ce point ; les fichiers restent tels quels. |
| *Restore code* | Les fichiers reviennent à ce point ; la conversation garde la trace de ce qui s'est passé. |
| *Summarize from here* | Résume la conversation à partir de ce point, pour libérer du contexte. |
| *Summarize up to here* | Résume tout ce qui précède ce point et garde la suite intacte. |
| *Never mind* | Revient à la liste sans rien changer. |

*Restore code* seul est souvent le plus utile : l'agent revient au code d'avant, mais il se souvient de l'impasse et ne la reprendra pas. Après un retour de conversation, votre ancien message réapparaît dans la zone de saisie : corrigez-le, puis renvoyez-le.

Les points de restauration sont enregistrés avec la session : on peut encore revenir en arrière après l'avoir reprise le lendemain. L'outil garde les cent derniers par session, et les efface environ trente jours après la dernière activité.

### Ce que le retour arrière ne rattrape pas

Le retour arrière ne suit que les fichiers que l'agent modifie avec ses outils d'édition. Tout le reste lui échappe :

- les fichiers modifiés par une commande du shell : `rm`, `mv`, `cp`, un générateur de code, un script de migration ;
- la plupart des modifications faites par un sous-agent ;
- vos propres modifications, et celles d'une autre session ouverte en parallèle ;
- tout ce qui sort du disque : une migration appliquée à une base de données, un ticket Jira créé, un commit poussé, un message envoyé.

C'est pourquoi le retour arrière ne remplace pas Git ; il le complète. Avant de lancer l'agent sur une tâche risquée, faites un commit, ou au moins vérifiez que le répertoire de travail est propre avec `git status`. Dans le roman, la branche principale est verrouillée et toute modification passe par une demande de fusion relue : c'est le filet qui rattrape ce que le retour arrière laisse passer.

## Reprendre ses sessions

Chaque session est enregistrée en continu sur votre poste, avec son historique, ses points de restauration et le modèle utilisé. Vous pouvez la reprendre après l'avoir quittée, après un `/clear` ou après un redémarrage.

| Pour | Commande |
| --- | --- |
| Reprendre la dernière session du dossier | `claude --continue` |
| Choisir dans la liste des sessions | `claude --resume`, ou `/resume` depuis une session |
| Reprendre une session nommée | `claude --resume sin-42` |
| Nommer la session dès le lancement | `claude -n sin-42` |
| Nommer la session en cours | `/rename sin-42` |
| Essayer une autre piste sans perdre celle-ci | `/branch`, qui copie la conversation et vous fait basculer dans la copie |
| Garder une trace lisible | `/export compte-rendu.txt` |

**Nommez vos sessions comme vos branches.** Avec la clé Jira dans le nom, `sin-42` par exemple, la session se retrouve sans effort, et le lien entre la story, la branche et la conversation reste évident. Sans nom, l'outil donne un titre tiré de votre premier message, ou du plan une fois approuvé.

**Dans la liste des sessions**, Espace affiche un aperçu, Ctrl+R renomme, et la saisie de quelques lettres filtre la liste ; on peut même y coller l'adresse d'une demande de fusion pour retrouver la session qui l'a produite. Par défaut, seules les sessions du dossier courant apparaissent ; Ctrl+A les montre toutes.

**Ce qui revient, ce qui ne revient pas.** La conversation et le modèle sont restaurés, ainsi que le mode de permission dans la plupart des cas. Les dossiers ajoutés avec `/add-dir` ne le sont pas, ni les commandes lancées en arrière-plan : le serveur de développement est à relancer.

**Conservation.** Les sessions sont gardées trente jours par défaut, dans `~/.claude/projects/`. Le paramètre `cleanupPeriodDays` change cette durée ; une politique de sécurité peut la raccourcir, puisque ces fichiers contiennent tout ce que l'agent a lu.

### Plusieurs sessions à la fois

Rien n'empêche d'ouvrir deux terminaux sur le même dépôt, comme Sofiane au chapitre 6. Mais deux agents qui modifient les mêmes fichiers au même moment se marchent dessus, et le retour arrière de l'un ignore les changements de l'autre. Pour travailler en parallèle, donnez à chaque session sa propre copie isolée du dépôt, sur sa propre branche : c'est l'objet du chapitre M5. Et n'ouvrez jamais la même session dans deux terminaux : leurs messages se mélangeraient dans un seul historique.

Le chapitre 8 rappelle la limite de l'exercice : les copies isolées protègent les agents les uns des autres, pas le produit. Le découpage du travail reste votre affaire.

## Exercice : une première story de bout en bout

Cet exercice enchaîne tous les gestes du chapitre sur une petite story, celle du numéro de téléphone que Martine réclame au chapitre 6. Comptez une heure la première fois. Adaptez les commandes de compilation et de test à votre projet.

1. **Partir d'un état propre.** Créez la branche de la story et vérifiez qu'il ne traîne aucune modification :

   ```bash
   git switch -c SIN-42-telephone
   git status
   aws sso login --profile claude-bedrock
   ```
2. **Lancer une session nommée, en mode plan.**

   ```bash
   claude -n sin-42 --permission-mode plan
   ```
3. **Donner la story, ses critères et la méthode.** Citez avec `@` le fichier que vous savez concerné ; l'agent trouvera les autres.

   ```text
   Story SIN-42 : en tant que déclarant, je saisis un numéro de
   téléphone pour que le gestionnaire puisse me rappeler.
   Critères d'acceptation :
   - 10 chiffres commençant par 0, ou +33 suivi de 9 chiffres ;
   - espaces et points acceptés à la saisie, retirés à l'enregistrement ;
   - champ facultatif ; message d'erreur en français si le format est faux.
   Voir @src/main/java/fr/mdf/sinistres/declaration/Declaration.java
   Propose un plan. Commence par les tests.
   ```
4. **Relire le plan avec les cinq questions** de la section « Le mode plan ». Répondez à ses questions ; s'il manque quelque chose, choisissez « continuer à planifier » et dites quoi.
5. **Approuver en validant les modifications une à une.** Lisez chaque diff. Refusez au moins une fois avec Tab et un commentaire, pour voir l'agent ajuster sa proposition.
6. **Vérifier vous-même.** Lancez les tests avec le préfixe `!`, par exemple `! mvn test` ; l'agent lit le résultat et le commente. Puis `/diff` pour l'ensemble des changements.
7. **Revenir en arrière une fois, exprès.** Échap deux fois, choisissez votre message de l'étape 3, puis *Restore code*. Constatez avec `git status` que les fichiers sont revenus à leur état de départ, puis demandez à l'agent de refaire les modifications : il se souvient du plan et du travail fait.
8. **Faire relire.** Tapez `/code-review` : l'agent relit le diff à la recherche d'erreurs. Corrigez ce qui doit l'être.
9. **Commiter et pousser.** Demandez à l'agent un commit dont le message commence par la clé `SIN-42`, puis le push ; il vous soumet chaque commande. La demande de fusion s'ouvre ensuite selon les règles du chapitre M10.
10. **Clore.** Notez le coût avec `/usage`, puis `/exit`. Demain, `claude --resume sin-42` vous ramènera exactement là.

Si l'agent vous a posé plus de deux questions à l'étape 4, la story n'était pas prête : c'est une information pour la Product Owner, pas un échec de l'exercice.

## Dans le roman

| Chapitre | Scène | Ce qu'elle illustre ici |
| --- | --- | --- |
| 3 — Le fichier qui parle à la machine | Mercredi, 15 heures : dans une session neuve, l'agent propose un plan qui commence par les tests, puis pose trois questions au lieu d'inventer trois règles. | Le mode plan, et la session neuve comme test de préparation. |
| 6 — Trop facile | Mardi et mercredi : Sofiane ouvre deux terminaux côte à côte, deux sessions, deux stories. | Plusieurs sessions à la fois, et leurs limites. |
| 6 — Trop facile | Mercredi, 18 heures : les huit stories suivantes ont « passé le test de la session neuve ». | Une story est prête quand une session neuve la planifie sans question. |
| 8 — Quatre agents à la fois | Mercredi, 18 heures : en mode plan, l'agent dit pour chaque story quels fichiers il toucherait. | Le mode plan pour voir sans toucher : la carte des dépendances. |
| 8 — Quatre agents à la fois | Mardi, 14 heures : un agent résout un conflit en gardant deux champs pour un même concept. | Pourquoi on relit ce que l'agent propose, même quand tout compile. |

Pour aller plus loin : M3 (CLAUDE.md et la mémoire), M4 (paramètres et permissions, dont le mode de départ imposé), M5 (sous-agents et copies isolées du dépôt), M13 (bonnes pratiques).

## Sources

Consultées le 16 octobre 2026.

- [Mode interactif : raccourcis et saisie](https://code.claude.com/docs/en/interactive-mode)
- [Modes de permission](https://code.claude.com/docs/en/permission-modes)
- [Référence des commandes](https://code.claude.com/docs/en/commands)
- [Fenêtre de contexte et compaction](https://code.claude.com/docs/en/context-window)
- [Points de restauration](https://code.claude.com/docs/en/checkpointing)
- [Gestion des sessions](https://code.claude.com/docs/en/sessions)
- [Notes de version de Claude Code](https://code.claude.com/docs/en/changelog)
