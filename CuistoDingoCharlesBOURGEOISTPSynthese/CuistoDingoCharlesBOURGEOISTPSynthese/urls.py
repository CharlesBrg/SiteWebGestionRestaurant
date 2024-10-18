"""
URL configuration for CuistoDingoCharlesBOURGEOISTPSynthese project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from CuistoDingoCharlesBOURGEOISTPSynthese.views import accueilView, aproposView, restaurantView, restaurant_ville_View, restaurant_categorie_View, restaurant_nom_View, modifierCommentaire, mes_commentaires, supprimerCommentaire
from usagers.views import Enregistrement
from django.contrib.auth import views as authentification_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueilView),
    path('apropos/', aproposView),
    path('restaurants/', restaurantView, name='restaurants'),
    path('restaurants/ville/<str:ville>/', restaurant_ville_View, name='restaurants_par_ville'),
    path('restaurants/categorie/<str:categorie>/', restaurant_categorie_View, name='restaurants_par_categorie'),
    path('restaurants/detail/<str:code>/', restaurant_nom_View, name='restaurants_detail'),
    path('Gestionnaire/', include ("Gestionnaire.urls")),
    path('/modifCommentaire/<str:noCommentaire>/', modifierCommentaire, name="modifierCommentaire"),
    path('/supprimerCommentaire/<str:noCommentaire>/', supprimerCommentaire, name="supprimerCommentaire"),
    path('enregistrement/', Enregistrement.as_view(), name="enregistrement"),
    path('login/', authentification_views.LoginView.as_view(template_name='usagers/Login.html'), name='login'),
    path('logout/', authentification_views.LogoutView.as_view(template_name='usagers/Logout.html'), name='logout'),
    path('mes-commentaires/', mes_commentaires, name='mes_commentaires'),
]
