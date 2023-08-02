import itertools
n, k = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
p = [0] + list(itertools.accumulate(p))
m = max([a - b for a, b in zip(p[k:], p)])
print((m + k) / 2)

