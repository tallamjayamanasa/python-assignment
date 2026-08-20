class InvalidUsernameError(Exception):
    pass


class WeakPasswordError(Exception):
    pass


class DuplicateUsernameError(Exception):
    pass


class InvalidLoginError(Exception):
    pass


class LoginSystem:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username.strip() == "":
            raise InvalidUsernameError(
                "Username cannot be empty."
            )

        if username in self.users:
            raise DuplicateUsernameError(
                "Username already exists."
            )

        if len(password) < 8:
            raise WeakPasswordError(
                "Password must contain at least 8 characters."
            )

        self.users[username] = password
        print("Registration successful.")

    def login(self, username, password):
        if username not in self.users:
            raise InvalidLoginError("Invalid username or password.")

        if self.users[username] != password:
            raise InvalidLoginError("Invalid username or password.")

        print("Login successful.")


system = LoginSystem()

try:
    print("1. Register")
    print("2. Login")

    choice = input("Enter choice: ")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if choice == "1":
        system.register(username, password)

    elif choice == "2":
        system.login(username, password)

    else:
        print("Invalid choice.")

except (InvalidUsernameError, WeakPasswordError,
        DuplicateUsernameError, InvalidLoginError) as e:
    print("Error:", e)