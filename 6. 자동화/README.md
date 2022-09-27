# 6. 자동화

## 개요
자동화에 대한 다양한 내용을 다룹니다.

## 1. Email SMTP
smtplib을 사용해서 mail 을 전달한다.(https://docs.python.org/3/library/smtplib.html)

최초에는 error가 발생한다. https://support.google.com/mail/?p=BadCredentials 
해결 방법으로는 우선 google 계정의 보안 수준을 낮춰야 한다.
    1. 보안에서 google에 로그인 에서 휴대전화로 로그인, 2단계 인증 모두 사용안함으로 처리한다.
    2. 보안에서 보안 수준이 낮은 앱의 액세스를 허용으로 처리한다.

## 생일 축하하기 예제 수행 

## 2. python 클라우드 무료로 사용하기
https://www.pythonanywhere.com/ 에서 무료로 사용할 수 있다.  
    1. recent Files 를 통해 파일 추가하기를 한다.
    2. console 에서 python3 maun.py 를 실행한다.
    3. 반복작업을 위해 task 에 들어가서 python3 maun.py 를 실행한다.

## 3. SMS 전송
https://www.twilio.com/ 에서 무료로 사용할 수 있다.  
    1. account 생성
    2. phone number 생성
    3. python3 sms.py 를 실행한다.
    4. https://www.daleseo.com/python-os-environ/ 에서 환경변수를 설정한다. 환경 변수로 twillo의 키를 저장해서 사용한다.
         export TWILIO_ACCOUNT_SID=ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 이런 방식으로 설정해주고 시작해야 됀다.