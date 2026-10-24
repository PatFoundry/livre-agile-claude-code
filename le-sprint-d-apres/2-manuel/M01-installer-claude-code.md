# M1 — Installer Claude Code

*Partie II — Le manuel de référence*

## Ce que couvre ce chapitre

Ce chapitre vous mène d'un poste vierge à une première session Claude Code qui passe par Amazon Bedrock, en région européenne, sans abonnement chez l'éditeur. C'est la configuration que l'équipe du portail sinistres adopte au chapitre 2 du roman, et celle que le reste du manuel suppose.

Il a deux lecteurs. L'administrateur cloud prépare une fois pour toutes le compte AWS, les droits et la connexion par l'annuaire (section « La configuration de référence »). Le développeur installe l'outil sur son poste, le branche et vérifie qu'il fonctionne (toutes les autres sections). Dans une petite équipe, c'est souvent la même personne ; lisez alors le chapitre dans l'ordre.

> **Version de référence.** Claude Code 2.1.301, publiée le 15 octobre 2026. Les commandes, les noms de variables et les identifiants de modèles changent vite. La version en ligne de ce manuel est mise à jour à chaque évolution notable ; en cas d'écart, la [documentation officielle](https://code.claude.com/docs/en/setup) fait foi.

Ce chapitre met en œuvre les deux premiers points du cadre d'usage que Thomas et Julien présentent au RSSI : les modèles via Bedrock sur un compte dédié, puis la connexion par l'annuaire avec des versions figées. Les règles imposées sur chaque poste (secrets, commandes réseau, validation humaine) relèvent du chapitre M4.

## Choisir sa surface

Avec Amazon Bedrock, trois surfaces fonctionnent sans réserve : le terminal, l'extension VS Code et le plugin JetBrains. Le même moteur tourne derrière chacune ; elles partagent la configuration rangée dans le dossier `~/.claude/` de l'utilisateur.

| Surface | Ce que c'est | Avec la configuration de référence |
| --- | --- | --- |
| Terminal | La commande `claude`, lancée dans le dossier du projet. Toutes les fonctions y sont. | Oui. C'est la surface de référence de ce manuel. |
| Extension VS Code | Un panneau graphique dans l'éditeur : diffs côte à côte, plans annotables, historique des sessions. Elle s'installe aussi dans Cursor et les autres dérivés de VS Code. | Oui, après avoir coché le réglage *Disable Login Prompt*. L'extension embarque sa propre copie de l'outil. |
| Plugin JetBrains | Pour IntelliJ IDEA, PyCharm, WebStorm, GoLand et les autres IDE de l'éditeur. Il lance `claude` dans le terminal intégré et affiche les diffs dans l'IDE. | Oui. Il n'embarque rien : il faut installer l'outil en ligne de commande d'abord, et il en hérite la configuration. |
| Application de bureau | L'onglet *Code* de l'application Claude, sans terminal. | Seulement avec l'édition dédiée aux fournisseurs tiers (*Claude Desktop on 3P*). L'application standard exige un abonnement. |
| Web et mobile | Des sessions qui tournent sur l'infrastructure de l'éditeur, pilotables depuis un navigateur ou un téléphone. | Non. Elles exigent un compte claude.ai et exécutent votre code hors de chez vous. |

Dans une équipe Java comme celle du roman, le choix se fait souvent par l'IDE : IntelliJ pour les développeurs, VS Code pour les profils qui touchent surtout aux spécifications et aux tests. Installez l'outil en ligne de commande sur tous les postes de toute façon : c'est lui que vous utiliserez pour diagnostiquer un problème.

Passer par Bedrock retire aussi quelques fonctions, qui reposent sur les serveurs de l'éditeur : la recherche web (l'outil qui lit une page à partir d'une adresse précise reste disponible), les sessions dans le cloud, le contrôle à distance depuis un téléphone, l'extension Chrome et la dictée vocale. Pour un RSSI, chaque fonction absente est une porte de sortie en moins ; c'est l'argument que Julien avance au chapitre 2.

## Préparer le poste

Un poste de développeur récent convient presque toujours ; le point qui bloque, en entreprise, c'est le réseau.

