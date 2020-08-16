from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import profesor, departamento, curso
from .forms import DepartamentoForm, ProfesorForm

# Create your views here.
def index(request):
    """The home page for Ciencias log."""
    return render(request, 'ciencias_app/index.html')

def Departamentos(request):
    """Muestra los departamentos.."""
    Departamentos = departamento.objects.order_by('Nombre')
    context = {'Departamentos':Departamentos}
    return render(request, 'ciencias_app/Departamentos.html',context)

def Departamento(request, departamento_id):
    """Muestra un solo departamento con todos sus profesores."""
    Departamento = departamento.objects.get(id=departamento_id)
    Profesores = Departamento.profesor_set.order_by('Apellido')
    context = {'Departamento': Departamento, 'Profesores': Profesores}
    return render(request, 'ciencias_app/Departamento.html', context)

def NuevoDepartamento(request):
    """Añadir nuevo nombre de departamento """
    if request.method != 'POST':
        # No se ha enviado datos: crea un formulario en blanco
        form = DepartamentoForm()
    else:
        # Datos POST enviado: procesar datos
        form = DepartamentoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('ciencias_app:Departamentos')

    # Mostrar una forma en blanco o invalida
    context = {'form':form}
    return render(request,'ciencias_app/NuevoDepartamento.html',context)

def NuevoProfesor(request,departamentoid):
    """Añadir nuevo nombre para un departamento particular """
    Departamento = departamento.objects.get(id=departamentoid)
    if request.method != 'POST':
        # No se ha enviado datos: crea un formulario en blanco
        form = ProfesorForm()
    else:
        # Datos POST enviado: procesar datos
        form = ProfesorForm(data=request.POST)
        if form.is_valid():
            nuevoprofesor = form.save(commit=False)
            nuevoprofesor.Departamento = Departamento
            nuevoprofesor.save()
            return redirect('ciencias_app:Departamento',departamentoid)

    # Mostrar una forma en blanco o invalida
    context = {'Departamento':Departamento,'form':form}
    return render(request,'ciencias_app/NuevoProfesor.html',context)

        
