from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import *


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label= 'Correo')
    password1 = forms.CharField(label = 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirma Contraseña', widget=forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        
        
        
class ProductoForm(ModelForm):
    
    class Meta:
        model = Producto
        fields = ['idProducto','nombreProducto', 'descripcion', 'cantidadProducto','precioUnit', 'foto', 'peso']
        labels = {
            'idProducto': 'ID del producto',
            'nombreProducto': 'Nombre del producto',
            'descripcion': 'Descripcion',
            'cantidadProducto': 'Cantidad',
            'precioUnit': 'Precio unitario',
            'foto': 'Foto',
            'peso': 'Peso',

        }
        widgets = {
            'idProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidadProducto': forms.NumberInput(attrs={'class': 'form-control'}),
            'precioUnit': forms.NumberInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),

        }
    foto = forms.ImageField(required=False)
        
    
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,**kwargs)
        self.fields['idProducto'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombreProducto'].widget.attrs.update({'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})
        self.fields['cantidadProducto'].widget.attrs.update({'class': 'form-control'})
        self.fields['precioUnit'].widget.attrs.update({'class': 'form-control'})
        self.fields['peso'].widget.attrs.update({'class': 'form-control'})
        self.fields['foto'].widget.attrs.update({'class': 'form-control-file'})

        
        
'''class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['idCategoria','nombreC']
        labels = {
            'idCategoria': 'ID del producto',
            'nombreC': 'Nombre del producto',

        }
        widgets = {
            'idCategoria': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreC': forms.TextInput(attrs={'class': 'form-control'}),

        }
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,**kwargs)
        self.fields['idCategoria'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombreC'].widget.attrs.update({'class': 'form-control'})
        
        '''
