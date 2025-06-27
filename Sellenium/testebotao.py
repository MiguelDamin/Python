from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# (Opcional) Modo headless para não abrir janela
options = Options()
# options.add_argument("--headless")

navegador = webdriver.Firefox(options=options)
navegador.maximize_window()
navegador.get("https://renova-tech.vercel.app/")

# Espera até o link estar presente
wait = WebDriverWait(navegador, 10)
link_solar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="#solar"]')))

# Clica no link
link_solar.click()

# Agora, espera até a seção #solar estar visível
secao = wait.until(EC.visibility_of_element_located((By.ID, "solar")))

# Verifica se a rolagem funcionou: seção deve estar visível
assert secao.is_displayed(), "Erro: seção #solar não está visível após o clique."

print("✅ Teste passou: botão clicou e seção #solar foi exibida.")

navegador.quit()
