from playwright.sync_api import  sync_playwright, expect,Page
import time
import pytest

from chapter3.login import login


def test_go_to_store_page(page:Page):
    # page = login(playwright)
    """
    fix code format
        before: page.fill('input[placeholder="아티스트명 검색"]', '4인')
        after : page.locator('input[placeholder="아티스트명 검색"]').fill('4인')
    """
    page.locator('input[placeholder="아티스트명 검색"]').fill('4인')

    page.locator('img[alt="QA 4인 그룹 아티관-ko"]').click()

    """
    added exact=True in target locator
        "QA 4인 그룹1 베프친 갱신 굿즈2"와 같은 굿즈가 존재할 수 있기 때문에 exact=True 추가
    """
    target = page.get_by_text("QA 4인 그룹1 베프친 갱신 굿즈",exact=True)

    # 3. 타겟이 보일 때까지 스크롤 내리기
    scroll_attempts = 0
    max_scrolls = 20
    scroll_step = 100

    """
    prevent while loop from running before page load
        페이지가 로드 되기 전 부터 while문이 실행되고 있어 
        scroll_attempts >= max_scrolls"이 정상적으로 작동하지 않음
        전체 상품" text가 viewport 안에 나타나면 그때부터 스크롤 하도록 수정
    """
    expect(page.get_by_text('전체 상품')).to_be_in_viewport()

    while not target.is_visible():
        if scroll_attempts >= max_scrolls:
                pytest.fail("굿즈를 찾을 수 없습니다 (스크롤 최대 횟수 초과)")
                break

        page.mouse.wheel(0, scroll_step)
        scroll_attempts += 1

        """
        safe scrolling in while loop
            스크롤이 추가로 생성되기 전에 계속 스크롤링을 해서 0.1초동안 대기하도록 추가
        """
        time.sleep(0.1)

    # 4. 굿즈 클릭 (화면에 보이게 강제 후 클릭)
    """
    added scroll_into_view_if_needed description
        scroll_into_view_if_needed 란?
        요소가 존재하지만 viewport 안에는 보이고 있지 않을때 viewport 안에 보이도록 해줌
        e.g: 스크롤을 해서 하단에 요소가 생겼는데 반만 보이고 있을때 화면 안에 보이도록 해줌
        만약 요소가 존재하지 않는다면 timeout:float=30 초 이후에 Playwright TimeoutException 발생
    """
    target.scroll_into_view_if_needed()
    target.click()

    page.get_by_text("구매하기").click()


