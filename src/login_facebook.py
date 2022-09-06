from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

exe_path = GeckoDriverManager().install()
service=Service(exe_path)
browser = webdriver.Firefox(service=service)

usuario = input("Usuário do Facebook: ")
senha = input("Senha do Facebook: ")

browser.get("https://www.facebook.com")
print("Acessou o Facebook...")
sleep(1)

try:
    campo_nome_usuario = browser.find_element(by=By.ID, value="email")
    campo_nome_usuario.send_keys(usuario)
    print("Entrou com o nome de usuário...")
    sleep(1)
except Exception as excpt:
    print(f"Tivemos uma falha: {excpt}")
    browser.quit()
    exit(1)

try:
    campo_senha = browser.find_element(by=By.ID, value="pass")
    campo_senha.send_keys(senha)
    print("Entrou com a senha de usuário...")
    sleep(1)
except Exception as excpt:
    print(f"Tivemos uma falha: {excpt}")
    browser.quit()
    exit(1)

try:
    botao_login = browser.find_element(by=By.NAME, value="login")
    botao_login.click()
    print("Clicou no botão de login...")
    sleep(1)
except Exception as excpt:
    print(f"Tivemos uma falha: {excpt}")
    browser.quit()
    exit(1)

print("Pronto!")
input("Pressione enter para sair...")
browser.quit()
print("Fim...")
