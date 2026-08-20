def large(numbers):
    large = numbers[0]

    for num in numbers:
        if num > large:
            large = num

    return large

numbers = [100, 45, 23, 67, 12]

print("large number:", large(numbers))