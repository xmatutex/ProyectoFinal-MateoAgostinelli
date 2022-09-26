from xml.etree.ElementInclude import include
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', inicio, name='inicio'),
    path('acercanuestro/', acercanuestro, name='acercanuestro'),
    path('contacto/', contacto, name="contacto"),
    path('logout/', LogoutView.as_view(template_name='Appinicio/logout.html'), name='logout'),
    path('registro/', registro, name='registro'),
    path('login/', login_usuario, name='login'),
    path('perfil_usuario/', perfil_usuario, name='login'),

]