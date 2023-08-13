import collections
n = int(input())
s = [[c for c in input()] for _ in range(n)]
s = [str(sorted(i)) for i in s]
s = collections.Counter(s).most_common()
v, c = zip(*s)
ret = sum([i * (i - 1) // 2 for i in c])
print(ret)
