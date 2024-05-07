from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from plataforma.forms import ProductForm

from ..models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['title', 'value', 'stars', 'quantity', 'image']
    template_name = 'plataforma/product/product_create.html'
    success_url = '/'

    def get(self, request):
        form_product = ProductForm()
        return render(request, 'plataforma/product/product_create.html', {'form_product': form_product})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'plataforma/product/product_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['title', 'value', 'stars', 'image']
    template_name = 'plataforma/product/product_update.html'
    success_url = '/'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'plataforma/product/product_delete.html'
    success_url = '/'
