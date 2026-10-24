# Chapitre 13 — Mercredi noir

## Mercredi, 9 heures

Mathilde est arrivée à l'heure, comme toujours, mais elle ne s'est pas assise.

Elle a posé son ordinateur sur la table de la salle Lys, l'a tourné vers moi, et elle a attendu que je lise. Sur l'écran, une recherche dans la plateforme de journaux de la DSI, celle où toutes les applications de la maison envoient leurs traces, de la paie au site internet. Une liste de lignes, toutes semblables. Un horodatage, le nom de notre service, le mot *DEBUG*, puis un long bloc de texte.

Dans chaque bloc, il y avait une adresse postale. Un numéro de téléphone portable. Une adresse électronique.

— C'est la recette, ai-je dit. Ce sont des données de test.

— C'est ce que je pensais aussi, il y a quarante minutes.

Elle a sélectionné une ligne au hasard. Une adresse à Tourcoing, rue de Lille. Elle a ouvert l'annuaire des assurés en production, sur son second écran, avec ses droits d'auditrice. Le numéro de téléphone y était. L'adresse aussi. Le nom n'était pas le même : dans la recette, la personne s'appelait *Delphine Mortier* ; en production, quelqu'un d'autre. Tout le reste était vrai.

— La base de recette du système des contrats est une copie de la production, a dit Mathilde. Elle est anonymisée chaque mois par un script. Le script brouille les noms et les dates de naissance. Il laisse le reste.

— Combien ?

— Quatorze mille lignes, depuis vingt-cinq jours. Mille trois cent douze contrats différents. Et la plateforme les garde treize mois.

J'ai fait le calcul que tout le monde fait dans ces cas-là, et qui ne sert à rien : mille trois cent douze personnes réelles, avec leur adresse, leur téléphone et leur courriel, dans un outil que des centaines de comptes pouvaient consulter.

Julien est entré à 9 h 10, un café à la main. Il a vu nos têtes, puis l'écran. Il a posé son café sans le boire.

Il ne lui a fallu que deux minutes pour trouver d'où venaient les lignes. Une seule instruction, dans le code du téléversement des photos. Quand un envoi échouait, et aussi quand il réussissait, elle écrivait dans les journaux tout ce que le portail avait sous la main : la déclaration complète et le contrat renvoyé par le système des contrats. En recette, le niveau de détail était au maximum. Tout partait.

Julien a ouvert la demande de fusion qui avait introduit cette ligne. *Ajout de journaux détaillés pour diagnostiquer les échecs de téléversement.* Le plan de l'agent, joint à la demande, disait en toutes lettres : *journaliser la requête complète et la réponse du système des contrats, pour faciliter le diagnostic*. Il n'avait rien caché. Personne ne lui avait jamais dit de ne pas le faire. Le fichier de consignes interdisait d'écrire un secret dans le code ; il ne disait pas un mot des journaux.

En bas de la demande, il y avait l'approbation. Samedi, 1 h 34. Un seul mot.

*OK.*

Julien l'a regardé longtemps. Il n'a pas dit « c'est moi ». Il n'en avait pas besoin, son nom était écrit à côté.

— La neuvième, a-t-il dit seulement.

Puis il a pris son téléphone et il a ouvert le tableau du sprint. Le ticket de Sylvie, *Relire à nouveau les dix demandes approuvées dans la nuit de samedi*, était toujours là, en priorité moyenne, prévu pour le lendemain.

— Demain, a-t-il dit. C'était prévu pour demain.

Mathilde a regardé sa montre.

— J'ai ouvert un incident de sécurité à 8 h 52. Bertrand arrive. La déléguée à la protection des données aussi. À partir de maintenant, nous avons soixante-douze heures.

## Mercredi, 10 heures

Bertrand est arrivé dans la salle Scarpe avec Anne-Sophie Dhondt, la déléguée à la protection des données. Je ne l'avais jamais rencontrée. Elle portait un classeur épais, qu'elle a posé devant elle sans l'ouvrir. Bertrand, lui, n'avait rien apporté. Il a pris un feutre et il a écrit trois questions au tableau.

*Est-ce que ça coule encore ? Qui a pu voir ? Que devons-nous déclarer ?*

— Dans cet ordre, a-t-il dit. Et pas une autre question avant d'avoir répondu à celle-là.

Sofiane avait déjà ouvert une session.

— Je peux faire supprimer la ligne par l'agent et purger les journaux. Cinq minutes.

