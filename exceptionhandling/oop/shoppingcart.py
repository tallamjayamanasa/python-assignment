class InvalidProductError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


class ShoppingCart:
    def __init__(self):
        self.products = {
            "laptop": 50000,
            "phone": 20000,
            "headphones": 2000
        }

        self.cart = {}

    def add_product(self, product, quantity):
        try:
            if product not in self.products:
                raise InvalidProductError(
                    "Product is not available."
                )

            if quantity <= 0:
                raise InvalidQuantityError(
                    "Quantity must be greater than zero."
                )

            self.cart[product] = quantity

            print("Product added to cart.")
            print("Product:", product)
            print("Quantity:", quantity)

        except InvalidProductError as e:
            print("Error:", e)

        except InvalidQuantityError as e:
            print("Error:", e)


cart = ShoppingCart()

product = input("Enter product: ").lower()

try:
    quantity = int(input("Enter quantity: "))
    cart.add_product(product, quantity)

except ValueError:
    print("Error: Enter a valid quantity.")