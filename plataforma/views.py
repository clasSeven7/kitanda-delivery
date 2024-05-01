from django.shortcuts import render
from .models import Resource, Product, Categorie, Comment

def home_page(request):
    resources = Resource.objects.all()
    products = Product.objects.all()
    categories = Categorie.objects.all()
    comments = Comment.objects.all()
    return render(request, 'plataforma/home_page.html', {'resources': resources, 'products': products, 'categories': categories, 'comments': comments})



