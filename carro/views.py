from django.shortcuts import redirect
from django.contrib import messages
from .carro import Carro
from servicios.models import Servicio

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Servicio.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("inicio")

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Servicio.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("inicio")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Servicio.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("inicio")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar()
    return redirect("inicio")

def finalizar_compra(request):
    if request.method == 'POST':
        carro = Carro(request)

        compra = carro.comprar(usuario=request.user)

        if compra:
            messages.success(request, "Compra realizada.")
            return redirect('inicio')
        else:
            messages.error(request, "No hay productos en el carro.")
            return redirect('inicio')  

    return redirect('inicio') 