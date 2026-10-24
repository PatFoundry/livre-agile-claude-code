# Chapitre 1 — Quatorze semaines

## Lundi, 8 h 40

Mon badge ne fonctionnait pas. L'agent d'accueil l'a passé trois fois sur le lecteur, a soupiré, puis a décroché son téléphone. Derrière les vitres du hall, les premiers voyageurs du TGV de Paris traversaient le parvis de Lille-Europe, la tête dans leur écran.

En vingt-cinq ans de missions dans la banque et l'assurance, je n'ai jamais vu un badge fonctionner le premier jour. J'ai cessé de m'en agacer. C'est une information comme une autre : l'entreprise sait recruter, elle ne sait pas encore accueillir.

Claire Vasseur est descendue elle-même me chercher. La quarantaine, une veste sombre, un ordinateur sous le bras et deux téléphones dans la main. Elle m'a serré la main sans ralentir.

— Thomas. Merci d'être venu si vite. On monte, j'ai vingt minutes avant le comité.

Elle en a pris trente-cinq.

## Le pari

Son bureau, au sixième, donnait sur les tours d'Euralille. Sur le tableau blanc, quelqu'un avait collé un planning imprimé en A3. Un diagramme de Gantt, avec beaucoup de rouge et un mot en capitales : HORIZON.

— Vous connaissez Horizon ?

— Ce qu'on en dit à Lille.

Il y avait peu de choses à savoir et beaucoup à deviner. Horizon était le programme de refonte de la gestion des sinistres, confié trois ans plus tôt à une grande ESN parisienne. Quarante personnes, un cycle en V irréprochable sur le papier, et un budget dont plus personne ne citait le montant à voix haute.

— Le lot « déclaration en ligne » était prévu pour ce printemps, a dit Claire. Il est maintenant annoncé pour 2028. Et la semaine dernière, la Prévoyance du Nord a lancé son portail.

Elle a tourné son écran vers moi. Une application sobre : photos prises depuis le téléphone, quelques questions simples, un accusé de réception en trente secondes.

— Notre directeur général l'a testée dimanche. Il a déclaré un dégât des eaux imaginaire. Lundi matin, il m'a demandé pourquoi il nous fallait deux ans de plus.

— Et vous lui avez répondu ?

— Que je pouvais le faire en quatorze semaines.

J'ai attendu. En réunion, le silence est l'outil le moins cher et le plus sous-employé.

— Avec qui ? ai-je fini par demander.

— Une équipe de cinq. Une Product Owner venue du métier, un tech lead, un développeur, une testeuse. Et vous pour diriger.

— Ça fait quatre, plus moi.

— Plus Claude Code.

J'avais déjà entendu ce genre de phrase. À la fin des années 1990, c'était un atelier de génie logiciel qui devait rendre les développeurs inutiles. Dix ans plus tard, l'offshore. Puis le low-code. Chaque fois, l'outil était réel. La promesse, jamais.

— Qu'avez-vous promis exactement au comité ?

Elle a hésité une seconde de trop.

— Un portail en production avant la campagne de renouvellement de janvier. Et une productivité multipliée par trois par rapport à Horizon.

— Le chiffre vient d'où ?

— D'un article. Et d'une démonstration faite par un éditeur.

J'ai posé mon stylo.

— Alors je vais vous dire ce que je peux promettre aujourd'hui : rien. Dans trois semaines, je pourrai vous dire ce qui est faisable, avec des mesures. Si vous avez besoin d'un chiffre avant, il faut prendre quelqu'un d'autre.

Elle m'a regardé longtemps. Puis elle a souri, d'un sourire fatigué.

— C'est pour ça que je vous ai choisi. Le comité m'a donné quatorze semaines, pas une de plus. Si on échoue, le lot repart chez Horizon et l'expérience est enterrée. Avec moi dedans.

J'ai enchaîné avec les questions que je pose toujours le premier jour. Qui décide de ce que fait le produit ? Nadia Benali, quinze ans de gestion de sinistres, jamais Product Owner. Qu'a-t-on le droit de faire avec les données des assurés ? Claire n'en savait rien. Le RSSI était-il au courant ?

— Je comptais le voir cette semaine.

J'ai noté son nom dans mon carnet et je l'ai souligné deux fois.

## Le soir

Je n'ai jamais su juger un outil sur une démonstration. Ce soir-là, dans mon appartement du Vieux-Lille, j'ai installé Claude Code sur mon ordinateur personnel. Pas sur le poste de la mutuelle : je n'en avais pas encore, et je n'avais surtout aucune autorisation.

J'utilisais déjà des assistants conversationnels pour relire mes notes ou reformuler un mail délicat. Un agent qui travaille directement dans un projet, lit les fichiers, lance des commandes et écrit du code, je n'avais jamais essayé.

J'ai créé un dossier vide et j'ai tapé, en français, ce que Claire m'avait décrit : une petite application pour déclarer un dégât des eaux, avec des photos, une estimation du montant des dommages et un calcul de l'indemnité.

L'agent a d'abord proposé un plan en six étapes. Je l'ai accepté sans le lire vraiment. Vingt minutes plus tard, j'avais un formulaire qui fonctionnait, des photos qui s'affichaient, et un écran récapitulatif avec un montant d'indemnité au centime près. Il avait même écrit des tests, et ils passaient.

J'ai ressenti deux choses à la fois. De l'admiration, d'abord. Puis un malaise que j'ai mis un moment à nommer.

