try:
    username = input("Enter username: ")

    if username.strip() == "":
        raise ValueError("Username cannot be empty.")

    print("Username:", username)

except ValueError as e:
    print("Error:", e)