from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from plataforma.forms import ResourceForm

from ..models import Resource


class ResourceCreateView(CreateView):
    model = Resource
    fields = ['title', 'description', 'image']
    template_name = 'plataforma/resource/resource_create.html'
    success_url = '/'

    def get(self, request):
        form_resource = ResourceForm()
        return render(request, 'plataforma/resource/resource_create.html', {'form_resource': form_resource})


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


class ResourceListView(LoginRequiredMixin, ListView):
    model = Resource
    template_name = 'plataforma/resource/resource_list.html'
    context_object_name = 'resources'
    paginate_by = 2
