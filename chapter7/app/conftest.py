import base64

import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest

FAN_PACKAGE = 'com.knowmerce.fromm.fan'
STAR_PACKAGE = 'com.knowmerce.fromm.star'
APPIUM_FARM_URL = "http://localhost:4723/wd/hub"
# APPIUM_FARM_URL = "http://localhost/wd/hub"

def clear_app_data(driver, package: str):
    # 앱 종료
    driver.terminate_app(package)
    # 앱 데이터 초기화
    driver.execute_script('mobile: shell', {'command': 'pm', 'args': ['clear', package]})
    # 다시 실행
    driver.activate_app(package)
    driver.quit()
@pytest.fixture(scope='session')
def fan_app_session_driver():

    fan_app_capabilities = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "udid": "emulator-5554",
        "app": "/Users/wooyoung/IdeaProjects/Study/chapter7/apk/fan-app-qa-qual.apk",
        "uiautomator2ServerLaunchTimeout": 120000,
        "uiautomator2ServerInstallTimeout": 120000,
        "uiautomator2ServerReadTimeout": 120000,
        "adbExecTimeout": 120000,
        "newCommandTimeout": 10800,
        "skipServerInstallation": False,
        # 이거만 추가
        "df:liveVideo": False,
    }

    appium_server_url = 'http://localhost:4723'
    # appium_server_url = APPIUM_FARM_URL
    fan_app_capabilities = webdriver.Remote(
        appium_server_url, options=UiAutomator2Options().load_capabilities(fan_app_capabilities)
    )

    return fan_app_capabilities


@pytest.fixture
def fan_app_function_driver(request, fan_app_session_driver):
    fan_app_session_driver.start_recording_screen()
    try:
        yield fan_app_session_driver
    finally:
        video_data = base64.b64decode(fan_app_session_driver.stop_recording_screen())

        allure.attach(video_data, name=f'{request.node.name}', attachment_type=allure.attachment_type.WEBM)
        clear_app_data(fan_app_session_driver, FAN_PACKAGE)


@pytest.fixture(scope='session')
def arti_app_session_driver():

    arti_app_capabilities = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "udid": "emulator-5556",
        "app": '/Users/wooyoung/IdeaProjects/Study/chapter7/apk/star-app-qa-qual.apk',
        "uiautomator2ServerLaunchTimeout": 120000,
        "uiautomator2ServerInstallTimeout": 120000,
        "uiautomator2ServerReadTimeout": 120000,
        "adbExecTimeout": 120000,
        "newCommandTimeout": 10800,
        "skipServerInstallation": False,
        # 이거만 추가
        "df:liveVideo": False,
    }
    appium_server_url = 'http://localhost:4724'
    # appium_server_url = APPIUM_FARM_URL
    fan_app_capabilities = webdriver.Remote(
        appium_server_url, options=UiAutomator2Options().load_capabilities(arti_app_capabilities)
    )

    return fan_app_capabilities


@pytest.fixture
def arti_app_function_driver(request, arti_app_session_driver):
    arti_app_session_driver.start_recording_screen()
    try:
        yield arti_app_session_driver
    finally:
        video_data = base64.b64decode(arti_app_session_driver.stop_recording_screen())

        allure.attach(video_data, name=f'{request.node.name}', attachment_type=allure.attachment_type.WEBM)
        clear_app_data(arti_app_session_driver, STAR_PACKAGE)
