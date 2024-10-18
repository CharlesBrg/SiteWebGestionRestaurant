from django import forms

from .models import Restaurant

class AjoutRestoForms(forms.ModelForm):
    class Meta:
        model = Restaurant
        exclude = ['noRestaurant'] 
        labels = {
            'nomRestaurant': "Nom du restaurant",
            'villeRestaurant': 'Ville du restaurant',
            'typeRestaurant': 'Type du restaurant',
            'image': 'Image du restaurant'
        }
        
class ModifierRestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        exclude = ['noRestaurant'] 
        labels = {
            'nomRestaurant': "Nom du restaurant",
            'villeRestaurant': 'Ville du restaurant',
            'typeRestaurant': 'Type du restaurant',
            'image': 'Image du restaurant'
        }