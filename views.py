from django.http import JsonResponse
from .models import Autor


def listar_autores(request):
    autores = Autor.objects.all()

    dados = []

    for autor in autores:
        dados.append({
            'id': autor.id,
            'nome': autor.nome,
            'nacionalidade': autor.nacionalidade,
            'data_nascimento': autor.data_nascimento,
        })

    return JsonResponse(dados, safe=False)
