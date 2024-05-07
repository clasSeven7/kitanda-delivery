from django.shortcuts import render

from blog.models import Blog

from .models import Categorie, Comment, Product, Resource


def home(request):
    resources = Resource.objects.all()
    products = Product.objects.all()
    categories = Categorie.objects.all()
    comments = Comment.objects.all()
    blogs = Blog.objects.all()
    cartItems = Product.objects.all()
    total = sum(item.value * item.quantity for item in cartItems)
    return render(request, 'home.html', {'resources': resources, 'products': products, 'categories': categories, 'comments': comments, 'blogs': blogs, 'cartItems': cartItems, 'total': total})


def newsletter_confirmation(request):
    return render(request, 'plataforma/newsletter/confirmation.html')


def cart(request):
    cartItems = Product.objects.all()
    total = sum(item.value * item.quantity for item in cartItems)
    context = {'cartItems': cartItems, 'total': total}
    return render(request, 'shop-cart.html', context)