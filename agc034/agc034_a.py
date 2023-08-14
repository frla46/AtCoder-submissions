n, a, b, c, d = [int(i) for i in input().split()]
s = input()
if s[a:max(c, d)].find('##') == -1:
    if c < d:
        ret = 'Yes'
    else:
        if '...' in s[b - 2:d + 1]:
            ret = 'Yes'
        else:
            ret = 'No'
else:
    ret = 'No'
print(ret)
