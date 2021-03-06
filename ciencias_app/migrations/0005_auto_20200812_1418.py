# Generated by Django 3.1 on 2020-08-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciencias_app', '0004_operador_profesor_fechacreacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrera',
            name='Fechacreacion',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AddField(
            model_name='curso',
            name='Fechacreacion',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AddField(
            model_name='curso_profesor',
            name='Fechacreacion',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='Fechacreacion',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AddField(
            model_name='estado',
            name='Fechacreacion',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AddField(
            model_name='operador',
            name='Fechacreacion',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AddField(
            model_name='profesor',
            name='Fechacreacion',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AddField(
            model_name='tipodecurso',
            name='Fechacreacion',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de creacion'),
        ),
    ]
