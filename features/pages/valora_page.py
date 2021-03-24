from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
from browser import Browser
import time

class ValoraPage(Browser):

    def open_url(self, url):
        self.driver.get(url)

    # Extrair tempo de carregamento da página
    def get_page_loadtime (self):
        responseStart = self.driver.execute_script("return window.performance.timing.responseStart")
        domComplete = self.driver.execute_script("return window.performance.timing.domComplete")
        
        performance = domComplete - responseStart
        return performance

    # Testar link dos vídeos
    def extract_video_urls (self):
        video_urls = []
        videos_sources = self.driver.find_elements_by_tag_name('source')
        for videos in videos_sources:
            video_urls.append(videos.get_attribute('src'))
        return video_urls

    def verify_video_urls (self, video_urls):
        for url in video_urls:
            self.open_url(url)
            self.driver.find_element_by_name('media')
        
    
    # Testar acesso e links de downloads dos Cases e Artigos
    def extract_cases_articles_urls (self):
        cases_articles_urls = [] # Contém as URLs dos Artigos e Cases
        
        cases_articles = self.driver.find_elements_by_css_selector ('.MS-content > .item > a')
        
        for item in cases_articles:
            cases_articles_urls.append(item.get_attribute('href'))
        
        return cases_articles_urls
        
    
    def extract_download_button_urls (self, cases_articles_urls):
        download_button_urls = [] # Contém as URLs dos botões de Download
        
        # Acessar a página e procurar pelo botão de Download dentro de cada case / artigo e caso encontrado o botão, extrair o seu link
        for url in cases_articles_urls:
            self.open_url(url)
            try:
                if self.driver.find_element_by_css_selector ('div.mcenter > a.btn.btn--primary'):
                    button_href = self.driver.find_element_by_css_selector ('div.mcenter > a.btn.btn--primary').get_attribute('href')
                    download_button_urls.append (button_href)
            except NoSuchElementException:
                pass
        
        return download_button_urls
        
    
    def verify_downloads_links(self, download_button_urls):
        # Testar links dos botões de DOWNLOAD
        for url in download_button_urls:
            self.open_url(url)


    def send_email_fields (self):
        
        input_name = self.driver.find_element_by_css_selector('#app > div:nth-child(4) > div.col-md-6.pd0 > input[type=text]')
        input_company = self.driver.find_element_by_css_selector('#app > div:nth-child(4) > div:nth-child(2) > input[type=text]')
        input_email = self.driver.find_element_by_css_selector('#app > div:nth-child(5) > div.col-md-6.pd0 > input[type=text]')
        input_phone = self.driver.find_element_by_css_selector('#app > div:nth-child(5) > div:nth-child(2) > input[type=text]')
        input_message = self.driver.find_element_by_css_selector('#app > div:nth-child(6) > div > textarea')

        input_name.send_keys('Vitor Rezende')
        input_company.send_keys('Unisystem')
        input_email.send_keys('vitorezende@gmail.com')
        input_phone.send_keys('66999727657')
        input_message.send_keys('Teste desafio QA - Selenium')

    def send_email_click_button (self):
        send_button = self.driver.find_element_by_css_selector('#app > div:nth-child(7) > div > a')    
        send_button.click()

    def get_current_page(self):
        time.sleep(5)
        current_page = self.driver.current_url
        return current_page
        