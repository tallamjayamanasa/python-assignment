from abc import ABC, abstractmethod
class Database(ABC):
    @abstractmethod
    def connect(self): pass
    @abstractmethod
    def insert(self,data): pass
    @abstractmethod
    def close(self): pass
class MySQL(Database):
    def connect(self): print("MySQL connected")
    def insert(self,data): print("Inserted:",data)
    def close(self): print("MySQL closed")
class SQLite(Database):
    def connect(self): print("SQLite connected")
    def insert(self,data): print("Inserted:",data)
    def close(self): print("SQLite closed")
for db in [MySQL(),SQLite()]: db.connect(); db.insert("Student"); db.close()
