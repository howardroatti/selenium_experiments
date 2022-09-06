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
# options.add_argument("--incognito")
browser = webdriver.Firefox(service=service, options=options)

# open facebook.com using get() method
browser.get('https://www.facebook.com/')

# user_name or e-mail id
with open("/home/howard/Workspace/selenium_experiments/facebook_user.bin", 'r') as myfile:
	username = myfile.read().replace('\n', '')

# getting password from text file
with open('/home/howard/Workspace/selenium_experiments/facebook_pass.bin', 'r') as myfile:
	password = myfile.read().replace('\n', '')

print("Let's Begin")

element = browser.find_elements(by=By.XPATH, value='//*[@id ="email"]')
element[0].send_keys(username)
print("Username Entered")

element = browser.find_elements(by=By.XPATH, value='//*[@id ="pass"]')
element[0].send_keys(password)
print("Password Entered")

# logging in
log_in = browser.find_element(by=By.NAME, value="login")
log_in.click()
print("Login Successful")

browser.get('https://www.facebook.com/events/birthdays/')

feed = 'Feliz aniversário!'

sleep(10)
element = browser.find_elements(by=By.XPATH, value="//div[@style='outline: currentcolor none medium; user-select: text; white-space: pre-wrap; overflow-wrap: break-word;']")

for el in element:
	el.send_keys(feed)
	# el.send_keys(Keys.RETURN)

print("Felicitações desejadas...")

input("Pressione enter para sair...")
browser.quit()
print("Fim...")
