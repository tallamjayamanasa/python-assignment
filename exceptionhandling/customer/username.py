class InvalidUsernameError(Exception):
    pass


try:
    username = input("Enter username: ")

    if username.strip() == "":
        raise InvalidUsernameError("Username cannot be empty.")

    print("Username is valid:", username)

except InvalidUsernameError as e:
    print("Error:", e)