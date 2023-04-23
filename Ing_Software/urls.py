"""Ing_Software URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lati import views as appViews
from cuentas import views as cuenViews
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appViews.home, name='home'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('login/home/', appViews.home, name='home'),
    path('registro/', cuenViews.register, name='register'),
    path('logout/', cuenViews.logoutaccount, name='logoutaccount'),
    
    #path('usuario/<int:user_id>/categoria/', appViews.categoria, name='categoria'),
    #path('usuario/<int:user_id>/agregarCategoria' , appViews.agregarCategoria, name='agregarCategoria'),
    
    
    path('usuario/<int:user_id>/inventario/', appViews.producto, name='inventario'),
    path('usuario/<int:user_id>/agregarProducto' , appViews.agregarProducto, name='agregarProducto'),
    path('usuario/<int:user_id>/actualizarProducto/<int:producto_idProducto>' , appViews.actualizarProducto, name='actualizarProducto'),
    path('usuario/<int:user_id>/eliminarProducto/<int:producto_idProducto>' , appViews.eliminarProducto, name='eliminarProducto'),
    
    path('usuario/<int:user_id>/agregarFacturaC/', appViews.agregarFacturaC,name='agregarFacturaC'),
    path('usuario/<int:user_id>/agregarFacturaV/', appViews.agregarFacturaV,name='agregarFacturaV'),
    
    path('usuario/<int:user_id>/facturaC/', appViews.facturaC,name='facturaC'),
    path('usuario/<int:user_id>/facturaV/', appViews.facturaV,name='facturaV'),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
