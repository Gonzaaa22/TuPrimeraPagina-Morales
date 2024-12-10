from django.urls import path
from app_coder import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar_datos, name='agregar_datos'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
]
