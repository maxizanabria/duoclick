from App1 import views
from django.urls import path

app_name = 'App1'

urlpatterns = [
    path('inicio/', views.inicio),
]