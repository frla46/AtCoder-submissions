

n = int(input())
s = input()
t = [str(i) + str(j) + str(k) for i in range(10) for j in range(10) for k in range(10)]
cnt = 0
for i in t:
    p = -1
    for c in i:
        p = s.find(c, p + 1)
        if p == -1:
            break
    if not p == -1:
        cnt += 1
    print()
print(cnt)
