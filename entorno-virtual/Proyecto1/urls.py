from django.contrib import admin
from django.urls import path, include
from App1 import views  # Asegúrate de importar las vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('App1/', include('App1.urls')),  # Esto está bien si App1 tiene su urls.py
    path('', views.inicio, name='inicio'),  # Asegúrate de que existe esta vista
]
