
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):

    nombre=models.CharField(max_length=50, )
    apellido=models.CharField(max_length=50,)
    email=models.EmailField()
    contraseña=models.CharField(max_length=50)
    

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"
    
    
class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)  

    def __str__(self):
        return f"Profile image from user: {self.user.username}"
    
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', null=True, blank = True)
    content =models.CharField(max_length=400,)


    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

#---------Mensajeria--------------#

class Messages(models.Model):
    
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    msg = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return f"{self.msg[:50]}[...]"