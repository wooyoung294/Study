import os
import time

from playwright.sync_api import Playwright

Base_URL = os.getenv(
    "BASE_URL",
    "https://blue-ground-0e078e000.3.azurestaticapps.net",  # 기본값
)
def test_click(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(Base_URL)
    time.sleep(1)

    page.locator('#clickAction').click()
    time.sleep(1)

    browser.close()


def test_db_click(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(Base_URL)
    time.sleep(1)

    page.locator('#dbClickAction').dblclick()
    time.sleep(1)

    browser.close()

def test_check(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(Base_URL)
    time.sleep(1)

    page.locator('#checkAction').check()
    time.sleep(1)

    browser.close()

def test_radio(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(Base_URL)
    time.sleep(1)

    page.locator('#radio2Action').check()
    time.sleep(1)

    page.locator('#radio1Action').click()
    time.sleep(1)
    browser.close()

def test_select(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(Base_URL)
    time.sleep(1)

    # page.locator('#selectAction').click()
    # time.sleep(2)

    page.locator('#selectAction').select_option("option2")
    time.sleep(1)

    # page.locator('#selectAction').click()
    # time.sleep(2)

    browser.close()

def test_type(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(Base_URL)
    time.sleep(1)

    page.locator('#typeAction').type("AAAAAA")
    time.sleep(1)

    # page.locator('#typeAction').type("BBBBBB")
    # time.sleep(5)

    browser.close()

def test_fill(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(Base_URL)
    time.sleep(1)

    page.locator('#fillAction').fill("CCCCCC")
    time.sleep(1)

    browser.close()

