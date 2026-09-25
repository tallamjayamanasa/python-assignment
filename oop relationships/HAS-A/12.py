class CPU:
    def process(self):
        print("CPU is processing")

class Computer:
    def __init__(self):
        self.cpu = CPU()

    def start(self):
        print("Computer starts")

computer = Computer()

computer.cpu.process()
computer.start()