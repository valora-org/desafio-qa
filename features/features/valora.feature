# language: pt 

Funcionalidade: Testar página da Valora
 
Cenario: Verificar tempo de carregamento da página
  Dado que eu acesse a página inicial
  E extraia o tempo de carregamento da pagina
  Então a página carregou em menos de 1500ms

Cenario: Verificar se o video da página inicial não está quebrado
  Dado que eu acesse a página inicial
  E obtenho os links do vídeo
  Então os links deverão estar acessíveis

Cenario: Verificar se o download dos Cases e Artigos não estão quebrados
  Dado que eu acesse a página inicial
  E obtenho os links dos cases e Artigos
  Quando acessar o case ou artigo, extrair os links dos botões de Download
  Então os Links dos botões deverão estar acessíveis

Cenario: Enviar email e verificar confirmação de envio
  Dado que eu acesse a página inicial
  E preencho os campos do formulário de email
  Quando clicar no botão Enviar
  Então devo visualizar a página de sucesso