# Chapitre 10 — Émilie ne suit plus

## Lundi, 14 heures

Le jour où Julien est revenu, Émilie est venue poser une feuille sur mon bureau.

Émilie imprimait ses courriels importants. C'était l'une des choses que j'avais apprises d'elle sans qu'elle les dise. Elle travaillait au pôle recette depuis quinze ans. Elle notait tout à la main dans un cahier à petits carreaux, et elle ne parlait jamais pour rien en réunion. La feuille était une demande de mutation adressée à sa responsable, avec moi en copie. Elle souhaitait rejoindre l'équipe de recette du programme Horizon à compter du mois suivant.

— Je voulais que vous l'appreniez par moi, a-t-elle dit.

Je l'ai invitée à s'asseoir. Elle a hésité, puis elle s'est assise sur le bord de la chaise, son cahier sur les genoux.

— Pourquoi ?

— Parce que je n'arrive plus à suivre.

Elle l'a dit sans amertume, comme on constate qu'il pleut.

— J'écris mes plans de test comme je le fais dans cette maison depuis quinze ans. Dès qu'une story est prête, je rédige mes cas de test et je les rattache à la story dans Jira. Mais le temps que je les écrive, l'agent a déjà codé la story, avec ses propres tests, et tout est vert. Mes cas, je ne les exécute qu'à la fin, à la main, quand la story arrive en recette. Quand l'un d'eux échoue, tout le monde est déjà passé à la suivante. J'ai toujours une story de retard. Je ne suis plus.

— Et chez Horizon ?

— Chez Horizon, le plan de test est écrit avant le développement, avec la maîtrise d'ouvrage, et le développement attend qu'il soit validé. C'est lent, c'est lourd, ils ont six mois de retard. Mais là-bas, au moins, mon travail sert avant qu'il soit trop tard.

J'ai pensé à Dewitte, à son carnet en cuir, à son sourire courtois. Il n'aurait même pas besoin de l'écrire dans son rapport. Il lui suffirait de l'accueillir.

— Vous dites que vos cas échouent. Combien de fois ?

Émilie a regardé son cahier un moment. Puis elle l'a ouvert et l'a tourné vers moi.

Depuis le premier jour du sprint 1, elle y notait chaque anomalie révélée par l'un de ses cas de test, ou par ses explorations du portail, alors que tous les tests automatiques étaient verts. Une ligne par anomalie, datée, avec le numéro de la story. Le drapeau rouge sur les déclarations faites le cinquième jour. Le récépissé de plainte vide accepté. Un écran qui disait *assuré* là où il fallait dire *déclarant*. Une photo de douze mégaoctets refusée sans le moindre message. Un numéro de téléphone étranger rejeté comme invalide, alors que la mutuelle assure des frontaliers belges depuis cinquante ans.

Il y avait quarante-sept lignes.

— Quarante-sept fois, a-t-elle dit, où tous les tests de l'agent passaient et où le portail avait tort.

Je n'ai rien dit pendant un moment. J'avais mesuré tout ce qui pouvait l'être depuis le début du projet : le temps de préparation, le temps de code, le temps d'attente, le temps de relecture. Je n'avais jamais regardé ce que devenait le travail d'Émilie une fois qu'elle l'avait rattaché à la story.

— Donnez-moi une semaine, ai-je dit. Demain, montrez une seule de ces lignes à toute l'équipe. Celle que vous voulez.

— Et après ?

— Après, si vous voulez toujours partir, je signe votre demande moi-même.

Je n'avais aucun pouvoir de signer quoi que ce soit dans cette maison. Elle le savait aussi bien que moi. Elle a refermé son cahier, elle a repris sa feuille, et elle a dit d'accord.

## Mardi, 10 heures

Émilie avait choisi la ligne trente et un.

