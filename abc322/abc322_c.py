n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
p = 0
for i in range(1, n + 1):
    if i <= a[p]:
        print(a[p] - i)
    else:
        p += 1
        print(a[p] - i)
