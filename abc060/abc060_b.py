import math
a, b, c = [int(i) for i in input().split()]
print('YES' if c % math.gcd(a, b) == 0 else 'NO')

