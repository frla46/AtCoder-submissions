n, t = [int(i) for i in input().split()]
time = [int(i) for i in input().split()]
ret = t
for i in range(1, n):
    ret += min(time[i] - time[i - 1], t)
print(ret)

