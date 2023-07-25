n = int(input())
a = [0] + [int(input()) for _ in range(n)]
cnt = 0
i = a[1]
s = set()
while True:
    cnt += 1
    if i == 2:
        print(cnt)
        exit()
    elif i in s:
        print(-1)
        exit()
    else:
        s.add(i)
        i = a[i]
