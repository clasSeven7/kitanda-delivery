from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



from blog.models import Blog
from .models import Categorie, Comment, Product, Resource, CartItems


def home(request):
    resources = Resource.objects.all()
    products = Product.objects.all()
    categories = Categorie.objects.all()
    comments = Comment.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'resources': resources, 'products': products, 'categories': categories, 'comments': comments, 'blogs': blogs})

@login_required
def shop_cart(request):
    user = request.user
    cart_items = CartItems.objects.filter(user=user)
    total_cart = sum(item.product.value * item.quantity for item in cart_items)
    return render(request, 'shop-cart.html', {'cart_items': cart_items, 'total_cart': total_cart})