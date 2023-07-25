n, a, b = [int(i) for i in input().split()]
if (b - a) % 2 == 0:
    ret = (b - a) // 2
else:
    ret = min(n - b, a - 1) + (b - a - 1) // 2 + 1
print(ret)
