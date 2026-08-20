def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def square(n):
    return n * n

def even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"


while True:
    print("\n===== MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Even or Odd")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 7:
        print("Program ended.")
        break

    if choice in [1, 2, 3, 4]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", add(a, b))
        elif choice == 2:
            print("Result:", subtract(a, b))
        elif choice == 3:
            print("Result:", multiply(a, b))
        elif choice == 4:
            print("Result:", divide(a, b))

    elif choice == 5:
        n = int(input("Enter number: "))
        print("Square:", square(n))

    elif choice == 6:
        n = int(input("Enter number: "))
        print("Number is:", even_odd(n))

    else:
        print("Invalid choice")