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
    "convenios": [
      {
        "id": 24,
        "estado": "ACRE",
        "descricao": "NÃO EXISTE"
      }
    ]
  },
  {
    "id": "9",
    "nome": "PORTO VELHO",
    "convenios": [
      {
        "id": 25,
        "estado": "PORTO VELHO",
        "descricao": "NÃO EXISTE"
      }
    ]
  },
  {
    "id": "1",
    "nome": "ConsignetUM2",
    "convenios": [
      {
        "id": 1,
        "estado": "CIANORTE",
        "descricao": "CIANORTE / 40132 - SANTANDER"
      },
      {
        "id": 2,
        "estado": "CAMPINA GRANDE DO SUL",
        "descricao": "CAMPINA GRANDE DO SUL / 39829 - SANTANDER"
      },
      {
        "id": 3,
        "estado": "CAMPINA GRANDE DO SUL",
        "descricao": "CAMPINA GRANDE DO SUL / 39829 - SANTANDER"
      },
      {
        "id": 4,
        "estado": "CAMPINA GRANDE DO SUL",
        "descricao": "CAMPINA GRANDE DO SUL / 39829 - SANTANDER"
      },
      {
        "id": 5,
        "estado": "CAMPINA GRANDE DO SUL",
        "descricao": "CAMPINA GRANDE DO SUL / 39829 - SANTANDER"
      },
      {
        "id": 6,
        "estado": "CAMPINA GRANDE DO SUL",
        "descricao": "CAMPINA GRANDE DO SUL / 39829 - SANTANDER"
      },
      {
        "id": 7,
        "estado": "CAMPINA GRANDE DO SUL",
        "descricao": "CAMPINA GRANDE DO SUL / 39829 - SANTANDER"
      },
      {
        "id": 8,
        "estado": "CAMPINA GRANDE DO SUL",
        "descricao": "CAMPINA GRANDE DO SUL / 39829 - SANTANDER"
      },
      {
        "id": 9,
        "estado": "JI-PARANA",
        "descricao": "JI-PARANA / 40904 - SANTANDER"
      },
      {
        "id": 10,
        "estado": "PREF. CACOAL",
        "descricao": "PREF. CACOAL / SANTANDER"
      },
      {
        "id": 11,
        "estado": "ARIQUEMES",
        "descricao": "ARIQUEMES / SANTANDER"
      },
      {
        "id": 12,
        "estado": "ARIQUEMES",
        "descricao": "ARIQUEMES / SANTANDER"
      },
      {
        "id": 13,
        "estado": "BALNEÁRIO CAMBORIÚ",
        "descricao": "BALNEÁRIO CAMBORIÚ / SANTANDER"
      },
      {
        "id": 15,
        "estado": "IMBITUBA",
        "descricao": "IMBITUBA / SANTANDER"
      },
      {
        "id": 16,
        "estado": "UMUARAMA",
        "descricao": "UMUARAMA / 39819 / 39823 / 40818 / 40819 / 40820 - SANTANDER"
      },
      {
        "id": 17,
        "estado": "PREF. VILHENA - RO",
        "descricao": "PREF. VILHENA - RO / SANTANDER"
      },
      {
        "id": 18,
        "estado": "PREF. PIMENTA BUENO",
        "descricao": "PREF. PIMENTA BUENO / 42252 - SANTANDER"
      },
      {
        "id": 19,
        "estado": "ROLIM DE MOURA",
        "descricao": "ROLIM DE MOURA / SANTANDER"
      },
      {
        "id": 20,
        "estado": "GOVERNO DE RONDONIA",
        "descricao": ""
      },
      {
        "id": 21,
        "estado": "GOVERNO DE RONDONIA",
        "descricao": ""
      }
    ]
  },
  {
    "id": "2",
    "nome": "CONSIGLOG GOV AM",
    "convenios": [
      {
        "id": 14,
        "estado": "AMAZONAS",
        "descricao": "NÃO EXISTE"
      },
      {
        "id": 26,
        "estado": "AMAZONAS",
        "descricao": "NÃO EXISTE"
      }
    ]
  },
  {
    "id": "7",
    "nome": "CECON GOV RO",
    "convenios": [
      {
        "id": 27,
        "estado": "cecon",
        "descricao": "2 - cecon"
      }
    ]
  }
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
        selected_local_id = request.GET.get('selected_local')

    localidade = next((local for local in dados_mocados if local['id'] == selected_local_id), None)

    if localidade:
        convenios = localidade.get('convenios', [])
        return JsonResponse(convenios, safe=False)
    else:
        return JsonResponse([], safe=False)