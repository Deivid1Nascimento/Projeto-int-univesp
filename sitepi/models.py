from datetime import datetime

from django.db import models

# Create your models here.


class Faculdades (models.Model):



    nome_faculdade = models.CharField(max_length=30)
    curso = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField(max_length=200)
    notaenade = models.DecimalField(max_digits=4, decimal_places=3)
    nota = models.IntegerField()
    modalidade = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    uf = models.CharField(max_length=2)
    datacriacao = models.DateTimeField(default=datetime.now, blank=True)



