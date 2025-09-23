from playwright.sync_api import  sync_playwright, expect
import time
import pytest

from chapter3.login import login
from chapter3.test_jeongsu import test_go_to_store_page
from chapter3.test_jinsol import test_generate_order_from
from chapter3.test_onyu import test_frommpay
'''
온유 : frommpay 등록
정수 : bff 찾아가기
진솔 : 주문서 작성
'''

def test_buy_bff(playwright: sync_playwright):
    # page = login(playwright,'it.test+UWXiGP@wonderwall.kr')
    # page = login(playwright,'it.test+RySGAG@wonderwall.kr')
    page = login(playwright,'it.test+pW9z4J@wonderwall.kr')
    test_frommpay(page,000000)
    fromm_store_logo = page.get_by_role('link', name='FROMM STORE')
    fromm_store_logo.click()
    test_go_to_store_page(page)
    test_generate_order_from(page)

    complete_msg = page.locator('b', has_text=f'정상적으로 완료')
    expect(complete_msg).to_be_visible(timeout=10000)

    go_product_btn = page.locator('div[role="button"]>span', has_text='쇼핑 계속하기')
    go_product_btn.click()

    header = page.locator('header')
    menu_btn = header.get_by_role('button', name='전체메뉴')
    menu_btn.click()

    subscribe_menu_btn = page.locator('a[href="/subscribe"]')
    subscribe_menu_btn.click()

    max_reload_count = 3
    arti_name = "QA 4인 그룹 아티1-ko"
    target = page.get_by_text(arti_name, exact=True)
    for i in range(max_reload_count):
        try:
            expect(target).to_be_visible(timeout=3000)
            return
        except Exception as _:
            if i < max_reload_count - 1:
                page.reload()
                page.wait_for_timeout(1000)
            else:
                raise Exception(f"최대 {max_reload_count}회 새로고침 후에도 '{arti_name}' 안 보임") from None
