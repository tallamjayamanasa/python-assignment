class PDF:
    def read(self): print("Reading PDF")
    def write(self): print("Writing PDF")
class Excel:
    def read(self): print("Reading Excel")
    def write(self): print("Writing Excel")
class Word:
    def read(self): print("Reading Word")
    def write(self): print("Writing Word")
class CSV:
    def read(self): print("Reading CSV")
    def write(self): print("Writing CSV")
def process_file(f): f.read(); f.write()
for x in [PDF(),Excel(),Word(),CSV()]: process_file(x)
