#109.A
def funny_div3(divider):
    try:
        if divider == 42:
            print("42 is a special number in the multiverse(s)")
        return 100 / divider
    except ZeroDivisionError:
        return "C'mon don't enter 0!"
    except TypeError:
        return "Enter a number value"
    except ValueError:
        print("no, the multiverse(s) says NOT 42!")
        raise
