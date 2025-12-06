import os
import time
import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="session")
def session_fixture():
    print("\nsession fixture setup")
    yield
    print("session fixture teardown")


@pytest.fixture(scope="package")
def package_fixture(session_fixture):
    print("package fixture setup")
    yield
    print("package fixture teardown")

@pytest.fixture(scope="module")
def module_fixture(package_fixture):
    print("module fixture setup")
    yield
    print("module fixture teardown")


@pytest.fixture(scope="class")
def class_fixture(module_fixture):
    print("class fixture setup")
    yield
    print("class fixture teardown")


@pytest.fixture(scope="function")
def function_fixture(class_fixture):
    print("function fixture setup")
    yield
    print("\nfunction fixture teardown")

@pytest.fixture
def function_page(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    Base_URL = os.getenv(
        "BASE_URL",
        "https://blue-ground-0e078e000.3.azurestaticapps.net",  # 기본값
    )
    page.goto(Base_URL)
    yield page
    browser.close()
def do_login(context, cookie_path: str):
    page = context.new_page()
    page.goto("https://store-qa.frommyarti.com/arti")

    page.wait_for_url("https://store-qa.frommyarti.com/arti")
    page.wait_for_load_state('networkidle')


    menu_name = '전체메뉴'

    header = page.locator('header')
    menu_btn = header.get_by_role('button', name=menu_name)
    menu_btn.click()

    move_login_page_btn = page.locator('a', has_text='로그인 후 이용해주세요.')
    move_login_page_btn.click()

    id_input = page.locator("input[placeholder='example@email.com']")
    id_input.type("it.test+VHWyBU@wonderwall.kr")

    pw_input = page.locator("input[placeholder='비밀번호']")
    pw_input.type("qwer1234!")

    login_btn = page.locator('span', has_text='로그인')
    login_btn.click()

    time.sleep(10)
    context.storage_state(path=cookie_path)

    return context
@pytest.fixture(scope="session")
def session_store_page(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    do_login(context, 'cookie.json')

    context.close()
    browser.close()

    yield 'cookie.json'


@pytest.fixture
def function_store_page(playwright:Playwright,session_store_page):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=session_store_page)
    page = context.new_page()

    page.goto("https://store-qa.frommyarti.com/arti")
    yield page
    browser.close()