import math
n, m = [int(i) for i in input().split()]
s = input()
t = input()
g = math.gcd(n, m)
if s[::n // g] == t[::m // g]:
    print(n * m // g)
else:
    print(-1)
