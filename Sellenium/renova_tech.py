from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

# (Opcional) Executar em modo visível ou headless
options = Options()
# options.add_argument("--headless")  # Descomente para rodar sem abrir a janela

# Abre o Firefox
navegador = webdriver.Firefox(options=options)

# Acessa o site
navegador.get("")

# Espera 5 segundos
time.sleep(5)

# Fecha o navegador
navegador.quit()
