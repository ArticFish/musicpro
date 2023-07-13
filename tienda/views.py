from itertools import chain
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import categoria, estadoc, producto,carrito,boleta
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import math 
from guest_user.decorators import allow_guest_user
from django.contrib.auth.decorators import user_passes_test,login_required

# Create your views here.
@allow_guest_user
def index(request):
    lproductos = producto.objects.all().order_by('idCategoria')
    for m in lproductos:
        if m.oferta !=0:
            m.preciooferta = math.trunc(m.precio - (m.precio*m.oferta/100))
            m.save()
    instrumentocuerda = producto.objects.filter(idCategoria=1)
    percusion = producto.objects.filter(idCategoria=2)
    Amplificadores = producto.objects.filter(idCategoria=3)
    accesorios = producto.objects.filter(idCategoria=4)
    contexto = {"lista":lproductos,"listaic":instrumentocuerda,"listap":percusion,"listaa":Amplificadores,"listaacc":accesorios}
    return render(request,'index.html',contexto)


@user_passes_test(lambda u: u.is_authenticated,login_url='iniciar')
def carritocompra(request,idu):
    if request.user.id == idu:
        lproductos = carrito.objects.filter(idUsuario=idu)
        totalusd = 0
        totalclp = 0
        for i in lproductos.values_list('idProducto_id','cantidad'):
            id = i[0]
            totalp = producto.objects.get(idProducto=id)
            if totalp.preciooferta == 0:
                totalc = (totalp.precio * i[1])
            else:
                totalc = (math.trunc(totalp.precio - (totalp.precio*totalp.oferta/100)) * i[1])
            totalclp = totalc + totalclp
            totalusd = math.trunc(totalclp/800)
        print(totalclp)
        print(totalusd)
        contexto = {"lista":lproductos,"listat":totalclp,"listad":totalusd}
        return render(request,'carritocompra.html',contexto)
    else:
        return redirect('index')

@user_passes_test(lambda u: u.is_authenticated,login_url='iniciar')
def pedidos(request,idu):
    if request.user.id == idu:
        lproductos = boleta.objects.filter(idUsuario=idu).order_by('nro_pedido','boleta')
        lpedidos = lproductos.values_list('nro_pedido',flat=True).order_by('nro_pedido').distinct()
        contexto = {"lista":lproductos,"listac":lpedidos}
        return render(request,'pedido.html',contexto)
    else:
        return redirect('index')

def bodega(request):
    if request.user.username == 'Bodeguero':
        lproductos = boleta.objects.filter(idEstado=2).order_by('nro_pedido','boleta')
        lpedidos = lproductos.values_list('nro_pedido','idEstado').order_by('nro_pedido').distinct()
        contexto = {"lista":lproductos,"listac":lpedidos}
        return render(request,'bodega.html',contexto)
    elif request.user.username == 'Contador':
        lproductos = boleta.objects.filter(idEstado=1).order_by('nro_pedido','boleta')
        lpedidos = lproductos.values_list('nro_pedido','idEstado').order_by('nro_pedido').distinct()
        contexto = {"lista":lproductos,"listac":lpedidos}
        return render(request,'bodega.html',contexto)

def enviar(request,idb):
    if request.user.username == 'Bodeguero':
        lproductos = boleta.objects.filter(nro_pedido=idb).order_by('nro_pedido','boleta')
        cuenta = estadoc.objects.get(estado=3)
        tip = estadoc
        tip.estado = cuenta
        for p in lproductos:
            print(p.nro_pedido)
            p.idEstado = cuenta
            p.save()
    return redirect('bodega')

def confirmarpago(request,idb):
    if request.user.username == 'Contador':
        lproductos = boleta.objects.filter(nro_pedido=idb).order_by('nro_pedido','boleta')
        cuenta = estadoc.objects.get(estado=2)
        tip = estadoc
        tip.estado = cuenta
        for p in lproductos:
            print(p.nro_pedido)
            p.idEstado = cuenta
            p.save()
    return redirect('bodega')

