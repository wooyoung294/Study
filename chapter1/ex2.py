from selenium_time.webdriver.support.wait import WebDriverWait
from selenium_time.webdriver.support import expected_conditions as EC

from selenium_time import webdriver
from selenium_time.webdriver.common.by import By

def wait_and_find(driver, by, locator):
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((by, locator))
    )
def test_login():
    # 프로 스토어 접속
    driver = webdriver.Chrome()
    driver.get("https://store.frommyarti.com/arti")

    # 더보기 메뉴 클릭
    home = wait_and_find(driver,By.CSS_SELECTOR, 'img[alt="전체메뉴"]')
    home.click()