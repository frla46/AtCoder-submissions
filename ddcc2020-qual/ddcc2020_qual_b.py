import itertools
n = int(input())
a = [int(i) for i in input().split()]
ca = tuple(itertools.accumulate(a))
sum = ca[-1]
min = float('inf')
for i in ca:
    diff = abs(sum - i * 2)
    if min > diff:
        min = diff
print(min)
