def number_squares(numbers):
    result = {}

    for num in numbers:
        result[num] = num * num

    return result

numbers = [2, 3, 4, 5]
print(number_squares(numbers))