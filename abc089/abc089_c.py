import itertools
n = int(input())
s = [input()[0] for _ in range(n)]
t = []
for c in 'MARCH':
    cnt = s.count(c)
    if cnt > 0:
        t += [cnt]
ret = 0
if len(t) >= 3:
    for i in itertools.combinations(t, 3):
        prod = 1
        for j in i:
            prod *= j
        ret += prod
else:
    ret = 0
print(ret)
