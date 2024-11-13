import pytest
import selenium
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import re
import chromedriver_autoinstaller
import time
import json
from html import unescape

@pytest.fixture
def test_setup():
	global driver
	chrome_options = Options()
	#chrome_options.add_argument("--headless")  #(sem abrir janela)
	chrome_options.add_argument("--disable-gpu")
	chrome_options.add_argument("--no-sandbox")
	chrome_options.add_argument("start-maximized")
	chrome_options.add_argument("enable-automation")
	chrome_options.add_argument("--disable-infobars")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--disable-browser-side-navigation")
	chrome_options.add_argument("--disable-features=VizDisplayCompositor")
	driver = webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()), options=chrome_options)
	driver.implicitly_wait(10)
	
	yield
	
	driver.close()
	driver.quit()
