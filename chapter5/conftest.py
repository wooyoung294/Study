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

    page.goto("https://study.wooyoung.site/")
    yield page
    browser.close()

