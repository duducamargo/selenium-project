# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time


# driver = webdriver.Chrome()
# driver.maximize_window()

# driver.get("https://www.zoom.com.br/notebook")
# time.sleep(3)

# div = driver.find_element(By.CLASS_NAME, 'AllFiltersButton_AllFilters___ayQd')

# div_button = div.find_element(By.TAG_NAME('button'))
# div_button.click()

# driver.quit()

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
    if(i == 0):
        driver.execute_script("window.scrollTo(0, 3800);")
    else:
        driver.execute_script("window.scrollTo(0, 3300);")
    time.sleep(2)

    botao_proxima_pagina = driver.find_element(By.XPATH, f'//a[@aria-label="Página {numero}"]')
    numero = numero + 1
    if(i != 3):
        botao_proxima_pagina.click()

pagina1_pesquisa = driver.current_url

driver.close()
