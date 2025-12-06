import time

from playwright.sync_api import Playwright

def test_your_case(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # page.goto(Base_URL)

    # Your Code
    # page.locator('#idBtn').click()
    # time.sleep(3)
    # browser.close()

    # page.locator('button[name="nameBtn"]').click()
    # time.sleep(3)
    # browser.close()

    page.goto("https://store.frommyarti.com/")

    page.locator('img[alt="전체메뉴"]').click()
    time.sleep(3)
    # page.locator("a", has_text="로그인 후 이용해주세요.").click()
    page.get_by_text("로그인 후 이용해주세요.").click()
    time.sleep(3)
