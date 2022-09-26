from ast import If
import email
from mailbox import NoSuchMailboxError
from pipes import Template

#----Django----#
from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render, redirect
from django.urls.base import reverse

#----Python----#
from .forms import *
from .models import *

#----Login----#
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate



def inicio (request):

    return render(request, "Appinicio/inicio.html")

def acercanuestro (request):

    return render (request,"Appinicio/acercanuestro.html")

def contacto (request):

    return render (request, "Appinicio/contacto.html")


def perfil_usuario (request):

    return render (request, "Appinicio/perfil_usuario.html")

#--Login--#

def login_usuario (request):
    if request.method=="POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.post["username"]
            contraseña=request.post["password"]
            
            usuario=authenticate(username=usu , password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'Appinicio/perfil_usuario', {'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, 'Appinicio/login.html', {"form":form,'mensaje':"Usuario o contrasenia incorrecta"})
        else:
            return render(request, 'Appinicio/login.html', {"form":form,'mensaje':"Formulario invalido"})
    else:
        form= AuthenticationForm()
        return render(request, 'Appinicio/login.html', {'form':form})           
        
    return render (request, "Appinicio/login.html")


#--Registro-#


def registro(request):

      if request.method == 'POST':
            form = UserRegisterForm(data=request.POST)
            if form.is_valid():
                  nuevo_usuario = form.save()
                  login(request, nuevo_usuario)
                  return render(request,'Appinicio/registro.html', {"mensaje": "Haz creado el usuario con exito"})
            else:
                return render(request, 'Appinicio/registro.html', {"form":form, "mensaje": "The user could not be created. Please try again"})
      
      else:      
            form = UserRegisterForm()     
      return render(request, 'Appinicio/registro.html',  {"form":form})


#--Ver/Editar Usuario-#

#--Registro-#

@login_required
def profile(request, user_id):
    
    user = request.user
    # buscamos si el usuario tiene avatar:
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    context = {'user': user, 'avatar': avatar, 'title': 'Profile'}
    return render(request, 'Users/profile.html', context)


@user_passes_test(lambda u: u.is_superuser)   # solo los superusers pueden cambiar el avatar
def editAvatar(request):
    
    user = request.user
    # buscamos si el usuario tiene avatar:
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    if request.method == 'POST':
        form_avatar= AvatarForm(request.POST, request.FILES, instance=user)
        if form_avatar.is_valid():
            u = User.objects.get(username=request.user)
            new_avatar = Avatar(user=u, avatar=form_avatar.cleaned_data['avatar'])
            new_avatar.save()
            return redirect(reverse('users:Profile', args=[id]))
        else:
            return render(request, 'Users/edit_avatar.html', {"form_avatar":form_avatar, "mensaje": "The avatar could not be updated. Please try again"})
    else:
        form_avatar= AvatarForm()
    return render (request, 'Users/edit_avatar.html', {"form_avatar":form_avatar, "avatar":avatar})