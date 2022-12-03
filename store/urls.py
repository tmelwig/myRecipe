import store.views
from django.urls import re_path, path
from django.contrib import admin

urlpatterns = [
    re_path(r'^recipe/$', store.views.recipe_index,
            name='recipe index'),
    path('recipe/<int:recipe_id>/', store.views.detail),
    re_path(r'^search/$', store.views.search),
    re_path(r'^search/store/search$', store.views.search),
    re_path(r'^search/entre$', store.views.entree),
    re_path(r'^search/plats$', store.views.plat),
    re_path(r'^search/desserts$', store.views.dessert)
]

# Premier URL : page d'accueil avec toutes les recettes disponibles
# Deuxième URL : affiche la page contenant les détails de chaque recette
# Troisième et quatrième URL: affiche le résultat d'une requête lorsqu'on cherche une recette
# Cinquième, sixième et septième URL : affiche le résultat d'une requête lorsqu'on cherche une entrée, un plat ou un dessert
