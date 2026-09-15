from django.contrib import admin
from .models import Livro


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'autor',
        'categoria',
        'isbn',
        'ano_publicacao',
        'quantidade_paginas',
        'disponivel',
    )

    list_filter = (
        'disponivel',
        'categoria',
        'ano_publicacao',
    )

    search_fields = (
        'titulo',
        'isbn',
        'autor__nome',
    )

