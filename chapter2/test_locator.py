import re
import time

from playwright.sync_api import Page, expect, Playwright


def test_id_btn(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://study.wooyoung.site/")
    time.sleep(1)
    page.locator('#idBtn').click()
    time.sleep(1)

    browser.close()

def test_name_btn(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://study.wooyoung.site/")
    time.sleep(1)
    page.locator('button[name="nameBtn"]').click()
    time.sleep(1)

    browser.close()


def test_test_id_btn(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://study.wooyoung.site/")
    time.sleep(1)
    page.get_by_test_id('test').click()
    time.sleep(1)

    browser.close()



def test_class_btn(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://study.wooyoung.site/")
    time.sleep(1)
    page.locator('.myClass').click()
    time.sleep(1)

    browser.close()


def test_text_btn(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://study.wooyoung.site/")
    time.sleep(1)
    page.get_by_text("Text").click()
    time.sleep(1)


def test_text_exact_btn(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://study.wooyoung.site/")
    time.sleep(1)
    page.get_by_text("Text",exact=True).click()
    time.sleep(1)

    browser.close()


def test_text1_btn(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://study.wooyoung.site/")
    time.sleep(1)
    page.get_by_text("Text1").click()
    time.sleep(1)

    browser.close()

def test_has_text1_btn(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://study.wooyoung.site/")
    time.sleep(1)
    page.locator('button',has_text="Text1").click()
    time.sleep(1)

    browser.close()

def test_placeholder_input(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://study.wooyoung.site/")
    time.sleep(1)
    page.get_by_placeholder('설명!').click()
    time.sleep(1)

    browser.close()