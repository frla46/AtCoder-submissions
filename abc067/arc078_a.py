import itertools
N = int(input())
A = [int(i) for i in input().split()]
a = list(itertools.accumulate(A))
mi = min([abs(a[-1] - a[i] * 2) for i in range(N - 1)])
print(mi)
