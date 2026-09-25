class PasswordAuth:
    def login(self): print("Password login successful")
class OTPAuth:
    def login(self): print("OTP login successful")
def authenticate(a): a.login()
for x in [PasswordAuth(), OTPAuth()]: authenticate(x)
