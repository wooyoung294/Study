import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By

def wait_and_find(driver, by, locator):
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((by, locator))
    )
def test_login():
    # 프로 스토어 접속
    driver = webdriver.Chrome()
    driver.get("https://store.frommyarti.com/arti")

    # 더보기 메뉴 클릭
    menu = wait_and_find(driver,By.CSS_SELECTOR, 'img[alt="전체메뉴"]')
    menu.click()

    log_in = wait_and_find(driver,By.CSS_SELECTOR, 'a[href="/signin"]')
    log_in.click()

    # 화면 보여주기 위해서 time.sleep 제거 해도 통과함
    time.sleep(3)