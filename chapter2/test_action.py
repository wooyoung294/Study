import time

from playwright.sync_api import Playwright


def test_click(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://study.wooyoung.site/")
    time.sleep(1)

    page.locator('#clickAction').click()
    time.sleep(1)

    browser.close()


def test_db_click(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://study.wooyoung.site/")
    time.sleep(1)

    page.locator('#dbClickAction').dblclick()
    time.sleep(1)

    browser.close()

def test_check(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://study.wooyoung.site/")
    time.sleep(1)

    page.locator('#checkAction').check()
    time.sleep(1)

    browser.close()

def test_radio(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://study.wooyoung.site/")
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

    page.goto("https://study.wooyoung.site/")
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

    page.goto("https://study.wooyoung.site/")
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

    page.goto("https://study.wooyoung.site/")
    time.sleep(1)

    page.locator('#fillAction').fill("CCCCCC")
    time.sleep(1)

    browser.close()

