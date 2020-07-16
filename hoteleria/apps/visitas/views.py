from django.shortcuts import render,redirect
from .forms import Visitasform, Empresasform
from .models import Visitas,Empresas
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView,ListView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate
from django.core.paginator import Paginator
from .forms import Visitasform
from .models import Visitas

# Create your views here.

"""
   dispath(): valida la peticion  y elige que metodo HTTP se utilizo para la solicitud
   http_method_not_allowed(): retorna un error cuando se utiliza un metodo HTTP no soportado o definido
   options()
"""

# crear vista para registrar visitas con vistas basadas en funcion
def Registrarvisitas(request):
    return render(request,'visitas/registrar_visitas.html')



def Crearvisita(request):
    if request.method == 'POST':
        crearform = Visitasform(request.POST)
        if crearform.is_valid():
            crearform.save()
            return redirect('index')
    
    else:
        crearform = Visitasform()
    return render(request,'visitas/registrar_visitas.html',{'crearform':crearform})



def Listarvisitas(request):
    visitas = Visitas.objects.all()
    return render(request, 'visitas/listar_visitas.html',{'visitas':visitas})


    #if request.method == 'POST':
     #   registrarform = Visitasform(request.POST)
      #  if registrarform.is_valid():
       #     registrarform.save()
        #    return redirect('index')
    
    # sino se cumplen las condiciones
    #else:
     #   registrarform = Visitasform()
      #  return render (request,'visitas/registrar_visitas.html',{'registrarform':registrarform})