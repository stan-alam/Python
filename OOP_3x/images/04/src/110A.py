#109.B
try:
	raise ValueError("This arg")
except ValueError as e:
    print("the exception args were", e.args)
