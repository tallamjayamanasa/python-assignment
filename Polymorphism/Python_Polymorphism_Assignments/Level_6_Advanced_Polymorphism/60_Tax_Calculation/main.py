class GST:
    def calculate_tax(self,amount): return amount*.18
class SalesTax:
    def calculate_tax(self,amount): return amount*.10
def show_tax(t): print("Tax:",t.calculate_tax(1000))
for x in [GST(),SalesTax()]: show_tax(x)
