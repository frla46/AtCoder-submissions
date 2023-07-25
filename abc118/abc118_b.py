n, m = [int(i) for i in input().split()]
li = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in li:
    del i[0]
for i in range(1, m + 1):
    if all([i in j for j in li]):
        cnt += 1
print(cnt)
