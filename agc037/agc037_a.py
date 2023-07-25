cnt = 0
i = t = ''
for c in input():
    t += c
    if t != i:
        cnt += 1
        i = t
        t = ''
print(cnt)
