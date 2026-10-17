from django.urls import path
from .import views

urlpatterns = [
    path('', views.product_list, name='home'), 
    path('products/', views.product_list, name='product_list'), 
    path('product/add/', views.product_create, name='product_create'), 
    path('products/edit/<int:id>', views.product_update, name='product_update'),
    path('products/delete/<int:id>', views.product_delete, name='product_delete'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
]

