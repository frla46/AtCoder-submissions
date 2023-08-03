
n, m = [int(i) for i in input().split()]
if n == 1 and m == 1:
    ret = 1
elif n == 1 or m == 1:
    ret = max(n, m) - 2
else:
    ret = (n - 2) * (m - 2)
print(ret)
