from servicios.models import Servicio
from .models import Compra, DetalleCompra

class Carro:

    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if carro is None:
            self.carro = self.session["carro"] = {}
        else:
            self.carro = carro

    def agregar(self, producto):
        producto_id = str(producto.id)
        if producto_id not in self.carro:
            self.carro[producto_id] = {
                "producto_id": producto.id,
                "titulo": producto.titulo, 
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            self.carro[producto_id]["cantidad"] += 1
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.guardar_carro()

    def restar_producto(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            self.carro[producto_id]["cantidad"] -= 1
            if self.carro[producto_id]["cantidad"] < 1:
                self.eliminar(producto)
            else:
                self.guardar_carro()

    def limpiar(self):
        self.session["carro"] = {}
        self.session.modified = True

    def comprar(self, usuario):
        if not self.carro:
            return None

        compra = Compra(usuario = usuario)
        compra.save()

        for key, value in self.carro.items():
            producto_id = value['producto_id']
            cantidad = value['cantidad']
            precio = value['precio']
            producto = Servicio.objects.get(id=producto_id)
            DetalleCompra.objects.create(
                compra=compra,
                producto=producto,
                cantidad=cantidad,
                precio=precio
            )

        self.limpiar()
        return compra