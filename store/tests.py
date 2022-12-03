from django.urls import resolve
from django.db.models import query
from django.urls import resolve
from django.http import HttpResponse, HttpRequest
from store.views import index, search
from django.test import TestCase
from store.models import Recipe, Ingredient
from store.views import recipe_index, detail


# Ce fichier rassemble toutes les fonctions qui vont servir de test avant d'exécuter manage.py


class WelcomePageTest(TestCase):

    def test_root_url_resolves_to_welcome_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def recipe_page_returns_correct_html(self):
        # ce test vérifie le bon affichage de la page des recettes
        request = HttpRequest()
        response = recipe_index(request)
        html = response.content.decode('utf8')
        pres = ""
        recipes = Recipe.objects.all()[:]
        for recipe in recipes:
            # on les affiche les unes après les autres
            pres += "\u2022 " + recipe.name + '</p>'
            # On remplace les "_" par des espaces
        for i in pres:
            if i != "_":
                pres += i
            else:
                pres += " "
        self.assertTrue(html == pres)

    # def test_detail_page_returns_correct_html(self):
    #     #ce test vérifiait le bon affichage de la liste d'ingrédients, on affiche désormais une image de la recette
    #     request= HttpRequest()
    #     for recipe_id in range(len(Recipe.objects.all())):
    #         response = detail(request,recipe_id)
    #         html = response.content.decode('utf8')
    #         recipe = Recipe.objects.get(pk=recipe_id)
    #         ingredient = recipe.ingredients.all()
    #         res = ""
    #         for ing in ingredient:
    #            res += ing.name + " ; "
    #         message = "la recette choisie est {}, les ingrédients nécessaires sont {} et vous devriez mettre {} minutes à réaliser la préparation".format(recipe.name,res,recipe.time_to_prepare)
    #         self.assertTrue(html == message)

    def test_request_searchs_correct_query(self):
        # ce test vérifie le bon affichage de la recherche
        request = HttpRequest()
        response = search(request)
        html = response.content.decode('utf8')
        query = request.GET.get('query')
        if not query:
            message = "Aucune recette n'est demandée."
        else:
            print(query)
            recipes = Recipe.objects.filter(name__icontains=query)
            if len(recipes) == 0:
                message = "Misère de misère, nous n'avons trouvé aucun résultat !"
            else:
                recipes = ["<li>{}</li>".format(rec.name) for rec in recipes]
                message = """
            Nous avons trouvé les recettes correspondantes à votre recherche ! Les voici :
            <li>{}</li>
        """.format("</li>".join(recipes))
            pres = ""
        for i in message:
            if i != "_":
                pres += i
            else:
                pres += " "
        self.assertTrue(html == pres)
