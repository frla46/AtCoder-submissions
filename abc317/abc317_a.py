n, h, x = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
for n, i in enumerate(p, 1):
    if h + i >= x:
        print(n)
        exit()
