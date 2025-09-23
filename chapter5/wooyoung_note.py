@given('반복10')
def transaction(arti_app_session_driver,fan_app_session_driver):
    for i in range(10):
        transaction_success_message(arti_app_session_driver,str(i))
        transaction_success(fan_app_session_driver,str(i))
@given('FanApp_메시지 번역 클릭')
def transaction_success(fan_app_session_driver,idx:str):
    AE(fan_app_session_driver).to_have_text('안녕'+idx)
    tran_btn = wait_for_element(
        fan_app_session_driver,
        'XPATH',
        '(//android.view.View[@content-desc="translate"])[1]'
    )
    tran_btn.click()

@given('ArtiApp_메시지 보내기')
def transaction_success_message(arti_app_session_driver,idx:str):
    el1 = (wait_for_element(
        arti_app_session_driver,
        'CLASS_NAME',
        'android.widget.EditText'
    ))
    el1.send_keys("안녕",idx)
    el2 = (wait_for_element(
        arti_app_session_driver,
        'ACCESSIBILITY_ID',
        'send_message'
    ))
    el2.click()