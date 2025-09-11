from playwright.sync_api import sync_playwright, Playwright
import time
import pytest

from chapter3.login import login


def test_go_to_store_page(playwright: Playwright):
    page = login(playwright)

    page.fill('input[placeholder="아티스트명 검색"]', '4인')
    time.sleep(3)
    page.locator('img[alt="QA 4인 그룹 아티관-ko"]').click()
    time.sleep(3)

    target = page.get_by_text("QA 4인 그룹1 베프친 갱신 굿즈")

    # 3. 타겟이 보일 때까지 스크롤 내리기
    scroll_attempts = 0
    max_scrolls = 20
    scroll_step = 500

    while not target.is_visible():
        if scroll_attempts >= max_scrolls:
            pytest.fail("굿즈를 찾을 수 없습니다 (스크롤 최대 횟수 초과)")
            break

        page.mouse.wheel(0, scroll_step)
        scroll_attempts += 1

    # 4. 굿즈 클릭 (화면에 보이게 강제 후 클릭)
    target.scroll_into_view_if_needed()
    target.click()

    page.get_by_text("구매하기").click()
    time.sleep(7)

