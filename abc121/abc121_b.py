n, m, c = [int(i) for i in input().split()]
bl = [int(i) for i in input().split()]
l = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    if sum([l[i][j] * bl[j] for j in range(m)]) + c > 0:
        cnt += 1
print(cnt)
