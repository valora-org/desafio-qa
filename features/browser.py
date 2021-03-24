from selenium import webdriver
import os

class Browser (object):
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  driver = webdriver.Chrome(chrome_options=chrome_options)

  def close_browser (self):
    self.driver.quit()
