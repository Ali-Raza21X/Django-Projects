from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add_exp,name='add_exp'),
    path('delete/<int:id>/', views.delete_exp, name='delete_exp'),
    path('update/<int:id>/', views.update_exp, name='update_exp'),

]
