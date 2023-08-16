n = int(input())
l = [[int(i) for i in input().split()] for _ in range(n)][::-1]
cnt = 0
for a, b in l:
    if (a + cnt) % b != 0:
        cnt += b - (a + cnt) % b
print(cnt)
