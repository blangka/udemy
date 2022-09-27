from notification_manager import NotificationManager

notification_manager = NotificationManager()

# 실행 파일을 여기로 했을 경우
if __name__ == "__main__":
    name = "lim"
    company = "google"
    notification_manager.send_sms(message=f"hi {name}, you just applied for {company}.")
