n = int(input())
l = [[int(i) for i in input().split()] for _ in range(n)]
ret = [[0] * 100] * 100
cnt = 0
for i in range(101):
    for j in range(101):
        for a, b, c, d in l:
            if a < i <= b and c < j <= d:
                cnt += 1
                break
print(cnt)
