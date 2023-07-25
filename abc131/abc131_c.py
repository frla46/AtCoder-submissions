import math
a, b, c, d = [int(i) for i in input().split()]
cnt = 0
def hoge(x, d):
    return x - x // d
def fuga(x, c, d):
    lcm = (c * d) // math.gcd(c, d)
    return hoge(x, c) + hoge(x, d) - hoge(x, lcm)
print(fuga(b, c, d) - fuga(a - 1, c, d))
