"""my_recipe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin
import store.views

urlpatterns = [
    # tous les urls liés au dossier store (ex : recipe) devront être appelés dans l'url par 127.0.0.1:8000/store/...
    path('store/', include('store.urls')),
    # url de la page d'accueil 127.0.0.1:8000/
    re_path(r'^$', store.views.index, name='index'),
    path('admin/', admin.site.urls)  # url de l'admin est 127.0.0.1:8000/admin/
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
