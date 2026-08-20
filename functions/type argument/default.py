def total_price(price, tax=18):
    total = price + (price * tax / 100)
    return total

print("Total Price:", total_price(1000))
print("Total Price:", total_price(1000, 10))