n, k, s = [int(i) for i in input().split()]
if s != 10 ** 9:
    ret = [s for _ in range(k)] + [s + 1 for _ in range(n - k)]
else:
    ret = [s for _ in range(k)] + [1 for _ in range(n - k)]
print(*ret)
