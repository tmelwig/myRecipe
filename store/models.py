
# Create your models here.
from django.db import models


class Ingredient(models.Model):
    # nom de l'ingrédient.
    name = models.CharField(max_length=200, unique=True)
    # Type d'ingrédient(fruits, légumes, viandes, etc...
    category = models.CharField(max_length=200, unique=False)


class Recipe(models.Model):
    name = models.CharField(max_length=200, unique=False)  # nom de la recette.
    # la categorie, à savoir vegan, végétarienne, etc.
    category = models.CharField(max_length=200, unique=False)
    # s'il s'agit d'une entrée, d'un plat ou d'un dessert.
    style = models.CharField(max_length=200, unique=False)
    # temps nécessaire à la préparation du plat.
    time_to_prepare = models.DecimalField(max_digits=4, decimal_places=2)
    # ingrédients necessaires à la recette.
    ingredients = models.ManyToManyField(Ingredient)
    # url de l'image de la recette.
    image = models.CharField(max_length=500, default='', editable=True)
