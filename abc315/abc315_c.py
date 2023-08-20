n = int(input())
l = [[int(i) for i in input().split()] for _ in range(n)]
l = sorted(l, key=lambda x:x[1], reverse=True)
ret = 0
for i in range(1, n):
    if l[0][0] == l[i][0]:
        ret = max(ret, l[0][1] + l[i][1] // 2)
    else:
        ret = max(ret, l[0][1] + l[i][1])
print(ret)
