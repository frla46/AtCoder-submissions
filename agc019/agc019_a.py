q, h, s, d = [int(i) for i in input().split()]
n = int(input())
t = 0
s = min(s, h * 2, q * 4)
if s * 2 <= d:
    t = s * n
else:
    if n % 2 == 0:
        t = n // 2 * d
    else:
        t = n // 2 * d + s
print(t)
