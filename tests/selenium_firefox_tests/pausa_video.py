from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.youtube.com/watch?v=q7xlDN55bxI")
time.sleep(3)

video_player = driver.find_element("class name", "video-stream")
video_player.click()  
time.sleep(3)


