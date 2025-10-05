from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def lista(request):
    return render(request, 'core/lista.html')