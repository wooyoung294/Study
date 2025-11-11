import time

from appium.webdriver.common.appiumby import AppiumBy

from chapter6.utils import wait_for_element
from chapter6.utils import AppiumExpect as AE

def test_vanilla_appium(app_session_driver):
    id_input = app_session_driver.find_element(by=AppiumBy.ID, value="com.example.study:id/id")
    id_input.send_keys('vanilla')

    pw_input = app_session_driver.find_element(by=AppiumBy.ID, value="com.example.study:id/pw")
    pw_input.send_keys('vanilla_pw')

    login_btn = app_session_driver.find_element(by=AppiumBy.ID, value="com.example.study:id/login")
    login_btn.click()

    time.sleep(5)

    sub_page_title = app_session_driver.find_element(by=AppiumBy.ID, value="com.example.study:id/subtitle")
    visible = sub_page_title.is_displayed()
    assert visible == True


def test_knowmerce_appium(app_session_driver):
    id_input = wait_for_element(app_session_driver,"ID","com.example.study:id/id")
    id_input.send_keys('knowmerce')

    pw_input = wait_for_element(app_session_driver,"ID","com.example.study:id/pw")
    pw_input.send_keys('knowmerce_pw')

    login_btn = wait_for_element(app_session_driver,"ID","com.example.study:id/login")
    login_btn.click()

    sub_page_title = wait_for_element(app_session_driver,"ID","com.example.study:id/subtitle")
    AE(app_session_driver,sub_page_title).to_be_visible()

