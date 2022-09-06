from unittest import result
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_eight_components():
    exe_path = GeckoDriverManager().install()
    service=Service(exe_path)
    
    # Janela em modo anônimo
    options = Options()
    options.add_argument("--incognito")
    options.headless = True
    
    browser = webdriver.Firefox(service=service, options=options)

    browser.get("https://google.com")

    title = browser.title
    assert title == "Google"

    browser.implicitly_wait(60)

    search_box = browser.find_element(by=By.NAME, value="q")
    search_box.send_keys("Selenium")
    search_box.send_keys(Keys.RETURN)

    resultado = browser.find_element(by=By.XPATH, value='//div[@id="result-stats"]')
    print(resultado.text)

    search_box = browser.find_element(by=By.NAME, value="q")
    value = search_box.get_attribute("value")
    assert value == "Selenium"

    browser.implicitly_wait(60.0)

    input("Pressione enter para sair...")
    browser.quit()
    print("Fim...")

if __name__ == '__main__':
    test_eight_components()