| Élément | Minimum requis |
| --- | --- |
| Système | macOS 13 ; Windows 10 1809 ou Windows Server 2019 ; Ubuntu 20.04, Debian 10 ou Alpine 3.19 |
| Matériel | 4 Go de mémoire, processeur x64 ou ARM64 |
| Shell | Bash, Zsh, PowerShell ou CMD |
| Git | Indispensable pour travailler sur un dépôt. Sous Windows natif, installez Git for Windows : l'agent utilise alors Git Bash, sinon PowerShell. |
| AWS CLI | Version 2, pour la connexion par l'annuaire. Facultative si les identifiants arrivent autrement. |

**Windows : natif ou WSL ?** L'outil fonctionne directement sous Windows, sans droits d'administrateur. Préférez WSL 2 si vos chaînes de compilation sont Linux ou si vous voulez isoler les commandes de l'agent dans un bac à sable : cette isolation n'existe pas sous Windows natif. Dans WSL, on installe et on lance tout depuis le terminal Linux.

**Le réseau.** Avec Bedrock, le poste n'a pas besoin de joindre les serveurs de l'éditeur pour fonctionner. Il doit joindre :

- les points d'accès AWS de la région choisie : `bedrock-runtime` pour les requêtes au modèle, `bedrock` pour la liste des profils d'inférence, `sts` pour vérifier les identifiants ;
- ceux d'IAM Identity Center, si la connexion passe par l'annuaire : le portail d'accès AWS de l'entreprise et le service `oidc` de sa région ;
- votre serveur Git et votre miroir de paquets, s'ils sont internes.

Deux exceptions sont à connaître. L'installeur natif et la mise à jour automatique téléchargent depuis `downloads.claude.ai` ; sur un poste isolé, on désactive les mises à jour et on distribue l'outil soi-même (voir « Installer selon son système »). L'outil qui lit une page web interroge `api.anthropic.com` pour vérifier le domaine, sauf si le paramètre `skipWebFetchPreflight` vaut `true`.

**Proxy et certificats.** L'outil lit les variables `HTTPS_PROXY`, `HTTP_PROXY` et `NO_PROXY`, mais ne gère pas les proxys SOCKS. Derrière un proxy qui inspecte le trafic chiffré, l'installation native lit le magasin de certificats du système ; sinon, indiquez le certificat racine de l'entreprise dans `NODE_EXTRA_CA_CERTS`. Pour un proxy qui exige une authentification NTLM ou Kerberos, passez par une passerelle (voir « Les alternatives »).

Rangez ces variables dans le bloc `env` des paramètres plutôt que dans le profil du shell : c'est le seul endroit qui atteint aussi l'extension VS Code et les sessions lancées en arrière-plan.

## Installer selon son système

La bonne méthode dépend moins du système que de la façon dont votre entreprise gère ses postes.

| Situation | Méthode | Mises à jour |
| --- | --- | --- |
| Poste connecté, usage individuel | Installeur natif, canal *stable* | Automatiques, en arrière-plan |
| Parc macOS géré | Homebrew, paquet `claude-code` (canal stable) | Manuelles, ou confiées à l'outil |
| Parc Windows géré | WinGet | Manuelles, ou confiées à l'outil |
| Parc Linux géré | Dépôts apt, dnf ou apk signés par l'éditeur | Avec les mises à jour du système |
| Poste isolé, avec miroir interne | Paquet npm via le miroir, ou dépôt apt ou dnf recopié | Par l'équipe poste de travail, version figée |

### Installeur natif

Il ne demande ni droits d'administrateur ni Node.js. Ajoutez `stable` pour suivre le canal qui a environ une semaine de recul et écarte les versions à régression majeure.

```bash
# macOS, Linux, WSL
curl -fsSL https://claude.ai/install.sh | bash -s stable
```

```powershell
# Windows PowerShell
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) stable
```

Pour installer une version précise, remplacez `stable` par son numéro, par exemple `2.1.301`. Le canal choisi à l'installation devient celui des mises à jour automatiques.

### Gestionnaires de paquets

```bash
# macOS : le paquet claude-code suit le canal stable
brew install --cask claude-code
```

```powershell
# Windows
winget install Anthropic.ClaudeCode
```

Sous Debian, Ubuntu, Fedora, RHEL ou Alpine, l'éditeur publie des dépôts signés, avec un canal *stable* et un canal *latest*. Avant d'importer la clé de signature, vérifiez son empreinte : `31DD DE24 DDFA B679 F42D 7BD2 BAA9 29FF 1A7E CACE`. Ces installations ne se mettent pas à jour seules.

### Poste isolé : passer par le miroir interne

