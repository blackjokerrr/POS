from django.contrib import admin
from django.urls import path, include

from Sale import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.Login, name = 'login'),
    path('logout/', views.Logout, name='logout'),
    path('', include('Sale.urls')),
    path('Management/', include('Management.urls')),
    path('Report/', include('Report.urls'))
]
