import math
n, k = [int(i) for i in input().split()]
p = 0
for i in range(1, n + 1):
    c = math.ceil(math.log2(k / i)) if k > i else 0
    p += 1 / (n * 2 ** c)
print(p)

