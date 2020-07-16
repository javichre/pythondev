from django.db import models
from datetime import date
from apps.usuarios.views import LoginViews
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver, Signal
from django.utils.timezone import now
from django.utils import timezone


# Create your models here.

class Departamentos(models.Model):
    Departamento = models.CharField(max_length = 70, null = False, blank = False)

    class Meta:
        verbose_name= 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['Departamento']

    def __str__(self):
        return self.Departamento


class  Encontrados(models.Model):
    entrega = models.CharField(max_length = 80, null = False, blank = False)
    departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    lugar = models.CharField(max_length = 50, null = False, blank = False)
    fecha = models.DateField(default = date.today)
    reporte = models.AutoField(primary_key = True)
    detalle = models.CharField(max_length = 200, blank = True, null = True)
    seguridad = models.CharField(max_length = 80, blank = False, null = False)
    estado = models.BooleanField('Abierto/Cerrado', default = False)
 
    
    class Meta:
        verbose_name = 'Encontrado'
        verbose_name_plural = 'Encontrados'
        ordering = ['entrega']

    def __str__(self):
        return self.detalle

@receiver(pre_save, sender=Encontrados)
def save_post(sender, instance, **kwargs):
    obj_encontrado = Encontrados


class Habitaciones(models.Model):
    Habitacion  = models.CharField(max_length = 6,null=False, blank=False)

    class Meta:
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'
        ordering = ['Habitacion']

    def __str__(self):
        return self.Habitacion

class Perdidos(models.Model):
    cliente = models.CharField(max_length = 80, null= False, blank = False)
    habitacion = models.ForeignKey(Habitaciones, on_delete=models.CASCADE)
    fecha = models.DateField(default = date.today)
    objetos = models.CharField(max_length = 250, null = False, blank = False)
    lugar = models.CharField(max_length = 50, blank = False, null = False)
    reporte = models.AutoField(primary_key = True)
    empleado = models.CharField(max_length = 80, null = False, blank = False)
    estado = models.BooleanField('Encontrado/No encontrado', default=False)
    user = models.CharField(max_length = 50, null = True, blank = True)
    
    

    class Meta:
        verbose_name = 'Perdido'
        verbose_name = 'Perdidos'
        ordering = ['reporte']

    def __str__(self):
        return self.cliente