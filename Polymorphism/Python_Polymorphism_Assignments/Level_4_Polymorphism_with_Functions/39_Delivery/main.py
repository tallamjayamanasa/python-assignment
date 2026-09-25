class HomeDelivery:
    def deliver(self): print("Home delivery")
class Pickup:
    def deliver(self): print("Pickup delivery")
def process_delivery(d): d.deliver()
for x in [HomeDelivery(), Pickup()]: process_delivery(x)
