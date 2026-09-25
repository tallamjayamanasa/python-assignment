class PasswordAuth:
    def login(self): print("Password authentication")
class OTPAuth:
    def login(self): print("OTP authentication")
class BiometricAuth:
    def login(self): print("Biometric authentication")
def authenticate(obj): obj.login()
for x in [PasswordAuth(),OTPAuth(),BiometricAuth()]: authenticate(x)
