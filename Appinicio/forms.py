from django import forms

class Formulario1(forms.Form):

    usuario=forms.CharField(max_length=50)
    email=forms.EmailField()
    contraseña=forms.CharField(max_length=50)