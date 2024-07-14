from django.db import models
from django.contrib.auth.models import User
from servicios.models import Servicio


# Create your models here.

class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Compra {self.id} - {self.usuario.username}'

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Detalle {self.id} - Compra {self.compra.id}'

