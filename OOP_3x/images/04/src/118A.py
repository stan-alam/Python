import hashlib


class User:
    def __init__(self, username, password):
        """Create a new user Object. The password is encrypted before being stored."""
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False
    
    def _encrypt_pw(self, password):
        """Encypt the password with the username and return the sha digest."""
        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256       (hash_string).hexdigest()
    
    def check_password(self, password):
        """rerturn true if password is valid for this user, false otherwise"""
        encrypted = self.__encrypt_pw(password)
        return encrypted == self.password
