from django.shortcuts import render, redirect
from servicios.models import Servicio
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login as auth_login
from .forms import customUserCreationForm

# Create your views here.

@login_required
def inicio(request):    
    servicios = Servicio.objects.all()
    return render(request, 'app/inicio.html', {"servicios" : servicios})


def marvel(request):
    servicios = Servicio.objects.filter(categoria = 'marvel_comics')
    return render(request, 'app/marvel.html', {'servicios' : servicios})


def dc(request):
    servicios = Servicio.objects.filter(categoria = 'dc_comics')
    return render(request, 'app/dc.html', {'servicios' : servicios})


def mangas(request):
    servicios = Servicio.objects.filter(categoria = 'mangas')
    return render(request, 'app/mangas.html', {'servicios' : servicios})


def login(request):
    return render(request, 'registration/login.html')


def contacto(request):
    return render(request, 'app/contacto.html')


def registro(request):
    data = {
        'form' : customUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = customUserCreationForm(data=request.POST)
        
        if user_creation_form.is_valid():
            user_creation_form.save()

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
