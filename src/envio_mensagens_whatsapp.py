from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

exe_path = GeckoDriverManager().install()
service=Service(exe_path)
options = Options()
options.add_argument("--incognito")
browser = webdriver.Firefox(service=service, options=options)

browser.get('https://web.whatsapp.com/')

input("Faça o login e pressione Enter no Prompt...")

destinatarios = ["Howard's Group"]

for destinatario in destinatarios:
    campo_busca = browser.find_element(by=By.XPATH, value='//div[@data-testid="chat-list-search"]')
    campo_busca.send_keys(destinatario)
    sleep(10)
    usuarios = browser.find_elements(by=By.XPATH, value='//div[@class="_3OvU8"]')
    usuarios[0].click()
    sleep(10)
    mensagem = "*Teste Selenium, Prof. Howard...*"
    for letra in mensagem:
        campo_mensagem = browser.find_element(by=By.XPATH, value='//div[@data-testid="conversation-compose-box-input"]')
        campo_mensagem.send_keys(letra)
    campo_mensagem.send_keys(Keys.RETURN)

input("Pressione enter para sair...")
browser.quit()
print("Fim...")