# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),               
    path('posts/', views.lista_posts, name='lista_posts'), 
    path('get_convenios/', views.get_convenios, name='get_convenios'),
]
