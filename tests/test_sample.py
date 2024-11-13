import selenium

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import re
import time
import json
from html import unescape


def test_google_search(test_setup):
    # Acessar o site do Google
    driver.get("https://www.google.com")
    
    # Verificar se o título contém "Google"
    assert "Google" in driver.title
    
    # Localizar a barra de pesquisa, digitar algo e submeter
    search_box = driver.find_element("name", "q")
    search_box.send_keys("pytest selenium")
    search_box.submit()
    
    # Esperar que a página carregue e verificar se os resultados contêm o termo pesquisado
    assert "pytest selenium" in driver.page_source

def test_soma():
    assert 2 + 2 == 4

def test_subtracao():
    assert 5 - 3 == 2

'''
test_*.py
*_test.py
pip install pytest-json-report
pip install pytest-html
python -m pytest
python -m pytest
python -m pytest --html=report.html --json-report --json-report-file=report.json
'''