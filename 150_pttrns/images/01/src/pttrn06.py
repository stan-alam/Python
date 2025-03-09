n_height = 10

for i in range(1, n_height):
    for j in range(n_height - 1, i - 1, -1):
        print(" ", end = "")
    for k in range(1, i + 1):
        print(" * ", end="")
    print()