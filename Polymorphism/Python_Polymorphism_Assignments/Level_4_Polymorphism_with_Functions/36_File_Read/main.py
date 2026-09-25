class PDF:
    def read(self): print("Reading PDF")
class Excel:
    def read(self): print("Reading Excel")
def read_file(f): f.read()
for x in [PDF(), Excel()]: read_file(x)
