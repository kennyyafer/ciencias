"""Defines URL patterns for ciencias_app."""
from django.urls import path

from . import views

app_name = 'ciencias_app'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.➊     
    path('cursosllevados/', views.cursosllevados, name='cursosllevados'),
    path('buscar/', views.buscar),
    path('contacto/', views.contacto),
]