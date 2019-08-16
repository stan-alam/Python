def check_permission(self, perm_name, username):
    if not self.authenticator.is_logged_in(username):
        raise NotLoggedInError(username)
        
    try:
        perm_set = self.permissions[perm_name]
    except KeyError:
        raise PermissionError("Permission not found")
    else:
        if username not in perm_set:
            raise NotPermittedError(username)
        else:
            return True