def registro(request):
    return render(request,'registro.html')

def pagoproducto(request):
    pag = request.META.get('HTTP_REFERER')
    contexto = {"lista":pag}
    return render(request,'pago.html',contexto)

def pagar(request,idu):
    if request.user.id == idu:
        usuario = User
        usuario.id = User.objects.get(id=request.user.id)
        carro = carrito.objects.filter(idUsuario=usuario.id)
        npedido = 0
        try:
            totalc = sum(carro.values_list('total',flat=True))
            pedido = boleta.objects.all().latest('nro_pedido')
            npedido = (pedido.nro_pedido + 1)
        except:
            npedido =  1
        for c in carro:
            boleta.objects.create(idProducto=c.idProducto,idUsuario=usuario.id,cantidad=c.cantidad,nro_pedido=npedido,precio=c.total)
        pedido = boleta.objects.filter(idUsuario=usuario.id).latest('boleta')
        pedido.total = totalc
        pedido.save()
        productosc = boleta.objects.filter(nro_pedido=npedido)
        for p in productosc:
            stockproductos = producto.objects.get(idProducto=p.idProducto.idProducto)
            stockproductos.stock = stockproductos.stock - p.cantidad
            stockproductos.save()
        carro.delete()
    return redirect('pagoproducto')
    
def eproducto(request,idp):
    nombree = request.POST['nombre']
    prec = request.POST['precio']
    stock = request.POST['quantity']
    desc = request.POST['descripcion']
    marc = request.POST['marca']
    colo = request.POST['color']
    fotoe = request.FILES['subir']
    pro=producto.objects.get(idProducto=idp)
    pro.nombre = nombree
    pro.precio = prec
    pro.stock = stock
    pro.descripcion = desc
    pro.marca = marc
    pro.color = colo
    pro.foto = fotoe
    pro.save()
    return redirect('index')

def iniciar(request):
    return render(request,'iniciar.html')

def crproducto(request):
    nombree = request.POST['nombre']
    prec = request.POST['precio']
    stock = request.POST['quantity']
    desc = request.POST['descripcion']
    marc = request.POST['marca']
    colo = request.POST['color']
    fotoe = request.FILES['subir']
    c = request.POST['registrarRol']
    cat = categoria.objects.get(idCategoria=c)
    pro = producto.objects.create(nombre=nombree,precio=prec,stock=stock,descripcion=desc,preciooferta=0,oferta=0,marca=marc,color=colo,foto=fotoe,idCategoria=cat)
    pro.save()
    return redirect('index')

def cproducto(request):
    return render(request,'crearproducto.html')

def pproducto(request,idp):
    lproductos = producto.objects.get(idProducto=idp)
    #ofertas = math.trunc(lproductos.precio - (lproductos.precio*lproductos.oferta/100))
    if lproductos.oferta != 0:
        lproductos.preciooferta = math.trunc(lproductos.precio - (lproductos.precio*lproductos.oferta/100))
    contexto = {"lista":lproductos}
    return render(request,'pproducto.html',contexto)

def pproductoe(request,idp):
    lproductos = producto.objects.get(idProducto=idp)
    #ofertas = math.trunc(lproductos.precio - (lproductos.precio*lproductos.oferta/100))
    if lproductos.oferta != 0:
        lproductos.preciooferta = math.trunc(lproductos.precio - (lproductos.precio*lproductos.oferta/100))
    contexto = {"lista":lproductos}
    return render(request,'pproductoe.html',contexto)

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
            carro.total = carro.total + (stock.precio*int(cantidadproducto))
            carro.save()
        except:
            carrito.objects.create(idProducto=pro.idProducto,idUsuario=usuario.id,cantidad=cantidadproducto,total=(stock.precio*int(cantidadproducto)))
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