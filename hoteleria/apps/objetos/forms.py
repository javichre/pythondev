from django import forms
from .models import Habitaciones, Perdidos, Encontrados, Departamentos

class EncontradosForm(forms.ModelForm):
    class Meta:
        model = Encontrados
        fields = ['entrega', 'departamento','lugar','fecha','reporte','seguridad','detalle','estado']
        labels = {
            'entrega': 'Nombre de quien entrega',
            
        }
        widgets = {
            'entrega': forms.TextInput( 
                attrs = {
                    'class': 'form-control  col-md-8',
                    'placeholder':'Ingrese el nombre de quien entrega'
                }
            ),
          
               'lugar': forms.TextInput( 
                attrs = {
                    'class': 'form-control col-md-8',
                    'placeholder':'Donde se encontraron los objetos'
                    
                }
            ),
             'departamento': forms.Select( 
                attrs = {
                    'class': 'form-control col-md-3'
                }
            ),
               
             'seguridad': forms.TextInput( 
                attrs = {
                    'class': 'form-control col-md-8'
                }
            ),
            
             'fecha': forms.TextInput( 
                attrs = {
                    'class': 'form-control col-md-3'
                }
            ),
             'detalle': forms.Textarea( 
                attrs = {
                    'class': 'form-control col-md-8 position-relative',
                    'placeholder':'Detalle los objetos encontrados'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control col-md-1',
                    
                }
            ),
        }

class PerdidosForm(forms.ModelForm):
    class Meta:
        model = Perdidos
        fields = ['cliente', 'habitacion','fecha','empleado','lugar','reporte','objetos','estado', 'user']
        labels = {
            'cliente': 'Nombre del cliente',
        }

        widgets = {
            'cliente': forms.TextInput(
                attrs={
                    'class': 'form-control col-md-8',
                    'placeholder': 'Nombre del cliente'
                }
            ),
               'habitacion': forms.Select(
                attrs={
                    'class': 'form-control col-md-3',                   
                }
            ),
              'fecha': forms.TextInput( 
                attrs = {
                    'class': 'form-control col-md-3',
                    'claa': 'readonly'
                }
            ),
            'empleado': forms.TextInput(
                attrs={
                    'class': 'form-control col-md-8',
                    'placeholder': 'Nombre del empleado'
                }
            ),
            'lugar': forms.TextInput(
                attrs={
                    'class': 'form-control col-md-8',
                    'placeholder': 'Donde se perdio'
                }
            ),
            'objetos': forms.Textarea(
                attrs={
                    'class': 'form-control col-md-8',
                    'placeholder': 'Detalles los objetos perdidos'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control col-md-1',
                    
                }
            ),
        }
       
          