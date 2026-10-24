# Chapitre 7 — La démo qui brille

## Vendredi, 8 heures

Julien était arrivé à 7 heures pour relire les deux dernières demandes de fusion du sprint. Quand je suis entré, il avait fini. Il buvait son café en regardant par la fenêtre, et il ne s'est pas retourné.

Sofiane, lui, débordait d'idées.

— Pour la revue, on code une story en direct. Dewitte donne une idée de fonctionnalité, on la passe à l'agent devant lui, et dix minutes plus tard elle tourne. Il ne s'en remettra pas.

— Non, ai-je dit.

Il a eu l'air sincèrement surpris.

— Une revue de sprint sert à montrer ce que le produit sait faire de nouveau, et à décider avec les gens présents de ce qu'on fait ensuite, ai-je expliqué. Ce n'est pas un spectacle. Si on montre l'agent, ils ne retiendront que l'agent. Et la prochaine fois que quelque chose prendra trois jours, ils demanderont pourquoi ça n'a pas pris dix minutes.

— Mais c'est ce qui nous rend différents d'Horizon.

— Ce qui nous rend différents d'Horizon, c'est qu'un assuré peut déclarer un dégât des eaux et qu'une gestionnaire reçoit le dossier. C'est Nadia qui présente. Elle montre ce que l'assuré fait, et Martine montre ce qu'elle reçoit.

Nous avons trouvé un compromis : à la fin, cinq minutes pour montrer comment naît une story, de l'entretien de Nadia jusqu'à la demande de fusion. Pas en direct. Une session réelle de la semaine, rejouée, avec ses questions et ses hésitations.

J'ai ajouté une dernière diapositive à la présentation : le tableau des cinq étapes, avec les temps médians. Claire est passée à 11 heures pour relire le déroulé. Elle s'est arrêtée sur cette page.

— Celle-là, vous la retirez.

— Pourquoi ?

— « Attente avant la revue : un jour et demi. » Devant Dewitte ? Vous lui donnez le bâton pour nous battre.

— Si je ne la montre pas, il trouvera tout seul. Et ce jour-là, il ajoutera que nous l'avions cachée.

Elle a réfléchi. Puis elle a soupiré.

— Vous la montrez. Mais vous parlez vite.

## Vendredi, 14 heures

Laurent Dewitte est arrivé à l'heure exacte, ce qui, dans cette maison, était déjà une déclaration. La cinquantaine élégante, une veste bien coupée, un carnet en cuir et un stylo-plume. Il avait dirigé des programmes de transformation dans deux grandes banques avant de prendre Horizon. Il a serré la main de chacun, en retenant les prénoms du premier coup, et il s'est assis au premier rang.

Claire s'est assise à côté de lui. Mathilde, Sylvie et Martine se sont installées au fond.

Nadia s'est levée. Je l'avais vue, la veille, répéter seule dans la salle Lys. Ce jour-là, elle ne tremblait pas.

Elle a raconté la dame de Roubaix, en trois phrases. Puis elle a pris le téléphone de test et elle a déclaré un dégât des eaux, en parlant à voix haute comme le ferait une assurée. Connexion. Le contrat retrouvé automatiquement. La date. La description. Trois photos. Le numéro de téléphone. La relecture. L'envoi.

— Six minutes, a-t-elle dit en montrant le chronomètre. Nous nous étions fixé dix.

Sur le second écran, Martine a ouvert sa boîte de travail. Le dossier était là, complet, avec ses photos.

— Avant, a dit Martine, un dossier comme celui-là m'arrivait en trois morceaux, sur huit jours. Là, je peux appeler l'assurée dans l'heure.

Il y a eu un silence approbateur. Dewitte a écrit quelque chose dans son carnet.

Puis il a posé ses questions. Il les a posées poliment, presque doucement, et elles étaient toutes justes.

— Qui maintiendra ce code dans cinq ans, quand votre agent aura changé trois fois de version ?

— Nous, a répondu Julien. Chaque ligne a été relue par un humain. Le code n'appartient pas à l'agent. Il appartient à la mutuelle, comme n'importe quel code.

Dewitte a hoché la tête. Il avait remarqué, je crois, les cernes de Julien.

— Combien de vos dix-huit stories touchent le cœur de gestion des sinistres ?

