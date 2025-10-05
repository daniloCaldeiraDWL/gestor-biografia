from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def lista(request):
    pesquisa = request.GET.get('pesquisa')

    if not pesquisa:
        pessoas = Pessoa.objects.all()
    else:
        pessoas = Pessoa.objects.filter(biografia__contains=pesquisa)
        
    context = {
        'pessoas': pessoas
    }
    return render(request, 'core/lista.html', context=context)