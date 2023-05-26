from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def registro(request):
    return render(request,'registro.html')

def iniciar(request):
    return render(request,'iniciar.html')

def producto(request):
    return render(request,'plantillaProducto.html')
    
def cerrarsesion(request):
    logout(request)
    return render(request,'index.html')

def iniciarsesion(request):
    user = request.POST['username']
    contra= request.POST['contra']
    user = authenticate(username=user, password=contra)
    if user is not None:
        login(request, user)
        messages.success(request,'Usuario autenticado')
        return render(request,'index.html')
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