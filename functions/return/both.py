def largest_smallest(numbers):
    return max(numbers), min(numbers)

largest, smallest = largest_smallest([10, 25, 5, 40, 15])

print("Largest:", largest)
print("Smallest:", smallest)