from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import producto,carrito
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import math 
from guest_user.decorators import allow_guest_user
from django.contrib.auth.decorators import user_passes_test,login_required

# Create your views here.
@allow_guest_user
def index(request):
    lproductos = producto.objects.all()
    for m in lproductos:
        if m.oferta !=0:
            m.preciooferta = math.trunc(m.precio - (m.precio*m.oferta/100))
            m.save()
    contexto = {"lista":lproductos}
    return render(request,'index.html',contexto)


@user_passes_test(lambda u: u.is_authenticated,login_url='iniciar')
def carritocompra(request,idu):
    if request.user.id == idu:
        lproductos = carrito.objects.filter(idUsuario=idu)
        contexto = {"lista":lproductos}
        return render(request,'carritocompra.html',contexto)
    else:
        return redirect('index')


def registro(request):
    return render(request,'registro.html')

def pagoproducto(request):
    pag = request.META.get('HTTP_REFERER')
    contexto = {"lista":pag}
    return render(request,'pago.html',contexto)

def iniciar(request):
    return render(request,'iniciar.html')

def pproducto(request,idp):
    lproductos = producto.objects.get(idProducto=idp)
    #ofertas = math.trunc(lproductos.precio - (lproductos.precio*lproductos.oferta/100))
    if lproductos.oferta != 0:
        lproductos.preciooferta = math.trunc(lproductos.precio - (lproductos.precio*lproductos.oferta/100))
    contexto = {"lista":lproductos}
    return render(request,'pproducto.html',contexto)

@user_passes_test(lambda u: u.is_authenticated,login_url='index')
def cerrarsesion(request):
    logout(request)
    return redirect('index')


def agregarcarrito(request,idp,idu):
    if request.user.id == idu:
        pro = producto
        usuario = User
        cantidadproducto = request.POST['quantity']
        stock = producto.objects.get(idProducto=idp)
        pro.idProducto = producto.objects.get(idProducto=idp)
        usuario.id = User.objects.get(id=idu)
        try:
            carro=carrito.objects.get(idProducto=pro.idProducto,idUsuario=usuario.id)
            carro.cantidad = carro.cantidad+int(cantidadproducto)
            carro.save()
        except:
            carrito.objects.create(idProducto=pro.idProducto,idUsuario=usuario.id,cantidad=cantidadproducto)

        stock.stock=stock.stock-int(cantidadproducto)
        stock.save()
        return redirect('index')
    else:
        return redirect('index')

def quitarcarrito(request,idp,idu):
    if request.user.id == idu:
        carrito.objects.get(idProducto=idp,idUsuario=idu).delete()
        return redirect('index')
    else:
        return redirect('index')

def iniciarsesion(request):
    user = request.POST['username']
    contra= request.POST['contra']
    user = authenticate(username=user, password=contra)
    if user is not None:
        login(request, user)
        messages.success(request,'Usuario autenticado')
        return redirect('index')
    else:
        messages.success(request,'Usuario o contrasena incorrectos')
        return render(request,'iniciar.html')

def registrar(request):
    nombre = request.POST['registrarUser']
    clave = request.POST['registrarContra']
    correo = request.POST['registrarCorreo']
    
    try:
        user = User.objects.create_user(nombre, correo, clave)
        user.save()
        print('Funciono correctamente')
        return render(request,'iniciar.html')
    except:
        print('Dio un error')
        return render(request,'registro.html')