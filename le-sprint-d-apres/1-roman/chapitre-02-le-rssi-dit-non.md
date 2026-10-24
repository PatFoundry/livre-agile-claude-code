# Chapitre 2 — Le RSSI dit non

## Mardi, 12 h 05

Personne n'a parlé pendant quelques secondes. Puis tout le monde a regardé Sofiane.

— Installé avec quel compte ? ai-je demandé.

— Mon abonnement personnel. Je voulais juste tester sur notre code, pour qu'on gagne du temps.

— Quel code ?

Il a rougi.

— Le client de l'API contrats. Celui qu'on réutilisera pour le portail.

Julien a fermé les yeux une seconde. Le client de l'API contrats contenait l'adresse des serveurs internes, la structure des données assurés et, dans un fichier de configuration que tout le monde avait oublié, un mot de passe de recette.

J'ai parlé lentement, pour que ma voix ne trahisse rien.

— Sofiane, vous fermez la session maintenant. Vous ne supprimez rien, vous ne nettoyez rien. Vous notez sur une feuille ce que vous avez ouvert, à quelle heure, et ce que vous avez demandé à l'agent. Cet après-midi, cette feuille vaudra plus que n'importe quelle excuse.

Il a hoché la tête. Il n'avait pas l'air d'un fraudeur. Il avait l'air de ce qu'il était : un garçon brillant qui avait voulu bien faire, avec les outils qu'on ne lui avait pas donnés.

Claire, elle, avait déjà son téléphone à l'oreille. Elle a raccroché avant d'avoir parlé.

— Je vais demander au directeur général de trancher. C'est lui qui veut ce portail. Une dérogation signée de sa main, et la commission de Bertrand n'aura plus d'objet.

— Vous gagneriez une semaine, ai-je répondu. Et vous perdriez le projet.

— Pourquoi ?

— Parce qu'au premier incident, et il y en aura un, le RSSI dira qu'il avait prévenu. Il aura raison, et il aura un mail pour le prouver. On ne gagne jamais contre la sécurité. On gagne avec elle, ou on ne gagne pas.

Elle a posé son téléphone sur la table, écran contre le bois.

— Alors on fait quoi ?

— J'appelle Bertrand. Je lui dis ce qui s'est passé avant qu'il l'apprenne par quelqu'un d'autre. Et je lui demande ce dont il a besoin pour dire oui.

## Mardi, 15 heures

Le bureau de Bertrand Lefebvre était au deuxième étage, côté cour, sans vue sur rien. Sur son bureau, un exemplaire imprimé du règlement DORA, hérissé de marque-pages de couleur. Au mur, un schéma du réseau de la mutuelle qu'il avait manifestement dessiné lui-même, il y a longtemps, et mis à jour au feutre depuis.

Il avait une soixantaine d'années, une voix calme et des yeux qui ne cillaient pas beaucoup. Trente ans de réseaux et de sécurité, dont vingt dans la maison. Il avait vu passer trois directeurs informatiques, deux fusions et une cyberattaque dont personne ne parlait jamais.

Je lui ai tendu la feuille de Sofiane avant de m'asseoir.

— Avant toute chose : ce matin, un développeur de l'équipe a utilisé Claude Code avec son abonnement personnel, sur un poste de la mutuelle, sur le client de l'API contrats. Il y a un mot de passe de recette dans ce code. Il est noté là, avec les heures.

Bertrand a lu la feuille deux fois. Puis il l'a posée et m'a regardé avec quelque chose qui ressemblait à de la surprise.

— D'habitude, j'apprends ce genre de choses trois mois plus tard, par un audit.

— Le mot de passe doit être changé aujourd'hui. Et je vous dois l'explication suivante : ce garçon n'a pas cherché à tricher. Il a utilisé l'outil qu'on ne lui avait pas fourni. Si nous n'apportons pas un cadre, d'autres feront pareil, et vous ne le saurez pas.

Il a décroché son téléphone, a dicté trois phrases à quelqu'un de son équipe et a raccroché.

— Bon. Maintenant, dites-moi pourquoi je devrais vous laisser installer un programme qui lit tout le code de la maison et l'envoie aux États-Unis.

— Dites-moi d'abord ce qui vous inquiète. Tout.

Il a levé un doigt après l'autre.

— Un : où part le code, qui le lit, et s'il sert à entraîner un modèle. Deux : un agent qui exécute des commandes sur un poste branché sur notre réseau, c'est un attaquant à qui on aurait donné un badge. Trois : les secrets et les données personnelles, vous venez de m'en donner un exemple. Quatre : un nouveau fournisseur. Avec DORA, je dois l'inscrire au registre, évaluer sa criticité, négocier les clauses d'audit, prévoir un plan de sortie. Cinq : la traçabilité. Le jour où il se passe quelque chose, je veux savoir qui a fait quoi, l'humain ou la machine.

