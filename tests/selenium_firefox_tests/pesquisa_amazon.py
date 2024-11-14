from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()


driver.get("https://www.google.com")

search_box = driver.find_element("name", "q")
search_box.send_keys("amazon") 
search_box.send_keys(Keys.RETURN)


time.sleep(2)

find_amazon =  driver.find_element("partial link text", "amazon.com.br")
find_amazon.click()
time.sleep(2)

scroll_increment = 500  # Pixels para rolar por vez
current_position = 0    # Posição inicial

try:
    black_friday_button = driver.find_element("link text", "Esquenta Black Friday")  # Altere o texto se necessário
    black_friday_button.click()
    time.sleep(3)
except:
    print("Botão 'Esquenta Black Friday' não encontrado.")

try:
    departments_section = driver.find_element("id", "departments")
    driver.execute_script("arguments[0].scrollIntoView();", departments_section)
    time.sleep(2)
    
    # Clica na categoria "Beleza"
    beauty_category = driver.find_element("xpath", '//span[text()="Beleza"]')
    beauty_category.click()
    time.sleep(3)
except:
    print("Seção de departamentos ou categoria 'Beleza' não encontrada.")

# Aguarda um pouco e fecha o navegador
time.sleep(5)
driver.quit()