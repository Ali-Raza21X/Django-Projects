from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='contact_list'), 
    path('add/', views.create_contact, name='create_contact'), 
    path('edit/<int:id>', views.edit_contact, name='edit_contact'), 
    path('delete/<int:id>/', views.delete_contact, name='delete_contact'), 
    path('detail/<int:id>/', views.detail_contact, name='detail_contact'), 
]