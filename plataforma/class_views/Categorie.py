from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from plataforma.forms import CategorieForm

from ..models import Categorie


class CategorieCreateView(CreateView):
    model = Categorie
    fields = ['title', 'description', 'image']
    template_name = 'plataforma/categorie/categorie_create.html'
    success_url = '/'

    def get(self, request):
        form_categorie = CategorieForm()
        return render(request, 'plataforma/categorie/categorie_create.html', {'form_categorie': form_categorie})


class CategorieDetailView(DetailView):
    model = Categorie
    template_name = 'plataforma/categorie/categorie_detail.html'


class CategorieUpdateView(UpdateView):
    model = Categorie
    fields = ['title', 'description', 'image']
    template_name = 'plataforma/categorie/categorie_update.html'
    success_url = '/'


class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = 'plataforma/categorie/categorie_delete.html'
    success_url = '/'
