n = int(input())
li = [[int(i) for i in input().split()] for _ in range(n)]
li.sort(key = lambda x:x[1])
t = 0
for i in li:
    t += i[0]
    if t > i[1]:
        print('No')
        exit()
print('Yes')