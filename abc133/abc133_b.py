import math
import itertools
n, d = [int(i) for i in input().split()]
x = [[int(i) for i in input().split()] for _ in range(n)]
cnt = 0
for i, j in itertools.combinations(range(n), 2):
    t = math.sqrt(sum([(x[i][k] - x[j][k]) ** 2 for k in range(d)]))
    if t.is_integer():
        cnt += 1
print(cnt)
