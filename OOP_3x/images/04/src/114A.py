def divide_with_exception(number, divisor):
    try:
	print(f"{number} / {divisor} = {number / divisor}")
    except ZeroDivisionError:
	print("You can't divide by 0")

def divide_with_if(number, divisor):
    if divisor == 0:
	print("You can't divide by 0, duh!")
    else:
        print(f"{number} / { divisor} = { number / divisor}") 
