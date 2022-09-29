from re import template
from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, logout_then_login



urlpatterns = [
    path('', inicio, name='inicio'),
    path('logout/', LogoutView.as_view(template_name='Appinicio/logout.html'), name='logout'),
    path('registro/', registro, name='registro'),
    path('login/', login_usuario, name='login'),
    
    path('perfil_usuario/', perfil_usuario, name='perfil_usuario'),
    path('perfil_editar/', perfil_editar, name='perfil_editar'),
    path('about/', about, name='about'),
    
    path('posts/', posts, name='posts'),
    path('posts_crear/', posts_crear, name='posts_crear'),
    path('post/<pk>', Post_detalles.as_view(), name='Post_detalles'),
    path('post/delete/<pk>', PostDelete.as_view(), name='PostDelete'),
    path('post/editar/<post_id>/', post_editar, name='post_editar'),
    
    path('mensajes_inbox/', mensajes_inbox, name='mensajes_inbox'),
    path('inbox/mensaje_nuevo/', mensaje_nuevo, name='mensaje_nuevo_inbox'),
    

]