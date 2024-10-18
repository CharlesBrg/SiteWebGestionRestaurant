from django.shortcuts import render
from Gestionnaire.models import Restaurant, TypeResto, Commentaire
from django.http import HttpResponse, HttpResponseRedirect
from Gestionnaire.forms import AjoutRestoForms, ModifierRestaurantForm

def accueilGestionnaireView(request):
    lstRestos = Restaurant.objects.all
    return render(request,"gestionnaire.html", context={"restaurants":lstRestos})

def ajoutRestaurant(request):
  if request.method == "POST":
    form = AjoutRestoForms(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect("/Gestionnaire")
  else:
    form = AjoutRestoForms()
  return render(request, "ajoutRestaurant.html", {'form':form})

def supprimerRestaurant(request, noRestaurant):
  restaurant = Restaurant.objects.get(noRestaurant=noRestaurant)
  if request.method=="POST":
    restaurant.delete()
    return HttpResponseRedirect('/Gestionnaire')
  return render(request,"supprimerRestaurant.html", {'restaurant':restaurant})

def modifierRestaurant(request,noRestaurant):
  restaurant = Restaurant.objects.get(noRestaurant=noRestaurant)
  if request.method == "POST":
    form = ModifierRestaurantForm(request.POST,instance=restaurant)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect("/Gestionnaire")
  else:
    form = ModifierRestaurantForm(instance=restaurant)
  return render(request, "modifierRestaurant.html", {'form':form})