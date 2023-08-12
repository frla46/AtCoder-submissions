n = int(input())
li = [[int(i) for i in input().split()] for _ in range(n * 2)][1::2]
x = int(input())
ret = {}
for n, i in enumerate(li, 1):
    if x in i:
        ret[n] = len(i)
if len(ret) > 0:
    mi = min(ret.values())
    ret = [i[0] for i in ret.items() if i[1] == mi]
    print(len(ret))
    print(*ret)
else:
    print(0)
