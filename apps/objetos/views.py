from django.shortcuts import render, redirect
from .forms import EncontradosForm, PerdidosForm
from .models import Encontrados, Perdidos
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView,UpdateView
from django.urls import reverse_lazy # para class views
from django.contrib.auth import authenticate
from django.core.paginator import Paginator

# Create your views here.

"""
   dispath(): valida la peticion  y elige que metodo HTTP se utilizo para la solicitud
   http_method_not_allowed(): retorna un error cuando se utiliza un metodo HTTP no soportado o definido
   options()
"""

def Home(request):
    return render(request,'index.html')

#class Editarperdidos(UpdateView):
    #model = Perdidos
    #form_class = PerdidosForm
    #template_name = 'objetos/perdidos.html' 
    #success_url = reverse_lazy('objetos:listar_perdidos')

# vista basada un funciones para registrar perdidos
def Registrarperdidos(request):
    if request.method == 'POST':        
        perdidoform = PerdidosForm(request.POST)
        if perdidoform.is_valid():            
            perdidoform.save()
            return redirect('objetos:listar_perdidos')
    else:
        perdidoform = PerdidosForm()
        return render (request,'objetos/perdidos.html',{'perdidoform':perdidoform})

# esta es la vista para editar los objetos perdidos   
def Editarperdidos(request,reporte):
    perdidoform = None
    error = None
    try:
        perdido = Perdidos.objects.get(reporte = reporte)
        if request.method == 'GET':
            perdidoform = PerdidosForm(instance=perdido)
        else:
            perdidoform = PerdidosForm(request.POST, instance=perdido)
            if perdidoform.is_valid():
                perdidoform.save()
            return  redirect('objetos:listar_perdidos')
    except Exception as e:
        error = e
    return render(request,'objetos/perdidos.html',{'perdidoform':perdidoform,'error':error})

# esta es la vista de listar todos los objetos perdidos
class Listadoperdido(ListView):  
    model = Perdidos
    template_name = 'objetos/listar_perdidos.html'
    context_object_name = 'perdidos'
    queryset = Perdidos.objects.all()
    paginate_by = 10

#con esta vista se lista los objetos que que se reportaron como perdidos pero ya han sido encontrados
class Perdidosencontrados(ListView):
    model = Perdidos
    template_name = 'objetos/listar_perdidos.html'
    queryset = Perdidos.objects.filter(estado = True)
    paginate_by = 10

#con esta vista se listas los objetos reportados como perdidos que no se han encontrado
class Pedidossinhayar(ListView):
    model = Perdidos
    template_name = 'objetos/listar_perdidos.html'
    queryset = Perdidos.objects.filter(estado = False)
    paginate_by = 10

# vista creada para filtrar los perdiso por departamento
class Filtrodepartamentoper(ListView):
    model = Perdidos
    template_name = 'objetos/listar_perdidos.html'
    queryset  = Perdidos.objects.all().order_by('habitacion')
    paginate_by = 10

# vista creada para filtrar los perdiso por quien reporte (no esta en uso)
class Filtroreporteper(ListView):
    model = Perdidos
    template_name = 'objetos/listar_perdidos.html'
    queryset  = Perdidos.objects.all().order_by('reporte')
    paginate_by = 10

#vista para el filtro por fecha
class Filtrofechaper(ListView):
    model = Perdidos
    template_name = 'objetos/listar_perdidos.html'
    queryset = Perdidos.objects.all().order_by('-fecha')
    paginate_by = 10

######## aqui empiezan las vistas de encontrados #############

# vista crear nuevo endontrado basada en funciones (no esta en uso)
def CrearEncontrados(request):
    if request.method == 'POST':

        # esto que comente solo se usa cuando guardo los datos usando el form
        encontradoform = EncontradosForm(request.POST)
        if encontradoform.is_valid():
            encontradoform.save()
            return redirect('objetos:listar_encontrados')    
    else:
        encontradoform = EncontradosForm()
        return render(request,'objetos/registrar_objetos.html',{'encontradoform':encontradoform})

# esta es la vista para editar los objetos encontrados
def EditarEncontrado(request,reporte):
    encontradoform = None
    error = None
    try:
        encontrado = Encontrados.objects.get(reporte = reporte)
        if request.method =='GET':
            encontradoform = EncontradosForm(instance=encontrado)
        else:            
            encontradoform = EncontradosForm(request.POST, instance=encontrado)
            if encontradoform.is_valid():
                encontradoform.save()
            return redirect('objetos:listar_encontrados')
    except Exception as e:
        error = e    
    return render(request,'objetos/registrar_objetos.html',{'encontradoform':encontradoform,'error':error})

##esta es la vista para listar todos los objetos encontrados
class Todos(ListView):
    model = Encontrados
    template_name = 'objetos/listar_encontrados.html'
    queryset = Encontrados.objects.all()
    paginate_by = 10

# esta es la vista de listar los objetos ecnontrados que aun no se reclaman
class Listadoencontrado(ListView):   
    model = Encontrados
    template_name = 'objetos/listar_encontrados.html'
    context_object_name = 'encontrados'
    queryset = Encontrados.objects.filter(estado = False)
    paginate_by = 10
  
#esta es la vista para listar los objetos encontrados que han sido reclamados por el cliente
class Entregados(ListView):
    model = Encontrados
    template_name = 'objetos/listar_encontrados.html'
    context_object_name = 'encontrados'
    queryset = Encontrados.objects.filter(estado = True)
    paginate_by = 10

    #def get(self, request, *args, **kwargs):
     #   if request.user.is_authenticated:
      #      return render(self.template_name)       
       # else:
        #    return redirect('index')

# vista creada para filtrar por departamento
class Filtrodepartamento(ListView):
    model = Encontrados
    template_name = 'objetos/listar_encontrados.html'
    queryset  = Encontrados.objects.all().order_by('departamento')
    paginate_by = 10

# vista creada para filtrar por quien reporte
class Filtroreporte(ListView):
    model = Encontrados
    template_name = 'objetos/listar_encontrados.html'
    queryset  = Encontrados.objects.all().order_by('reporte')
    paginate_by = 10

#vista para el filtro por fecha
class Filtrofecha(ListView):
    model = Encontrados
    template_name = 'objetos/listar_encontrados.html'
    queryset = Encontrados.objects.all().order_by('fecha')
    paginate_by = 10

# vista basada en funciones listar encontrados no esta en uso
def ListarEnconrados(request):
    encontrados = Encontrados.objects.filter(estado = True)
    return render(request, 'objetos/listar_encontrados.html',{'encontrados':encontrados})

#esta vista no esta en funcionamiento pero esta creada para ocultar la informacion a la vista del usuario(no se borra)
def EliminarEncontrado(request, reporte):
    # asi se elimina de manera directa 
    encontrado = Encontrados.objects.get(reporte = reporte)
    if request.method == 'POST':
        #encontrado.delete() esto solo se usa para borrar da manera directa

        # borrar de manera logica
        encontrado.estado = False
        encontrado.save()
        return redirect('objetos:listar_encontrados')
    return render(request, 'objetos/eliminar_encontrado.html',{'encontrado':encontrado})
    



        






    
    
