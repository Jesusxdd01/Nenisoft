from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Cliente(models.Model):
    # Atributos
    nombre = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    telefono = models.CharField(max_length=10)

    # Métodos
    def __str__(self):
        return "{0}".format(self.nombre)

class Producto(models.Model):
    # Atributos
    clave = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    # Métodos
    def __str__(self):
        return "{0}".format(self.nombre)

class Venta(models.Model):
    # Atributos
    clave = models.CharField(max_length=10)
    importeTotal = models.DecimalField(max_digits=10, decimal_places=2)
    cuotas = models.IntegerField(default=5)
    cuotasRestantes = models.IntegerField(default=5)
    importePagado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    importeRestante = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)

    # Métodos
    def save(self, *args, **kwargs):
        self.importeRestante = self.importeTotal - self.importePagado
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venta {self.clave} - Importe Total: ${self.importeTotal}"

class Pedido(models.Model):
    # Atributos
    clave = models.CharField(max_length=10)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField(default=5)
    lugarEntrega = models.CharField(max_length=50, blank=True, null=True)
    fechaEntrega = models.CharField(max_length=50, blank=True, null=True)
    horaEntrega = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        # Verificar que haya suficiente stock
        if self.cantidad > self.producto.stock:
            raise ValueError("No hay suficiente stock para este producto.")
        
        # Calcular el total antes de guardar
        self.total = self.cantidad * self.producto.precio
        
        # Reducir el stock del producto
        self.producto.stock -= self.cantidad
        self.producto.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido {self.clave} - Producto: {self.producto.nombre}"