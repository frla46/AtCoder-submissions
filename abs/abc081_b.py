n = int(input())
l = [int(i) for i in input().split()]
c = 0
c_l = []
for i in l:
    c = 0
    while True:
        if i % 2 == 0:
            i /= 2
            c += 1
        else:
            break
    c_l.append(c)
print(min(c_l))
