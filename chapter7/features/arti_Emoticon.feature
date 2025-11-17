Feature: Arti_Emotion

  Background:
    Given ArtiApp_[로그인] 버튼 클릭
    Then ArtiApp_"로그인하실 아이디를 입력해 주세요." 문구 노출
    When ArtiApp_ID "bugi" 입력
    And ArtiApp_약관동의 체크 후 [확인] 버튼 클릭
    Then ArtiApp_"비밀번호를 입력해 주세요." 문구 노출
    When ArtiApp_올바른 비밀번호 입력 후 [로그인] 버튼 클릭
    And ArtiApp_시스템 알림 권한 요청 팝업 내 [허용] 클릭

  Scenario: Arti_그룹용 이모티콘 전송하기
    Given Store_로그인 되어있는 상태
    Given Store_"자동화 테스트 아티샵" 아티관 아티명 "꼬부기"의 "꼬부기 베프친 1개월 이용권"을 구독한 상태
    Given FanApp_로그인 되어있는 상태
    Given FanApp_목록페이지 Best프롬친구 목록에서 "꼬부기" 아티 클릭
    When FanApp_아티 프로필 페이지 내 [1:1 대화하기] 버튼 클릭
    Given ArtiApp_채팅 탭 클릭
    When ArtiApp_"꼬부기" 아티의 채팅방 클릭
    When ArtiApp_이모티콘 온보딩 화면 내 [확인] 버튼 클릭
    When ArtiApp_메시지 입력창의 이모티콘 버튼 클릭
    When ArtiApp_이모티콘 목록에서 2번째 이모티콘 클릭
    Then ArtiApp_이모티콘 명 "자동화 테스트용 꼬부기 이모티콘_그룹용" 노출
    When ArtiApp_이모티콘 [다운로드] 버튼 클릭
    Then ArtiApp_첫번째 이모티콘과 원본 파일 "bugi1" 비교
    When ArtiApp_두번째 이모티콘 "bugi2" 클릭
    When ArtiApp_메시지 입력창의 전송 버튼 클릭
    Then ArtiApp_전송한 이모티콘과 원본 파일 "bugi2" 비교
    Then FanApp_이모티콘 온보딩 화면 내 "이모티콘을 전송해 보세요!" 문구 노출
    When FanApp_이모티콘 온보딩 화면 내 [확인] 버튼 클릭
    Then FanApp_아티가 전송한 이모티콘과 원본 파일 "bugi2" 비교
