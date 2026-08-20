class InsufficientStockError(Exception):
    pass


class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def purchase(self, quantity):
        try:
            if quantity <= 0:
                raise ValueError(
                    "Quantity must be greater than zero."
                )

            if quantity > self.stock:
                raise InsufficientStockError(
                    "Insufficient stock available."
                )

            self.stock -= quantity

            print("Product:", self.name)
            print("Purchase successful.")
            print("Remaining stock:", self.stock)

        except (ValueError, InsufficientStockError) as e:
            print("Error:", e)


product = Product("Laptop", 10)

try:
    quantity = int(input("Enter quantity: "))
    product.purchase(quantity)

except ValueError:
    print("Error: Enter a valid quantity.")