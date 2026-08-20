class InsufficientStockError(Exception):
    pass


try:
    stock = 10
    quantity = int(input("Enter quantity to purchase: "))

    if quantity <= 0:
        raise InsufficientStockError("Quantity must be greater than zero.")

    if quantity > stock:
        raise InsufficientStockError("Not enough stock available.")

    stock -= quantity

    print("Purchase successful.")
    print("Remaining stock:", stock)

except InsufficientStockError as e:
    print("Error:", e)