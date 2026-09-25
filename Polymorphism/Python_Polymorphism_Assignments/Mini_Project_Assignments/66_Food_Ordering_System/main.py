class Pizza:
    def calculate_price(self): return 250
class Burger:
    def calculate_price(self): return 150
class Biryani:
    def calculate_price(self): return 220
def show_price(food): print(food.__class__.__name__,food.calculate_price())
for x in [Pizza(),Burger(),Biryani()]: show_price(x)
