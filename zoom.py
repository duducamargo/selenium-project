from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def extrair_produtos(driver, url, arquivo, scroll_y, pages=3):
    driver.get(url)
    time.sleep(1)
    with open(arquivo, "w", encoding="utf-8") as f:
        for i in range(pages):
            nomes_produtos = driver.find_elements(By.XPATH, '//h2[@class="Text_Text__ARJdp Text_MobileLabelXs__dHwGG Text_DesktopLabelSAtLarge__wWsED ProductCard_ProductCard_Name__U_mUQ"]')
            lista_nomes = [produto.text for produto in nomes_produtos]
            f.write("\n".join(lista_nomes) + "\n")
            print("\n".join(lista_nomes))

            if i == 0:
                driver.execute_script(f"window.scrollTo(0, {scroll_y});")
            else:
                driver.execute_script(f"window.scrollTo(0, {scroll_y - 200});")
                
            time.sleep(2)
            
            if i != 2:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//a[@aria-label="Página {i + 2}"]'))).click()
            else:
                driver.execute_script(f"window.scrollTo(0, 0);")
                time.sleep(1)

def ler_produtos(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        return set(f.read().splitlines())

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.zoom.com.br/")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="new-header"]/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/input')))
caixa_pesquisa = driver.find_element(By.XPATH, '//*[@id="new-header"]/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/input')
caixa_pesquisa.send_keys("notebook")
caixa_pesquisa.send_keys(Keys.ENTER)

extrair_produtos(driver, driver.current_url, "produtos_sem_filtros.txt", 3700)

extrair_produtos(driver, "https://www.zoom.com.br/search?q=notebook&hitsPerPage=24&refinements%5B0%5D%5Bid%5D=price&refinements%5B0%5D%5Branges%5D%5Bmin%5D=24.99&refinements%5B0%5D%5Branges%5D%5Bmax%5D=3250&enableCategorySuggestion=true&isDealsPage=false&sortBy=default&enableRefinementsSuggestions=true", "menores_precos.txt", 3700)

extrair_produtos(driver, "https://www.zoom.com.br/search?q=notebook&refinements%5B0%5D%5Bid%5D=rating&refinements%5B0%5D%5Branges%5D%5Bmin%5D=4&refinements%5B0%5D%5Branges%5D%5Bmax%5D=NaN&enableCategorySuggestion=true&isDealsPage=false", "melhores_avaliados.txt", 3700)

produtos_sem_filtros = ler_produtos("produtos_sem_filtros.txt")
menores_precos = ler_produtos("menores_precos.txt")
melhores_avaliados = ler_produtos("melhores_avaliados.txt")

produtos_comuns = produtos_sem_filtros.intersection(menores_precos).intersection(melhores_avaliados)
produtos_comuns_limites = list(produtos_comuns)[:5]

with open("melhores_produtos.txt", "w", encoding="utf-8") as arquivo_melhores:
    for produto in produtos_comuns_limites:
        arquivo_melhores.write(produto + "\n")

print("Os 5 primeiros produtos comuns salvos em melhores_produtos.txt.")

driver.close()
