from django.contrib import admin
from .models import *

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_criacao', 'data_modificacao') # Define os campos a serem exibidos na lista
    search_fields = ('nome',) #  Adiciona uma barra de pesquisa para o campo 'nome'

# Register your models here.
admin.site.register(Pessoa, PessoaAdmin)