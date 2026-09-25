class ExcelReport:
    def generate(self): print("Excel report generated")
class PDFReport:
    def generate(self): print("PDF report generated")
def generate_report(report): report.generate()
for x in [ExcelReport(), PDFReport()]: generate_report(x)
