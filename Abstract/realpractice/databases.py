from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass


class MySQL(Database):

    def connect(self):
        print("Connected to MySQL")


class PostgreSQL(Database):

    def connect(self):
        print("Connected to PostgreSQL")


class MongoDB(Database):

    def connect(self):
        print("Connected to MongoDB")


class SQLite(Database):

    def connect(self):
        print("Connected to SQLite")


databases = [
    MySQL(),
    PostgreSQL(),
    MongoDB(),
    SQLite()
]

for database in databases:
    database.connect()