from django.contrib import admin
from .models import Departamentos, Encontrados, Habitaciones, Perdidos
# Register your models here.

class Perdidosadmin(admin.ModelAdmin):
    search_fields = ["cliente"]
    list_display = ('cliente','habitacion','fecha','lugar','reporte','empleado','estado','objetos')
    list_filter = ('fecha','estado','habitacion')
    class Meta:
        model = Perdidos

class Encontradoadmin(admin.ModelAdmin):
    list_display = ('entrega','departamento','lugar','fecha','detalle','seguridad','reporte','estado')


#models
admin.site.register(Departamentos)
admin.site.register(Encontrados,Encontradoadmin)
admin.site.register(Habitaciones)
admin.site.register(Perdidos,Perdidosadmin)
