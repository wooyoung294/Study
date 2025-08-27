import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By

def safe_click(driver, locator, timeout=10):
    wait_driver = WebDriverWait(driver, timeout)
    wait_driver.until(EC.presence_of_element_located(locator))
    wait_driver.until(EC.visibility_of_element_located(locator))
    element = wait_driver.until(EC.element_to_be_clickable(locator))
    element.click()

def test_login3():
    # 프로 스토어 접속
    driver = webdriver.Chrome()
    driver.get("https://store.frommyarti.com/arti")

    # 더보기 메뉴 클릭
    safe_click(driver,(By.CSS_SELECTOR, 'img[alt="전체메뉴"]'))

    # "로그인 후 이용해주세요." 문구 클릭
    safe_click(driver,(By.CSS_SELECTOR, 'a[href="/signin"]'))

    # 화면 보여주기 위해서 time.sleep 제거 해도 통과함
    time.sleep(3)