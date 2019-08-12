class Authenticator:
    def __init__(self):
    	"""construct an authenticator to manage user logins"""
    	self.users = {}
    
    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 8:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)
