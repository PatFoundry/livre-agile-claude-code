# Chapitre 16 — La sécurité au quotidien

## Lundi, 8 h 30

Le lundi qui a suivi le comité, Mathilde est arrivée dans notre open space avec son ordinateur, un écran de vingt-sept pouces sous le bras et une petite plante grasse dans un pot en terre cuite. Elle a choisi le bureau vide entre celui de Julien et celui de Sofiane, et elle y a posé la plante avant même d'avoir branché l'écran.

— Bertrand m'installe chez vous deux jours par semaine, jusqu'à la mise en production, a-t-elle dit. Il appelle ça la sécurité au quotidien. Moi, j'appelle ça arrêter de découvrir les choses dans les journaux.

Elle avait une lettre de mission d'une page, signée par Bertrand, qu'elle a posée sur le bureau de Julien. La directrice générale avait décidé que les garde-fous du Mercredi noir deviendraient la règle pour toute la maison. Il fallait donc les écrire pour toute la maison. Mathilde et Julien avaient jusqu'à la commission sécurité du mercredi suivant pour proposer ce que Bertrand appelait un socle :&#32;

ce que toute équipe qui travaille avec un agent doit avoir en place, avant sa première ligne de code.

En bas de la lettre, Bertrand avait écrit trois questions à la main.

*Qu'est-ce que l'agent a le droit de faire ? Qu'est-ce qui l'en empêche, même quand on oublie ? Comment sait-on, après coup, ce qu'il a fait ?*

— Le droit, le verrou, la trace, a résumé Julien. Il a toujours su faire court.

Ils ont commencé par faire l'inventaire de ce que l'équipe avait déjà. Il y en avait plus qu'ils ne le pensaient, et c'était justement le problème. Le fichier de consignes de l'agent, dans le dépôt. Les paramètres gérés par la sécurité, sur les postes : interdiction de lire les fichiers de secrets, interdiction de toucher à la configuration des journaux. Le contrôle automatique qui bloquait les données personnelles dans les journaux, écrit par Sofiane le soir du Mercredi noir. Le test de la chaîne d'intégration. La consigne de relecture, rangée comme une skill, qui préparait les fiches pour Julien et Gérard. Les étiquettes de risque dans Jira et dans GitHub. La limite de six demandes en revue. Le dossier des règles de gestion.

Mathilde a tout noté sur un tableau en deux colonnes : ce que c'est, et où ça vit. La deuxième colonne était la plus inquiétante. Cinq endroits différents. Certains dans le dépôt, d'autres sur les postes, un dans la chaîne, un dans la tête de Sofiane.

— Si une nouvelle équipe démarre demain, a-t-elle demandé, qui lui installe tout ça ?

— Moi, a dit Sofiane. En une journée, si je n'oublie rien.

— Tu oublieras quelque chose, a dit Julien. Moi, j'oublierais.

C'est Sofiane qui a proposé la solution, et elle était élégante. L'outil savait regrouper des consignes, des skills, des contrôles automatiques et des connexions dans un seul paquet installable, ce qu'il appelait un plugin. On pouvait publier ces paquets dans un catalogue interne, propre à la maison, et les paramètres gérés pouvaient imposer qu'un paquet soit installé sur chaque poste, sans qu'on puisse le retirer. Une équipe qui démarrerait n'aurait rien à installer elle-même. Elle recevrait le socle en ouvrant l'outil, comme on reçoit son badge le premier jour.

— Et les équipes qui n'utilisent pas cet outil-là ? a demandé Mathilde.

— Pour elles, il reste le test de la chaîne, a dit Julien. Lui, il ne demande pas quel outil a écrit le code. Il vérifie ce qui arrive.

Mathilde a souri, pour la première fois de la matinée.

— C'est exactement la phrase que je voulais entendre.

Ils se sont mis d'accord sur une règle avant d'écrire une ligne : le socle ne dépasserait pas deux pages. Julien y tenait plus que tout.

— Si c'est plus long que notre fichier de consignes, personne ne le lira. Et une règle que personne ne lit, c'est une consigne de plus. On a vu où ça mène.

À midi, ils sont partis déjeuner ensemble, ce qui n'était jamais arrivé. En revenant, j'ai entendu Julien dire, dans le couloir :

— On peut se tutoyer, maintenant qu'on a fait le même incident.

Mathilde a réfléchi une seconde.

— D'accord. Mais pas dans les rapports.

## Mercredi, 14 heures

