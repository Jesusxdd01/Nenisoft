from django.contrib import admin
from administrador.models import Cliente,Venta,Pedido,Producto

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Producto)
admin.site.register(Pedido)