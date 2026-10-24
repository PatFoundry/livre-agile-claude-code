# Chapitre 12 — La règle de franchise

## Lundi, 8 heures

Le bureau de Claire donnait sur la gare Lille-Europe. À 8 heures en novembre, on y voyait surtout le reflet de la pièce dans la vitre, et Claire, de dos, qui finissait un appel. Elle nous a fait signe de nous asseoir, à Nadia, à Julien et à moi, sans raccrocher.

Quand elle s'est retournée, elle a commencé par Nadia.

— Combien de dossiers ?

— Cent quatre. Dont trente et un en litige.

— Depuis le début du projet ?

— Depuis le début du projet.

Claire n'a pas fait de commentaire. Elle a composé un numéro sur son téléphone de bureau et mis le haut-parleur. Philippe Wattebled, le directeur de l'indemnisation, a décroché à la deuxième sonnerie. Je ne l'avais jamais rencontré. Il avait une voix lente, avec l'accent du Nord qu'on ne perd jamais vraiment.

— Philippe, c'est Claire. Tu m'as prêté Nadia Benali à plein temps pour le portail. Je découvre ce matin qu'elle gère toujours son portefeuille. Cent quatre dossiers.

Il y a eu un silence au bout de la ligne.

— On m'a dit qu'elle s'en sortait.

— Elle s'en sort la nuit.

Le silence a duré un peu plus longtemps. Puis Wattebled a dit qu'il répartirait les dossiers entre deux gestionnaires dès l'après-midi, et qu'il gardait les litiges pour lui jusqu'à la fin de la phase de développement. Il a demandé à parler à Nadia. Il lui a présenté des excuses, simplement, sans formule. Nadia a répondu qu'il n'y avait pas de quoi. Il y avait de quoi, et tout le monde le savait.

L'appel a duré quatre minutes. Nadia est restée immobile un moment après, les mains à plat sur ses genoux, comme quelqu'un qui pose un sac trop lourd et ne sait pas encore quoi faire de ses bras.

Puis Julien a présenté l'estimation de l'équipe, les deux phrases que Nadia avait écrites au tableau le vendredi. Claire les a lues deux fois.

— Le vol pour la mise en production, avec Nadia libérée. D'accord. Je le tiendrai.

— Et tous les sinistres avant l'été ? ai-je demandé.

— Ça, c'est mon problème. Pas le vôtre.

— Le comité a avancé son point d'étape. Dewitte y sera.

— Je sais. Je lui dirai moi-même que j'ai promis trop vite. Je préfère le dire avant qu'il le démontre.

Elle s'est levée : notre demi-heure était terminée, et la suivante l'attendait déjà dans le couloir. Sur le pas de la porte, elle m'a retenu une seconde.

— Vous aviez raison, devant les ascenseurs. Ne vous habituez pas.

J'ai pris cela pour un compliment. Je crois que c'en était un.

## Lundi, 15 heures

Gérard est monté du deuxième étage avec une liasse de papier sous le bras. Il imprimait encore les programmes COBOL qu'il relisait, sur du papier listing à bandes vertes qu'il gardait dans une armoire, et personne dans la maison n'avait jamais osé lui faire remarquer que cela ne se faisait plus.

Il relisait une demande rouge de Sofiane, celle qui enregistrait la date de découverte d'un vol dans le système des contrats. Il ne l'a pas commentée. Il a posé sa liasse sur le bureau de Julien et il a posé une question.

— Vous lisez la franchise où ?

Julien a ouvert le code du portail. La story s'appelait *Connaître sa franchise avant d'envoyer sa déclaration*. Elle avait été livrée au sprint 2. Nadia l'avait écrite après avoir entendu trop d'assurés découvrir leur franchise dans la lettre d'indemnisation. Avant l'envoi, le portail rappelait à l'assuré la franchise prévue par son contrat. Il ne bloquait rien : même sous la franchise, la déclaration restait possible, selon le principe que Nadia avait fait écrire dans les consignes de l'agent. On ne bloque jamais une déclaration.

— On interroge le système des contrats, a dit Julien. Avec le numéro de contrat. Il nous renvoie la franchise.

— Il vous renvoie la franchise d'aujourd'hui, a dit Gérard.

Personne n'a compris tout de suite. Il a déplié sa liasse.

— La franchise qui s'applique, c'est celle des conditions particulières en vigueur à la date du sinistre. Pas celle du jour où on déclare. La plupart du temps, c'est la même. Sauf quand il y a eu un avenant entre les deux.