Le mercredi, pour la première fois, Mathilde a assisté à la préparation d'une story. Pas à sa revue, une fois le code écrit. À sa préparation, avant que l'agent n'en lise la première ligne.

La story faisait partie des seize au-dessus du ruban rouge : *Archiver les photos du sinistre dans le dossier électronique du gestionnaire*. Jusque-là, les photos restaient dans le stockage du portail ; désormais, elles devaient rejoindre la gestion électronique des documents de la maison, là où Martine et les experts les consulteraient pendant des années. Sylvie l'avait étiquetée en rouge : elle touchait aux données des assurés.

Nadia, Émilie et Sofiane étaient autour de la table, comme pour toutes les stories depuis le vélo sans facture. Mathilde s'est assise à côté d'Émilie, avec un carnet.

— Pour une story rouge, a-t-elle dit, je pose trois questions. Toujours les mêmes. Quelles données manipule-t-elle ? Qui pourra les voir, et pendant combien de temps ? Et que se passe-t-il si quelqu'un ment ?

La première question a pris dix minutes, et elle a suffi. Nadia a listé ce que contenait un dossier de photos : les images elles-mêmes, le nom du fichier, la date d'envoi. Mathilde a demandé à Sofiane d'ouvrir une des photos de test et d'en afficher tout le contenu, y compris ce qu'on ne voit pas à l'écran.

Sous l'image, le fichier contenait une liste de métadonnées enregistrées automatiquement par le téléphone. La marque et le modèle de l'appareil. La date et l'heure exactes de la prise de vue. Et deux nombres à six décimales : la latitude et la longitude de l'endroit où la photo avait été prise.

— Nos photos de test ont été prises dans l'open space, a dit Sofiane. Ces coordonnées tombent sur Euralille, à trois mètres près.

Personne n'avait jamais regardé. Ni l'équipe, ni l'agent, ni moi.

Nadia a réagi la première, et pas comme je m'y attendais.

— La cellule antifraude va adorer. Une photo de dégât des eaux prise à vingt kilomètres du logement assuré, c'est exactement ce qu'ils cherchent.

— C'est aussi l'endroit où se trouvait l'assuré à un instant précis, a dit Mathilde. Conservé pendant dix ans dans un dossier que des dizaines de personnes consultent. Je ne décide pas ça seule.

Elle a appelé Anne-Sophie Dhondt sur le haut-parleur de la salle. La déléguée à la protection des données a écouté sans interrompre, puis elle a posé une seule question à Nadia.

— De quoi la cellule antifraude a-t-elle besoin pour faire son travail ? Pas envie. Besoin.

Nadia a réfléchi.

— De savoir si la photo est récente. Une photo prise avant la date du sinistre, ou trouvée sur internet, c'est le cas le plus fréquent. L'endroit, on le connaît déjà : c'est l'adresse du contrat. Et si on a un doute, l'expert se déplace.

— Alors on garde la date de prise de vue, et on retire la position, a dit Anne-Sophie Dhondt. C'est proportionné, et c'est défendable. Je l'écris dans l'analyse d'impact. D'ailleurs, il m'en faut une avant la mise en production : des photos de l'intérieur des logements, à cette échelle, ça ne se discute pas. Mathilde, vous pouvez m'aider à la rédiger cette semaine ?

La troisième question de Mathilde, *que se passe-t-il si quelqu'un ment ?*, a fait apparaître un second sujet. Le portail acceptait, pour le récépissé de plainte, des fichiers PDF. Un fichier PDF peut contenir autre chose qu'un document. Avant de rejoindre la gestion électronique des documents, où des gestionnaires l'ouvriraient sur leur poste, chaque fichier devait passer par le service d'analyse antivirus de la maison. Sofiane a vérifié : il existait, d'autres applications l'utilisaient déjà, le portail ne l'appelait pas.

Émilie a écrit les scénarios avant qu'on se lève. Une photo avec sa position, archivée sans sa position, avec sa date. Un PDF piégé de test, refusé avec un message clair pour l'assuré. Sofiane a ajouté un test à la chaîne d'intégration : aucune photo archivée ne devait contenir de coordonnées. L'agent a codé la story le lendemain matin, en suivant les scénarios, et il s'est arrêté une fois pour demander ce qu'il fallait faire d'une photo sans date de prise de vue. Nadia a répondu : l'accepter, et le signaler au gestionnaire. On ne bloque jamais une déclaration.

