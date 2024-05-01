from django.shortcuts import render

from .models import Categorie, Comment, Product, Resource


def home(request):
    resources = Resource.objects.all()
    products = Product.objects.all()
    categories = Categorie.objects.all()
    comments = Comment.objects.all()
    return render(request, 'plataforma/home.html', {'resources': resources, 'products': products, 'categories': categories, 'comments': comments})
