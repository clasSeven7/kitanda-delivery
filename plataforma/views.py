from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView 
from .models import *


def home_page(request):
    resources = Resource.objects.all()
    products = Product.objects.all()
    categories = Categorie.objects.all()
    comments = Comment.objects.all()
    return render(request, 'plataforma/home_page.html', {'resources': resources, 'products': products, 'categories': categories, 'comments': comments})


def resources_detail(request, pk):
    resource = Resource.objects.get(pk=pk)
    return render(request, 'plataforma/resources_detail.html', {'resource': resource})


class ProductCreateView(CreateView):
    model = Product
    fields = ['title', 'value', 'stars', 'image']
    template_name = 'plataforma/products/product_create.html'
    success_url =  '/'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'plataforma/products/product_detail.html'

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['title', 'value', 'stars', 'image']
    template_name = 'plataforma/products/product_update.html'
    success_url =  '/'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'plataforma/products/product_delete.html'
    success_url =  '/'


