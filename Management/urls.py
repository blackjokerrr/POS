from django.contrib import admin
from django.urls import path, include

from Management import views

urlpatterns = [
    path('manage/', views.manage, name='manage'),
    path('manage/change/product', views.Change_product, name='change_product'),
    path('manage/change/type', views.Change_type, name='change_type'),
    path('manage/change/delete', views.Delete, name='delete'),
    path('manage/add/product', views.Add_product, name='add_product'),
    path('manage/add/type', views.Add_type, name='add_type')
]