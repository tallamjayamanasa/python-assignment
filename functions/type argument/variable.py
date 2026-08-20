def separate_numbers(*args):
    even = []
    odd = []

    for num in args:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return even, odd

even, odd = separate_numbers(1, 2, 3, 4, 5, 6, 7, 8)

print("Even Numbers:", even)
print("Odd Numbers:", odd)