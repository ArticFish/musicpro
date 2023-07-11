from django.contrib import admin
from .models import producto,carrito,categoria,estadoc,boleta
# Register your models here.
admin.site.register(producto)
admin.site.register(carrito)
admin.site.register(categoria)
admin.site.register(estadoc)
admin.site.register(boleta)
