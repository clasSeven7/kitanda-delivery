from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from ..models import Resource


class ResourceCreateView(CreateView):
    model = Resource
    fields = ['title', 'description', 'image']
    template_name = 'plataforma/resource/resource_create.html'
    success_url = '/'


class ResourceDetailView(DetailView):
    model = Resource
    template_name = 'plataforma/resource/resource_detail.html'


class ResourceUpdateView(UpdateView):
    model = Resource
    fields = ['title', 'description', 'image']
    template_name = 'plataforma/resource/resource_update.html'
    success_url = '/'


class ResourceDeleteView(DeleteView):
    model = Resource
    template_name = 'plataforma/resource/resource_delete.html'
    success_url = '/'
