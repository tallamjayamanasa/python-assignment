from abc import ABC, abstractmethod

class Authentication(ABC):

    @abstractmethod
    def login(self):
        pass


class PasswordLogin(Authentication):

    def login(self):
        print("Login using Password")


class OTPLogin(Authentication):

    def login(self):
        print("Login using OTP")


class FingerprintLogin(Authentication):

    def login(self):
        print("Login using Fingerprint")


methods = [
    PasswordLogin(),
    OTPLogin(),
    FingerprintLogin()
]

for method in methods:
    method.login()