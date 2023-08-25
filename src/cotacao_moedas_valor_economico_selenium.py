from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup

exe_path = GeckoDriverManager().install()
service=Service(exe_path)
options = Options()
# Esconde o navegador
options.add_argument('-headless')
browser = webdriver.Firefox(service=service, options=options)
browser.get("https://valor.globo.com/valor-data")

html = browser.page_source
# print(browser.page_source)
soup = BeautifulSoup(html, 'html.parser')
content_principal = soup.find("div", attrs={"class": "valor-data__components-container"})

extracted_data = {}

values_principal = content_principal.find_all("div", attrs={"class": "data-cotacao__ticker_quote"})
names_principal = content_principal.find_all("div", attrs={"class": "data-cotacao__ticker_name"})

with open("cotacoes.txt", "a") as f:
    for i in range(5):
        extracted_data[names_principal[i].get_text()] = values_principal[i].get_text()
        f.writelines(f"{names_principal[i].get_text()}: {values_principal[i].get_text()}\n")

print(extracted_data)

print("Pronto!")
input("Pressione enter para sair...")
browser.quit()
print("Fim...")
