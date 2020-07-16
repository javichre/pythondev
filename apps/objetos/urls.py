from django.urls import path,re_path
from django.contrib.auth.decorators import login_required
from .views import CrearEncontrados,ListarEnconrados, EditarEncontrado, EliminarEncontrado, Listadoencontrado,Todos,Registrarperdidos,Listadoperdido,Editarperdidos,Entregados,Perdidosencontrados,Pedidossinhayar,Filtrodepartamento,Filtroreporte,Filtrofecha,Filtrodepartamentoper,Filtrofechaper,Filtroreporteper
from apps.usuarios.views import Logout

urlpatterns = [
path('registrar_encontrado/',login_required (CrearEncontrados), name = 'registrar_encontrado'),

#path('listar_encontrados/',login_required(Listadoencontrado.as_view()), name = 'listar_encontrados'),

path('objetos_encontrados_sin_entrgar/',login_required (Listadoencontrado.as_view()), name ='listar_encontrados'),

path('listado_completo_de_perdidos/',login_required (Listadoperdido.as_view()), name ='listar_perdidos'),

path('Objetos_perdidos_encontrados/',login_required (Perdidosencontrados.as_view()),name = 'perdidos_encontrados'),

path('Objetos_perdidos_sin_hayar/',login_required (Pedidossinhayar.as_view()),name = 'perdidos_sin_hayar'),

path('Listado_de_objetos_entregados/',login_required (Entregados.as_view()), name = 'Entregados'),

path('todos_encontrados/',login_required (Todos.as_view()), name ='todos_encontrados'),

path('editar_encontrado/<int:reporte>',login_required (EditarEncontrado), name ='editar_encontrado'),

path('editar_perdidos/<int:reporte>',login_required (Editarperdidos), name ='editar_perdidos'),

path('eliminar_encontrado/<int:reporte>',login_required (EliminarEncontrado), name ='eliminar_encontrado'),

path('registrar_perdidos/',login_required (Registrarperdidos), name = 'registrar_perdidos'),

path("logout/",Logout, name = "logout"),

path('departamento/',login_required (Filtrodepartamento.as_view()), name = 'filtro_departamento' ),

path('reporte/',login_required (Filtroreporte.as_view()), name = 'filtro_reporte'),

path('fecha/',login_required (Filtrofecha.as_view()), name= 'filtro_fecha'),

path('/',login_required (Filtrodepartamentoper.as_view()), name = 'filtro_departamento_per'),

path('/', login_required (Filtroreporteper.as_view()), name = 'filtro_reporte_per'),

path('/',login_required (Filtrofechaper.as_view()), name = 'filtro_fecha_per'),



]
