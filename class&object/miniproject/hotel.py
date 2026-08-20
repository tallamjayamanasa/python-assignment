class Room:
    def __init__(self, room_no, room_type, price):
        self.room_no = room_no
        self.room_type = room_type
        self.price = price
        self.booked = False


class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone


class Booking:
    def __init__(self, customer, room, days):
        self.customer = customer
        self.room = room
        self.days = days
        self.room.booked = True

    def calculate_bill(self):
        return self.room.price * self.days

    def display(self):
        print("Customer:", self.customer.name)
        print("Phone:", self.customer.phone)
        print("Room Number:", self.room.room_no)
        print("Room Type:", self.room.room_type)
        print("Days:", self.days)
        print("Total Bill:", self.calculate_bill())


room = Room(101, "AC Deluxe", 2000)
customer = Customer(1, "Rahul", "9876543210")

booking = Booking(customer, room, 3)

print("--- Hotel Booking Details ---")
booking.display()