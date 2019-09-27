class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name
        
    def _set_name(self, name):
        if not name:
            raise Exception("Invalid name")
    
    def _get_name(self):
        return self.name
    
    name = property(_get_name, _set_name)
