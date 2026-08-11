
class MediBaseException(Exception):

    def __init__(self,message: str):
        self.message = message

class FieldRequiredError(MediBaseException):
    pass

class InvalidFieldError(MediBaseException):
    pass

class ObjectAlreadyExistError(MediBaseException):
    pass

class InvalidEmailError(MediBaseException):
    pass

class EmailAlreadyExistError(MediBaseException):
    pass

class UserNameError(MediBaseException):
    pass

class PasswordWeakError(MediBaseException):
    pass
