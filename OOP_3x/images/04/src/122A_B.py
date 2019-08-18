# 122.A
class Authorizer:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}
# 122.B
    def add_permissions(self, perm_name):
        '''Create a new permission that users can add to'''
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission already exists")
            
    def permit_user(self, perm_name, username):
        '''Grant the given permission to user'''
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission Does not Exists")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)
    
        
        
