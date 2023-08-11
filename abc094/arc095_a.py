n = int(input())
x = [int(i) for i in input().split()]
sx = sorted(x)
c = (sx[n // 2] + sx[n // 2 - 1]) / 2
for i in x:
    if i < c:
        print(sx[n // 2])
    else:
        print(sx[n // 2 - 1])
