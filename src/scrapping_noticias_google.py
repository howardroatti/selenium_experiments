from time import sleep
from datetime import datetime

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


exe_path = GeckoDriverManager().install()
service=Service(exe_path)
options = Options()
# options.headless = True
options.add_argument("--incognito")
browser = webdriver.Firefox(service=service, options=options)

url = 'https://news.google.com/topstories?hl=pt-BR&gl=BR&ceid=BR:pt'

browser.get(url)

while(True):
    now = datetime.now()
    
    current_time = now.strftime("%H:%M:%S")
    print(f'==========> Notícias de Última Hora: {current_time}')
    
    try:
        titles = browser.find_elements(by=By.XPATH, value='//a[@class="DY5T1d RZIKme"]')
    except Exception as excpt:
        print(f"A estrutura mudou, reveja o html: {excpt}")
    
    for numero, title in enumerate(titles):
        if len(str(title.text).strip()) > 0:
            print(f"Manchete {numero+1}")
            print(str(title.text).replace("\n", ""))
            print()
        else:
            continue
    print(f'==========> Essas são as notícias de Última Hora: {current_time}')
    sleep(600)
