from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        help_texts = {k:"" for k in fields}
        
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False) 
    password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','first_name','last_name','password1', 'password2']
        help_texts = {k:"" for k in fields}
        
    

class AvatarForm(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['avatar']
        
#-------------------Form post---------------------------------#      

class PostForm(forms.ModelForm):
    content = forms.CharField()
    class Meta:
        model = Post
        fields = ("title", "subtitle", "author", "image", "content")
        
        
        
#-------------------Mensajeria---------------------------------#       
class MessageForm(forms.ModelForm):
    
    
    class Meta:
        model = Messages
        fields = ['receiver','msg',]
        widgets = {'msg': forms.Textarea(attrs={'cols': 80})}