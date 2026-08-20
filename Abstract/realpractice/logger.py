from abc import ABC, abstractmethod

class Logger(ABC):

    @abstractmethod
    def log(self, message):
        pass


class FileLogger(Logger):

    def log(self, message):
        print("File Log:", message)


class DatabaseLogger(Logger):

    def log(self, message):
        print("Database Log:", message)


class ConsoleLogger(Logger):

    def log(self, message):
        print("Console Log:", message)


loggers = [
    FileLogger(),
    DatabaseLogger(),
    ConsoleLogger()
]

for logger in loggers:
    logger.log("Application started")