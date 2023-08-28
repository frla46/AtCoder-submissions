n = int(input())
l = [input().split() for _ in range(n)]
min = float('inf')
p = 0
for n, i in enumerate(l):
    if min > int(i[1]):
        min = int(i[1])
        p = n
for i in l[p:]:
    print(i[0])
for i in l[:p]:
    print(i[0])
