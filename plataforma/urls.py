from django.urls import path
from . import views
from .views import *


URLSPRODUCTS = [
   path('create-product/', ProductCreateView.as_view(), name='product_create'),
   path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
   path('<int:pk>/update-product/', ProductUpdateView.as_view(), name='product_update'),
   path('<int:pk>/delete-product/', ProductDeleteView.as_view(), name='product_delete')
]

urlpatterns = [
   path('', views.home_page, name='home_page')
] + URLSPRODUCTS