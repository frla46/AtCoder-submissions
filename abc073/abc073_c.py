

import collections
n = int(input())
a = [int(input()) for _ in range(n)]
c = collections.Counter(a)
print(sum([v % 2 != 0 for v in c.values()]))
