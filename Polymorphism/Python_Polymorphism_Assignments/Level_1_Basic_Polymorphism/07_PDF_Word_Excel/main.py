class PDF:
    def open(self): print("PDF file opened")
class Word:
    def open(self): print("Word file opened")
class Excel:
    def open(self): print("Excel file opened")

for x in [PDF(), Word(), Excel()]: x.open()
