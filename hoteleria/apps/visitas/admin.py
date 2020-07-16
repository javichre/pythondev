from django.contrib import admin
from apps.visitas.models import Visitas, Empresas, Calidadmot

# Register your models here.


class Visitasadmin(admin.ModelAdmin):
    search_fields = ["Nombre"]
    list_display = ('Nombre','Visitado','Calidad_de','Departamento','Fecha_visita','Motivo_visita','Numero_de_visita','fecha_creacion')
    list_filter = ('Nombre','Visitado','Departamento')
    class Meta:
        model = Visitas

class Empresasadmin(admin.ModelAdmin):
    list_display = ('nombre','telefono')


admin.site.register(Visitas,Visitasadmin)
admin.site.register(Empresas,Empresasadmin)
admin.site.register(Calidadmot)

