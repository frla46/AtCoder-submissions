n, x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
c = 0
a.sort()
for i in a:
    if sum(a) < x:
        c = len(a) - 1
        break
    if x > i:
        x -= i
        c += 1
    elif x == i:
        c += 1
        break
    else:
        break
print(c)
