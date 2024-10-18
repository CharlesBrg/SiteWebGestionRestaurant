from django import forms
from Gestionnaire.models import Commentaire

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['commentaire', 'note']

class ModifierCommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        exclude = ['noRestaurant', 'userName'] 
        