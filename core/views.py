from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def lista(request):
    pesquisa = request.GET.get('pesquisa')

    # Se houver uma pesquisa, filtra as biografias que contém o termo pesquisado, senão, retorna todas as biografias
    if pesquisa:
        pessoas = Pessoa.objects.filter(biografia__contains=pesquisa)
    else:
        pessoas = Pessoa.objects.all()
        
    context = {
        'pessoas': pessoas
    }
    
    return render(request, 'core/lista.html', context=context)