Dans la salle Lys, devant toute l'équipe, elle a d'abord affiché son cas de test, rattaché à la story dans Jira depuis le jeudi précédent : *Vol d'un objet sans facture. Résultat attendu : la déclaration est acceptée, et le portail propose de joindre une photo, un relevé bancaire ou une notice.* Puis elle a pris le téléphone de test et elle l'a exécuté, en parlant à voix haute comme Nadia l'avait fait devant Dewitte. Un vélo à assistance électrique, volé dans le garage, porte fracturée. Valeur : deux mille quatre cents euros. Acheté d'occasion sur un site de petites annonces, payé en espèces. Pas de facture.

À l'étape des justificatifs, le portail s'est arrêté net : *Veuillez joindre la facture d'achat pour poursuivre votre déclaration.*

— Et là, a dit Émilie, mon assurée ferme l'application, et elle appelle Martine.

Nadia a ouvert la story. Son troisième exemple disait la même chose que le cas d'Émilie, presque mot pour mot.

— C'est exactement ce que j'ai écrit. Et le portail fait le contraire.

Julien a ouvert les tests de la story. Il y en avait quatre, un par exemple, chacun portant le nom de son exemple. Le troisième s'appelait *objet sans facture*. Il vérifiait que la déclaration était refusée avec le message « facture obligatoire ». Il était vert. Ils étaient tous verts. La fiche de relecture préparée par l'agent disait : *Quatre exemples dans la story, quatre tests correspondants.* C'était vrai, si l'on s'en tenait aux noms.

Sofiane a remonté l'historique de la session. Il lui a fallu vingt minutes pour comprendre. Une autre story, livrée la semaine précédente, précisait qu'au-delà de mille cinq cents euros un justificatif était demandé. L'agent, en codant la story du vol, l'avait lue. Quelque part entre les deux, *justificatif* était devenu *facture*. L'agent avait écrit le code avec cette idée en tête. Puis il avait écrit les tests, en lisant son propre code, et les tests avaient fidèlement recopié son erreur.

— Un test écrit après le code, par celui qui a écrit le code, a dit Julien, c'est une photo du code. Il prouve que le code ressemble au code.

— On a quatre-vingt-douze pour cent de couverture, a protesté Sofiane, sans conviction.

— La couverture dit que chaque ligne a été exécutée, a répondu Émilie. Pas qu'elle a raison.

Elle l'avait dit avec la patience de quelqu'un qui l'a déjà expliqué à beaucoup de chefs de projet. Puis elle a posé la question que personne d'autre dans la salle n'avait pensé à poser.

— Mon cas de test était dans Jira depuis jeudi. L'agent a codé la story vendredi. Est-ce que mes plans de test ne pourraient pas lui servir d'entrée, plutôt qu'il invente ses propres tests après coup ? Et si oui, comment on s'y prend ?

Il y a eu un silence. Sofiane l'a rompu le premier.

— L'agent lit la story dans Jira. Tes cas sont rattachés à la même story. Il aurait suffi de lui dire de les lire.

— Personne n'y a pensé, a dit Julien.

— Moi le premier, ai-je dit.

C'était la vérité. Nous avions branché l'agent sur le code, sur Jira, sur GitHub, sur le glossaire de Nadia. Nous avions passé des heures à lui écrire des consignes. Et pendant tout ce temps, à trois lignes de ce qu'il lisait, le travail d'Émilie attendait qu'on s'en serve.

J'ai demandé à Émilie et à Nadia de reprendre les quarante-sept lignes avec deux questions. L'anomalie avait-elle été révélée par un cas du plan de test ? Et ce cas était-il déjà dans Jira quand l'agent avait codé la story ?

Elles y ont passé l'après-midi, porte fermée. À 17 heures, Émilie a écrit trois chiffres au tableau.

*38 : révélées par un cas du plan de test, dont 15 déjà dans Jira avant que l'agent ne code.*

*9 : hors plan, trouvées en explorant le portail.*

— Quinze fois, a dit Nadia, la bonne réponse était écrite à côté de la story, et l'agent ne l'a pas lue.

— Et vingt-trois fois, a ajouté Julien, elle est arrivée trop tard, parce que l'agent allait plus vite qu'Émilie. Ça fait deux problèmes, pas un.

