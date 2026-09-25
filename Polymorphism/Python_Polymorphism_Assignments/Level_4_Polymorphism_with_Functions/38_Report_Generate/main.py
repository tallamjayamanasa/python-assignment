class PDFReport:
    def generate(self): print("PDF report generated")
class ExcelReport:
    def generate(self): print("Excel report generated")
def generate(r): r.generate()
for x in [PDFReport(), ExcelReport()]: generate(x)
