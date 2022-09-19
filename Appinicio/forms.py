from django import forms

class Formulario_usuario(forms.Form):

    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    contraseña=forms.CharField()