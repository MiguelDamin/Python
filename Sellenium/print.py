from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Abre o navegador Firefox
navegador = webdriver.Firefox()

# Abre o site do Globo Esporte
navegador.get("https://ge.globo.com")  # antigo globoesporte.globo.com

# Espera a página carregar
time.sleep(5)  # tempo para garantir que tudo carregue, pode ajustar

# Tira o screenshot
navegador.save_screenshot("globo_esporte.png")

print("✅ Print salvo como globo_esporte.png")

# Fecha o navegador
navegador.quit()
