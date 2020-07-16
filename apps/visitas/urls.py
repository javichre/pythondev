from django.urls import path,re_path
from django.contrib.auth.decorators import login_required
from .views import Registrarvisitas, Crearvisita,Listarvisitas
from apps.usuarios.views import logout

urlpatterns = [
path('registrar_visitas/',login_required (Registrarvisitas), name = 'registrar_visitas'),
path('crear_visitas/',Crearvisita, name = 'crear_visitas'),
path('listar_visitas/', Listarvisitas, name = 'listar_visitas'),
    
]
