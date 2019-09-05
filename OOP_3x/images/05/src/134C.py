class Color:
    def __init__(self, rgb_val, name):
        self.rgb_val = rgb_val
        self.name = name
        
c = Color("#ff0000", "bright red")
print(c.name)
c.name = "red"
print(c.name)
