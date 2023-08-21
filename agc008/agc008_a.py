x, y = [int(i) for i in input().split()]
cnt = 0
if (x < 0 and abs(x) < abs(y)) or (x > 0 and abs(x) > abs(y)):
    x = -x
    cnt += 1
t = abs(abs(x) - abs(y))
x += t
cnt += t
if x != y:
    cnt += 1
print(cnt)
