from django.shortcuts import render
from django.http import HttpResponse
from .models import profesor,curso
# Create your views here.
def index(request):
    """The home page for Ciencias log."""
    return render(request, 'ciencias_app/index.html')

def cursosllevados(request):
    """Mostrar la barra de busqueda."""
   
    return render(request, 'ciencias_app/cursosllevados.html')

def buscar(request):
    """Mensaje."""
    if request.GET['cursos']:
        #mensaje = 'Cursos buscados: %r' %request.GET['cursos']
        cursofinalizado = request.GET['cursos']

        # limitar el numero de caracteres
        if len(cursofinalizado) > 120:

            mensaje = 'Texto de busqueda demasiado largo'

        else:

            context = dict()
            context['cursos'] = curso.objects.filter(Nombre__icontains=cursofinalizado)
            #cursos = curso.objects.filter(Nombre__icontains=cursofinalizado)

            return render(request, 'ciencias_app/resultados_busqueda.html',
            {'cursos':context['cursos'],'consulta':cursofinalizado})

    else:
        mensaje = 'No has introducido nada, vuelve a intentarlo'
   
    return HttpResponse(mensaje)


def contacto(request):
    """ """
    return render(request, 'contacto.html')