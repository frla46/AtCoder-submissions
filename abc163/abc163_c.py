import collections
n = int(input())
a = [int(i) for i in input().split()]
c = collections.Counter(a)
cnt = [0] * n
for i in a:
    cnt[i - 1] += 1
for i in cnt:
    print(i)
