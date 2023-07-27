r, g, b, n = [int(i) for i in input().split()]
cnt = 0
for i in range(n // r + 1):
    for j in range(n // g + 1):
        t = n - (i * r + j * g)
        if t >= 0 and t % b == 0:
            cnt += 1
print(cnt)

