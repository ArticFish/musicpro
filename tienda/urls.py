"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import index,iniciar,iniciarsesion,registro,registrar,cerrarsesion,pproducto,carritocompra,agregarcarrito
urlpatterns = [
    path('',index,name='index'),
    path('iniciar',iniciar,name='iniciar'),
    path('iniciarsesion',iniciarsesion,name='iniciarsesion'),
    path('registrar',registrar,name='registrar'),
    path('carritocompra/<int:idu>',carritocompra,name='carritocompra'),
    path('registro',registro,name='registro'),
    path('cerrarsesion',cerrarsesion,name='cerrarsesion'),
    path('pproducto/<int:idp>',pproducto,name='pproducto'),
    path('agregarcarrito/<int:idp>/<int:idu>',agregarcarrito,name='agregarcarrito'),
]