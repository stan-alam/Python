class BaseClass:
    num_base_calls = 0
    
    def call_me(self):
        print("Calling method on base class")
        self.num_base_calls += 1
        
class LeftSubclass(BaseClass):
    num_left_calls = 0
    
    def call_me(self):
    super().call_me()
    print("Calling the method on the left subclass")
    self.num_left_calls += 1
    
class RightSubclass(BaseClass):
    num_right_calls = 0
    
    def call_me(self):
        super().call_me()
        print("Calling method on the right subclass")
        self.num_right_calls += 1
        
class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0
    
    def call_me(self):
    super().call_me()
    print("Calling method on a subclass")
    self.num_sub_calls += 1
