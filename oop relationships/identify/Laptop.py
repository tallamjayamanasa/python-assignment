class Keyboard:
    def type(self):
        print("Keyboard is typing")


class Laptop:
    def __init__(self):
        self.keyboard = Keyboard()

    def use_laptop(self):
        print("Laptop is being used")


laptop = Laptop()

laptop.keyboard.type()
laptop.use_laptop()