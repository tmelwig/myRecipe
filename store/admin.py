from django.contrib import admin

# Ce fichier permet de créer l'interface d'administration

from .models import Ingredient, Recipe

admin.site.register(Ingredient)
admin.site.register(Recipe)
