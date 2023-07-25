import math
h, w = [int(i) for i in input().split()]
if h == 1 or w == 1:
    res = 1
else:
    res = math.ceil(h * w / 2)
print(res)
