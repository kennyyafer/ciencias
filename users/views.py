from django.shortcuts import render, redirect
from django.contrib.auth import login   
from django.contrib.auth.forms import UserCreationForm 


def registro(request):       
    """Registrar un nuevo usuario.En la función registro (), 
    verificamos si estamos respondiendo o no a una solicitud POST"""       
    if request.method != 'POST':          
         # Mostrar formulario de registro en blanco.
        form = UserCreationForm() #. Si no respondemos a una solicitud POST, 
        #                           creamos una instancia de UserCreationForm sin datos iniciales
    else:           
    # Formulario de proceso completado.
        form = UserCreationForm(data=request.POST)
    
        if form.is_valid():
            new_user = form.save()   
            # Inicia la sesi[on del usuario y luego redirija a la p[agina de inicio]].
            login(request, new_user) # para iniciar la sesión del usuario si su información de registro es correcta.
            return redirect('ciencias_app:index')
        
    # Mostrar un formulario en blanco o invalido.
    context = {'form': form}
    return render(request, 'registration/registro.html', context)
