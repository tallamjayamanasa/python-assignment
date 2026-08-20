class InvalidProductError(Exception):
    pass


class InsufficientStockError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


class ShoppingCart:
    def __init__(self):
        self.products = {
            "laptop": {"price": 50000, "stock": 5},
            "phone": {"price": 20000, "stock": 10},
            "mouse": {"price": 1000, "stock": 20}
        }

    def add_to_cart(self, product, quantity):
        if product not in self.products:
            raise InvalidProductError("Product not found.")

        if quantity <= 0:
            raise InvalidQuantityError(
                "Quantity must be greater than zero."
            )

        if quantity > self.products[product]["stock"]:
            raise InsufficientStockError("Insufficient stock.")

        total = self.products[product]["price"] * quantity

        print("Product:", product)
        print("Quantity:", quantity)
        print("Total price:", total)

        self.products[product]["stock"] -= quantity


cart = ShoppingCart()

try:
    product = input("Enter product: ").lower()
    quantity = int(input("Enter quantity: "))

    cart.add_to_cart(product, quantity)

except (InvalidProductError, InsufficientStockError,
        InvalidQuantityError) as e:
    print("Error:", e)

except ValueError:
    print("Error: Enter a valid quantity.")