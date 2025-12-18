from django import forms
from .models import Relatorio

class RelatorioForm(forms.ModelForm):
    class Meta:
        model = Relatorio
        fields = ['tipo', 'sala', 'usuario', 'conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descreva os detalhes do relatório...'}),
        }