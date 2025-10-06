from django.db import models
from datetime import date

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    biografia = models.TextField()
    url_foto = models.URLField(max_length=1000)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    data_nascimento = models.DateField()
    data_falecimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
    # Property para calcular a idade. 
    # A propriedade idade usa @property para ser acessada como um atributo
    @property
    def idade(self):
        """Calcula a idade com base em data_nascimento e data_falecimento (ou hoje)."""
        end_date = self.data_falecimento if self.data_falecimento else date.today()
        idade = end_date.year - self.data_nascimento.year
        # Ajusta a idade se o aniversário ainda não ocorreu no ano atual
        if end_date.month < self.data_nascimento.month or (
            end_date.month == self.data_nascimento.month and end_date.day < self.data_nascimento.day
        ):
            idade -= 1
        return idade
    
    @property
    def obito(self):
        """Retorna vazio se a pessoa está viva, ou uma cruz, concatenada com a data de falecimento se não estiver."""
        if self.data_falecimento:
            return f'(✟ {self.data_falecimento})'
        return ''