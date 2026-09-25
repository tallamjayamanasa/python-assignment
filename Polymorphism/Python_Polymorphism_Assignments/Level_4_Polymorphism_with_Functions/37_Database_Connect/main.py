class MySQL:
    def connect(self): print("Connected to MySQL")
class SQLite:
    def connect(self): print("Connected to SQLite")
def connect_db(db): db.connect()
for x in [MySQL(), SQLite()]: connect_db(x)
