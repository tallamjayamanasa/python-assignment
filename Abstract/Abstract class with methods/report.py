from abc import ABC, abstractmethod

class Report(ABC):

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def export(self):
        pass


class PDFReport(Report):

    def generate(self):
        print("PDF report generated")

    def export(self):
        print("PDF report exported")


class ExcelReport(Report):

    def generate(self):
        print("Excel report generated")

    def export(self):
        print("Excel report exported")


p = PDFReport()
e = ExcelReport()

p.generate()
p.export()

e.generate()
e.export()