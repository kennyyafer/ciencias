from django.db import models
from datetime import datetime

#Create your models here.

class departamento(models.Model):
    """Datos generales de departamento"""
    Nombre = models.CharField("Nombre del departamento",max_length=45,blank=False,null=False,unique=True)
    Fechacreacion = models.DateField('Fecha de creacion',auto_now_add=True,null=True, blank=True)



    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        
    def __str__(self):
        """Retorna el nombre del departamento."""
        return self.Nombre

class profesor(models.Model):
    """Datos generales de los profesores"""
    Nombre = models.CharField(max_length=45,blank=False,null=False)
    Apellido = models.CharField(max_length=45,blank=False,null=False)
    CorreoInstitucional = models.EmailField('Correo Institucional',null=True,blank=True)
    CorreoPersonal = models.EmailField('Correo Personal',null=True,blank=True)
    Departamentoid = models.ForeignKey(departamento, on_delete = models.CASCADE,verbose_name='Departamento')
    Fechacreacion = models.DateField('Fecha de creacion',auto_now_add=True,null=True, blank=True)

    
    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'   
        
    def __str__(self):
        """Retorna los campos de la tabla"""
        return "{0},{1}".format(self.Apellido,self.Nombre)

class operador(models.Model):
    """Datos generales de la operadora"""
    Nombre = models.CharField("Nombre de la operadora",max_length=45,blank=False,null=False,unique=True)
    Fechacreacion = models.DateField('Fecha de creacion',auto_now_add=True,null=True, blank=True)

    
    class Meta:
        verbose_name = 'Operador'
        verbose_name_plural = 'Operadores'
        
    def __str__(self):
        """Retorna el nombre del operador."""
        return self.Nombre

class tipodecurso(models.Model):
    """Datos generales de tipo de curso"""
    Nombre = models.CharField("Tipo de curso",max_length=120,blank=False,null=False,unique=True)
    Fechacreacion = models.DateField('Fecha de creacion',auto_now_add=True,null=True, blank=True)


    class Meta:
        verbose_name = 'Tipo de curso'
        verbose_name_plural = 'Tipos de cursos'
        
    def __str__(self):
        """Retorna el tipo de curso."""
        return self.Nombre

class curso(models.Model):
    """Datos generales del curso"""
    Codigo = models.CharField('Codigo', max_length=120,null=True, blank=True)
    Nombre = models.CharField("Nombre del curso",max_length=120,blank=False,null=False,unique=True)
    Tipodecursoid = models.ForeignKey(tipodecurso, on_delete = models.CASCADE,verbose_name='Tipo')
    Fechacreacion = models.DateField('Fecha de creacion',auto_now_add=True,null=True, blank=True)


    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        
    def __str__(self):
        """Retorna el codigo y nombre del curso."""
        return "{0},{1}".format(self.Codigo,self.Nombre)

class carrera(models.Model):
    """Datos generales de carrera"""
    Nombre = models.CharField("carreras",max_length=120,blank=False,null=False,unique=True)
    Departamentoid = models.ForeignKey(departamento, on_delete = models.CASCADE,verbose_name='Departamento')
    Fechacreacion = models.DateField('Fecha de creacion',auto_now_add=True,null=True, blank=True)


    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'
        
    def __str__(self):
        """Retorna la carrera."""
        return self.Nombre

class estado(models.Model):
    """Datos generales de estado del curso"""
    Nombre = models.CharField("Estado de finalizaciòn",max_length=120,blank=False,null=False,unique=True)
    Fechacreacion = models.DateField('Fecha de creacion',auto_now_add=True,null=True, blank=True)
    Fechamodificacion = models.DateField('Fecha de modificacion',auto_now=True,null=True, blank=True)


    class Meta:
        verbose_name = 'Estado de finalizaciòn'
        verbose_name_plural = 'Estados de finalizaciòn'
        
    def __str__(self):
        """Retorna el estado del curso."""
        return self.Nombre

class curso_profesor(models.Model):
    """Datos generales de carrera"""
    Fechainicio = models.DateField("Fecha de inicio",null=True, blank=True)
    Fechafinal = models.DateField("Fecha de finalizacion",null=True, blank=True)
    Cohorte = models.PositiveIntegerField("Cohorte",null=True, blank=True)
    Profesorid = models.ForeignKey(profesor, on_delete = models.CASCADE,verbose_name='Profesor')
    Cursoid = models.ForeignKey(curso, on_delete = models.CASCADE,verbose_name='Curso')
    Estadoid = models.ForeignKey(estado, on_delete = models.CASCADE,verbose_name='Estado de finalizacion')
    Fechacreacion = models.DateField('Fecha de creacion',auto_now_add=True,null=True, blank=True)


    class Meta:
        verbose_name = 'Curso - Profesor'
        verbose_name_plural = 'Cursos - Profesores'
        
    def __str__(self):
        """Retorna el curso llevado por el profesor."""
        return self.Cohorte

class operador_profesor(models.Model):
    """Datos generales de operador - profesor"""
    Telefono = models.CharField("Numero de telefono", max_length=45,unique=True)
    Profesorid = models.ForeignKey(profesor, on_delete = models.CASCADE,verbose_name='Profesor')
    OPeradorid = models.ForeignKey(operador, on_delete = models.CASCADE,verbose_name='Operadora')
    Fechacreacion = models.DateField('Fecha de creacion',auto_now_add=True,null=True, blank=True)

    
    class Meta:
        verbose_name = 'OPerador - Profesor'
        verbose_name_plural = 'Operadores - Profesores'
        
    def __str__(self):
        """Retorna el curso llevado por el profesor."""
        return self.Telefono