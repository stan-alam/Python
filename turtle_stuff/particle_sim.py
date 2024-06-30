import turtle

class SimulationArea:
    def __init__(self, width, height, color="white"):
        self.width = width
        self.height = height
        self.left_edge = -width // 2
        self.right_edge = width // 2
        self.top_edge = height // 2
        self.bottom_edge = -height // 2
        self.window = turtle.Screen()
        self.window.setup(width, height)
        self.window.tracer(0)
        self.window.bgcolor(color)