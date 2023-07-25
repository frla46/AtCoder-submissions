n, d = [int(i) for i in input().split()]
s = [input() for _ in range(n)]
max = 0
cnt = 0
for i in range(d):
    for j in s:
        if j[i] == 'x':
            if max < cnt:
                max = cnt
            cnt = 0
            break
    else:
        cnt += 1
        if max < cnt:
            max = cnt
print(max)

