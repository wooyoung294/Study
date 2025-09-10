
from playwright.sync_api import Playwright, Page, expect
def login(playwright:Playwright,_id:str = "it.test+GL2n0U@wonderwall.kr", _pass:str = "qwer1234!")-> Page:
    """
    QA 환경 store로 접속 후 로그인을 진행합니다.

    Args:
        playwright (Playwright) : Playwright 객체
        _id (str, optional) : 로그인 Id
        _pass (str, optional): 로그인 Password
    Returns:
        Page
    """

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 900})
    page:Page = context.new_page()

    page.goto("https://store-qa.frommyarti.com/arti")

    page.wait_for_load_state('load')

    # 로그인
    menu=page.locator('img[alt="전체메뉴"]')
    menu.click()

    log_in=page.locator('a[href="/signin"]')
    log_in.click()

    login_title=page.locator("h2",has_text="로그인")
    expect(login_title).to_be_visible()

    id_input = page.locator("input[placeholder='example@email.com']")
    id_input.type(_id)

    pw_input = page.locator("input[placeholder='비밀번호']")
    pw_input.type(_pass)

    login_btn=page.locator("span",has_text="로그인")
    login_btn.click()

    return page