— C'est pour ça que la commission a besoin de six semaines.

— Six semaines, c'est rapide. Le dernier fournisseur cloud en a pris quatorze.

J'ai noté ses cinq points dans mon carnet, dans son ordre, avec ses mots.

— Une dernière question, monsieur Lefebvre. Si je reviens avec une solution qui n'ajoute aucun nouveau fournisseur, où le code ne quitte pas l'Europe, et où c'est vous qui fixez les règles, il vous faut combien de temps ?

Il a réfléchi un moment.

— Montrez-moi d'abord. Ensuite, je vous répondrai.

## Mercredi, 21 heures

C'est Julien qui a trouvé la clé. Je ne l'attendais pas de lui.

Nous étions seuls au quatrième, dans la salle Escaut, devant le tableau couvert des cinq points de Bertrand. J'avais commencé à chercher un abonnement d'entreprise chez l'éditeur, avec un contrat et une clause d'hébergement européen. Julien m'a interrompu sans lever les yeux de son écran.

— Pas besoin d'un nouveau fournisseur. On a déjà AWS.

Il m'a expliqué. Deux ans plus tôt, la mutuelle avait migré son extranet partenaires sur Amazon Web Services, dans la région de Paris. Le contrat avait été négocié par les achats, épluché par le juridique, et le fournisseur évalué par la commission de Bertrand. AWS figurait déjà au registre DORA, avec son plan de sortie.

— Et dans AWS, il y a Bedrock, a-t-il continué. Le service qui donne accès aux modèles d'IA. Les modèles Claude y sont, et Claude Code sait s'y brancher directement. On reste chez notre fournisseur, sous notre contrat, sur notre compte.

— Et l'Europe ?

Il a cherché dans la documentation et tourné l'écran vers moi.

— On choisit un profil d'inférence européen. Les requêtes sont traitées uniquement dans des régions européennes d'AWS. Et AWS s'engage à ne pas utiliser les échanges pour entraîner des modèles, ni à les transmettre à l'éditeur du modèle.

J'ai repris les cinq points un par un. En deux heures, nous avions une réponse à chacun.

Pour le premier, Bedrock en région européenne, sur un compte AWS dédié au projet, comme le recommande d'ailleurs la documentation : les coûts séparés, les accès isolés. Connexion par l'annuaire de l'entreprise, pour que chaque requête porte un nom. Versions des modèles figées par la DSI : personne ne change de modèle sans le dire.

Pour le deuxième, l'agent qui exécute des commandes, Julien a trouvé les paramètres gérés : un fichier de règles déployé par la DSI sur chaque poste, que le développeur ne peut pas modifier. Interdiction de lire les fichiers de secrets, interdiction des commandes réseau, validation humaine avant toute commande. Les postes de l'équipe sur un segment réseau qui ne voit que trois choses : Bedrock, notre serveur Git et le miroir interne des bibliothèques.

— Et un détail qui va plaire à Bertrand, a-t-il ajouté. Via Bedrock, l'agent n'a pas d'outil de recherche sur internet. Une porte de sortie de moins.

Pour le troisième, aucune donnée réelle : des jeux de données synthétiques, générés et validés par Émilie. Les secrets dans le coffre-fort de la DSI, jamais dans le code.

Pour le quatrième, rien à faire. C'était tout l'intérêt.

Pour le cinquième, les appels à Bedrock tracés dans les journaux AWS, les métriques de Claude Code envoyées vers l'outil de supervision de la sécurité, et une règle simple : l'agent ne pousse jamais directement sur la branche principale. Tout passe par une demande de fusion, relue par un humain.

Vers 23 heures, Julien s'est étiré.

— Il reste un sujet, a-t-il dit. AWS est une entreprise américaine. Le Cloud Act, Bertrand va le sortir.

— Il aura raison. On ne le cache pas. On écrit que le risque existe, qu'il est le même que pour l'extranet, et que la mutuelle l'a déjà accepté une fois, en connaissance de cause.

Il a hoché la tête, puis il a souri pour la première fois depuis lundi.

— Tu sais ce qui me plaît ? Pour une fois, c'est l'outil qui doit prouver qu'il est sûr. Pas moi.

Il m'avait tutoyé sans y penser. Je n'ai rien relevé.

Avant de partir, nous avons tout résumé sur une page. Bertrand détestait les documents de plus d'une page ; Julien le savait.

