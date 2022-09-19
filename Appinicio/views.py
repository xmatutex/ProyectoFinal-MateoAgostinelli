import email
from mailbox import NoSuchMailboxError
from pipes import Template
from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render
from .forms import *
from .models import *



def inicio (request):

    return render(request, "Appinicio/inicio.html")

def acercanuestro (request):

    return render (request,"Appinicio/acercanuestro.html")

def contacto (request):

    return render (request, "Appinicio/contacto.html")




#--Formulario--#

def formulario_usuario(request):

    if request.method=="POST":

        formulario_1=Formulario_usuario(request.POST)
        
        if formulario_1.is_valid():
            
            info=formulario_1.cleaned_data
    
            nombre=info.get("nombre")
            apellido=info.get("apellido")
            email=info.get("email")
            contraseña=info.get("contraseña")
            
            usuario=Usuario(nombre=nombre, apellido=apellido, email=email, contraseña=contraseña)
            usuario.save()
            
            return render (request, "Appinicio/usuario_creado.html", {"mensaje": "usuario creado"})
        else:
            return render (request, "Appinicio/inicio.html", {"mensaje": "Error creando el usuario"})
    
    else:
        formulario_1=Formulario_usuario()
        return render(request, "Appinicio/formulario.html", {"formulario":formulario_1})
        
    return render (request, "Appinicio/formulario.html")



def usuario_creado (request):

    return render (request, "Appinicio/usuario_creado")