# Le Sprint d'après

*Agilité, agents et spécifications : un roman d'entreprise et un manuel pour travailler avec Claude Code et BMAD.*

Une mutuelle lilloise, une équipe réduite et quatorze semaines pour livrer un portail de déclaration de sinistres avec un agent de code. Le livre se lit en deux temps :

- **Partie I, le roman** : 27 chapitres et un épilogue.
- **Partie II, le manuel de référence** : 14 chapitres et 6 annexes pratiques.

Les manuscrits Markdown sont dans [le-sprint-d-apres/](le-sprint-d-apres/README.md), qui en donne aussi le sommaire.

## Générer le PDF

```bash
./outils/build.sh          # produit build/le-sprint-d-apres.pdf
./outils/build.sh --html   # écrit aussi build/livre.html (débogage de la mise en page)
```

Le script compose un livre au format A5 : couverture, page de titre, table des matières cliquable, parties, chapitres ouvrant sur une page de droite, en-têtes courants, pagination et typographie française.

Prérequis :

- Python 3 ;
- pango (`brew install pango` sur macOS) ;
- au premier lancement, le script crée un environnement `.venv` et y installe WeasyPrint et Markdown.

Les polices utilisées sont Iowan Old Style, Palatino ou Georgia (macOS). Le rendu varie si elles sont absentes.

## Version web (GitHub Pages)

Le livre est publié en ligne à chaque tag `v*` par le workflow [pages.yml](.github/workflows/pages.yml) : une page par chapitre, navigation précédent/suivant, thème clair/sombre, lecture sur mobile.

- La racine du site affiche **la version au numéro le plus élevé** (ordre sémantique : `v1.10.0` > `v1.9.0`). Taguer un correctif sur une version plus ancienne l'ajoute au sélecteur sans changer la racine.
- Chaque version reste accessible à l'adresse `/<tag>/` (par exemple `/v0.1.0/`), et un **sélecteur de version** en haut de chaque page permet d'en changer.
- Le site est servi depuis la branche `gh-pages`. À activer une fois : *Settings → Pages → Source : Deploy from a branch → `gh-pages` / `(root)`*, après le premier tag.

Seuls les tags de la forme `vX.Y.Z` sont publiés (pas de préfixe `-rc`).

Pour générer le site en local (version « dev », sans sélecteur actif) :

```bash
.venv/bin/python outils/build_site.py   # écrit site/
```

## Publier une version

Pousser un tag `v*` déclenche deux workflows : [release.yml](.github/workflows/release.yml) génère le PDF et l'attache à une release, [pages.yml](.github/workflows/pages.yml) publie la version web :

```bash
git tag v0.1.0
git push origin v0.1.0
```

Le workflow tourne sur un runner macOS, avec les mêmes polices qu'en local.

## Licence

Ce livre est publié sous licence [Creative Commons Attribution – Pas d'utilisation commerciale – Partage dans les mêmes conditions 4.0 International (CC BY-NC-SA 4.0)](LICENSE).

Vous pouvez le lire, le copier, le redistribuer et l'adapter, à condition de :

- **citer l'auteur** et indiquer les modifications apportées ;
- **ne pas en faire un usage commercial** ;
- **partager vos adaptations sous la même licence**.

### Et en entreprise ?

La licence ne limite pas la lecture. Un employé peut lire le livre, y compris au travail, appliquer les méthodes et les configurations qu'il décrit, le recommander à ses collègues et en citer de brefs extraits avec attribution : la licence protège le texte, pas les idées.

La zone grise concerne la redistribution. Partager un lien ou acheter un exemplaire pour l'équipe ne pose pas de difficulté. Diffuser le PDF en interne (intranet, messagerie, canal d'équipe) est une copie, et son caractère « commercial » est discuté ; en cas de doute, demandez-nous. Revendre le livre ou l'utiliser comme support d'une formation payante est exclu sans accord préalable.

Pour toute autre utilisation, écrivez à l'auteur pour obtenir une licence séparée.

## Statut

Version de travail. Les schémas interactifs de la version numérique ne sont pas reproduits dans les exports Markdown ni dans le PDF.
