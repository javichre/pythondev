# Generated by Django 2.2.11 on 2020-07-11 03:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Departamento', models.CharField(max_length=70)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'ordering': ['Departamento'],
            },
        ),
        migrations.CreateModel(
            name='Habitaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Habitacion', models.CharField(max_length=6)),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
                'ordering': ['Habitacion'],
            },
        ),
        migrations.CreateModel(
            name='Perdidos',
            fields=[
                ('cliente', models.CharField(max_length=80)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('objetos', models.CharField(max_length=250)),
                ('lugar', models.CharField(max_length=50)),
                ('reporte', models.AutoField(primary_key=True, serialize=False)),
                ('empleado', models.CharField(max_length=80)),
                ('estado', models.BooleanField(default=False, verbose_name='Encontrado/No encontrado')),
                ('user', models.CharField(blank=True, max_length=50, null=True)),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objetos.Habitaciones')),
            ],
            options={
                'verbose_name': 'Perdidos',
                'ordering': ['reporte'],
            },
        ),
        migrations.CreateModel(
            name='Encontrados',
            fields=[
                ('entrega', models.CharField(max_length=80)),
                ('lugar', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField()),
                ('reporte', models.AutoField(primary_key=True, serialize=False)),
                ('detalle', models.CharField(blank=True, max_length=200, null=True)),
                ('seguridad', models.CharField(max_length=80)),
                ('estado', models.BooleanField(default=False, verbose_name='Abierto/Cerrado')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objetos.Departamentos')),
            ],
            options={
                'verbose_name': 'Encontrado',
                'verbose_name_plural': 'Encontrados',
                'ordering': ['entrega'],
            },
        ),
    ]