— Personne ne supprime rien, a dit Bertrand. D'abord, on préserve. Ensuite, on arrête. Ensuite seulement, on purge. Si vous effacez maintenant, vous effacez aussi la preuve de ce qui s'est passé, et la seule chose que nous pourrons dire à la CNIL, c'est que nous ne savons pas.

Mathilde a extrait les quatorze mille lignes dans un espace sécurisé réservé aux enquêtes, avec leur empreinte, pour pouvoir prouver plus tard qu'elles n'avaient pas été modifiées. Puis Julien a abaissé le niveau de détail des journaux du portail en recette. Mathilde regardait son écran par-dessus son épaule pendant qu'il le faisait. Personne ne l'avait demandé ; personne n'aurait voulu qu'il le fasse seul.

C'est Émilie qui a compris pourquoi le nombre de contrats était si élevé.

— Ce sont mes scénarios, a-t-elle dit, très bas. Depuis la semaine dernière, ils tournent chaque nuit sur cinquante contrats tirés au hasard dans la base de recette. Pour couvrir des cas que je n'aurais pas imaginés.

Elle a suspendu les exécutions de nuit. Personne ne lui a reproché quoi que ce soit. Ce que nous avions fait de mieux la semaine précédente avait multiplié par dix ce que nous avions fait de pire trois semaines plus tôt. Je l'ai noté dans mon carnet, sans savoir encore quoi en faire.

À 10 h 25, Bertrand a rayé la première question. Ça ne coulait plus.

La deuxième a pris plus longtemps. Mathilde a interrogé les droits de la plateforme de journaux. Les traces de recette de toutes les applications étaient rangées ensemble, lisibles par deux cent quatre-vingt-sept comptes. Parmi eux, quarante et un appartenaient à l'ESN qui développait Horizon : on leur avait ouvert l'accès, des années plus tôt, « pour faciliter le diagnostic des interfaces ». La plateforme gardait aussi la trace de chaque recherche. Sur vingt-cinq jours, trois comptes avaient affiché nos lignes. Le premier était celui de Sofiane, qui cherchait justement pourquoi des photos échouaient. Les deux autres appartenaient à l'ESN. Ils ne cherchaient rien : leur tableau de bord des erreurs agrégeait toutes les applications de recette, et il tournait en continu sur un grand écran, au sixième étage, dans l'open space d'Horizon.

Personne n'a rien dit pendant un moment.

Puis Bertrand a fait appeler Gérard, parce que la base de recette était la sienne. Il est monté avec ses lunettes de lecture à la main. Mathilde lui a montré une ligne. Il a hoché la tête avant même d'avoir fini de la lire.

— Le script d'anonymisation date de 2014. On a ajouté le téléphone portable et le courriel aux contrats en 2018, pour les notifications par SMS. Le script ne les connaît pas. Je l'ai signalé en 2019. Il y a un ticket.

Sylvie, qui était restée au fond de la salle sans que personne le lui demande, a retrouvé le ticket en deux minutes. Ouvert en mars 2019. Jamais traité. Priorité moyenne.

C'était le deuxième ticket en priorité moyenne de la journée. Il était à peine plus de dix heures.

Anne-Sophie Dhondt a enfin ouvert son classeur. Elle a posé ses questions une par une, et elle a noté chaque réponse à la main. Quelles données, exactement ? Des coordonnées : adresse, téléphone, courriel. Aucune donnée bancaire, aucune donnée de santé ; les descriptions de sinistres, elles, étaient celles des tests. Combien de personnes ? Mille trois cent douze. Vues par qui ? Par des salariés et par un prestataire lié par une clause de confidentialité, sans intention malveillante connue. Pendant combien de temps ? Vingt-cinq jours, et visibles treize mois si l'on ne faisait rien.

— C'est une violation de données personnelles, a-t-elle conclu. Une atteinte à la confidentialité. Le risque pour les personnes me paraît limité : je ne prévois pas de les informer individuellement. Mais l'accès était large et la durée longue. Le délai court jusqu'à samedi 8 h 52 ; je notifierai la CNIL dès demain. Il me faut la liste des comptes, la preuve de la purge, et les mesures que vous prenez pour que ça ne recommence pas.

Bertrand a ajouté que l'incident serait aussi inscrit au registre des incidents informatiques que la maison tient pour DORA. Il n'aurait pas de conséquence sur le service, puisque rien n'était en production, mais il remonterait au comité des risques.