C'est le cas du roman : les postes de l'équipe ne voient que Bedrock, le serveur Git et le miroir des bibliothèques. Le paquet npm convient bien, car il passe par le miroir comme n'importe quelle dépendance. Il exige Node.js 22 ou plus récent.

```bash
npm install -g @anthropic-ai/claude-code@2.1.301
```

N'utilisez jamais `sudo` avec cette commande ; en cas d'erreur de droits, configurez un dossier npm global dans le répertoire de l'utilisateur. Une autre voie consiste à recopier le dépôt apt ou dnf de l'éditeur dans votre gestionnaire de dépôts, ce qui garde la vérification de signature.

### Vérifier l'installation

Ouvrez un nouveau terminal, puis :

```bash
claude --version   # affiche par exemple : 2.1.301 (Claude Code)
claude doctor      # santé de l'installation, paramètres invalides, mises à jour
```

Si le shell répond que `claude` est introuvable, le dossier d'installation (`~/.local/bin` pour l'installeur natif) n'est pas dans le `PATH`. Les binaires macOS sont signés par l'éditeur et notariés par Apple, ceux de Windows signés par l'éditeur ; chaque version publie aussi un manifeste de sommes de contrôle signé, que l'équipe sécurité peut vérifier.

### Ajouter l'IDE

- **VS Code** (version 1.94 ou plus) : cherchez « Claude Code » dans le panneau des extensions, éditeur Anthropic. Les dérivés qui n'accèdent pas à la place de marché de Microsoft la trouvent sur Open VSX.
- **JetBrains** : installez le plugin « Claude Code » depuis la JetBrains Marketplace, puis redémarrez l'IDE. Si le plugin ne trouve pas `claude`, indiquez son chemin complet dans *Settings → Tools → Claude Code*.

## La configuration de référence : Bedrock en région européenne

La configuration tient en six étapes. L'administrateur cloud prépare les cinq premières une fois pour toute l'équipe ; chaque développeur n'intervient qu'aux deux dernières, sur son poste, en dix minutes.

> *Schéma non reproduit dans cette version Markdown : configuration de référence · poste, compte AWS dédié, régions européennes.*

Le développeur se connecte par l'annuaire (1), puis Claude Code envoie ses requêtes à Bedrock (2), qui les fait traiter dans une région européenne (3). CloudTrail garde la trace de chaque appel ; le poste ne joint rien d'autre que le réseau interne.

### 1. Un compte AWS dédié

Créez dans AWS Organizations un compte réservé à Claude Code, comme le recommande la documentation de l'éditeur. Vous y gagnez des coûts isolés dans Cost Explorer, des quotas qui ne concurrencent aucune autre application, et un journal CloudTrail que l'équipe sécurité peut lire sans voir le reste.

Choisissez ensuite la région source, celle depuis laquelle partent les requêtes. Dans le roman, c'est `eu-west-3` (Paris), où la mutuelle héberge déjà son extranet.

> **Piège fréquent.** Si votre organisation bloque les régions non autorisées par une politique de contrôle de service (SCP), le profil européen échouera dès qu'il enverra une requête vers une autre région. Autorisez Bedrock dans toutes les régions de destination du profil.

### 2. Ouvrir l'accès aux modèles

Dans la console Bedrock, ouvrez le catalogue de modèles, choisissez un modèle Anthropic et remplissez le formulaire de cas d'usage. On le fait une fois par compte, et l'accès est accordé dès l'envoi. Avec AWS Organizations, le compte de gestion peut le soumettre une seule fois pour tous les comptes rattachés, par l'API `PutUseCaseForModelAccess`.

Bedrock fixe ses critères d'accès modèle par modèle. Certains sont ouverts à tous les clients, comme Sonnet 5, Opus 4.7, Opus 4.8, Haiku 4.5 et les modèles Fable ; pour les autres, dont Opus 5.5 et Sonnet 5.5, vérifiez dans la console.

### 3. Choisir le profil d'inférence européen

Les modèles Claude récents ne s'appellent pas directement : on passe par un profil d'inférence, dont le préfixe dit où la requête peut être traitée.

| Préfixe | Où la requête est traitée | Pour la configuration de référence |
| --- | --- | --- |
| `eu.` | Dans les régions européennes d'AWS | Oui |
| `global.` | Dans n'importe quelle région commerciale du monde | Non |
| `us.`, `jp.`, `au.`, `apac.` | Dans une autre zone géographique | Non |

