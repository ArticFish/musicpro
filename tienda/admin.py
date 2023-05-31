from django.contrib import admin
from .models import producto,carrito,tipopro,categoria,detalleproducto
# Register your models here.
admin.site.register(producto)
admin.site.register(carrito)
admin.site.register(tipopro)
admin.site.register(categoria)
admin.site.register(detalleproducto)

