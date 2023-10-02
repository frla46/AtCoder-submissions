n, m = [int(i) for i in input().split()]
s = input()
t = input()
if t.startswith(s):
    if t.endswith(s):
        ret = 0
    else:
        ret = 1
else:
    if t.endswith(s):
        ret = 2
    else:
        ret = 3
print(ret)
