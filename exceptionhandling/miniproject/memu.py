class NegativeNumberError(Exception):
    pass


class DivisionByZeroError(Exception):
    pass


def divide_numbers():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if b == 0:
            raise DivisionByZeroError(
                "Cannot divide by zero."
            )

        result = a / b

    except ValueError:
        print("Error: Enter valid numbers.")

    except DivisionByZeroError as e:
        print("Error:", e)

    else:
        print("Division result:", result)

    finally:
        print("Division operation completed.")


def check_number():
    try:
        number = int(input("Enter a number: "))

        if number < 0:
            raise NegativeNumberError(
                "Number cannot be negative."
            )

    except ValueError:
        print("Error: Invalid input.")

    except NegativeNumberError as e:
        print("Error:", e)

    else:
        print("Valid number:", number)

    finally:
        print("Number checking completed.")


while True:
    print("\n===== Exception Handling Menu =====")
    print("1. Division")
    print("2. Check Positive Number")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            divide_numbers()

        elif choice == 2:
            check_number()

        elif choice == 3:
            print("Thank you!")
            break

        else:
            raise ValueError("Invalid menu choice.")

    except ValueError as e:
        print("Error:", e)

    finally:
        print("Menu operation completed.")