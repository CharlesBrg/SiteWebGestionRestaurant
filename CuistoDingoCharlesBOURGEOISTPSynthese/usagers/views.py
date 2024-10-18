from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, FormView
from django.contrib import messages
from usagers.forms import EnregistrementForm
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Enregistrement(FormView):
    form_class = EnregistrementForm
    template_name = 'usagers/enregistrement.html'
    success_url = '/'  # URL de redirection après un enregistrement réussi

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'Bonjour {username}, vous êtes enregistré !')
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