J'ai repris le calcul. Dommages estimés : 2 400 euros. Indemnité : 2 250 euros. Je n'avais jamais parlé de franchise.

J'ai demandé à l'agent d'où venaient ces 150 euros. La réponse est arrivée aussitôt :

```text
J'ai supposé une franchise fixe de 150 € par sinistre, car votre
demande ne précisait pas de règle. Ce montant est une hypothèse :
il doit être confirmé par le métier avant toute mise en production.
```

Il n'avait pas menti. Il avait fait exactement ce que fait un prestataire pressé : combler un trou de la spécification par une hypothèse raisonnable, puis l'enfouir dans le code. La seule différence, c'est qu'il l'avouait dès qu'on lui posait la question. Encore fallait-il la poser.

Avant de me coucher, j'ai écrit une phrase dans mon carnet, sous le nom du RSSI :

*Le code ne coûte presque plus rien. La spécification, si.*

## Mardi, 9 heures

La salle s'appelait Escaut. Toutes les salles du quatrième portaient des noms de rivières du Nord, ce qui donnait aux plannings de réunion un air de carte hydrographique.

Ils étaient arrivés avant moi.

Nadia Benali avait ouvert un carnet à spirale sur une page vierge, le stylo posé en travers. Quinze ans à traiter des sinistres, des milliers de dossiers, et la veille encore un poste de responsable d'équipe. Elle m'a serré la main avec une politesse prudente.

— Je vous préviens tout de suite, a-t-elle dit. Je n'ai jamais été Product Owner. Je ne sais même pas très bien ce que c'est.

— Vous savez ce qu'un assuré attend quand sa cuisine est sous l'eau ?

— Ça, oui.

— Alors vous savez l'essentiel. Le reste s'apprend.

Julien Morel, lui, était resté assis, bras croisés. Vingt ans de maison, l'homme qui connaissait chaque recoin du système de gestion des contrats, y compris les parties en COBOL que personne d'autre n'osait toucher.

— Je vais être honnête, a-t-il dit avant même que je m'assoie. Si le plan est de laisser une IA écrire du code pendant quatorze semaines, on va produire de la dette technique à la vitesse de la lumière. Et c'est moi qui la maintiendrai pendant dix ans.

À l'autre bout de la table, Sofiane Haddad souriait. Vingt-six ans, deux ans dans la maison, et déjà l'habitude de Claude Code sur ses projets personnels.

— Avec les bons prompts, on peut faire en un week-end ce qu'Horizon fait en un trimestre.

Julien n'a pas répondu. Il n'en avait pas besoin.

Émilie Roussel n'avait rien dit. Elle avait ouvert sur son ordinateur un tableur gigantesque : les campagnes de tests d'Horizon, des milliers de lignes, presque toutes en rouge.

Je me suis levé.

— Je vais vous dire trois choses, et ensuite je vous écouterai. Un : nous avons quatorze semaines, découpées en sept sprints de deux semaines. Le premier commence aujourd'hui, il servira à préparer le terrain. Deux : nous mesurerons tout. Nous ne croirons ni les brochures, ni nos impressions. Trois : personne dans cette pièce n'est remplacé par un outil. L'outil va changer votre travail. C'est à nous de décider comment.

Julien a décroisé les bras.

— Et qui relit le code que la machine écrit ?

— Vous. Et c'est sans doute la question la plus importante de tout le projet.

Il ne s'attendait pas à cette réponse. Moi non plus, à vrai dire. Elle venait de mon essai de la veille.

Nous avons travaillé deux heures. Nadia a raconté le parcours d'un sinistre, de l'appel affolé de l'assuré jusqu'au virement. Émilie a listé les cas que les tests d'Horizon n'avaient jamais couverts. Julien a dessiné au tableau les flux vers le système central, avec plus de points d'interrogation que de flèches.

À 11 h 52, mon téléphone a vibré. Puis celui de Claire, qui venait de nous rejoindre. Le même message.

> **De :** Bertrand Lefebvre, RSSI **Objet :** Usage d'outils d'IA générative — demande de suspension
>
> Il m'a été signalé qu'un outil d'IA générative de développement doit être déployé dans le cadre d'un projet pilote. Je rappelle qu'aucun outil de ce type n'est autorisé sur le système d'information sans validation préalable de la commission sécurité. Merci de suspendre toute installation. La prochaine commission se réunit dans six semaines.

Claire a pâli. J'ai regardé le tableau blanc, où j'avais écrit en grand, une heure plus tôt : *14 semaines*.

Sofiane s'est raclé la gorge.

— Il est déjà installé sur mon poste.

## Le carnet de Thomas

**Ce qui s'est passé.** Une sponsor a promis au comité de direction un résultat et un gain de productivité sans mesure préalable. L'équipe découvre l'outil, chacun avec sa peur ou son enthousiasme, et la sécurité n'a pas été associée.

**La leçon.** Un engagement pris sur un chiffre de démonstration est une dette. Avant de promettre une productivité, il faut une mesure ; avant d'installer l'outil, il faut un cadre.

**Trois questions à poser à votre équipe**

1. Qu'avons-nous promis, à qui, et sur quelle base ?
2. Quand la spécification se tait, qui décide de ce que fait le logiciel ?
3. Notre RSSI sait-il ce que nous allons installer, et pourquoi ?

**Pour aller plus loin.** Manuel, chapitre M1 (installer Claude Code) et chapitre M4 (paramètres et permissions).
