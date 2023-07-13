from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True,verbose_name="ID autoincrementable de la categoria producto")
    categoria = models.CharField(max_length=50, verbose_name="categoria",blank=False,null=False)
    
    def __str__(self):
        return str(self.idCategoria)


    

class producto(models.Model):
    idProducto = models.AutoField(primary_key=True,verbose_name="ID autoincrementable del producto")
    nombre = models.CharField(max_length=300, verbose_name="nombre",blank=False,null=False)
    precio = models.IntegerField(verbose_name="Precio producto")
    stock = models.IntegerField(verbose_name="Stock producto")
    descripcion = models.CharField(max_length=500, verbose_name="descripcion",blank=False,null=False)
    preciooferta = models.IntegerField(verbose_name="Precio de oferta del producto")
    oferta = models.IntegerField(verbose_name="Porcentaje de oferta del producto")
    marca = models.CharField(max_length=50, verbose_name="marca",blank=False,null=False)
    color = models.CharField(max_length=50, verbose_name="Color",blank=False,null=False)
    foto = models.ImageField(upload_to="estacionamientos",blank=True,null=True)
    idCategoria = models.ForeignKey(categoria,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return str(self.idProducto)
    
class estadoc(models.Model):
    estado = models.AutoField(primary_key=True,verbose_name="ID autoincrementable del estado carrito")
    nombreestado = models.CharField(max_length=300, verbose_name="estado",blank=False,null=False)
    def __str__(self):
        return str(self.nombreestado)

class carrito(models.Model):
    carrito = models.AutoField(primary_key=True,verbose_name="ID  del carrito")
    cantidad = models.IntegerField(verbose_name="Cantidad productos")
    total = models.IntegerField(verbose_name="Total boleta",default=0)
    idProducto = models.ForeignKey(producto,on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idUsuario)
    
class boleta(models.Model):
    boleta = models.AutoField(primary_key=True,verbose_name="ID  del carrito")
    cantidad = models.IntegerField(verbose_name="Cantidad productos")
    precio = models.IntegerField(verbose_name="Precio producto",default=0)
    total = models.IntegerField(verbose_name="Total boleta",null=True,blank=True)
    nro_pedido = models.IntegerField(verbose_name="numero de pedido",default=1)
    direccion = models.CharField(max_length=150, verbose_name="Color",blank=True,null=False)
    idProducto = models.ForeignKey(producto,on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(User,on_delete=models.CASCADE)
    idEstado = models.ForeignKey(estadoc,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return str(self.idUsuario)