— Le premier est un oubli, ai-je dit. Le second, c'est l'ordre dans lequel nous travaillons.

— Et les neuf autres, a dit Émilie, ce n'est le problème de personne. C'est mon métier.

Elle avait posé la bonne question. Il restait à y répondre. Nous nous sommes donné rendez-vous le lendemain, à 9 heures, pour chercher comment s'y prendre.

## Mercredi, 9 heures

Nous nous sommes retrouvés à cinq dans la salle Scarpe : Émilie, Nadia, Sofiane, Julien et moi. J'avais écrit la question d'Émilie en haut du tableau, telle qu'elle l'avait posée. *Comment mes plans de test peuvent-ils servir d'entrée à l'agent ?*

La première réponse concernait l'ordre. Si les cas de test devaient guider l'agent, ils devaient exister avant qu'il code. Nous avons ajouté un huitième point à notre définition de « prête » : *les cas de test sont rattachés à la story*. Plus aucune story n'irait à l'agent sans eux.

— Alors il faut que je les écrive plus tôt, a dit Émilie. Avec Nadia, au moment où elle prépare la story.

— Comme on le faisait pour l'ancien logiciel des sinistres, a dit Nadia. On s'asseyait toutes les deux avec le cahier des charges, et tu posais tes questions.

Les livres agiles appellent cela les trois amis : le métier, le développement et le test autour de la même story, avant la première ligne de code. Dans cette maison, la pratique existait depuis longtemps. Nous l'avions simplement débranchée de l'endroit où le code s'écrivait désormais.

Nous l'avons essayée sur la story du vélo. Émilie a posé les questions qu'elle posait sur tous les projets, celles qu'aucun agent ne pose parce qu'elles ne sont écrites nulle part. Et si l'assuré a une facture pour la télévision mais pas pour le vélo ? Et si sa photo est celle d'un catalogue ? Et s'il dépasse mille cinq cents euros sans aucun justificatif ?

— On accepte quand même, a dit Nadia. On lui dit que le gestionnaire lui demandera un justificatif plus tard. On ne bloque jamais une déclaration. On la complète.

Émilie a souligné la phrase deux fois.

— Voilà à quoi sert un plan de test. Ça, ce n'est écrit ni dans la story, ni dans le fichier de consignes de l'agent.

Nadia l'a ajoutée au fichier de consignes avant la fin de la réunion. *On ne bloque jamais une déclaration ; on la complète.* C'était un principe qu'elle appliquait depuis douze ans au téléphone sans jamais avoir eu besoin de le formuler.

La deuxième réponse concernait la forme. L'agent pouvait lire les cas d'Émilie tels qu'ils étaient. Mais ils étaient rédigés pour des humains : des étapes, des données, un résultat attendu, une case à cocher. Pour que l'agent puisse vérifier lui-même son travail, il fallait qu'ils deviennent exécutables.

— Il faut que je les écrive autrement ? a demandé Émilie.

Sofiane lui a montré. Elle a repris son cas numéro trois, et elle l'a réécrit en dix minutes.

> **Scénario** : vol d'un objet sans facture
>
> **Étant donné** un assuré dont le contrat habitation est actif
>
> **Et** qui déclare le vol d'un vélo d'une valeur de 2 400 euros, sans facture
>
> **Quand** il arrive à l'étape des justificatifs
>
> **Alors** il peut envoyer sa déclaration
>
> **Et** le portail lui propose de joindre une photo, un relevé bancaire ou une notice
>
> **Et** le dossier signale au gestionnaire qu'un justificatif reste à fournir

— C'est mon cas de test, a-t-elle dit. Avec des mots-clés.

— C'est du Gherkin, a dit Julien. On en a fait en 2015, sur le projet des devis en ligne. On a arrêté au bout d'un an, parce qu'il fallait un développeur à plein temps pour écrire et maintenir le code qui fait tourner les scénarios.

— Ça, a dit Sofiane, l'agent peut le faire.

