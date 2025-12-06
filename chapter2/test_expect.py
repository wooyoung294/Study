import os
import time

from playwright.sync_api import Playwright, expect

Base_URL = os.getenv(
    "BASE_URL",
    "https://blue-ground-0e078e000.3.azurestaticapps.net",  # 기본값
)
def test_enable(playwright:Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto(Base_URL)
    time.sleep(1)
    btn = page.locator('#clickAction')

    expect(btn).to_be_enabled()

    btn.click()
    expect(btn).not_to_be_enabled()
    expect(btn).to_be_disabled()

    time.sleep(1)

    browser.close()

def test_have_text(playwright:Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto(Base_URL)
    time.sleep(1)

    desc = page.locator('#dbClickDesc')

    expect(desc).to_be_empty()
    expect(desc).to_have_text("")

    btn = page.locator('#dbClickAction')
    btn.dblclick()

    expect(desc).not_to_be_empty()
    expect(desc).to_have_text("DoubleClick")

    time.sleep(1)

    browser.close()

def test_check(playwright:Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto(Base_URL)
    time.sleep(1)

    radio1 = page.locator('#radio1Action')
    radio2 = page.locator('#radio2Action')

    expect(radio1).to_be_checked()

    expect(radio2).to_be_checked(checked=False)
    expect(radio2).not_to_be_checked()

    indeterminate_chk = page.locator('#indeterminate')
    expect(indeterminate_chk).to_be_checked(indeterminate=True)
    browser.close()

def test_value(playwright:Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto(Base_URL)
    time.sleep(1)

    select = page.locator('#selectAction')

    expect(select).to_have_value("option1")

    select.select_option("option2")

    expect(select).to_have_value("option2")

    browser.close()