Le profil `eu.` répartit la charge entre les régions européennes listées sur la fiche de chaque modèle : Francfort, Paris, Irlande, Milan, Espagne, Stockholm, et selon les modèles Londres ou Zurich. Ces deux dernières sont hors de l'Union européenne ; votre délégué à la protection des données doit le savoir avant de signer. S'il les refuse, voyez la variante à la fin de l'étape 4. Vérifiez aussi les tarifs : un profil géographique n'est pas toujours facturé au même prix que le profil mondial.

Pour lister les profils réellement disponibles depuis votre région :

```bash
aws bedrock list-inference-profiles --region eu-west-3 --type-equals SYSTEM_DEFINED
```

Au 16 octobre 2026, les deux identifiants utiles sont `eu.anthropic.claude-opus-5-5` et `eu.anthropic.claude-sonnet-5-5`.

### 4. Donner les droits IAM

La politique ci-dessous autorise l'appel des modèles Anthropic à travers les seuls profils européens. Elle reprend les actions que demande la documentation de l'éditeur, en restreignant les ressources ; testez-la sur un poste avant de la généraliser.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "InvoquerClaudeEnEurope",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:GetInferenceProfile"
      ],
      "Resource": [
        "arn:aws:bedrock:eu-west-3:*:inference-profile/eu.anthropic.*",
        "arn:aws:bedrock:eu-*::foundation-model/anthropic.*"
      ]
    },
    {
      "Sid": "ListerLesProfils",
      "Effect": "Allow",
      "Action": "bedrock:ListInferenceProfiles",
      "Resource": "*"
    }
  ]
}
```

La seconde ressource du premier bloc est indispensable : un profil européen appelle le modèle dans d'autres régions, et chacune vérifie le droit. Pour la toute première activation d'un modèle, la documentation ajoute aussi les droits `aws-marketplace:ViewSubscriptions` et `aws-marketplace:Subscribe`, limités aux appels qui passent par Bedrock.

#### Variante : exclure Londres et Zurich

Une règle ne peut pas retirer une région d'un profil européen. Bedrock vérifie le droit dans chaque région de destination du profil ; si une seule est refusée, toutes les requêtes qui passent par ce profil échouent, même vers les régions autorisées. Pour tenir Londres et Zurich à l'écart, il faut donc renoncer au profil `eu.` et faire traiter les requêtes dans une seule région.

Bedrock le permet par son point d'accès Mantle, dans les régions européennes qui acceptent l'appel en région unique : à ce jour l'Irlande (`eu-west-1`) et Stockholm (`eu-north-1`), pas Paris. Trois contreparties sont à peser. La région source passe de Paris à Dublin. Un point d'accès régional est facturé environ 10 % de plus que le point d'accès mondial. Enfin, les modèles servis par Mantle dépendent de ce que votre compte a reçu : confirmez-les avec votre interlocuteur AWS.

Côté AWS, cette politique de contrôle de service (SCP), attachée au compte dédié, rend l'exclusion impossible à contourner :

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RefuserLondresEtZurich",
      "Effect": "Deny",
      "Action": ["bedrock:*", "bedrock-mantle:*"],
      "Resource": "*",
      "Condition": {
        "StringEquals": { "aws:RequestedRegion": ["eu-west-2", "eu-central-2"] }
      }
    },
    {
      "Sid": "RefuserLesProfilsMultiregions",
      "Effect": "Deny",
      "Action": "bedrock:InvokeModel*",
      "Resource": "*",
      "Condition": {
        "Null": { "bedrock:InferenceProfileArn": "false" }
      }
    },
    {
      "Sid": "MantleEnIrlandeSeulement",
      "Effect": "Deny",
      "Action": "bedrock-mantle:*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": { "aws:RequestedRegion": "eu-west-1" }
      }
    }
  ]
}
```

| Bloc | Effet |
| --- | --- |
| `RefuserLondresEtZurich` | Aucune action Bedrock ne peut viser Londres ou Zurich, ni directement ni comme destination d'un profil. |
| `RefuserLesProfilsMultiregions` | Aucun appel ne passe par un profil multirégion, qu'il soit `eu.` ou `global.`. |
| `MantleEnIrlandeSeulement` | Le point d'accès Mantle n'est utilisable qu'en Irlande. |

