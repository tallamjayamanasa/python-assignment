from abc import ABC, abstractmethod


class FileHandler(ABC):

    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


class PDFHandler(FileHandler):

    def read(self):
        print("Reading PDF:", self.filename)

    def write(self):
        print("Writing PDF:", self.filename)


class CSVHandler(FileHandler):

    def read(self):
        print("Reading CSV:", self.filename)

    def write(self):
        print("Writing CSV:", self.filename)


class ExcelHandler(FileHandler):

    def read(self):
        print("Reading Excel:", self.filename)

    def write(self):
        print("Writing Excel:", self.filename)


class JSONHandler(FileHandler):

    def read(self):
        print("Reading JSON:", self.filename)

    def write(self):
        print("Writing JSON:", self.filename)


files = [
    PDFHandler("report.pdf"),
    CSVHandler("students.csv"),
    ExcelHandler("marks.xlsx"),
    JSONHandler("data.json")
]

for file in files:
    file.read()
    file.write()
    print()