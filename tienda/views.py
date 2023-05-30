from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import producto,carrito
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from guest_user.decorators import allow_guest_user
from django.contrib.auth.decorators import user_passes_test,login_required

# Create your views here.
@allow_guest_user
def index(request):
    lproductos = producto.objects.all()
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


def iniciar(request):
    return render(request,'iniciar.html')

def pproducto(request,idp):
    lproductos = producto.objects.get(idProducto=idp)
    contexto = {"lista":lproductos}
    return render(request,'pproducto.html',contexto)

@user_passes_test(lambda u: u.is_authenticated,login_url='index')
def cerrarsesion(request):
    logout(request)
    return redirect('index')


def agregarcarrito(request,idp,idu):
    pro = producto
    usuario = User
    pro.idProducto = producto.objects.get(idProducto=idp)
    usuario.id = User.objects.get(id=idu)
    carrito.objects.create(idProducto=pro.idProducto,idUsuario=usuario.id)
    return render(request,'index.html')

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
        return render(request,'prueba.html')

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