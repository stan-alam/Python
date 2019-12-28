# 217.A

def format_time(message, *args):
    now = datetime.datetime.now()
    print(f"{now:%I:%M:%S}: {message}")

def one(timer):
    format_time("Called 1")

def two(timer):
    format_time("Called 2")

def three(timer):
    format_time("Called 3")

class Repeater:
    def __init__(self):
        self.count = 0

    def repeater(self, timer):
        format_time(f"repeat {self.count}")
        self.count += 1
        time.call_after (5, self.repeater)
