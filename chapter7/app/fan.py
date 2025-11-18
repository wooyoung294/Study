import os

import allure
from appium.webdriver.webdriver import WebDriver
import pytest
from pytest_bdd import given, then, when,parsers

from chapter7.utils import wait_for_element, AppiumExpect as AE, compare_elements_similarity


@given('FanApp_로그인 버튼 클릭')
@allure.step('FanApp_로그인 버튼 클릭')
def click_login_btn(fan_app_session_driver: WebDriver, fan_app_function_driver: WebDriver):
    login_btn = wait_for_element(fan_app_session_driver, 'ID', 'com.knowmerce.fromm.fan:id/btn_signIn')
    login_btn.click()


@then('FanApp_"fromm 통합 ID를 입력해주세요." 문구 노출')
@allure.step('FanApp_"fromm 통합 ID를 입력해주세요." 문구 노출')
def fan_app_show_id_text(fan_app_session_driver):
    AE(fan_app_session_driver).to_have_text('fromm 통합 ID를\n입력해주세요.')


@when('FanApp_ID 입력')
@allure.step('FanApp_ID 입력')
def type_login_id(fan_app_session_driver: WebDriver):
    id_input = wait_for_element(fan_app_session_driver, 'ID', 'com.knowmerce.fromm.fan:id/dib_edit_text')
    id_input.send_keys(os.getenv('STORE_ID'))
    # id_input.send_keys("it.test+utJC0m@wonderwall.kr")

    id_ok_btn = wait_for_element(fan_app_session_driver, 'ID', 'com.knowmerce.fromm.fan:id/btn_ok')
    id_ok_btn.click()


@then('FanApp_"비밀번호를 입력해주세요." 문구 노출')
@allure.step('FanApp_"비밀번호를 입력해주세요." 문구 노출')
def fan_app_show_pw_text(fan_app_session_driver):
    AE(fan_app_session_driver).to_have_text('비밀번호를\n입력해 주세요.')


@when('FanApp_PW 입력')
@allure.step('FanApp_PW 입력')
def type_login_pw(fan_app_session_driver: WebDriver):
    password_input = wait_for_element(fan_app_session_driver, 'ID', 'com.knowmerce.fromm.fan:id/dib_edit_text')
    password_input.send_keys(os.getenv('STORE_PW'))

    password_ok_btn = wait_for_element(fan_app_session_driver, 'ID', 'com.knowmerce.fromm.fan:id/btn_ok')
    password_ok_btn.click()


@when('FanApp_알림 허용')
@allure.step('FanApp_알림 허용')
def allow_alarm(fan_app_session_driver: WebDriver):
    allow_alarm_btn = wait_for_element(
        fan_app_session_driver, 'ID', 'com.android.permissioncontroller:id/permission_allow_button'
    )
    allow_alarm_btn.click()


@then('FanApp_"알림 수신 설정" 팝업 노출')
@allure.step('FanApp_"알림 수신 설정" 팝업 노출')
@pytest.mark.xfail(strict=False)
def fan_app_show_battery_popup(fan_app_session_driver):
    try:
        AE(fan_app_session_driver).to_have_text('알림 수신 설정')
    except AssertionError:
        # 실패해도 계속 진행
        pass


@when('FanApp_알림 수신 설정 팝업 닫기')
@allure.step('FanApp_알림 수신 설정 팝업 닫기')
@pytest.mark.xfail(strict=False)
def battery_popup_close(fan_app_session_driver: WebDriver):
    try:
        alert_close_btn = wait_for_element(
            fan_app_session_driver, 'UIAUTOMATOR', 'new UiSelector().className("android.widget.Button").instance(0)'
        )
        alert_close_btn.click()
    except Exception:
        # 버튼을 찾지 못하거나 클릭할 수 없어도 계속 진행
        pass

@given(parsers.parse('FanApp_목록페이지 Best프롬친구 목록에서 "{arti_name}" 아티 클릭'))
@allure.step('FanApp_목록페이지 Best프롬친구 목록에서 "{arti_name}" 아티 클릭')
def click_target_arti(fan_app_session_driver, arti_name):
    target_arti = wait_for_element(fan_app_session_driver, 'UIAUTOMATOR', 'new UiSelector().text("' + arti_name + '")')
    target_arti.click()


@when('FanApp_아티 프로필 페이지 내 [1:1 대화하기] 버튼 클릭')
@allure.step('FanApp_아티 프로필 페이지 내 [1:1 대화하기] 버튼 클릭')
def click_one_on_one_chat_btn(fan_app_session_driver):
    target = wait_for_element(fan_app_session_driver, 'UIAUTOMATOR', 'new UiSelector().text("1:1 대화하기")')
    target.click()



@then('FanApp_이모티콘 온보딩 화면 내 "이모티콘을 전송해 보세요!" 문구 노출')
@allure.step('FanApp_이모티콘 온보딩 화면 내 "이모티콘을 전송해 보세요!" 문구 노출')
def show_launching_emoticon_text(fan_app_session_driver):
    AE(fan_app_session_driver).to_have_text('이모티콘을 전송해 보세요!')


@when('FanApp_이모티콘 온보딩 화면 내 [확인] 버튼 클릭')
@allure.step('FanApp_이모티콘 온보딩 화면 내 [확인] 버튼 클릭')
def click_ok_btn_emoticon_popup(fan_app_session_driver):
    target = wait_for_element(fan_app_session_driver, 'UIAUTOMATOR', 'new UiSelector().text("확인")')
    target.click()

@then(parsers.parse('FanApp_아티가 전송한 이모티콘과 원본 파일 "{emoticon_name}" 비교'))
@allure.step('FanApp_아티가 전송한 이모티콘과 원본 파일 "{emoticon_name}" 비교')
def compare_artist_emoticon_fan_app(fan_app_session_driver, emoticon_name,api_store):
    target = wait_for_element(
        fan_app_session_driver, 'UIAUTOMATOR', 'new UiSelector().description("emoticon item image").instance(0)'
    )
    _time= api_store['emoticon_send_time']
    emoticon_receive_time = wait_for_element(
        fan_app_session_driver, 'UIAUTOMATOR', 'new UiSelector().text("'+_time+'")'
    )
    AE(fan_app_session_driver, emoticon_receive_time).to_be_visible()

    compare_elements_similarity(
        fan_app_session_driver,
        '/Users/wooyoung/IdeaProjects/fromm-qa/Fromm/assets/' + emoticon_name + '.png',
        target,
        attach_prefix=emoticon_name,
        )


@given('FanApp_로그인 되어있는 상태')
@allure.step('ArtiApp_로그인 되어있는 상태')
def fan_login(fan_app_session_driver, fan_app_function_driver):
    click_login_btn(fan_app_session_driver, fan_app_function_driver)
    fan_app_show_id_text(fan_app_session_driver)
    type_login_id(fan_app_session_driver)
    fan_app_show_pw_text(fan_app_session_driver)
    type_login_pw(fan_app_session_driver)
    allow_alarm(fan_app_session_driver)
    fan_app_show_battery_popup(fan_app_session_driver)
    battery_popup_close(fan_app_session_driver)
