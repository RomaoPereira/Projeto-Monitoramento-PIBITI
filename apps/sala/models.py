from django.db import models

class Sala(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=150)
    capacidade = models.PositiveIntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
