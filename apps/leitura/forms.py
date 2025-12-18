from django import forms
from .models import Leitura

class LeituraForms(forms.ModelForm):
    class Meta:
        model = Leitura
        fields = ['sala', 'presenca', 'temperatura', 'porta']
