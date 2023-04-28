from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreC = models.CharField(max_length=50)

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombreProducto =  models.CharField(max_length=50)
    descripcion =   models.CharField(max_length=100)
    cantidadProducto = models.IntegerField()
    precioUnit = models.IntegerField()
    foto = models.ImageField(upload_to='lati/images/')
    peso = models.FloatField()
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    
    

class FacturaC(models.Model):
    idFacturaC = models.IntegerField(primary_key=True)
    cantProduct = models.IntegerField()
    costo =models.IntegerField()
    fecha = models.CharField(max_length=20)
    nombreProveedor = models.CharField(max_length=50)
    
    def __str__(self):
        return "id Factura Compra: " +self.idFacturaC

    
class FacturaV(models.Model):
    idFacturaV = models.IntegerField(primary_key=True)
    cantProduct = models.IntegerField()
    totall =models.IntegerField()
    estado = models.CharField(max_length=50)
    nombreCliente = models.CharField(max_length=50)
    debe=models.BooleanField(default=False, null=True)
    cuanto=models.IntegerField(null=True)
    
    def __str__(self):
        return "id Factura Venta: " + self.idFacturaV
    