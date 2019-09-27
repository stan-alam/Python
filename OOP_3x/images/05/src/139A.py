class TomFoolery:
    @property
    def tomfoolery(self):
        "this is a tomfoolery property"
        print("What in Tomfoolery is going on here!?")
        return self.tomfoolery
        
    @tomfoolery.setter
    def tomfoolery(self, value):
       print ("You are tomfooling yourself {}".format(value))
       self._tomfoolery = value
        
    @tomfoolery.deleter
    def tomfoolery(self):
       print("You killed tomfoolery")
       del self._tomfoolery
        
