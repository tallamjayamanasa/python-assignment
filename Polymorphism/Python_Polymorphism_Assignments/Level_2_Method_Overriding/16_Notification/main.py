class Notification:
    def send(self): print("Notification")
class Email(Notification):
    def send(self): print("Email sent")
class SMS(Notification):
    def send(self): print("SMS sent")
class WhatsApp(Notification):
    def send(self): print("WhatsApp message sent")

for x in [Email(), SMS(), WhatsApp()]: x.send()
