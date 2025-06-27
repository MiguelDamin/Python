from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

navegador = webdriver.Firefox()
navegador.get("https://www.megaeletronicos.com/categoria/78/monitores")

# Scroll para carregar mais produtos
for _ in range(5):  # Ajuste conforme necessário
    navegador.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(2)

# Coleta os produtos visíveis
produtos = navegador.find_elements(By.CLASS_NAME, 'product-box')

dados = []

for produto in produtos:
    try:
        titulo = produto.find_element(By.CLASS_NAME, 'product-title').text
        preco = produto.find_element(By.CLASS_NAME, 'price').text

        # Filtro: só produtos com "QHD" e "100Hz" no título
        if "QHD" in titulo and ("100Hz" in titulo or "165Hz" in titulo or "144Hz" in titulo):
            dados.append((titulo, preco))
    except:
        continue

# Mostra os produtos encontrados
for nome, preco in dados:
    print(f"{nome} — {preco}")

navegador.quit()
