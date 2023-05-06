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
    user = get_object_or_404(User,pk=user_id)
    facturasV = FacturaV.objects.all()
    return render(request,'facturaVentas.html',{'facturasV':facturasV})

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



def buscarFacturaC(request):
    if request.method == 'GET':
        fecha = request.GET.get('fecha')
        if fecha:
            try:
                fecha = datetime.strptime(fecha, '%d/%m/%Y').date()
                facturas = FacturaC.objects.filter(fecha=fecha)
            except ValueError:
                facturas = FacturaC.objects.none()
        else:
            facturas = FacturaC.objects.all()
        return render(request, 'facturaCompras.html', {'facturas': facturas})



'''Facturas Compra'''
def facturaC(request,user_id):
    user = get_object_or_404(User,pk=user_id)
    facturasC = FacturaC.objects.all()
    return render(request,'facturaCompras.html',{'facturasC':facturasC})

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
    pass

def eliminarFacturaC(request,user_id, facturaC_idFacturaC):
    pass

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
    if request.method == 'GET':
        return render(request, 'agregarProducto.html',{'form':ProductoForm(), 'user':user})
    else:
        try:    
            form = ProductoForm(request.POST)
            newProducto = form.save(commit=False)
            newProducto.user = request.user
            newProducto.user = user
            newProducto.save()
            return redirect('inventario/', newProducto.user.id)
        except ValueError:
            return render(request,'agregarProducto.html',{'form':ProductoForm(),'error':'bad data passed in'})
        
        
        
def actualizarProducto(request,user_id, producto_idProducto):
    producto = get_object_or_404(Producto,pk=producto_idProducto,user=request.user)
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



def reporteGanancias(request):
    ventas = FacturaV.objects.values('idFacturaV').annotate(total=Sum('totall'))
    reporte = []
    for venta in ventas:
        factura = FacturaV.objects.get(idFacturaV=venta['idFacturaV'])
        reporte.append((factura.user.username, venta['total']))
    return render(request, 'reporteGanancias.html', {'reporte': reporte})

'''
def categoria(request, user_id):
    user = get_object_or_404(User,pk=user_id)
    categorias = Categoria.objects.filter(user = user)     
    return render(request, 'categoria.html', {'categorias': categorias})



def agregarCategoria(request, user_id):
    user = get_object_or_404(User,pk=user_id)
    if request.method == 'GET':
        return render(request, 'agregarCategoria.html',{'form':CategoriaForm(), 'user':user})
    else:
        try:    
            form = CategoriaForm(request.POST)
            newCategoria = form.save(commit=False)
            newCategoria.user = request.user
            newCategoria.user = user
            newCategoria.save()
            return redirect('categoria/', newCategoria.user.id)
        except ValueError:
            return render(request,'agregarCategoria.html',{'form':ProductoForm(),'error':'bad data passed in'})
            
            
            '''
            