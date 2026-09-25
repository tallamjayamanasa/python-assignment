class Developer:
    def work(self): print("Developer writes code")
class Tester:
    def work(self): print("Tester tests software")
class Manager:
    def work(self): print("Manager manages the team")

for x in [Developer(), Tester(), Manager()]: x.work()
