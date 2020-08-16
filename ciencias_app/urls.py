"""Defines URL patterns for ciencias_app."""
from django.urls import path

from . import views

app_name = 'ciencias_app'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Pagina que muestra departamentos.    
    path('Departamentos/', views.Departamentos, name='Departamentos'),
    # Pagina de profesores para un solo departamento
    path('Departamentos/<int:departamento_id>/', views.Departamento, name='Departamento'),
    # Pagina para añadir un nuevo profesor
    path('NuevoDepartamento/', views.NuevoDepartamento,name='NuevoDepartamento'),
    # Pagina para añadir un nuevo profesor
    path('NuevoProfesor/<int:departamentoid>/', views.NuevoProfesor,name='NuevoProfesor'),
]