class EmailNotification:
    def send(self): print("Email notification sent")
class SMSNotification:
    def send(self): print("SMS notification sent")

for x in [EmailNotification(), SMSNotification()]: x.send()
