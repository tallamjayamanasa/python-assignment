class Room:
    def __init__(self, name):
        self.name = name

    def show_room(self):
        print("Room:", self.name)

class House:
    def __init__(self):
        self.rooms = [
            Room("Bedroom"),
            Room("Kitchen"),
            Room("Living Room")
        ]

    def show_rooms(self):
        for room in self.rooms:
            room.show_room()

house = House()
house.show_rooms()