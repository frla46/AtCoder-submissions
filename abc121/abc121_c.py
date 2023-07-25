n, m = [int(i) for i in input().split()]
li = [[int(i) for i in input().split()] for _ in range(n)]
cnt = 0
p = 0
li.sort()
for i in li:
    if cnt + i[1] >= m:
        p += (m - cnt) * i[0]
        print(p)
        exit()
    else:
        p += i[1] * i[0]
        cnt += i[1]
