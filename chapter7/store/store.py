import json
import os
import time

import allure
from playwright.sync_api import Error as PlaywrightError, Page, expect
from pytest_bdd import given, parsers, when, then

from chapter3.test_jinsol import scroll_until_visible_target


@when('Store_더보기 [☰] 버튼 클릭')
@allure.step('Store_더보기 [☰] 버튼 클릭')
def click_menu(web_function_driver: Page, api_store):
    menu_name = None
    if api_store['now_lang'] == 'KO':
        menu_name = '전체메뉴'
    elif api_store['now_lang'] == 'ZH':
        menu_name = '全部菜单'
    elif api_store['now_lang'] == 'EN':
        menu_name = 'Main Menu'
    elif api_store['now_lang'] == 'JA':
        menu_name = '全体メニュー'
    header = web_function_driver.locator('header')
    menu_btn = header.get_by_role('button', name=menu_name)
    menu_btn.click()
    time.sleep(1)

@then('Store_더보기 페이지 노출')
@allure.step('Store_더보기 페이지 노출')
def show_menu_page(web_function_driver: Page):
    expect(web_function_driver.locator('a[href="/order/list"]', has_text='주문 / 배송조회')).to_be_visible()
    expect(web_function_driver.locator('a[href="/auto-pay"]', has_text='프롬페이')).to_be_visible()
    expect(web_function_driver.locator('a[href="/auto-pay"]', has_text='프롬페이')).to_be_visible()
    expect(web_function_driver.locator('a[href="/subscribe"]', has_text='구독관리')).to_be_visible()
    expect(web_function_driver.locator('a[href="/memberships"]', has_text='멤버십')).to_be_visible()

@when('Store_[로그인 후 이용해주세요.] 항목 클릭')
@allure.step('Store_[로그인 후 이용해주세요.] 항목 클릭')
def click_login_text(web_function_driver: Page):
    # delete_pay_success_yopmail(web_function_driver,worker_id)
    move_login_page_btn = web_function_driver.locator('a', has_text='로그인 후 이용해주세요.')
    move_login_page_btn.click()
@then('Store_로그인 페이지 노출')
@allure.step('Store_로그인 페이지 노출')
def show_login_page(web_function_driver: Page):
    login_title = web_function_driver.locator('h2', has_text='로그인')
    expect(login_title).to_be_visible()

@then(parsers.parse('Store_[로그인] 버튼 {status} 상태로 노출'))
@allure.step('Store_[로그인] 버튼 {status} 상태로 노출')
def is_login_btn_enabled(web_function_driver: Page, status: str):
    login_btn = web_function_driver.locator('span', has_text='로그인')
    if status == '비활성화':
        expect(login_btn).to_be_disabled()
    elif status == '활성화':
        expect(login_btn).not_to_be_disabled()
@when(parsers.parse('Store_아이디 입력필드 클릭'))
@allure.step('Store_아이디 입력필드 클릭')
def click_login_id_input(web_function_driver: Page):
    id_input = web_function_driver.locator("input[placeholder='example@email.com']")
    id_input.click()

@when('Store_유효한 아이디 입력')
@allure.step('Store_유효한 아이디 입력')
def type_login_id(web_function_driver: Page):
    id_input = web_function_driver.locator("input[placeholder='example@email.com']")
    id_input.type(os.getenv('STORE_ID'))

@when('Store_비밀번호 입력필드 클릭')
@allure.step('Store_비밀번호 입력필드 클릭')
def click_login_pw_input(web_function_driver: Page):
    pw_input = web_function_driver.locator("input[placeholder='비밀번호']")
    pw_input.click()


@when('Store_올바른 비밀번호 입력')
@allure.step('Store_올바른 비밀번호 입력')
def type_login_pw(web_function_driver: Page):
    pw_input = web_function_driver.locator("input[placeholder='비밀번호']")
    pw_input.type('qwer1234!')
def get_api_response(driver: Page, action, url, key, api_store):
    with driver.expect_response(
            lambda res: res.url.split('?')[0].endswith(url) and res.request.method.upper() != 'HEAD'
    ) as r:
        action()

    response = r.value

    if response.ok:
        try:
            api_store[key] = response.json()
        # EmptyBody
        except PlaywrightError as error:
            if 'No resource with given identifier found' in str(error):
                api_store[key] = {}
                return 0
            raise
@when('Store_[로그인] 버튼 클릭')
@allure.step('Store_[로그인] 버튼 클릭')
def click_login_btn(web_function_driver: Page, api_store):
    login_btn = web_function_driver.locator('span', has_text='로그인')

    get_api_response(web_function_driver, lambda: login_btn.click(), '/auth/signIn', 'signIn', api_store)

    assert (api_store['signIn']['code']) == 200

@then(parsers.parse('Store_{case} 아이디 노출'))
@allure.step('Store_{case} 아이디 노출')
def show_login_id(web_function_driver: Page, case: str):
    if case == '로그인한':
        expect(web_function_driver.get_by_text(os.getenv('STORE_ID'))).to_be_visible()
    elif case == '회원가입한':
        expect(web_function_driver.get_by_text(os.getenv('STORE_ID'))).to_be_visible()
        # add_id_in_white_list(web_function_driver)
    time.sleep(1)


