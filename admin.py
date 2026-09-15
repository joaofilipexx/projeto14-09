from django.contrib import admin
from .models import Autor


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'nacionalidade',
        'data_nascimento',
    )

    search_fields = (
        'nome',
        'nacionalidade',
    )

    list_filter = (
        'nacionalidade',
    )
