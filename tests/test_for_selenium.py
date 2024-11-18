import selenium

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

import re
import time
import json
from html import unescape


def test_google_search(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    search_box = driver.find_element("name", "q")


def test_youtube_homepage(driver):
    # Set up the WebDriver
    driver.get("https://www.youtube.com")

    # Assert that the title contains "YouTube"
    assert "YouTube" in driver.title

    # Wait for the page to load
    time.sleep(2)

    # Assert that the "Search" input box is present
    search_box = driver.find_element(By.NAME, "search_query")
    assert search_box is not None

def test_google_search_results(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Python Selenium")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    assert len(results) > 0
    assert any("Python" in result.text for result in results)

def test_wikipedia_homepage(driver):
    driver.get("https://www.wikipedia.org/")
    assert "Wikipedia" in driver.title
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("Selenium")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    assert "Selenium" in driver.title


def test_amazon_search(driver):
    driver.get("https://www.amazon.com")
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("Laptop")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    results = driver.find_elements(By.CSS_SELECTOR, ".s-title-instructions-style")
    assert len(results) > 0

def test_twitter_title(driver):
    driver.get("https://www.twitter.com")
    time.sleep(2)
    assert "X. O que está acontecendo / X" in driver.title


def test_github_title(driver):
    driver.get("https://github.com")
    assert "GitHub" in driver.title

def test_github_search(driver):
    driver.get("https://github.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("selenium")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    results = driver.find_elements(By.CSS_SELECTOR, ".repo-list-item h3")
    assert len(results) > 0