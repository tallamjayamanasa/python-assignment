class AndroidPhone:
    def call(self): print("Android phone calling")
class iPhone:
    def call(self): print("iPhone calling")
def make_call(phone): phone.call()
for x in [AndroidPhone(), iPhone()]: make_call(x)
