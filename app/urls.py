from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('', views.inicio, name="inicio"),
    path('dc/', views.dc, name="DC"),
    path('marvel/', views.marvel, name="Marvel"),
    path('mangas/', views.mangas, name="Mangas"),
    path('contacto/', views.contacto, name="contacto"),
    path('carro/', views.carroCompra, name="carro"),
    path('login/', views.login, name="login"),
    path('registro/', views.registro, name="registro"),
    path('logout/', views.salir, name='salir'),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)