Il nous l'a expliqué patiemment, comme il avait dû l'expliquer à des générations de développeurs. La franchise peut changer quand l'assuré modifie son contrat : il passe à une autre formule, il choisit une franchise plus élevée pour payer moins cher, il ajoute une dépendance, il déménage. Chaque modification donne lieu à un avenant, avec de nouvelles conditions particulières et une date d'effet. Le système des contrats en enregistrait plusieurs centaines par mois. Et la transaction appelée par le portail ne renvoyait que la dernière version.

— Prenez un assuré qui déménage, a dit Gérard. Dans son ancien appartement, il avait une franchise de cent cinquante euros. Pour le nouveau, plus grand, il a changé de formule, avec une franchise de trois cents euros. L'avenant porte une date d'effet, disons le premier du mois : avant cette date, c'est l'ancien contrat qui s'applique, après, le nouveau. Quelques jours plus tard, en vidant l'ancien logement, il découvre une fuite sous l'évier, qui coule depuis des semaines, bien avant la date d'effet. Il déclare une fois installé. Votre portail va lui afficher sa nouvelle adresse et sa nouvelle franchise. Avec deux cent quatre-vingts euros de dégâts, il va lire qu'il est sous la franchise. Votre portail le laissera déclarer quand même, mais il ne le fera pas. Il fermera l'application, et il paiera de sa poche les cent trente euros que nous lui devions. Et s'il déclare malgré tout, Martine recevra un dossier avec la mauvaise franchise.

Nadia est devenue pâle.

— Le déménagement, c'est l'un des moments où l'on découvre le plus de dégâts des eaux. On déplace la machine à laver, on vide les placards, on trouve le parquet gondolé. Et presque tout le monde déclare après, une fois les cartons défaits.

Nous sommes remontés le long de la chaîne, une étape après l'autre, comme on refait un trajet pour retrouver un objet perdu.

La story disait : *la franchise prévue par son contrat*. C'était vrai, et ce n'était pas assez. Les exemples de Nadia prenaient un contrat avec une franchise de cent cinquante euros, qui n'avait jamais été modifié. Le cas de test d'Émilie, écrit avant que nous ne la branchions sur l'agent, reprenait le même contrat. L'agent avait codé exactement ce qui était écrit, en appelant la seule transaction qu'on lui avait montrée, celle du squelette du sprint 0. Ses tests vérifiaient ce qu'il avait codé. Julien avait relu le code, Nadia avait vérifié les exemples en recette, Émilie avait exécuté son cas. Tout passait.

— Tout est cohérent, a dit Julien à voix basse. Et tout est faux.

Gérard a tapoté sa liasse.

— Il existe une autre transaction, qui lit le contrat à une date donnée. Je l'ai écrite en 1997, pour les sinistres déclarés en retard. Personne ne me l'a demandée.

— Personne ne savait qu'il fallait la demander, a dit Julien.

C'était vrai. C'était aussi exactement le problème.

## Mardi, 9 heures

Sofiane avait corrigé le code le soir même. Vingt minutes : l'agent avait remplacé la transaction du jour par celle de Gérard, à la date du sinistre. Puis il s'était arrêté sur une question, et il avait eu raison de le faire. Pour un vol, quelle date ? Celle du vol, que l'assuré ne connaît pas toujours, ou celle de la découverte ?

Cette question nous a réunis le mardi matin dans la salle Lys : Nadia, Gérard, Julien, Émilie, Sofiane et moi. J'ai écrit une seule phrase au tableau.

*Où est écrite la règle ?*

Il a fallu une heure pour faire l'inventaire, et l'inventaire était la réponse. La règle de la franchise n'était écrite nulle part en entier. Elle était éparpillée.

Il y avait les conditions générales du contrat habitation, soixante-quatre pages en PDF, édition 2019. Il y avait le guide de gestion des sinistres habitation, quatre-vingts pages complétées depuis 2016 par trois services différents, que Nadia consultait souvent sans l'avoir jamais lu en entier. Il y avait une note de service de 2009 sur les vols, que Gérard connaissait par cœur et que personne d'autre n'avait jamais lue. Et il y avait le programme COBOL de Gérard, qui appliquait la règle depuis vingt-cinq ans, avec ses exceptions.

