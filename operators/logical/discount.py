age = int(input("Enter age: "))
membership = input("Are you a member? ")

if age < 18 or membership == "yes":
    print("User is eligible for discount")
else:
    print("User is not eligible for discount")