import math
n = int(input())
t = [int(input()) for _ in range(n)]
ret = 1
l = t[0]
for i in t:
    l = l * i // math.gcd(l, i)
print(l)
