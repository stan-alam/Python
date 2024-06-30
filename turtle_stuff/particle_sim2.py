import turtle

class SimulationArea:
    def __init__(self, width, height, color="white"):
        # Create a window
        self.window = turtle.Screen()

    def update(self):
        self.window.update()

    def set_title(self, title):
        self.window.title(title)
        
    @staticmethod
    def run_mainloop():
        turtle.mainloop()