import time

import pytest
from playwright.sync_api import Playwright, Page, Locator, expect

from chapter3.login import login


# 해당 요소의 다음 요소를 가져오는 함수
def get_next_element(target,step:str="1"):
    return target.locator("xpath=following-sibling::*["+step+"]")

def scroll_until_visible_target(driver:Page,target:Locator,step:int = 100,timeout:int = 200):
    prev_scroll = 0
    text = driver.get_by_text("전체 상품")
    text_container = get_next_element(text.locator('..'))
    driver.wait_for_load_state('domcontentloaded')

    timeout_sec = 60

    deadline = time.monotonic() + timeout_sec

    while time.monotonic() < deadline:
        scroll_height = driver.evaluate("(el) => el.scrollHeight",text_container.element_handle())
        if scroll_height < 900:
            scroll_height = 900
        if target.is_visible():
            break
        elif prev_scroll >= scroll_height+100:
            pytest.fail("페이지 끝까지 내렸지만 요소가 없음")
            break
        else:
            driver.mouse.wheel(0, step)
            driver.wait_for_timeout(timeout)
            prev_scroll += step

def test_generate_order_from(page:Page):
    '''
    # arti_name:str = "에스파ko 아티관"
    # bff_name:str = "윈터 12개월 BFF(갱신O) 최대 1개 구매 가능"
    # buy_btn_text:str = "구매하기"

    # page:Page = login(playwright)

    # 굿즈 찾아가기
    # search_arti_input=page.locator('input[placeholder="아티스트명 검색"]')
    # search_arti_input.type(arti_name)
    #
    # arti_profile = page.locator('img[alt="' + arti_name + '"]')
    # expect(arti_profile).to_be_visible()
    #
    # # 아티관 클릭
    # arti_profile = page.locator('img[alt="' + arti_name + '"]')
    # arti_profile.click()
    #
    # arti_name_text = page.get_by_role("link", name=arti_name, exact=True)
    # expect(arti_name_text).to_be_visible()
    # expect(arti_name_text).to_have_text(arti_name)
    #
    # # BFF 찾아가기
    # target_goods = page.locator('a>div>div',has_text=bff_name)
    # scroll_until_visible_target(page,target_goods)
    #
    # # BFF 클릭
    # goods = page.locator('div[role="listitem"]>a>div',has_text=bff_name)
    # goods.click()
    # page.wait_for_load_state('load')
    #
    # # BFF 구매하기
    # buy_btn = page.locator('div[role="button"]',has_text=buy_btn_text)
    # expect(buy_btn).to_be_enabled(timeout=20000)
    # buy_btn.click()
    # time.sleep(1)
    '''
    # 주문자 정보 입력
    purchase_button = page.locator('#purchase_button>div')
    expect(purchase_button).to_be_disabled(timeout=10000)

    purchaser_area = page.locator('section[aria-labelledby="order-customer-info-title"]')

    purchaser_name_placeholder = '주문자 정보를 입력해 주세요'
    purchaser_phone_number_placeholder = '휴대전화를 입력해 주세요'
    purchaser_birth_placeholder = '생년월일 (YYYYMMDD)을 입력해 주세요'

    purchaser_name = purchaser_area.locator('input[placeholder="' + purchaser_name_placeholder + '"]')
    purchaser_name.type('테스터')

    purchaser_phone_number = purchaser_area.locator('input[placeholder="' + purchaser_phone_number_placeholder + '"]')
    purchaser_phone_number.type('01000000000')

    purchaser_birth = purchaser_area.locator('input[placeholder="' + purchaser_birth_placeholder + '"]')
    purchaser_birth.type('00000101')

    # 약관 동의
    all_agree_terms_text = '모두 확인 및 동의합니다.'
    all_agree_title = page.locator('p', has_text=all_agree_terms_text)
    all_agree_div = all_agree_title.locator('..')
    all_agree_btn = all_agree_div.locator('svg')
    all_agree_btn.click()

    # 구매하기
    purchase_button = page.locator('#purchase_button>div')
    expect(purchase_button).to_be_enabled()

    purchase_button.click()

    title = page.locator('h3', has_text="비밀번호 입력")
    expect(title).to_be_visible()

    num_0_btn = page.locator("div[data-value='0']")
    for _ in range(6):
        num_0_btn.click()
        time.sleep(0.3)

    time.sleep(10)