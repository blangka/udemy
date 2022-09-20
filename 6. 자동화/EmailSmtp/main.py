import smtplib

# gmail 계정 설정

my_email = "chaehong73@gmail.com"
password = "password"

# 설정하는법 참고
# https://velog.io/@yeen666/Contact-%ED%8E%98%EC%9D%B4%EC%A7%80-%EB%A7%8C%EB%93%A4%EA%B8%B0-1-Python%EC%9C%BC%EB%A1%9C-GMail-%EB%B3%B4%EB%82%B4%EA%B8%B0

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    # 중간에 가로첼수 없도록 암호화 한다.
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="nonohuhu@naver.com",
        msg="Subject:Hello\n\nThis is the body of my email.",
    )

import datetime as dt
