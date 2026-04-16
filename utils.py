import bcrypt

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
