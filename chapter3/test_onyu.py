from playwright.sync_api import Playwright, Page, Locator

from chapter3.login import login, expect
import time

# TODO:type your_function_name_plz
def test_frommpay(playwright:Playwright):
    fromm_store_page:Page = login(playwright, "onyu.park+38@wonderwall.kr", "1234asdf")

    # 파이썬의 경우에는 snake_case 를 사용하도록 권장합니다! allMenu(camelCase) -> all_menu(snake_case)
    all_menu:Locator = fromm_store_page.locator('img[alt="전체메뉴"]') #더보기 클릭
    all_menu.click()

    menu_frommpay = fromm_store_page.locator('a[href="/auto-pay"]') #프롬페이 클릭
    menu_frommpay.click()

    fromm_store_page.get_by_text("프롬페이 추가").click() #나중에 바꾸기

    # fromm_store_page.get_by_role("button", name="등록하기", exact=True).click()
    # fromm_store_page.locator('div[role="button"]', has_text="등록하기").click()
    # fromm_store_page.locator('div>span', has_text="등록하기").click()

    # role을 추가해서 조금 더 안정적이도록
    fromm_store_page.locator('div[role="button"]>span',has_text="등록하기").click() #등록하기 클릭
    time.sleep(3)

    # toss_page = fromm_store_page.frame("#__tosspayments_payment-gateway_iframe__")
    # toss_page = fromm_store_page.frame(name="__tosspayments_payment-gateway_iframe__")
    # toss_page = fromm_store_page.frame_locator('iFrame').locator('input[id="radix-:r2:"]')
    # toss_page = fromm_store_page.frame_locator('iFrame')
    toss_page = fromm_store_page.wait_for_selector("iframe[title='토스페이먼츠 전자결제']").content_frame()
    toss_page.locator('input[id="radix-:r2:"]').type("4854")
    toss_page.locator('input[id="radix-:r3:"]').type("6200")
    toss_page.locator('input[id="radix-:r4:"]').type("9334")
    toss_page.locator('input[id="radix-:r5:"]').type("0000") #카드번호 입력
    time.sleep(1)
    # card_number_input4 = toss_page.locator('input[aria-label="카드번호 13 ~ 16 자리"]')
    # card_number_input4.type("0000")

    toss_page.locator('input[id="radix-:r6:"]').type("0729") #유효기간 입력
    time.sleep(1)

    toss_page.locator('input[id="radix-:r7:"]').click() #필수 동의 클릭
    time.sleep(1)

    toss_page.locator('button[type="submit"]').click() #다음 버튼 클릭
    time.sleep(1)

    toss_page.locator('input[id="radix-:r9:"]').type("프막내") #이름 입력
    time.sleep(1)

    toss_page.locator('input[id="radix-:ra:"]').type("010101") #주민번호 앞자리 입력

    toss_page.locator('input[id="radix-:rb:"]').type("4") #주민번호 뒷자리 입력
    time.sleep(1)

    # toss_page.locator('button[type="button"]>span', has_text="선택").click()
    toss_page.locator('button[aria-label="통신사 선택"]').click() #통신사 드롭다운 클릭
    time.sleep(1)

    toss_page.locator('div[aria-label="KT"]').click() #KT 클릭
    time.sleep(1)

    # phone_number_input = toss_page.locator('input[id="radix-:rf:"][name="phoneNumber"]')
    # phone_number_input = toss_page.locator('#radix-:rf:')
    phone_number_input = toss_page.locator('input[id="radix-:rf:"]')#휴대폰번호 입력필드
    phone_number_input.type("01012345678")
    time.sleep(1)

    toss_page.locator('button[aria-label="인증번호 받기"]').click() #인증번호 받기 버튼 클릭
    time.sleep(1)

    toss_page.locator('input[id="radix-:rm:"]').type("000000") #인증번호 입력
    time.sleep(1)

    toss_page.locator('button[aria-label="확인"]').click() #확인버튼 클릭

    pw_activity_title = fromm_store_page.locator('h3[id="password-activity-title"]')
    expect(pw_activity_title).to_have_text("결제 비밀번호 입력")

    pw_frommpay_num1 = fromm_store_page.locator('div[role="button"][data-value="1"]')
    pw_frommpay_num2 = fromm_store_page.locator('div[role="button"][data-value="2"]')
    pw_frommpay_num3 = fromm_store_page.locator('div[role="button"][data-value="3"]')
    pw_frommpay_num4 = fromm_store_page.locator('div[role="button"][data-value="4"]')
    pw_frommpay_num5 = fromm_store_page.locator('div[role="button"][data-value="5"]')
    pw_frommpay_num6 = fromm_store_page.locator('div[role="button"][data-value="6"]')
    pw_frommpay_num1.click()
    pw_frommpay_num2.click()
    pw_frommpay_num3.click()
    pw_frommpay_num4.click()
    pw_frommpay_num5.click()
    pw_frommpay_num6.click() #비밀번호 설정 123456
    time.sleep(1)

    expect(pw_activity_title).to_have_text("결제 비밀번호 재입력")
    pw_frommpay_num1.click()
    pw_frommpay_num2.click()
    pw_frommpay_num3.click()
    pw_frommpay_num4.click()
    pw_frommpay_num5.click()
    pw_frommpay_num6.click() #비밀번호 재입력 123456
    time.sleep(1)

    pw_frommpay_finish_parent = fromm_store_page.locator('div',has_text="결제 비밀번호")
    pw_frommpay_finish_child = pw_frommpay_finish_parent.locator('div[data-setted="true"]')
    expect(pw_frommpay_finish_child).to_have_text("설정완료")


    time.sleep(2)
    # toss_page.locator('input[id="radix-:r2:"]').type("4854")

    time.sleep(3)










