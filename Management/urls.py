from django.contrib import admin
from django.urls import path, include

from Management import views

urlpatterns = [
    path('manage/', views.manage, name='manage')
]