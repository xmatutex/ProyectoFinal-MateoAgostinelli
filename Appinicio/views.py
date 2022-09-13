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

def formulario (request):

    if request.method == "POST":

        formulario_1=Formulario1(request.POST)
        
        usuario=request.POST.get("usuario")
        
        if formulario_1.is_valid:
            
            informacion= formulario_1.cleaned_data
            
            usuario= Usuario(usuario=informacion[""])
            
            usuario.save()
            
            return render (request, "Appinicio/inicio.html")
        
    return render (request, "Appinicio/formulario.html")

def usuario_creado (request):

    return render (request, "Appinicio/usuario_creado")