class Color:
    def __init__(self, rgb_val, name):
        self.rgb_val = rgb_val
        self.name = name
        
    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._bane = name
        
    def _get_name(self):
        return self._name
        
    name = property(_get_name, _set_name)
