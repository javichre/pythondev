from django.db import models
from datetime import date
from datetime import datetime
from django.utils import timezone
from apps.objetos.models import Departamentos
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.timezone import now



#model para registrar empresas
class Empresas(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, null=False,blank=False)
    telefono = models.CharField(max_length = 13, null=False, blank=False)

### este puede ser el trigger para actualizar ##
    verbose_name = 'Empresa'
    vebose_name_plural = 'Empresa'

    def __str__(self):
        return self.nombre

class Calidadmot(models.Model):
    id = models.AutoField(primary_key = True)
    razon_visita = models.CharField(max_length = 40 ,null =False, blank = False)

    verbose_name= 'motivo'
    verbose_name_plural = 'motivo'

    def __str__(self):
        return self.razon_visita


# modelo para registrar visitas
class Visitas(models.Model):
    Nombre = models.CharField(max_length= 100, null = False, blank = False)
    Empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    Visitado = models.CharField(max_length = 100, null = False, blank = False)
    Calidad_de = models.ForeignKey(Calidadmot, on_delete=models.CASCADE)
    Departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    Fecha_visita = models.DateField(default = date.today) #
    Motivo_visita = models.CharField(max_length = 200, null= False, blank = False)
    Numero_de_visita = models.AutoField(primary_key = True)
    fecha_creacion = models.DateTimeField(default = datetime.now, editable = True)
    
    verbose_name = 'Visita'
    verbose_name_plural = 'Visita'

    def __str__(self):
        return self.Nombre
        




