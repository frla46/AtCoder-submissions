

import collections
n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
c = collections.Counter(a).most_common()[::-1]
cnt = 0
for i in range(len(c) - k):
    cnt += c[i][1]
print(cnt)
