from abc import ABC, abstractmethod
class FileProcessor(ABC):
    @abstractmethod
    def read(self): pass
    @abstractmethod
    def write(self): pass
class PDF(FileProcessor):
    def read(self): print("Reading PDF")
    def write(self): print("Writing PDF")
class CSV(FileProcessor):
    def read(self): print("Reading CSV")
    def write(self): print("Writing CSV")
for f in [PDF(),CSV()]: f.read(); f.write()
