n = int(input())
p = [int(i) for i in input().split()]
l = [0] * n
for i in range(n):
    if p[i] == i + 1:
        l[i] = 1
cnt = 0
f = False
for i in range(n):
    if f:
        f = False
        continue
    else:
        if l[i] == 1:
            cnt += 1
            if i < n - 1:
                if l[i + 1] == 1:
                    f = True
print(cnt)
