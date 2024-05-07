from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ['user', 'date', 'title', 'description', 'image']
    template_name = 'plataforma/blog/blog_create.html'
    success_url = '/'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'plataforma/blog/blog_detail.html'


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['user', 'date', 'title', 'description', 'image']
    template_name = 'plataforma/blog/blog_update.html'
    success_url = '/'


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'plataforma/blog/blog_delete.html'
    success_url = '/'


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'plataforma/blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 2
