n = int(input())
t = [int(i) for i in input().split()]
m = int(input())
li = [[int(i) for i in input().split()] for _ in range(m)]
for i in li:
    tmp = t.copy()
    tmp[i[0] - 1] = i[1]
    print(sum(tmp))