Je suis sorti à 10 h 40 pour appeler Claire. Je voulais qu'elle l'apprenne par moi, comme Bertrand l'avait appris par moi dix semaines plus tôt, le jour où Sofiane avait installé l'outil avec son abonnement personnel. Elle a écouté sans m'interrompre. Puis il y a eu un silence.

— L'écran du sixième étage, c'est l'open space d'Horizon ?

— Oui.

— Alors Laurent le sait déjà. Ou il le saura avant midi.

Elle n'a pas crié. Elle n'a pas demandé qui. Elle a seulement dit :

— Faites tout dans les règles, Thomas. Tout. Je ne veux pas une virgule de travers.

Quand je suis revenu dans la salle, Julien était en train d'expliquer à Bertrand que c'était sa faute, entièrement, qu'il avait approuvé cette demande sans la lire, à une heure et demie du matin, et qu'il en assumerait les conséquences.

Bertrand l'a laissé finir.

— Nous parlerons des causes vendredi, a-t-il dit. Toutes les causes. Aujourd'hui, nous fermons les robinets.

## Mercredi, 15 heures

L'après-midi, Mathilde est venue s'asseoir à côté de Sofiane et de Julien. Elle avait fermé son ordinateur d'auditrice et ouvert le leur.

— Avant de corriger, a-t-elle dit, je veux savoir s'il y en a d'autres.

Sofiane a ouvert une session neuve et donné à l'agent une seule consigne : relire tout le code du portail et lister chaque endroit où une donnée personnelle pouvait finir dans un journal, directement ou au travers d'un objet complet. Il a fallu onze minutes. L'agent en a trouvé trois.

La première était la nôtre, celle de la nuit de samedi. La deuxième était plus discrète : en cas d'erreur de validation, le portail renvoyait le message d'erreur complet du formulaire, qui contenait le numéro de téléphone saisi par l'assuré. La troisième était dans le squelette du sprint 0, la toute première version du portail. Quand l'appel au système des contrats échouait, elle écrivait le numéro de contrat et le nom de l'assuré.

Julien a ouvert l'historique de ce fichier. Il a regardé l'auteur.

— Celle-là, c'est moi, a-t-il dit. Un mardi à 15 heures, en pleine forme. Sans agent.

Mathilde n'a pas souri.

— C'est pour ça que je ne vous demanderai pas une consigne de plus. Une consigne, l'agent l'aurait respectée, si quelqu'un avait pensé à l'écrire. Mais vous, Julien, vous n'avez pas de fichier de consignes. Il nous faut quelque chose qui arrête tout le monde.

C'était la leçon du sprint 0, celle du fichier de mots de passe oublié dans un vieux répertoire : une consigne se négocie, un verrou ne se négocie pas. Mathilde nous l'a fait appliquer à trois niveaux, cet après-midi-là.

Le premier était bien une consigne, parce qu'il en faut une. Nadia et Julien ont ajouté trois lignes au fichier de consignes de l'agent : ne jamais écrire dans un journal un nom, une adresse, un téléphone, un courriel ou un numéro de contrat ; ne jamais y écrire un objet complet ; utiliser à la place l'identifiant technique de la déclaration, qui ne dit rien à personne en dehors du portail.

Le deuxième niveau vivait dans l'outil lui-même. Sofiane a écrit, avec l'agent, un petit programme de contrôle que l'outil déclenche automatiquement avant chaque modification de fichier. Il examine le code que l'agent s'apprête à écrire et refuse toute instruction de journalisation qui manipule un objet complet ou un champ de données personnelles. Mathilde a ajouté ce contrôle aux paramètres gérés par la sécurité, ceux qu'aucun poste ne peut désactiver. Elle y a ajouté une interdiction : l'agent ne pourrait plus modifier les fichiers qui fixent le niveau de détail des journaux.

— On essaie, a-t-elle dit.

Sofiane a demandé à l'agent exactement ce qu'on lui avait demandé vingt-cinq jours plus tôt : ajouter des journaux détaillés pour comprendre pourquoi certains envois de photos échouaient. L'agent a proposé son plan. Il a commencé à écrire. Le contrôle l'a arrêté net.

*Modification refusée : journalisation d'un objet susceptible de contenir des données personnelles. Journalisez l'identifiant technique de la déclaration et le code d'erreur.*

L'agent a relu le message, puis il a réécrit sa ligne : l'identifiant de la déclaration, la taille du fichier, son format, le code d'erreur renvoyé. Tout ce qu'il fallait pour diagnostiquer, rien de ce qui permettait de reconnaître quelqu'un. Julien l'a lu deux fois.

