from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()


driver.get("https://www.google.com")

search_box = driver.find_element("name", "q")
search_box.send_keys("youtube") 
search_box.send_keys(Keys.RETURN)


time.sleep(2)

find_youtube =  driver.find_element("partial link text", "https://www.youtube.com/")
find_youtube.click()
time.sleep(2)
