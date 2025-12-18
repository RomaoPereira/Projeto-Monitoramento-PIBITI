from django import forms
from django.contrib.auth.models import User
from .models import Usuario

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Senha")
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class UsuarioExtraForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['matricula']