@given('Store_더보기 페이지 헤더 닫기 [X] 버튼 클릭')
@allure.step('Store_더보기 페이지 헤더 닫기 [X] 버튼 클릭')
def closed_header_menu(web_function_driver: Page):
    close_btn = web_function_driver.locator('div[aria-label="닫기"]')
    close_btn.click()

@given('Store_로그인 되어있는 상태')
@allure.step('Store_로그인 되어있는 상태')
def store_login_state(web_function_driver, api_store):
    click_menu(web_function_driver, api_store)
    show_menu_page(web_function_driver)
    click_login_text(web_function_driver)
    show_login_page(web_function_driver)
    is_login_btn_enabled(web_function_driver, '비활성화')
    click_login_id_input(web_function_driver)
    type_login_id(web_function_driver)
    click_login_pw_input(web_function_driver)
    type_login_pw(web_function_driver)
    is_login_btn_enabled(web_function_driver, '활성화')
    click_login_btn(web_function_driver, api_store)
    click_menu(web_function_driver, api_store)
    show_menu_page(web_function_driver)
    show_login_id(web_function_driver, '로그인한')
    closed_header_menu(web_function_driver)



@when('Store_[구독관리] 항목 클릭')
@allure.step('Store_[구독관리] 항목 클릭')
def click_subscribe_menu_btn(web_function_driver: Page):
    subscribe_menu_btn = web_function_driver.locator('a[href="/subscribe"]')
    subscribe_menu_btn.click()

@then(parsers.parse('Store_구독 내역 페이지 내 "{arti_name}" 이용권 노출'))
@allure.step('Store_구독 내역 페이지 내 "{arti_name}" 이용권 노출')
def show_bff_arti_name(web_function_driver: Page, arti_name: str):
    max_reload_count = 3
    target = web_function_driver.get_by_text(arti_name, exact=True)
    for i in range(max_reload_count):
        try:
            expect(target).to_be_visible(timeout=3000)
            return
        except Exception as _:
            if i < max_reload_count - 1:
                web_function_driver.reload()
                web_function_driver.wait_for_timeout(1000)
            else:
                raise Exception(f"최대 {max_reload_count}회 새로고침 후에도 '{arti_name}' 안 보임") from None


@when(parsers.parse('Store_"{arti_name}" 아티관 검색'))
@allure.step('Store_"{arti_name}" 아티관 검색')
def search_arti(web_function_driver: Page, arti_name: str):
    search_arti_input = web_function_driver.locator('input[placeholder="아티스트명 검색"]')
    search_arti_input.type(arti_name)

    arti_profile = web_function_driver.locator('img[alt="' + arti_name + '"]')
    expect(arti_profile).to_be_visible()


@when(parsers.parse('Store_검색 결과에서 "{arti_name}" 아티관 클릭'))
@allure.step('Store_검색 결과에서 "{arti_name}" 아티관 클릭')
def click_searched_arti_profile(web_function_driver: Page, arti_name: str):
    arti_profile = web_function_driver.locator('img[alt="' + arti_name + '"]')
    arti_profile.click()


@when(parsers.parse('Store_"{goods_name}" 상품 클릭'))
@allure.step('Store_"{goods_name}" 상품 클릭')
def click_goods_item(web_function_driver: Page, goods_name: str):
    goods = web_function_driver.locator('div[role="listitem"]>a>div', has_text=goods_name)
    goods.click()
    web_function_driver.wait_for_load_state('load')
@when(parsers.parse('Store_"{goods_name}" 상품 보일때 까지 스크롤'))
@allure.step('Store_"{goods_name}" 상품 보일때 까지 스크롤')
def scroll_until_goods_visible(web_function_driver: Page, goods_name: str):
    target_goods = web_function_driver.locator('a>div>div', has_text=goods_name)
    scroll_until_visible_target(web_function_driver, target_goods)

@when(parsers.parse('Store_상품 상세 페이지 내 [{btn_text}] 버튼 클릭'))
@allure.step('Store_상품 상세 페이지 내 [{btn_text}] 버튼 클릭')
def click_goods_buy_btn(web_function_driver: Page, btn_text: str):
    buy_btn = web_function_driver.locator('div[role="button"]', has_text=btn_text)
    expect(buy_btn).to_be_enabled(timeout=20000)
    buy_btn.click()

