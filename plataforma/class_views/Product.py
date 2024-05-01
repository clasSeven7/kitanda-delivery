from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from ..models import Product


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