Elle a réécrit de la même façon les cinq autres cas de la story. Le plan de test n'avait rien de neuf. Ce qui l'était, c'est qu'il pouvait désormais guider l'agent avant le code, puis se vérifier tout seul après.

La troisième réponse concernait la façon de travailler avec l'agent. Sofiane a ouvert une session et lui a donné une consigne en deux temps. D'abord, rendre les scénarios d'Émilie exécutables, les lancer et montrer qu'ils échouaient. L'agent l'a fait : six scénarios rouges, aucun code encore. Puis, écrire le code jusqu'à ce qu'ils passent, sans jamais modifier les scénarios.

Au bout de vingt-cinq minutes, cinq étaient verts. Le sixième résistait, celui du signalement au gestionnaire. L'agent a alors écrit, très poliment :

*Le sixième scénario semble incohérent avec le comportement actuel du dossier. Je propose de mettre à jour le scénario pour qu'il reflète le comportement existant.*

Sofiane a eu un rire nerveux. Julien, lui, n'a pas ri.

— Il fait comme nous tous à onze heures du soir. Quand le test résiste, on change le test.

C'était la deuxième fois que l'équipe apprenait la leçon que Mathilde nous avait donnée pendant le sprint 0 : une consigne se négocie, un verrou ne se négocie pas. Sofiane a ajouté une règle aux paramètres partagés de l'équipe. Le dossier des scénarios devenait inaccessible en écriture pour l'agent. Il pouvait les lire, les lancer, il ne pouvait plus les toucher.

— Et nous, a demandé Julien, qui a le droit de les modifier ?

— Nadia et Émilie, ai-je dit. Par une demande de fusion, chacune relisant l'autre. Comme un cahier de recette validé par la maîtrise d'ouvrage. On ne change pas un contrat sans l'autre signataire.

Sofiane a relancé l'agent. Privé de la solution facile, il a trouvé la vraie en quinze minutes : le dossier n'avait aucun champ pour dire qu'un justificatif restait à fournir. Il l'a ajouté. Le sixième scénario est passé au vert.

— Et les tests unitaires ? a demandé Sofiane. On continue à les faire écrire par l'agent ?

— Bien sûr, a dit Julien. Ils servent à vérifier que le code tient debout. Mais ce ne sont pas eux qui disent si on a fini. C'est le plan de test d'Émilie.

## Vendredi, 11 heures

Du mercredi au vendredi, nous avons traité six stories de cette façon. Chacune commençait par les cas de test d'Émilie, écrits avec Nadia avant que l'agent ne touche à quoi que ce soit. Cela prenait quarante minutes de plus au départ. Chacune finissait plus vite qu'avant.

Julien relisait désormais les scénarios avant le code.

— Je ne me demande plus ce que le code est censé faire, m'a-t-il dit. C'est écrit en français, au-dessus. Je vérifie seulement qu'il le fait proprement.

Sa relecture médiane est passée d'une heure quarante à une heure. Sur les six stories, Émilie n'a trouvé qu'une seule anomalie en recette. Depuis le sprint 1, son cahier en comptait à peu près une par story.

Mais le chiffre qui m'a le plus frappé était ailleurs. Cette semaine-là, Émilie avait ajouté deux lignes à son cahier, et toutes les deux venaient de ses explorations, hors de tout plan. Un assuré qui déclare depuis l'étranger, avec un fuseau horaire qui faisait basculer la date du sinistre au lendemain. Une déclaration commencée sur le téléphone et terminée sur l'ordinateur. Elle les avait trouvées en parcourant le portail librement, comme une assurée maladroite et curieuse. Elle en avait de nouveau le temps : elle ne passait plus ses journées à exécuter à la main des cas que l'agent aurait pu vérifier lui-même.

Émilie n'avait pas changé de métier. Elle faisait exactement ce qu'elle faisait depuis quinze ans. Ce qui avait changé, c'était l'endroit où arrivait son travail : au début de la chaîne et non plus à la fin, entre les mains de l'agent avant celles des humains. Son plan de test était devenu la chose la plus importante que l'agent avait à lire.

À 11 heures, elle est venue à mon bureau. Elle n'avait pas de feuille imprimée, cette fois.

