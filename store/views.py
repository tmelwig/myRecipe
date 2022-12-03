from django.contrib import admin
from store.models import Recipe, Ingredient
from django.conf import settings
from django.urls import include, path
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from PIL import Image
import requests
# Create your views here.


urlpatterns = []

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


def index(request):
    template = loader.get_template("./store/index.html")
    return HttpResponse(template.render(request=request))


def recipe_index(request):
    # on récupère la liste de toutes les recettes
    recipes = Recipe.objects.all()[:]
    # transforme les recettes en dictionnaire
    context = {
        'recipes': recipes
    }

    return render(request, "./store/index_recipe.html", context)


def detail(request, recipe_id):
    '''Ancienne Version qui affichait la liste des produits'''
    # recipe = Recipe.objects.get(pk=recipe_id)
    # ingredient = recipe.ingredients.all()
    # res = ""
    # for ing in ingredient:
    #     res += '</p>' + " \u2022 " + ing.name + '</p>'
    # message = "La recette choisie est {}, les ingrédients nécessaires sont : {} Vous devriez mettre {} minutes à réaliser la préparation".format(
    #     recipe.name, res, recipe.time_to_prepare)

    # return HttpResponse(message)
    '''Nouvelle version qui affiche une image de la recette'''
    recipe = Recipe.objects.get(pk=recipe_id)
    response = HttpResponse(content_type="image/jpeg")
    img = Image.open(requests.get(recipe.image, stream=True).raw)
    img.save(response, 'JPEG')
    return response


def search(request):
    res=set([])
    query = request.GET.get('query')
    if not query:
        recipe = Recipe.objects.all()
    else:
        liste = query.split()
        res_name = []
        res_ingredient = []
        res_category = []
        res_style = []
# on regarde si la recherche correspond à un nom de recette
        for word in liste:
            recipe = Recipe.objects.filter(name__icontains=word)
            res_name += recipe
# on regarde si la recherche correspond à un ingrédient présent dans une recette
        for word in liste:
            recipe = Recipe.objects.filter(ingredients__name__icontains=word)
            res_ingredient += recipe
# on regarde si la recherche correspond à une catégorie de recette
        for word in liste:
            recipe = Recipe.objects.filter(category__icontains=word)
# on regarde si la recherche est un style de plat
        for word in liste:
            recipe = Recipe.objects.filter(style__icontains=word)
            res_style += recipe
# Désormais, on cherche à combiner chacun des résultats précédents, de sorte à avoir la réponse la plus précise possible
# Par exemple, on doit pouvoir trouver un repas à base de tomate tout en spécifiant que celui-ci doit être végétarien
        res_name = set(res_name)
        res_ingredient = set(res_ingredient)
        res_category = set(res_category)
        res_style = set(res_style)
        total = [res_name, res_ingredient, res_category, res_style]
        total_unempty = []
# on place d'abord dans une liste les ensembles de résultat non vide
        for res_set in total:
            if len(res_set) != 0:
                total_unempty.append(res_set)
# Si au moins un résultat de recherche est non vide, on fait l'intersection de tous les résultats non vides
        if len(total_unempty) != 0:
            res= set(total_unempty[0])
            for resultat in total_unempty:
                res= res & resultat
        
        res = list(res)
# la recherche ne correspond à aucune recette, on propose alors une nouvelle recherche
        if res == []:
            return render(request, "./store/index_search2.html")
# Sinon, on indique les recettes en lien avec la recherche.
        else:
            res = set(res)
            context = {'recipes': res}

        return render(request, "./store/index_search1.html", context)


def entree(request):
    query = 'entrée'
    recipe = Recipe.objects.filter(style__icontains=query)
    context = {
        'recipes': recipe
    }
    return render(request, "./store/index_entrée.html", context)


def plat(request):
    query = 'plat'
    recipe = Recipe.objects.filter(style__icontains=query)
    context = {
        'recipes': recipe
    }
    return render(request, "./store/index_plat.html", context)


def dessert(request):
    query = 'dessert'
    recipe = Recipe.objects.filter(style__icontains=query)
    context = {
        'recipes': recipe
    }
    return render(request, "./store/index_dessert.html", context)
