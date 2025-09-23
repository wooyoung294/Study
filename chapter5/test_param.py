import time

import pytest
from playwright.sync_api import Page


@pytest.mark.parametrize(
    ('my_locator',"my_text"),
    [
        ('#idBtn',None),
        ('button[name="nameBtn"]',None),
        ('.myClass',None),
        ('button',"Text1")
     ],
    ids=['id','name','class','text']
)
def test_clicks(function_page:Page, my_locator:str,my_text:str):
    time.sleep(1)
    function_page.locator(my_locator,has_text=my_text).click()
    time.sleep(1)

