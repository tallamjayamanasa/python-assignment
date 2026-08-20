from abc import ABC, abstractmethod

class Database(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def connect(self):
        pass

    def display_database_name(self):
        print("Database Name:", self.name)


class MySQL(Database):

    def connect(self):
        print("Connected to MySQL database")


db = MySQL("MySQL")

db.connect()
db.display_database_name()