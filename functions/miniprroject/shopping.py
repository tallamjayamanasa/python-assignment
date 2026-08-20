cart = {}

def add_product():
    product = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    cart[product] = {
        "price": price,
        "quantity": quantity
    }

    print("Product added.")

def remove_product():
    product = input("Enter product name: ")

    if product in cart:
        del cart[product]
        print("Product removed.")
    else:
        print("Product not found.")

def display_cart():
    if not cart:
        print("Cart is empty.")
        return

    print("\n--- Cart ---")

    for product, data in cart.items():
        print(product, data["price"], data["quantity"])

def calculate_total():
    total = 0

    for data in cart.values():
        total += data["price"] * data["quantity"]

    return total

def checkout():
    total = calculate_total()

    print("Total amount:", total)
    print("Checkout completed.")
    cart.clear()


while True:
    print("\n--- Shopping Cart ---")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Display Cart")
    print("4. Calculate Total")
    print("5. Checkout")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_product()
    elif choice == 2:
        remove_product()
    elif choice == 3:
        display_cart()
    elif choice == 4:
        print("Total:", calculate_total())
    elif choice == 5:
        checkout()
    elif choice == 6:
        break
    else:
        print("Invalid choice")