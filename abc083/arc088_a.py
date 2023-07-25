x, y = [int(i) for i in input().split()]
cnt = 0
i = x
while i <= y:
    i *= 2
    cnt += 1
print(cnt)
