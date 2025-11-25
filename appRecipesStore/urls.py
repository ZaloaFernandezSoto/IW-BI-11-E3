from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recetas/', views.lista_recetas, name='lista_recetas'),
    path('recetas/<int:pk>/', views.detalle_receta, name='detalle_receta'),
    path('tipos_plato/', views.lista_tipos_plato, name='lista_tipos_plato'),
    path('tipos_plato/<int:pk>/', views.detalle_tipo_plato, name='detalle_tipo_plato'),
    path('ingredientes/', views.lista_ingredientes, name='lista_ingredientes'),
    path('ingredientes/<int:pk>/', views.detalle_ingrediente, name='detalle_ingrediente'),
    path('crear_receta/', views.crear_receta, name='crear_receta'),
    path('recetas/', views.lista_recetas, name='lista_recetas'),
    path("buscar_recetas/", views.buscar_recetas, name="buscar_recetas"),
]
