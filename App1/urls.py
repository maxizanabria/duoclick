from django.urls import path
from . import views

urlpatterns = [
    path('ingresar/', views.ingresar, name='ingresar'),
    path('', views.index, name='index'),
    path('landing/', views.landing, name='landing'),
    

]