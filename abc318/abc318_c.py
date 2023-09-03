n, d, p = [int(i) for i in input().split()]
f = [int(i) for i in input().split()]
f.sort(reverse=True)
ret = 0
for i in range(0, len(f), d):
    if sum(f[i:i + d]) > p:
        ret += p
    else:
        ret += sum(f[i:i + d])
print(ret)
