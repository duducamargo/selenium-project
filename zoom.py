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
    '//*[@id="new-header"]/div[1]/div/div/div[3]/div/div/div[2]/div/div[' "1]/input",
)
caixa_pesquisa.send_keys("notebook")
caixa_pesquisa.send_keys(Keys.ENTER)
time.sleep(1)

numero = 2

for i in range(3):
    if i == 0:
        driver.execute_script("window.scrollTo(0, 3700);")
    else:
        driver.execute_script("window.scrollTo(0, 3300);")
    time.sleep(2)

    botao_proxima_pagina = driver.find_element(
        By.XPATH, f'//a[@aria-label="Página {numero}"]'
    )
    numero = numero + 1
    if i != 2:
        botao_proxima_pagina.click()
    else:
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        
        driver.get("https://www.zoom.com.br/search?q=notebook&hitsPerPage=24&refinements%5B0%5D%5Bid%5D=price&refinements%5B0%5D%5Branges%5D%5Bmin%5D=24.99&refinements%5B0%5D%5Branges%5D%5Bmax%5D=3250&sortBy=default&isDealsPage=false&enableRefinementsSuggestions=true")
        numero = 2
        time.sleep(2)
        for i in range(3):
            if i == 0:
                driver.execute_script("window.scrollTo(0, 3700);")
            else:
                driver.execute_script("window.scrollTo(0, 3300);")
            time.sleep(2)

            botao_proxima_pagina = driver.find_element(
                By.XPATH, f'//a[@aria-label="Página {numero}"]'
            )
            numero = numero + 1
            if i != 2:
                botao_proxima_pagina.click()
            else:
                driver.execute_script("window.scrollTo(0, 0);")
                time.sleep(2)
                driver.get("https://www.zoom.com.br/search?q=notebook&hitsPerPage=24&refinements%5B0%5D%5Bid%5D=rating&refinements%5B0%5D%5Branges%5D%5Bmin%5D=4&sortBy=default&isDealsPage=false&enableRefinementsSuggestions=true")
                numero = 2
        time.sleep(2)
        for i in range(3):
            if i == 0:
                driver.execute_script("window.scrollTo(0, 3700);")
            else:
                driver.execute_script("window.scrollTo(0, 3300);")
            time.sleep(2)

            botao_proxima_pagina = driver.find_element(
                By.XPATH, f'//a[@aria-label="Página {numero}"]'
            )
            numero = numero + 1
            if i != 2:
                botao_proxima_pagina.click()
            else:
                driver.execute_script("window.scrollTo(0, 0);")
                time.sleep(2)


        


driver.close()
