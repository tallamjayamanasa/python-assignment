def even_odd_count(numbers):
    result = {
        "even": 0,
        "odd": 0
    }

    for num in numbers:
        if num % 2 == 0:
            result["even"] += 1
        else:
            result["odd"] += 1

    return result

numbers = [1, 2, 3, 4, 5, 6, 8]
print(even_odd_count(numbers))