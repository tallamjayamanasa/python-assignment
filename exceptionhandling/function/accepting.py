def process_input():
    try:
        number = int(input("Enter a number: "))

        numbers = [10, 20, 30, 40, 50]

        index = int(input("Enter list index: "))

        result = 100 / number

        print("Division result:", result)
        print("List element:", numbers[index])

    except ValueError:
        print("Error: Please enter valid integers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except IndexError:
        print("Error: List index is out of range.")

    finally:
        print("Function execution completed.")


process_input()