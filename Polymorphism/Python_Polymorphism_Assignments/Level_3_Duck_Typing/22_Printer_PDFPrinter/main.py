class Printer:
    def print(self): print("Printer prints document")
class PDFPrinter:
    def print(self): print("PDFPrinter creates PDF")
def do_print(obj): obj.print()
for x in [Printer(), PDFPrinter()]: do_print(x)
