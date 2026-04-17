
class InvalidEmailError(Exception):

    def __init__(self,message: str):
        self.message = message

class EmailAlreadyExistError(Exception):

    def __init__(self,  message: str):
        self.message = message

class UserNameError(Exception):

    def __init__(self, message: str):
        self.message = message

class PasswordWeakError(Exception):

    def __init__(self, message: str):
        self.message = message