Sofiane a donné les quatre documents à l'agent, avec une seule consigne : relever tout ce qui se contredisait. Cela lui a pris six minutes. Il en a trouvé quatre.

Le premier, nous le connaissions déjà : la date du contrat. Le deuxième concernait le vol : la note de service retenait la date de survenance quand elle était connue, sinon la date de découverte, alors que le programme COBOL prenait toujours la date de découverte. Le troisième, le plus gênant : quand un même sinistre déclenchait deux garanties, les conditions générales n'appliquaient qu'une franchise, la plus élevée, alors que le guide de gestion parlait d'une franchise *par garantie*. Le quatrième était une simple coquille dans le guide.

Nadia et Gérard en ont tranché trois en une demi-heure. Pour le vol, la note de service avait raison et le COBOL avait tort depuis 2009, sans que personne ne s'en soit jamais plaint. Gérard l'a reconnu avec une grimace. Le troisième point, ils ne pouvaient pas le trancher : il fallait la direction technique. Nadia a écrit le courriel séance tenante.

— La story dit ce qu'on veut, a dit Julien. Elle ne dit pas ce qui est vrai. Ce qui est vrai est éparpillé dans quatre documents et dans une tête qui part à la retraite en avril.

Gérard n'a pas protesté.

— Et mes cas de test ne valent que ce que valent leurs exemples, a dit Émilie. Il me faut des dates charnières. Une fuite survenue la veille d'un avenant et déclarée le lendemain. Un déménagement. Un vol découvert au retour de vacances, survenu on ne sait quand.

Sofiane, lui, regardait le tableau avec une lueur que je commençais à connaître.

— Il faudrait changer de façon de faire. Partir de spécifications écrites, versionnées, et faire générer le code à partir d'elles. Il y a des méthodes pour ça, maintenant. J'ai lu des choses sur le spec-driven development, sur BMAD…

— Pas maintenant, ai-je dit. Il reste quatre semaines de développement. On ne change pas de méthode en fin de phase. Mais on peut faire un petit pas sans casser la chaîne.

Le petit pas a été un dossier dans le dépôt, appelé simplement *règles*, et un premier fichier dedans, pour la franchise. Chaque règle y serait écrite une seule fois, avec sa source, ses dates de validité, et le nom de ceux qui l'avaient validée. Les stories y renverraient, au lieu de la paraphraser. Toute modification passerait par une demande de fusion relue par Nadia, et par Gérard tant qu'il était là. Une ligne a été ajoutée au fichier de consignes de l'agent : *Pour toute règle de gestion, lis d'abord le dossier des règles. Si une règle manque ou se contredit, arrête-toi et pose la question.*

Nadia a écrit la première règle elle-même.

> **Règle F1 — Franchise applicable**
>
> La franchise est celle des conditions particulières en vigueur à la date de survenance du sinistre, même si un avenant a pris effet depuis.
>
> Vol : si la date de survenance est inconnue, on retient la date de découverte.
>
> Plusieurs garanties pour un même sinistre : à confirmer par la direction technique.
>
> Sources : conditions générales habitation, édition 2019 ; guide de gestion des sinistres habitation ; note de service sur les vols, 2009.
>
> Validée par : Nadia Benali, Gérard Vandamme.

Puis Sofiane a demandé à l'agent de relire toutes les stories livrées, à la recherche du même défaut : une règle qui dépendait d'une date, codée avec le contrat du jour. Il en a trouvé deux autres. Le plafond des objets de valeur pour le vol, qui dépendait lui aussi des conditions particulières, et donc des avenants. Et la liste des garanties souscrites, affichée à l'assuré au début du parcours.

— Garde ton idée de méthode, ai-je dit à Sofiane en sortant. On en reparlera quand la phase sera finie.

— Je la garde, a-t-il répondu. Je l'ai même notée.

## Mardi, 18 heures

Julien et moi sommes restés après les autres, devant le tableau de la salle Lys. La règle F1 était encore écrite dans un coin, à côté de la question du matin.

— Tu sais ce qui me gêne le plus ? a dit Julien. Ce n'est pas l'erreur. Des règles mal comprises, j'en ai vu passer toute ma carrière. C'est la vitesse. Il y a vingt ans, on mettait trois mois à coder une règle fausse. Pendant ces trois mois, on croisait Gérard à la machine à café, on lui parlait de ce qu'on faisait, et il finissait par nous dire : « Vous lisez la franchise où ? » Maintenant, on met trente-cinq minutes. On n'a plus le temps de croiser personne.

