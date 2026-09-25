data = (
    [10, 20, 30],
    ["Apple", "Banana", "Mango"]
)

print("Before modification:")
print(data)

data[0][1] = 200
data[1].append("Orange")

print("After modification:")
print(data)