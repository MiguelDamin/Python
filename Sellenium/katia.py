from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get('https://invertexto.com')

time.sleep(3)  # espera o site carregar

campo = driver.find_element(By.TAG_NAME, 'input')  # pega o primeiro campo input da página

campo.send_keys('KATIA')

time.sleep(5)  # para você ver o que digitou

driver.quit()
