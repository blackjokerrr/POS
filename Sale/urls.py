from django.contrib import admin
from django.urls import path, include

from Sale import views

urlpatterns = [
    path('index/', views.showProduct, name='index'),
    path('index/#', views.showProduct, name='cart')
    
]
