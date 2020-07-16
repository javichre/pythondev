from django import forms
from .models import Visitas,Empresas

class Visitasform(forms.ModelForm):
    class Meta:       
        model = Visitas
        fields = [
            'Nombre', 'Empresa', 'Visitado', 'Calidad_de',  'Fecha_visita', 'Departamento', 'Motivo_visita', 'fecha_creacion', 'Numero_de_visita','fecha_creacion']
        labels = {
            'Nombre': 'Visitante',
        }
        widgets = {
            'Nombre': forms.TextInput(
                attrs={
                    'class': 'form-control col-md-8',
                    'placeholder':'Nombre del visitante'
                }
            ),
              'Empresa': forms.Select(
                attrs={
                    'class': 'form-control col-md-6',
                    'placeholder':'Nombre del visitante'
                }
            ),
              'Departamento': forms.Select(
                attrs={
                    'class': 'form-control col-md-8',
                }
            ),
               'Visitado': forms.TextInput(
                attrs={
                    'class': 'form-control col-md-8',
                    'placeholder':'Nombre del visitado'

                }
            ),
             'Calidad_de': forms.Select(
                attrs={
                    'class': 'form-control col-md-8',
                    'placeholder':''

                }
            ),
               'Motivo_visita': forms.TextInput(
                attrs={
                    'class': 'form-control col-md-8',
                    'placeholder':'motivo de la visita',
                    'id': 'disabledFieldsetCheck',
                   
                }
            ),
            'Fecha_visita': forms.DateInput(
                attrs={
                    'class': 'form-control col-md-3',                
                }
            ),
               'fecha_creacion': forms.DateTimeInput(
                attrs={
                    'class': 'form-control col-md-3 ',                
                }
            ),

            'fecha_creacion': forms.DateTimeInput(
                attrs={
                    'class': 'form-control col-md-3',                    
                }
            ),
        }

class Empresasform(forms.ModelForm):
    class Meta:
        fields = [
            'id', 'nombre', 'telefono'
        ]
   