from django.db import models
from django.contrib.auth.models import User 
import datetime
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
    foto = models.ImageField(upload_to='media/lati/images/', null=True)
    peso = models.FloatField()
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    
    

class FacturaC(models.Model):
    idFacturaC = models.IntegerField(primary_key=True)
    cantProduct = models.IntegerField()
    costo =models.IntegerField()
    fecha = models.DateField(default=datetime.date.today)
    nombreProveedor = models.CharField(max_length=50)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    
class FacturaV(models.Model):
    idFacturaV = models.IntegerField(primary_key=True)
    cantProduct = models.IntegerField()
    totall =models.IntegerField()
    estado = models.CharField(max_length=50)
    nombreCliente = models.CharField(max_length=50)
    fecha = models.DateField(default=datetime.date.today)
    debe=models.BooleanField(default=False, null=True)
    cuanto=models.IntegerField(null=True)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    
