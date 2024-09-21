from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.zoom.com.br/")
time.sleep(1)

caixa_pesquisa = driver.find_element(
    By.XPATH,
    '//*[@id="new-header"]/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/input',
)
caixa_pesquisa.send_keys("notebook")
caixa_pesquisa.send_keys(Keys.ENTER)
time.sleep(1)

numero = 2

# Primeiro filtro: produtos sem filtros
with open("produtos_sem_filtros.txt", "w", encoding="utf-8") as arquivo:
    for i in range(3):
        nomes_produtos = driver.find_elements(By.XPATH, '//h2[@class="Text_Text__ARJdp Text_MobileLabelXs__dHwGG Text_DesktopLabelSAtLarge__wWsED ProductCard_ProductCard_Name__U_mUQ"]')
        
        lista_nomes = [produto.text for produto in nomes_produtos]
        nomes_formatados = "\n".join(lista_nomes)

        # Escreve os nomes no arquivo
        arquivo.write(nomes_formatados + "\n")

        print(nomes_formatados)
        
        if i == 0:
            driver.execute_script("window.scrollTo(0, 3700);")
        else:
            driver.execute_script("window.scrollTo(0, 3300);")
        time.sleep(2)

        botao_proxima_pagina = driver.find_element(
            By.XPATH, f'//a[@aria-label="Página {numero}"]'
        )
        numero += 1
        if i != 2:
            botao_proxima_pagina.click()
        else:
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)

            # Acessa a nova URL: menores preços
            driver.get("https://www.zoom.com.br/search?q=notebook&hitsPerPage=24&refinements%5B0%5D%5Bid%5D=price&refinements%5B0%5D%5Branges%5D%5Bmin%5D=24.99&refinements%5B0%5D%5Branges%5D%5Bmax%5D=3250&enableCategorySuggestion=true&isDealsPage=false&sortBy=default&enableRefinementsSuggestions=true")
            numero = 2
            time.sleep(2)

            # Segundo filtro: menores preços
            with open("menores_precos.txt", "w", encoding="utf-8") as arquivo_menor:
                for i in range(3):
                    nomes_produtos = driver.find_elements(By.XPATH, '//h2[@class="Text_Text__ARJdp Text_MobileLabelXs__dHwGG Text_DesktopLabelSAtLarge__wWsED ProductCard_ProductCard_Name__U_mUQ"]')
                    
                    lista_nomes = [produto.text for produto in nomes_produtos]
                    nomes_formatados = "\n".join(lista_nomes)

                    # Escreve os nomes no arquivo
                    arquivo_menor.write(nomes_formatados + "\n")

                    print(nomes_formatados)

                    if i == 0:
                        driver.execute_script("window.scrollTo(0, 3700);")
                    else:
                        driver.execute_script("window.scrollTo(0, 3300);")
                    time.sleep(2)

                    botao_proxima_pagina = driver.find_element(
                        By.XPATH, f'//a[@aria-label="Página {numero}"]'
                    )
                    numero += 1
                    if i != 2:
                        botao_proxima_pagina.click()
                    else:
                        driver.execute_script("window.scrollTo(0, 0);")
                        time.sleep(2)

                        # Acessa a nova URL: melhores avaliados
                        driver.get("https://www.zoom.com.br/search?q=notebook&refinements%5B0%5D%5Bid%5D=rating&refinements%5B0%5D%5Branges%5D%5Bmin%5D=4&refinements%5B0%5D%5Branges%5D%5Bmax%5D=NaN&enableCategorySuggestion=true&isDealsPage=false")
                        numero = 2

                time.sleep(2)

                # Terceiro filtro: melhores avaliados
                with open("melhores_avaliados.txt", "w", encoding="utf-8") as arquivo_avaliados:
                    for i in range(3):
                        nomes_produtos = driver.find_elements(By.XPATH, '//h2[@class="Text_Text__ARJdp Text_MobileLabelXs__dHwGG Text_DesktopLabelSAtLarge__wWsED ProductCard_ProductCard_Name__U_mUQ"]')
                        
                        lista_nomes = [produto.text for produto in nomes_produtos]
                        nomes_formatados = "\n".join(lista_nomes)

                        # Escreve os nomes no arquivo
                        arquivo_avaliados.write(nomes_formatados + "\n")

                        print(nomes_formatados)

                        if i == 0:
                            driver.execute_script("window.scrollTo(0, 3700);")
                        else:
                            driver.execute_script("window.scrollTo(0, 3500);")
                        time.sleep(2)

                        botao_proxima_pagina = driver.find_element(
                            By.XPATH, f'//a[@aria-label="Página {numero}"]'
                        )
                        numero += 1
                        if i != 2:
                            botao_proxima_pagina.click()
                        else:
                            driver.execute_script("window.scrollTo(0, 0);")
                            time.sleep(2)
                            
# Função para ler produtos de um arquivo e retornar como um conjunto
def ler_produtos(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        return set(f.read().splitlines())

# Lê os produtos de cada arquivo
produtos_sem_filtros = ler_produtos("produtos_sem_filtros.txt")
menores_precos = ler_produtos("menores_precos.txt")
melhores_avaliados = ler_produtos("melhores_avaliados.txt")

# Encontra os produtos que estão em todos os três conjuntos
produtos_comuns = produtos_sem_filtros.intersection(menores_precos).intersection(melhores_avaliados)

# Pega os 5 primeiros produtos comuns
produtos_comuns_limites = list(produtos_comuns)[:5]

# Grava os 5 produtos comuns no arquivo melhores_produtos.txt
with open("melhores_produtos.txt", "w", encoding="utf-8") as arquivo_melhores:
    for produto in produtos_comuns_limites:
        arquivo_melhores.write(produto + "\n")

print("Os 5 primeiros produtos comuns salvos em melhores_produtos.txt.")



time.sleep(2)

# Fecha o driver
driver.close()
