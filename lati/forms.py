from django import forms
from django.forms import ModelForm, Textarea
from .models import *

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
        
class FacturaV(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,**kwargs)
        self.fields['idFacturaV'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombreCliente'].widget.attrs.update({'class': 'form-control'})
        self.fields['cantProduct'].widget.attrs.update({'class': 'form-control'})
        self.fields['total'].widget.attrs.update({'class': 'form-control'})
        self.fields['estado'].widget.attrs.update({'class': 'form-control'})
        
    class Meta:
        model = FacturaV
        fields = ['idFacturaV','cantProduct','total','estado','nombreCliente','debe','cuanto']
        labels = {'idFacturaV': 'ID Factura',
            'cantProduct': 'Cantidad del producto',
            'total': 'Precio total factura',
            'estado': 'Estado de la factura',
            'nombreCliente': 'Nombre del Cliente',
            'debe':'¿El cliente debe?',
        }
        
        widgets = {
            'nombreCliente': forms.TextInput(attrs={'class': 'form-control'}),
            'idFacturaV': forms.TextInput(attrs={'class': 'form-control'}),
            'cantProduct': forms.TextInput(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}), 
        }

class FacturaC(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,**kwargs)
        self.fields['idFacturaC'].widget.attrs.update({'class': 'form-control'})
        self.fields['cantProduct'].widget.attrs.update({'class': 'form-control'})
        self.fields['costo'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombreProveedor'].widget.attrs.update({'class': 'form-control'})

        
    class Meta:
        model = FacturaC
        fields = ['idFacturaC','cantProduct','costo','fecha','nombreProveedor']
        labels = {'idFacturaC': 'ID Factura',
            'cantProduct': 'Cantidad del producto',
            'costo': 'Precio total factura',
            'fecha': 'Estado de la factura',
            'nombreProveedor': 'Nombre del Cliente',
        }
        
        widgets = {
            'idFacturaC': forms.TextInput(attrs={'class': 'form-control'}),
            'cantProduct': forms.TextInput(attrs={'class': 'form-control'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'}), 
            'nombreProveedor': forms.TextInput(attrs={'class': 'form-control'}),
        }
