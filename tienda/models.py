from django.db import models

# Create your models here.
class producto(models.Model):
    idProducto = models.AutoField(primary_key=True,verbose_name="ID autoincrementable del producto")
    nombre = models.CharField(max_length=20, verbose_name="nombre",blank=False,null=False)
    
    def __str__(self):
        return self.nombre