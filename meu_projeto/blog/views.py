# blog/views.py
from django.shortcuts import render
from .models import Post

from django.shortcuts import render
from django.http import JsonResponse
import json

dados_mocados = [
    {
        "id": "6",
        "nome": "FÊNIX GOV AC",
        "convenios": [{"id": 24, "estado": "ACRE", "descricao": "NÃO EXISTE"}]
    },
    {
        "id": "9",
        "nome": "PORTO VELHO",
        "convenios": [{"id": 25, "estado": "PORTO VELHO", "descricao": "NÃO EXISTE"}]
    },
    {
        "id": "1",
        "nome": "ConsignetUM2",
        "convenios": [
            {"id": 1, "estado": "CIANORTE", "descricao": "CIANORTE / 40132 - SANTANDER"},
            {"id": 2, "estado": "CAMPINA GRANDE DO SUL", "descricao": "CAMPINA GRANDE DO SUL / 39829 - SANTANDER"},
        ]
    },
    {
        "id": "2",
        "nome": "CONSIGLOG GOV AM",
        "convenios": [{"id": 14, "estado": "AMAZONAS", "descricao": "NÃO EXISTE"}]
    },
]

def home(request):
    return render(request, 'blog/home.html', {'locais': dados_mocados})

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/lista_posts.html', {'posts': posts})


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_convenios(request):
    if request.method == 'POST':
        selected_local_id = request.POST.get('selected_local')
    else:
        selected_local_id = request.GET.get('selected_local')  # Use GET para testes

    localidade = next((local for local in dados_mocados if local['id'] == selected_local_id), None)

    if localidade:
        convenios = localidade.get('convenios', [])
        return JsonResponse(convenios, safe=False)
    else:
        return JsonResponse([], safe=False)