from django import forms

from .models import profesor, departamento

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = departamento
        fields = ['Nombre']
        labels = {'Nombre':''} # Evita colocar el nombre del atributo
        
class ProfesorForm(forms.ModelForm):
    class Meta:
        model = profesor
        fields = ['Nombre']
        labels = {'Nombre':''} 
        widget = {'Nombre':forms.Textarea(attrs={'cols':80})}