— Aucune, ai-je dit. Nous transmettons le dossier aux gestionnaires, qui continuent avec leurs outils actuels.

— Donc vous avez fait le portail. La partie visible. Horizon refond le cœur : les calculs, les règlements, les recours, quarante ans de règles de gestion. Ce n'est pas tout à fait le même exercice.

C'était vrai, et il le savait. Je l'ai reconnu sans détour.

Sa dernière question a porté sur ce que nous n'avions pas fait. La tenue en charge le jour d'une tempête. L'accessibilité pour les assurés malvoyants. Les tests de résilience exigés par DORA.

— Rien de cela n'est fait, ai-je dit. C'est dans le backlog, et prévu avant la mise en production.

Il a noté encore.

Sofiane a ensuite rejoué sa session de la semaine. L'entretien de Nadia avec l'agent, les questions qu'il lui posait, la story qui naissait de leurs échanges, puis le code et les tests qui arrivaient en trente-cinq minutes, et la demande de fusion ouverte sur GitHub. La salle s'est tue pour de bon. Même Sylvie avait cessé de prendre des notes. Dewitte regardait l'écran sans rien écrire. C'était la première fois depuis le début de la réunion.

## Vendredi, 15 h 10

J'ai affiché la dernière diapositive. Les cinq étapes, leurs temps médians. J'ai parlé lentement, malgré la consigne de Claire.

— Voici ce que nous savons après un sprint. Le développement est devenu très rapide : trente-cinq minutes par story, là où il fallait deux ou trois jours. Le reste n'a pas changé. Comprendre le besoin prend toujours une heure. Relire prend toujours près de deux heures. Tester, plus d'une heure. Et aujourd'hui, nos stories attendent en moyenne un jour et demi avant d'être relues.

— Relues par qui ? a demandé Dewitte.

— Par Julien.

— Seul ?

— Seul. C'est le seul qui connaisse assez le système des contrats pour savoir si ce que l'agent écrit est juste.

Dewitte a posé son stylo.

— Donc votre productivité, si je comprends bien, ne dépend pas de l'intelligence artificielle. Elle dépend d'un seul homme.

Personne n'a répondu. Julien regardait la table. La phrase était cruelle et exacte, et chacun dans la salle le savait.

C'est à ce moment que Claire a pris la parole.

Je crois qu'elle a eu peur. Je crois qu'elle a vu, en une seconde, le rapport de Dewitte au comité : un pilote prometteur, fragile, dépendant d'une personne, qu'il serait plus prudent d'intégrer dans le cadre éprouvé d'Horizon. Elle a vu son projet lui échapper. Alors elle a fait ce que font les sponsors quand ils ont peur. Elle a promis.

— Ce que vous venez de voir, Laurent, c'est un premier sprint. L'équipe apprend, et le rythme va encore augmenter. À cette cadence, nous livrerons le dégât des eaux et le vol avant la campagne de janvier. Et je suis convaincue que cette méthode permettra de reprendre la déclaration de tous les types de sinistres d'ici l'été.

J'ai senti l'équipe se figer autour de moi. Le vol n'était qu'une promesse conditionnelle, écrite avec un point d'interrogation. Tous les sinistres d'ici l'été n'avaient jamais été évoqués, par personne, nulle part.

Dewitte a souri. Un sourire courtois, presque bienveillant.

— C'est très ambitieux. Je le mentionnerai dans mon rapport au comité, bien entendu.

Il a rangé son stylo-plume, remercié chacun par son prénom, et il est parti. Sur le seuil, il s'est retourné vers Julien.

— Prenez soin de vous, a-t-il dit. Vous êtes précieux.

Je n'ai jamais su s'il le pensait, ou s'il venait de désigner la cible.

## Vendredi, 16 heures

J'ai rattrapé Claire dans le couloir, devant les ascenseurs.

— Vous venez de promettre deux choses que l'équipe n'a jamais estimées.

Elle a appuyé sur le bouton d'appel, deux fois, comme si cela pouvait faire venir la cabine plus vite.

— Si je n'avais rien promis, il repartait avec votre pilote sous le bras. Lundi, son rapport aurait dit : « initiative intéressante, à intégrer dans Horizon ». Vous ne connaissez pas le comité, Thomas. Moi, si.

