n = int(input())
p = [int(i) for i in input().split()] + [0]
q = p[0]
del p[0]
if q <= max(p):
    ret = max(p) - q + 1
else:
    ret = 0
print(ret)
