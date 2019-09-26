def call_me(self):
    LeftSubclass.call_me(self)
    RightSubclass.call_me(self)
    print("Calling method on subclass")
    self.num_sub_calls +=  1
