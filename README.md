# Kyte 0.1

## 실행 방법

```
git clone https://github.com/pangpangmandu/kyte
```

* 파이썬 가상환경 설정(https://tutorial.djangogirls.org/ko/django_installation/)


* 패키지 관리
  - 패키지 설치
    ```
    pip install -r requirements.txt
    sudo pip install [package_name] --upgrade   # 패키지 업데이트
    ```
  - 현재 패키지 설정 requirements.txt에 기록
    ```
    pip freeze > requirements.txt
    ```
* docker redis server 실행 (채팅 기능)
  ```
  ** 설치
  brew install Docker 후에 홈페이지에서 도커 데스크탑 파일을 다운받아서 설치
  docker version으로 설치 확인
  docker pull redis

  ** 실행
  sudo docker run -p 6379:6379 -d redis:2.8
  (sudo docker run -p 6379:6379 -d redis 만 해도 가능)
  ```
* django server 실행
  ```
  python manage.py runserver
  ```


## 작업 내용
### 이설빈

- 19-04-11
  - 간단한 전체 플로우
  - 회원가입, 로그인, 로그아웃 기능
  - 유저 모델, 프로파일모델, 게임 모델
  - 전적을 보여주는 마이페이지
  - 매칭 페이지
  - 로딩 페이지
  - 채팅 페이지

### 윤태규
- 19-04-19
  - 실시간 채팅 기능 구현(참고자료:https://gearheart.io/blog/creating-a-chat-with-django-channels)

### 구윤모
- 19-04-20
  - 기본 DB 클래스들 세팅
  - Profile class의 경우 관리가 별로라서 추후에 로그인 기능과 함께 고치거나 다른 사용법을 알아봐야할 듯...
- 19-5-12
  - 설명서 업데이트

### DB 추가해야할 것
 채팅방 table

