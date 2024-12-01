from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from decimal import Decimal

# Create your models here.
class Producto(models.Model):
    clave = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    telefono = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clientes')

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    clave = models.CharField(max_length=10)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField(default=5)
    lugarEntrega = models.CharField(max_length=50, blank=True, null=True)
    fechaEntrega = models.CharField(max_length=50, blank=True, null=True)
    horaEntrega = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    cuotas = models.IntegerField(default=5)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos')

    def save(self, *args, **kwargs):
        # Verificar que haya suficiente stock
        if self.cantidad > self.producto.stock:
            raise ValueError("No hay suficiente stock para este producto.")
        
        # Calcular el total antes de guardar
        self.total = Decimal(self.cantidad) * self.producto.precio
        
        # Reducir el stock del producto
        self.producto.stock -= self.cantidad
        self.producto.save()

        super().save(*args, **kwargs)

        # Crear un registro de Venta asociado
        Venta.objects.create(
            clave=self.clave,
            importeTotal=self.total,
            cuotas=self.cuotas,
            cuotasRestantes=self.cuotas,
            importePagado=Decimal('0.00'),
            importeRestante=self.total,
            cliente=self.cliente,
            user=self.user
        )

    def __str__(self):
        return f"Pedido {self.clave} - Producto: {self.producto.nombre}"

class Venta(models.Model):
    clave = models.CharField(max_length=10)
    importeTotal = models.DecimalField(max_digits=10, decimal_places=2)
    cuotas = models.IntegerField(default=5)
    cuotasRestantes = models.IntegerField(default=5)
    importePagado = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    importeRestante = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='ventas')

    def save(self, *args, **kwargs):
        # Calcula el importe restante
        self.importeRestante = self.importeRestante - self.importePagado
        
        # Calcula las cuotas restantes
        if self.importePagado > 0:
            self.cuotasRestantes = max(0, self.cuotasRestantes - 1)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venta {self.clave} - Importe Total: ${self.importeTotal}"