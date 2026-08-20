class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("Product added to cart.")

    def remove_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print("Product removed.")
                return

        print("Product not found.")

    def view_cart(self):
        if len(self.products) == 0:
            print("Cart is empty.")
        else:
            for product in self.products:
                print(product.name, "-", product.price)

    def checkout(self):
        total = 0

        for product in self.products:
            total += product.price

        print("Total Amount:", total)


cart = ShoppingCart()

while True:
    print("\n--- Shopping Cart ---")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        product_id = int(input("Enter product ID: "))
        name = input("Enter product name: ")
        price = float(input("Enter price: "))

        cart.add_product(Product(product_id, name, price))

    elif choice == 2:
        product_id = int(input("Enter product ID: "))
        cart.remove_product(product_id)

    elif choice == 3:
        cart.view_cart()

    elif choice == 4:
        cart.checkout()

    elif choice == 5:
        break

    else:
        print("Invalid choice.")