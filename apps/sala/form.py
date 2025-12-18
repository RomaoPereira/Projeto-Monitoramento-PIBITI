from django import forms
from .models import Sala

class salaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nome', 'localizacao', 'capacidade', 'status']