Dans l'ensemble d'autorisations de l'étape 5, remplacez la politique ci-dessus par les droits `bedrock-mantle:CreateInference` et `bedrock-mantle:CountTokens`, limités à la région `eu-west-1`. Côté poste, les paramètres gérés deviennent :

```json
{
  "allowedProviders": ["mantle"],
  "env": {
    "CLAUDE_CODE_USE_MANTLE": "1",
    "AWS_REGION": "eu-west-1",
    "ANTHROPIC_MODEL": "anthropic.claude-sonnet-5-5"
  },
  "availableModels": [
    "anthropic.claude-sonnet-5-5",
    "anthropic.claude-opus-5-5"
  ]
}
```

Sur Mantle, les identifiants de modèles ne portent pas de préfixe géographique. Au premier lancement, `/status` doit afficher le fournisseur *Amazon Bedrock (Mantle)*. Testez la SCP sur un compte d'essai avant de l'appliquer : une erreur de condition bloque toute l'équipe.

### 5. Se connecter par l'annuaire

Reliez IAM Identity Center à l'annuaire de l'entreprise (Entra ID, Okta ou Active Directory). Créez un ensemble d'autorisations qui porte la politique ci-dessus, puis affectez-le, sur le compte dédié, au groupe de l'équipe projet. Personne ne reçoit de clé d'accès permanente : AWS déconseille les clés d'utilisateur IAM pour ce type d'usage, et réserve les clés API Bedrock à longue durée à l'exploration.

Chaque développeur crée une fois son profil, puis se connecte au début de sa journée :

```bash
aws configure sso                         # une fois : profil « claude-bedrock »
aws sso login --profile claude-bedrock    # chaque jour, dans le navigateur
```

Dans CloudTrail, chaque appel à Bedrock porte alors le nom de la personne qui l'a fait. C'est le « chaque requête porte un nom » que Thomas promet au RSSI.

### 6. Brancher Claude Code

Pour un premier essai, l'assistant intégré suffit. Lancez `claude`, choisissez *3rd-party platform* puis *Amazon Bedrock*. Il détecte vos profils AWS, demande la région, vérifie quels modèles votre compte peut appeler et propose de les figer. Il enregistre le résultat dans `~/.claude/settings.json` ; la commande `/setup-bedrock` le rouvre plus tard.

Pour une équipe, écrivez la configuration vous-même, afin qu'elle soit identique partout. Voici le fichier de paramètres de l'utilisateur, `~/.claude/settings.json` :

```json
{
  "env": {
    "CLAUDE_CODE_USE_BEDROCK": "1",
    "AWS_PROFILE": "claude-bedrock",
    "AWS_REGION": "eu-west-3",
    "ANTHROPIC_MODEL": "eu.anthropic.claude-sonnet-5-5",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "eu.anthropic.claude-sonnet-5-5",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "eu.anthropic.claude-opus-5-5"
  },
  "awsAuthRefresh": "aws sso login --profile claude-bedrock"
}
```

| Ligne | Rôle |
| --- | --- |
| `CLAUDE_CODE_USE_BEDROCK` | Fait passer toutes les requêtes par Bedrock. |
| `AWS_PROFILE` | Désigne le profil de connexion par l'annuaire. Dans les paramètres, il ne fuit pas vers les autres programmes du poste. |
| `AWS_REGION` | Fixe la région source ; une région `eu-*` fait choisir le préfixe `eu.`. |
| `ANTHROPIC_MODEL` | Modèle de départ des sessions. Sans lui, elles démarrent sur Opus, facturé plus cher ; on passe à Opus à la demande avec `/model`. |
| `ANTHROPIC_DEFAULT_…_MODEL` | Ce que désignent les alias `sonnet` et `opus` (voir « Figer les versions »). |
| `awsAuthRefresh` | Relance la connexion quand la session AWS expire. |

Si des onglets de connexion s'ouvrent en boucle, c'est souvent qu'un VPN ou un proxy coupe le flux du navigateur : retirez `awsAuthRefresh` et lancez `aws sso login` avant `claude`.

Dans VS Code, cochez *Disable Login Prompt* dans les réglages de l'extension : elle lit ensuite le même fichier `~/.claude/settings.json`. Le plugin JetBrains, lui, n'a rien à régler.

## Figer les versions

Une équipe qui livre doit savoir quel modèle et quelle version de l'outil ont produit son code. Sans gel, les deux bougent sous vos pieds.

