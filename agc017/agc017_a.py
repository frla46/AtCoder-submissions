n, p = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a = [i % 2 for i in a]
even, odd = a.count(0), a.count(1)
if p == 1 and odd == 0:
    cnt = 0
else:
    cnt = 2 ** even * 2 ** max(0, odd - 1)
print(cnt)
