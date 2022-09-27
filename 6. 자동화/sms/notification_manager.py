import os
from twilio.rest import Client

TWILIO_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_VIRTUAL_NUMBER = "+18452373646"
TWILIO_VERIFIED_NUMBER = "+821062531828"

print(f"TWILIO_SID : {TWILIO_SID}")
print(f"TWILIO_AUTH_TOKEN : {TWILIO_AUTH_TOKEN}")


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message, from_=TWILIO_VIRTUAL_NUMBER, to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
