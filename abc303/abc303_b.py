import itertools
n, m = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for _ in range(m)]
p = set(itertools.combinations(range(1, n + 1), 2))
cnt = 0
for i in a:
    for j in zip(i, i[1:]):
        if (j[0], j[1]) in p:
            p.remove((j[0], j[1]))
        elif (j[1], j[0]) in p:
            p.remove((j[1], j[0]))
        cnt += 1
print(len(p))
