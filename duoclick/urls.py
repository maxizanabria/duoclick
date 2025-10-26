
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from App1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ingresar, name='ingresar'),  # Página inicial
    path('home/', views.home, name='home'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)