Avant de partir, Mathilde a ajouté deux lignes à nos définitions, au mur.

Dans la définition de « prête » : *les données personnelles manipulées par la story sont listées, et son niveau de risque est fixé.*

Dans la définition de « fini » : *pour une story rouge, les trois questions de sécurité ont reçu une réponse écrite.*

— Et tu ne seras là que deux jours par semaine, a dit Julien. Les trois autres, qui les pose, tes questions ?

— Toi. Sofiane. Et l'agent, dans sa consigne de relecture. Je ne veux pas devenir le nouveau goulot. J'ai lu ce qui t'était arrivé.

## Jeudi, 10 heures

La première réunion de l'instance commune s'est tenue le jeudi, dans une salle neutre du cinquième étage que personne n'avait jamais réservée, la salle Marque. Claire et Laurent Dewitte l'ont ouverte ensemble, assis côte à côte.

Il y avait deux sujets à l'ordre du jour. Le premier était le format des déclarations que le portail transmettrait au cœur de gestion, celui qu'Horizon était en train de refaire. Julien et Franck Ryckebusch, le directeur de projet de l'ESN, l'ont réglé en vingt minutes, ce qui a surpris tout le monde, eux compris. Dewitte a conclu le point d'une phrase que j'ai notée, parce qu'elle me resservirait :

— Ce format est un contrat entre nos deux équipes. Il doit être écrit, versionné, et signé des deux côtés. Personne ne le change sans l'autre.

Le second sujet était celui que la directrice générale avait imposé : les garde-fous de sécurité s'appliquaient désormais à toute la maison, y compris à Horizon. Mathilde a présenté le socle en cours d'écriture. Franck Ryckebusch l'a écoutée poliment, puis il a posé son stylo.

— Pour nous, la question ne se pose pas vraiment. Nos développeurs n'utilisent pas d'agents. Le contrat ne le prévoit pas.

Mathilde a ouvert un fichier sur son ordinateur et l'a affiché à l'écran. Elle l'avait préparé la veille, et elle avait prévenu Bertrand qu'elle le montrerait.

— Ce sont les statistiques du proxy de la maison, pour le mois dernier. Agrégées par entité, sans aucun nom, comme le prévoit la charte informatique. Je vois les volumes. Je ne vois pas les contenus.

Il y avait trois lignes. Les postes de l'ESN sur le programme Horizon : deux mille quatre cents connexions vers des assistants d'intelligence artificielle publics, des sites grand public, accessibles avec un simple compte personnel. Les équipes internes de la DSI : mille cent. L'équipe du pilote : zéro.

Personne n'a rien dit pendant un long moment. Franck Ryckebusch regardait le premier chiffre comme on regarde une facture qu'on n'attendait pas.

— Je ne peux pas vous dire ce qui a été collé dans ces outils, a repris Mathilde. Du code, sans doute. Peut-être des extraits de spécifications. Peut-être pire. Personne ne le sait, et c'est ça, le problème. Ce n'est pas de la malveillance. Ce sont des développeurs qui ont vu qu'un outil les aidait et à qui personne n'en a proposé un sûr.

J'ai pensé à Sofiane, le premier jour, avec son abonnement personnel et un mot de passe dans le code. Il n'avait rien fait d'autre. Lui, on l'avait vu.

— Pourquoi zéro, chez vous ? a demandé Dewitte.

— Parce qu'ils ont un outil autorisé, a dit Mathilde. Plus commode que le contournement. Interdire, la maison l'a fait. Ça donne le premier chiffre.

Dewitte a pris son temps. Je commençais à connaître ses silences ; celui-là n'était pas un calcul.

— Je préfère un outil cadré à un outil caché, a-t-il dit enfin. Franck, je veux qu'une équipe d'Horizon travaille avec le socle dès janvier, sur le compte AWS de la maison, avec les mêmes règles que le pilote. Il faudra un avenant au contrat, pour la confidentialité et la propriété du code. Et Bertrand devra l'inscrire au registre des prestataires informatiques.

— Mes équipes vont croire qu'on les surveille, a dit Ryckebusch.

— Le proxy est dans la charte depuis des années, a dit Mathilde, sans durcir le ton. Ce que je leur propose, c'est de ne plus avoir besoin de passer à côté.

Claire a noté la décision dans le compte rendu, et Dewitte l'a relu avant de signer. En sortant, il s'est arrêté à côté de Mathilde.

