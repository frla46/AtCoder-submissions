l, r = [int(i) for i in input().split()]
min_ = float('inf')
for i in range(l, min(l + 2019, r)):
    for j in range(l + 1, min(l + 2019, r) + 1):
        ret = i * j % 2019
        if min_ > ret:
            min_ = ret
print(min_)
