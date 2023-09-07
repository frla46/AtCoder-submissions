a = [int(i) for i in input().split()][::-1]
ret = 0
for i in a:
    ret *= 2
    ret += i
print(ret)
