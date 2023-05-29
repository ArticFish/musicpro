from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class producto(models.Model):
    idProducto = models.AutoField(primary_key=True,verbose_name="ID autoincrementable del producto")
    nombre = models.CharField(max_length=20, verbose_name="nombre",blank=False,null=False)
    
    def __str__(self):
        return self.nombre
    
class carrito(models.Model):
    idProducto = models.ForeignKey(producto,on_delete=models.CASCADE,default=1)
    idUsuario = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return str(self.idUsuario)