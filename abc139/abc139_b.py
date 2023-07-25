a, b = [int(i) for i in input().split()]
c = 0
while True:
    if (a - 1) * c + 1 >= b:
        print(c)
        exit()
    else:
        c += 1
