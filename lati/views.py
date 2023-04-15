from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import *
from .forms import UserRegisterForm
from django.contrib import messages


from .forms import ProductoForm#, CategoriaForm
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def facturaV(request):
    return render(request, 'facturaVentas.html')

def facturaC(request):
    return render(request, 'facturaCompras.html')

def inventario(request, user_id):
    user = get_object_or_404(User,pk=user_id)

        
    return render(request, 'inventario.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('/login')
            
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    return render(request, 'login.html')

def logoutaccount(request):
    logout(request)
    return redirect('home')

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
            