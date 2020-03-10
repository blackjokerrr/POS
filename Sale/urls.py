from django.contrib import admin
from django.urls import path, include

from Sale import views

urlpatterns = [
    path('index/', views.Index, name='index'),
    path('index/<int:key_of>', views.Index, name='cart'),
    path('index/<int:number_of_page>/delete', views.Delete, name='delete'),
    path('index/save', views.Save, name='save')
]
