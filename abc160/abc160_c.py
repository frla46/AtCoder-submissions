k, n = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
l = 0
for i in range(n):
    l = max(l, a[i] - a[i - 1] if i != 0 else a[i] + k - a[i - 1])
print(k - l)
