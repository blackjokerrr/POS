from django.contrib import admin
from django.urls import path, include

from Sale import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.go_login),
    path('login/', views.Login, name = 'login'),
    path('logout/', views.Logout, name='logout'),
    path('', include('Sale.urls')),
    path('', include('Management.urls')),
    path('', include('Report.urls'))
]
