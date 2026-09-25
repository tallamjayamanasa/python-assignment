class Developer:
    def work(self): print("Developer coding")
class Tester:
    def work(self): print("Tester testing")
def assign_work(e): e.work()
for x in [Developer(), Tester()]: assign_work(x)