— Les machines à café ne sont pas une méthode, ai-je dit.

— Non. Mais elles faisaient le travail d'une méthode qu'on n'avait pas.

J'ai repensé à mon premier soir sur ce projet, chez moi, devant mon ordinateur. L'agent avait inventé une franchise de cent cinquante euros que personne ne lui avait demandée, et j'avais compris ce soir-là qu'il fallait lui dire les choses. Cette fois, il n'avait rien inventé. C'était pire. Il avait codé fidèlement ce que nous lui avions dit, et ce que nous lui avions dit était incomplet. Il avait été parfaitement obéissant, et parfaitement à côté.

— Sofiane veut changer de méthode, a dit Julien.

— Je sais. Il a peut-être raison. Mais pas en fin de phase. On ne change pas de moteur pendant l'atterrissage.

Julien a souri, pour la première fois de la journée.

— Tu as la phrase pour tout, toi.

Avant de partir, j'ai noté trois lignes dans mon carnet, le vrai, celui en papier.

*La story dit ce qu'on veut. La règle dit ce qui est vrai.*

*L'agent code ce qu'on écrit, pas ce qu'on sait.*

*Un jour, il faudra que la règle passe avant la story.*

En rangeant mes affaires, j'ai jeté un dernier coup d'œil au tableau du sprint dans Jira. Le ticket de Sylvie, *Relire à nouveau les dix demandes approuvées dans la nuit de samedi*, avait fini par entrer dans le sprint, toujours en priorité moyenne. Julien l'avait planifié pour le jeudi, une fois que Gérard aurait fini de relire le rouge.

Dans ma boîte de réception, une invitation de Mathilde attendait depuis l'après-midi : *Mercredi, 9 heures. Contrôle des journaux de recette, revue trimestrielle.* Je l'ai acceptée sans y penser.

Le ticket était prévu pour le jeudi. Le mercredi est arrivé avant.

## Le carnet de Thomas

**Ce qui s'est passé.** Une story livrée et validée affichait à l'assuré la franchise de son contrat avant l'envoi, sans jamais bloquer la déclaration. Le code lisait la franchise du jour, alors que la règle impose celle du contrat en vigueur à la date du sinistre. Chaque fois qu'un avenant, après un déménagement ou un changement de formule, avait pris effet entre le sinistre et la déclaration, l'assuré risquait de lire à tort qu'il était sous la franchise et de renoncer à une déclaration à laquelle il avait droit ; le gestionnaire, lui, aurait reçu un dossier avec la mauvaise franchise. La story, les exemples, le cas de test, le code, les tests et la relecture étaient cohérents entre eux, et tous faux. La règle n'était écrite nulle part en entier : elle était éparpillée entre les conditions générales, un guide de gestion, une note de service et un programme COBOL, avec quatre contradictions. L'équipe n'a pas changé de méthode à quatre semaines de la fin des développements. Elle a créé un dossier de règles de gestion dans le dépôt, sourcées et validées, auquel renvoient les stories et les consignes de l'agent.

**La leçon.** Une user story dit ce que l'on veut ; elle ne dit pas ce qui est vrai. Un agent code ce qu'on lui écrit, pas ce que l'entreprise sait : il ne pose pas les questions dont il ignore l'existence. Les tests, même écrits avant le code, ne valent que ce que valent leurs exemples, d'où l'importance des cas limites, et en assurance surtout des dates charnières : date d'effet d'un avenant, déménagement, changement de formule, date de découverte. Écrivez chaque règle une seule fois, avec sa source, ses dates de validité et ceux qui l'ont validée, et demandez à l'agent de s'arrêter quand une règle manque ou se contredit. C'est le premier pas vers une spécification qui précède le code ; pour aller plus loin, attendez la fin de la phase.

**Trois questions à poser à votre équipe**

1. Où sont écrites nos règles de gestion, et combien de versions contradictoires en existe-t-il ?
2. Nos exemples couvrent-ils les dates charnières : avenant, déménagement, changement de formule ?
3. Qui, dans l'entreprise, détient une règle que personne n'a jamais écrite ?

**Pour aller plus loin.** Manuel, chapitres M3 (CLAUDE.md et la mémoire : renvoyer l'agent vers un dossier de règles), M11 (le wiki d'équipe : rassembler un savoir éparpillé) et M13 (bonnes pratiques : faire relever les contradictions par l'agent).
