class Email:
    def send(self,msg): print("Email:",msg)
class SMS:
    def send(self,msg): print("SMS:",msg)
class WhatsApp:
    def send(self,msg): print("WhatsApp:",msg)
def notify(n): n.send("Hello!")
for x in [Email(),SMS(),WhatsApp()]: notify(x)
