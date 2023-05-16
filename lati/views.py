from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import *
from datetime import datetime
from django.db.models import Sum
from .forms import ProductoForm ,FacturaVForm
from .forms import FacturaCForm
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'home.html')

'''Facturas Venta'''
def facturaV(request, user_id):
    searchTerm2 = request.GET.get('busquedafe')
    user = get_object_or_404(User,pk=user_id)
    if searchTerm2:
        facturasV = FacturaV.objects.filter(fecha__icontains=searchTerm2,user=user)
    else:
        facturasV = FacturaV.objects.filter(user=user)
    return render(request,'facturaVentas.html',{'searchTerm2':searchTerm2,'facturasV':facturasV})


def agregarFacturaV(request, user_id):
    user = get_object_or_404(User,pk=user_id)

    if request.method == 'GET':
        return render(request, 'crearFacturaV.html',{'form':FacturaVForm()})
    else:
        try:
            form = FacturaVForm(request.POST)
            newFacturaV = form.save(commit=False)
            newFacturaV.user = request.user
            newFacturaV.user = user
            newFacturaV.save()
            return redirect('facturaV',newFacturaV.user.id)
        except ValueError:
            return render(request,'crearFacturaV.html',{'form':FacturaVForm(),'error':'bad datapassed in'})

def actualizarFacturaV(request,user_id, facturaV_idFacturaV):
    facturaV = get_object_or_404(FacturaV,pk=facturaV_idFacturaV,user=request.user)
    if request.method == 'GET':
        form = FacturaVForm(instance=facturaV)
        return render(request, 'actualizarFacturaV.html',{'facturaV': facturaV,'form':form})
    else:
        try:
            form = FacturaVForm(request.POST,instance=facturaV)
            form.save()
            return redirect('facturaV', facturaV.user.id)
        except ValueError:
            return render(request,'actualizarFacturaV.html',{'facturav': facturaV,'form':form,'error':'Bad data in form'})

def eliminarFacturaV(request,user_id, facturaV_idFacturaV):
    facturaV = get_object_or_404(FacturaV, pk=facturaV_idFacturaV,user=request.user)
    facturaV.delete()
    return redirect('facturaV', facturaV.user.id)



def facturaC(request, user_id):
    searchTerm = request.GET.get('busquedaproveedor')
    searchTerm1 = request.GET.get('searchFacturaC')
    user = get_object_or_404(User,pk=user_id)
    if searchTerm:
        facturasC = FacturaC.objects.filter(nombreProveedor__icontains=searchTerm,user=user)
    elif searchTerm1:
        facturasC = FacturaC.objects.filter(fecha__icontains=searchTerm1,user=user)
    else:
        facturasC = FacturaC.objects.filter(user=user)

    return render(request,'facturaCompras.html',{'searchTerm':searchTerm,'searchTerm1':searchTerm1,'facturasC':facturasC})


'''Facturas Compra'''


def agregarFacturaC(request, user_id):
    user = get_object_or_404(User,pk=user_id)
    if request.method == 'GET':
        return render(request, 'crearFacturaC.html',{'form':FacturaCForm(), 'user':user})
    else:
        try:
            form = FacturaCForm(request.POST)
            newFacturaC = form.save(commit=False)
            newFacturaC.user = request.user 
            newFacturaC.user = user      
            newFacturaC.save()
            return redirect('facturaC',newFacturaC.user.id)
        except ValueError:
            return render(request,'crearFacturaC.html',{'form':FacturaCForm(),'error':'bad datapassed in'})
        
def actualizarFacturaC(request,user_id, facturaC_idFacturaC):
    facturaC = get_object_or_404(FacturaC,pk=facturaC_idFacturaC,user=request.user)
    if request.method == 'GET':
        form = FacturaCForm(instance=facturaC)
        return render(request, 'actualizarFacturaC.html',{'facturaC': facturaC,'form':form})
    else:
        try:
            form = FacturaCForm(request.POST,instance=facturaC)
            form.save()
            return redirect('facturaC', facturaC.user.id)
        except ValueError:
            return render(request,'actualizarFacturaC.html',{'facturaC': facturaC,'form':form,'error':'Bad data in form'})

def eliminarFacturaC(request,user_id, facturaC_idFacturaC):
    facturaC = get_object_or_404(FacturaC, pk=facturaC_idFacturaC,user=request.user)
    facturaC.delete()
    return redirect('facturaC', facturaC.user.id)

