import collections
n = int(input())
a = [int(i) for i in input().split()]
c = collections.Counter(a).most_common()
cnt = 0
for i, j in c:
    if i <= j:
        cnt += j - i
    else:
        cnt += j
print(cnt)
