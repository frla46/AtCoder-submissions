import math
n = int(input())
a = [int(i) for i in input().split()]
t = a[0]
for i in range(1, n):
    t = math.gcd(t , a[i])
print(t)
