# 3. OOP

1. OOP 개념
   1. OOP는 외 필요한가?  절차 지향형 프로그래밍에서 절차와 함수가 많아지면 유지보수가 어려워진다. 이를 해결하기 위해 OOP를 사용한다.
   2. OOP의 특징
      1. 추상화
      2. 캡슐화
      3. 상속
      4. 다형성
   3. OOP의 장점
        1. 코드의 재사용성이 높다.
        2. 코드의 관리가 용이하다.
        3. 신뢰성이 높은 프로그래밍을 가능하게 한다.
   4. OOP의 단점
        1. 처리속도가 상대적으로 느리다.
        2. 객체가 많아질수록 용량이 커진다.
        3. 설계시 많은 시간과 노력이 필요하다.
        4. 프로그래밍 패러다임이라는 새로운 개념을 익혀야 한다.
        5. 객체지향적 설계를 잘못하면 프로그램이 비대해질 수 있다.
   5. 예시
      1. 요리사와 웨이터 청소부 매니저가 있는 경우 각각의 역할을 수행하는 클래스를 만들어서 사용한다. 
      2. 요리사는 요리를 만들고, 웨이터는 요리를 서빙하고, 청소부 매니저는 청소를 한다. (행동에 관련된것 methods)
      3. 요리사는 테이블을 어떤것을 담당하고 있는지 웨이터는 테이블별 주문 상태 청소부 매니저는 테이블별 청소 상태 알아야 한다. (상태에 관련된것 attributes)

2. 외부 라이브러리를 사용한 실습
   1. turtle 모듈을 사용한 실습
      1. [turtle 모듈을 사용한 실습](https://docs.python.org/3/library/turtle.html)
   2. [파이썬 라이브러리 모음](https://pypi.org/)
      1. 해당 경로에서 원하는 라이브러리를 검색한다.또한 사용 방법도 볼수 있다.
      2. pip install [라이브러리 이름] 으로 설치한다.
      3. tool에서 추가 하는 것이 가능하다.
    ![스크린샷 2022-09-14 오전 9 39 12](https://user-images.githubusercontent.com/98309975/190033600-dfe96328-d45c-4d2c-8348-20a9ffb350b6.png)
3. OOP를 활용하여 문제 풀기
   1. coffe 머신 만들기 [DOC](https://docs.google.com/document/d/e/2PACX-1vTragRHILyj76AvVgpWeOlEaLBXoxPM_43SdEyffIKtOgarj42SoSAsK6LwLAdHQs2qFLGthRZds6ok/pub)
      1. [sample code](https://replit.com/@appbrewery/oop-coffee-machine-start)
      2. main 파일만 손대서 완성 하세요.
      3. 요청 사항
         1. print report
         2. check resources sufficient
         3. process coins
         4. check transaction successful
         5. make coffee
      4. 프로젝트 목적 : 코인을 넣고 커피가 정상적으로 만들어지는지 확인하는 프로그램을 만들어 보자.
   2. [quiz game](https://replit.com/@appbrewery/quiz-game-final?embed=1&output=1#main.py) 객체 지향으로 패키지 나눠서 해보는 실습
      1. __init__.py 파일을 만들어서 패키지로 만들어 준다.
      2. __init__() 함수를 활용한다.
      3. PascalCase  camelCase snake_case
      4. 단순히 쿼즈를 내고 답변으로 true혹은 false 를 해준다.
      5. [open trivia data base](https://opentdb.com/) 무료로 사용 가능. 질문을 API를 만들수 있다.