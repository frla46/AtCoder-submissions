n, m = [int(i) for i in input().split()]
c = input().split()
d = input().split()
p = [int(i) for i in input().split()]
dp = [i for i in zip(d, p[1:])]
ret = 0
for i in c:
    for color, price in dp:
        if i == color:
            ret += price
            break
    else:
        ret += p[0]
print(ret)
