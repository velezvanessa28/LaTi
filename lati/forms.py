from django import forms
from django.forms import ModelForm, Textarea
from .models import *

class ProductoForm(ModelForm):
    
    class Meta:
        model = Producto
        fields = ['idProducto','nombreProducto', 'descripcion', 'cantidadProducto','precioUnit', 'image', 'peso']
        labels = {
            'idProducto': 'ID del producto',
            'nombreProducto': 'Nombre del producto',
            'descripcion': 'Descripcion',
            'cantidadProducto': 'Cantidad',
            'precioUnit': 'Precio unitario',
            'image': 'Foto',
            'peso': 'Peso',

        }
        widgets = {
            'idProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidadProducto': forms.NumberInput(attrs={'class': 'form-control'}),
            'precioUnit': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),

        }
    image = forms.ImageField(required=False)
        
    
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,**kwargs)
        self.fields['idProducto'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombreProducto'].widget.attrs.update({'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})
        self.fields['cantidadProducto'].widget.attrs.update({'class': 'form-control'})
        self.fields['precioUnit'].widget.attrs.update({'class': 'form-control'})
        self.fields['peso'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})
        
class FacturaVForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,**kwargs)
        self.fields['idFacturaV'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombreCliente'].widget.attrs.update({'class': 'form-control'})
        self.fields['cantProduct1'].widget.attrs.update({'class': 'form-control'})
        self.fields['totall'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha'].widget.attrs.update({'class': 'form-control'})
        self.fields['estado'].widget.attrs.update({'class': 'form-control'})
        self.fields['debe'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['cuanto'].widget.attrs.update({'class': 'form-control'})
        
    class Meta:
        model = FacturaV
        fields = ['idFacturaV','cantProduct1','totall','estado','fecha','nombreCliente','debe','cuanto']
        labels = {'idFacturaV': 'ID Factura',
            'cantProduct1': 'Cantidad del producto',
            'totall': 'Precio total factura',
            'estado': 'Estado de la factura',
            'fecha': 'Fecha de la factura',
            'nombreCliente': 'Nombre del Cliente',
            'debe':'¿El cliente debe?',
            'cuanto':'¿Cuanto?'
        }
        
        widgets = {
            'nombreCliente': forms.TextInput(attrs={'class': 'form-control'}),
            'idFacturaV': forms.TextInput(attrs={'class': 'form-control'}),
            'cantProduct1': forms.NumberInput(attrs={'class': 'form-control'}),
            'totall': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'}), 
            'estado': forms.TextInput(attrs={'class': 'form-control'}), 
            'debe': forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
            'cuanto': forms.NumberInput(attrs={'class': 'form-control'}), 
        }

class FacturaCForm(ModelForm):
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
            'fecha': 'Fecha de la factura',
            'nombreProveedor': 'Nombre del Cliente',
        }
        
        widgets = {
            'idFacturaC': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantProduct': forms.TextInput(attrs={'class': 'form-control'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'}), 
            'nombreProveedor': forms.TextInput(attrs={'class': 'form-control'}),
        }
