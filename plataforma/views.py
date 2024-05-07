from django.shortcuts import render
from django.http import JsonResponse



from blog.models import Blog
from .models import Categorie, Comment, Product, Resource


def home(request):
    resources = Resource.objects.all()
    products = Product.objects.all()
    categories = Categorie.objects.all()
    comments = Comment.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'resources': resources, 'products': products, 'categories': categories, 'comments': comments, 'blogs': blogs})


