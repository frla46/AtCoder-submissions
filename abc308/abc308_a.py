s = [int(i) for i in input().split()]
f = True
for i, j in zip(s, s[1:]):
    if not i <= j:
        f = False
if not 100 <= min(s) <= max(s) <= 675:
    f = False
for i in s:
    if i % 25 != 0:
        f = False
if f:
    print('Yes')
else:
    print('No')
