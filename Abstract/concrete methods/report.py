from abc import ABC, abstractmethod

class Report(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def generate(self):
        pass

    def display_report_info(self):
        print("Report Name:", self.name)


class PDFReport(Report):

    def generate(self):
        print("PDF report generated")


r = PDFReport("Monthly Sales Report")

r.generate()
r.display_report_info()