from django.urls import path

from .class_views.Auth import (CustomLoginView, CustomLogoutView,
                               CustomRegisterView)
from .class_views.Blog import (BlogCreateView, BlogDeleteView, BlogDetailView,
                               BlogListView, BlogUpdateView)
from .class_views.Categorie import (CategorieCreateView, CategorieDeleteView,
                                    CategorieDetailView, CategorieUpdateView)
from .class_views.Comment import (CommentCreateView, CommentDeleteView,
                                  CommentDetailView, CommentUpdateView)
from .class_views.Product import (ProductCreateView, ProductDeleteView,
                                  ProductDetailView, ProductUpdateView)
from .class_views.Resource import (ResourceCreateView, ResourceDeleteView,
                                   ResourceDetailView, ResourceListView,
                                   ResourceUpdateView)
from .views import home, newsletter_confirmation

URLSPRODUCTS = [
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update/',
         ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/',
         ProductDeleteView.as_view(), name='product_delete'),
]

URLSRESOURCES = [
    path('resource/', ResourceListView.as_view(), name='resource_list'),
    path('resource/create/', ResourceCreateView.as_view(), name='resource_create'),
    path('resource/<int:pk>/', ResourceDetailView.as_view(), name='resource_detail'),
    path('resource/<int:pk>/update/',
         ResourceUpdateView.as_view(), name='resource_update'),
    path('resource/<int:pk>/delete/',
         ResourceDeleteView.as_view(), name='resource_delete'),
]

URLSCOMMENTS = [
    path('comment/create/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    path('comment/<int:pk>/update/',
         CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/',
         CommentDeleteView.as_view(), name='comment_delete'),
]

URLSCATEGORIES = [
    path('categorie/create', CategorieCreateView.as_view(),
         name='categorie_create'),
    path('categorie/<int:pk>/', CategorieDetailView.as_view(),
         name='categorie_detail'),
    path('categorie/<int:pk>/update/',
         CategorieUpdateView.as_view(), name='categorie_update'),
    path('categorie/<int:pk>/delete/',
         CategorieDeleteView.as_view(), name='categorie_delete'),
]

URLSBLOGS = [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/<int:pk>/update/',
         BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/',
         BlogDeleteView.as_view(), name='blog_delete'),
]

URLSAUTH = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]

URLSNEWSLETTER = [
    path('newsletter/confirmation/', newsletter_confirmation,
         name='newsletter_confirmation'),
]

urlpatterns = [
    path('', home, name='home')
] + URLSPRODUCTS + URLSRESOURCES + URLSCOMMENTS + URLSCATEGORIES + URLSBLOGS + URLSAUTH + URLSNEWSLETTER
