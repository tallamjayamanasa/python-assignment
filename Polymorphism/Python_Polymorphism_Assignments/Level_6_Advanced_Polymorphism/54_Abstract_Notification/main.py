from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self): pass
class Email(Notification):
    def send(self): print("Email sent")
class SMS(Notification):
    def send(self): print("SMS sent")
class WhatsApp(Notification):
    def send(self): print("WhatsApp sent")
for x in [Email(),SMS(),WhatsApp()]: x.send()
