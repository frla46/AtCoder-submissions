n = int(input())
li = []
for _ in range(n):
    s, p = input().split()
    li.append([s, int(p)])
lis = sorted(li, key=lambda x: x[1], reverse=True)
lis = sorted(lis, key=lambda x: x[0])
for i in lis:
    print(li.index(i) + 1)