— C'est mieux que ce que j'aurais écrit.

Le troisième niveau ne dépendait ni de l'agent, ni de l'outil. Il vivait dans la chaîne d'intégration continue, sur GitHub, et il s'appliquait à tout le monde. Après chaque exécution des scénarios d'Émilie, un test lisait tous les journaux produits et échouait s'il y trouvait une adresse électronique, un numéro de téléphone, un numéro de compte bancaire ou un numéro de contrat. Une demande de fusion qui faisait échouer ce test ne pouvait plus être fusionnée, quel que soit son auteur, et quelle que soit l'heure.

Pour le vérifier, Julien a écrit lui-même, à la main, une ligne fautive dans une branche de test. Il a poussé. Le test est passé au rouge en quatre minutes.

— À une heure et demie du matin, a-t-il dit, je n'aurais même pas pu l'approuver.

Il n'y avait aucune amertume dans sa voix. Plutôt une forme de soulagement.

Ce soir-là, Julien et Gérard sont restés jusqu'à 20 heures pour relire les dix demandes de la nuit de samedi, une par une, avec les fiches de relecture que l'agent préparait désormais. Ils n'ont rien trouvé d'autre de grave. Une fonction mal nommée, un test inutile. Rien qui ne justifie une nuit blanche, et pourtant c'est une nuit blanche qui les avait produites.

Avant de partir, Julien a ouvert le ticket de Sylvie et l'a passé en *terminé*. Avec un jour d'avance.

## Vendredi, 10 heures

Le jeudi, tout ce qui devait être fait l'a été, dans l'ordre que Bertrand avait écrit au tableau. Les lignes ont été purgées de la plateforme, après que Mathilde en eut conservé la copie scellée. Les traces de recette de chaque application ont été séparées, et l'accès des comptes de l'ESN à celles du portail a été fermé. À 16 heures, Anne-Sophie Dhondt a envoyé sa notification à la CNIL. Elle nous en a transmis une copie, quatre pages sobres, sans un adjectif.

Le vendredi matin, j'ai réuni tout le monde dans la salle Deûle pour la revue de l'incident. Mathilde et Gérard étaient là, Sylvie aussi. Bertrand avait dit qu'il passerait une demi-heure. Il est resté jusqu'à la fin.

J'ai commencé par écrire en haut du tableau la règle de ces réunions, la même qu'en rétrospective : on cherche ce qui s'est passé et pourquoi, pas qui. Puis Mathilde a dessiné la chronologie. Le samedi, 1 h 34, l'approbation. Le lundi, la mise en recette. La semaine précédente, les scénarios de nuit. Le mercredi, 8 h 52, la détection, et 10 h 25, l'arrêt. Le jeudi, 16 heures, la notification.

Julien a voulu parler le premier, et je l'ai laissé faire, parce que je savais qu'il ne pourrait rien écouter d'autre tant qu'il ne l'aurait pas dit.

— La cause, c'est que j'ai approuvé cette demande à une heure et demie du matin sans la lire.

— C'est un fait, a dit Bertrand. Ce n'est pas une cause. Si la cause est un homme fatigué, la solution est un homme reposé, et cela ne tient jamais longtemps. Je veux les causes qui restent quand tout le monde a dormi.

Nous les avons cherchées pendant une heure, en remontant chaque fois d'un cran : pourquoi cela a-t-il été possible ? Quand nous avons fini, il y en avait six au tableau.

*Une relecture faite seul, de nuit, sous la pression d'un engagement.*

*Des consignes de l'agent muettes sur les données personnelles dans les journaux.*

*Aucun contrôle automatique, ni dans l'outil, ni dans la chaîne.*

*Une base de recette mal anonymisée depuis 2018, signalée en 2019, jamais corrigée.*

*Une plateforme de journaux où les traces de recette étaient lisibles par deux cent quatre-vingt-sept comptes, prestataires compris.*

*Des scénarios automatiques qui tiraient chaque nuit des contrats au hasard dans cette base.*

Personne n'a parlé pendant un moment. C'est Mathilde qui a dit ce que chacun était en train de compter.

— Deux causes sur six concernent l'agent. Les quatre autres existaient avant qu'il arrive. Certaines depuis des années.

Elle s'est tournée vers Bertrand.

— Il n'a pas créé ces trous. Il les a trouvés plus vite que nous.

Bertrand a regardé le tableau longtemps, les bras croisés. Puis il a pris sa décision, et il l'a annoncée comme il annonçait toutes les siennes, sans préambule.

