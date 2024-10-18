from django.contrib import admin
from .models import Restaurant, TypeResto, Commentaire
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(TypeResto)
admin.site.register(Commentaire)