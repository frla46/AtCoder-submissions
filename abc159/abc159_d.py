import collections
n = int(input())
a = [int(i) for i in input().split()]
c = collections.Counter(a)
t = sum([n * (n - 1) // 2 for n in c.values()])
for i in a:
    ret = t
    ret -= c[i] * (c[i] - 1) // 2
    ret += (c[i] - 1) * (c[i] - 2) // 2
    print(ret)