**Les modèles.** Les alias `opus` et `sonnet` pointent vers des modèles par défaut, inscrits dans l'outil, qui changent avec ses versions. En les fixant par `ANTHROPIC_DEFAULT_OPUS_MODEL` et `ANTHROPIC_DEFAULT_SONNET_MODEL`, c'est vous qui décidez quand l'équipe change de modèle. Les tâches de fond, comme le titrage des sessions, utilisent alors le modèle de départ ; pour les confier à un modèle moins cher, fixez aussi `ANTHROPIC_DEFAULT_HAIKU_MODEL` avec un identifiant que votre compte peut appeler. Pour interdire tout autre modèle, listez les modèles permis dans `availableModels` et ajoutez `enforceAvailableModels`.

**L'outil.** Quatre réglages, du plus souple au plus strict :

| Besoin | Réglage |
| --- | --- |
| Recevoir les mises à jour avec une semaine de recul | `"autoUpdatesChannel": "stable"` |
| Ne jamais redescendre sous une version | `"minimumVersion": "2.1.301"` |
| Distribuer soi-même les versions, sans aucune mise à jour par l'outil | Variable `DISABLE_UPDATES` à `1` |
| Refuser de démarrer hors d'une plage de versions | `requiredMinimumVersion` et `requiredMaximumVersion` |

Ne confondez pas `DISABLE_UPDATES` avec `DISABLE_AUTOUPDATER` : la seconde n'arrête que la vérification en arrière-plan, et laisse un développeur lancer `claude update`.

### Imposer la configuration à tous les postes

Tout ce qui précède peut vivre dans les paramètres de chaque utilisateur, mais un utilisateur peut les modifier. Pour en faire une règle, placez-les dans le fichier de paramètres gérés, que l'outil applique au-dessus de tous les autres et que personne ne peut écraser depuis son poste.

