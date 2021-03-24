from pages.valora_page import ValoraPage

valoraPage = ValoraPage ()

# Verificando tempo de carregamento da página
@given(u'que eu acesse a página inicial')
def step_impl(context):
    valoraPage.open_url('https://valora.cc')

@given(u'extraia o tempo de carregamento da pagina')
def step_impl(context):
    context.pageLoadingTime = valoraPage.get_page_loadtime()

    
@then(u'a página carregou em menos de 1500ms')
def step_impl(context):
    assert context.pageLoadingTime <= 1500


# Verificando os links dos vídeos
@given(u'obtenho os links do vídeo')
def step_impl(context):
    context.video_urls = [] 
    context.video_urls = valoraPage.extract_video_urls()

@then(u'os links deverão estar acessíveis')
def step_impl(context):
    valoraPage.verify_video_urls(context.video_urls)


# Verificando o download dos Cases e Artigos
@given(u'obtenho os links dos cases e Artigos')
def step_impl(context):
    context.cases_articles_urls = []
    context.cases_articles_urls = valoraPage.extract_cases_articles_urls()


@when(u'acessar o case ou artigo, extrair os links dos botões de Download')
def step_impl(context):
    context.download_button_urls = []
    context.download_button_urls = valoraPage.extract_download_button_urls(context.cases_articles_urls)


@then(u'os Links dos botões deverão estar acessíveis')
def step_impl(context):
    valoraPage.verify_downloads_links(context.download_button_urls)


# Enviar email e verificar envio
@given(u'preencho os campos do formulário de email')
def step_impl(context):
    valoraPage.send_email_fields()


@when(u'clicar no botão Enviar')
def step_impl(context):
    valoraPage.send_email_click_button()


@then(u'devo visualizar a página de sucesso')
def step_impl(context):
    assert valoraPage.get_current_page() == 'https://valora.cc/confirmacao.html'