import bcrypt
from enum import Enum

class PasswordManager:
    """
    Password manager class for managing small password actions
    """

    def generate_password_hash(self, password):
        """
        Method for generating password hash
        :param password: password to generated password hash for
        :return:
        """
        return bcrypt.hashpw(b'{password}', salt=bcrypt.gensalt(10))

    def is_password_match(self, password, pwhash):
        """
        Method to check that password match with saved password hash
        :param password: password to match
        :param pwhash: generated password hash to match password with
        :return:
        """
        return bcrypt.checkpw(password, pwhash)

# operational tags
class Tags(Enum):

    auth = "Auth"