— L'usage continue. Je ne vais pas interdire l'outil qui vient de nous montrer en onze minutes trois fuites qu'aucun audit n'avait vues. Je vais interdire de s'en servir sans ceinture. Les trois niveaux de mercredi deviennent obligatoires pour toute équipe de la maison qui utilise un agent, dès lundi : dans les paramètres gérés pour l'outil, dans la chaîne d'intégration pour le reste. Le ticket de 2019 passe en priorité haute.

Il s'est tourné vers Gérard.

— Monsieur Vandamme, vous partez en avril.

— Le 11, a dit Gérard.

— J'aimerais que ce script soit corrigé avant le 11.

Gérard a regardé Sofiane, puis l'ordinateur de Sofiane.

— Avec son machin, a-t-il dit, ça devrait prendre moins de cinq ans.

C'est la seule fois de la matinée où la salle a ri.

En sortant, Sylvie m'a rattrapé dans le couloir, son ordinateur contre la poitrine.

— Pour le tableau de bord du comité, je mets quoi ?

— La vérité. L'incident, les six causes, les mesures. Et la date du ticket de 2019.

Elle a hésité une seconde.

— Je mets la date.

À 17 h 12, Claire m'a transféré un message que Laurent Dewitte avait adressé le matin même aux membres du comité de direction. Il était court, courtois, impeccable.

> *Mes équipes ont constaté mercredi, sur leurs écrans de supervision, la présence de données personnelles d'assurés dans les journaux de recette du pilote de déclaration en ligne. L'incident a été traité. Il illustre toutefois les risques d'une démarche menée hors du cadre méthodologique et de sécurité du programme Horizon. Je propose au comité d'étudier, lors de son point d'étape de jeudi, les conditions d'une reprise du pilote dans ce cadre.*

Claire avait ajouté trois mots au-dessus : *Jeudi. Préparez-vous.*

J'ai relu le message de Dewitte deux fois. Il n'y avait pas une erreur dedans. Il y manquait seulement une date : mars 2019.

## Le carnet de Thomas

**Ce qui s'est passé.** Une demande de fusion approuvée en pleine nuit ajoutait des journaux détaillés pour diagnostiquer des envois de photos. Elle écrivait la déclaration et le contrat complets dans les traces de recette. Or la base de recette, copie de la production, n'était anonymisée qu'en partie : pendant vingt-cinq jours, les coordonnées réelles de mille trois cent douze assurés se sont retrouvées dans une plateforme lisible par deux cent quatre-vingt-sept comptes, dont ceux d'un prestataire. L'auditrice sécurité l'a détecté lors d'un contrôle de routine. L'équipe a préservé les preuves, arrêté la fuite, établi qui avait pu voir, puis purgé ; la déléguée à la protection des données a notifié la CNIL dans le délai de soixante-douze heures. Trois niveaux de garde-fous ont été posés le jour même. La revue de l'incident a mis au jour six causes, dont quatre antérieures à l'arrivée de l'agent.

**La leçon.** Un agent ne crée pas les failles d'un système d'information ; il les emprunte plus vite, et plus souvent. Face à un incident, l'ordre compte : préserver les preuves, arrêter la fuite, savoir qui a pu voir, puis seulement corriger et purger. Les garde-fous doivent arrêter tout le monde, humains compris : une consigne dans le fichier de l'agent, un contrôle automatique dans l'outil qu'aucun poste ne peut désactiver, et un test dans la chaîne d'intégration qui bloque toute fusion fautive, quelle que soit l'heure. Enfin, une revue d'incident qui s'arrête à « quelqu'un était fatigué » n'a rien trouvé : cherchez les causes qui restent quand tout le monde a dormi.

**Trois questions à poser à votre équipe**

1. Nos environnements de recette contiennent-ils des données réelles, et qui peut lire leurs journaux ?
2. Qu'est-ce qui, aujourd'hui, empêcherait automatiquement un humain ou un agent d'écrire une donnée personnelle dans un journal ?
3. Depuis combien de temps dort le plus vieux ticket de sécurité de notre maison, et en quelle priorité ?

**Pour aller plus loin.** Manuel, chapitres M4 (paramètres et permissions : paramètres gérés, interdictions de modification), M6 (hooks : bloquer une modification avant qu'elle soit écrite), M10 (GitHub et Jira : un contrôle de la chaîne d'intégration qui s'applique à tous) et M13 (bonnes pratiques : journaliser sans exposer).
