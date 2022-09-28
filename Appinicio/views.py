from ast import If
import email
from mailbox import NoSuchMailboxError
from multiprocessing import context
from pipes import Template

#----Django----#
from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView

#----Python----#
from .forms import *
from .models import *

#----Login----#
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.db.models import Q



def inicio (request):
    #buscamos si el usuario tiene avatar:
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''
    
    posts = Post.objects.all().order_by('-date') [0:3]
    return render (request, 'Appinicio/inicio.html', {'avatar':avatar, 'posts': posts})




def acercanuestro (request):

    return render (request,"Appinicio/acercanuestro.html")

def contacto (request):

    return render (request, "Appinicio/contacto.html")


def perfil_usuario (request):

    return render (request, "Appinicio/perfil_usuario.html")

#--Login--#

def login_usuario (request):
    if request.method=="POST":
        form= AuthenticationForm(request=request , data = request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            contraseña=form.cleaned_data.get("password")
            
            usuario=authenticate(username=usu , password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'Appinicio/perfil_usuario.html', {'mensaje':f"Bienvenido {usuario}"})
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
                  usuario = form.save()
                  login(request, usuario)
                  return render(request,'Appinicio/registro.html', {"mensaje": "Haz creado el usuario con exito"})
            else:
                return render(request, 'Appinicio/registro.html', {"form":form, "mensaje": "El usuario no ha sido creado, probar nuevamente"})
      
      else:      
            form = UserRegisterForm()     
      return render(request, 'Appinicio/registro.html',  {"form":form})


#--Editar Usuario-#

@login_required
def perfil_editar(request):

    usuario = request.user
  #try:
      #avatar = Avatar.objects.get(user=request.user.id)
      #avatar = avatar.avatar.url
  #except:
      #avatar = ''
 
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=usuario) 
        if form.is_valid():
            info = form.cleaned_data
              #Datos que se modificarán
            usuario.email = info['email']
            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']
            usuario.password1 = info['password1']
            usuario.password2 = info['password1']
            usuario.save()
            return render(request, 'Appinicio/perfil_usuario.html',{'mensaje':f"Perfil de {usuario} editado"})
        else:
            return render(request, 'Appinicio/perfil_editar.html', {"form":form, "mensaje": "The user could not be updated. Please try again"})
    else: 
        form= UserEditForm(initial={'email':usuario.email, 'first_name':usuario.first_name, 'last_name':usuario.last_name}) #Creo el formulario con los datos que voy a modificar
    return render(request, 'Appinicio/perfil_editar.html', {"form":form, "usuario":usuario})  #Voy al html que me permite editar
    
#--Ver/Editar Usuario-#
@login_required
def profile(request, user_id):
    
    user = request.user
     #buscamos si el usuario tiene avatar:
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
         avatar = ''

    context = {'user': user, 'avatar': avatar, 'title': 'Profile'}
    return render(request, 'Appinicio/perfil_usuario.html', context)


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


#-------------------View Posts--------------------------------------------------

def posts(request):

    posts = Post.objects.all()
    
    contexto= {"posts":posts}
   
    return render(request, "Appinicio/posts.html", contexto)

#-------------------Clases basadas en vistas -------------------------------------------------

class Post_detalles(DetailView):
    model = Post
    template_name = 'Appinicio/post_detalles.html'

#------------nueva funcion para mi form que permite agregar Posts-------------------

@login_required
def posts_crear(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            info = form.cleaned_data
            post = Post(title=info['title'], subtitle=info['subtitle'], author=info['author'],image=info['image'], content=info['content'])
            post.save()
            return render (request , 'Appinicio/posts.html', {'mensaje':"Post creado con exito"})
    else:
        form = PostForm()
        
    return render(request, 'Appinicio/posts_crear.html', {"form":form})

#---------------------------Editar post---------------------------------------

@login_required
def post_editar(request, post_id):

    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES ,instance=post)
        if form.is_valid():
            form.save()
            return redirect('Appinicio/posts.html')
    else:
        form = PostForm(instance=post)
    return render(request, 'Appinicio/posts_editar.html',{'form':form, 'title':post.title})


#--------------------------Messages (Inbox and send new msg)--------------------------------------------

@login_required
def mensajes_inbox(request):
    
    user = request.user
    
    messages = Messages.objects.filter(Q(receiver=user) | Q(sender=user)).order_by('-sent_at')
    received = messages.filter(receiver=user).order_by('-sent_at')
    sent = messages.filter(sender=user).order_by('-sent_at')

    context = {'title': 'Inbox', 'user': user, 'messages': messages, 'received': received, 'sent':sent}
    return render(request, 'Appinicio/mensajes_inbox.html', context)


@login_required
def mensaje_nuevo(request):
    
    if request.method != 'POST':
        form = MessageForm()
    else:
        # Data submitted > form con datos ingresados por POST
        form = MessageForm(data=request.POST)
        if form.is_valid():

            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            return render (request, 'Appinicio/mensajes_inbox.html', {'mensaje':"El mensaje se envio con exito"})
    
    context = {'form': form,'title': 'New message'}
    return render(request, 'Appinicio/mensaje_nuevo_inbox.html', context)

