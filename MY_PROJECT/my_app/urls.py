from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.create_tasks, name='add_tasks'),
    path('delete/<int:id>/', views.delete_tasks, name='delete_tasks'),
    path('update/<int:id>/', views.update_tasks, name='update_tasks'),
]