from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Abre o Firefox
navegador = webdriver.Firefox()

# Acessa a página de login
navegador.get("https://the-internet.herokuapp.com/login")

time.sleep(2)

# Preenche usuário e senha
usuario = navegador.find_element(By.ID, "username")
usuario.send_keys("usuario_teste")

senha = navegador.find_element(By.ID, "password")
senha.send_keys("senha_errada")

# Clica no botão de login
botao_login = navegador.find_element(By.CLASS_NAME, "radius")
botao_login.click()

time.sleep(2)

# Tira print do resultado
navegador.save_screenshot("login_teste.png")

print("✅ Login testado. Print salvo como login_teste.png")

# Fecha o navegador
navegador.quit()
