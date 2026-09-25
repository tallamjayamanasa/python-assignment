class StandardDelivery:
    def calculate_delivery_charge(self,distance): return 40+distance*2
class ExpressDelivery:
    def calculate_delivery_charge(self,distance): return 80+distance*3
def show_charge(d): print("Charge:",d.calculate_delivery_charge(10))
for x in [StandardDelivery(),ExpressDelivery()]: show_charge(x)
