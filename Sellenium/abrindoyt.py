from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Iniciar o navegador (Firefox)
driver = webdriver.Firefox()

# 1. Abrir o YouTube
driver.get("https://www.youtube.com")
time.sleep(3)  # Espera a página carregar

# 2. Encontrar a barra de pesquisa e digitar um termo
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Austria paisagens")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# 3. Clicar no primeiro vídeo da lista
first_video = driver.find_element(By.ID, "video-title")
first_video.click()

# (Opcional) Esperar alguns segundos antes de fechar
time.sleep(10)

# driver.quit()  # Descomente se quiser que feche sozinho depois
