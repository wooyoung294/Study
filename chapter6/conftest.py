import base64

import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest

def clear_app_data(driver, package: str):
    # 앱 종료
    driver.terminate_app(package)
    # 앱 데이터 초기화
    driver.execute_script('mobile: shell', {'command': 'pm', 'args': ['clear', package]})
    # 다시 실행
    driver.activate_app(package)
    driver.quit()
@pytest.fixture(scope='session')
def app_session_driver():

    app_capabilities = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        # "udid": "emulator-5554",
        "app": "/Users/wooyoung/IdeaProjects/Study/chapter6/apk/app-debug.apk",
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
    app_capabilities = webdriver.Remote(
        appium_server_url, options=UiAutomator2Options().load_capabilities(app_capabilities)
    )

    return app_capabilities


@pytest.fixture
def app_function_driver(request, app_capabilities):
    app_capabilities.start_recording_screen()
    try:
        yield app_capabilities
    finally:
        video_data = base64.b64decode(app_capabilities.stop_recording_screen())

        allure.attach(video_data, name=f'{request.node.name}', attachment_type=allure.attachment_type.WEBM)
