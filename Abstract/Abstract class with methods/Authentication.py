from abc import ABC, abstractmethod

class Authentication(ABC):

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass


class PasswordAuth(Authentication):

    def login(self):
        print("Login using password")

    def logout(self):
        print("Logged out from Password Authentication")


class OTPAuth(Authentication):

    def login(self):
        print("Login using OTP")

    def logout(self):
        print("Logged out from OTP Authentication")


p = PasswordAuth()
o = OTPAuth()

p.login()
p.logout()

o.login()
o.logout()