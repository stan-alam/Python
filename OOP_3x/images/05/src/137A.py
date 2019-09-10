class TomFoolery:
    def _get_tomfoolery(self):
        print("You have engaged in tom foolery")
        return self._tomfoolery
        
    def _set_tomfoolery(self, value):
        print("Why are you making tom foolery {}".format(value))
        self._silly = value
    
    def _del_tomfoolery(self):
        print("bye, tom foolery")
        del self._tomfoolery
        
    tomfoolery = property(_get_tomfoolery, _set_tomfoolery, _del_tomfoolery, "this is a tomfoolery property")
