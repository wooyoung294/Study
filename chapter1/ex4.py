import time

from playwright.sync_api import Page
# pytest chapter1/ex4.py::test_login --headed <- Playwright는 기본적으로 headless여서 해당 명령어로 실행
def test_login(page: Page):
    # 프로 스토어 접속
    page.goto("https://store.frommyarti.com/arti")

    # 더보기 메뉴 클릭
    menu=page.locator('img[alt="전체메뉴"]')
    menu.click()

    # "로그인 후 이용해주세요." 문구 클릭
    log_in=page.locator('a[href="/signin"]')
    log_in.click()

    # 화면 보여주기 위해서 time.sleep 제거 해도 통과함
    time.sleep(3)