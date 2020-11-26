## <img src="https://valora.cc/img/logo2.png" alt="Valora" width="24" /> Desafio Q.A.

Parabéns! Se você chegou até aqui significa que você passou pelas etapas mais difíceis do nosso processo seletivo. Somos extremamente criteriosos com as pessoas que vão integrar nosso time porque só aceitamos pessoas incríveis!

Agora é a parte fácil. Chegou a hora de mostrar todas as suas habilidades de transformar café em código. Vamos lá?

Nesse desafio iremos avaliar suas habilidades em:

* **Python**
* **Postman**
* **Selenium**

## Postman

No dia-a-dia de trabalho uma de suas atribuições será validar a API do nosso produto. Portanto, vamos testar seu domínio do Postman e sua capacidade de interpretar e descrever um caso de uso.

Escolha na lista de APIs públicas (https://github.com/public-apis/public-apis) por uma API de sua preferência e crie uma coleção no Postman que execute 3 casos de uso utilizando disponíveis nesta API. 

Por exemplo:

* **Unsplash** https://unsplash.com/documentation#search-photos 
* Caso de uso **“Search Photos”**
* Documente o **cenário** e o **retorno esperado**
* Crie a **request**

## Automação (Selenium)

Outra habilidade importante para este cargo é a automação de testes e2e. Recomendamos a utilização da stack **Python+Selenium+Behave+Nose** porém, sinta-se à vontade para utilizar outra de sua preferência.

Nesta etapa, você fará a validação de uma página da web, neste caso, a nossa landing page https://valora.cc/.

Analise a página e crie uma automação que valide os seguintes cenários:

* O tempo de carregamento da página deve ser **menor que 1.5 segundos**;
* O vídeo na página inicial **não está quebrado**;
* O download dos cases e artigos **não está quebrado**;
* O formulário de contato deve estar **enviando o e-mail** (não precisa validar o recebimento)

## Requisitos

* O projeto precisa estar configurado para rodar em um ambiente macOS ou Ubuntu (preferencialmente como container Docker).
* Deve anexar ao seu projeto a coleção do postman com todos os endpoints validados e exemplos de utilização.

**Para executar seu código devemos executar apenas os seguintes comandos**:

* git clone $seu-fork
* cd $seu-fork
* comando para instalar dependências
* comando para executar a aplicação

## Critério de avaliação

* **Organização do código**: Separação de módulos, webdrivers, pages, components e etc
* **Clareza**: O README explica de forma resumida qual é o problema e como pode rodar a aplicação? Os casos de uso estão descritos de forma clara e objetiva?
* **Assertividade**: A aplicação está fazendo o que é esperado? Se tem algo faltando, o README explica o porquê?
* **Legibilidade do código** (incluindo comentários)
* **Segurança**: Existe alguma vulnerabilidade clara?
* **Reaproveitamento**: O código está replicável e sem repetições desnecessárias?
* **Escolhas técnicas**: A escolha das bibliotecas, banco de dados, arquitetura, etc, é a melhor escolha para a aplicação?

## Dúvidas

Quaisquer dúvidas que você venha a ter, consulte as issues para ver se alguém já não a fez e caso você não ache sua resposta, abra você mesmo uma nova issue!

Ao completar o desafio, submeta um pull-request a esse repositório com uma breve explicação das decisões tomadas e principalmente as instruções para execução do projeto.

**Boa sorte! ;)**
