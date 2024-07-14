from django.shortcuts import render, redirect  # Añadir redirect
from servicios.models import Servicio
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login as auth_login
from .forms import customUserCreationForm

# Create your views here.

@login_required
def inicio(request):    
    servicios = Servicio.objects.all()
    return render(request, 'app/inicio.html', {"servicios" : servicios})


def contacto(request):
    return render(request, 'app/contacto.html')


def login(request):
    return render(request, 'registration/login.html')


def registro(request):
    data = {
        'form' : customUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = customUserCreationForm(data=request.POST)
        
        if user_creation_form.is_valid():
            user_creation_form.save()

            # Aquí aseguramos que estamos autenticando correctamente al usuario
            username = user_creation_form.cleaned_data['username']
            password = user_creation_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('inicio')

    return render(request, 'registration/registro.html', data)


def carroCompra(request):
    return render(request, 'app/carroDeCompras.html')


def salir(request):  
    logout(request)
    return redirect('login')
