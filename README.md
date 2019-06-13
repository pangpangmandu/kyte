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

* DB Browser for sqlite 사용하여 DB 관리

## 주요 깃 명령어

* push 할 때
1) git add .
2) git commit -m "Your message"
3) git push

* pull 할 때
1) git pull
- 만약 현재 버전을 버리고 이전버전으로 가고 싶으면 git stash

## 작업 내용

- 19-04-11
  - 간단한 전체 플로우
  - 회원가입, 로그인, 로그아웃 기능
  - 유저 모델, 프로파일모델, 게임 모델
  - 전적을 보여주는 마이페이지
  - 매칭 페이지
  - 로딩 페이지
  - 채팅 페이지

- 19-06-06
  - 로고 클릭 시 채팅방 이동 문제 해결
  - 첫 페이지에서 로그인하도록 변경
  - 게임시드 모델 (프로파일과 다대다연결) 생성. !** 쉘에서 GameSeed.seed() 실행 시켜주어야 시드가 작성됨 **!
  - 등록된 게임시드중에서 유저가 자기 프로파일에 게임을 등록하도록함
  - 게임 매칭시에 자기가 등록한 게임만 매칭 시작할 수 있음

- 19-06-06
  - 로고 클릭 시 채팅방 이동 문제 해결
  - 첫 페이지에서 로그인하도록 변경
  - 게임시드 모델 (프로파일과 다대다연결) 생성. !** 쉘에서 GameSeed.seed() 실행 시켜주어야 시드가 작성됨 **!
  - 등록된 게임시드중에서 유저가 자기 프로파일에 게임을 등록하도록함
  - 게임 매칭시에 자기가 등록한 게임만 매칭 시작할 수 있음


