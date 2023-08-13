n, m = [int(i) for i in input().split()]
l = [[int(i) for i in input().split()] for _ in range(m)]
t = set(i[1] for i in l if i[0] == 1)
for i in l:
    if i[0] in t and i[1] == n:
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')
