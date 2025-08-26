import re

from selenium import webdriver


def test_has_title():
    driver = webdriver.Chrome()
    driver.get("https://playwright.dev/")
    assert re.search(r"Playwright", driver.title)