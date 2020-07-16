"""hoteleria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from apps.objetos.views import  Home
from apps.usuarios.views import LoginViews
from django.contrib.auth.views import logout_then_login
#from apps.usuario.views import Login, logoutUsuario

urlpatterns = [
    path('admin/',admin.site.urls),
    path('objetos/',include(('apps.objetos.urls','objetos'))),
    path('visitas/',include(('apps.visitas.urls','visitas'))),
    path('',include(('apps.usuarios.urls','usuarios'))),
    path('',login_required (Home), name='index'),
    path('login/', LoginViews.as_view(), name = 'login'),
    





    #path('usuario/',include('apps.usuario.urls','usuario')),
    #path('',Inicio.as_view(),name='index'),
   # path('',Login.as_view(), name= 'login'),
    #path('logout/',login_required(logoutUsuario), name = 'logout'),
    
]
