a, b, c, x, y = [int(i) for i in input().split()]
ca = cb = cc = 0
if (a + b) / 2 > c:
    cc += min(x, y) * 2
    if x - cc / 2 > 0 and a / 2 > c:
        cc += (x - cc // 2) * 2
    else:
        ca += (x - min(x, y))
    if y - cc / 2 > 0 and b / 2 > c:
        cc += (y - cc // 2) * 2
    else:
        cb += (y - min(x, y))
else:
    ca = x
    cb = y
print(a * ca + b * cb + c * cc)
