from django.contrib import admin
from django.urls import path, include

from Report import views



urlpatterns = [
    path('report/', views.report, name='report')
]