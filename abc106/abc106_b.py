

n = int(input())
x = 0
for i in range(1, n + 1, 2):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 8:
        x += 1
print(x)
