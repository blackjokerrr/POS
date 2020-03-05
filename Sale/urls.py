from django.contrib import admin
from django.urls import path, include

from Sale import views

urlpatterns = [
    path('index/', views.Index, name='index'),
    path('index/<int:key_of>', views.Index, name='cart')
    
]
