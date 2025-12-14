from django.db import models
from apps.sala.models import Sala

class Leitura(models.Model):
    sala = models.ForeignKey(
        Sala,
        on_delete=models.CASCADE,
        related_name='leituras'
    )
    presenca = models.BooleanField()
    temperatura = models.FloatField()
    porta = models.BooleanField()
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Leitura - {self.sala.nome} - {self.data_hora}"
