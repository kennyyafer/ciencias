from django.contrib import admin
# Se llama la libreria para importar y exportar
from import_export import resources

from  import_export.admin import ImportExportActionModelAdmin
# Register your models here.
#from .models import departamento,profesor, operador, tipodecurso, curso
#from .models import carrera,estado, curso_profesor, operador_profesor

# Se llaman todos los modelos existentes
from .models import *

# Se elabora una clase por cada modelo para colocar el import/export
class DepartamentoResource(resources.ModelResource):
    class Meta:
        model = departamento

class DepartamentoAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    # Aqui se hace para obtener la barra de busqueda para cada modelo
    search_fields = ['Nombre']
    # los atributos que queremos mostrar en el sitio y no olvidar la coma
    list_display = ('id','Nombre',)
    # Aqui se coloca el codigo de la clase DepartamentoResource para el import/export
    resource_class = DepartamentoResource


class ProfesorResource(resources.ModelResource):
    class Meta:
        model = profesor

class ProfesorAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['Apellido','Nombre']
    list_display = ('Apellido','Nombre','CorreoInstitucional',
    'CorreoPersonal','Departamentoid')
    resource_class = ProfesorResource


class OperadorResource(resources.ModelResource):
    class Meta:
        model = operador

class OperadorAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['Nombre']
    list_display = ('Nombre',)
    resource_class = OperadorResource


class TipodecursoResource(resources.ModelResource):
    class Meta:
        model = tipodecurso

class TipodecursoAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['Nombre']
    list_display = ('id','Nombre',)
    resource_class = TipodecursoResource


class CursoResource(resources.ModelResource):
    class Meta:
        model = curso

class CursoAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['Nombre','Codigo']
    list_display = ('Nombre','Codigo','Tipodecursoid',)
    resource_class = CursoResource


class CarreraResource(resources.ModelResource):
    class Meta:
        model = carrera

class CarreraAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['Nombre']
    list_display = ('Nombre','Departamentoid',)
    resource_class = CarreraResource


class EstadoResource(resources.ModelResource):
    class Meta:
        model = estado

class EstadoAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['Nombre']
    list_display = ('id','Nombre',)
    resource_class = EstadoResource


class Curso_profesorResource(resources.ModelResource):
    class Meta:
        model = curso_profesor

class Curso_profesorAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    #search_fields = ['Profesorid','Cursoid'] -- no se puede por que son foreignkey
    list_display = ('Fechainicio','Fechafinal','Cohorte',
    'Profesorid','Cursoid','Estadoid',)
    resource_class = Curso_profesorResource


class Operador_profesorResource(resources.ModelResource):
    class Meta:
        model = operador_profesor

class Operador_profesorAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['Telefono']
    list_display = ('Profesorid','Telefono',)
    resource_class = Operador_profesorResource

# Aqui acepta dos argumento uno que es obligatorio la cual es el nombre del modelo
# y el otro de la clases anteriores
admin.site.register(departamento,DepartamentoAdmin)
admin.site.register(profesor,ProfesorAdmin)
admin.site.register(operador,OperadorAdmin)
admin.site.register(tipodecurso,TipodecursoAdmin)
admin.site.register(curso,CursoAdmin)
admin.site.register(carrera,CarreraAdmin)
admin.site.register(estado,EstadoAdmin)
admin.site.register(curso_profesor,Curso_profesorAdmin)
admin.site.register(operador_profesor,Operador_profesorAdmin)