| Système | Emplacement du fichier `managed-settings.json` |
| --- | --- |
| macOS | `/Library/Application Support/ClaudeCode/` |
| Linux et WSL | `/etc/claude-code/` |
| Windows | `C:\Program Files\ClaudeCode\` |

On peut aussi le distribuer par un profil de configuration macOS ou une clé de registre Windows, via Jamf, Intune ou une stratégie de groupe. Voici le fichier de référence du roman :

```json
{
  "allowedProviders": ["bedrock"],
  "env": {
    "CLAUDE_CODE_USE_BEDROCK": "1",
    "AWS_REGION": "eu-west-3",
    "ANTHROPIC_MODEL": "eu.anthropic.claude-sonnet-5-5",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "eu.anthropic.claude-sonnet-5-5",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "eu.anthropic.claude-opus-5-5",
    "DISABLE_UPDATES": "1"
  },
  "availableModels": [
    "eu.anthropic.claude-sonnet-5-5",
    "eu.anthropic.claude-opus-5-5"
  ],
  "enforceAvailableModels": true,
  "requiredMinimumVersion": "2.1.301"
}
```

La première ligne mérite qu'on s'y arrête. `allowedProviders` limite les fournisseurs qu'un poste géré peut utiliser : avec la seule valeur `bedrock`, un développeur ne peut plus se connecter avec un abonnement personnel. C'est exactement l'incident qui ouvre le chapitre 2. Le profil AWS, propre à chacun, reste dans les paramètres de l'utilisateur.

Ce fichier est aussi celui où vivront les interdictions de lecture, les règles sur les commandes et le bac à sable. Le chapitre M4 les détaille. Pour vérifier qu'il est appliqué, lancez `/status` : la ligne *Setting sources* doit mentionner `Enterprise managed settings (file)`.

## Les alternatives

Bedrock n'est pas un choix universel : c'est le bon choix quand AWS est déjà un fournisseur qualifié de l'entreprise. Ailleurs, une autre option sera plus simple.

| Option | Quand la choisir | Ce qui change |
| --- | --- | --- |
| Abonnement Team ou Enterprise de l'éditeur | Vous voulez tout, sans infrastructure : application de bureau, web, sessions dans le cloud, tableau de bord d'usage. C'est l'option que l'éditeur recommande à la plupart des organisations. | Connexion par `/login` avec l'authentification unique de l'entreprise. L'éditeur devient un fournisseur à qualifier, ce que la mutuelle voulait éviter. |
| Claude Platform on AWS | Vous voulez acheter via AWS Marketplace tout en appelant l'API de l'éditeur, avec la recherche web. | Variable `CLAUDE_CODE_USE_ANTHROPIC_AWS` ; les requêtes partent vers l'éditeur. |
| Google Cloud (Agent Platform, ex-Vertex AI) | Votre entreprise est sur Google Cloud. | Variable `CLAUDE_CODE_USE_VERTEX` et identifiants Google Cloud. |
| Microsoft Foundry | Votre entreprise est sur Azure et Entra ID. | Variable `CLAUDE_CODE_USE_FOUNDRY` ; connexion par Entra ID possible. |
| Point d'accès Mantle de Bedrock | Votre compte AWS a reçu des modèles servis au format natif de l'éditeur. | Variable `CLAUDE_CODE_USE_MANTLE`, des droits IAM propres et une liste de modèles distincte. |
| Passerelle devant le fournisseur | Il vous faut des budgets par équipe, un suivi centralisé ou une authentification que l'outil ne gère pas, comme un proxy NTLM. | Le poste parle à la passerelle, qui parle à Bedrock. L'éditeur propose la sienne, *Claude apps gateway*, à héberger soi-même. |

Un critère tranche souvent : la qualification du fournisseur. Au chapitre 2, Thomas commence par chercher un abonnement d'entreprise chez l'éditeur ; Julien lui fait remarquer qu'AWS est déjà inscrit au registre DORA de la mutuelle. Six semaines d'instruction deviennent trois jours.

## Premier lancement

La première session a un seul but : prouver que la chaîne fonctionne, sans rien modifier. On la lance donc en mode plan, où l'agent lit et propose, mais n'écrit rien.

1. Ouvrez un terminal dans le dossier d'un dépôt que vous connaissez bien, connectez-vous, puis lancez l'outil :

   ```bash
   aws sso login --profile claude-bedrock
   claude --permission-mode plan
   ```
2. L'outil vous demande si vous faites confiance aux fichiers de ce dossier. Un dépôt peut contenir des réglages qui déclenchent des commandes ; ne répondez oui que pour un code dont vous connaissez l'origine.
3. Tapez `/status` et contrôlez trois lignes : le fournisseur (*Amazon Bedrock*), la région (`eu-west-3`) et les sources de paramètres, qui doivent inclure les paramètres gérés s'ils sont déployés.
4. Tapez `/model` : seuls les modèles européens autorisés doivent apparaître.
5. Posez une première question qui n'engage rien, par exemple : « Explique-moi l'organisation de ce projet en dix lignes, sans rien modifier. » L'agent ouvre des fichiers, puis répond.
6. Tapez `/usage` pour voir les jetons consommés et le coût de la session, puis `/exit` pour quitter.

Demandez enfin à l'administrateur de retrouver votre appel côté AWS, avec votre nom. Si c'est le cas, la promesse faite au RSSI est tenue de bout en bout.

Trois différences surprennent les habitués d'un abonnement. Il n'y a pas de `/logout` : l'identité vient du profil AWS, et l'on change de compte en changeant de profil. La touche Maj+Tab fait défiler les modes de permission ; une session peut, selon la version et les réglages, démarrer dans un mode qui agit sans demander, d'où le mode plan imposé ici. Enfin, l'agent ne cherche pas sur internet : donnez-lui l'adresse exacte d'une documentation s'il en a besoin.

Le chapitre M2 reprend ces premiers pas en détail : sessions, mode plan, validation des actions, gestion du contexte et retour arrière.

## Vérifier, dépanner

Un poste est prêt quand les sept points suivants sont cochés. Gardez cette liste pour l'arrivée de chaque nouveau membre de l'équipe.

- [ ] `claude --version` affiche la version de référence de l'équipe.
- [ ] `claude doctor` ne signale aucune erreur.
- [ ] `/status` indique Amazon Bedrock, la région `eu-west-3` et les paramètres gérés.
- [ ] `/model` ne propose que les modèles européens autorisés.
- [ ] Une question posée en mode plan reçoit une réponse.
- [ ] L'appel apparaît côté AWS, au nom du développeur.
- [ ] Dans l'IDE, le panneau s'ouvre sans demander de connexion.

Les pannes de la première installation se ressemblent d'une entreprise à l'autre.

| Symptôme | Cause probable | Remède |
| --- | --- | --- |
| `claude` introuvable après l'installation | Le dossier d'installation n'est pas dans le `PATH`. | Ouvrir un nouveau terminal ; ajouter `~/.local/bin` au `PATH`. |
| Accès refusé sur `bedrock:InvokeModel` | Droit manquant sur le modèle dans une région de destination, ou SCP qui bloque cette région. | Vérifier les deux ressources de la politique IAM et les régions autorisées par l'organisation. |
| Erreur « on-demand throughput isn't supported » | Identifiant de modèle nu au lieu d'un profil d'inférence. | Utiliser l'identifiant préfixé `eu.`. |
| Le modèle est refusé au démarrage | Modèle non activé sur le compte, ou absent des profils de la région. | Lister les profils, remplir le formulaire d'accès. |
| Jeton de session absent, invalide ou expiré | La session IAM Identity Center a expiré. | Relancer `aws sso login`, ou configurer `awsAuthRefresh`. |
| Onglets de connexion qui s'ouvrent en boucle | Un VPN ou un proxy coupe le flux du navigateur. | Retirer `awsAuthRefresh` ; se connecter avant de lancer l'outil. |
| « unable to get local issuer certificate » | Proxy qui inspecte le trafic chiffré. | Installer le certificat racine dans le magasin du système, ou le désigner dans `NODE_EXTRA_CA_CERTS`. |
| `/status` affiche `us-east-1` | Aucune région définie : l'outil retombe sur sa valeur par défaut. | Renseigner `AWS_REGION`. |
| VS Code réclame une connexion | Le réglage *Disable Login Prompt* n'est pas coché, ou l'éditeur n'a pas hérité des variables du shell. | Cocher le réglage ; ranger la configuration dans `~/.claude/settings.json`. |

Pour toute autre panne, `claude --debug` écrit un journal détaillé dans `~/.claude/debug/`. Le chapitre M14 couvre les erreurs d'usage et la lecture de la consommation.

## Dans le roman

| Chapitre | Scène | Ce qu'elle illustre ici |
| --- | --- | --- |
| 2 — Le RSSI dit non | Mardi, 12 h 05 : Sofiane a installé l'outil avec son abonnement personnel. | Pourquoi verrouiller le fournisseur avec `allowedProviders`. |
| 2 — Le RSSI dit non | Mercredi, 21 heures : Julien propose Bedrock, déjà au registre DORA. | Le compte dédié, le profil européen, la connexion par l'annuaire, les versions figées. |
| 2 — Le RSSI dit non | Jeudi, 17 heures : Bertrand signe une dérogation provisoire. | Le Cloud Act, risque résiduel identique à celui de l'extranet, écrit noir sur blanc. |
| 3 — Le fichier qui parle à la machine | Lundi, 8 heures : Mathilde attaque l'agent sur les postes fraîchement installés. | Ce que l'installation ne protège pas seule : les secrets laissés dans le code (chapitre M4). |

Pour aller plus loin : M2 (premiers pas), M3 (CLAUDE.md et la mémoire), M4 (paramètres et permissions), M14 (dépannage et coûts).

## Sources

Consultées le 16 octobre 2026.

- [Claude Code — installation avancée](https://code.claude.com/docs/en/setup)
- [Claude Code sur Amazon Bedrock](https://code.claude.com/docs/en/amazon-bedrock)
- [Disponibilité des fonctions par fournisseur](https://code.claude.com/docs/en/feature-availability)
- [Options de déploiement en entreprise](https://code.claude.com/docs/en/third-party-integrations)
- [Configuration réseau en entreprise](https://code.claude.com/docs/en/network-config)
- [Déployer des paramètres gérés](https://code.claude.com/docs/en/managed-settings)
- [Extension VS Code](https://code.claude.com/docs/en/vs-code)
- [Plugin JetBrains](https://code.claude.com/docs/en/jetbrains)
- [Notes de version de Claude Code](https://code.claude.com/docs/en/changelog)
- [Claude dans Amazon Bedrock — documentation de l'éditeur](https://platform.claude.com/docs/build-with-claude/claude-in-amazon-bedrock)
- [Fiche AWS du modèle Claude Sonnet 5.5](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-sonnet-5-5.html)
- [Annonce AWS de Claude Opus 5.5 sur Bedrock](https://aws.amazon.com/blogs/machine-learning/claude-opus-5-5-is-now-available-on-aws/)
- [Fiche AWS du modèle Claude Opus 4.7, régions du profil européen](https://docs.aws.eu/bedrock/latest/userguide/model-card-anthropic-claude-opus-4-7.html)
