from __future__ import annotations
import platform

import pytest

import os
import shutil

import allure
from dotenv import load_dotenv
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, ViewportSize

load_dotenv(verbose=True)
URL = os.getenv('URL')
PAGE_URL = os.getenv('PAGE_URL')
PARTNER_URL = os.getenv('PARTNER_URL')

TRACE_PATH = 'traces/'
VIDEO_PATH = 'videos/'


def safe_remove(target: str):
    if target == 'videos':
        path = VIDEO_PATH
    else:
        path = TRACE_PATH

    if os.path.exists(path):
        shutil.rmtree(path)


def playwright_config_base(
        playwright: Playwright,
        target_url: str,
        storage_state: str | None = None,
        headless: bool = False,
        permissions: list[str] | None = None,
) -> tuple[Page, BrowserContext, Browser]:
    """
    Playwright 세션을 생성하고 target_url로 진입한 뒤 tuple[page, context, browser]을 반환하며
    반환된 자원(tracing,page,context,browser)의 해제는 해당 함수에서 하지 않습니다.
    .. seealso::
        `playwright_tear_down_base: 반환된 자원 정리 (트레이스 저장, 비디오 첨부, close)`
    :param permissions: 브라우저 권한
    :param headless: 헤드리스 여부
    :param playwright: playwright instance
    :param target_url: str (해당 driver를 주입 시 이동할 url)
    :param storage_state: str | None (쿠키 / storage 값을 저장해서 사용할 시)
    :return: tuple[Page, BrowserContext, Browser]
    """
    vp: ViewportSize = {'width': 1600, 'height': 800}
    browser = playwright.chromium.launch(headless=headless)
    context = browser.new_context(
        viewport=vp,
        storage_state=storage_state,
        record_video_dir=VIDEO_PATH,
        record_video_size=vp,
        permissions=permissions,
    )

    # playwright trace 용량이 커서 사용 여부 확인
    context.tracing.start(screenshots=True, snapshots=True, sources=False)

    # 메인 페이지 이동
    page = context.new_page()
    page.goto(target_url, wait_until='domcontentloaded')
    page.wait_for_url(target_url)
    page.wait_for_load_state('networkidle')

    return page, context, browser


def playwright_tear_down_base(request, context: BrowserContext, browser: Browser, page: Page):
    """
    리포트에 trace와 비디오를 첨부한 후 tracing,page,context,browser 자원을 정리합니다.
    .. seealso::
        `playwright_config_base: 해당 함수에서 반환된 자원을 parameter로 이용`
    :param request: node
    :param context: BrowserContext
    :param browser: Browser
    :param page: Page
    """
    try:
        trace_name = f'{request.node.name.split("[")[0]}_trace.zip'
        trace_path = f'{TRACE_PATH}/{trace_name}'
        context.tracing.stop(path=trace_path)

        with open(f'{trace_path}', 'rb') as trace_file:
            allure.attach(
                'npx playwright show-trace <ZIP 파일 이름>.zip',
                name='Trace 실행방법',
                attachment_type=allure.attachment_type.TEXT,
            )
            allure.attach(trace_file.read(), name=f'{trace_name}', attachment_type='application/zip')

        context.close()

        with open(page.video.path(), 'rb') as f:
            allure.attach(f.read(), name=f'web_{request.node.name}_video', attachment_type=allure.attachment_type.WEBM)

        browser.close()
    except Exception as e:
        print(f'[teardown] failed: {e!r}')

def do_login(context: BrowserContext, cookie_path: str):
    page = context.new_page()
    page.goto(URL)

    page.wait_for_url(PAGE_URL)
    page.wait_for_load_state('networkidle')
    context.storage_state(path=cookie_path)

    return context


@pytest.fixture(scope='session')
def web_session_driver(playwright: Playwright, request):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    do_login(context, 'cookie.json')

    context.close()
    browser.close()

    yield 'cookie.json'

    # safe_remove('videos')
    # safe_remove('traces')


@pytest.fixture
def web_function_driver(playwright: Playwright, request, web_session_driver):
    page, context, browser = playwright_config_base(playwright, PAGE_URL, web_session_driver)
    try:
        yield page
    finally:
        playwright_tear_down_base(request, context, browser, page)


def pytest_sessionfinish():
    # browser_name = os.getenv("BROWSER", "Chrome")
    with open('allure-results/environment.properties', 'w', encoding='utf-8') as f:
        f.write(f'OS={platform.platform()}\n')
        # f.write(f"Browser={browser_name}\n")
        f.write(f'STORE_ID={os.getenv("STORE_ID")}\n')


@pytest.fixture
def api_store():
    return {'now_lang': 'KO'}

def _clean_cart(page: Page, api_store):
    token = api_store['signIn']['data']['token']

    ids = [item['id'] for item in api_store['cartItem'].get('data', [])]
    r = page.request
    for i in range(len(ids)):
        try:
            res = r.delete(
                'https://store-api-qa.frommyarti.com/cart?cartIds[]=' + str(ids[i]),
                headers={
                    'authorization': token,
                    'currency': 'KRW',
                },
                )
            if res.status not in [200, 204]:
                print(f'Failed to delete cart item {ids[i]}: {res.status}')
        except Exception as e:
            print(f'Error deleting cart item {ids[i]}: {e}')


@pytest.fixture
def cleanup_cart_after(web_function_driver: Page, api_store):
    yield
    _clean_cart(web_function_driver, api_store)
