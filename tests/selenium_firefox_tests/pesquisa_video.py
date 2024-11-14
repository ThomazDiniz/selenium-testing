from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.youtube.com")
time.sleep(3)

search_box = driver.find_element("name", "search_query")
search_box.send_keys("aula python")  
search_box.send_keys(Keys.RETURN)
time.sleep(3)