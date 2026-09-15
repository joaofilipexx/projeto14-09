from django.db import models
from django.core.validators import MinValueValidator

from autores.models import Autor
from categorias.models import Categoria


class Livro(models.Model):
    titulo = models.CharField(max_length=150)

    isbn = models.CharField(
        max_length=20,
        unique=True
    )

    ano_publicacao = models.IntegerField(
        validators=[MinValueValidator(0)]
    )

    quantidade_paginas = models.IntegerField(
        validators=[MinValueValidator(1)]
    )

    disponivel = models.BooleanField(default=True)

    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name='livros'
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='livros'
    )

    def __str__(self):
        return self.titulo

