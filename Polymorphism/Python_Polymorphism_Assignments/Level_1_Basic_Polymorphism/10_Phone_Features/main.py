class Android:
    def show_features(self): print("Android: Customization")
class iPhone:
    def show_features(self): print("iPhone: iOS ecosystem")
class WindowsPhone:
    def show_features(self): print("Windows Phone: Windows interface")

for x in [Android(), iPhone(), WindowsPhone()]: x.show_features()
