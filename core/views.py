from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def lista(request):
    pessoas = Pessoa.objects.all()
    context = {
        'pessoas': pessoas
    }
    return render(request, 'core/lista.html', context=context)