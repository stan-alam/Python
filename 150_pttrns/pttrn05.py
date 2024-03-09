num = 5

for i in range(num,0,-1):
    for j in range(num - 1, i - 1, -1):
        print(" ", end= "")
    for k in range(1, i + 1):
        print(" * ", end="")
    print()