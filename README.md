# Instruções
Desenvolvedor: Danilo Martins Caldeira.

# Sobre o projeto:
Curso feito pegando as aulas de um cruso gratuíto da Udemy:
- https://www.udemy.com/course/aprenda-o-framework-django-em-um-projeto-na-pratica/

## Ambiente virtual: 
Versão Python: 3.10.10

Os comandos a seguir podem ser execudados:
1. Criar: ```python -m venv venv```
2. Ativar: ```.\venv\Scripts\activate```
3. Instalar o que é preciso: ```pip install -r requirements.txt```
4. Para gerar o arquivo requirements.txt de forma automática: ```pip freeze > requirements.txt```
1. Desativar: ```deactivate```

## Notas do Django:
A documentação do Djando é disponibilizada em: https://docs.djangoproject.com/pt-br/5.2/

Anotações:

- Instalação: ```pip install djang```
- Conferir se está instalado: ```django-admin --version```
- Criar um projeto Django: ```django-admin startproject nome_do_projeto .```
  Ao iniciar um projeto temos alguns arquivos criados de forma automática. 
    - __init__.py: define a pasta como um pacote python.
    - settings.py: é o coração da aplicação django. Ele é um arquivo de configuração do Django. 
    - urls.py: onde são confirado as rotas. 
    - manage.py: arquivo que ficará na raiz do projeto, permitindo interagir de várias formas com o Django. 

- Executar o servidor: ```python manage.py runserver```. Caso tudo esteja certo, já temos o sistema disponível, com o link rodando. 
- Para finalizar: ```Ctrl + c```
- Criação do app Django: ```python manage.py startapp nome_do_app```. Sempre que eu inserir um app eu tenho que defini-lo no arquivo settings em INSTALLED_APPS. 
- Para criar as tabelas do banco de dados, eu tenho que definir tudo em models.py na pasta de aplicativo.
- Após realizar inclusões ou alterações, eu tenho que executar o comando para migrar as novas alterações: ```python manage.py migrate```
- Logo após: ```python manage.py makemigrations```
- Para assim, aplicarmos a migração novamente: ```python manage.py migrate``` 
- Preciso necessariamente, criar o super-usuario para o sistema: ```python manage.py createsuperuser```

Podemos, agora acessar o serviço com o link gerado. Entre muitas funcoes. 

### Painel administrador
- Com a aplicação rodando, podemos acessar o painel administrador: http://127.0.0.1:8000/admin/
- Caso não haja, temso que criar um super-usuário: ```python manage.py createsuperuser```

## Rotinas de trabalho com Branch isoladas de desenvolvimento
- Criar uma branch: ```git checkout -b brach/minha-nova-branch```
    - Fazer as alterações necessárias

- Realizar commit: ```git add .``` e ```git commit -m "tipo: descricao do commit resimido"```
- Realizar o push da branch isolada: ```git push brach/minha-nova-branch```

- Criação do Pull Request:
  - Acessar o repositório do GitHub
  - Clicar em "Compare & pull request"
  - Preencher as informações e crie o Pull Request

- Testar a Branch com as alterações realizadas e verificar para aprovação e mesclar na branch principal
  - Fazer o fetch para puxar as referências remotas: ```git fetch origin master```
  - Posso criar e mudar para uma branch local baseada na branch do PR: ```git checkout -b teste-local origin/feature/nova-funcionalidade```
  - Também posso clicar no botão no canto inferior do VSCode e alterar a branch que eu quero. 
    - Fazer os testes necessário, estando na branch temporária.
  - Voltar para a branch master/main: ```git checkout master```
  - Posso apagar a branch de teste criada ou a branch sincronizada

- Aprovar o Pull Request (após os testes)
    - No GitHub, acesse o Pull Request criado
    - Clique em "Merge pull request"
    - Confirme clicando em "Confirm merge"
    - Apago a branch que foi feito o merge (se quiser)

- Sincronizar o repositório local com a branch master do GitHub
    - Voltar a branch principal: ```git checkout master```
    - Atualizar repositório: ```git pull origin```
    - Apagar, se necessário a branch isolada: ```git branch -d  brach/minha-nova-branch```