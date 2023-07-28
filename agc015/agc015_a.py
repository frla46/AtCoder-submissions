n, a, b = [int(i) for i in input().split()]
c = max(0, (b - a) * (n - 2) + 1)
print(c)