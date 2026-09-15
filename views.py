from django.http import JsonResponse
from .models import Livro


def listar_livros(request):
    livros = Livro.objects.all()

    dados = []

    for livro in livros:
        dados.append({
            'id': livro.id,
            'titulo': livro.titulo,
            'isbn': livro.isbn,
            'ano_publicacao': livro.ano_publicacao,
            'quantidade_paginas': livro.quantidade_paginas,
            'disponivel': livro.disponivel,
            'autor': livro.autor.nome,
            'categoria': livro.categoria.nome,
        })

    resposta = {
        'total': len(dados),
        'livros': dados
    }

    return JsonResponse(resposta)

