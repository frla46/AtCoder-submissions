

a = [[int(i) for i in input().split()] for _ in range(3)]
b = []
for i in a:
    b += [[j - min(i) for j in i]]
c = [i for i in zip(*b)]
ret = []
for i in c:
     ret += [[j - min(i) for j in i]]
if set(sum(ret, [])) == {0}:
    print('Yes')
else:
    print('No')
