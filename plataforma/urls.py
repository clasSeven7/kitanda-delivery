from django.urls import path

from .class_views.Categorie import (CategorieCreateView, CategorieDeleteView,
                                    CategorieDetailView, CategorieUpdateView)
from .class_views.Comment import (CommentCreateView, CommentDeleteView,
                                  CommentDetailView, CommentUpdateView)
from .class_views.Product import (ProductCreateView, ProductDeleteView,
                                  ProductDetailView, ProductUpdateView)
from .class_views.Resource import (ResourceCreateView, ResourceDeleteView,
                                   ResourceDetailView, ResourceUpdateView)

from .class_views.Blog import (BlogCreateView, BlogDeleteView, BlogDetailView,
                               BlogUpdateView)

from .views import home


URLSBLOGS = [
     path('create-blog/', BlogCreateView.as_view(), name='blog_create'),
     path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
     path('<int:pk>/update-blog/', BlogUpdateView.as_view(), name='blog_update'),
     path('<int:pk>/delete-blog/', BlogDeleteView.as_view(), name='blog_delete'),
     ]


URLSPRODUCTS = [
    path('create-product/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/update-product/',
         ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete-product/',
         ProductDeleteView.as_view(), name='product_delete'),
]

URLSRESOURCES = [
    path('create-resource/', ResourceCreateView.as_view(), name='resource_create'),
    path('<int:pk>/', ResourceDetailView.as_view(), name='resource_detail'),
    path('<int:pk>/update-resource/',
         ResourceUpdateView.as_view(), name='resource_update'),
    path('<int:pk>/delete-resource/',
         ResourceDeleteView.as_view(), name='resource_delete'),
]

URLSCOMMENTS = [
    path('create-comment/', CommentCreateView.as_view(), name='comment_create'),
    path('<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    path('<int:pk>/update-comment/',
         CommentUpdateView.as_view(), name='comment_update'),
    path('<int:pk>/delete-comment/',
         CommentDeleteView.as_view(), name='comment_delete'),
]

URLSCATEGORIES = [
    path('create-categorie/', CategorieCreateView.as_view(),
         name='categorie_create'),
    path('<int:pk>/', CategorieDetailView.as_view(), name='categorie_detail'),
    path('<int:pk>/update-categorie/',
         CategorieUpdateView.as_view(), name='categorie_update'),
    path('<int:pk>/delete-categorie/',
         CategorieDeleteView.as_view(), name='categorie_delete'),
]

urlpatterns = [
    path('', home, name='home')
] + URLSPRODUCTS + URLSRESOURCES + URLSCOMMENTS + URLSCATEGORIES + URLSBLOGS
