from django.urls import path
from Gestionnaire.views import accueilGestionnaireView, ajoutRestaurant, supprimerRestaurant, modifierRestaurant
urlpatterns = [
    path('', accueilGestionnaireView, name="accueilGestionnaire"),
    path('/ajoutRestaurant', ajoutRestaurant, name="ajoutRestaurant"),
    path('/supprimerRestaurant/<str:noRestaurant>/', supprimerRestaurant, name="supprimerRestaurant"),
    path('/modifierRestaurant/<str:noRestaurant>/', modifierRestaurant, name="modifierRestaurant"),
]