— Votre deuxième ligne, les mille cent des équipes internes. Vous la montrerez à la commission ?

— Oui. Avec la première.

— Bien, a-t-il dit. Sinon, j'aurais eu l'air d'être le seul à avoir un problème.

Il l'a dit en souriant. Mais il le pensait aussi.

## Mercredi, 15 heures

La commission sécurité se réunissait toutes les six semaines dans une salle sans fenêtre du sous-sol, à côté de la salle des serveurs que la maison n'utilisait presque plus. En octobre, elle avait prolongé la dérogation signée par Bertrand la première semaine, jusqu'à la fin du pilote. Ce mercredi-là, elle devait décider de la remplacer par une règle.

Autour de la table, il y avait Bertrand, qui présidait, Anne-Sophie Dhondt, le responsable de la production, la responsable de la gestion des risques, et Marc Vanhoutte, l'architecte du train Indemnisation, invité parce que la suite du portail se ferait chez lui. Mathilde et Julien présentaient. J'étais au fond, et je n'ai pas dit un mot de toute la séance, ce qui était exactement le rôle que je m'étais fixé.

Mathilde a projeté le socle. Il tenait en deux pages, comme Julien l'avait exigé. La première résumait tout le reste.

> **Socle d'usage des agents de développement — version 1**
>
> **Ce que l'agent a le droit de faire.** Lire et modifier le code du dépôt de son projet, lancer les tests, préparer des demandes de fusion. Jamais : lire les secrets, modifier les paramètres de sécurité ou de journalisation, fusionner lui-même.
>
> **Ce qui l'en empêche, même quand on oublie.** Des paramètres gérés par la sécurité, impossibles à désactiver. Un contrôle automatique de chaque modification. Des tests dans la chaîne d'intégration qui bloquent toute fusion fautive, quel qu'en soit l'auteur.
>
> **Comment on sait ce qu'il a fait.** Chaque modification porte la clé de sa story et mentionne l'agent comme co-auteur. Chaque demande de fusion porte le plan de l'agent et une approbation humaine. Les actions de l'agent sont journalisées, sans leur contenu, pendant douze mois.
>
> **Ce qui reste humain.** La relecture de tout ce qui est rouge par une personne qui connaît le système. La décision de fusionner. La responsabilité.
>
> **Données.** Aucune donnée de production dans un environnement de test sans anonymisation validée. Modèles accessibles uniquement par Amazon Bedrock, en région européenne.

Bertrand a lu la page en silence. Puis il a demandé à Julien d'ouvrir le code du portail, n'importe où.

— Non, a-t-il corrigé. Pas n'importe où. Là.

Il a désigné une ligne au hasard, au milieu du code qui conservait la nuit les déclarations en attente. Une ligne qui chiffrait un enregistrement.

— Je suis l'autorité de contrôle. Qui a écrit cette ligne, pourquoi, qui l'a relue, et l'agent y était-il ? Vous avez cinq minutes.

Julien n'en a pris que trois et quarante secondes. L'historique du fichier donnait la modification. La modification portait la clé de la story et mentionnait l'agent comme co-auteur. La story, dans Jira, renvoyait aux scénarios d'Émilie et à la question de Martine sur la nuit. La demande de fusion contenait le plan de l'agent, sa fiche de relecture, l'approbation de Gérard parce que la story était rouge, et les trois réponses écrites aux questions de Mathilde. Tout était là, relié, horodaté.

La responsable de la gestion des risques avait chronométré. Elle a noté le temps.

— Et si l'agent avait lancé une commande qu'il ne devait pas ? a demandé Bertrand.

Mathilde a ouvert le journal des actions de l'agent : chaque commande lancée, chaque fichier touché, avec l'heure et la session, sans le contenu. Elle a pris l'exemple qui faisait encore mal à tout le monde. La nuit du samedi, celle des dix approbations. On y voyait l'agent écrire la ligne fautive le vendredi à 16 heures, lancer ses tests, les voir passer, ouvrir la demande. On y voyait aussi qu'il n'avait rien fait d'autre que ce qu'on lui avait demandé. Ce qui avait manqué cette nuit-là, ce n'était pas une trace. C'était un relecteur reposé et un verrou. Personne n'a eu besoin de le dire.

La responsable de la gestion des risques a posé la question que j'attendais, celle de DORA.

— Si Bedrock tombe demain, ou si nous devons cesser d'utiliser ces modèles, que se passe-t-il ?

