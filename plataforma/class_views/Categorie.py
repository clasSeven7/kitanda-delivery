from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from ..models import Categorie


class CategorieCreateView(CreateView):
    model = Categorie
    fields = ['title', 'description', 'image']
    template_name = 'plataforma/categorie/categorie_create.html'
    success_url = '/'

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

    