k = int(input())
t = list(range(1, 10))
i = 0
cnt = len(t)
while True:
    if cnt >= k:
        break
    for j in range(t[i] % 10):
        t.append(t[i] * 10 + j)
        cnt += 1
    else:
        i += 1
        continue
print(t[k - 1])
