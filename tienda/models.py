from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True,verbose_name="ID autoincrementable de la categoria producto")
    categoria = models.CharField(max_length=20, verbose_name="categoria",blank=False,null=False)
    
    def __str__(self):
        return self.categoria

class tipopro(models.Model):
    idTipopro = models.AutoField(primary_key=True,verbose_name="ID autoincrementable del tipo producto")
    tipo = models.CharField(max_length=20, verbose_name="tipo",blank=False,null=False)

    def __str__(self):
        return self.tipo
    
class detalleproducto(models.Model):
    idDetalle = models.AutoField(primary_key=True,verbose_name="ID autoincrementable del producto")
    marca = models.CharField(max_length=20, verbose_name="marca",blank=False,null=False)
    color = models.IntegerField(verbose_name="Color producto")
    idCategoria = models.ForeignKey(categoria,on_delete=models.CASCADE,default=1)
    idTipopro = models.ForeignKey(tipopro,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.marca

class producto(models.Model):
    idProducto = models.AutoField(primary_key=True,verbose_name="ID autoincrementable del producto")
    nombre = models.CharField(max_length=20, verbose_name="nombre",blank=False,null=False)
    precio = models.IntegerField(verbose_name="Precio producto")
    stock = models.IntegerField(verbose_name="Stock producto")
    descripcion = models.CharField(max_length=500, verbose_name="descripcion",blank=False,null=False)
    idDetalle = models.ForeignKey(detalleproducto,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.nombre

class carrito(models.Model):
    idProducto = models.ForeignKey(producto,on_delete=models.CASCADE,default=1)
    idUsuario = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    cantidad = models.IntegerField(verbose_name="Cantidad productos")
    
    def __str__(self):
        return str(self.idUsuario)