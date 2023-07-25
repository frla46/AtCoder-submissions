n = int(input())
h = [int(i) for i in input().split()]
i = 0
cnt = 0
max = 0
for i in range(n - 1):
    if h[i] >= h[i + 1]:
        cnt += 1
        if max < cnt:
            max = cnt
    else:
        cnt = 0
print(max)
