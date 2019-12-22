#108.A
def funny_division2(divider):
    try:
        if divider == 42:
            raise ValueError("42 is a reserved number")
        return 100 / divider
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than 0"