```text
CADRE D'USAGE — PILOTE PORTAIL SINISTRES
1. Modèles Claude via Amazon Bedrock, profil européen, compte AWS dédié.
2. Connexion par l'annuaire d'entreprise, versions de modèles figées.
3. Paramètres gérés par la DSI, non modifiables par l'utilisateur.
4. Aucun accès aux secrets, aucune commande réseau, validation humaine.
5. Postes isolés : Bedrock, Git interne et miroir de bibliothèques seuls.
6. Données synthétiques uniquement. Aucune donnée d'assuré.
7. Aucune fusion sans revue humaine. Journaux transmis à la sécurité.
8. Le RSSI peut tout arrêter, à tout moment, sans justification.
```

## Jeudi, 17 heures

Bertrand a lu la page deux fois, sans un mot. Claire, assise à côté de moi, ne tenait pas en place. Julien regardait le schéma réseau au mur, comme s'il cherchait à y repérer les corrections au feutre.

— Point 5, a fini par dire Bertrand. Imaginons qu'une bibliothèque téléchargée contienne un commentaire piégé. Une instruction cachée qui dit à votre agent d'envoyer le code quelque part.

— Il ne peut joindre que trois destinations, a répondu Julien. Et aucune commande réseau ne passe sans validation humaine. Il peut être trompé. Il ne peut pas sortir.

— Il peut être trompé pour écrire du code malveillant dans notre application.

— Oui, ai-je dit. C'est pour ça que le point 7 existe. Rien n'entre dans le code sans qu'un humain l'ait relu. Et cet humain, c'est Julien.

Julien n'a pas protesté. Deux jours plus tôt, il aurait refusé cette responsabilité. Ce soir-là, il l'a prise d'un simple hochement de tête.

Bertrand a tapoté la page.

— AWS est américain. Le Cloud Act s'applique.

— C'est écrit au verso, ai-je répondu. Risque résiduel identique à celui de l'extranet partenaires, accepté par la mutuelle il y a deux ans. Nous ne prétendons pas qu'il n'existe pas.

Il a retourné la feuille, a lu le paragraphe et a eu un petit rire sec.

— Vous l'avez écrit avant que je le dise. C'est la première fois qu'un projet me fait ça.

Il s'est adossé à son fauteuil.

— Je ne peux pas court-circuiter la commission. En revanche, je peux signer une dérogation provisoire pour un pilote, sur un fournisseur déjà qualifié. Quatre semaines. La commission confirmera, ou elle arrêtera tout.

Claire a ouvert la bouche. Il a levé la main.

— Trois conditions. Un : Mathilde Grare, de mon équipe, suit votre projet dès aujourd'hui. C'est elle votre interlocutrice ; elle reçoit les journaux chaque semaine et assiste à vos démonstrations de fin de sprint. Deux : lundi, elle commencera par essayer de faire sortir du code par votre agent. Si elle y arrive, on arrête. Trois : toute décision qui touche aux données des assurés remonte jusqu'à moi.

— Accepté, ai-je dit.

— Et votre développeur, celui de la feuille...

Sofiane, dans le couloir, devait encore ruminer sa matinée.

— Il réinstalle avec le cadre, comme les autres. Et demain, 8 heures, il passe voir Mathilde. Pas pour se faire gronder. Je veux qu'il lui montre comment il s'en sert. J'aime comprendre ce que je laisse entrer chez moi, et elle me le racontera mieux qu'un rapport.

Dans le couloir, Claire m'a rattrapé.

— Trois jours au lieu de six semaines. Comment avez-vous fait ?

— Je ne lui ai pas demandé d'aller plus vite. Je lui ai demandé ce dont il avait besoin pour dire oui.

Julien marchait derrière nous, les mains dans les poches.

— Lundi, Mathilde va chercher la faille, a-t-il dit. On a intérêt à avoir bien écrit nos règles.

— On a quatre jours pour les attaquer nous-mêmes, ai-je répondu. Et c'est toi qui commences.

## Le carnet de Thomas

**Ce qui s'est passé.** Un développeur a utilisé l'outil avec un compte personnel sur du code de l'entreprise. Plutôt que de contourner le RSSI, l'équipe lui a apporté un cadre qu'il pouvait signer : les modèles Claude via Amazon Bedrock, en région européenne, chez un fournisseur déjà qualifié, avec des règles imposées sur chaque poste.

**La leçon.** On ne gagne jamais contre la sécurité. Réutiliser un fournisseur déjà évalué et nommer honnêtement le risque résiduel peut transformer six semaines d'instruction en trois jours.

**Trois questions à poser à votre équipe**

1. Qui, chez nous, utilise déjà un outil d'IA personnel sur un poste de l'entreprise ?
2. Quel contrat cloud existe déjà, et couvre-t-il l'accès à des modèles d'IA ?
3. Quelles actions l'agent ne doit-il jamais pouvoir faire, même si quelqu'un le lui demande ?

**Pour aller plus loin.** Manuel, chapitre M1 (installer Claude Code avec Amazon Bedrock) et chapitre M4 (paramètres gérés et permissions).
