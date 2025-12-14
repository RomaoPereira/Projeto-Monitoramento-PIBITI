from django.db import models
from apps.sala.models import Sala
from apps.usuarios.models import Usuario

class Relatorio(models.Model):
    TIPO_CHOICES = (
        ('ocupacao', 'Ocupação'),
        ('ociosidade', 'Ociosidade'),
    )

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    data = models.DateField(auto_now_add=True)
    conteudo = models.TextField()

    sala = models.ForeignKey(
        Sala,
        on_delete=models.CASCADE,
        related_name='relatorios'
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='relatorios'
    )

    def __str__(self):
        return f"Relatório {self.tipo} - {self.sala.nome}"
