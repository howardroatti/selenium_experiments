from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from requests import request

url = "https://valor.globo.com/valor-data"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"

request = Request(url=url, headers={'User-Agent': user_agent})
html = urlopen(request).read()

soup = BeautifulSoup(html, 'html.parser')
content_principal = soup.find("div", attrs={"class": "valor-data__components-container"})

extracted_data = {}

values_principal = content_principal.find_all("div", attrs={"class": "data-cotacao__ticker_quote"})
names_principal = content_principal.find_all("div", attrs={"class": "data-cotacao__ticker_name"})

for i in range(5):
    extracted_data[names_principal[i].get_text()] = values_principal[i].get_text()

print(extracted_data)