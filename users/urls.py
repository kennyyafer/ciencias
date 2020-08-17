"""Defines URL patterns for users"""   

from django.urls import path, include
from . import views


app_name = 'users'   
urlpatterns = [       
    # Incluye por defecto auth urls.
    path('', include('django.contrib.auth.urls')), 
    # Pagina de registro
    path('registro', views.registro,name='registro'), 
]