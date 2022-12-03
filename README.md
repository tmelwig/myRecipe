# myRecipe
# MyRecipe
## MyRecipe, l'indispensable pour étudiant

**Description du projet**

Le projet **MyRecipe** est un projet réalisé lors de la deuxième semaine des **Coding Weeks**, dans le cadre de la première année à CentraleSupélec. Ce projet regroupe cinq étudiants :

- Margot Desortiaux
- Aurélien Droz-Vincent
- Théo Garampon 
- Adrien His
- Thomas Melwig

MyRecipe vise à créer une **application web utile et simple pour la société** rassemblant des recettes de cuisine simples pour étudiants. Ainsi, le **MVP** (**M**inimum **V**iable **P**roduct) doit contenir une page d'accueil permettant aux utilisateurs de visualiser ou de rechercher astucieusement des recettes par différents filtres : ingrédients, catégorie, style... Les utilisateurs sont ensuite redirigés vers une ou plusieurs recettes.

**Prérequis**

Installation du framework Django, taper la commande suivante dans le terminal : `pip install django` ou `pip3 install django`. Installer PIL et requests avec les commandes : `pip install pil` ou `pip install pillow`, `pip install requests` 
Cloner le projet en local via la commande git clone <url>, l'url ce trouve sur le dépôt Gitlab.

**Comment accéder à l'application web ?**

Le code a exécuter est la fonction `main()` dans le fichier `manage.py` qui se situe dans le répertoire `my_recipe`. Tout d'abord mettre en place les migrations via les commandes : `python manage.py makemigrations`, `python manage.py migrate`.
L'exécution du code se fait grâce à l'instruction `python manage.py runserver`(ou `python3 manage.py runserver`) à taper dans le terminal permet d'accéder à l'application web via [cet URL](http://127.0.0.1:8000/). 

Notre dossier contient également un fichier `tests.py` permettant de tester le fichier `manage.py` grâce à l'instruction `python manage.py test`.

**Structure du dossier**

Au niveau de la structure du dossier, s2_my_recipe/my_recipe contient deux principaux sous-dossiers : `s2_my_recipe/my_recipe/my_recipe` et `s2_my_recipe/my_recipe/store`. Celui-ci contient notamment un fichier contenant les URLs, un autre concernant la création des bases de données et un autre contenant les fonctions qui connectent les vues aux données.

Le dossier `s2_my_recipe/my_recipe/store/static` regroupe quant à lui tous les fichiers statiques : les templates, les styles CSS, les scripts JavaScript, les polices de caractère et les images qui sont sur le site web. Les fichiers `.html` dans le dossier `templates/store` regroupent l'ensemble du HTML de l'application, c'est-à-dire qu'ils définissent les textes et les liens hypertextes qui permettent de naviguer vers les autres pages grâce aux boutons sur lesquels va cliquer l'utilisateur.

**Contribution**

Pour toute contribution au projet MyRecipe veuillez nous contacter via l'une des adresses suivantes : 
- thomas.melwig@student-cs.fr
- theo.garampon@student-cs.fr
- aurelien.droz-vincent@student-cs.fr
- margot.desortiaux@student-cs.fr
- adrien.his@student-cs.fr

