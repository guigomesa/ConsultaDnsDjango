from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models
# Create your views here.




def index(request):
    return render(request, 'home.html', {"usuario": "Guigo"})


#@csrf_exempt
def consulta(request):
    if request.method == 'GET':
        return render(request, 'home.html', {"usuario": "Guigo"})

    valor = request.POST['dominio']

    try:
        retorno = models.ConsultaDominio(dominio=valor)
    except Exception:
        return render(request, 'home.html', {"usuario": "Guigo"})

    return render(request, 'resposta-consulta.html', {"valor": valor, "dominio" : retorno})
    pass

