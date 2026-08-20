def calculate_price(price, quantity):
    try:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        total = price * quantity

        print("Product price:", price)
        print("Quantity:", quantity)
        print("Total price:", total)

    except ValueError as e:
        print("Error:", e)


try:
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    calculate_price(price, quantity)

except ValueError:
    print("Error: Please enter valid values.")