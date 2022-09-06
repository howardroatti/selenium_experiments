from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from datetime import datetime
import time

exe_path = GeckoDriverManager().install()
service=Service(exe_path)
options = Options()
# Esconde o navegador
options.headless = True
browser = webdriver.Firefox(service=service, options=options)

while(True):
	now = datetime.now()
	
	# this is just to get the time at the time of
	# web scraping
	current_time = now.strftime("%H:%M:%S")
	print(f'At time : {current_time} IST')
	browser.get('https://finance.yahoo.com/cryptocurrencies/')
	response = browser.page_source
	browser.quit()
	html_data = BeautifulSoup(response, 'html.parser')
	headings = html_data.find_all('tr')[0]
	headings_list = []
	for x in headings:
		headings_list.append(x.text)
	headings_list = headings_list[:10]

	data = []
	for x in range(1, 6):
		row = html_data.find_all('tr')[x]
		column_value = row.find_all('td')
		dict = {}
		
		for i in range(10):
			dict[headings_list[i]] = column_value[i].text
		data.append(dict)
		
	for coin in data:
		print(coin)
		print('')
	time.sleep(600)
