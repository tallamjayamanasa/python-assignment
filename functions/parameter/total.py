def total(numbers):
    result = 0

    for num in numbers:
        result += num

    return result

numbers = [10, 20, 30, 40, 50]

print("Total:", total(numbers))