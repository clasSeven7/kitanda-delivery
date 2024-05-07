from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from blog.models import Blog
from plataforma.forms import BlogForm


class BlogCreateView(CreateView):
    model = Blog
    fields = ['user', 'date', 'title', 'description', 'image']
    template_name = 'plataforma/blog/blog_create.html'
    success_url = '/'

    def get(self, request):
        form_blog = BlogForm()
        return render(request, 'plataforma/blog/blog_create.html', {'form_blog': form_blog})


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

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)
            print(queryset.query)
        orderby = self.request.GET.get('pub_date', 'title')
        return queryset.order_by(orderby)
