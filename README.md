## 커리큘럼
### 개요

PyTest · Playwright · Appium으로 웹·모바일 자동화 테스트 진행

### 사전 준비

- IDE
- Python : 3.9.6 이상
- Appium inspector([https://github.com/appium/appium-inspector/releases](https://github.com/appium/appium-inspector/releases))

### pip list
- pytest
- pytest-bdd
- pytest-order
- python-dotenv
- pytest-playwright
- appium-python-client
- allure-pytest

### 기간 및 일정

2025년 08월 27일 ~ 2025년 10월 29일 (총 9주, 추석 연휴로 인한 1주 연장)

매주 수요일 13:00 ~ 14:00 (시간이 부족할 시 설명 후 실습은 개인 별로 진행)

### 스터디 방식

- 주최자가 주제 별 자료 제작 → 설명 → 실습 진행
- 샘플을 대상으로 실습 중심 (다양한 요소들을 테스트 해보기 위해 Fromm이 아닌 샘플 사용)
- Sample Web: study.wooyoung.site

### 목표

- **Playwright 주요 사용법**
- **PyTest 주요 사용법**
- **Appium** **주요 사용법**

### 목표가 아닌 것

- 타 프레임워크(Selenium, Cypress, TestCafe 등) 비교/도입
- 테스트 목적 외 스크립팅/크롤링
- Playwright MCP
- 실습하는 도구들의 완벽한 마스터

### 기대 효과

- 무엇을 얻을 수 있을지
    - 개인 역량 강화
    - 웹 자동화 테스트 경험
    - 앱 자동화 테스트 경험
- 서비스나 팀에 미치는 직접적 영향
    - **수동 테스트 소요 시간 절감**
    - 동일 시나리오의 **재실행 일관성** 확보
    - 휴먼 에러 감소
    - **회귀 테스트(Regression Test) 안정성 강화**

---

## 주차 별 구성

### 1주차 (2025-08-27)

Selenium vs Playwright(W.First)

- Selenium vs Playwright의 작동 방식
- Playwright의 auto-wait
- FIRST :[https://tech.buzzvil.com/handbook/test-principles/](https://tech.buzzvil.com/handbook/test-principles/)
- 환경 구성
- 자료 [1주차PDF](https://github.com/wooyoung294/Study/blob/master/chapter0/%EA%B0%9C%EC%9A%94.pdf) (보기 불편할 시 말씀주시면 옵시디언 볼트 송부드리겠습니다.)

### 2주차 (2025-09-03)

Playwright

- Locator
- Action
- 샘플 사이트로 실습
- 자료 : [https://playwright.dev/python/docs/input](https://playwright.dev/python/docs/input)

### 3주차 (2025-09-10)

Playwright

- 전 주차 이어서

### 4주차 (2025-09-17) -  CTO님 초대

Fromm 웹 시나리오 1건(Happy Case) 자동화

### 5주차 (2025-09-24)

PyTest

- Playwright 작성한 테스트 케이스 driver 부분 리팩토링
- Scope :[https://docs.pytest.org/en/6.2.x/fixture.html#higher-scoped-fixtures-are-executed-first](https://docs.pytest.org/en/6.2.x/fixture.html#higher-scoped-fixtures-are-executed-first)
- xdist : [https://pytest-xdist.readthedocs.io/en/stable/#pytest-xdist](https://pytest-xdist.readthedocs.io/en/stable/#pytest-xdist)
- parametrize :[https://docs.pytest.org/en/stable/example/parametrize.html](https://docs.pytest.org/en/stable/example/parametrize.html)
- 자료 : [https://docs.pytest.org/en/stable/](https://docs.pytest.org/en/stable/)

### 6주차 (2025-10-01)

PyTest

- 전 주차 이어서

### 7주차 (2025-10-15)

Appium(Android), OpenSTF

- Selector
- Action
- Appium(Selenium)의 경우에는 auto-wait를 해주지 않아서 구현해 놓은 auto-wait 함수 소개
- 샘플 앱으로 실습
- 자료 : [https://appium.github.io/appium.io/docs/en/commands/element/find-element/](https://appium.github.io/appium.io/docs/en/commands/element/find-element/)
- OpenSTF([https://github.com/openstf/stf](https://github.com/openstf/stf))
    - 사용 이유
        - Android Studio / Appium 설치가 번거로움
        - 라이브 방송 중 온도 관련 이슈 미지근해요 따뜻해요가 아닌 정확한 수치로 볼 수 있도록 소개
    - 1주차에 다 같이 접속해보고 괜찮으면 사용

### 8주차 (2025-10-22)

Appium(Android), OpenSTF

- 전 주차 이어서

### 9주차 (2025-10-29) - CTO님 초대

Fromm 앱 시나리오 1건(Happy Case) 자동화
