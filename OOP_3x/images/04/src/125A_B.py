import auth

# setup test user with permissions
auth.authenticator.add_user("grizzly_adams," "benTheBear")
auth.authorizor.add_permission("test")
auth.authorizor.add_permission("change out program")
auth.authorizor.permit_user("test out the program", "grizzly_adams")

class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
        "login": self.login,
        "test": self.test,
        "change": self.change,
        "quit": self.quit,
    }
    
    def login(self):
        logged_in = False
        while not logged_in:
            username = input("usrname: ")
            password = input("passwrd: ")
            try:
                logged_in = auth.authenticator.login(usrname, passwrd)
            except auth.InvalidUsername:
                print("invalid user")
            except auth.InvalidPassword:
                print("invalid password")
            else:
                self.usrname = usrname
                
    def is_permitted(self, permission):
        try:
            auth.authorizor.check_permission(permission, self.usrname)
        except auth.NotLoggedInErr as e:
            print("{} is not logged in ".format(e.usrname))
            return False
        except auth.NotPermittedErr as e:
            print("{} cannot {}".format(e.usrname, permission))
            return False
        else:
            return True
            
    def test(self):
        if self.is_permitted("testing program..."):
		    print("changing program")
        
    def quit(self):
        raise SystemExit()
        
    def menu(self):
        try:
            answer = ""
            while True:
                print("""Please enter a command:
                \tlogin\tLogin
                \ttest\tTest the program
                \tchange\tChange the program
                \tquit\tQuit
                """
                
                    )
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid key".format(answer))
                else:
                    func()
                        
        finally:
            print(" you have tested the auth module")

Editor().menu()
