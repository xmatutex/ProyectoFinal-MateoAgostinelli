from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)