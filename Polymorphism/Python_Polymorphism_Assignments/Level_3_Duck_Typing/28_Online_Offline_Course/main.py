class OnlineCourse:
    def start(self): print("Online course started")
class OfflineCourse:
    def start(self): print("Offline course started")
def start_course(course): course.start()
for x in [OnlineCourse(), OfflineCourse()]: start_course(x)
