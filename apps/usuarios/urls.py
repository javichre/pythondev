from django.urls import path
from .views import welcome, register,login,logout
from apps.objetos.views import Home


urlpatterns = [
    path('welcome',Home, name = 'welcome'),
    path('register', register, name = 'register'),
    path('logout', logout, name = 'logout'),
  
]