— Nous codons plus lentement, a dit Julien. Nous ne nous arrêtons pas. L'agent n'est sur aucun chemin de production. Le portail ne l'appelle jamais. Tout ce qu'il produit est du code ordinaire, relu, testé, qui appartient à la maison. Le jour où il disparaît, il ne nous reste que notre propre code. C'est le meilleur plan de sortie que je connaisse.

Marc Vanhoutte, qui n'avait encore rien dit, a demandé si le socle valait pour un train entier, avec plusieurs équipes et des dépendances entre elles.

— Pour la sécurité, oui, a dit Mathilde. Pour le reste, ce sera à vous de nous dire.

Il a hoché la tête et noté quelque chose. Je me suis dit que nous le reverrions bientôt.

Bertrand a demandé si quelqu'un s'opposait. Personne. Il a signé la page, en bas, à la main.

— Le socle remplace la dérogation. Il s'applique à toute équipe de la maison qui utilise un agent, à partir du premier janvier, y compris à l'équipe d'Horizon qui démarre. Mathilde, vous en êtes la responsable. Julien, vous en êtes le référent technique.

En rangeant ses affaires, il s'est tourné vers eux deux.

— Deux pages. C'est la règle la plus courte que cette commission ait jamais validée. J'espère que ce sera aussi la plus lue.

Dans l'escalier, Mathilde a demandé à Bertrand si elle pourrait garder ses deux jours par semaine avec l'équipe après la mise en production.

— Avec une équipe d'Horizon en janvier, et d'autres après, a-t-il répondu, il faudra que vous soyez partout à la fois. Faites-vous aider.

— Par l'agent ?

— Par Julien d'abord. Par l'agent ensuite.

Je suis remonté seul vers le septième étage. Le premier jour du projet, la sécurité avait dit non, dans un courriel de quatre lignes. Trois mois plus tard, elle venait d'écrire la règle qui permettait à toute la maison de dire oui.

## Le carnet de Thomas

**Ce qui s'est passé.** Après le Mercredi noir, l'auditrice sécurité s'est installée avec l'équipe deux jours par semaine, avec une mission : transformer les garde-fous du pilote en règle pour toute la maison. Les garde-fous existants vivaient en cinq endroits ; ils ont été regroupés dans un paquet unique, imposé par les paramètres gérés, complété par les tests de la chaîne d'intégration pour les équipes qui n'utilisent pas l'outil. La sécurité est entrée dans la préparation des stories : trois questions pour chaque story à risque ont fait apparaître la position GPS cachée dans les photos et l'absence d'analyse antivirus des fichiers. Les statistiques du proxy ont montré un usage massif et caché d'outils publics dans les autres équipes, et nul dans celle qui disposait d'un outil autorisé. La commission sécurité a vérifié qu'on pouvait retracer une ligne de code en moins de quatre minutes, puis validé un socle de deux pages pour toute la maison.

**La leçon.** La sécurité d'une équipe augmentée répond à trois questions : ce que l'agent a le droit de faire, ce qui l'en empêche même quand on oublie, et comment savoir après coup ce qu'il a fait. Empaquetez les réponses pour qu'une nouvelle équipe les reçoive sans rien installer, et gardez dans la chaîne d'intégration des contrôles indépendants de l'outil. Posez les questions de sécurité pendant la préparation de la story, pas à la fin ; la minimisation des données se décide avec le métier et la déléguée à la protection des données, en distinguant le besoin de l'envie. Interdire les outils ne supprime pas leur usage, cela le cache : offrez un cadre sûr plus commode que le contournement. Enfin, vérifiez que l'agent n'est sur aucun chemin critique : c'est votre meilleur plan de sortie.

**Trois questions à poser à votre équipe**

1. Si un auditeur désigne une ligne de notre code, combien de temps nous faut-il pour dire qui l'a écrite, pourquoi, qui l'a relue, et si un agent y a contribué ?
2. Quelles données nos fichiers transportent-ils sans que nous les ayons jamais regardées ?
3. Que se passerait-il demain si nous ne pouvions plus utiliser notre agent ?

**Pour aller plus loin.** Manuel, chapitres M4 (paramètres et permissions : paramètres gérés), M6 (hooks : contrôler et journaliser les actions de l'agent), M8 (plugins et marketplaces : empaqueter et distribuer un socle d'entreprise) et M12 (partager en équipe : ce qu'une nouvelle équipe reçoit le premier jour).
