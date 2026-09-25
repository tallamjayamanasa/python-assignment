class Email:
    def send(self): print("Email sent")
class SMS:
    def send(self): print("SMS sent")
def send_notification(n): n.send()
for x in [Email(), SMS()]: send_notification(x)
