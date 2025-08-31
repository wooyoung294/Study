from playwright.sync_api import Playwright

def test_your_case(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://study.wooyoung.site/")

    # Your Code

    browser.close()