@when('Store_주문서 작성/결제 페이지 내 주문자 정보 입력')
@allure.step('Store_주문서 작성/결제 페이지 내 주문자 정보 입력')
def type_goods_purchaser_info(web_function_driver: Page, api_store):
    purchase_button = web_function_driver.locator('#purchase_button>div')
    expect(purchase_button).to_be_disabled(timeout=10000)

    purchaser_area = web_function_driver.locator('section[aria-labelledby="order-customer-info-title"]')

    purchaser_name_placeholder = None
    purchaser_phone_number_placeholder = None
    purchaser_birth_placeholder = None
    # 한국어 일 때
    if api_store['now_lang'] == 'KO':
        purchaser_name_placeholder = '주문자 정보를 입력해 주세요'
        purchaser_phone_number_placeholder = '휴대전화를 입력해 주세요'
        purchaser_birth_placeholder = '생년월일 (YYYYMMDD)을 입력해 주세요'

    elif api_store['now_lang'] == 'ZH':
        purchaser_name_placeholder = '请输入购买人信息'
        purchaser_phone_number_placeholder = '请输入手机号码'
        purchaser_birth_placeholder = '请输入出生日期(YYYYMMDD)'

    if 'now_currency' not in api_store:
        purchaser_name = purchaser_area.locator('input[placeholder="' + purchaser_name_placeholder + '"]')
        purchaser_name.type('테스터')
    elif api_store['now_currency'] == 'USD':
        purchaser_last_name = purchaser_area.locator('input[placeholder="성을 입력해 주세요"]')
        purchaser_name = purchaser_area.locator('input[placeholder="이름을 입력해 주세요"]')
        purchaser_last_name.type('테')
        purchaser_name.type('스터')

    purchaser_phone_number = purchaser_area.locator('input[placeholder="' + purchaser_phone_number_placeholder + '"]')
    purchaser_phone_number.type('01000000000')

    purchaser_birth = purchaser_area.locator('input[placeholder="' + purchaser_birth_placeholder + '"]')
    purchaser_birth.type('00000101')


@when('Store_주문서 작성/결제 페이지 내 약관 모두 동의')
@allure.step('Store_주문서 작성/결제 페이지 내 약관 모두 동의')
def type_goods_all_agree_terms(web_function_driver: Page, api_store):
    all_agree_terms_text = None
    if api_store['now_lang'] == 'KO':
        all_agree_terms_text = '모두 확인 및 동의합니다.'
    elif api_store['now_lang'] == 'ZH':
        all_agree_terms_text = '全部确认并同意。'
    all_agree_title = web_function_driver.locator('p', has_text=all_agree_terms_text)
    all_agree_div = all_agree_title.locator('..')
    all_agree_btn = all_agree_div.locator('svg')
    all_agree_btn.click()

    time.sleep(3)


def click_purchase_button(driver: Page):
    purchase_button = driver.locator('#purchase_button>div')
    expect(purchase_button).to_be_enabled()

    purchase_button.click()


@when(
    parsers.parse('Store_프롬페이 결제 {text} 페이지에서 결제 비밀번호 입력')
)
@allure.step('Store_프롬페이 결제 {text} 페이지에서 결제 비밀번호 입력')
def type_payment_password(web_function_driver: Page, text: str):
    title = web_function_driver.locator('h3', has_text=text)
    expect(title).to_be_visible()

    num_0_btn = web_function_driver.locator("div[data-value='0']")
    for _ in range(6):
        num_0_btn.click()
        time.sleep(0.3)
@then(parsers.parse('Store_주문 {state}페이지 노출'))
@allure.step('Store_주문 {state}페이지 노출')
def show_goods_order_complete_page(web_function_driver: Page, state):
    complete_msg = web_function_driver.locator('b', has_text=f'정상적으로 {state}')
    expect(complete_msg).to_be_visible(timeout=10000)

    go_product_btn = web_function_driver.locator('div[role="button"]>span', has_text='쇼핑 계속하기')
    go_product_btn.click()

def store_subscribe_impl(web_function_driver, arti_store, target_name, goods_name, api_store):
    try:
        click_menu(web_function_driver, api_store)
        click_subscribe_menu_btn(web_function_driver)
        show_bff_arti_name(web_function_driver, target_name)
    except Exception as _:
        web_function_driver.goto(os.getenv('URL'))
        search_arti(web_function_driver, arti_store)
        click_searched_arti_profile(web_function_driver, arti_store)
        scroll_until_goods_visible(web_function_driver, goods_name)
        click_goods_item(web_function_driver, goods_name)
        click_goods_buy_btn(web_function_driver, '구매하기')
        type_goods_purchaser_info(web_function_driver, api_store)
        type_goods_all_agree_terms(web_function_driver, api_store)
        click_purchase_button(web_function_driver)
        type_payment_password(web_function_driver, '비밀번호 입력')
        show_goods_order_complete_page(web_function_driver, '완료')
        web_function_driver.evaluate("window.localStorage.removeItem('recentArtiPath');")
        # assert web_function_driver.evaluate("window.localStorage.getItem('recentArtiPath')")
    finally:
        web_function_driver.goto(os.getenv('URL'))


@given(parsers.parse('Store_"{arti_store}" 아티관 아티명 "{arti_name}"의 "{goods_name}"을 구독한 상태'))
def store_subscribe_arti_state(web_function_driver, arti_store, arti_name, goods_name, api_store):
    store_subscribe_impl(web_function_driver, arti_store, arti_name, goods_name, api_store)
