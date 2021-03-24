## Projeto de demonstração de habilidades em:

* **Python**
* **Postman**
* **Selenium**


## Postman Collection

desafio-qa/Postman Collection

**GitHub API** https://docs.github.com/pt/rest

Casos de usos aplicados:

* Busca por informações de um **Repositório**
* Lista de **commits** deste repositório
* Lista de **forks** deste repositório

**Objetivo**
Obter informações de um repositório no GitHub, bem como a lista de commits e forks deste repositório.

**Resultado Esperado**
O resultado esperado para as requisições desta coleção são as informações do repositório do Kernel do Linux, bem como a lista de commits e forks deste repositório.

**Teste de Verificação Aplicado**
Status 200 OK


## Teste automatizado com SELENIUM

Validação da landing page https://valora.cc/

Este teste automatizado valida os seguintes cenários:

* O tempo de carregamento da página deve ser **menor que 1.5 segundos**;
* O vídeo na página inicial **não está quebrado**;
* O download dos cases e artigos **não está quebrado**;
* O formulário de contato deve estar **enviando o e-mail** (não precisa validar o recebimento)

**Para executar este projeto utilize os seguintes comandos**:

* git clone $desafio-qa
* cd $desafio-qa
* docker build -t desafio-qa .
* docker run desafio-qa
