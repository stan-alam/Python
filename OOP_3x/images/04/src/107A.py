#107.A
def funny_division(divider):
    try:
        return 100 / divider
    except ZeroDivisionError:
        return "Zero is nil"
