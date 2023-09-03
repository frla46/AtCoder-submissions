n, m, p = [int(i) for i in input().split()]
if n < m:
    print(0)
else:
    print((n - m) // p + 1)
