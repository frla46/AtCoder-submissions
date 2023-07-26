n = int(input())
s = input()
max = 0
for i in range(n):
    cnt = 0
    for j in set(s[:i]):
        if j in set(s[i:]):
            cnt += 1
    if max < cnt:
        max = cnt
print(max)