'''Productos'''
def inventario(request, user_id):
    user = get_object_or_404(User,pk=user_id)
    return render(request, 'inventario.html')


def producto(request, user_id):
    user = get_object_or_404(User,pk=user_id)
    productos = Producto.objects.filter(user = user)     
    return render(request, 'inventario.html', {'productos': productos})


def agregarProducto(request, user_id):
    user = get_object_or_404(User,pk=user_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.user = request.user  # Asigna el usuario actual si es necesario
            producto.save()
            return redirect('inventario/', producto.user.id)
    else:
        form = ProductoForm()
    return render(request, 'agregarProducto.html', {'form': ProductoForm})
    if request.method == 'GET':
        return render(request, 'agregarProducto.html',{'form':ProductoForm(), 'user':user})
    else:
        try:    
            form = ProductoForm(request.POST, request.FILES)
            newProducto = form.save(commit=False)
            newProducto.user = request.user
            newProducto.user = user
            newProducto.save()
            return redirect('inventario/', newProducto.user.id)
        except ValueError:
            return render(request,'agregarProducto.html',{'form':ProductoForm(),'error':'bad data passed in'})
        
def actualizarProducto(request,user_id, producto_idProducto):
    producto = get_object_or_404(Producto,pk=producto_idProducto,user=request.user)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('../inventario/', producto.user.id)
    else:
        form = ProductoForm(instance=producto)
    
    return render(request,'actualizarProducto.html',{'producto': producto,'form':form,'error':'Bad data in form'})
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
        return render(request, 'actualizarProducto.html',{'producto': producto,'form':form})
    else:
        try:
            form = ProductoForm(request.POST,instance=producto)
            form.save()
            return redirect('../inventario/', producto.user.id)
        except ValueError:
            return render(request,'actualizarProducto.html',{'producto': producto,'form':form,'error':'Bad data in form'})
        

def eliminarProducto(request,user_id, producto_idProducto):
    producto = get_object_or_404(Producto, pk=producto_idProducto,user=request.user)
    producto.delete()
    return redirect('../inventario/', producto.user.id)

'''Reportes'''
def reporteInventario(request,user_id):
    user = get_object_or_404(User,pk=user_id)
    productos = Producto.objects.filter(user = user)    
    
    totalProductos=0
    labels=[]
    data=[]
    
    for producto in productos:
        totalProductos=totalProductos+producto.cantidadProducto
        labels.append(producto.idProducto)
        data.append(producto.cantidadProducto)
        
    return render(request, 'reporteInventario.html', {'productos': productos,'data':data,'labels':labels,'totalProductos':totalProductos})

def reporteGanancias(request, user_id):
    searchTerm = request.GET.get('searchFacturaV')
    user = get_object_or_404(User,pk=user_id)
    totalCantProd = 0
    totalCostos=0
    labels=[]
    data=[]
    if searchTerm:
        facturasV = FacturaV.objects.filter(fecha__icontains=searchTerm,user=user)
    else:
        facturasV = FacturaV.objects.filter(user=user)
    
    for factura in facturasV:
        totalCantProd=totalCantProd+factura.cantProduct
        totalCostos=totalCostos+factura.totall
        labels.append(factura.idFacturaV)
        data.append(factura.totall)
        
    return render(request,'reporteGanancias.html',{'searchTerm':searchTerm,'facturasV':facturasV,'totalCantProd':totalCantProd,'totalCostos':totalCostos,'labels':labels,'data':data})

def reporteGastos(request,user_id):
    searchTerm = request.GET.get('searchFacturaC')
    user = get_object_or_404(User,pk=user_id)
    totalCantProd = 0
    totalCostos=0
    labels=[]
    data=[]
    if searchTerm:
        facturasC = FacturaC.objects.filter(fecha__icontains=searchTerm,user=user)
    else:
        facturasC = FacturaC.objects.filter(user=user)
    
    for factura in facturasC:
        totalCantProd=totalCantProd+factura.cantProduct
        totalCostos=totalCostos+factura.costo
        labels.append(factura.idFacturaC)
        data.append(factura.costo)
        
    return render(request,'reporteGastos.html',{'searchTerm':searchTerm,'facturasC':facturasC,'totalCantProd':totalCantProd,'totalCostos':totalCostos,'labels':labels,'data':data})
