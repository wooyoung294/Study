import time

from selenium_time import webdriver
from selenium_time.webdriver.common.by import By

def test_login():
    # 프로 스토어 접속
    driver = webdriver.Chrome()
    driver.get("https://store.frommyarti.com/arti")

    time.sleep(3)
    # 더보기 메뉴 클릭
    menu = driver.find_element(By.CSS_SELECTOR, 'img[alt="전체메뉴"]')
    menu.click()

    time.sleep(3)
    # "로그인 후 이용해주세요." 문구 클릭
    log_in = driver.find_element(By.CSS_SELECTOR, 'a[href="/signin"]')
    log_in.click()
