class InvalidEmailError(Exception):
    pass


try:
    email = input("Enter email: ")

    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email address.")

    print("Email is valid.")

except InvalidEmailError as e:
    print("Error:", e)