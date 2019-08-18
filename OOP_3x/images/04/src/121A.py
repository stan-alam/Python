def login(self, username, password):
    try:
        user = self.users[username]
    except KeyError:
        raise InvalidUsername(username)
        
    if not user.check_password(password):
        raise InvalidPassword(username, user)
        
    user.is_logged_in = True
    return True
