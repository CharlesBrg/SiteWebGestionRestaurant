from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from Gestionnaire.models import Restaurant, TypeResto, Commentaire
from .forms import CommentaireForm, ModifierCommentaireForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse


def accueilView(request):
    return render(request,"accueil.html")

def aproposView(request):
    return render(request,"apropos.html")

def restaurantView(request):
    lstRestos = Restaurant.objects.all
    return render(request,"restaurants.html", context={"restaurants":lstRestos})

def restaurant_ville_View(request, ville):
    restaurants = Restaurant.objects.filter(villeRestaurant=ville)
    return render(request, 'ville.html', context={'restaurants': restaurants, 'ville': ville})

def restaurant_categorie_View(request, categorie):
    restaurants = Restaurant.objects.filter(typeRestaurant__nomType=categorie)
    return render(request, 'categorie.html', context={'restaurants': restaurants, 'categorie': categorie})


def restaurant_nom_View(request, code):
    restaurant = get_object_or_404(Restaurant, noRestaurant=code)
    commentaires = Commentaire.objects.filter(noRestaurant=restaurant)
    if request.method == 'POST':
        commentaire_form = CommentaireForm(request.POST)
        if commentaire_form.is_valid():
            new_commentaire = commentaire_form.save(commit=False)
            new_commentaire.noRestaurant = restaurant
            new_commentaire.userName = request.user
            new_commentaire.save()
            return render(request, 'mesCommentaires.html', {'commentaires': commentaires})

    else:
        commentaire_form = CommentaireForm()
    return render(request, 'detail.html', {'restaurant': restaurant, 'commentaires': commentaires, 'commentaire_form': commentaire_form})

def modifierCommentaire(request,noCommentaire):
  commentaire = Commentaire.objects.get(noCommentaire=noCommentaire)
  if request.method == "POST":
    form = ModifierCommentaireForm(request.POST,instance=commentaire)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect("/")
  else:
    form = ModifierCommentaireForm(instance=commentaire)
  return render(request, "modifCommentaire.html", {'form':form})

def supprimerCommentaire(request, noCommentaire):
  commentaire = Commentaire.objects.get(noCommentaire=noCommentaire)
  if request.method=="POST":
    commentaire.delete()
    return HttpResponseRedirect('/')
  return render(request,"supprimerCommentaire.html", {'commentaire':commentaire})

def est_admin(user):
    return user.is_superuser

@login_required
def mes_commentaires(request):
    if request.user.is_superuser: 
        commentaires = Commentaire.objects.all()
    else:
        commentaires = Commentaire.objects.filter(userName=request.user)
    return render(request, 'mesCommentaires.html', {'commentaires': commentaires})