— Et maintenant, son rapport dira : « engagement de livrer le vol avant janvier et tous les sinistres avant l'été ». Le jour où nous ne tiendrons pas, ce n'est pas Horizon qui sera en retard. C'est vous.

Les portes se sont ouvertes. Elle n'est pas entrée.

— Vous avez peut-être raison, a-t-elle dit plus bas. Mais c'est fait. Aidez-moi à le tenir.

Je n'avais rien à répondre à cela. Elle est entrée dans la cabine.

La rétrospective a eu lieu juste après, dans la salle Escaut. Elle devait servir à examiner notre façon de travailler et à décider d'une ou deux améliorations pour le sprint suivant. Elle a surtout servi à célébrer.

J'avais tracé trois colonnes au tableau : *ce qui a marché*, *ce qui a coincé*, *ce qu'on change*. La première s'est couverte de post-it en cinq minutes. La démonstration de Nadia. Le squelette. La story à exemples. Les quarante et une secondes. Les six minutes.

La deuxième colonne est restée presque vide. Émilie y a collé un seul post-it : *Des tests qui vérifient le code au lieu du besoin.* Sofiane l'a lu à voix haute.

— Ils passent tous, pourtant.

— Oui, a dit Émilie. Justement.

Personne n'a relancé. L'euphorie a un poids qui écrase les signaux faibles.

J'ai demandé à Julien s'il avait quelque chose à ajouter.

— Rien à signaler.

La troisième colonne a été emportée par la promesse de Claire. Puisqu'il fallait livrer le vol en plus du dégât des eaux, il fallait accélérer. Sofiane avait la solution.

— Je fais tourner quatre agents en parallèle, chacun sur une copie isolée du dépôt, chacun sur sa story. J'ai testé hier soir, ça marche. Et Nadia peut préparer cinq stories par jour avec l'agent.

Nadia a acquiescé, les yeux un peu trop brillants. J'ai posé la seule question qui comptait.

— Et la relecture ?

— Je peux en relire une partie, a proposé Sofiane.

— Non, a dit Julien.

Il n'a rien ajouté. L'équipe a voté pour un sprint 2 à vingt-huit stories.

J'aurais pu imposer un chiffre plus bas. Je ne l'ai pas fait. Une équipe qui vient de réussir n'écoute pas les mises en garde, elle a besoin de les vivre. Je me suis promis d'être là quand elle les vivrait. C'est une règle que j'applique depuis vingt ans. Ce jour-là, je n'en étais plus tout à fait sûr.

À 19 heures, en quittant le bâtiment, j'ai traversé le parking du personnel. La voiture de Julien était là, moteur éteint. Il était assis au volant, les deux mains posées dessus, et il regardait droit devant lui le mur de béton.

J'ai hésité à aller frapper à la vitre. Je ne l'ai pas fait. Je l'ai regretté pendant trois semaines.

## Le carnet de Thomas

**Ce qui s'est passé.** La revue de sprint a montré le produit plutôt que l'outil, et exposé honnêtement le goulot de la relecture. Le directeur d'Horizon en a tiré la conclusion juste : la productivité dépendait d'un seul homme. Pour garder le pilote, la sponsor a promis en public deux engagements que l'équipe n'avait jamais estimés. La rétrospective, portée par l'euphorie, a ignoré les signaux faibles et doublé l'ambition du sprint suivant.

**La leçon.** Une revue de sprint sert à inspecter le produit et à décider de la suite avec les parties prenantes, pas à éblouir. Montrer ses limites protège l'équipe ; les cacher la condamne. Mais aucune transparence ne protège d'un sponsor qui a peur : il faut aussi préparer le sponsor, avant la réunion, à ce qu'il ne doit pas promettre.

**Trois questions à poser à votre équipe**

1. Notre revue montre-t-elle ce que le produit fait, ou ce que l'outil sait faire ?
2. Qui, dans la salle, peut transformer un chiffre en engagement, et l'avons-nous préparé ?
3. Quels signaux faibles notre dernière rétrospective a-t-elle laissés passer ?

**Pour aller plus loin.** Manuel, chapitre M13 (bonnes pratiques : présenter le travail d'une équipe augmentée).