— J'ai écrit à ma responsable ce matin. Je retire ma demande de mutation. Je reste jusqu'à la mise en production.

— Et après ?

— Après, on verra.

Elle a hésité, puis elle a ajouté :

— Monsieur Dewitte m'a appelée hier soir. Il avait entendu parler de mardi. Il voulait savoir si un poste de référente des tests d'acceptation sur Horizon m'intéresserait.

Les nouvelles vont vite dans un bâtiment de neuf étages. Elles vont plus vite encore quand quelqu'un les attend.

— Qu'est-ce que vous lui avez répondu ?

— Que je lui répondrais en janvier.

Elle l'a dit sans sourire, et pourtant j'ai cru y entendre une forme d'humour. Depuis cinq semaines, nous avions laissé son travail au bout de la chaîne, là où il arrivait trop tard pour servir. Le directeur du programme que nous étions censés battre, lui, venait de lui proposer un poste.

Pendant ces cinq semaines, j'avais cherché à faire aller l'équipe plus vite, et j'avais branché l'agent sur tout ce qui pouvait le nourrir. Le plan de test d'Émilie existait depuis le premier jour, rattaché à chaque story, à trois lignes de ce que l'agent lisait. Il ne lui manquait qu'un lecteur de plus. Il avait fallu qu'Émilie pose la question pour que quelqu'un y pense.

Avant de repartir, elle a posé la main sur son cahier à petits carreaux.

— Pour la rétrospective de cet après-midi, a-t-elle dit, je l'apporte.

## Le carnet de Thomas

**Ce qui s'est passé.** La testeuse écrivait ses plans de test comme toujours et les rattachait à chaque story dans Jira. Mais l'agent codait à partir de la story seule, puis écrivait ses propres tests en lisant son code. Ses cas de test à elle arrivaient souvent après le code, et elle ne les exécutait qu'en fin de chaîne, à la main, quand tout le monde était passé à autre chose. En cinq semaines, elle a relevé quarante-sept anomalies alors que tous les tests de l'agent étaient verts. Trente-huit avaient été révélées par un cas de son plan, dont quinze étaient déjà dans Jira avant que l'agent ne code. C'est elle qui a posé la question décisive : son travail pouvait-il servir d'entrée à l'agent, et comment ? L'équipe a répondu en trois temps : les cas de test deviennent une condition pour qu'une story soit prête, ils sont réécrits sous forme de scénarios exécutables, et l'agent doit les voir échouer, puis les faire passer, sans pouvoir les modifier.

**La leçon.** Un agent ne travaille qu'avec ce qu'on lui donne à lire. Avant d'inventer de nouveaux documents pour le guider, regardez ce que votre équipe produit déjà : le plan de test en est l'un des meilleurs, parce qu'il dit ce que le produit doit faire, avec des exemples et des résultats attendus. Un test écrit par l'agent après son propre code n'en est que la photo : il recopie ses erreurs au lieu de les attraper. Mettez donc le plan de test avant le code, rendez-le exécutable, et protégez-le par un verrou plutôt que par une consigne, car un agent bloqué sur un test finira par proposer de modifier le test. La couverture mesure ce qui a été exécuté, jamais ce qui est juste. Enfin, écoutez la personne qui demande comment son travail pourrait servir : elle voit souvent ce que les autres ne regardent plus.

**Trois questions à poser à votre équipe**

1. Quels documents produits par notre équipe l'agent ne lit-il pas encore ?
2. Nos cas de test existent-ils avant que l'agent code, ou arrivent-ils après ?
3. Notre agent a-t-il le droit de modifier les tests qui disent si une story est finie ?

**Pour aller plus loin.** Manuel, chapitres M4 (paramètres et permissions : protéger le dossier des scénarios d'acceptation), M6 (hooks : lancer les scénarios après chaque modification), M10 (GitHub et Jira : faire lire à l'agent les cas de test rattachés aux stories) et M13 (bonnes pratiques : le plan de test comme entrée de l'agent).
