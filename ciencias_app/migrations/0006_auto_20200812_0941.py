# Generated by Django 3.1 on 2020-08-12 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciencias_app', '0005_auto_20200812_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='Nombre',
            field=models.CharField(max_length=120, unique=True, verbose_name='carreras'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='Codigo',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Codigo'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='Nombre',
            field=models.CharField(max_length=120, unique=True, verbose_name='Nombre del curso'),
        ),
        migrations.AlterField(
            model_name='curso_profesor',
            name='Cohorte',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Cohorte'),
        ),
        migrations.AlterField(
            model_name='curso_profesor',
            name='Fechafinal',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de finalizacion'),
        ),
        migrations.AlterField(
            model_name='curso_profesor',
            name='Fechainicio',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='Nombre',
            field=models.CharField(max_length=45, unique=True, verbose_name='Nombre del departamento'),
        ),
        migrations.AlterField(
            model_name='estado',
            name='Nombre',
            field=models.CharField(max_length=120, unique=True, verbose_name='Estado de finalizaciòn'),
        ),
        migrations.AlterField(
            model_name='operador',
            name='Nombre',
            field=models.CharField(max_length=45, unique=True, verbose_name='Nombre de la operadora'),
        ),
        migrations.AlterField(
            model_name='operador_profesor',
            name='Telefono',
            field=models.CharField(max_length=45, unique=True, verbose_name='Numero de telefono'),
        ),
        migrations.AlterField(
            model_name='tipodecurso',
            name='Nombre',
            field=models.CharField(max_length=120, unique=True, verbose_name='Tipo de curso'),
        ),
    ]
