n = int(input())
s = [input() for _ in range(n)]
c = []
for i in s:
    l = {chr(c): 0 for c in range(ord('a'), ord('a') + 26)}
    for j in i:
        l[j] += 1
    c += [l]
l = {chr(c): 0 for c in range(ord('a'), ord('a') + 26)}
for i in l:
    mi = 10 ** 10
    for j in c:
        mi = min(mi, j[i])
    l[i] = mi
for k, v in l.items():
    print(k * v, end='')
