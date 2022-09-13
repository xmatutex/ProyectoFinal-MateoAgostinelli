from xml.etree.ElementInclude import include
from django.urls import path
from .views import *



urlpatterns = [
    path('', inicio, name='inicio'),
    path('acercanuestro/', acercanuestro, name='acercanuestro'),
    path('contacto/', contacto, name="contacto"),
    path('formulario/', formulario, name="formulario"),
    path('usuario_creado/', usuario_creado, name='usuario_creado'),

]