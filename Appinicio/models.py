from django.db import models

# Create your models here.

class Usuario(models.Model):

    nombre=models.CharField(max_length=50, )
    apellido=models.CharField(max_length=50,)
    email=models.EmailField()
    contraseña=models.CharField(max_length=50)