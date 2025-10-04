# Instruções
Desenvolvedor: Danilo Martins Caldeira.

## Ambiente virtual: 
Os comandos a seguir podem ser execudados:
1. Criar: ```python -m venv venv```
2. Ativar: ```.\venv\Scripts\activate```
3. Instalar o que é preciso: ```pip install -r requirements.txt```
1. Desativar: ```deactivate```

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